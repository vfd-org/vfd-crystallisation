"""v0.5 full diagnostic: all admissibility classes + Eisenstein
projection + explicit formula.

Applies the now-complete v0.5 engine to multiple candidates and
reports the verdict matrix:

  SM | FE | DN | GUE | CUSPIDAL_BOUND | SATO_TATE | EXPLICIT_FORMULA

A candidate passing ALL of these at CANDIDATE+ is in HP territory.

This diagnostic also demonstrates the Eisenstein projection on the
SAGE Brandt data — extracting the cuspidal sub-spectrum that should
satisfy Ramanujan.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "code"))

import deep_admissibility_calibrated as deepc
import admissibility as adm
import cuspidal_admissibility as cusp
import explicit_formula as ef


def main():
    print("=" * 80)
    print("v0.5 FULL DIAGNOSTIC: 7 admissibility classes + Eisenstein "
          "projection")
    print("=" * 80)

    GAMMAS = deepc.GAMMAS
    candidates = []

    # ----- Source 1: gamma_n itself (gold standard)
    Gam_pos = np.diag(GAMMAS)
    candidates.append(("Diagonal gamma_n (target)", Gam_pos, None))

    # ----- Source 2: Sign-paired gamma_n
    gam_signed = np.concatenate([GAMMAS[:13], -GAMMAS[:13]])
    candidates.append(("Sign-paired gamma_n", np.diag(gam_signed), None))

    # ----- Source 3: SAGE level-31 BrandtModule with Eisenstein
    # projection
    print("\n[Eisenstein projection on SAGE Brandt matrices]")
    with open(HERE.parent / "data" / "brandt_level31.json") as f:
        bd = json.load(f)

    cuspidal_eigvals_sage = {}
    eisenstein_eigvals_sage = []
    for h in bd["hecke_operators"]:
        p = h["prime"]
        M = np.array(h["matrix"], dtype=float)
        cusp_sub, eis_eig, cusp_eigs = ef.project_out_eisenstein(M)
        eisenstein_eigvals_sage.append(eis_eig)
        # The cuspidal eigenvalues for this prime
        if len(cusp_eigs) > 0:
            # Take the cuspidal eigenvalue with largest |.|
            cuspidal_eigvals_sage[p] = (float(max(cusp_eigs, key=abs)),
                                          "rational")

    eis_strs = []
    for h, e in zip(bd['hecke_operators'], eisenstein_eigvals_sage):
        p = h['prime']
        if math.isnan(e):
            eis_strs.append(f"{p}:NaN")
        else:
            eis_strs.append(f"{p}:{int(round(e))}")
    print(f"  Eisenstein eigvals (should be p+1 for prime p): "
          f"{eis_strs}")
    print(f"  Cuspidal eigvals (should satisfy Ramanujan):")
    for p, (lam, _) in cuspidal_eigvals_sage.items():
        bound = 2 * math.sqrt(p)
        ratio = abs(lam) / bound
        flag = "OK" if ratio <= 1.05 else "VIOLATION"
        print(f"    p = {p:<4} cusp_eig = {lam:<8.3f} bound = "
              f"{bound:<6.3f}  ratio = {ratio:.3f}  {flag}")

    # Build a candidate operator from cuspidal SAGE eigvals
    sage_cusp_spec = sorted([lam for (lam, _) in
                              cuspidal_eigvals_sage.values()])
    sage_cusp_spec_signed = sorted(sage_cusp_spec
                                     + [-x for x in sage_cusp_spec])
    if len(sage_cusp_spec_signed) >= 26:
        spec_use = np.array(sage_cusp_spec_signed[:26])
    else:
        spec_use = np.concatenate([sage_cusp_spec_signed,
                                    np.zeros(26 - len(sage_cusp_spec_signed))])
    candidates.append(
        ("SAGE Brandt cuspidal projection",
         np.diag(spec_use), cuspidal_eigvals_sage))

    # ----- Source 4: icosian Eisenstein eigvals
    icosian_eigs = {}
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
        if p == 2:
            icosian_eigs[p] = (24.0, "anomalous")
        elif p == 5:
            icosian_eigs[p] = (248.0, "ramified")
        elif p % 5 in (2, 3):
            icosian_eigs[p] = (8 * (1 + p * p), "inert")
        elif p % 5 in (1, 4):
            icosian_eigs[p] = (8 * (1 + p), "split_a")

    ic_spectrum = sorted([float(lam) for (lam, _) in icosian_eigs.values()])
    ic_signed = sorted(ic_spectrum + [-x for x in ic_spectrum])
    if len(ic_signed) >= 26:
        ic_use = ic_signed[:26]
    else:
        ic_use = ic_signed + [0.0] * (26 - len(ic_signed))
    candidates.append(
        ("Icosian native (Eisenstein)",
         np.diag(np.array(ic_use)), icosian_eigs))

    # Run all checks
    print()
    print("=" * 100)
    print("VERDICT MATRIX")
    print("=" * 100)
    print()
    print(f"{'Candidate':<35} | {'SM':<8} {'FE':<8} {'DN':<8} {'GUE':<8} {'EF':<8} {'CB':<8} {'ST':<8} | {'FormType'}")
    print("-" * 110)

    for label, op, prime_eigs in candidates:
        sm_v, sm_r, _ = adm.check_spectral_match(op, GAMMAS,
                                                  use_abs=True)
        deep_s = deepc.evaluate_calibrated(op)
        ef_v, ef_r, _ = ef.check_explicit_formula(np.diag(op)
                                                    if op.ndim == 2
                                                    else op)
        if prime_eigs:
            cusp_s = cusp.overall_form_type(prime_eigs, weight=2)
            cb_v = cusp_s["cuspidal_bound"]["verdict"]
            st_v = cusp_s["sato_tate"]["verdict"]
            ft = cusp_s["form_type"]
        else:
            cb_v = "N/A"
            st_v = "N/A"
            ft = "—"

        print(f"{label:<35} | {sm_v:<8} "
              f"{deep_s['functional_equation']['verdict']:<8} "
              f"{deep_s['density_consistent']['verdict']:<8} "
              f"{deep_s['gue_distributed']['verdict']:<8} "
              f"{ef_v:<8} {cb_v:<8} {st_v:<8} | {ft}")

    print()
    print("Legend: SM=SpectralMatch FE=FunctionalEq DN=Density "
          "GUE=Pairing EF=ExplicitFormula CB=CuspidalBound ST=SatoTate")

    print()
    print("=" * 80)
    print("WHAT THIS NARROWS")
    print("=" * 80)
    print()
    print("The engine now has 7 INDEPENDENT necessary conditions for an HP")
    print("candidate. Any candidate failing any of them is ruled out.")
    print()
    print("Before v0.5: 4 conditions (SM, FE, DN, GUE)")
    print("After v0.5:  7 conditions (+ EF, CB, ST)")
    print()
    print("The search space is now sharply constrained: T must satisfy")
    print("ALL of {sign-symmetric, N(T) density, GUE pairing,")
    print("explicit-formula respected, Ramanujan-bounded, Sato-Tate}")
    print()
    print("This is the MAXIMUM the engine can check WITHOUT external")
    print("cuspidal HMF data.")
    print()
    print("WHAT'S STILL MISSING (v0.6):")
    print("  - real cuspidal HMF data from LMFDB (or Magma/SAGE-dev)")
    print("  - HECKE_ISOTYPIC_EMBED: lift Hecke action onto V_600's")
    print("    26-dim block via 2I-equivariance")
    print("  - NEWFORM_LEVEL_SEARCH: systematic level/weight scan")
    print()
    print("All three are well-scoped follow-ons. The engine architecture")
    print("supports them by drop-in extension of the existing kinds and")
    print("admissibility classes.")


if __name__ == "__main__":
    main()
