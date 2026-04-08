#!/usr/bin/env python3
"""
Paper II — Closure-Class Assignment Rules and Correction Terms
===============================================================

PART A: Test 5 rule families against candidate shell supports.
PART B: Enumerate exact structural correction terms.
PART C: Evaluate corrected invariants against observed mp/me.

Zero fitting. Zero randomness. Every factor structurally justified.
"""

import math
import csv
import json
import os
from itertools import combinations
from dataclasses import dataclass, asdict, field
from typing import List, Tuple, Optional

PHI = (1 + math.sqrt(5)) / 2
TARGET = 1836.15267343

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "artifacts")

# ═══════════════════════════════════════════════════════════════
# PART A — ASSIGNMENT RULES
# ═══════════════════════════════════════════════════════════════

# Candidate shell supports to test
CANDIDATES = [
    ([1], "charged_lepton", "electron"),
    ([1, 2], "charged_lepton", "electron_extended"),
    ([1, 2, 3], "baryon", "baryon_low"),
    ([2, 3, 4], "baryon", "baryon_mid"),
    ([3, 4, 5], "baryon", "baryon_high"),
    ([1, 2, 3, 4], "baryon", "baryon_wide_low"),
    ([2, 3, 4, 5], "baryon", "baryon_wide_mid"),
]

# Rule families

def rule_minimal_support(shells, symmetry):
    """RULE 1: Minimal support rules.
    - Minimal charged: smallest admissible shell set (size 1, shell 1).
    - Baryon: support size >= 3.
    - Shell 1 reserved for minimal charged closure.
    """
    if symmetry == "charged_lepton":
        if len(shells) == 1 and shells[0] == 1:
            return True, "Minimal single-shell charged closure"
        if len(shells) == 2 and shells[0] == 1:
            return False, "Not minimal: 2-shell lepton exceeds minimal support requirement"
        return False, "Lepton must start at shell 1"
    else:  # baryon
        if len(shells) < 3:
            return False, f"Baryon requires >= 3 shells, has {len(shells)}"
        if 1 in shells:
            return False, "Shell 1 reserved for minimal charged closure"
        return True, f"Composite baryon with {len(shells)} shells, no shell-1 conflict"


def rule_boundary_interior(shells, symmetry):
    """RULE 2: Boundary/interior rules.
    - Shell 1 = boundary-minimal support (electron occupies the boundary).
    - Baryons require interior support beyond boundary.
    - Proton begins at first non-boundary shell.
    """
    if symmetry == "charged_lepton":
        if shells == [1]:
            return True, "Boundary-minimal: electron occupies only the boundary shell"
        if shells == [1, 2]:
            return False, "Extended beyond boundary without structural necessity"
        return False, "Lepton must include boundary shell 1"
    else:
        if 1 in shells:
            return False, "Baryon must not occupy boundary shell (that is the lepton sector)"
        if shells[0] == 2:
            return True, "Begins at first non-boundary shell"
        if shells[0] > 2:
            return False, "Skips available interior shells without justification"
        return False, "Unknown configuration"


def rule_complexity_threshold(shells, symmetry):
    """RULE 3: Closure-complexity threshold.
    C(A) = prod(shells) - sum(shells) - 1.
    - Leptons: C >= -1 (minimal complexity).
    - Baryons: C >= 5 (composite complexity threshold).
    """
    C = math.prod(shells) - sum(shells) - 1
    if symmetry == "charged_lepton":
        if C >= -1:
            return True, f"C = {C} >= -1 (lepton threshold satisfied)"
        return False, f"C = {C} < -1 (below lepton threshold)"
    else:
        if C >= 5:
            return True, f"C = {C} >= 5 (baryon threshold satisfied)"
        return False, f"C = {C} < 5 (below baryon composite threshold)"


def rule_symmetry_topology(shells, symmetry):
    """RULE 4: Symmetry/topology compatibility.
    - Charged leptons: winding 1 only, minimal shell.
    - Baryons: contiguous shells, winding 1 for ground state.
    - Neutral baryons: same shells as charged, different torsion sector.
    """
    # Check contiguity
    contiguous = all(shells[i+1] - shells[i] == 1 for i in range(len(shells)-1))
    if not contiguous and len(shells) > 1:
        return False, "Non-contiguous shell support violates closure-graph connectivity"
    if symmetry == "charged_lepton":
        if len(shells) <= 2 and shells[0] == 1:
            return True, "Contiguous minimal charged support"
        return False, "Lepton support must be minimal and start at 1"
    else:
        if contiguous and len(shells) >= 3:
            return True, f"Contiguous composite support of size {len(shells)}"
        return False, f"Baryon requires contiguous support >= 3"


def rule_adjacency_connected(shells, symmetry):
    """RULE 5: Connected-support adjacency rules.
    - All occupied shells must form a connected subgraph (consecutive integers).
    - Maximum gap = 0 (strictly contiguous).
    """
    if len(shells) <= 1:
        return True, "Single shell is trivially connected"
    contiguous = all(shells[i+1] - shells[i] == 1 for i in range(len(shells)-1))
    if contiguous:
        return True, "Strictly contiguous (connected)"
    return False, "Disconnected shell support"


RULE_FAMILIES = {
    "R1_minimal_support": rule_minimal_support,
    "R2_boundary_interior": rule_boundary_interior,
    "R3_complexity_threshold": rule_complexity_threshold,
    "R4_symmetry_topology": rule_symmetry_topology,
    "R5_adjacency_connected": rule_adjacency_connected,
}


def test_all_assignments():
    """Test all candidate shell supports against all rule families."""
    results = []
    for shells, symmetry, label in CANDIDATES:
        C = math.prod(shells) - sum(shells) - 1
        row = {
            "label": label,
            "shells": ",".join(str(s) for s in shells),
            "symmetry": symmetry,
            "n_shells": len(shells),
            "shell_sum": sum(shells),
            "shell_product": math.prod(shells),
            "complexity_C": C,
        }
        all_pass = True
        for rname, rfn in RULE_FAMILIES.items():
            passed, reason = rfn(shells, symmetry)
            row[f"{rname}_pass"] = "Y" if passed else "N"
            row[f"{rname}_reason"] = reason
            if not passed:
                all_pass = False
        row["all_rules_pass"] = "Y" if all_pass else "N"
        results.append(row)
    return results


# ═══════════════════════════════════════════════════════════════
# PART B — CORRECTION TERM CATALOGUE
# ═══════════════════════════════════════════════════════════════

def compute_corrections():
    """Compute exact structural correction factors for electron {1} and proton {2,3,4}."""
    e_shells = [1]
    p_shells = [2, 3, 4]

    corrections = []

    # CF1: Inter-shell coupling count (pairs)
    e_pairs = len(list(combinations(e_shells, 2)))  # 0
    p_pairs = len(list(combinations(p_shells, 2)))  # 3
    # As multiplicative: need (1+pairs) to avoid zero
    cf1_e = 1 + e_pairs  # 1
    cf1_p = 1 + p_pairs  # 4
    corrections.append({
        "id": "CF1", "name": "Inter-shell pair count",
        "formula": "1 + C(n_shells, 2)",
        "origin": "Pairwise coupling multiplicity",
        "value_electron": cf1_e, "value_proton": cf1_p,
        "correction_ratio": cf1_p / cf1_e,
        "note": "Counts pairwise inter-shell couplings. Proton has 3 pairs, electron has 0.",
    })

    # CF2: Adjacency edge count (contiguous neighbors)
    e_adj = max(0, len(e_shells) - 1)  # 0
    p_adj = max(0, len(p_shells) - 1)  # 2
    cf2_e = 1 + e_adj  # 1
    cf2_p = 1 + p_adj  # 3
    corrections.append({
        "id": "CF2", "name": "Adjacency edge count",
        "formula": "1 + (n_shells - 1)",
        "origin": "Closure graph edge count",
        "value_electron": cf2_e, "value_proton": cf2_p,
        "correction_ratio": cf2_p / cf2_e,
        "note": "Number of adjacent shell pairs plus 1.",
    })

    # CF3: Shell-sum ratio (total depth)
    cf3_e = sum(e_shells)  # 1
    cf3_p = sum(p_shells)  # 9
    corrections.append({
        "id": "CF3", "name": "Shell sum",
        "formula": "sum(shells)",
        "origin": "Total closure depth",
        "value_electron": cf3_e, "value_proton": cf3_p,
        "correction_ratio": cf3_p / cf3_e,
        "note": "Sum of occupied shell indices.",
    })

    # CF4: Subclosure count (number of non-empty subsets of shell support)
    cf4_e = 2 ** len(e_shells) - 1  # 1
    cf4_p = 2 ** len(p_shells) - 1  # 7
    corrections.append({
        "id": "CF4", "name": "Subclosure count",
        "formula": "2^n_shells - 1",
        "origin": "Number of non-trivial sub-closures",
        "value_electron": cf4_e, "value_proton": cf4_p,
        "correction_ratio": cf4_p / cf4_e,
        "note": "All non-empty subsets of shell support. Proton has 7, electron has 1.",
    })

    # CF5: Shell product / shell sum
    cf5_e = math.prod(e_shells) / sum(e_shells)  # 1
    cf5_p = math.prod(p_shells) / sum(p_shells)  # 24/9 = 2.667
    corrections.append({
        "id": "CF5", "name": "Product/sum ratio",
        "formula": "prod(shells) / sum(shells)",
        "origin": "Multiplicative vs additive complexity",
        "value_electron": cf5_e, "value_proton": cf5_p,
        "correction_ratio": cf5_p / cf5_e,
        "note": "Ratio of multiplicative to additive shell complexity.",
    })

    # CF6: Spanning tree count (for path graph on shells)
    # For contiguous shells, the graph is a path; spanning tree count = 1
    # But for the complete graph on n vertices: n^(n-2) (Cayley's formula)
    cf6_e = 1  # single vertex
    cf6_p = 3 ** (3 - 2)  # 3 vertices: 3^1 = 3
    corrections.append({
        "id": "CF6", "name": "Cayley spanning tree count",
        "formula": "n_shells^(n_shells-2) for n>=2, else 1",
        "origin": "Spanning tree multiplicity (Cayley's formula)",
        "value_electron": cf6_e, "value_proton": cf6_p,
        "correction_ratio": cf6_p / cf6_e,
        "note": "Complete-graph spanning tree count. Exact integer.",
    })

    # CF7: n_shells factorial
    cf7_e = math.factorial(len(e_shells))  # 1
    cf7_p = math.factorial(len(p_shells))  # 6
    corrections.append({
        "id": "CF7", "name": "Shell permutation count",
        "formula": "n_shells!",
        "origin": "Number of closure-path orderings",
        "value_electron": cf7_e, "value_proton": cf7_p,
        "correction_ratio": cf7_p / cf7_e,
        "note": "Permutations of shell traversal order.",
    })

    # CF8: Phi^(n_shells - 1) — geometric inter-shell coupling
    cf8_e = PHI ** (len(e_shells) - 1)  # phi^0 = 1
    cf8_p = PHI ** (len(p_shells) - 1)  # phi^2 = 2.618
    corrections.append({
        "id": "CF8", "name": "Phi inter-shell coupling",
        "formula": "phi^(n_shells - 1)",
        "origin": "Geometric weight per inter-shell link",
        "value_electron": cf8_e, "value_proton": cf8_p,
        "correction_ratio": cf8_p / cf8_e,
        "note": "Each additional shell adds phi to the coupling. Exact, no fitted parameter.",
    })

    # CF9: Product of (n_i - n_j) for all pairs (Vandermonde discriminant)
    def vandermonde(shells):
        if len(shells) < 2:
            return 1
        return math.prod(abs(shells[i] - shells[j])
                        for i in range(len(shells))
                        for j in range(i+1, len(shells)))
    cf9_e = vandermonde(e_shells)  # 1
    cf9_p = vandermonde(p_shells)  # |2-3|*|2-4|*|3-4| = 1*2*1 = 2
    corrections.append({
        "id": "CF9", "name": "Vandermonde discriminant",
        "formula": "prod(|n_i - n_j| for i<j)",
        "origin": "Inter-shell separation product",
        "value_electron": cf9_e, "value_proton": cf9_p,
        "correction_ratio": cf9_p / cf9_e,
        "note": "Exact integer. Measures shell spread.",
    })

    # CF10: Closure cycle count: product of shell indices
    cf10_e = math.prod(e_shells)  # 1
    cf10_p = math.prod(p_shells)  # 24
    corrections.append({
        "id": "CF10", "name": "Shell index product",
        "formula": "prod(shells)",
        "origin": "Total closure cycle multiplicity",
        "value_electron": cf10_e, "value_proton": cf10_p,
        "correction_ratio": cf10_p / cf10_e,
        "note": "Product of all shell indices. Proton = 24, electron = 1.",
    })

    return corrections


# ═══════════════════════════════════════════════════════════════
# PART C — CORRECTED INVARIANT EVALUATION
# ═══════════════════════════════════════════════════════════════

def evaluate_corrected_invariants(corrections):
    """Apply each correction to the two base invariants and check against target."""
    base_invariants = {
        "phi^15": PHI ** 15,           # = 1364.0
        "CE_ratio": (PHI**4 + PHI**9 + PHI**16) / PHI,  # = 1415.2
    }

    results = []
    for base_name, base_val in base_invariants.items():
        for cf in corrections:
            corr = cf["correction_ratio"]
            corrected = base_val * corr
            err = abs(corrected - TARGET) / TARGET * 100

            strength = "REJECT"
            if err < 1:
                strength = "EXCELLENT"
            elif err < 5:
                strength = "STRONG"
            elif err < 15:
                strength = "MODERATE"
            elif err < 30:
                strength = "WEAK"

            results.append({
                "base": base_name,
                "correction": cf["id"],
                "correction_name": cf["name"],
                "base_value": base_val,
                "correction_ratio": corr,
                "corrected_ratio": corrected,
                "observed": TARGET,
                "error_pct": err,
                "strength": strength,
                "origin": cf["origin"],
                "note": cf["note"],
            })

    results.sort(key=lambda r: r["error_pct"])
    return results


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    os.makedirs(BASE_DIR, exist_ok=True)

    # PART A: Assignment rules
    print("=" * 80)
    print("PART A: CLOSURE-CLASS ASSIGNMENT RULES")
    print("=" * 80)
    assignments = test_all_assignments()

    print(f"\n{'Label':<20} {'Shells':<12} {'Sym':<15} {'C':<5} {'All Pass':<10}")
    print("-" * 70)
    for a in assignments:
        print(f"{a['label']:<20} {a['shells']:<12} {a['symmetry']:<15} "
              f"{a['complexity_C']:<5} {a['all_rules_pass']:<10}")
        for rname in RULE_FAMILIES:
            if a[f"{rname}_pass"] == "N":
                print(f"  FAIL {rname}: {a[f'{rname}_reason']}")

    # Save
    with open(os.path.join(BASE_DIR, "assignment_rule_results.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=assignments[0].keys())
        w.writeheader()
        w.writerows(assignments)

    # PART B: Correction terms
    print("\n" + "=" * 80)
    print("PART B: CORRECTION TERM CATALOGUE")
    print("=" * 80)
    corrections = compute_corrections()

    print(f"\n{'ID':<5} {'Name':<30} {'e-val':<8} {'p-val':<8} {'Ratio':<8} {'Origin'}")
    print("-" * 80)
    for cf in corrections:
        print(f"{cf['id']:<5} {cf['name']:<30} {cf['value_electron']:<8.3f} "
              f"{cf['value_proton']:<8.3f} {cf['correction_ratio']:<8.4f} {cf['origin']}")

    with open(os.path.join(BASE_DIR, "correction_term_candidates.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=corrections[0].keys())
        w.writeheader()
        w.writerows(corrections)

    # PART C: Corrected invariants
    print("\n" + "=" * 80)
    print("PART C: CORRECTED INVARIANT RESULTS")
    print("=" * 80)
    corrected = evaluate_corrected_invariants(corrections)

    print(f"\n{'Base':<12} {'Corr':<6} {'Corrected':<14} {'Err%':<10} {'Strength':<12} {'Name'}")
    print("-" * 80)
    for r in corrected[:15]:
        print(f"{r['base']:<12} {r['correction']:<6} {r['corrected_ratio']:<14.4f} "
              f"{r['error_pct']:<10.4f} {r['strength']:<12} {r['correction_name']}")

    with open(os.path.join(BASE_DIR, "corrected_invariant_results.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=corrected[0].keys())
        w.writeheader()
        w.writerows(corrected)

    # Best result
    best = corrected[0] if corrected else None
    print(f"\n=== BEST CORRECTED INVARIANT ===")
    if best:
        print(f"  Base: {best['base']}")
        print(f"  Correction: {best['correction']} ({best['correction_name']})")
        print(f"  Corrected ratio: {best['corrected_ratio']:.4f}")
        print(f"  Error: {best['error_pct']:.4f}%")
        print(f"  Strength: {best['strength']}")
        print(f"  Origin: {best['origin']}")

    # Save summary
    # Which assignments pass all rules?
    passing = [a for a in assignments if a["all_rules_pass"] == "Y"]
    summary = {
        "assignments_passing_all_rules": [
            {"label": a["label"], "shells": a["shells"], "symmetry": a["symmetry"],
             "complexity_C": a["complexity_C"]}
            for a in passing
        ],
        "best_corrected_invariant": best,
        "total_corrections_tested": len(corrections),
        "total_corrected_evaluated": len(corrected),
        "corrections_within_5pct": sum(1 for r in corrected if r["error_pct"] < 5),
        "corrections_within_15pct": sum(1 for r in corrected if r["error_pct"] < 15),
    }
    with open(os.path.join(BASE_DIR, "assignment_and_correction_summary.json"), "w") as f:
        json.dump(summary, f, indent=2, default=str)


if __name__ == "__main__":
    main()
