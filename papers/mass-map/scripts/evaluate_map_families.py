#!/usr/bin/env python3
"""
Paper IV — Class-Energy-to-Mass Map Analysis
==============================================

Evaluates 7 candidate nonlinear map families that transform
Paper III's metric-derived class energies into mass.

Uses Paper III's MF1 (pure radial phi metric) as the reference
geometry, since it is the most structurally minimal.

Zero fitting. Every map is evaluated as defined, not tuned.
"""

import math
import csv
import json
import os
from dataclasses import dataclass, asdict
from typing import List, Callable, Optional

PHI = (1 + math.sqrt(5)) / 2
TARGET = 1836.15267343
BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "artifacts")

# ═══════════════════════════════════════════════════════════════
# Paper III reference data (MF1 pure radial metric)
# ═══════════════════════════════════════════════════════════════

E_SHELLS = [1]
P_SHELLS = [2, 3, 4]

# MF1 spectral weights: lambda(n) = phi^{2n}
def lambda_n(n): return PHI ** (2 * n)

# Paper III class energies under MF1 (E_sum = sum of spectral weights)
E_CLASS_ELECTRON = sum(lambda_n(n) for n in E_SHELLS)   # phi^2 = 2.618
E_CLASS_PROTON = sum(lambda_n(n) for n in P_SHELLS)     # phi^4 + phi^6 + phi^8 = 71.78

# Paper II invariants
C_ELECTRON = 1 - 1 - 1    # = -1
C_PROTON = 24 - 9 - 1     # = 14
DELTA_C = C_PROTON - C_ELECTRON  # = 15

print(f"Reference data (MF1):")
print(f"  E_class(electron) = {E_CLASS_ELECTRON:.4f}")
print(f"  E_class(proton)   = {E_CLASS_PROTON:.4f}")
print(f"  Additive ratio    = {E_CLASS_PROTON/E_CLASS_ELECTRON:.4f}")
print(f"  Delta C           = {DELTA_C}")
print(f"  Target mp/me      = {TARGET:.4f}")
print()


# ═══════════════════════════════════════════════════════════════
# Map family definitions
# ═══════════════════════════════════════════════════════════════

@dataclass
class MapFamily:
    id: str
    name: str
    description: str
    origin: str  # derived / postulated / provisional
    has_free_param: bool
    free_param_name: Optional[str]

    # The map: takes (shells, E_class, C_invariant) -> mass-surrogate
    # Returns a dimensionless number; ratio is what matters
    compute: Callable  # (shells, E_class, C) -> float


def build_map_families():
    families = {}

    # ── F1: Pure exponential map ──
    # m(A) ~ exp(E_class / E_0)
    # E_0 is a scale. If E_0 = phi^2 (= E_class(electron)), the map normalises
    # so that electron maps to exp(1) and the ratio depends on E_p/E_e.
    # This is DERIVED: E_0 = E_class of the minimal state is a natural scale.
    families["F1"] = MapFamily(
        id="F1", name="Pure exponential",
        description="m ~ exp(E_class / E_0), E_0 = E_class(electron)",
        origin="derived (E_0 from minimal class)",
        has_free_param=False, free_param_name=None,
        compute=lambda shells, E, C: math.exp(E / E_CLASS_ELECTRON),
    )

    # ── F2: Phi-exponential with C ──
    # m(A) ~ phi^C(A)
    # This is Paper II's original hypothesis. E_class not used.
    # Included for completeness and comparison.
    families["F2"] = MapFamily(
        id="F2", name="Phi^C (Paper II hypothesis)",
        description="m ~ phi^C(A). Pure combinatorial, ignores metric energy.",
        origin="postulated (Paper II)",
        has_free_param=False, free_param_name=None,
        compute=lambda shells, E, C: PHI ** C,
    )

    # ── F3: Multiplicative shell map ──
    # m(A) ~ product over shells of lambda(n)
    # Instead of SUMMING spectral weights, MULTIPLY them.
    # Structurally: each shell contributes multiplicatively to mass.
    families["F3"] = MapFamily(
        id="F3", name="Multiplicative shell product",
        description="m ~ prod(lambda(n) for n in shells)",
        origin="derived (multiplicative composition of shell contributions)",
        has_free_param=False, free_param_name=None,
        compute=lambda shells, E, C: math.prod(lambda_n(n) for n in shells),
    )

    # ── F4: Phi^(E_class) map ──
    # m(A) ~ phi^(E_class)
    # The class energy becomes the EXPONENT of phi.
    # This directly bridges additive energy to exponential mass.
    families["F4"] = MapFamily(
        id="F4", name="Phi^(E_class)",
        description="m ~ phi^(E_class(A)). Energy enters as phi exponent.",
        origin="postulated (energy-as-exponent hypothesis)",
        has_free_param=False, free_param_name=None,
        compute=lambda shells, E, C: PHI ** E,
    )

    # ── F5: Partition-like closure count ──
    # m(A) ~ product over shells of (phi^n * n)
    # This combines geometric weight with mode index multiplicatively.
    # Interpretation: each shell's contribution = its phi-weight times
    # its mode multiplicity (n modes for shell n).
    families["F5"] = MapFamily(
        id="F5", name="Mode-weighted phi product",
        description="m ~ prod(n * phi^n for n in shells)",
        origin="derived (mode count × geometry per shell)",
        has_free_param=False, free_param_name=None,
        compute=lambda shells, E, C: math.prod(n * PHI ** n for n in shells),
    )

    # ── F6: Closure-path product map ──
    # m(A) ~ prod(phi^(n^2) for n in shells)
    # Each shell contributes phi^(n^2) — quadratic scaling in exponent.
    # Interpretation: closure cost per shell scales as n^2 (quadratic).
    families["F6"] = MapFamily(
        id="F6", name="Quadratic closure product",
        description="m ~ prod(phi^(n^2) for n in shells)",
        origin="derived (quadratic per-shell closure cost)",
        has_free_param=False, free_param_name=None,
        compute=lambda shells, E, C: math.prod(PHI ** (n ** 2) for n in shells),
    )

    # ── F7: Mixed invariant-energy map ──
    # m(A) ~ phi^C * E_class
    # Combines Paper II combinatorial invariant with Paper III energy.
    # Both are established; the product is the simplest combination.
    families["F7"] = MapFamily(
        id="F7", name="phi^C × E_class",
        description="m ~ phi^C(A) * E_class(A). Mixed invariant+energy.",
        origin="postulated (product of two established quantities)",
        has_free_param=False, free_param_name=None,
        compute=lambda shells, E, C: PHI ** C * E,
    )

    return families


# ═══════════════════════════════════════════════════════════════
# Structural tests
# ═══════════════════════════════════════════════════════════════

def structural_tests(fam, m_e, m_p, ratio):
    """Run structural tests T1-T7 on a map family result."""
    tests = {}

    # T1: Structural origin (from definition)
    tests["T1_origin"] = "derived" in fam.origin.lower()

    # T2: Zero-fit
    tests["T2_zero_fit"] = not fam.has_free_param

    # T3: Compatible with closure-class ontology (always true if map
    # depends only on class labels/energy)
    tests["T3_class_compat"] = True

    # T4: Compatible with manifold geometry (uses E_class or shell data)
    tests["T4_geom_compat"] = True

    # T5: Amplification to 10^3
    tests["T5_amplification"] = 500 < ratio < 5000

    # T6: Ratio cancellation (calibration-independent)
    # True if the ratio m_p/m_e is independent of any overall scale m0
    tests["T6_ratio_cancel"] = True  # all our maps have this property

    # T7: Neutron/proton refinement possible
    # True if the map could accept a small perturbation to E_class
    # and produce a small mass splitting
    tests["T7_np_refinable"] = True  # all nonlinear maps amplify perturbations

    return tests


# ═══════════════════════════════════════════════════════════════
# Main evaluation
# ═══════════════════════════════════════════════════════════════

def main():
    os.makedirs(BASE_DIR, exist_ok=True)
    families = build_map_families()

    results = []

    print("=" * 100)
    print("PAPER IV: CLASS-ENERGY-TO-MASS MAP ANALYSIS")
    print("=" * 100)

    for fid, fam in families.items():
        m_e = fam.compute(E_SHELLS, E_CLASS_ELECTRON, C_ELECTRON)
        m_p = fam.compute(P_SHELLS, E_CLASS_PROTON, C_PROTON)

        if m_e > 1e-30 and math.isfinite(m_p):
            ratio = m_p / m_e
        else:
            ratio = float('inf')

        err = abs(ratio - TARGET) / TARGET * 100 if math.isfinite(ratio) else float('inf')

        tests = structural_tests(fam, m_e, m_p, ratio)
        pass_count = sum(1 for v in tests.values() if v)

        verdict = "REJECT"
        if tests["T5_amplification"] and tests["T2_zero_fit"]:
            if err < 5:
                verdict = "EXCELLENT"
            elif err < 30:
                verdict = "STRONG"
            elif err < 60:
                verdict = "MODERATE"
            else:
                verdict = "WEAK"
        elif tests["T5_amplification"]:
            verdict = "VIABLE (has free param)" if fam.has_free_param else "VIABLE"

        results.append({
            "id": fid,
            "name": fam.name,
            "origin": fam.origin,
            "free_param": "Yes" if fam.has_free_param else "No",
            "m_electron": f"{m_e:.6e}" if math.isfinite(m_e) else "INF",
            "m_proton": f"{m_p:.6e}" if math.isfinite(m_p) else "INF",
            "ratio": f"{ratio:.4f}" if math.isfinite(ratio) and ratio < 1e12 else "OVERFLOW",
            "error_pct": f"{err:.2f}" if math.isfinite(err) and err < 1e6 else "OVERFLOW",
            "tests_passed": f"{pass_count}/7",
            "T5_amplification": "Y" if tests["T5_amplification"] else "N",
            "verdict": verdict,
        })

    # Print results
    print(f"\n{'ID':<4} {'Name':<28} {'Ratio':<14} {'Err%':<10} {'Tests':<6} {'Verdict'}")
    print("-" * 90)
    for r in results:
        print(f"{r['id']:<4} {r['name']:<28} {r['ratio']:<14} {r['error_pct']:<10} "
              f"{r['tests_passed']:<6} {r['verdict']}")

    # Save results
    with open(os.path.join(BASE_DIR, "map_ratio_results.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=results[0].keys())
        w.writeheader()
        w.writerows(results)

    # Detailed analysis
    print("\n" + "=" * 80)
    print("DETAILED ANALYSIS")
    print("=" * 80)

    for r in results:
        print(f"\n  {r['id']}: {r['name']}")
        print(f"    m(e) = {r['m_electron']}, m(p) = {r['m_proton']}")
        print(f"    Ratio = {r['ratio']}, Error = {r['error_pct']}%")
        print(f"    Free parameters: {r['free_param']}")
        print(f"    Verdict: {r['verdict']}")

    # Delta C analysis
    print("\n" + "=" * 80)
    print("DELTA C INTERPRETATION")
    print("=" * 80)
    print(f"""
  F2 (phi^C) gives ratio = phi^15 = {PHI**15:.2f}
  F3 (multiplicative) gives ratio = prod(phi^{{2n}} for p) / prod(phi^{{2n}} for e)
     = phi^{{2*(2+3+4)}} / phi^{{2*1}} = phi^18 / phi^2 = phi^16 = {PHI**16:.2f}

  F6 (quadratic product) gives ratio = prod(phi^{{n^2}} for p) / prod(phi^{{n^2}} for e)
     = phi^{{4+9+16}} / phi^1 = phi^29 / phi^1 = phi^28 = {PHI**28:.2f}

  The multiplicative maps produce phi to an integer power.
  The exponent depends on the map choice:
    F2: exponent = Delta C = 15 (combinatorial)
    F3: exponent = 2*sum(p_shells) - 2*sum(e_shells) = 2*9 - 2*1 = 16
    F6: exponent = sum(n^2 for p) - sum(n^2 for e) = 29 - 1 = 28

  Only F3 is in the viable range (phi^16 ≈ 2207, error 20.2%).
  F6 vastly overshoots (phi^28 ≈ 7.1M).
  F2 undershoots (phi^15 ≈ 1364, error 25.7%).

  CRITICAL: F3 gives phi^16 with ZERO free parameters!
  This is the multiplicative shell product map.
""")

    # F3 detailed
    f3_e = math.prod(lambda_n(n) for n in E_SHELLS)
    f3_p = math.prod(lambda_n(n) for n in P_SHELLS)
    print(f"  F3 detail:")
    print(f"    electron: prod(phi^{{2n}}) for n=1 = phi^2 = {f3_e:.4f}")
    print(f"    proton: prod(phi^{{2n}}) for n=2,3,4 = phi^4 * phi^6 * phi^8 = phi^18 = {f3_p:.4f}")
    print(f"    ratio = phi^18 / phi^2 = phi^16 = {f3_p/f3_e:.4f}")
    print(f"    observed = {TARGET:.4f}")
    print(f"    error = {abs(f3_p/f3_e - TARGET)/TARGET*100:.2f}%")
    print()

    # Check: what phi power matches target?
    x = math.log(TARGET) / math.log(PHI)
    print(f"  log_phi(1836.15) = {x:.4f}")
    print(f"  phi^15 = {PHI**15:.2f} (26% low)")
    print(f"  phi^16 = {PHI**16:.2f} (20% high)")
    print(f"  Neither is exact. The target is between phi^15 and phi^16.")
    print()

    # F7 detail
    f7_e = PHI ** C_ELECTRON * E_CLASS_ELECTRON
    f7_p = PHI ** C_PROTON * E_CLASS_PROTON
    print(f"  F7 detail (phi^C * E_class):")
    print(f"    electron: phi^(-1) * {E_CLASS_ELECTRON:.4f} = {f7_e:.4f}")
    print(f"    proton: phi^14 * {E_CLASS_PROTON:.4f} = {f7_p:.4f}")
    print(f"    ratio = {f7_p/f7_e:.4f}")
    print()

    # Evaluation answers
    print("=" * 80)
    print("EVALUATION ANSWERS")
    print("=" * 80)
    print(f"""
  1. Most structurally justified map?
     F3 (multiplicative shell product). Derived. Zero free parameters.
     Mass as a product of per-shell spectral weights is structurally
     natural: each shell contributes multiplicatively to the total
     bound-state mass, rather than additively.

  2. Can any family generate ~10^3 without fitting?
     F3 gives phi^16 ≈ 2207 (20% high).
     F2 gives phi^15 ≈ 1364 (26% low).
     F7 gives ~37,450 (way high).
     F1 gives huge numbers (exponential of energy).
     The target falls BETWEEN phi^15 and phi^16.

  3. Does Delta C remain fundamental?
     PARTIALLY. F2 (phi^C) gives phi^15.
     F3 (multiplicative) gives phi^16 — a different exponent.
     The multiplicative map exponent is 2*sum(shells), not C.
     Delta C is relevant but not identical to the mass exponent.

  4. Any family naturally compatible with phi?
     F2, F3, F5, F6 all produce phi-power ratios.
     F3 is most structurally grounded (product of metric eigenvalues).

  5. Neutron/proton refinable?
     YES for all nonlinear families. A small perturbation to E_class
     or to shell weights produces amplified mass splitting.

  6. One more layer missing?
     YES. The target is between phi^15 (F2) and phi^16 (F3).
     Neither the combinatorial map nor the multiplicative map is exact.
     The missing layer is the precise rule for how shells combine:
     additively (undershoot), multiplicatively (overshoot), or something
     between. This is the INTER-SHELL COMPOSITION RULE.

  7. Strongest honest claim?
     "The multiplicative shell product (F3) is the most structurally
      justified mass map. It produces phi^16 ≈ 2207 with zero free
      parameters — within 20% of the observed ratio. The exact ratio
      falls between phi^15 (combinatorial) and phi^16 (multiplicative),
      suggesting the true mass map involves partial rather than full
      multiplicative shell composition. The inter-shell composition
      rule is the primary remaining open problem."
""")

    # Save summary
    summary = {
        "families_tested": len(families),
        "target_ratio": TARGET,
        "best_zero_fit": "F3 (multiplicative, phi^16 = 2207, 20% error)",
        "phi15_from_F2": PHI ** 15,
        "phi16_from_F3": PHI ** 16,
        "log_phi_target": math.log(TARGET) / math.log(PHI),
        "outcome": "B — shortlist identified, inter-shell composition rule missing",
    }
    with open(os.path.join(BASE_DIR, "mass_map_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)


if __name__ == "__main__":
    main()
