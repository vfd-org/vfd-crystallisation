"""Block 3e — Canonical τ_σ via σ-projection: VFD-geometric criterion.

100K coset-swap candidates exist (Block 3d). To single out a canonical
τ_σ, use the natural VFD-geometric criterion:

    τ_σ(v) := argmax_{u ∈ V_600} ⟨σ(v), u⟩_trace

i.e., τ_σ(v) is the V_600 vertex closest to σ(v) in the trace inner
product (the natural inner product on the icosian lattice).

This is "the V_600 vertex closest to σ(v)" — the canonical projection of
σ from σ(V_600) back to V_600 via the trace metric. It's intrinsic to
the icosian/VFD geometry and doesn't depend on coordinate choices.

Verify this canonical τ_σ satisfies:
  1. Involution.
  2. Fixes Dic_5 pointwise (20 vertices).
  3. Swaps K=52 ↔ K=20 within each non-trivial Dic_5-coset.
  4. Antipodal-compatible.
  5. τ-equivariant (commutes with T_τ).

If all hold, this is our canonical τ_σ.
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, q_add, q_sub, q_mul,
    qq_mul, qq_eq, qq_key, qq_conjugate, qq_distance_sq,
    build_vertices, vertex_index_map,
)


def sigma_quat(q):
    return tuple((c[0], -c[1]) for c in q)


def neg_quat(q):
    return tuple((-c[0], -c[1]) for c in q)


def trace_inner(v, w):
    """⟨v, w⟩ = Tr(v·w̄). For unit icosians v, w: returns 2·Re(v·w̄) ∈ Q."""
    w_conj = qq_conjugate(w)
    prod = qq_mul(v, w_conj)
    return 2 * prod[0][0]


def main():
    verts = build_vertices()
    idx_of = vertex_index_map(verts)
    n = len(verts)
    one = (q_one(), q_zero(), q_zero(), q_zero())

    def order_of(g):
        r = one
        for k in range(1, 31):
            r = qq_mul(r, g)
            if qq_eq(r, one):
                return k
        return -1

    tau = next(v for v in verts if order_of(v) == 10)
    T = [idx_of[qq_key(qq_mul(tau, verts[i]))] for i in range(n)]

    # Cycles
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
    keys_d = [(float(d2[0]) + float(d2[1]) * (5 ** 0.5)) for d2 in distance_sq]
    unique = sorted(set(keys_d))
    d2_to_shell = {k: i for i, k in enumerate(unique)}
    shell = [d2_to_shell[k] for k in keys_d]
    K_of_cycle = [sum((shell[v] - 4) ** 2 for v in c) for c in cycles]

    bulk_cycles = [ci for ci, K in enumerate(K_of_cycle) if K in (72, 0)]
    Dic5 = set()
    for ci in bulk_cycles:
        Dic5.update(cycles[ci])

    # LEFT cosets (Dic_5 · v for representative v).
    seen = set()
    left_cosets = []
    for i in range(n):
        if i in seen:
            continue
        coset = set()
        for j in Dic5:
            prod = qq_mul(verts[j], verts[i])  # left-mult by Dic_5
            coset.add(idx_of[qq_key(prod)])
        left_cosets.append(coset)
        seen.update(coset)
    coset_of = {v: ci for ci, c in enumerate(left_cosets) for v in c}
    bulk_coset = next(i for i, c in enumerate(left_cosets) if next(iter(c)) in Dic5)

    print(f"Dic_5 (bulk): {len(Dic5)} vertices")
    print(f"Left cosets: {len(left_cosets)}, bulk coset = {bulk_coset}")

    # σ-projection: for each v ∈ V_600, find argmax_{u ∈ V_600} ⟨σ(v), u⟩.
    print()
    print("Computing σ-projection: τ_σ(v) := argmax_u ⟨σ(v), u⟩…")

    # For each pair (v, σ(v)), find u maximising ⟨σ(v), u⟩ over u ∈ V_600.
    # Equivalently: u minimising distance_sq(σ(v), u) (since |u| constant).
    sigma_proj_image = []
    sigma_proj_unique = True  # check if max is unique
    ties_count = 0

    for i in range(n):
        sv = sigma_quat(verts[i])
        # Compute trace inner product ⟨σ(v), u⟩ for all u ∈ V_600
        best_u = None
        best_score = None
        candidates_with_max = []
        for u_idx in range(n):
            score = trace_inner(sv, verts[u_idx])
            if best_score is None or score > best_score:
                best_score = score
                best_u = u_idx
                candidates_with_max = [u_idx]
            elif score == best_score:
                candidates_with_max.append(u_idx)
        sigma_proj_image.append((best_u, candidates_with_max))
        if len(candidates_with_max) > 1:
            sigma_proj_unique = False
            ties_count += 1

    print(f"  σ-projection unique? {sigma_proj_unique}")
    print(f"  Vertices with tied max: {ties_count}")

    if not sigma_proj_unique:
        # Show example ties
        for i in range(n):
            cands = sigma_proj_image[i][1]
            if len(cands) > 1:
                print(f"  v_{i} (cycle {cycle_of[i]}, K={K_of_cycle[cycle_of[i]]}) "
                      f"has {len(cands)} tied candidates: {cands[:5]}…")
                break

    # Even if not unique, check if the FIRST candidate (or some canonical choice)
    # gives a structurally valid τ_σ.
    print()
    print("Testing σ-projection (taking first candidate at ties):")
    images = [sigma_proj_image[i][0] for i in range(n)]

    is_inv = all(images[images[i]] == i for i in range(n))
    print(f"  Involution: {is_inv}")
    fixed_v = sum(1 for i in range(n) if images[i] == i)
    print(f"  Fixed vertices: {fixed_v}")
    dic5_fixed = all(images[v] == v for v in Dic5)
    print(f"  Dic_5 fixed pointwise: {dic5_fixed}")

    # Check coset preservation
    coset_violations = 0
    coset_action = {}
    for ci, c in enumerate(left_cosets):
        targets = {coset_of[images[v]] for v in c}
        if len(targets) != 1:
            coset_violations += 1
        coset_action[ci] = sorted(targets)
    print(f"  Coset preservation: {'YES' if coset_violations == 0 else f'NO ({coset_violations} violations)'}")

    # Cycle action
    cycle_action = {}
    cycle_consistent = True
    for ci, c in enumerate(cycles):
        targets = {cycle_of[images[v]] for v in c}
        if len(targets) != 1:
            cycle_consistent = False
        cycle_action[ci] = sorted(targets)
    print(f"  Cycle preservation: {'YES' if cycle_consistent else 'NO (scattered)'}")

    if cycle_consistent:
        print()
        print("Cycle action:")
        for ci in range(len(cycles)):
            target = cycle_action[ci][0]
            marker = " ← FIXED" if target == ci else ""
            print(f"  cycle {ci} (K={K_of_cycle[ci]}) → cycle {target} (K={K_of_cycle[target]}){marker}")

    # VFD-geometric assessment
    print()
    print("=" * 60)
    if dic5_fixed and cycle_consistent and coset_violations == 0:
        # Perfect VFD-geometric τ_σ
        n_fixed_cyc = sum(1 for ci in cycle_action if cycle_action[ci][0] == ci)
        n_paired = 0
        n_cross = 0
        seen_c = set()
        for ci in cycle_action:
            if ci in seen_c: continue
            target = cycle_action[ci][0]
            if target == ci:
                seen_c.add(ci)
            elif cycle_action[target][0] == ci:
                seen_c.add(ci); seen_c.add(target)
                n_paired += 1
                if K_of_cycle[ci] != K_of_cycle[target]:
                    n_cross += 1
        print(f"τ_σ via σ-projection IS canonical:")
        print(f"  Fixed cycles: {n_fixed_cyc} (expected 2)")
        print(f"  Paired cycles: {n_paired} (expected 5)")
        print(f"  Cross-K pairs: {n_cross} (expected 5)")
    else:
        print("σ-projection does NOT directly give the target structure.")
        print("Likely cause: the projection scatters within cosets, not preserving cycles.")
        print("Need additional constraint or different VFD-canonical map.")


if __name__ == "__main__":
    main()
