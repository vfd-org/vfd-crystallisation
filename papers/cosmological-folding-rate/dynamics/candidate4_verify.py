"""Candidate 4 verification — σ as Elkies E₈ ↔ 2I ⊕ σ(2I) involution.

Per `docs/glossary.md` ("σ-intertwining: Galois twist √5 ↦ -√5 on Z[φ]
extends to an automorphism of E₈ that swaps two conjugate H₄ copies"),
the σ in closure-cosmogenesis acts on E₈ = 2I ⊕ σ(2I), not on 2I alone.

Restricted to 2I:
  - σ-fixed vertices form a subset (the rational-quaternion icosians)
  - σ maps non-fixed vertices to σ(2I), outside 2I
  - But cycles can still be classified:
      "σ-fixed cycle"  = T_τ cycle entirely inside the σ-fixed subset
      "σ-mobile cycle" = cycle with at least one σ-non-fixed vertex

Prediction: of T_τ's 12 cycles, exactly 2 are σ-fixed cycles (the K=72
and K=0 bulk) and 10 are σ-mobile. The σ-mobile cycles pair into 5
"natural pairs" via an identification σ(2I) ↔ 2I to be specified.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, qq_mul, qq_eq, qq_key,
    build_vertices, vertex_index_map,
)


def sigma_quat(q):
    """Galois σ on Q(√5) coordinates."""
    return tuple((c[0], -c[1]) for c in q)


def main():
    verts = build_vertices()
    idx_of = vertex_index_map(verts)
    n = len(verts)

    # σ-fixed vertices: σ(v) = v (works only on the 24 rational-quaternion icosians)
    sigma_fixed_vertices = set()
    for i, v in enumerate(verts):
        if qq_key(sigma_quat(v)) == qq_key(v):
            sigma_fixed_vertices.add(i)
    print(f"σ-fixed vertices in 2I: {len(sigma_fixed_vertices)}")

    # Find an order-10 element τ and build T_τ permutation
    one = (q_one(), q_zero(), q_zero(), q_zero())

    def order_of(g):
        result = one
        for k in range(1, 31):
            result = qq_mul(result, g)
            if qq_eq(result, one):
                return k
        return -1

    tau = next(v for v in verts if order_of(v) == 10)
    T = [idx_of[qq_key(qq_mul(tau, verts[i]))] for i in range(n)]

    # Decompose into cycles
    visited = [False] * n
    cycles = []
    for s in range(n):
        if visited[s]:
            continue
        c = []
        cur = s
        while not visited[cur]:
            visited[cur] = True
            c.append(cur)
            cur = T[cur]
        cycles.append(c)

    print(f"T_τ cycle structure: {len(cycles)} cycles, lengths {sorted(set(len(c) for c in cycles))}")

    # Classify cycles by σ-fixed-vertex content
    cycle_class = []
    for ci, c in enumerate(cycles):
        sf = sum(1 for v in c if v in sigma_fixed_vertices)
        if sf == len(c):
            cycle_class.append(("entirely-σ-fixed", ci, sf))
        elif sf == 0:
            cycle_class.append(("entirely-σ-mobile", ci, sf))
        else:
            cycle_class.append(("mixed", ci, sf))

    classes_count = {}
    for cls, ci, sf in cycle_class:
        classes_count.setdefault(cls, []).append((ci, sf))
    print(f"\nCycle σ-classification:")
    for cls, items in classes_count.items():
        print(f"  {cls:<22}: {len(items):>2} cycles, σ-fixed counts = "
              f"{[sf for _, sf in items]}")

    n_entire_fixed = len(classes_count.get("entirely-σ-fixed", []))
    n_entire_mobile = len(classes_count.get("entirely-σ-mobile", []))
    n_mixed = len(classes_count.get("mixed", []))
    total_sf_in_fixed_cycles = sum(sf for _, sf in classes_count.get("entirely-σ-fixed", []))

    print(f"\n--- Candidate 4 prediction check ---")
    print(f"  expected (closure-cosmogenesis):")
    print(f"    bulk     = 2 entirely-σ-fixed cycles, 20 σ-fixed vertices")
    print(f"    boundary = 10 σ-paired cycles")
    print(f"  observed:")
    print(f"    entirely-σ-fixed cycles: {n_entire_fixed} (vertices: {total_sf_in_fixed_cycles})")
    print(f"    mixed cycles:            {n_mixed}")
    print(f"    entirely-σ-mobile cycles: {n_entire_mobile}")
    print()
    if n_entire_fixed == 2 and total_sf_in_fixed_cycles == 20:
        print("  ✓ MATCH: 2 entirely-σ-fixed cycles with 20 σ-fixed vertices.")
        print("    Closure-cosmogenesis bulk = entirely-σ-fixed cycles. CONFIRMED.")
    else:
        print(f"  ⚠ DOES NOT MATCH the 2/10/20/100 structure as expected.")
        print(f"    Need to investigate the cycle-σ relationship more carefully.")

    # Print cycle vertex contents for first few cycles
    print(f"\nFirst few cycles:")
    for ci, c in enumerate(cycles[:3]):
        sf_idx = [v for v in c if v in sigma_fixed_vertices]
        print(f"  cycle {ci}: {len(sf_idx)}/{len(c)} σ-fixed; σ-fixed indices {sf_idx}")


if __name__ == "__main__":
    main()
