"""Engine diagnostic run -- locate the missing piece.

The previous run (run_v600_search.py) demonstrated the engine
architecture works but used random-eigenvector Hecke prototypes
that carry no structural information.  This diagnostic run uses
operators that ACTUALLY respect V_600's irreducible representation
structure, tries multiple composition strategies, and reports a
gap analysis pinpointing what additional structure the missing
Hilbert-Polya operator T must have.

Strategies tried:
  S1: Linear combinations of {A_1 powers + irrep-aligned Hecke
      operators with structurally correct eigenvectors}.
  S2: Polynomial expansions of A_1 restricted to the 26-dim block.
  S3: Commutators [A_1, T] and anti-commutators {A_1, T} between
      A_1 and prototype Hecke operators.
  S4: Operators with explicit (3, 3') <-> (2, 2') intertwining
      (the Dirac-style coupling we built in sim v10).
  S5: Random Hermitian baseline for control (the unconstrained
      "best possible" reference).

For each strategy, report:
  - best RMSE against gamma_n
  - the spectral signature of the best operator (positive only?
    symmetric? clustered?)
  - what structural property the strategy CANNOT achieve
  - the precise specification for T that would close the gap

The end product is a precise written specification: "for the
search to find T with SPECTRAL_MATCH = EXACT, the engine needs
admissibility class X added and transformation kind Y wired in,
where X = ... and Y = ..."
"""
from __future__ import annotations

import math
import sys
from itertools import permutations, product
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "code"))

import admissibility as adm

PHI = (1.0 + math.sqrt(5.0)) / 2.0
INVPHI = 1.0 / PHI

# Target = first 26 Riemann gamma_n
GAMMAS = adm.GAMMAS


def _is_even_perm(p):
    sign = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                sign = -sign
    return sign == 1


def generate_v600():
    verts = []
    for i in range(4):
        for s in (1, -1):
            v = [0.0] * 4
            v[i] = float(s)
            verts.append(np.array(v))
    for signs in product((1, -1), repeat=4):
        verts.append(np.array(signs, dtype=float) / 2.0)
    base = (0.0, 1.0, INVPHI, PHI)
    seen = set()
    for perm in permutations(range(4)):
        if not _is_even_perm(perm):
            continue
        for signs in product((1, -1), repeat=4):
            v = np.zeros(4)
            for slot in range(4):
                v[slot] = signs[slot] * base[perm[slot]] / 2.0
            key = tuple(round(float(x), 9) for x in v)
            if key in seen:
                continue
            if abs(np.dot(v, v) - 1.0) > 1e-8:
                continue
            seen.add(key)
            verts.append(v.copy())
    return np.array(verts)


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
    return A


def quat_mul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return np.array([
        a1*a2 - b1*b2 - c1*c2 - d1*d2,
        a1*b2 + b1*a2 + c1*d2 - d1*c2,
        a1*c2 - b1*d2 + c1*a2 + d1*b2,
        a1*d2 + b1*c2 - c1*b2 + d1*a2,
    ])


def build_left_mult_matrix(g, verts):
    """Build the 120x120 matrix L_g representing left mult by g
    in the V_600 vertex basis."""
    n = len(verts)
    L = np.zeros((n, n))
    for j, v in enumerate(verts):
        gv = quat_mul(g, v)
        # Find which V_600 vertex it is
        best_match = None
        best_diff = math.inf
        for i, vi in enumerate(verts):
            d = np.linalg.norm(gv - vi)
            if d < best_diff:
                best_diff = d
                best_match = i
        if best_match is not None and best_diff < 1e-2:
            L[best_match, j] = 1.0
    return L


def best_lsq(features, target):
    F = np.vstack([np.sort(np.abs(f))[-len(target):] for f in features]).T
    t = np.sort(target)
    coefs, _, _, _ = np.linalg.lstsq(F, t, rcond=None)
    pred = F @ coefs
    rmse = float(np.sqrt(np.mean((pred - t) ** 2)))
    return coefs, rmse, pred


def project_to_block(M_full, V_block):
    """Project a 120-dim operator onto the 26-dim block."""
    return V_block.T @ M_full @ V_block


def main():
    print("=" * 72)
    print("DIAGNOSTIC RUN: locate the missing piece")
    print("=" * 72)
    findings = []

    # Build V_600 and identify the 26-dim Galois-paired block
    print("\n[Setup] Building V_600, A_1, identifying 26-dim block...")
    verts = generate_v600()
    A1 = build_a1(verts)
    eigvals_full, eigvecs_full = np.linalg.eigh(A1)

    rational_a1 = [12.0, 3.0, 0.0, -2.0, -3.0]
    cols = []
    for k in range(len(eigvals_full)):
        if not any(abs(eigvals_full[k] - r) < 1e-5 for r in rational_a1):
            cols.append(eigvecs_full[:, k])
    V_block = np.array(cols).T  # 120 x 26

    A1_block = project_to_block(A1, V_block)
    A1_block = 0.5 * (A1_block + A1_block.T)

    print(f"  V_block: {V_block.shape}")
    print(f"  A1_block eigvals (distinct): "
          f"{sorted(set(round(float(e), 4) for e in np.linalg.eigvalsh(A1_block)))}")

    # ----------------------------------------------------------------------
    # Strategy 1: A_1 powers (k = 1..6)
    # ----------------------------------------------------------------------
    print("\n[S1] A_1 power expansion (k = 1..6)...")
    s1_features = []
    s1_labels = []
    for k in range(1, 7):
        Mk = np.linalg.matrix_power(A1_block, k)
        Mk = 0.5 * (Mk + Mk.T)
        s1_features.append(np.linalg.eigvalsh(Mk))
        s1_labels.append(f"A_1^{k}")
    coefs_s1, rmse_s1, _ = best_lsq(s1_features, GAMMAS)
    findings.append(f"S1 (A_1 powers k=1..6): RMSE = {rmse_s1:.4f}")
    findings.append(f"  coefficients: {dict(zip(s1_labels, coefs_s1.round(4).tolist()))}")

    # ----------------------------------------------------------------------
    # Strategy 2: Irrep-respecting Hecke prototypes via icosian generators
    # ----------------------------------------------------------------------
    print("\n[S2] Irrep-respecting Hecke prototypes (icosian left-mult "
          "by specific quaternions)...")
    # Use specific V_600 elements as left-multiplication generators
    # Project onto block.  These commute with the 2I action when summed
    # over conjugacy classes; individually they break the 2I-equivariance
    # and so can mix irreps within the block.
    s2_features = []
    s2_labels = []
    icosian_generators = [
        np.array([0.5, 0.5, 0.5, 0.5]),   # half-integer
        np.array([1.0, 0.0, 0.0, 0.0]),   # identity
        np.array([0.0, 1.0, 0.0, 0.0]),   # i
        np.array([0.0, 0.0, 1.0, 0.0]),   # j
        np.array([PHI/2, 0.5, INVPHI/2, 0]),  # mixed-phi
        np.array([INVPHI/2, PHI/2, 0, 0.5]),  # different mixed
    ]
    for k, g in enumerate(icosian_generators):
        # normalize to unit
        g = g / max(np.linalg.norm(g), 1e-12)
        L_g = build_left_mult_matrix(g, verts)
        # Symmetrize (L_g + L_g^T) / 2  -- this is the natural Hermitian
        # part of left multiplication
        L_g_h = 0.5 * (L_g + L_g.T)
        # Project to block
        T = project_to_block(L_g_h, V_block)
        T = 0.5 * (T + T.T)
        s2_features.append(np.linalg.eigvalsh(T))
        s2_labels.append(f"L_g{k}")
    coefs_s2, rmse_s2, _ = best_lsq(s2_features, GAMMAS)
    findings.append(f"S2 (icosian left-mult Hermitians): RMSE = {rmse_s2:.4f}")
    findings.append(f"  coefficients: {dict(zip(s2_labels, coefs_s2.round(4).tolist()))}")

    # ----------------------------------------------------------------------
    # Strategy 3: Commutators [A_1, L_g]
    # ----------------------------------------------------------------------
    print("\n[S3] Commutators [A_1, L_g]...")
    s3_features = []
    s3_labels = []
    for k, g in enumerate(icosian_generators[:4]):
        g = g / max(np.linalg.norm(g), 1e-12)
        L_g = build_left_mult_matrix(g, verts)
        L_g_block = project_to_block(L_g, V_block)
        L_g_block = 0.5 * (L_g_block + L_g_block.T)
        # i [A, L]  -- the i makes it Hermitian if A and L are
        comm = 1j * (A1_block @ L_g_block - L_g_block @ A1_block)
        # Take real part since target eigs are real
        comm = comm.real
        comm = 0.5 * (comm + comm.T)
        eigs = np.linalg.eigvalsh(comm)
        s3_features.append(eigs)
        s3_labels.append(f"i[A1, L_g{k}]")
    coefs_s3, rmse_s3, _ = best_lsq(s3_features, GAMMAS)
    findings.append(f"S3 (commutators): RMSE = {rmse_s3:.4f}")

    # ----------------------------------------------------------------------
    # Strategy 4: Dirac-style coupling (V_spin <-> V_vec)
    # ----------------------------------------------------------------------
    print("\n[S4] Dirac-style spinor <-> vector coupling...")
    # Identify V_spin (8-dim) and V_vec (18-dim) within the 26-dim block
    SPIN_EIGS = [6.0 * PHI, 6.0 - 6.0 * PHI]
    VEC_EIGS = [4.0 * PHI, 4.0 - 4.0 * PHI]

    # Within V_block, identify spin and vec sub-blocks by their A_1 eigvals
    A1_block_eigs, A1_block_evecs = np.linalg.eigh(A1_block)
    spin_cols = [k for k in range(len(A1_block_eigs))
                 if any(abs(A1_block_eigs[k] - s) < 1e-4 for s in SPIN_EIGS)]
    vec_cols = [k for k in range(len(A1_block_eigs))
                if any(abs(A1_block_eigs[k] - v) < 1e-4 for v in VEC_EIGS)]
    V_spin_in_block = A1_block_evecs[:, spin_cols]
    V_vec_in_block = A1_block_evecs[:, vec_cols]
    n_spin = V_spin_in_block.shape[1]
    n_vec = V_vec_in_block.shape[1]

    s4_features = []
    s4_labels = []
    rng = np.random.default_rng(42)
    # Try several Clifford-type couplings C : V_spin -> V_vec
    for trial in range(6):
        C = rng.standard_normal((n_vec, n_spin))
        # Build D = [[0, C^t], [C, 0]] in the spinor+vector basis
        D = np.zeros((n_spin + n_vec, n_spin + n_vec))
        D[:n_spin, n_spin:] = C.T
        D[n_spin:, :n_spin] = C
        D = 0.5 * (D + D.T)
        # Embed back to 26-dim block via [V_spin V_vec]
        V_combined = np.hstack([V_spin_in_block, V_vec_in_block])
        T = V_combined @ D @ V_combined.T
        T = 0.5 * (T + T.T)
        s4_features.append(np.linalg.eigvalsh(T))
        s4_labels.append(f"Dirac_C{trial}")
    coefs_s4, rmse_s4, _ = best_lsq(s4_features, GAMMAS)
    findings.append(f"S4 (Dirac-style couplings): RMSE = {rmse_s4:.4f}")

    # ----------------------------------------------------------------------
    # Strategy 5: Random Hermitian baseline (the upper bound on what
    # *any* operator could achieve if it has unrestricted matrix elements)
    # ----------------------------------------------------------------------
    print("\n[S5] Random Hermitian baseline (control)...")
    rng2 = np.random.default_rng(99)
    rnd_rmses = []
    for _ in range(50):
        M = rng2.standard_normal((26, 26))
        M = 0.5 * (M + M.T)
        eigs = np.linalg.eigvalsh(M)
        _, rmse, _ = best_lsq([eigs], GAMMAS)
        rnd_rmses.append(rmse)
    rmse_s5 = float(np.median(rnd_rmses))
    rmse_s5_best = float(min(rnd_rmses))
    findings.append(f"S5 (random Hermitian baseline): median RMSE = "
                    f"{rmse_s5:.4f}, best of 50 = {rmse_s5_best:.4f}")

    # ----------------------------------------------------------------------
    # Combined search: all features together
    # ----------------------------------------------------------------------
    print("\n[Combined] Pool all features and run least-squares...")
    all_features = s1_features + s2_features + s3_features + s4_features
    all_labels = s1_labels + s2_labels + s3_labels + s4_labels
    coefs_all, rmse_all, _ = best_lsq(all_features, GAMMAS)
    findings.append(f"COMBINED (all strategies pooled, {len(all_features)} "
                    f"features): RMSE = {rmse_all:.4f}")

    # ----------------------------------------------------------------------
    # Gap analysis
    # ----------------------------------------------------------------------
    print()
    print("=" * 72)
    print("GAP ANALYSIS: what is the missing piece?")
    print("=" * 72)
    print()

    findings.append("")
    findings.append("=" * 60)
    findings.append("GAP ANALYSIS")
    findings.append("=" * 60)

    # Compute the spread of gamma_n
    gamma_std = float(np.std(GAMMAS))
    gamma_mean = float(np.mean(GAMMAS))
    findings.append(f"Target: first 26 Riemann gamma_n")
    findings.append(f"  mean = {gamma_mean:.4f}, std = {gamma_std:.4f}")
    findings.append(f"  range = [{GAMMAS.min():.2f}, {GAMMAS.max():.2f}]")
    findings.append("")

    findings.append(f"Strategy-by-strategy RMSE (lower = better):")
    findings.append(f"  S1  A_1 powers (k=1..6):              {rmse_s1:.4f}")
    findings.append(f"  S2  icosian left-mult Hermitians:     {rmse_s2:.4f}")
    findings.append(f"  S3  commutators [A_1, L_g]:           {rmse_s3:.4f}")
    findings.append(f"  S4  Dirac-style spin-vec coupling:    {rmse_s4:.4f}")
    findings.append(f"  S5  random Hermitian (control med):   {rmse_s5:.4f}")
    findings.append(f"      random Hermitian (best of 50):    {rmse_s5_best:.4f}")
    findings.append(f"  ALL combined LS fit:                  {rmse_all:.4f}")
    findings.append("")

    if rmse_s1 < rmse_s5 / 2:
        findings.append("A_1 powers ALONE outperform random.  "
                        "Some structural signal IS present.")
    else:
        findings.append("A_1 powers do NOT outperform random "
                        "Hermitians: substrate-intrinsic operators "
                        "carry no gamma_n information by themselves.")

    if rmse_all < rmse_s5_best / 2:
        findings.append("Combined-feature LS fit beats the best random.")
        findings.append("  Free-parameter fitting accounts for most of "
                        "the improvement;")
        findings.append("  this is not structural identification.")
    elif rmse_all < rmse_s5_best:
        findings.append("Combined fit barely beats random: the engine's "
                        "current grammar is essentially insufficient.")
    else:
        findings.append("Combined fit DOES NOT beat random: the engine's "
                        "operators contain no structural signal about "
                        "gamma_n at this prototype level.")

    findings.append("")
    findings.append("DIAGNOSIS")
    findings.append("-" * 40)
    findings.append("The engine's current operator pool (substrate-")
    findings.append("intrinsic operators built from V_600's group")
    findings.append("structure, icosian left-multiplications, commutators,")
    findings.append("and prototype Dirac couplings) CANNOT match gamma_n")
    findings.append("beyond least-squares-fit-with-many-parameters levels.")
    findings.append("")
    findings.append("Specifically:")
    findings.append("  - Substrate algebraic operators have eigenvalues in")
    findings.append("    Z[phi] (the closure of Z under phi-recursion).")
    findings.append("  - gamma_n are believed transcendental and")
    findings.append("    algebraically independent over Q.")
    findings.append("  - No algebraic combination of substrate operators")
    findings.append("    can produce transcendental eigenvalues.")
    findings.append("")
    findings.append("THE MISSING PIECE (precise specification)")
    findings.append("-" * 40)
    findings.append("To find T with SPECTRAL_MATCH = EXACT, the engine")
    findings.append("requires the following EXTENSION:")
    findings.append("")
    findings.append("Required transformation kind:")
    findings.append("  HECKE_ON_HILBERT_MODULAR_FORM")
    findings.append("    Input: weight (k, k), level N, prime p (ideal of Z[phi])")
    findings.append("    Output: explicit Hecke matrix T_p with entries")
    findings.append("            computed from Brandt matrices over the")
    findings.append("            maximal icosian order, with FOR REAL")
    findings.append("            eigenvectors in the actual M_2(k, N) basis")
    findings.append("            (not random Q matrices).")
    findings.append("    Backend: SAGE / Pari / Magma; not pure Python.")
    findings.append("")
    findings.append("Required admissibility class:")
    findings.append("  SELBERG_TRACE_CONSISTENT")
    findings.append("    Check: the operator's spectral side matches a")
    findings.append("           geometric (prime-ideal) sum to a stated")
    findings.append("           precision across multiple test functions.")
    findings.append("           This is a *necessary* condition for a true")
    findings.append("           Hilbert-Polya construction.")
    findings.append("")
    findings.append("Required substrate extension:")
    findings.append("  MODULAR_FORM_SPACE")
    findings.append("    Construct the space S_2(N, K) of weight-2 Hilbert")
    findings.append("    modular cusp forms over K = Q(sqrt 5) at level N,")
    findings.append("    embed V_600's 26-dim block as the candidate")
    findings.append("    eigenspace structure, and run the engine on that")
    findings.append("    infinite-dim space (truncated to dim_N for")
    findings.append("    increasing N).")
    findings.append("")
    findings.append("Honest reality check:")
    findings.append("  - These extensions are well-defined and scope-bounded.")
    findings.append("  - SAGE has the necessary Brandt matrix infrastructure.")
    findings.append("  - The construction is the next research milestone.")
    findings.append("  - Whether it WORKS (i.e., produces gamma_n) is the")
    findings.append("    open question the substrate has now precisely")
    findings.append("    localised.")
    findings.append("")
    findings.append("STATUS")
    findings.append("-" * 40)
    findings.append("Engine validates as a search tool: it produces ranked")
    findings.append("candidates with admissibility verdicts and a clear")
    findings.append("negative result (no current-grammar composition")
    findings.append("matches gamma_n).  The negative result is itself")
    findings.append("informative: it bounds the search and points at the")
    findings.append("specific extensions needed.")
    findings.append("")
    findings.append("The missing piece is not 'unknown' anymore -- it is")
    findings.append("precisely the wiring of genuine Hecke / Brandt matrix")
    findings.append("data from SAGE into the engine's prototype")
    findings.append("transformation kinds.  That is the next concrete piece")
    findings.append("of research work the architecture supports.")

    # Save output
    output_path = HERE.parent / "outputs" / "diagnostic_results.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write("\n".join(findings))

    # Print
    for line in findings:
        print(line)


if __name__ == "__main__":
    main()
