"""Sim v10: Dirac-style spin-coupled operator on V_600's 26-dim block.

Sim v9 tested generic operators on the 26-dim Galois-paired block but
did NOT explicitly use the spin structure (the (2,2') subblock is a
true spin irrep pair from the central extension Z/2 -> 2I -> A_5).

A Dirac operator is canonically constructed by coupling SPINORS to
VECTORS via Clifford multiplication. In our setting:
  - (2, 2') = 8-dim spinor sub-block of the 26-dim Galois-paired block
  - (3, 3') = 18-dim vector sub-block
  - Dirac operator D = gamma^i d_i where gamma^i are Clifford
    generators acting on spinors and d_i are vector-side derivatives.

For V_600, the "derivative" analog is the A_1 graph-Laplacian-like
operator restricted to the (3, 3') sub-block. The "Clifford
generators" gamma^i act on the (2, 2') sub-block. The Dirac operator
D ties them together by coupling each gamma^i to a copy of A_1's
action on (3, 3').

We construct an explicit Dirac-style operator and check whether its
eigenvalues approach gamma_n more closely than the generic operators
of sim v9.

Construction:
  Decompose the 26-dim block as V_paired = V_spin (+) V_vec
  where:
    V_spin: 8-dim = (2-dim irrep) (+) (2'-dim irrep) appearing with
            multiplicity 2 each.  Wait: 4+4 = 8, mult-2 of dim-2
            and mult-2 of dim-2'.  Actually each 2-irrep appears
            with multiplicity 2 in regular rep, giving 4-dim total.
            So V_spin = 2 copies of (2-irrep) + 2 copies of
            (2'-irrep) = 4 + 4 = 8.
    V_vec: 18-dim = 3 copies of (3-irrep) + 3 copies of (3'-irrep)
           = 9 + 9 = 18.

  We construct an intertwiner C: V_spin -> V_vec (and its adjoint)
  using a specific Clifford-like coupling.  The Dirac operator is

    D = [ 0    C^t ]
        [ C    0   ]

  This is automatically self-adjoint and has eigenvalues +-sigma_k
  where sigma_k are singular values of C.

  We try several natural choices for C:
    C1: random C (control)
    C2: C constructed from icosian quaternion multiplication
    C3: C built from W(H_4)-equivariant Clifford generators
    C4: C = some specific entangling using the actual icosian
        structure (Hopf-like)

Compare eigenvalue spectra of D to gamma_n.
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
OUTPUTS = HERE.parent / "outputs" / "v10"
DATA = HERE.parent / "data" / "v10"
OUTPUTS.mkdir(parents=True, exist_ok=True)
DATA.mkdir(parents=True, exist_ok=True)

PHI = (1.0 + math.sqrt(5.0)) / 2.0
INVPHI = 1.0 / PHI

GAMMAS = np.array([
    14.134725141734693, 21.022039638771555, 25.010857580145688,
    30.424876125859513, 32.935061587739190, 37.586178158825671,
    40.918719012147495, 43.327073280914999, 48.005150881167160,
    49.773832477672302, 52.970321477714461, 56.446247697063246,
    59.347044002602353, 60.831778524609811, 65.112544048081607,
    67.079810529494173, 69.546401711173979, 72.067157674481907,
    75.704690699083933, 77.144840068874806, 79.337375020249367,
    82.910380854086030, 84.735492980517050, 87.425274613125229,
    88.809111207634465, 92.491899270558484,
])

# A_1 eigenvalues by irrep block (numeric values)
# 2-spin pair: +6 phi, +6-6phi numeric values
SPIN_EIGS = [6.0 * PHI, 6.0 - 6.0 * PHI]  # mult 4 each, so 8 dim total
# 3-vector pair: +4 phi, +4-4phi
VEC_EIGS  = [4.0 * PHI, 4.0 - 4.0 * PHI]  # mult 9 each, so 18 dim total

RATIONAL_A1 = [12.0, 3.0, 0.0, -2.0, -3.0]


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


def build_projector_to_eigenspaces(A1, target_eigs, tol=1e-5):
    """Return the matrix V such that V's columns are A_1 eigenvectors
    at eigvals matching target_eigs.  Returns (V, dim).
    """
    eigvals, eigvecs = np.linalg.eigh(A1)
    cols = []
    for k in range(len(eigvals)):
        if any(abs(eigvals[k] - t) < tol for t in target_eigs):
            cols.append(eigvecs[:, k])
    if not cols:
        return np.zeros((A1.shape[0], 0)), 0
    V = np.array(cols).T
    return V, V.shape[1]


def quat_mul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return np.array([
        a1*a2 - b1*b2 - c1*c2 - d1*d2,
        a1*b2 + b1*a2 + c1*d2 - d1*c2,
        a1*c2 - b1*d2 + c1*a2 + d1*b2,
        a1*d2 + b1*c2 - c1*b2 + d1*a2,
    ])


def best_linear_fit(features, target):
    F = np.vstack([np.sort(f) for f in features]).T
    t = np.sort(target)
    coefs, _, _, _ = np.linalg.lstsq(F, t, rcond=None)
    pred = F @ coefs
    rmse = float(np.sqrt(np.mean((pred - t) ** 2)))
    return coefs, rmse, pred


def main():
    findings = []
    print("=" * 70)
    print("SIM v10: Dirac-style spin-coupled operator on 26-dim block")
    print("=" * 70)

    print("\n[1] Build V_600, A_1, identify spin (8) and vector (18) blocks...")
    verts = generate_v600()
    A1 = build_a1(verts)

    V_spin, d_spin = build_projector_to_eigenspaces(A1, SPIN_EIGS)
    V_vec,  d_vec  = build_projector_to_eigenspaces(A1, VEC_EIGS)
    findings.append(f"V_spin: {d_spin}-dim (expected 8 = 4+4 from "
                    "(2,2') irreps)")
    findings.append(f"V_vec:  {d_vec}-dim (expected 18 = 9+9 from "
                    "(3,3') irreps)")
    findings.append(f"Total: {d_spin + d_vec} (expected 26)")
    findings.append("")

    # ---- Construct candidate Clifford-like couplings C: V_spin -> V_vec
    # General shape: each spinor basis vector maps to a linear
    # combination of vector basis vectors.  We try several:

    rng = np.random.default_rng(42)

    candidates_C = {}

    # C1: random
    candidates_C["random Clifford"] = rng.standard_normal((d_vec, d_spin))

    # C2: structured via icosian quaternion multiplication.
    # Build C as the matrix elements <vec_a | q_i . spin_b> where q_i
    # are a fixed set of icosian quaternion generators acting on V_600
    # by left multiplication, restricted to the 26-dim block.
    #
    # Pick a single icosian g = phi/2 + i/2 + (1/phi)/2 j + 0 k as
    # a generator that mixes spinor and vector blocks.
    g = np.array([PHI / 2, 0.5, INVPHI / 2, 0])
    g = g / np.linalg.norm(g)

    # Build the 120x120 matrix L_g representing left multiplication
    # by g (in some basis); restrict it to V_spin -> V_vec block.
    L_g = np.zeros((120, 120))
    for j, v in enumerate(verts):
        # g . v as a quaternion
        gv = quat_mul(g, v)
        # Find which V_600 vertex this is (approximately)
        best_match = None
        best_diff = math.inf
        for i, vi in enumerate(verts):
            diff = np.linalg.norm(gv - vi)
            if diff < best_diff:
                best_diff = diff
                best_match = i
        if best_match is not None and best_diff < 1e-2:
            L_g[best_match, j] = 1.0

    # Project: <vec basis | L_g | spin basis>
    candidates_C["icosian g-coupling"] = V_vec.T @ L_g @ V_spin

    # C3: another icosian generator
    g2 = np.array([0, 1, 0, 0])  # i
    L_g2 = np.zeros((120, 120))
    for j, v in enumerate(verts):
        gv = quat_mul(g2, v)
        best_match = None
        best_diff = math.inf
        for i, vi in enumerate(verts):
            diff = np.linalg.norm(gv - vi)
            if diff < best_diff:
                best_diff = diff
                best_match = i
        if best_match is not None and best_diff < 1e-2:
            L_g2[best_match, j] = 1.0
    candidates_C["i-coupling"] = V_vec.T @ L_g2 @ V_spin

    # C4: combined icosian-driven Clifford
    L_combo = L_g + 0.5 * L_g2
    candidates_C["combined icosian"] = V_vec.T @ L_combo @ V_spin

    # ---- For each C, build D = [[0, C^T], [C, 0]] (26x26) and
    # compute eigenvalues
    findings.append("Dirac-style operator D = [[0, C^T],[C, 0]] on "
                    "V_spin (+) V_vec (26-dim total):")

    fit_results = {}
    for name, C in candidates_C.items():
        # Build D
        D = np.zeros((26, 26))
        D[:d_spin, d_spin:] = C.T
        D[d_spin:, :d_spin] = C
        # Symmetrize for numerical stability
        D = 0.5 * (D + D.T)
        eigs = np.linalg.eigvalsh(D)
        # 1-feature LS fit to gamma_n
        coefs, rmse, pred = best_linear_fit([eigs], GAMMAS)
        fit_results[name] = (rmse, coefs, pred, eigs)
        findings.append(f"  {name:<25} RMSE = {rmse:.4f}  "
                        f"coef = {coefs[0]:.4f}  "
                        f"spectral range = [{eigs.min():.3f}, "
                        f"{eigs.max():.3f}]")

    findings.append("")

    # Try absolute-value Dirac (|D| has only positive eigvals matching
    # gamma_n positivity)
    findings.append("Absolute-value Dirac |D| spectra (positive only):")
    for name, (rmse, coefs, pred, eigs) in fit_results.items():
        abs_eigs = np.sort(np.abs(eigs))
        coefs2, rmse2, _ = best_linear_fit([abs_eigs], GAMMAS)
        findings.append(f"  |{name}|: RMSE = {rmse2:.4f}  "
                        f"coef = {coefs2[0]:.4f}")

    # Multi-feature combined fit
    all_eigs_list = [fit_results[k][3] for k in fit_results]
    coefs_all, rmse_all, pred_all = best_linear_fit(all_eigs_list, GAMMAS)
    findings.append("")
    findings.append(f"COMBINED 4-Dirac fit: RMSE = {rmse_all:.4f}")
    for name, c in zip(fit_results.keys(), coefs_all):
        findings.append(f"  {name:<25} c = {c:.6f}")

    # Random control: best of 20 random Dirac
    rng2 = np.random.default_rng(99)
    rnd_rmses = []
    for _ in range(20):
        C_rnd = rng2.standard_normal((d_vec, d_spin))
        D_rnd = np.zeros((26, 26))
        D_rnd[:d_spin, d_spin:] = C_rnd.T
        D_rnd[d_spin:, :d_spin] = C_rnd
        D_rnd = 0.5 * (D_rnd + D_rnd.T)
        eigs_rnd = np.linalg.eigvalsh(D_rnd)
        _, rmse_rnd, _ = best_linear_fit([eigs_rnd], GAMMAS)
        rnd_rmses.append(rmse_rnd)

    findings.append("")
    findings.append(f"Random-Dirac control (20 samples):")
    findings.append(f"  median 1-feature RMSE = {np.median(rnd_rmses):.4f}")
    findings.append(f"  best    1-feature RMSE = {min(rnd_rmses):.4f}")

    # Save
    with open(DATA / "dirac_fit_results.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["candidate", "rmse_single", "coef_single",
                    "spec_min", "spec_max"])
        for name, (rmse, coefs, _, eigs) in fit_results.items():
            w.writerow([name, f"{rmse:.6f}", f"{coefs[0]:.6f}",
                        f"{eigs.min():.4f}", f"{eigs.max():.4f}"])

    # ---- Plot
    fig, ax = plt.subplots(figsize=(13, 7))
    xs = np.arange(26) + 1
    ax.plot(xs, GAMMAS, "o-", color="black", linewidth=1.5,
            markersize=6, label="Riemann gamma_n (target)")

    # Best candidate prediction
    best_key = min(fit_results, key=lambda k: fit_results[k][0])
    _, _, pred_best, _ = fit_results[best_key]
    ax.plot(xs, np.sort(pred_best), "s--", color="tab:red",
            linewidth=1.2, markersize=5,
            label=f"Best Dirac: {best_key} (RMSE = "
                  f"{fit_results[best_key][0]:.2f})")

    # Combined fit
    ax.plot(xs, np.sort(pred_all), "d-.", color="tab:green",
            linewidth=1.2, markersize=5,
            label=f"Combined 4-Dirac LS fit (RMSE = {rmse_all:.2f})")

    ax.set_title(
        "Sim v10: Dirac-style spin-coupled operators on V_600 26-dim "
        "block\n"
        "vs. first 26 Riemann gamma_n"
    )
    ax.set_xlabel("Riemann zero index n")
    ax.set_ylabel("gamma_n (target) or predicted")
    ax.legend(loc="best")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUTS / "01_dirac_vs_gamma.png", dpi=140)
    plt.close()

    # RMSE bar
    fig, ax = plt.subplots(figsize=(11, 6))
    names = list(fit_results.keys())
    rmses = [fit_results[n][0] for n in names]
    ax.bar(names, rmses, color="tab:purple", edgecolor="black")
    ax.axhline(np.median(rnd_rmses), color="red", linestyle="--",
               label=f"random-Dirac median RMSE = "
                     f"{np.median(rnd_rmses):.2f}")
    ax.axhline(rmse_all, color="green", linestyle=":",
               label=f"combined 4-Dirac fit = {rmse_all:.2f}")
    ax.set_ylabel("RMSE vs. gamma_n (1-feature fit)")
    ax.set_title("Per-Dirac-construction 1-feature RMSE")
    ax.legend()
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUTS / "02_dirac_rmse.png", dpi=140)
    plt.close()

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for line in findings:
        print(line)

    with open(DATA / "findings.txt", "w") as f:
        f.write("\n".join(findings))


if __name__ == "__main__":
    main()
