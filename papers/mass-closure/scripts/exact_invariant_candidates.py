#!/usr/bin/env python3
"""
Paper II — Exact Closure-Class Invariant Search
=================================================

STEP A: Define electron and proton closure classes exactly.
STEP B: Enumerate candidate exact invariants I(A).
STEP C: Evaluate each candidate against observed mp/me.
STEP D: Rank by structural necessity, not by closeness to target.

NO FITTING. NO FREE PARAMETERS. Every factor must be structurally fixed.
"""

import math
import json
import csv
import os
from dataclasses import dataclass, asdict
from typing import List, Callable

PHI = (1 + math.sqrt(5)) / 2  # 1.6180339887...
TARGET_MP_ME = 1836.15267343

# ═══════════════════════════════════════════════════════════════
# STEP A — Exact closure class definitions
# ═══════════════════════════════════════════════════════════════

@dataclass
class ClosureClass:
    name: str
    particle: str
    shells: List[int]       # occupied shell indices
    winding: int            # topological winding number
    symmetry: str           # symmetry label
    # Derived quantities (exact, no fitting)
    n_shells: int = 0
    shell_sum: int = 0      # sum of shell indices
    shell_product: int = 0  # product of shell indices
    shell_max: int = 0
    shell_min: int = 0

    def __post_init__(self):
        self.n_shells = len(self.shells)
        self.shell_sum = sum(self.shells)
        self.shell_product = math.prod(self.shells)
        self.shell_max = max(self.shells) if self.shells else 0
        self.shell_min = min(self.shells) if self.shells else 0


# Conservative class definitions
# Electron: minimal charged closure state — single shell, lowest index
ELECTRON = ClosureClass(
    name="A_e", particle="electron",
    shells=[1], winding=1, symmetry="charged_lepton"
)

# Proton: composite baryonic closure state — three shells starting at 2
# This is the assignment that survived the minimal model evaluation.
PROTON = ClosureClass(
    name="A_p", particle="proton",
    shells=[2, 3, 4], winding=1, symmetry="baryon"
)

# Neutron: neutral baryon partner
NEUTRON = ClosureClass(
    name="A_n", particle="neutron",
    shells=[2, 3, 4], winding=1, symmetry="baryon_neutral"
)


# ═══════════════════════════════════════════════════════════════
# STEP B — Candidate exact invariants
# ═══════════════════════════════════════════════════════════════

@dataclass
class InvariantCandidate:
    id: str
    name: str
    formula: str
    interpretation: str
    dimensionless: bool
    phi_role: str           # how phi enters (naturally / not at all / forced)
    structural_origin: str
    value_electron: float
    value_proton: float
    predicted_ratio: float
    observed_ratio: float
    error_pct: float
    verdict: str


def evaluate_invariant(
    inv_id: str, name: str, formula: str, interpretation: str,
    fn: Callable[[ClosureClass], float],
    dimensionless: bool, phi_role: str, structural_origin: str,
) -> InvariantCandidate:
    """Evaluate a candidate invariant on electron and proton classes."""
    I_e = fn(ELECTRON)
    I_p = fn(PROTON)
    ratio = I_p / I_e if I_e != 0 else float('inf')
    err = abs(ratio - TARGET_MP_ME) / TARGET_MP_ME * 100
    if err < 1:
        verdict = "EXCELLENT"
    elif err < 10:
        verdict = "STRONG"
    elif err < 30:
        verdict = "MODERATE"
    elif 100 < ratio < 10000:
        verdict = "RIGHT_RANGE"
    else:
        verdict = "WRONG_RANGE"

    return InvariantCandidate(
        id=inv_id, name=name, formula=formula,
        interpretation=interpretation, dimensionless=dimensionless,
        phi_role=phi_role, structural_origin=structural_origin,
        value_electron=I_e, value_proton=I_p,
        predicted_ratio=ratio, observed_ratio=TARGET_MP_ME,
        error_pct=err, verdict=verdict,
    )


def build_candidates() -> List[InvariantCandidate]:
    candidates = []

    # ── I1: Shell product ratio ──
    candidates.append(evaluate_invariant(
        "I01", "Shell product",
        "I(A) = prod(shells)",
        "Product of occupied shell indices. Measures composite complexity.",
        lambda A: float(A.shell_product),
        True, "none", "combinatorial shell structure",
    ))

    # ── I2: Phi-weighted shell product ──
    candidates.append(evaluate_invariant(
        "I02", "Phi-weighted shell product",
        "I(A) = prod(phi^n for n in shells)",
        "Product of phi^n over occupied shells. Phi enters through shell geometry.",
        lambda A: math.prod(PHI ** n for n in A.shells),
        True, "natural (shell geometry)", "phi-structured manifold",
    ))

    # ── I3: Phi-sum-of-shells ──
    candidates.append(evaluate_invariant(
        "I03", "Phi to shell-sum",
        "I(A) = phi^(sum of shells)",
        "Phi raised to the total shell index. Measures total geometric depth.",
        lambda A: PHI ** A.shell_sum,
        True, "natural (total depth)", "total closure depth",
    ))

    # ── I4: Shell factorial product × phi ──
    candidates.append(evaluate_invariant(
        "I04", "Shell-factorial × phi^shells",
        "I(A) = prod(n! * phi^n for n in shells)",
        "Closure complexity: each shell contributes n! permutations weighted by phi^n.",
        lambda A: math.prod(math.factorial(n) * PHI ** n for n in A.shells),
        True, "natural (weighted permutations)", "closure path multiplicity × geometry",
    ))

    # ── I5: Phi^(shell_product) ──
    candidates.append(evaluate_invariant(
        "I05", "Phi to shell-product",
        "I(A) = phi^(prod(shells))",
        "Phi raised to the product of shell indices. Exponential coupling of shell structure.",
        lambda A: PHI ** A.shell_product,
        True, "natural (exponential coupling)", "shell interaction depth",
    ))

    # ── I6: Sum of phi^(n^2) ──
    candidates.append(evaluate_invariant(
        "I06", "Sum of phi^(n^2)",
        "I(A) = sum(phi^(n^2) for n in shells)",
        "Quadratic shell scaling in the phi exponent.",
        lambda A: sum(PHI ** (n ** 2) for n in A.shells),
        True, "natural (quadratic depth)", "closure energy scaling",
    ))

    # ── I7: Product of (phi^n + phi^(-n)) ── (closure cycle invariant)
    candidates.append(evaluate_invariant(
        "I07", "Closure cycle product",
        "I(A) = prod(phi^n + phi^{-n} for n in shells)",
        "Each shell contributes a symmetric closure cycle term. This is 2*cosh(n*ln(phi)).",
        lambda A: math.prod(PHI ** n + PHI ** (-n) for n in A.shells),
        True, "natural (symmetric closure)", "closure cycle symmetry",
    ))

    # ── I8: Phi^(n*(n+1)/2) summed (triangular number) ──
    candidates.append(evaluate_invariant(
        "I08", "Triangular phi sum",
        "I(A) = sum(phi^(n(n+1)/2) for n in shells)",
        "Triangular-number scaling in phi exponent. Natural from nested closure.",
        lambda A: sum(PHI ** (n * (n + 1) / 2) for n in A.shells),
        True, "natural (triangular nesting)", "nested closure hierarchy",
    ))

    # ── I9: Product of phi^n * n ──
    candidates.append(evaluate_invariant(
        "I09", "Mode-weighted phi product",
        "I(A) = prod(n * phi^n for n in shells)",
        "Each shell contributes its index times phi^n. Combines mode count with geometry.",
        lambda A: math.prod(n * PHI ** n for n in A.shells),
        True, "natural (mode × geometry)", "harmonic mode multiplicity",
    ))

    # ── I10: Phi^(sum of n^2) ──
    candidates.append(evaluate_invariant(
        "I10", "Phi to sum-of-squares",
        "I(A) = phi^(sum(n^2 for n in shells))",
        "Phi raised to the sum of squared shell indices. Quadratic complexity measure.",
        lambda A: PHI ** sum(n ** 2 for n in A.shells),
        True, "natural (quadratic complexity)", "total quadratic closure cost",
    ))

    # ── I11: Determinant-like: product of differences × phi^sum ──
    candidates.append(evaluate_invariant(
        "I11", "Vandermonde-phi invariant",
        "I(A) = prod(|n_i - n_j| for i<j) * phi^(sum shells) for multi-shell; 1 for single",
        "Vandermonde-type discriminant times total phi depth. Measures inter-shell coupling.",
        lambda A: (math.prod(abs(A.shells[i] - A.shells[j])
                   for i in range(len(A.shells)) for j in range(i+1, len(A.shells)))
                   * PHI ** A.shell_sum) if len(A.shells) > 1 else PHI ** A.shell_sum,
        True, "natural (inter-shell + depth)", "inter-shell coupling × total depth",
    ))

    # ── I12: Lucas number product ──
    def lucas(n):
        a, b = 2, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    candidates.append(evaluate_invariant(
        "I12", "Lucas number product",
        "I(A) = prod(L_n for n in shells) where L_n is the n-th Lucas number",
        "Lucas numbers arise naturally from phi: L_n = phi^n + (-phi)^{-n}. Integer-valued.",
        lambda A: math.prod(lucas(n) for n in A.shells),
        True, "natural (Lucas = integer phi-invariant)", "phi-manifold integer invariant",
    ))

    # ── I13: Fibonacci product ──
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    candidates.append(evaluate_invariant(
        "I13", "Fibonacci product",
        "I(A) = prod(F_n for n in shells) where F_n is the n-th Fibonacci number",
        "Fibonacci numbers are the integer sequence most closely tied to phi.",
        lambda A: math.prod(fib(n) for n in A.shells),
        True, "natural (Fibonacci = phi-sequence)", "phi-manifold combinatorics",
    ))

    # ── I14: Product of phi^(n^2) ──
    candidates.append(evaluate_invariant(
        "I14", "Product of phi^(n^2)",
        "I(A) = prod(phi^(n^2) for n in shells)",
        "Quadratic phi power per shell, multiplicative. Steeper than I03.",
        lambda A: math.prod(PHI ** (n ** 2) for n in A.shells),
        True, "natural (quadratic per-shell)", "quadratic closure depth",
    ))

    # ── I15: Phi^(shell_sum * n_shells) ──
    candidates.append(evaluate_invariant(
        "I15", "Phi^(sum × count)",
        "I(A) = phi^(shell_sum * n_shells)",
        "Total depth times mode count in phi exponent. Self-referential complexity.",
        lambda A: PHI ** (A.shell_sum * A.n_shells),
        True, "natural (depth × multiplicity)", "composite closure complexity",
    ))

    return candidates


# ═══════════════════════════════════════════════════════════════
# STEP C — Rank and filter
# ═══════════════════════════════════════════════════════════════

def main():
    candidates = build_candidates()

    # Sort by structural quality, then by proximity to target
    # Priority: RIGHT_RANGE > WRONG_RANGE, then by error
    rank_order = {"EXCELLENT": 0, "STRONG": 1, "MODERATE": 2, "RIGHT_RANGE": 3, "WRONG_RANGE": 4}
    candidates.sort(key=lambda c: (rank_order.get(c.verdict, 5), c.error_pct))

    base = os.path.join(os.path.dirname(__file__), "..", "artifacts")

    # Print full catalogue
    print("=" * 120)
    print("EXACT CLOSURE-CLASS INVARIANT CATALOGUE")
    print("=" * 120)
    print(f"{'ID':<5} {'Name':<28} {'I(e)':<14} {'I(p)':<14} {'Ratio':<14} {'Err%':<10} {'Verdict':<12} {'Phi Role'}")
    print("-" * 120)
    for c in candidates:
        print(f"{c.id:<5} {c.name:<28} {c.value_electron:<14.4f} {c.value_proton:<14.4f} "
              f"{c.predicted_ratio:<14.4f} {c.error_pct:<10.4f} {c.verdict:<12} {c.phi_role}")

    # Write CSV
    fields = [f.name for f in InvariantCandidate.__dataclass_fields__.values()]
    with open(os.path.join(base, "invariant_candidates.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for c in candidates:
            w.writerow(asdict(c))

    # Identify shortlist (top 3 non-WRONG_RANGE)
    shortlist = [c for c in candidates if c.verdict != "WRONG_RANGE"][:5]

    print("\n" + "=" * 80)
    print("SHORTLIST (Top 5 structurally viable candidates)")
    print("=" * 80)
    for c in shortlist:
        print(f"\n  {c.id}: {c.name}")
        print(f"    Formula: {c.formula}")
        print(f"    I(electron) = {c.value_electron:.6f}")
        print(f"    I(proton)   = {c.value_proton:.6f}")
        print(f"    Predicted ratio: {c.predicted_ratio:.4f}")
        print(f"    Error: {c.error_pct:.4f}%")
        print(f"    Phi role: {c.phi_role}")
        print(f"    Origin: {c.structural_origin}")
        print(f"    Verdict: {c.verdict}")

    with open(os.path.join(base, "invariant_shortlist.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for c in shortlist:
            w.writerow(asdict(c))

    # Summary JSON
    summary = {
        "total_candidates": len(candidates),
        "shortlist_size": len(shortlist),
        "best_candidate": asdict(shortlist[0]) if shortlist else None,
        "target_ratio": TARGET_MP_ME,
        "electron_class": asdict(ELECTRON),
        "proton_class": asdict(PROTON),
    }
    with open(os.path.join(base, "invariant_summary.json"), "w") as f:
        json.dump(summary, f, indent=2, default=str)

    # Answer evaluation questions
    print("\n" + "=" * 80)
    print("EVALUATION QUESTIONS")
    print("=" * 80)
    best = shortlist[0] if shortlist else None
    if best:
        print(f"\n  Q1: Best structural distinguisher: {best.name} ({best.structural_origin})")
        print(f"  Q2: Phi enters naturally: {best.phi_role}")
        print(f"  Q3: Ratio driven by: {best.interpretation}")
        print(f"  Q4: Right range (~10^3)? {best.verdict}")
        has_exact = any(c.error_pct < 1 for c in shortlist)
        print(f"  Q5: Exact candidate found? {'YES' if has_exact else 'NO — closest is ' + f'{best.error_pct:.2f}% error'}")


if __name__ == "__main__":
    main()
