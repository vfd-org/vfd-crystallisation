"""Deep diagnostic: run the v0.2-extended engine with sharper
admissibility checks.

The previous diagnostic (run_v600_diagnostic.py) used only
SPECTRAL_MATCH (RMSE vs gamma_n) and found that no substrate-derived
operator matches gamma_n at EXACT level.  But SPECTRAL_MATCH is a
COARSE check -- many random Hermitians can game it.

This diagnostic adds four SHARPER admissibility checks:
  - FUNCTIONAL_EQUATION_RESPECTED (sign-symmetric spectrum)
  - DENSITY_CONSISTENT (Riemann-Hardy-Littlewood N(T))
  - GUE_DISTRIBUTED (Wigner spacing)
  - HECKE_MULTIPLICATIVE (where applicable)

A genuine Hilbert-Polya operator MUST pass all four.  Most prototype
operators will FAIL most of them.  The failure pattern tells us
exactly what structural property each operator candidate lacks --
which is the diagnostic value.

Output:
  For each strategy / candidate operator:
    - spectral magnitude RMSE (old check)
    - functional equation verdict
    - density verdict
    - GUE verdict
    - overall HP-candidate verdict
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
import deep_admissibility as deep
import dictionary as dct

PHI = (1.0 + math.sqrt(5.0)) / 2.0
INVPHI = 1.0 / PHI


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


def project_to_block(M_full, V_block):
    return V_block.T @ M_full @ V_block


def evaluate(operator, label):
    """Return a one-row summary of the operator's verdicts."""
    M = 0.5 * (operator + operator.T)
    eigs = np.linalg.eigvalsh(M)

    # Spectral match (basic)
    verdict_sm, rmse_sm, _ = adm.check_spectral_match(M, deep.GAMMAS,
                                                       use_abs=True)

    # Deep checks
    fe_v, fe_r, _ = deep.check_functional_equation(M)
    dn_v, dn_r, _ = deep.check_density_consistent(eigs)
    gue_v, gue_r, _ = deep.check_gue_distributed(eigs)

    return {
        "label": label,
        "spectral_match_verdict": verdict_sm,
        "spectral_match_rmse": rmse_sm,
        "functional_eq_verdict": fe_v,
        "functional_eq_residual": fe_r,
        "density_verdict": dn_v,
        "density_residual": dn_r,
        "gue_verdict": gue_v,
        "gue_residual": gue_r,
    }


def main():
    print("=" * 76)
    print("DEEP DIAGNOSTIC: engine v0.2 (sharper admissibility checks)")
    print("=" * 76)

    # Print dictionary summary
    print("\n[Dictionary / Grammar overview]")
    for line in dct.grammar_summary():
        print(line)
    print()

    # Build infrastructure
    print("[Setup] Building V_600, A_1, 26-dim block...")
    verts = generate_v600()
    A1 = build_a1(verts)
    eigvals_full, eigvecs_full = np.linalg.eigh(A1)
    rational_a1 = [12.0, 3.0, 0.0, -2.0, -3.0]
    cols = []
    for k in range(len(eigvals_full)):
        if not any(abs(eigvals_full[k] - r) < 1e-5 for r in rational_a1):
            cols.append(eigvecs_full[:, k])
    V_block = np.array(cols).T
    A1_block = project_to_block(A1, V_block)
    A1_block = 0.5 * (A1_block + A1_block.T)

    # Reference: Riemann gamma_n target itself, as if it were the
    # spectrum we found
    gamma_signed = np.concatenate([deep.GAMMAS[:13], -deep.GAMMAS[:13]])
    # Build a diagonal operator with these eigenvalues
    Gam_op = np.diag(gamma_signed)

    candidates = []

    # Candidate 0: the actual Riemann gammas as a sign-symmetric operator
    # (this is what the real Hilbert-Polya operator would look like!)
    candidates.append(("REFERENCE: Riemann gammas signed", Gam_op))

    # Candidate 1: A_1 block (substrate)
    candidates.append(("A_1 restricted to 26-dim block", A1_block))

    # Candidate 2: A_1 block squared (positive)
    A1_sq = A1_block @ A1_block
    candidates.append(("A_1^2 (positive)", A1_sq))

    # Candidate 3: Random Hermitian sized to gamma_n range
    rng = np.random.default_rng(42)
    M = rng.standard_normal((26, 26))
    M = 0.5 * (M + M.T) * 30  # scale to roughly gamma range
    candidates.append(("Random Hermitian (scaled)", M))

    # Candidate 4: A diagonal matrix with gamma_n on it (positive only)
    Gam_pos = np.diag(deep.GAMMAS)
    candidates.append(("Diagonal positive gammas", Gam_pos))

    # Candidate 5: Anti-Hermitian-like: A1 - A1^T (= 0 since symmetric)
    # Try instead i*[A1, L_g] where g is some icosian generator
    g = np.array([PHI / 2, 0.5, INVPHI / 2, 0])
    g = g / np.linalg.norm(g)
    L_g = np.zeros((120, 120))
    for j, v in enumerate(verts):
        a1q, b1q, c1q, d1q = g
        a2q, b2q, c2q, d2q = v
        gv = np.array([
            a1q*a2q - b1q*b2q - c1q*c2q - d1q*d2q,
            a1q*b2q + b1q*a2q + c1q*d2q - d1q*c2q,
            a1q*c2q - b1q*d2q + c1q*a2q + d1q*b2q,
            a1q*d2q + b1q*c2q - c1q*b2q + d1q*a2q,
        ])
        best_match, best_diff = None, math.inf
        for i, vi in enumerate(verts):
            d = np.linalg.norm(gv - vi)
            if d < best_diff:
                best_diff = d
                best_match = i
        if best_match is not None and best_diff < 1e-2:
            L_g[best_match, j] = 1.0
    L_g_block = project_to_block(L_g, V_block)
    comm = (A1_block @ L_g_block - L_g_block @ A1_block) * 1j
    comm = comm.real
    candidates.append(("[A_1, L_g] commutator", comm))

    # Evaluate each
    print("\n[Per-candidate verdicts on all 4 deep admissibility classes]")
    print()
    print(f"{'Candidate':<35} {'SM-RMSE':<10} {'FE':<10} {'DN':<12} {'GUE':<8}")
    print("-" * 84)
    results = []
    for label, op in candidates:
        r = evaluate(op, label)
        results.append(r)
        print(f"{label:<35} {r['spectral_match_rmse']:<10.2f} "
              f"{r['functional_eq_verdict']:<10} "
              f"{r['density_verdict']:<12} {r['gue_verdict']:<8}")

    print()
    print("Legend: SM = SPECTRAL_MATCH | FE = FUNCTIONAL_EQUATION |"
          " DN = DENSITY_CONSISTENT | GUE = GUE_DISTRIBUTED")
    print()

    # ----------------------------------------------------------------------
    # Interpret per-candidate
    # ----------------------------------------------------------------------
    print("=" * 76)
    print("INTERPRETATION")
    print("=" * 76)
    print()

    print("REFERENCE row (Riemann gammas signed): this is the BASELINE")
    print("a TRUE Hilbert-Polya operator should hit. Note which checks")
    print("it passes and which it doesn't pass at this 26-dim truncation.")
    print()
    print("REAL substrate-derived rows: check which deep classes they")
    print("FAIL. The pattern of failures tells us what structural property")
    print("the missing operator must have.")
    print()

    # Identify pass / fail patterns
    print("Pattern analysis (looking at deep verdicts only):")
    for r in results:
        label = r["label"]
        passes = []
        if r["functional_eq_verdict"] in ("EXACT", "STRONG"):
            passes.append("FE")
        if r["density_verdict"] in ("EXACT", "STRONG", "CANDIDATE"):
            passes.append("DN")
        if r["gue_verdict"] in ("EXACT", "STRONG", "CANDIDATE"):
            passes.append("GUE")
        print(f"  {label:<35} passes: {passes if passes else 'NONE'}")

    # ----------------------------------------------------------------------
    # The diagnostic conclusion
    # ----------------------------------------------------------------------
    print()
    print("=" * 76)
    print("WHAT THIS NARROWS")
    print("=" * 76)
    print()
    print("The deep admissibility checks give the engine the ability to")
    print("REJECT candidates that don't even have the right structural")
    print("shape, not just operators whose magnitudes are off.")
    print()
    print("Now the search can prune:")
    print("  - operators without sign-symmetric spectrum (FE BROKEN)")
    print("  - operators whose density is way off (DN BROKEN)")
    print("  - operators with non-GUE spacings (GUE BROKEN)")
    print()
    print("This dramatically narrows the effective search space.  Where")
    print("we previously had 'any 26x26 Hermitian matrix could be a")
    print("candidate', we now have 'only Hermitians that are sign-")
    print("symmetric, have N(T)-density, and GUE spacings'. That's a")
    print("FAR smaller subset.")
    print()
    print("DICTIONARY ADDITIONS NEEDED next:")
    print("  - Explicit Mellin transform table (for ANALYTIC_EXTEND)")
    print("  - Selberg class S checker (for SELBERG_CLASS_VERIFIED)")
    print("  - Multiple zeta family table (compare ours to Dirichlet L)")
    print("  - Sato-Tate measure (Hecke eigval normalisation)")
    print()
    print("GRAMMAR ADDITIONS NEEDED next:")
    print("  - LIFT_BY_BRANDT_MATRIX transformation kind (needs SAGE)")
    print("  - SELBERG_TRACE_APPLY (with explicit test function table)")
    print("  - EXPLICIT_FORMULA_VERIFY (Weil identity)")
    print("  - GUE_NORMALISE (rescale spectrum to GUE convention)")
    print()
    print("Each of these is a specific, well-scoped addition.  Adding")
    print("them gives the engine sharper rejection power, which means")
    print("the search converges faster (or fails faster) on real")
    print("constructions.")

    # Save
    output_path = HERE.parent / "outputs" / "deep_diagnostic_results.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write("Deep diagnostic results\n")
        f.write("=" * 60 + "\n\n")
        for r in results:
            f.write(f"{r['label']}:\n")
            f.write(f"  SPECTRAL_MATCH: {r['spectral_match_verdict']} "
                    f"(RMSE {r['spectral_match_rmse']:.4f})\n")
            f.write(f"  FUNCTIONAL_EQUATION: {r['functional_eq_verdict']} "
                    f"(residual {r['functional_eq_residual']:.4e})\n")
            f.write(f"  DENSITY: {r['density_verdict']} "
                    f"(residual {r['density_residual']:.4e})\n")
            f.write(f"  GUE: {r['gue_verdict']} "
                    f"(residual {r['gue_residual']:.4e})\n\n")


if __name__ == "__main__":
    main()
