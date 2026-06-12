"""v0.4 runner: hybrid probe with ICOSIAN-specific Brandt matrices.

After ~/miniconda3/bin/sage sage_scripts/compute_brandt_icosian_v04.sage
produces data/brandt_icosian.json, this script feeds it to the engine.

Runs the same hybrid probe as run_v600_hybrid_probe.py but with
icosian-native Hecke matrices instead of the level-31 over-Q proxy.

Key empirical question:
  Does the icosian-specific Hecke action push the candidate operator
  from HILBERT_POLYA_PARTIAL (achieved in v0.3) to HILBERT_POLYA_STRONG?

Three possible outcomes:
  1. STRONG verdict reached -- substrate-side Hilbert-Polya candidate.
     Publish immediately; analytical verification next.
  2. Same PARTIAL verdict as v0.3 -- the icosian distinction doesn't
     help, the wall is elsewhere. Pin down where.
  3. WORSE than v0.3 -- substrate is genuinely deficient at finite
     levels. Likely outcome given class number 1.

Any outcome is informative.
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


def main():
    print("=" * 76)
    print("v0.4 ICOSIAN-SPECIFIC HECKE PROBE")
    print("=" * 76)

    data_path = HERE.parent / "data" / "brandt_icosian.json"
    if not data_path.exists():
        print(f"\nERROR: {data_path} does not exist.")
        print("Run sage_scripts/compute_brandt_icosian_v04.sage first")
        print("(requires SAGE 10+).")
        return

    with open(data_path) as f:
        data = json.load(f)

    print(f"\nField: {data['field']}")
    print(f"Class number: {data['field_class_number']}")

    if "conclusion" in data:
        print(f"\n{data['conclusion']}")
        print()
        print("Substrate-side conclusion: at finite levels with class")
        print("number 1, the icosian Brandt action is trivial. To get")
        print("non-trivial action, we need either:")
        print("  - higher levels with composite ideal structure")
        print("  - a different quaternion algebra (e.g. ramified at")
        print("    finite primes)")
        print("  - infinite-level / asymptotic constructions")
        print()
        print("This is itself the answer the engine surfaces: the")
        print("substrate's native Hecke action at finite levels does")
        print("not produce non-trivial spectral data. The Hilbert-Polya")
        print("construction (if it exists) must come from a non-trivial")
        print("level or non-trivial twist.")
        return

    print(f"Brandt module dimension: {data['brandt_module']['dimension']}")
    print(f"Hecke operators computed: {len(data['hecke_operators'])}")
    print()

    # Aggregate eigenvalues from all icosian Hecke matrices
    print("Hecke eigenvalues per prime:")
    all_eigs = []
    for h in data["hecke_operators"]:
        M = np.array(h["matrix"], dtype=float)
        M_sym = 0.5 * (M + M.T)
        eigs = np.linalg.eigvalsh(M_sym)
        all_eigs.extend(eigs.tolist())
        print(f"  prime norm {h['prime_norm']:<4} trace={h['trace']:<6}"
              f" det={h['det']:<8} eigs={sorted(eigs.tolist())}")

    spectrum = np.array(sorted(all_eigs))
    print(f"\nTotal eigenvalues: {len(spectrum)}")
    print(f"Range: [{spectrum.min():.3f}, {spectrum.max():.3f}]")

    # Run calibrated deep checks
    candidate = np.diag(spectrum)
    summary = deepc.evaluate_calibrated(candidate)
    sm_v, sm_r, _ = adm.check_spectral_match(candidate, deepc.GAMMAS,
                                              use_abs=True)
    print(f"\nDeep admissibility verdicts:")
    print(f"  SM (spectral match):  {sm_v} (RMSE {sm_r:.4f})")
    print(f"  FE (functional eq):   "
          f"{summary['functional_equation']['verdict']}")
    print(f"  DN (density):         "
          f"{summary['density_consistent']['verdict']}")
    print(f"  GUE (spacing):        "
          f"{summary['gue_distributed']['verdict']}")
    print(f"  Overall:              {summary['overall']}")

    # Compare to v0.3 result
    print()
    print("Comparison to v0.3 (level-31 over-Q):")
    print("  v0.3: HILBERT_POLYA_PARTIAL  (FE CANDIDATE, GUE CANDIDATE)")
    print(f"  v0.4: {summary['overall']}")

    if summary["overall"] == "HILBERT_POLYA_STRONG":
        print("  -> ICOSIAN HECKE REACHES STRONG.  This is the")
        print("     substrate-localised Hilbert-Polya candidate.")
        print("     Next: high-precision Mellin verification + paper draft.")
    elif summary["overall"] == "HILBERT_POLYA_PARTIAL":
        print("  -> Same level as v0.3.  The icosian distinction doesn't")
        print("     help at this level; need higher-level / weighted")
        print("     constructions.")
    else:
        print(f"  -> {summary['overall']}: icosian-specific Hecke at this")
        print("     level is structurally deficient.  The wall is at the")
        print("     class-number-1 limit; need composite-level or twisted")
        print("     forms.")

    # Save
    out = HERE.parent / "outputs" / "icosian_hecke_v04_results.txt"
    with open(out, "w") as f:
        f.write("v0.4 icosian-specific Hecke probe\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Field: {data['field']}\n")
        if "conclusion" in data:
            f.write(f"\n{data['conclusion']}\n")
        else:
            f.write(f"Brandt dim: {data['brandt_module']['dimension']}\n")
            f.write(f"Hecke primes: {len(data['hecke_operators'])}\n\n")
            f.write(f"SM:  {sm_v} (RMSE {sm_r:.4f})\n")
            f.write(f"FE:  {summary['functional_equation']['verdict']}\n")
            f.write(f"DN:  {summary['density_consistent']['verdict']}\n")
            f.write(f"GUE: {summary['gue_distributed']['verdict']}\n")
            f.write(f"Overall: {summary['overall']}\n")


if __name__ == "__main__":
    main()
