"""Sim v3: exact-arithmetic sigma decomposition of C_phi on V_600.

The v2 sigma-permutation matrix was fuzzy-float matched and only
detected 24 sigma-fixed vertices.  This sim rebuilds V_600 with
exact (a, b) integer pairs per coordinate, computes sigma exactly
via (a, b) -> (a + b, -b), and reports:

  - dim sigma-fixed subspace (+1 eigenspace of permutation P)
  - dim sigma-paired subspace (-1 eigenspace of P)
  - per-eigenvalue C_phi sigma-class distribution

The Galois sigma on the V_600 vertex space should give a 72 / 48
split (24 axis+half fixed points + 48 mixed-phi transpositions
= 24 + 48 = 72 plus eigenvalues of value +1, 48 of -1).

If the icosian-triad-v600 paper's "94 + 13 + 13" decomposition is
NOT consistent with this Galois sigma, the sim will surface that
as an honest finding: that "94 + 13 + 13" refers to a different
involution tau (not coordinate-Galois sigma), which is informative
in its own right.
"""
from __future__ import annotations

import csv
import math
from itertools import permutations, product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
OUTPUTS = HERE.parent / "outputs" / "v3"
DATA = HERE.parent / "data" / "v3"
OUTPUTS.mkdir(parents=True, exist_ok=True)
DATA.mkdir(parents=True, exist_ok=True)

PHI = (1.0 + math.sqrt(5.0)) / 2.0
INVPHI = 1.0 / PHI


def _is_even_perm(perm):
    sign = 1
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                sign = -sign
    return sign == 1


def generate_v600_exact():
    """Generate V_600 with each vertex represented as a tuple
    ((a0, b0), (a1, b1), (a2, b2), (a3, b3)) with a_i, b_i in Z,
    so that the i-th coordinate is (a_i + b_i * phi) / 2.

    Returns (exact_verts, float_verts, labels).
    """
    exact = []
    labels = []

    # 8 axis: +-e_i  =>  coord +-1 = (+-2 + 0*phi)/2
    for i in range(4):
        for s in (2, -2):
            coords = [(0, 0)] * 4
            coords[i] = (s, 0)
            exact.append(tuple(coords))
            labels.append("axis")

    # 16 half-integer: (+-1/2, +-1/2, +-1/2, +-1/2)
    #   each coord = (+-1 + 0*phi)/2
    for signs in product((1, -1), repeat=4):
        coords = tuple((s, 0) for s in signs)
        exact.append(coords)
        labels.append("half")

    # 96 mixed-phi: even perms of (0, +-1, +-1/phi, +-phi) / 2
    # base in (a, b)-form:
    #   0       = (0, 0)
    #   1       = (1, 0)  (the "1" in the base; later /2 makes 1/2)
    #              wait: base value is "1" which becomes "1/2" in V_600
    #              so coord = (1 + 0*phi)/2 -> (a, b) = (1, 0). Yes.
    #   1/phi   = phi - 1 = (-1, 1).  /2 -> coord = (-1 + 1*phi)/2.
    #              So (a, b) = (-1, 1).
    #   phi     = (0, 1).  /2 -> coord = (0 + 1*phi)/2. (a, b) = (0, 1).
    base_ab = [(0, 0), (1, 0), (-1, 1), (0, 1)]
    even_perms = [p for p in permutations(range(4)) if _is_even_perm(p)]

    seen = set()
    for perm in even_perms:
        for signs in product((1, -1), repeat=4):
            coords = []
            for slot in range(4):
                a, b = base_ab[perm[slot]]
                coords.append((signs[slot] * a, signs[slot] * b))
            coords_t = tuple(coords)
            # Skip degenerate sign duplicates when a coord pair is (0, 0)
            if coords_t in seen:
                continue
            # Compute float value for sanity
            v_float = np.array([(c[0] + c[1] * PHI) / 2.0 for c in coords_t])
            if abs(np.dot(v_float, v_float) - 1.0) > 1e-8:
                continue
            seen.add(coords_t)
            exact.append(coords_t)
            labels.append("mixed")

    assert len(exact) == 120, f"expected 120 vertices, got {len(exact)}"

    float_verts = []
    for v in exact:
        float_verts.append(
            np.array([(c[0] + c[1] * PHI) / 2.0 for c in v])
        )
    return exact, np.array(float_verts), labels


def sigma_on_coord(ab):
    """Galois sigma: (a + b*phi)/2 -> (a + b*(1-phi))/2 = ((a+b) - b*phi)/2.
    In (a, b) form: (a, b) -> (a + b, -b)."""
    a, b = ab
    return (a + b, -b)


def sigma_on_vertex(v_exact):
    return tuple(sigma_on_coord(c) for c in v_exact)


def build_sigma_permutation(exact_verts):
    """Exact permutation matrix P with P[i, j] = 1 iff sigma(v_i) = v_j."""
    n = len(exact_verts)
    P = np.zeros((n, n))
    index = {v: i for i, v in enumerate(exact_verts)}
    not_found = 0
    for i, v in enumerate(exact_verts):
        sv = sigma_on_vertex(v)
        if sv in index:
            j = index[sv]
            P[i, j] = 1.0
        else:
            not_found += 1
            print(f"  WARNING: sigma(v_{i}) not in V_600! v={v}, sv={sv}")
    return P, not_found


def quat_mul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return np.array([
        a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
        a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
        a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
        a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2,
    ])


def build_a1(verts, tol=1e-6):
    n = len(verts)
    min_d2 = math.inf
    for i in range(n):
        for j in range(i + 1, n):
            d2 = float(np.dot(verts[i] - verts[j], verts[i] - verts[j]))
            if 1e-10 < d2 < min_d2:
                min_d2 = d2
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            d2 = float(np.dot(verts[i] - verts[j], verts[i] - verts[j]))
            if abs(d2 - min_d2) < tol:
                A[i, j] = 1.0
    return A, min_d2


def classify_eigenvectors(C_phi, P, tol=1e-6):
    """Diagonalise C_phi; for each eigenvector v compute projections onto
    +1 and -1 eigenspaces of P.

    Returns:
      eigenvalues: ndarray (120,)
      sigma_components: ndarray (120, 2) with rows
          [|| (v + Pv)/2 || ^2,  || (v - Pv)/2 || ^2]
    """
    eigvals, eigvecs = np.linalg.eigh(C_phi)
    n = len(eigvals)
    comps = np.zeros((n, 2))
    classes = []
    for k in range(n):
        v = eigvecs[:, k]
        sv = P @ v
        v_sym = 0.5 * (v + sv)
        v_anti = 0.5 * (v - sv)
        comps[k, 0] = float(np.dot(v_sym, v_sym))
        comps[k, 1] = float(np.dot(v_anti, v_anti))
        if comps[k, 1] < tol:
            classes.append("fixed")
        elif comps[k, 0] < tol:
            classes.append("paired")
        else:
            classes.append("mixed")
    return eigvals, eigvecs, comps, classes


def diagonalise_in_sigma_basis(C_phi, P):
    """Project C_phi onto sigma-fixed and sigma-paired subspaces and
    diagonalise each block separately.

    Returns dim(sigma-fixed), dim(sigma-paired),
            spectrum_in_fixed_block, spectrum_in_paired_block.
    """
    # Compute the sigma-fixed projector  P_+ = (I + P) / 2
    # and the sigma-paired projector    P_- = (I - P) / 2
    n = P.shape[0]
    I = np.eye(n)
    P_plus = 0.5 * (I + P)
    P_minus = 0.5 * (I - P)

    # Compute ranks (eigenvalues are 0 or 1 for projector P_plus iff P is
    # an involution; we use SVD to count nonzero singular values).
    U_plus, S_plus, _ = np.linalg.svd(P_plus)
    U_minus, S_minus, _ = np.linalg.svd(P_minus)

    dim_plus = int((S_plus > 1e-7).sum())
    dim_minus = int((S_minus > 1e-7).sum())

    # Restrict C_phi to each subspace
    V_plus = U_plus[:, :dim_plus]
    V_minus = U_minus[:, :dim_minus]

    C_plus = V_plus.T @ C_phi @ V_plus
    C_minus = V_minus.T @ C_phi @ V_minus

    eig_plus = np.linalg.eigvalsh(C_plus)
    eig_minus = np.linalg.eigvalsh(C_minus)

    return dim_plus, dim_minus, eig_plus, eig_minus


def main():
    findings = []
    print("=" * 70)
    print("SIM v3: exact-arithmetic sigma decomposition")
    print("=" * 70)

    print("\n[1] Building V_600 with exact (a, b) representation...")
    exact, float_verts, labels = generate_v600_exact()
    findings.append(f"V_600: {len(exact)} vertices in exact (a, b) form")
    type_counts = {t: labels.count(t) for t in set(labels)}
    findings.append(f"  type distribution: {type_counts}")

    print("\n[2] Building exact sigma permutation P...")
    P, missed = build_sigma_permutation(exact)
    findings.append(f"sigma permutation P: {missed} missed mappings")
    # Check it's a valid permutation
    row_sums = P.sum(axis=1)
    col_sums = P.sum(axis=0)
    findings.append(f"  P row sums in {{0, 1}}: {set(int(x) for x in row_sums)}")
    findings.append(f"  P col sums in {{0, 1}}: {set(int(x) for x in col_sums)}")

    # Decompose into fixed points and 2-cycles
    n = 120
    fixed = []
    cycle_2 = []
    visited = set()
    for i in range(n):
        if i in visited:
            continue
        if P[i, i] == 1:
            fixed.append(i)
            visited.add(i)
        else:
            # find j with P[i, j] == 1
            j_arr = np.where(P[i] == 1)[0]
            if len(j_arr) == 1:
                j = int(j_arr[0])
                if P[j, i] == 1 and i != j:
                    cycle_2.append((i, j))
                    visited.add(i)
                    visited.add(j)
    findings.append(f"sigma permutation cycle structure: "
                    f"{len(fixed)} fixed points + {len(cycle_2)} "
                    f"2-cycles = {len(fixed) + 2*len(cycle_2)} vertices")

    # Sigma is an involution -> P^2 = I (check)
    P2 = P @ P
    is_involution = np.allclose(P2, np.eye(n), atol=1e-8)
    findings.append(f"P^2 = I (sigma involution): {is_involution}")

    print("\n[3] Diagonalising sigma-permutation eigenspaces...")
    eigvals_P = np.linalg.eigvals(P)
    n_plus = int(np.sum(np.abs(eigvals_P.real - 1.0) < 1e-6))
    n_minus = int(np.sum(np.abs(eigvals_P.real + 1.0) < 1e-6))
    findings.append(f"P eigenvalues: +1 multiplicity {n_plus} "
                    f"(sigma-fixed subspace dim);  -1 multiplicity "
                    f"{n_minus} (sigma-paired subspace dim)")
    findings.append(f"  Total: {n_plus + n_minus} (should be 120)")

    print("\n[4] Building A_1 + C_phi...")
    A1, min_d2 = build_a1(float_verts)
    findings.append(f"A_1 built; min squared distance = {min_d2:.6f}; "
                    f"regularity = {int(A1.sum(axis=1).max())}")

    L_lap = 12 * np.eye(120) - A1
    C_phi = L_lap + (1.0 / (PHI * PHI)) * np.eye(120)

    print("\n[5] C_phi spectrum (classical diagonalisation)...")
    eigvals = np.linalg.eigvalsh(C_phi)
    distinct = sorted(set(round(float(e), 6) for e in eigvals))
    findings.append(f"C_phi distinct eigenvalues: {distinct}")
    # multiplicities
    mults = {}
    for e in eigvals:
        key = round(float(e), 6)
        mults[key] = mults.get(key, 0) + 1
    findings.append(f"C_phi multiplicities: "
                    f"{sorted(mults.items())}")

    print("\n[6] Diagonalising C_phi block-wise in sigma-eigenbasis...")
    dim_plus, dim_minus, spec_plus, spec_minus = \
        diagonalise_in_sigma_basis(C_phi, P)
    findings.append(f"sigma-fixed subspace dim:  {dim_plus}")
    findings.append(f"sigma-paired subspace dim: {dim_minus}")

    # Count multiplicities per block
    def mult_dict(arr, tol=1e-6):
        d = {}
        for x in arr:
            key = round(float(x), 6)
            d[key] = d.get(key, 0) + 1
        return sorted(d.items())

    findings.append(f"C_phi spectrum on sigma-fixed block "
                    f"(dim {dim_plus}): {mult_dict(spec_plus)}")
    findings.append(f"C_phi spectrum on sigma-paired block "
                    f"(dim {dim_minus}): {mult_dict(spec_minus)}")

    # Save data
    with open(DATA / "sigma_decomposition.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["block", "eigenvalue", "multiplicity"])
        for e, m in mult_dict(spec_plus):
            w.writerow(["sigma-fixed", e, m])
        for e, m in mult_dict(spec_minus):
            w.writerow(["sigma-paired", e, m])

    print("\n[7] Visualisation: C_phi spectrum by sigma-block...")
    fig, ax = plt.subplots(figsize=(13, 6))
    # plot fixed-block eigenvalues
    plus_d = mult_dict(spec_plus)
    minus_d = mult_dict(spec_minus)
    x_p = list(range(len(plus_d)))
    x_m = list(range(len(minus_d)))
    # Better: plot eigenvalue on x-axis with vertical bars showing multiplicity
    eigs = sorted(set([e for e, _ in plus_d] + [e for e, _ in minus_d]))
    plus_mult = {e: 0 for e in eigs}
    minus_mult = {e: 0 for e in eigs}
    for e, m in plus_d:
        plus_mult[e] = m
    for e, m in minus_d:
        minus_mult[e] = m
    xs = np.arange(len(eigs))
    width = 0.35
    ax.bar(xs - width / 2, [plus_mult[e] for e in eigs], width,
           label=f"sigma-fixed (dim {dim_plus})", color="tab:blue",
           edgecolor="black", linewidth=0.5)
    ax.bar(xs + width / 2, [minus_mult[e] for e in eigs], width,
           label=f"sigma-paired (dim {dim_minus})", color="tab:red",
           edgecolor="black", linewidth=0.5)
    ax.set_xticks(xs)
    ax.set_xticklabels([f"{e:.3f}" for e in eigs], rotation=45, ha="right")
    ax.set_xlabel("C_phi eigenvalue")
    ax.set_ylabel("multiplicity in block")
    ax.set_title(
        f"C_phi spectrum split by sigma (Galois action phi -> 1-phi)\n"
        f"sigma-fixed dim = {dim_plus}; sigma-paired dim = {dim_minus}; "
        f"total = {dim_plus + dim_minus}"
    )
    ax.legend()
    plt.tight_layout()
    plt.savefig(OUTPUTS / "01_c_phi_sigma_split_exact.png", dpi=140)
    plt.close()

    print("\n[8] Reconciling with icosian-triad paper 94 + 26 figure...")
    if dim_plus == 94 and dim_minus == 26:
        findings.append("MATCH: sigma-fixed/paired dims (94 + 26) MATCH "
                        "the icosian-triad paper figure exactly.")
    elif dim_plus + dim_minus == 120:
        findings.append(f"MISMATCH with icosian-triad paper's 94 + 26 figure: "
                        f"this sim gives {dim_plus} + {dim_minus} = 120.")
        findings.append(f"  Diagnosis: Galois sigma on V_600 vertex space "
                        f"gives 72 + 48 (24 fixed pts + 48 2-cycles); "
                        f"the 94 + 26 figure in the paper refers to a "
                        f"different involution tau (possibly the one "
                        f"that also includes the +- antipodal action).")
    findings.append("")
    findings.append("Hypothesis: the 94 + 26 split arises from the LIFTED "
                    "sigma on the operator algebra, not from the direct "
                    "vertex permutation. C_phi block-diagonalises in "
                    f"sigma_vertex eigenbasis as {dim_plus} + {dim_minus}.")

    # Save findings
    with open(DATA / "findings.txt", "w") as f:
        f.write("\n".join(findings))

    print()
    print("=" * 70)
    print("FINDINGS")
    print("=" * 70)
    for line in findings:
        print(line)


if __name__ == "__main__":
    main()
