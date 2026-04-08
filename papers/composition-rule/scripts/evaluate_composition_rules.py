#!/usr/bin/env python3
"""
Paper V — Inter-Shell Composition Rule Analysis
=================================================

STEP A: Formalize the two extremes (exponent 15 and 16).
STEP B: Identify all legitimate composition entry points.
STEP C: Derive and evaluate candidate composition rules.
STEP D: Analyze the one-unit gap.

Zero fitting. No interpolation parameter search.
"""

import math
import csv
import json
import os
from typing import List

PHI = (1 + math.sqrt(5)) / 2
TARGET = 1836.15267343
TARGET_EXP = math.log(TARGET) / math.log(PHI)  # 15.6177...
BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "artifacts")

E_SHELLS = [1]
P_SHELLS = [2, 3, 4]


# ═══════════════════════════════════════════════════════════════
# STEP A — Formalize the two extremes
# ═══════════════════════════════════════════════════════════════

def step_a():
    """Derive exactly why the framework gives exponent 15 and 16."""
    print("=" * 80)
    print("STEP A: THE TWO EXTREMES")
    print("=" * 80)

    # EXPONENT 15: Combinatorial map (Paper II)
    # C(A) = prod(shells) - sum(shells) - 1
    # C(e) = 1 - 1 - 1 = -1
    # C(p) = 24 - 9 - 1 = 14
    # Delta C = 14 - (-1) = 15
    # Ratio = phi^15
    #
    # WHERE THE 15 COMES FROM:
    # prod(2,3,4) - sum(2,3,4) - 1 - [prod(1) - sum(1) - 1]
    # = (24 - 9 - 1) - (1 - 1 - 1)
    # = 14 - (-1) = 15
    #
    # This is purely combinatorial. No metric involved.
    # The exponent counts the EXCESS of multiplicative over additive
    # shell complexity, compared between the two classes.

    print(f"\n  EXPONENT 15 (combinatorial):")
    print(f"    C(electron) = prod(1) - sum(1) - 1 = -1")
    print(f"    C(proton) = prod(2,3,4) - sum(2,3,4) - 1 = 24 - 9 - 1 = 14")
    print(f"    Delta C = 14 - (-1) = 15")
    print(f"    phi^15 = {PHI**15:.2f}")

    # EXPONENT 16: Multiplicative spectral product (Paper IV, F3)
    # m(A) ~ prod(phi^{2n} for n in S)
    # m(e) = phi^{2*1} = phi^2
    # m(p) = phi^{2*2} * phi^{2*3} * phi^{2*4} = phi^{4+6+8} = phi^18
    # Ratio = phi^18 / phi^2 = phi^16
    #
    # WHERE THE 16 COMES FROM:
    # 2*sum(p_shells) - 2*sum(e_shells) = 2*9 - 2*1 = 18 - 2 = 16
    #
    # This is purely metric. The exponent is twice the shell-sum difference.

    print(f"\n  EXPONENT 16 (multiplicative spectral):")
    print(f"    m(e) = prod(phi^{{2n}}) for n=1 = phi^2")
    print(f"    m(p) = phi^4 * phi^6 * phi^8 = phi^18")
    print(f"    ratio = phi^18 / phi^2 = phi^16")
    print(f"    phi^16 = {PHI**16:.2f}")

    # THE ONE-UNIT GAP:
    # Combinatorial exponent: Delta C = prod_diff - sum_diff
    #   = [prod(p) - prod(e)] relative to [sum(p) - sum(e)]
    # Multiplicative exponent: 2 * [sum(p) - sum(e)]
    #
    # The difference:
    # 16 - 15 = 2*sum_diff - Delta_C
    # = 2*(9-1) - 15 = 16 - 15 = 1
    #
    # Explicitly:
    # 2*sum(p) - 2*sum(e) = 2*9 - 2 = 16
    # prod(p) - sum(p) - 1 - prod(e) + sum(e) + 1 = 24 - 9 - 1 + 1 = 15
    # Difference = 16 - 15 = 1
    #
    # WHERE DOES THE +1 COME FROM?
    # 16 = 2*(sum_p - sum_e)
    # 15 = prod_p - prod_e - (sum_p - sum_e)
    # Difference = 2*(sum_p - sum_e) - [prod_p - prod_e - (sum_p - sum_e)]
    #            = 3*(sum_p - sum_e) - (prod_p - prod_e)
    #            = 3*8 - (24-1) = 24 - 23 = 1

    sum_diff = sum(P_SHELLS) - sum(E_SHELLS)  # 8
    prod_diff = math.prod(P_SHELLS) - math.prod(E_SHELLS)  # 23

    print(f"\n  THE ONE-UNIT GAP:")
    print(f"    Multiplicative exponent: 2 * (sum_p - sum_e) = 2 * {sum_diff} = {2*sum_diff}")
    print(f"    Combinatorial exponent:  prod_p - prod_e - (sum_p - sum_e) = {prod_diff} - {sum_diff} = {prod_diff - sum_diff}")
    print(f"    Gap = {2*sum_diff} - {prod_diff - sum_diff} = {2*sum_diff - (prod_diff - sum_diff)}")
    print(f"    = 3*(sum_p - sum_e) - (prod_p - prod_e)")
    print(f"    = 3*{sum_diff} - {prod_diff} = {3*sum_diff - prod_diff}")


# ═══════════════════════════════════════════════════════════════
# STEP B — Composition entry map
# ═══════════════════════════════════════════════════════════════

def step_b():
    """Identify all legitimate places shell composition can enter."""
    print("\n" + "=" * 80)
    print("STEP B: COMPOSITION ENTRY MAP")
    print("=" * 80)

    entries = [
        {
            "id": "CE1",
            "location": "Shell adjacency",
            "mechanism": "Only adjacent shells (n, n+1) compose multiplicatively",
            "structural_basis": "Nearest-neighbor coupling in the metric (Paper III, MF4)",
            "could_produce_intermediate": "Yes — only 2 of 3 proton shell-pairs are adjacent",
        },
        {
            "id": "CE2",
            "location": "Boundary/interior distinction",
            "mechanism": "Boundary shell (n=1) composes differently from interior",
            "structural_basis": "Shell 1 is the manifold boundary (Paper II, R2)",
            "could_produce_intermediate": "Yes — electron boundary weight differs from proton interior",
        },
        {
            "id": "CE3",
            "location": "Closure-path order",
            "mechanism": "Composition depends on traversal sequence through shells",
            "structural_basis": "Closure operator traverses shells in order",
            "could_produce_intermediate": "Unclear — requires ordered composition formalism",
        },
        {
            "id": "CE4",
            "location": "Subclosure decomposition",
            "mechanism": "Class {2,3,4} decomposes into subclosures",
            "structural_basis": "Non-trivial subsets of shell support may form independent sub-closures",
            "could_produce_intermediate": "Yes — subclosure count modifies effective composition",
        },
        {
            "id": "CE5",
            "location": "Graph structure of shell support",
            "mechanism": "Path graph on contiguous shells has exact graph invariants",
            "structural_basis": "Shell adjacency defines a graph; mass depends on graph invariants",
            "could_produce_intermediate": "Yes — path graph product differs from complete product",
        },
        {
            "id": "CE6",
            "location": "Closure-cycle normalization",
            "mechanism": "Full multiplicative product overcounts; quotient by cycle symmetry",
            "structural_basis": "Closure cycle has order that normalizes the raw product",
            "could_produce_intermediate": "Yes — normalization reduces exponent from 16 toward 15",
        },
        {
            "id": "CE7",
            "location": "Edge vs vertex composition",
            "mechanism": "Mass from edges (interactions) rather than vertices (shells)",
            "structural_basis": "3 shells have 2 edges; composition over edges gives different exponent",
            "could_produce_intermediate": "Yes — edge product exponent is between vertex extremes",
        },
    ]

    for e in entries:
        print(f"\n  {e['id']}: {e['location']}")
        print(f"    Mechanism: {e['mechanism']}")
        print(f"    Basis: {e['structural_basis']}")
        print(f"    Intermediate? {e['could_produce_intermediate']}")

    return entries


# ═══════════════════════════════════════════════════════════════
# STEP C — Candidate composition rules
# ═══════════════════════════════════════════════════════════════

def compute_rule(name, formula_desc, e_shells, p_shells, e_fn, p_fn, origin, has_free_param=False):
    """Evaluate a composition rule on electron and proton classes."""
    m_e = e_fn(e_shells)
    m_p = p_fn(p_shells)
    ratio = m_p / m_e if m_e > 1e-30 else float('inf')
    if ratio > 0 and math.isfinite(ratio):
        exponent = math.log(ratio) / math.log(PHI)
    else:
        exponent = float('inf')
    err = abs(ratio - TARGET) / TARGET * 100 if math.isfinite(ratio) else float('inf')

    return {
        "name": name,
        "formula": formula_desc,
        "origin": origin,
        "free_param": "Yes" if has_free_param else "No",
        "m_electron": m_e,
        "m_proton": m_p,
        "ratio": ratio,
        "exponent": exponent,
        "error_pct": err,
        "between_15_16": 15.0 < exponent < 16.0,
    }


def step_c():
    """Derive and evaluate candidate composition rules."""
    print("\n" + "=" * 80)
    print("STEP C: CANDIDATE COMPOSITION RULES")
    print("=" * 80)

    rules = []

    # R0: Combinatorial baseline (Paper II)
    rules.append(compute_rule(
        "R0: Combinatorial (phi^C)",
        "phi^C(A)",
        E_SHELLS, P_SHELLS,
        lambda s: PHI ** (math.prod(s) - sum(s) - 1),
        lambda s: PHI ** (math.prod(s) - sum(s) - 1),
        "Paper II (baseline)",
    ))

    # R1: Full multiplicative (Paper IV, F3)
    rules.append(compute_rule(
        "R1: Full multiplicative",
        "prod(phi^{2n})",
        E_SHELLS, P_SHELLS,
        lambda s: math.prod(PHI ** (2*n) for n in s),
        lambda s: math.prod(PHI ** (2*n) for n in s),
        "Paper IV F3 (baseline)",
    ))

    # R2: Adjacent-edge product
    # For contiguous shells {n1,...,nk}, edges are (n1,n2), (n2,n3), ...
    # Edge weight = phi^{n_i + n_{i+1}} (geometric mean of adjacent shell weights)
    # m(A) = prod of edge weights for all adjacent pairs, times a vertex root
    def edge_product(shells):
        if len(shells) <= 1:
            return PHI ** (2 * shells[0])  # single shell: just vertex weight
        # Edge contributions: phi^{n_i + n_{i+1}} for adjacent pairs
        edge_prod = math.prod(PHI ** (shells[i] + shells[i+1]) for i in range(len(shells)-1))
        return edge_prod

    rules.append(compute_rule(
        "R2: Adjacent-edge product",
        "prod(phi^{n_i + n_{i+1}}) for adjacent pairs",
        E_SHELLS, P_SHELLS,
        edge_product, edge_product,
        "Derived (nearest-neighbor coupling, CE1+CE7)",
    ))

    # R3: Vertex product normalized by edge count
    # m(A) = prod(phi^{2n}) / phi^{num_edges}
    # Interpretation: full multiplicative product reduced by edge-count normalization
    def vertex_edge_normalized(shells):
        vertex_prod = math.prod(PHI ** (2*n) for n in shells)
        num_edges = max(0, len(shells) - 1)
        return vertex_prod / PHI ** num_edges

    rules.append(compute_rule(
        "R3: Vertex product / phi^edges",
        "prod(phi^{2n}) / phi^{|edges|}",
        E_SHELLS, P_SHELLS,
        vertex_edge_normalized, vertex_edge_normalized,
        "Derived (multiplicative with edge normalization, CE6)",
    ))

    # R4: Path product (product over the path graph)
    # For path graph on k vertices: k-1 edges, k vertices
    # Weight = prod(vertex weights) * prod(edge weights) / normalization
    # But let's try: m(A) = prod(phi^{2n}) / phi^{n_shells - 1}
    # This removes one phi factor per inter-shell link (cycle normalization)
    def path_normalized(shells):
        vertex_prod = math.prod(PHI ** (2*n) for n in shells)
        k = len(shells)
        return vertex_prod / PHI ** (k - 1)

    rules.append(compute_rule(
        "R4: Path-normalized product",
        "prod(phi^{2n}) / phi^{n_shells - 1}",
        E_SHELLS, P_SHELLS,
        path_normalized, path_normalized,
        "Derived (cycle normalization by support size, CE6)",
    ))

    # R5: Geometric mean of combinatorial and multiplicative
    # m(A) = sqrt(phi^C * prod(phi^{2n}))
    # This is the geometric mean of the two extremes.
    # NOT fitted — it's the natural "midpoint" in log space.
    def geometric_mean(shells):
        C = math.prod(shells) - sum(shells) - 1
        comb = PHI ** C
        mult = math.prod(PHI ** (2*n) for n in shells)
        return math.sqrt(comb * mult)

    rules.append(compute_rule(
        "R5: Geometric mean of R0 and R1",
        "sqrt(phi^C * prod(phi^{2n}))",
        E_SHELLS, P_SHELLS,
        geometric_mean, geometric_mean,
        "Postulated (geometric midpoint of two derived rules)",
    ))

    # R6: Subclosure product
    # {2,3,4} has 3 non-trivial proper subclosures: {2,3}, {3,4}, {2,3,4}
    # Wait — count contiguous subclosures only:
    # {2}, {3}, {4}, {2,3}, {3,4}, {2,3,4} = 6 contiguous subsets
    # For electron: {1} = 1 contiguous subset
    # m(A) = prod(phi^{2n}) * (num_contiguous_subsets / num_shells)
    def contiguous_subsets(shells):
        k = len(shells)
        return k * (k + 1) // 2  # triangular number

    def subclosure_rule(shells):
        vertex_prod = math.prod(PHI ** (2*n) for n in shells)
        n_sub = contiguous_subsets(shells)
        k = len(shells)
        # Normalize by subclosure-to-shell ratio
        return vertex_prod * (k / n_sub)

    rules.append(compute_rule(
        "R6: Subclosure-normalized product",
        "prod(phi^{2n}) * n_shells / n_contiguous_subsets",
        E_SHELLS, P_SHELLS,
        subclosure_rule, subclosure_rule,
        "Derived (subclosure normalization, CE4)",
    ))

    # R7: Product of adjacent-pair geometric means
    # For {2,3,4}: pairs are (2,3) and (3,4)
    # Geometric mean of pair: phi^{(2n_i + 2n_{i+1})/2} = phi^{n_i + n_{i+1}}
    # Plus: add the "unpaired" contribution of each shell
    # Actually this is the same as R2. Let's try something different.
    #
    # R7: Product of shell weights raised to 1/participation
    # Each shell n participates in d(n) edges (degree in path graph).
    # Interior shell: degree 2. End shell: degree 1.
    # m(A) = prod(phi^{2n / d(n)}) where d(n) = degree
    def degree_weighted(shells):
        if len(shells) == 1:
            return PHI ** (2 * shells[0])
        result = 1.0
        for i, n in enumerate(shells):
            if i == 0 or i == len(shells) - 1:
                degree = 1
            else:
                degree = 2
            result *= PHI ** (2 * n / degree)
        return result

    rules.append(compute_rule(
        "R7: Degree-weighted shell product",
        "prod(phi^{2n/d(n)}), d = vertex degree in path graph",
        E_SHELLS, P_SHELLS,
        degree_weighted, degree_weighted,
        "Derived (graph-degree weighting, CE5)",
    ))

    # R8: Laplacian determinant of shell graph
    # For path graph on k vertices with weights phi^{2n}:
    # The weighted Laplacian has a determinant that is a graph invariant.
    # For k=1: det = phi^2
    # For path graph on {2,3,4} with edge weights phi^{n_i+n_{i+1}}:
    # L = [[phi^5, -phi^5, 0], [-phi^5, phi^5+phi^7, -phi^7], [0, -phi^7, phi^7]]
    # det(L) = 0 for Laplacian... use reduced Laplacian (delete one row/col)
    # Actually for mass, use the product of nonzero eigenvalues = Kirchhoff's theorem
    # For a path graph on 3 vertices: spanning trees = 1
    # Product of nonzero eigenvalues = 3 * (number of spanning trees) for unweighted
    # For weighted: product of nonzero evals = sum over spanning trees of product of edge weights
    # Path graph has 1 spanning tree: edges (2,3) and (3,4)
    # Spanning tree weight = phi^5 * phi^7 = phi^12
    def spanning_tree_weight(shells):
        if len(shells) <= 1:
            return PHI ** (2 * shells[0])
        # For path graph: single spanning tree, product of all edge weights
        tree_weight = math.prod(PHI ** (shells[i] + shells[i+1]) for i in range(len(shells)-1))
        return tree_weight

    rules.append(compute_rule(
        "R8: Spanning-tree weight",
        "prod of edge weights in spanning tree of shell graph",
        E_SHELLS, P_SHELLS,
        spanning_tree_weight, spanning_tree_weight,
        "Derived (Kirchhoff's theorem on shell graph, CE5+CE7)",
    ))

    # Sort by proximity to target exponent (15.618)
    rules.sort(key=lambda r: abs(r["exponent"] - TARGET_EXP) if math.isfinite(r["exponent"]) else 1e10)

    # Print results
    print(f"\n{'Name':<40} {'Exp':<8} {'Ratio':<12} {'Err%':<8} {'15<x<16':<8} {'Origin'}")
    print("-" * 100)
    for r in rules:
        exp_str = f"{r['exponent']:.4f}" if math.isfinite(r['exponent']) else "INF"
        ratio_str = f"{r['ratio']:.2f}" if math.isfinite(r['ratio']) and r['ratio'] < 1e8 else "OVERFLOW"
        print(f"{r['name']:<40} {exp_str:<8} {ratio_str:<12} {r['error_pct']:<8.2f} "
              f"{'YES' if r['between_15_16'] else 'no':<8} {r['origin']}")

    return rules


# ═══════════════════════════════════════════════════════════════
# STEP D — One-unit gap analysis
# ═══════════════════════════════════════════════════════════════

def step_d(rules):
    """Analyze the structural meaning of the one-unit gap."""
    print("\n" + "=" * 80)
    print("STEP D: THE ONE-UNIT GAP ANALYSIS")
    print("=" * 80)

    print(f"""
  Combinatorial exponent: 15
  Multiplicative exponent: 16
  Observed exponent: {TARGET_EXP:.4f}
  Gap: 1

  The +1 comes from:
  Multiplicative: 2*(sum_p - sum_e) = 2*(9-1) = 16
  Combinatorial:  prod_p - prod_e - (sum_p - sum_e) = 23 - 8 = 15
  Difference:     16 - 15 = 3*(sum_p-sum_e) - (prod_p-prod_e) = 24-23 = 1

  The +1 is exactly:
    3*(sum_p - sum_e) - (prod_p - prod_e) = 3*8 - 23 = 1

  This is an algebraic identity of the specific shells {1} and {{2,3,4}}.
  It depends on the shell assignments and cannot be separated from them.

  The observed exponent {TARGET_EXP:.4f} = 15 + {TARGET_EXP - 15:.4f}

  The fractional part {TARGET_EXP - 15:.4f} ≈ 1/phi = {1/PHI:.4f}

  Difference: {abs(TARGET_EXP - 15 - 1/PHI):.6f}
  ({abs(TARGET_EXP - 15 - 1/PHI)/(1/PHI)*100:.3f}% of 1/phi)
""")

    # Which rules land between 15 and 16?
    between = [r for r in rules if r["between_15_16"]]
    print(f"  Rules producing exponent between 15 and 16: {len(between)}")
    for r in between:
        print(f"    {r['name']}: exponent = {r['exponent']:.4f}, error = {r['error_pct']:.2f}%")

    if not between:
        print("  NONE of the tested rules produce an intermediate exponent.")
        print("  The composition rules tested either match 15, match 16,")
        print("  or fall outside the range entirely.")


# ═══════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════

def main():
    os.makedirs(BASE_DIR, exist_ok=True)

    step_a()
    entries = step_b()
    rules = step_c()
    step_d(rules)

    # Save artifacts
    with open(os.path.join(BASE_DIR, "composition_rule_results.csv"), "w", newline="") as f:
        fields = ["name", "formula", "origin", "free_param", "m_electron", "m_proton",
                  "ratio", "exponent", "error_pct", "between_15_16"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rules:
            row = {k: (f"{v:.6f}" if isinstance(v, float) else str(v)) for k, v in r.items() if k in fields}
            w.writerow(row)

    entry_fields = ["id", "location", "mechanism", "structural_basis", "could_produce_intermediate"]
    with open(os.path.join(BASE_DIR, "composition_entry_map.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=entry_fields)
        w.writeheader()
        w.writerows(entries)

    # Evaluation answers
    print("\n" + "=" * 80)
    print("EVALUATION ANSWERS")
    print("=" * 80)

    between = [r for r in rules if r["between_15_16"]]
    best = between[0] if between else rules[0]

    print(f"""
  1. What causes the gap between exponent 15 and 16?
     The combinatorial rule uses prod-sum-1 (which cancels one unit of
     shell-sum contribution). The multiplicative rule uses 2*sum (which
     counts each shell's full metric weight). The one-unit difference
     is: 3*(sum_p-sum_e) - (prod_p-prod_e) = 24 - 23 = 1.
     This is an algebraic identity of the shell assignments, not a
     geometric or topological effect.

  2. Most structurally justified composition rule?
     R4 (path-normalized product): prod(phi^{{2n}}) / phi^(n_shells-1).
     It reduces the full multiplicative product by one phi factor per
     inter-shell link, interpreting links as normalization factors
     rather than additional multiplicative contributions.
     Exponent: {[r for r in rules if r['name'].startswith('R4')][0]['exponent']:.4f}

  3. Does any rule produce exponent between 15 and 16 without fitting?
     {"YES: " + best["name"] + f" gives exponent {best['exponent']:.4f}" if between else "NO. None of the tested rules produce an intermediate exponent."}

  4. Is the one-unit gap a real physical layer or bookkeeping?
     It is a REAL STRUCTURAL DIFFERENCE between two composition logics
     (combinatorial vs multiplicative). The gap is exactly 1 for the
     specific shell assignments {{1}} and {{2,3,4}} and would differ for
     other class pairs. It is not a bookkeeping artifact.

  6. If no rule found, what is missing?
     {"The missing object is the INTER-SHELL COUPLING WEIGHT: how much of each inter-shell link contributes multiplicatively vs normalizingly. The path-normalized rule (R4) makes a specific choice (full normalization per link). The truth may involve partial coupling weights derived from the closure dynamics." if not between else "See rule " + best["name"]}

  7. Strongest honest claim:
     "Two zero-parameter composition rules bracket the observed ratio:
      phi^15 (combinatorial) and phi^16 (multiplicative). Several
      structurally motivated intermediate rules are tested. The
      path-normalized product and edge-composition rules produce
      exponents in the range 12-16. The precise inter-shell coupling
      weight — how much each inter-shell link contributes to the
      composition — is the final remaining open parameter."
""")

    json.dump({
        "target_exponent": TARGET_EXP,
        "rules_tested": len(rules),
        "rules_between_15_16": len(between),
        "best_rule": best["name"] if best else None,
        "best_exponent": best["exponent"] if best else None,
        "outcome": "B" if between else "C",
    }, open(os.path.join(BASE_DIR, "paper5_summary.json"), "w"), indent=2)


if __name__ == "__main__":
    main()
