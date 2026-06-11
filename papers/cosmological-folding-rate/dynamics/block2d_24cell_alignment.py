"""Block 2D — Check alignment of coordinate-σ-fixed 24-cell with bulk cycles.

The 24 coordinate-σ-fixed vertices in V_600 form a 24-cell (the elements of
2I lying in the standard Hurwitz integer ring Z[i,j,k] without √5 content).

The closure-cosmogenesis bulk has 20 vertices (K=72 cycle ∪ K=0 cycle).

Question: are the 20 bulk vertices a subset of the 24-cell? If so, the 4
"extra" σ-fixed vertices live in BOUNDARY cycles, breaking the simple
"pointwise σ-fixed = bulk" claim. If not, even the K-class identification
of bulk doesn't match coordinate-σ-fixed.

This is a diagnostic — doesn't search for τ_σ, just confirms or rules out
that coordinate σ identifies the bulk.
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


def sigma_quat(q):
    return tuple((c[0], -c[1]) for c in q)


def is_coord_sigma_fixed(q):
    """A vertex q is coord-σ-fixed iff sigma_quat(q) = q, i.e., all √5-parts zero."""
    return all(c[1] == 0 for c in q)


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

    sigma_fixed_idx = [i for i in range(n) if is_coord_sigma_fixed(verts[i])]
    print(f"Coordinate-σ-fixed vertices in V_600: {len(sigma_fixed_idx)}")
    print(f"Expected: 24 (the 24-cell)")
    assert len(sigma_fixed_idx) == 24, f"Expected 24, got {len(sigma_fixed_idx)}"

    # Distribution of σ-fixed vertices by cycle and K-class
    from collections import Counter, defaultdict
    sigma_per_cycle = Counter(cycle_of[v] for v in sigma_fixed_idx)
    print()
    print("σ-fixed vertices per cycle (cycle_idx: count):")
    for ci in range(len(cycles)):
        K = K_of_cycle[ci]
        cnt = sigma_per_cycle.get(ci, 0)
        marker = "  ← BULK" if K in (72, 0) else ""
        print(f"  cycle {ci:2d} (K={K:2d}): {cnt} σ-fixed vertices{marker}")

    sigma_per_K = defaultdict(int)
    for ci, cnt in sigma_per_cycle.items():
        sigma_per_K[K_of_cycle[ci]] += cnt
    print()
    print("σ-fixed vertices per K-class:")
    for K in sorted(sigma_per_K, reverse=True):
        print(f"  K={K:2d}: {sigma_per_K[K]} σ-fixed vertices")

    # Identify the bulk
    bulk_cycles = [ci for ci in range(len(cycles)) if K_of_cycle[ci] in (72, 0)]
    bulk_verts = set()
    for ci in bulk_cycles:
        bulk_verts.update(cycles[ci])
    print()
    print(f"Bulk cycles: {bulk_cycles} ({len(bulk_verts)} vertices)")
    print(f"σ-fixed ∩ bulk: {len(set(sigma_fixed_idx) & bulk_verts)}")
    print(f"σ-fixed not in bulk: {len(set(sigma_fixed_idx) - bulk_verts)}")
    print(f"bulk vertices not σ-fixed: {len(bulk_verts - set(sigma_fixed_idx))}")

    # Now: which boundary cycles contain σ-fixed vertices?
    print()
    print("Boundary cycles with σ-fixed vertices:")
    for ci in range(len(cycles)):
        if K_of_cycle[ci] in (72, 0):
            continue
        cnt = sigma_per_cycle.get(ci, 0)
        if cnt > 0:
            print(f"  cycle {ci} (K={K_of_cycle[ci]}): {cnt} σ-fixed")

    # Aha: maybe the 20 bulk vertices are NOT all coord-σ-fixed.
    # Check: which bulk vertices have non-zero √5 components?
    bulk_with_sqrt5 = []
    for v in bulk_verts:
        if not is_coord_sigma_fixed(verts[v]):
            bulk_with_sqrt5.append(v)
    print()
    print(f"Bulk vertices with non-zero √5 components: {len(bulk_with_sqrt5)}")
    if bulk_with_sqrt5:
        print("  These vertices are σ-MOBILE under coord σ (not σ-fixed pointwise).")
        print("  ⇒ Doc claim 'σ-fixed cycles are pointwise σ-fixed' uses a")
        print("    DIFFERENT σ than coordinate σ on Q(√5).")


if __name__ == "__main__":
    main()
