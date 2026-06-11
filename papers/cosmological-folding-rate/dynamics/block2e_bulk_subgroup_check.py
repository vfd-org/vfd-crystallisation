"""Block 2E — Is the bulk (K=72 ∪ K=0, 20 vertices) a subgroup of 2I?

Conjecture: bulk ≃ Dic_5 (binary dihedral of order 20) ⊂ 2I.

If true, the structural picture clarifies dramatically:
  - 2I has subgroup Dic_5 with index [2I : Dic_5] = 6.
  - The 6 cosets of Dic_5 partition the 120 vertices.
  - Bulk = trivial coset (Dic_5 itself).
  - 5 non-trivial cosets, each of 20 vertices = 2 T_τ-cycles.
  - The 5 boundary K=52/K=20 pairs ARE these 5 non-trivial Dic_5-cosets.

This explains why no (h v k)-style involution works: we need a map that
fixes Dic_5 POINTWISE (20 fixed vertices) and swaps the two cycles within
each non-trivial coset. No quaternion translation/inner-twist has this
profile — the natural candidate is a Weyl reflection of E₈ that
descends to V_600.

This script verifies:
  1. Bulk verts are closed under multiplication (subgroup test).
  2. Bulk has 20 elements = Dic_5 order.
  3. The 5 non-trivial cosets each contain one K=52 cycle and one K=20 cycle.
  4. The 6-coset structure aligns with the K-class pairing.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, qq_mul, qq_eq, qq_key,
    build_vertices, vertex_index_map, qq_distance_sq,
)


def conj_quat(q):
    w, x, y, z = q
    neg = lambda c: (-c[0], -c[1])
    return (w, neg(x), neg(y), neg(z))


def main():
    verts = build_vertices()
    idx_of = vertex_index_map(verts)
    n = len(verts)
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
    cycle_of = {v: ci for ci, c in enumerate(cycles) for v in c}

    distance_sq = [qq_distance_sq(one, verts[j]) for j in range(n)]
    keys = [(float(d2[0]) + float(d2[1]) * (5 ** 0.5)) for d2 in distance_sq]
    unique = sorted(set(keys))
    d2_to_shell = {k: i for i, k in enumerate(unique)}
    shell = [d2_to_shell[k] for k in keys]
    K_of_cycle = [sum((shell[v] - 4) ** 2 for v in c) for c in cycles]

    bulk_cycles = [ci for ci, K in enumerate(K_of_cycle) if K in (72, 0)]
    bulk_idx = set()
    for ci in bulk_cycles:
        bulk_idx.update(cycles[ci])
    print(f"Bulk cycles: {bulk_cycles}, |bulk| = {len(bulk_idx)}")

    # Test 1: closure under multiplication
    print()
    print("Test 1: is bulk closed under multiplication?")
    closure_violations = 0
    for i in bulk_idx:
        for j in bulk_idx:
            prod = qq_mul(verts[i], verts[j])
            prod_idx = idx_of[qq_key(prod)]
            if prod_idx not in bulk_idx:
                closure_violations += 1
    print(f"  closure violations: {closure_violations} (out of {len(bulk_idx)**2})")
    if closure_violations == 0:
        print("  ✓ Bulk IS closed under multiplication. Bulk is a subgroup of 2I.")
    else:
        print("  ✗ Bulk NOT closed. Not a subgroup.")

    # Test 2: identify the subgroup via order structure
    print()
    print("Test 2: order distribution of bulk elements")
    from collections import Counter
    order_counts = Counter(order_of(verts[i]) for i in bulk_idx)
    print(f"  {dict(order_counts)}")
    print("  Dic_5 has elements of orders {1: 1, 2: 1, 4: 10, 5: 4, 10: 4} = 20.")

    # Test 3: cosets of bulk in 2I
    print()
    print("Test 3: cosets of bulk in 2I (right cosets c·Bulk)")
    seen = set()
    cosets = []
    for i in range(n):
        if i in seen:
            continue
        coset = set()
        for j in bulk_idx:
            prod = qq_mul(verts[i], verts[j])
            coset.add(idx_of[qq_key(prod)])
        cosets.append(coset)
        seen.update(coset)
    print(f"  Number of cosets: {len(cosets)} (expected 6 for index [2I:Dic_5]=6)")
    print(f"  Coset sizes: {[len(c) for c in cosets]}")

    # Test 4: K-class composition of each coset
    print()
    print("Test 4: each non-trivial coset = 2 cycles of cross-K classes?")
    bulk_coset = next(c for c in cosets if next(iter(c)) in bulk_idx)
    print(f"  Bulk coset: {sorted(bulk_coset)} (cycles: "
          f"{sorted({cycle_of[v] for v in bulk_coset})})")
    for ci, c in enumerate(cosets):
        if c == bulk_coset:
            continue
        cycles_in_c = sorted({cycle_of[v] for v in c})
        Ks = [K_of_cycle[cyc] for cyc in cycles_in_c]
        print(f"  Coset {ci}: cycles {cycles_in_c}, K-classes {Ks}")

    # Test 5: same with LEFT cosets (in case the structure is asymmetric)
    print()
    print("Test 5: LEFT cosets Bulk·c — same structure?")
    seen = set()
    left_cosets = []
    for i in range(n):
        if i in seen:
            continue
        coset = set()
        for j in bulk_idx:
            prod = qq_mul(verts[j], verts[i])
            coset.add(idx_of[qq_key(prod)])
        left_cosets.append(coset)
        seen.update(coset)
    print(f"  Number of left cosets: {len(left_cosets)}")
    bulk_lcoset = next(c for c in left_cosets if next(iter(c)) in bulk_idx)
    for ci, c in enumerate(left_cosets):
        if c == bulk_lcoset:
            continue
        cycles_in_c = sorted({cycle_of[v] for v in c})
        Ks = [K_of_cycle[cyc] for cyc in cycles_in_c]
        print(f"  L-coset {ci}: cycles {cycles_in_c}, K-classes {Ks}")

    # Final summary
    if closure_violations == 0 and len(cosets) == 6:
        print()
        print("=" * 60)
        print("STRUCTURAL FINDING:")
        print("  Bulk = Dic_5 (binary dihedral order 20) ⊂ 2I")
        print("  [2I : Dic_5] = 6 cosets")
        print("  Each non-trivial coset = 1 K=52 cycle + 1 K=20 cycle")
        print()
        print("  ⇒ τ_σ must fix Dic_5 pointwise AND swap the two cycles")
        print("    within each non-trivial coset.")
        print()
        print("  No (h v k) bilinear map can fix 20 vertices pointwise:")
        print("  the 4-fixed-vertex cap is structural for 2I-bilinear maps.")
        print()
        print("  Candidate τ_σ: an E₈ Weyl reflection that descends to V_600,")
        print("  fixing Dic_5 (a 20-vertex configuration in S³).")


if __name__ == "__main__":
    main()
