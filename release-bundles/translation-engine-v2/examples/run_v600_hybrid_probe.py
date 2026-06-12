"""Hybrid operator probe: SAGE Hecke data + V_600 26-dim block.

This is the genuine engine v0.3 application: take real SAGE Hecke
eigenvalues and use them to PARAMETERISE candidate operators on
V_600's 26-dim Galois-paired block, then test against the
calibrated deep checks.

The construction:
  1. From SAGE: real Hecke matrices T_p for primes 2..47
     (BrandtModule(31, 1) over Q).
  2. Extract Hecke eigenvalues e_p,1, e_p,2, e_p,3 for each prime p.
  3. Build candidate operators on V_600's 26-dim block of the form:
        T_candidate = sum_p sum_i alpha_{p,i} * P_p,i
     where P_p,i is a structure-preserving projector onto eigenspaces
     of A_1 weighted by Hecke eigenvalue e_p,i.
  4. For each construction, compute the calibrated deep checks
     (FE / DN / GUE) and report.

The honest question: do hybrid constructions get CLOSER to
HILBERT_POLYA_STRONG than substrate-only operators?

If yes: we have a concrete path toward T.
If no: the wall is precisely identified.
"""
from __future__ import annotations

import json
import math
import sys
from itertools import permutations, product
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "code"))

import deep_admissibility_calibrated as deepc
import admissibility as adm

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


def project_to_block(M, V_block):
    return V_block.T @ M @ V_block


def main():
    print("=" * 76)
    print("HYBRID OPERATOR PROBE: SAGE Hecke + V_600 26-dim block")
    print("=" * 76)

    print("\n[1] Load SAGE Hecke data...")
    with open(HERE.parent / "data" / "brandt_level31.json") as f:
        brandt_data = json.load(f)
    n_primes = len(brandt_data["hecke_operators"])
    print(f"  Loaded {n_primes} Hecke operators")

    # Extract Hecke eigenvalues
    hecke_eigvals = {}
    for h in brandt_data["hecke_operators"]:
        M = np.array(h["matrix"], dtype=float)
        M_sym = 0.5 * (M + M.T)
        eigs = np.linalg.eigvalsh(M_sym)
        hecke_eigvals[h["prime"]] = (eigs, h["kind_in_Q_sqrt_5"])

    print("  Prime  Kind         Hecke eigenvalues")
    for p, (eigs, kind) in sorted(hecke_eigvals.items()):
        print(f"  {p:<6} {kind:<12} {sorted(eigs.tolist())}")

    print("\n[2] Build V_600, A_1, identify 26-dim Galois-paired block...")
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
    print(f"  V_block: {V_block.shape}, A1_block on 26-dim")

    A1_block_eigvals, A1_block_eigvecs = np.linalg.eigh(A1_block)
    print(f"  A1 block eigenvalues (distinct): "
          f"{sorted(set(round(float(e), 4) for e in A1_block_eigvals))}")

    # ----------------------------------------------------------------------
    # Construction 1: weight A1 eigenspaces by Hecke eigenvalues
    # ----------------------------------------------------------------------
    print("\n[3] Construction 1: A1 eigenspace * Hecke weighting")
    print("    Use the FIRST Hecke eigenvalue of each prime as a")
    print("    weight on A1's eigenspaces (in order of |eigenvalue|).")

    # Group A1 eigenvectors by their eigenvalue
    block_distinct = sorted(set(round(float(e), 4)
                                  for e in A1_block_eigvals))
    # We have 4 distinct A1-eigenvalues in 26-dim block
    # Pick first 4 Hecke eigenvalues from primes 2, 3, 5, 7
    hecke_weights = []
    primes_used = [2, 3, 5, 7]
    for p in primes_used:
        eigs = hecke_eigvals[p][0]
        hecke_weights.append(float(eigs[0]))  # smallest Hecke eigval
    print(f"  Using primes {primes_used}, smallest Hecke eigvals: "
          f"{hecke_weights}")

    T_c1 = np.zeros((26, 26))
    for k, A1_e in enumerate(block_distinct):
        weight = hecke_weights[k] if k < len(hecke_weights) else 0.0
        # Project onto this A1 eigenspace and weight by Hecke eigval
        proj = np.zeros((26, 26))
        for i, e in enumerate(A1_block_eigvals):
            if abs(float(e) - A1_e) < 1e-4:
                v = A1_block_eigvecs[:, i:i+1]
                proj += v @ v.T
        T_c1 += weight * proj
    T_c1 = 0.5 * (T_c1 + T_c1.T)
    print(f"  Construction 1 spectrum: "
          f"{sorted(np.linalg.eigvalsh(T_c1).tolist())}")

    summary_c1 = deepc.evaluate_calibrated(T_c1)
    sm_v, sm_r, _ = adm.check_spectral_match(T_c1, deepc.GAMMAS,
                                              use_abs=True)
    print(f"  Verdicts: SM={sm_v} (RMSE {sm_r:.2f}) | "
          f"FE={summary_c1['functional_equation']['verdict']} | "
          f"DN={summary_c1['density_consistent']['verdict']} | "
          f"GUE={summary_c1['gue_distributed']['verdict']} | "
          f"Overall: {summary_c1['overall']}")

    # ----------------------------------------------------------------------
    # Construction 2: linear combination using ALL Hecke trace data
    # ----------------------------------------------------------------------
    print("\n[4] Construction 2: linear combination of A1 powers and "
          "Hecke-weighted projectors")
    # Build operator = sum_k alpha_k A1^k + sum_p beta_p (eigenval-weighted)
    # with coefficients chosen to maximise the SPECTRAL_MATCH

    features = []
    labels = []
    for k in range(1, 5):
        Ak = np.linalg.matrix_power(A1_block, k)
        Ak = 0.5 * (Ak + Ak.T)
        features.append(np.sort(np.abs(np.linalg.eigvalsh(Ak))))
        labels.append(f"A1^{k}")
    # Add Hecke-weighted projectors
    for p in [2, 3, 5, 7, 11, 13]:
        eigs = hecke_eigvals[p][0]
        # For each Hecke eigenvalue, build A1-eigenspace projector
        # weighted by it
        for h_idx, h_eig in enumerate(eigs):
            proj = np.zeros((26, 26))
            for i, e in enumerate(A1_block_eigvals):
                # weight by exp(-(e - target)^2)
                target = block_distinct[
                    h_idx % len(block_distinct)]
                w = math.exp(-((float(e) - target) ** 2))
                v = A1_block_eigvecs[:, i:i+1]
                proj += w * float(h_eig) * v @ v.T
            proj = 0.5 * (proj + proj.T)
            features.append(np.sort(np.abs(np.linalg.eigvalsh(proj))))
            labels.append(f"T_{p}_e{h_idx}")

    print(f"  Total features (operators): {len(features)}")

    # LS fit
    feature_specs = []
    for f in features:
        if len(f) < len(deepc.GAMMAS):
            f = np.concatenate([f, np.zeros(len(deepc.GAMMAS) - len(f))])
        feature_specs.append(f[-len(deepc.GAMMAS):])
    F = np.vstack(feature_specs).T
    t = np.sort(deepc.GAMMAS)
    coefs, _, _, _ = np.linalg.lstsq(F, t, rcond=None)
    pred = F @ coefs
    rmse = float(np.sqrt(np.mean((pred - t) ** 2)))
    print(f"  LS-fit RMSE: {rmse:.4f}")
    print(f"  Top 5 coefficients by |coef|:")
    coef_abs_sorted = sorted(zip(labels, coefs.tolist()),
                              key=lambda x: -abs(x[1]))[:5]
    for label, c in coef_abs_sorted:
        print(f"    {label:<15} c = {c:+.4f}")

    # ----------------------------------------------------------------------
    # Construction 3: Direct Hecke embedding into 26-dim block
    # ----------------------------------------------------------------------
    print("\n[5] Construction 3: embed Hecke matrices directly into 26-dim "
          "block")
    print("    Build 26x26 block-diagonal: T_2 (+) T_3 (+) ... padded")
    # Stack 3x3 Hecke matrices into a 26x26 block
    T_c3 = np.zeros((26, 26))
    offset = 0
    primes_for_embed = [2, 3, 5, 7, 11, 13, 17, 19]  # 8 primes x 3 = 24 dim
    for p in primes_for_embed:
        if offset + 3 > 26:
            break
        T_p = np.array([h["matrix"] for h in brandt_data["hecke_operators"]
                        if h["prime"] == p][0], dtype=float)
        T_p = 0.5 * (T_p + T_p.T)
        T_c3[offset:offset+3, offset:offset+3] = T_p
        offset += 3
    # Last 2 dims: leave zero (or fill with average eigval)

    summary_c3 = deepc.evaluate_calibrated(T_c3)
    sm_v3, sm_r3, _ = adm.check_spectral_match(T_c3, deepc.GAMMAS,
                                                 use_abs=True)
    print(f"  Construction 3 spectrum: "
          f"{sorted(np.linalg.eigvalsh(T_c3).tolist())}")
    print(f"  Verdicts: SM={sm_v3} (RMSE {sm_r3:.2f}) | "
          f"FE={summary_c3['functional_equation']['verdict']} | "
          f"DN={summary_c3['density_consistent']['verdict']} | "
          f"GUE={summary_c3['gue_distributed']['verdict']} | "
          f"Overall: {summary_c3['overall']}")

    # ----------------------------------------------------------------------
    # Conclusion
    # ----------------------------------------------------------------------
    print()
    print("=" * 76)
    print("FINDINGS")
    print("=" * 76)
    print()
    print("Construction 1 (A1 eigenspaces weighted by Hecke):")
    print(f"  Overall: {summary_c1['overall']}")
    print()
    print(f"Construction 2 (LS fit over {len(features)} hybrid features):")
    print(f"  RMSE: {rmse:.4f}")
    print()
    print(f"Construction 3 (direct Hecke embedding):")
    print(f"  Overall: {summary_c3['overall']}")
    print()
    print("INTERPRETATION:")
    print("  We now have real Hecke data combined with V_600's 26-dim")
    print("  structure. The hybrid constructions test whether genuine")
    print("  number theory operations + substrate geometry can produce")
    print("  candidate Hilbert-Polya operators.")
    print()

    best_overall = max([
        ("Construction 1", summary_c1["overall"]),
        ("Construction 3", summary_c3["overall"])
    ], key=lambda x: {"HILBERT_POLYA_STRONG": 3,
                       "HILBERT_POLYA_PARTIAL": 2,
                       "PARTIAL_PASS": 1,
                       "RULED_OUT": 0}.get(x[1], 0))
    print(f"  Best hybrid construction: {best_overall[0]} "
          f"({best_overall[1]})")
    print()

    if "HILBERT_POLYA" in best_overall[1]:
        print("  This indicates structural alignment.  Further work needed:")
        print("    - higher-resolution Hecke data (more primes)")
        print("    - SAGE 10+ for icosian-specific BrandtModule")
        print("    - finer composition search")
    else:
        print("  No hybrid construction reaches HILBERT_POLYA territory.")
        print("  This bounds the search:")
        print("    - the level-31 Hecke action is not the right one")
        print("    - the icosian-specific Hecke (SAGE 10+) might be")
        print("    - or a fundamentally different combination is needed")
    print()
    print("THE PRECISE NEXT STEP:")
    print("  Install SAGE 10+ (conda-forge has 10.9), compute the icosian")
    print("  BrandtModule over Q(sqrt 5), re-run this exact probe with")
    print("  the icosian Hecke matrices.")
    print()
    print("  All v0.3 architecture is in place.  v0.4 is the SAGE 10")
    print("  upgrade + one-line script edit (level=31 -> icosian order).")

    # Save
    out_path = HERE.parent / "outputs" / "hybrid_probe_results.txt"
    with open(out_path, "w") as f:
        f.write("Hybrid operator probe: SAGE Hecke + V_600 26-dim\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"C1 verdict: {summary_c1['overall']}\n")
        f.write(f"C2 LS-fit RMSE: {rmse:.4f}\n")
        f.write(f"C3 verdict: {summary_c3['overall']}\n")
        f.write(f"\nBest: {best_overall[0]} ({best_overall[1]})\n")


if __name__ == "__main__":
    main()
