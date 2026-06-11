"""Block 3b — τ_σ via σ + parity-flip projection P.

Structural realisation (Block 3a):
  σ takes V_600 (even-permutation 600-cell) to the odd-permutation 600-cell
  in the SAME R⁴. The two share only the 24-cell.

  σ(v_24..119) lands in odd-perm space, NOT in V_600 (96 escapes).
  σ(v_0..23)  fixes the 24-cell elements (the 24 σ-fixed of V_600).

For τ_σ: V_600 → V_600 we compose σ with a parity-flipping map P that
sends odd-perm 600-cell back to even-perm V_600.

CANDIDATES for P:
  Class A — Coordinate transpositions: swap two of (w, x, y, z).
            Each flips permutation parity. 6 candidates.
  Class B — Coordinate negations: negate a single component.
            Negation of one component changes parity. 4 candidates.
  Class C — Unit-quaternion left-mult: v → q · v for q ∈ 2I.
            Some q's swap the two 600-cells.
  Class D — Composition: P = transposition ∘ negation, etc.

For each (P, σ) pair, define τ(v) := P(σ(v)) and check:
  1. closes on V_600 (P maps σ(V_600) into V_600).
  2. is an involution: (P∘σ)² = id ⇒ σ∘P∘σ = P (since P² = id for reflections).
  3. cycle action: consistent? 2 fixed cycles + 5 cross-K pairs?
"""
from __future__ import annotations

import sys
import time
import itertools
from fractions import Fraction
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, q_add, q_sub, q_neg, q_mul, q_scale,
    qq_mul, qq_eq, qq_key, qq_conjugate, qq_norm_sq, qq_distance_sq,
    build_vertices, vertex_index_map,
)


def sigma_quat(q):
    return tuple((c[0], -c[1]) for c in q)


def conj_quat(q):
    w, x, y, z = q
    neg = lambda c: (-c[0], -c[1])
    return (w, neg(x), neg(y), neg(z))


def neg_quat(q):
    return tuple((-c[0], -c[1]) for c in q)


def transpose_quat(q, i, j):
    """Swap components i and j of quaternion q."""
    out = list(q)
    out[i], out[j] = out[j], out[i]
    return tuple(out)


def negate_component(q, i):
    """Negate i-th component of quaternion q."""
    out = list(q)
    out[i] = (-out[i][0], -out[i][1])
    return tuple(out)


def main():
    verts = build_vertices()
    idx_of = vertex_index_map(verts)
    n = len(verts)
    one = (q_one(), q_zero(), q_zero(), q_zero())

    # Build T_τ cycles + K-classes
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
    print(f"K-multiset confirmed: {sorted(K_of_cycle)}")
    print(f"Bulk cycles: {bulk_cycles}, K=72={[c for c in bulk_cycles if K_of_cycle[c]==72]}, K=0={[c for c in bulk_cycles if K_of_cycle[c]==0]}")

    # Build candidate P maps
    candidates = {}

    # Class A: 6 transpositions of coordinate pairs (i, j) with i < j
    for i in range(4):
        for j in range(i + 1, 4):
            name = f"transp({i},{j})"
            candidates[name] = (lambda q, i=i, j=j: transpose_quat(q, i, j))

    # Class B: 4 single-component negations
    for i in range(4):
        name = f"neg_coord{i}"
        candidates[name] = (lambda q, i=i: negate_component(q, i))

    # Class C: left-multiplication by each q ∈ 2I (120 candidates)
    # We'll add these in the scan loop, since 120 × 1 = 120 candidates.

    # Class D: transposition + negation combos (4 × 6 = 24 candidates)
    for i in range(4):
        for ti in range(4):
            for tj in range(ti + 1, 4):
                name = f"transp({ti},{tj})+neg{i}"
                candidates[name] = (
                    lambda q, ti=ti, tj=tj, i=i: negate_component(transpose_quat(q, ti, tj), i)
                )

    print()
    print(f"Testing {len(candidates)} explicit P candidates + 120 left-mult P's…")
    print()

    def test_tau_sigma(name, fn_p):
        """fn_p: quaternion → quaternion. Test τ(v) = fn_p(σ(v))."""
        # Compute images
        images = []
        for i in range(n):
            sv = sigma_quat(verts[i])
            tv = fn_p(sv)
            j = idx_of.get(qq_key(tv))
            if j is None:
                return None  # not closed
            images.append(j)

        # Involution check
        if not all(images[images[i]] == i for i in range(n)):
            return None

        # Skip identity
        if all(images[i] == i for i in range(n)):
            return None

        # Cycle action consistency
        m = {}
        for ci, c in enumerate(cycles):
            tgt = {cycle_of[images[v]] for v in c}
            if len(tgt) != 1:
                return None
            m[ci] = next(iter(tgt))

        # Classify orbits
        seen = set()
        orbits = []
        for ci in range(len(cycles)):
            if ci in seen:
                continue
            cur = m[ci]
            if cur == ci:
                orbits.append(("fix", ci))
                seen.add(ci)
            elif m[cur] == ci:
                orbits.append(("pair", ci, cur))
                seen.add(ci)
                seen.add(cur)
            else:
                return None

        n_fixed = sum(1 for o in orbits if o[0] == "fix")
        pairs = [o for o in orbits if o[0] == "pair"]
        n_paired = len(pairs)
        n_cross = sum(1 for o in pairs
                      if K_of_cycle[o[1]] != K_of_cycle[o[2]])

        # Count fixed vertices (NOT just fixed cycles)
        fixed_v = sum(1 for i in range(n) if images[i] == i)

        return {
            "name": name,
            "n_fixed_cycles": n_fixed,
            "n_paired_cycles": n_paired,
            "n_cross_K": n_cross,
            "fixed_vertices": fixed_v,
            "orbits": orbits,
            "images": images,
        }

    # Test class A, B, D
    target_hits = []
    near_misses = []
    closed_count = 0
    involutions = 0

    for name, fn in candidates.items():
        result = test_tau_sigma(name, fn)
        if result is None:
            continue
        closed_count += 1
        involutions += 1
        if (result["n_fixed_cycles"] == 2 and
            result["n_paired_cycles"] == 5 and
            result["n_cross_K"] == 5):
            fixed_K = sorted(K_of_cycle[o[1]] for o in result["orbits"] if o[0] == "fix")
            if fixed_K == [0, 72] and result["fixed_vertices"] == 20:
                target_hits.append(result)
                print(f"*** TARGET HIT: P = {name} ***")
                print(f"    Fixed vertices: {result['fixed_vertices']}")
                print(f"    Cycle structure: 2 fixed (K=0, 72) + 5 cross-K pairs")
                for o in result["orbits"]:
                    if o[0] == "fix":
                        print(f"      fixed cycle {o[1]}: K={K_of_cycle[o[1]]}")
                    else:
                        print(f"      pair {o[1]} ↔ {o[2]}: K={K_of_cycle[o[1]]} ↔ K={K_of_cycle[o[2]]}")
                print()
        elif result["n_cross_K"] >= 1 or result["fixed_vertices"] >= 8:
            near_misses.append(result)

    # Test class C: left-mult by each 2I element
    print(f"Class A/B/D: {closed_count} closed-and-involution, {len(target_hits)} target hits")
    print()
    print("Class C: left-mult by q ∈ 2I (120 candidates)…")
    t0 = time.time()
    for q_idx in range(n):
        q = verts[q_idx]
        name = f"left_mult_q{q_idx}"
        fn = (lambda v, q=q: qq_mul(q, v))
        result = test_tau_sigma(name, fn)
        if result is None:
            continue
        closed_count += 1
        if (result["n_fixed_cycles"] == 2 and
            result["n_paired_cycles"] == 5 and
            result["n_cross_K"] == 5):
            fixed_K = sorted(K_of_cycle[o[1]] for o in result["orbits"] if o[0] == "fix")
            if fixed_K == [0, 72] and result["fixed_vertices"] == 20:
                target_hits.append(result)
                print(f"*** TARGET HIT: P = {name} ***")
        elif result["n_cross_K"] >= 1 or result["fixed_vertices"] >= 8:
            near_misses.append(result)
    print(f"  Class C scan complete in {time.time()-t0:.1f}s")

    # Test class C2: right-mult
    print("Class C2: right-mult by q ∈ 2I (120 candidates)…")
    t0 = time.time()
    for q_idx in range(n):
        q = verts[q_idx]
        name = f"right_mult_q{q_idx}"
        fn = (lambda v, q=q: qq_mul(v, q))
        result = test_tau_sigma(name, fn)
        if result is None:
            continue
        closed_count += 1
        if (result["n_fixed_cycles"] == 2 and
            result["n_paired_cycles"] == 5 and
            result["n_cross_K"] == 5):
            fixed_K = sorted(K_of_cycle[o[1]] for o in result["orbits"] if o[0] == "fix")
            if fixed_K == [0, 72] and result["fixed_vertices"] == 20:
                target_hits.append(result)
                print(f"*** TARGET HIT: P = {name} ***")
        elif result["n_cross_K"] >= 1 or result["fixed_vertices"] >= 8:
            near_misses.append(result)
    print(f"  Class C2 scan complete in {time.time()-t0:.1f}s")

    print()
    print("=" * 60)
    print(f"Total closed-and-involution candidates: {closed_count}")
    print(f"Target hits: {len(target_hits)}")
    print(f"Near misses: {len(near_misses)}")

    if target_hits:
        print()
        print("FOUND τ_σ! See target hits above.")
    elif near_misses:
        print()
        print("Top near-misses by (cross_K desc, fixed_vertices desc):")
        ranked = sorted(near_misses,
                        key=lambda r: (-r["n_cross_K"], -r["fixed_vertices"]))
        for r in ranked[:20]:
            print(f"  {r['name']:<28} fixed_v={r['fixed_vertices']:3d} "
                  f"fixed_cyc={r['n_fixed_cycles']} paired={r['n_paired_cycles']} "
                  f"crossK={r['n_cross_K']}")


if __name__ == "__main__":
    main()
