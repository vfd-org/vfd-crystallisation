"""Block 1 — Compute the K-class of each T_τ cycle on V_600.

K(C) = Σ_{v ∈ C} κ(v),  κ(v) = (shell(v) − 4)²

where shell(v) is the graph-distance shell of v from the identity vertex
1 ∈ 2I in the 600-cell adjacency graph (12-regular, 720 edges).

Predicted (closure-cosmogenesis.md): K-multiset = {72:1, 0:1, 52:5, 20:5}.
This means:
  - 1 cycle with K = 72 (bulk: K=72 cycle)
  - 1 cycle with K = 0  (bulk: K=0 cycle)
  - 5 cycles with K = 52 (boundary)
  - 5 cycles with K = 20 (boundary)
"""
from __future__ import annotations

import sys
from collections import deque
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, qq_mul, qq_eq, qq_key,
    build_vertices, vertex_index_map, qq_distance_sq,
)


def main() -> None:
    verts = build_vertices()
    idx_of = vertex_index_map(verts)
    n = len(verts)

    # Identity vertex
    one = (q_one(), q_zero(), q_zero(), q_zero())
    one_idx = idx_of[qq_key(one)]
    print(f"V_600 size: {n}, identity at index {one_idx}")

    # Build adjacency graph: 12-regular, edges = nearest neighbours.
    # Find minimum non-zero pairwise squared distance.
    min_d2 = None
    for j in range(n):
        if j == one_idx:
            continue
        d2 = qq_distance_sq(one, verts[j])
        if min_d2 is None or _qsqrt5_lt(d2, min_d2):
            min_d2 = d2
    print(f"min squared-distance from identity: {min_d2}")

    # Build adjacency
    adj: list[list[int]] = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d2 = qq_distance_sq(verts[i], verts[j])
            if d2 == min_d2:
                adj[i].append(j)
                adj[j].append(i)

    valences = [len(a) for a in adj]
    val_min, val_max = min(valences), max(valences)
    print(f"adjacency valence: min={val_min}, max={val_max} "
          f"({'OK 12-regular' if val_min == val_max == 12 else 'FAIL'})")

    # Euclidean shells from identity: group vertices by squared distance.
    # 600-cell has 9 distinct shells: 1+12+20+12+30+12+20+12+1 = 120.
    distance_sq = []
    for j in range(n):
        d2 = qq_distance_sq(one, verts[j])
        distance_sq.append(d2)
    # Find unique squared distances (sorted)
    unique_d2_keys = sorted({(float(d2[0]) + float(d2[1]) * (5 ** 0.5)): d2
                              for d2 in distance_sq}.keys())
    d2_to_shell = {key: i for i, key in enumerate(unique_d2_keys)}
    shell = [d2_to_shell[float(d2[0]) + float(d2[1]) * (5 ** 0.5)]
             for d2 in distance_sq]

    # Shell histogram
    shell_count: dict[int, int] = {}
    for s in shell:
        shell_count[s] = shell_count.get(s, 0) + 1
    print("\nshell histogram (vertex count per shell):")
    for s in sorted(shell_count):
        print(f"  shell {s}: {shell_count[s]} vertices, κ=(s-4)²={(s-4)**2}")

    # Build T_τ cycles
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
    print(f"\nT_τ cycles: {len(cycles)}, all length {sorted({len(c) for c in cycles})}")

    # K-class per cycle
    cycle_K = []
    for c in cycles:
        K = sum((shell[v] - 4) ** 2 for v in c)
        cycle_K.append(K)

    print("\n--- Block 1 result ---")
    print(f"K-class per cycle: {sorted(cycle_K)}")
    K_multiset: dict[int, int] = {}
    for K in cycle_K:
        K_multiset[K] = K_multiset.get(K, 0) + 1
    print(f"K-multiset: {K_multiset}")
    print(f"expected:   {{72: 1, 0: 1, 52: 5, 20: 5}}")
    if K_multiset == {72: 1, 0: 1, 52: 5, 20: 5}:
        print("\n✓ MATCHES closure-cosmogenesis.md K-multiset.")
    else:
        print("\n⚠ does NOT match — actual K-multiset differs from doc claim.")
        print("  This is a real finding: either the doc has wrong K-values,")
        print("  or the script is computing shell incorrectly.")
        print(f"  Sum of K-class values: {sum(cycle_K)} (expected 432 = 72+0+5·52+5·20)")
        # Show cycle-by-cycle data
        print("\nDetailed breakdown:")
        for ci, c in enumerate(cycles):
            kappas = [(shell[v] - 4) ** 2 for v in c]
            print(f"  cycle {ci}: K={cycle_K[ci]}, "
                  f"shells={[shell[v] for v in c]}, "
                  f"κ-values={kappas}")


def _qsqrt5_lt(a, b):
    """Compare two Q(√5) elements (a0+a1√5) < (b0+b1√5)."""
    a_real = float(a[0]) + float(a[1]) * (5 ** 0.5)
    b_real = float(b[0]) + float(b[1]) * (5 ** 0.5)
    return a_real < b_real


if __name__ == "__main__":
    main()
