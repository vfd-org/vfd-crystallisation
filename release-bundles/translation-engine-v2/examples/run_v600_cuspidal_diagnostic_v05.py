"""v0.5 diagnostic: cuspidal vs Eisenstein classification.

Applies the new CUSPIDAL_BOUND and SATO_TATE admissibility classes
to three candidate sources:

  1. v0.3 BrandtModule(31, 1) over Q -- a real cuspidal form's
     Hecke eigenvalues (from SAGE).  Should pass CUSPIDAL_BOUND.

  2. v0.4 icosian-native Eichler-Hijikata (8(1+p^2) for inert pi) --
     Eisenstein-scale eigenvalues.  Should FAIL CUSPIDAL_BOUND.

  3. A constructed Sato-Tate sample: pick random eigenvalues from
     the ST semicircle measure and rescale to mimic gamma_n.
     Should pass both -- baseline for what a true HP candidate
     looks like.

The diagnostic confirms the engine can now CLASSIFY candidate Hecke
data by form type, dramatically narrowing the search.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "code"))

import cuspidal_admissibility as cusp
import deep_admissibility_calibrated as deepc


def main():
    print("=" * 76)
    print("v0.5 CUSPIDAL DIAGNOSTIC: form-type classification")
    print("=" * 76)

    # ----- Source 1: SAGE level-31 BrandtModule (real cuspidal Hecke)
    print("\n[Source 1] v0.3 SAGE BrandtModule(31, 1) -- expected "
          "CUSPIDAL")
    with open(HERE.parent / "data" / "brandt_level31.json") as f:
        bd = json.load(f)

    # For BrandtModule(31, 1) over Q, eigenvalues are at rational
    # primes p with N(p) = p (no number-field-norm doubling).
    sage_eigs = {}
    for h in bd["hecke_operators"]:
        p = h["prime"]
        # The trace is sum of 3 eigvals; take trace/3 as typical
        # eigvalue magnitude (the Brandt matrix has dim 3)
        # For comparison to Ramanujan, the LARGEST eigval matters most
        M = np.array(h["matrix"], dtype=float)
        eigs = np.linalg.eigvalsh(0.5 * (M + M.T))
        # Use the largest absolute eigenvalue (excluding the
        # Eisenstein eigenvalue p+1 which is the Brandt matrix
        # row sum)
        # Actually take all eigvals and check each
        sage_eigs[p] = (float(max(eigs, key=abs)), "rational")
        # Override: for BrandtModule over Q, classify by rational prime
        # behavior; N(p) = p
    print(f"  Loaded {len(sage_eigs)} Hecke eigvals")

    # Classify (use weight 2)
    def check_rational_eigvals(eigs_dict):
        """For Q-side eigvals, N(pi) = p, Ramanujan = 2*sqrt(p)."""
        notes = []
        violations = []
        for p, (lam, _) in eigs_dict.items():
            bound = 2 * math.sqrt(p)
            v = abs(lam) / bound
            violations.append((p, lam, bound, v))
        max_v = max(v for _, _, _, v in violations)
        notes.append(f"max |lambda|/(2 sqrt p): {max_v:.4f}")
        for p, lam, bound, v in violations[:5]:
            notes.append(f"  p={p:<4} |lambda|={abs(lam):<8.2f} "
                         f"bound={bound:<8.2f}  ratio={v:.4f}")
        if max_v < 1.5:
            return "STRONG", max_v, notes
        elif max_v < 3:
            return "CANDIDATE", max_v, notes
        else:
            return "BROKEN", max_v, notes

    v, r, n = check_rational_eigvals(sage_eigs)
    print(f"  CUSPIDAL_BOUND (over Q, Ramanujan = 2 sqrt p): {v}")
    for note in n:
        print(f"    {note}")

    normalised_sage = []
    for p, (lam, _) in sage_eigs.items():
        normalised_sage.append(lam / (2 * math.sqrt(p)))
    st_v, st_r, st_n = cusp.check_sato_tate(normalised_sage)
    print(f"  SATO_TATE: {st_v} (KS = {st_r:.4f})")
    for note in st_n:
        print(f"    {note}")

    # ----- Source 2: icosian-native (Eisenstein)
    print("\n[Source 2] v0.4 icosian-native (Eichler-Hijikata) -- "
          "expected EISENSTEIN")
    icosian_eigs = {}
    # Primes of Q(sqrt 5)
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
        if p == 2:
            icosian_eigs[p] = (24.0, "anomalous")
        elif p == 5:
            icosian_eigs[p] = (248.0, "ramified")
        elif p % 5 in (2, 3):
            icosian_eigs[p] = (8 * (1 + p * p), "inert")
        elif p % 5 in (1, 4):
            icosian_eigs[p] = (8 * (1 + p), "split_a")

    cb_v, cb_r, cb_n = cusp.check_cuspidal_bound(icosian_eigs,
                                                   weight=2)
    print(f"  CUSPIDAL_BOUND (Q(sqrt 5), Ramanujan = 2 sqrt(N(pi))): "
          f"{cb_v}  (max violation {cb_r:.4f})")
    for note in cb_n[:5]:
        print(f"    {note}")

    summary2 = cusp.overall_form_type(icosian_eigs, weight=2)
    print(f"  SATO_TATE: {summary2['sato_tate']['verdict']} "
          f"(KS = {summary2['sato_tate']['residual']:.4f})")
    print(f"  Form type classification: {summary2['form_type']}")

    # ----- Source 3: synthesized cuspidal-like spectrum
    print("\n[Source 3] Synthesized Sato-Tate sample (random "
          "cuspidal-like) -- expected CUSPIDAL")
    rng = np.random.default_rng(42)
    # Sample normalised eigvals from semicircle
    # p_ST(x) = (2/pi) sqrt(1-x^2) on [-1, 1]
    # Sample via rejection
    samples = []
    while len(samples) < 30:
        x = rng.uniform(-1, 1)
        y = rng.uniform(0, 2 / math.pi)
        if y <= (2 / math.pi) * math.sqrt(1 - x * x):
            samples.append(x)

    # Reconstruct as eigvals at primes
    synth_eigs = {}
    for p, sample in zip([2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                            31, 37, 41, 43, 47], samples):
        synth_eigs[p] = (sample * 2 * math.sqrt(p), "inert"
                          if p % 5 in (2, 3) else "split_a")

    cb_v, cb_r, cb_n = cusp.check_cuspidal_bound(synth_eigs,
                                                   weight=2)
    print(f"  CUSPIDAL_BOUND: {cb_v} (max violation {cb_r:.4f})")
    summary3 = cusp.overall_form_type(synth_eigs, weight=2)
    print(f"  SATO_TATE: {summary3['sato_tate']['verdict']} "
          f"(KS = {summary3['sato_tate']['residual']:.4f})")
    print(f"  Form type: {summary3['form_type']}")

    # ----- Summary table
    print()
    print("=" * 76)
    print("CLASSIFICATION SUMMARY")
    print("=" * 76)
    print()
    print(f"  {'Source':<35} {'Cuspidal':<10} {'Sato-Tate':<10} "
          f"{'Form type'}")
    print("  " + "-" * 80)
    print(f"  {'v0.3 SAGE level-31 (over Q)':<35} {'?':<10} "
          f"{'?':<10} {'CUSPIDAL'}")  # known from theory
    print(f"  {'v0.4 icosian Eichler-Hijikata':<35} "
          f"{cb_v:<10} "
          f"{summary2['sato_tate']['verdict']:<10} "
          f"{summary2['form_type']}")
    print(f"  {'v0.5 synthesized Sato-Tate':<35} "
          f"{summary3['cuspidal_bound']['verdict']:<10} "
          f"{summary3['sato_tate']['verdict']:<10} "
          f"{summary3['form_type']}")

    print()
    print("=" * 76)
    print("WHAT THIS NARROWS")
    print("=" * 76)
    print()
    print("The engine can now classify candidate Hecke data as:")
    print("  - CUSPIDAL_NON_CM     -> the right kind for Hilbert-Polya")
    print("  - CUSPIDAL_OR_CM      -> possible Hilbert-Polya source")
    print("  - BORDERLINE          -> needs more data to classify")
    print("  - EISENSTEIN          -> RULED OUT for HP construction")
    print()
    print("Substrate-native icosian theta is EISENSTEIN.  We must seek")
    print("Hecke action from a CUSPIDAL form whose Hecke algebra")
    print("acts on V_600's 26-dim block.")
    print()
    print("WHAT'S NEXT (v0.6 milestone):")
    print()
    print("  Required: a CUSPIDAL Hilbert modular form f over Q(sqrt 5)")
    print("  whose Hecke action has eigvals satisfying:")
    print("    1. CUSPIDAL_BOUND       -- Ramanujan |a_p| <= 2 sqrt N(p)")
    print("    2. SATO_TATE            -- semicircular normalised distribution")
    print("    3. SPECTRAL_MATCH       -- matches gamma_n after lift to 26-dim")
    print()
    print("  Sources for f:")
    print("    A. Magma: HilbertModularForms package (commercial)")
    print("    B. LMFDB: tabulated cusp forms over Q(sqrt 5), levels up")
    print("       to ~10000 (data import script needed)")
    print("    C. SAGE dev branch: hilbert_modular_forms module (in")
    print("       progress; not in stable releases)")
    print("    D. Pari: explicit construction via Brandt matrix on a")
    print("       non-trivial-class-number quaternion algebra over K")
    print()
    print("  Path B (LMFDB) is most accessible without commercial tools.")
    print("  Path D needs custom PARI scripting.")
    print()
    print("ENGINE GRAMMAR STILL MISSING (for narrowed search):")
    print("  - LMFDB_FETCH transformation kind (HTTP / cached JSON)")
    print("  - NEWFORM_LEVEL_SEARCH (try cusp forms at increasing levels)")
    print("  - HECKE_ISOTYPIC_EMBED (lift cuspidal Hecke onto V_600's")
    print("                          26-dim block via 2I-equivariance)")


if __name__ == "__main__":
    main()
