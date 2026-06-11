"""Block 3g — VFD-canonical τ_σ via coset+K-opposite σ-projection.

Construction:
  τ_σ(v) := v                                          if v ∈ Dic_5
            argmax_{u ∈ coset(v) ∩ K_opp(v)} ⟨σ(v), u⟩  if v ∈ boundary

where K_opp(v) is the K-class-opposite cycle in v's left coset (the K=20
cycle if v is in a K=52 cycle, and vice versa).

This construction is fully VFD-geometric:
  - Bulk Dic_5 is fixed by definition (closure-invariant region).
  - Boundary swap respects (a) coset structure (Dic_5-cosets), (b)
    K-class duality (52 ↔ 20), and (c) trace-metric proximity to σ.

Verify properties:
  1. Involution.
  2. Fixes Dic_5 pointwise (by definition).
  3. Swaps K=52 ↔ K=20 within each non-trivial coset (by definition).
  4. τ-equivariant?
  5. Antipodal-compatible?
  6. Conjugation-compatible?
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, qq_mul, qq_eq, qq_key, qq_conjugate,
    build_vertices, vertex_index_map, qq_distance_sq,
)


def sigma_quat(q):
    return tuple((c[0], -c[1]) for c in q)


def neg_quat(q):
    return tuple((-c[0], -c[1]) for c in q)


def trace_inner(v, w):
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
            if qq_eq(r, one): return k
        return -1

    tau = next(v for v in verts if order_of(v) == 10)
    T = [idx_of[qq_key(qq_mul(tau, verts[i]))] for i in range(n)]
    visited = [False] * n
    cycles = []
    for s in range(n):
        if visited[s]: continue
        c = []; cur = s
        while not visited[cur]:
            visited[cur] = True; c.append(cur); cur = T[cur]
        cycles.append(c)
    cycle_of = {v: ci for ci, c in enumerate(cycles) for v in c}

    distance_sq = [qq_distance_sq(one, verts[j]) for j in range(n)]
    keys_d = [(float(d2[0]) + float(d2[1]) * (5 ** 0.5)) for d2 in distance_sq]
    unique_d = sorted(set(keys_d))
    d2_to_shell = {k: i for i, k in enumerate(unique_d)}
    shell = [d2_to_shell[k] for k in keys_d]
    K_of_cycle = [sum((shell[v] - 4) ** 2 for v in c) for c in cycles]

    bulk_cycles = [ci for ci, K in enumerate(K_of_cycle) if K in (72, 0)]
    Dic5 = set()
    for ci in bulk_cycles:
        Dic5.update(cycles[ci])

    # Left cosets
    seen = set()
    left_cosets = []
    for i in range(n):
        if i in seen: continue
        coset = set()
        for j in Dic5:
            prod = qq_mul(verts[j], verts[i])
            coset.add(idx_of[qq_key(prod)])
        left_cosets.append(coset)
        seen.update(coset)
    coset_of = {v: ci for ci, c in enumerate(left_cosets) for v in c}

    # For each coset, identify K=52 and K=20 cycle
    coset_K52 = {}
    coset_K20 = {}
    for ci, c in enumerate(left_cosets):
        cycles_in_c = sorted({cycle_of[v] for v in c})
        for cy in cycles_in_c:
            if K_of_cycle[cy] == 52:
                coset_K52[ci] = cy
            elif K_of_cycle[cy] == 20:
                coset_K20[ci] = cy

    print(f"Dic_5: {len(Dic5)} verts; left cosets: {len(left_cosets)}")
    print()

    # Build τ_σ
    images = [None] * n

    # Fix Dic_5
    for v in Dic5:
        images[v] = v

    # For boundary vertices: argmax within (coset ∩ K-opposite cycle)
    tied = 0
    for i in range(n):
        if i in Dic5: continue
        v_coset = coset_of[i]
        v_cycle = cycle_of[i]
        v_K = K_of_cycle[v_cycle]
        # K-opposite cycle in same coset
        if v_K == 52:
            target_cycle = coset_K20[v_coset]
        elif v_K == 20:
            target_cycle = coset_K52[v_coset]
        else:
            assert False, f"v_{i} in cycle {v_cycle} with K={v_K} not handled"

        # Candidates: vertices in target_cycle (10 of them)
        candidate_pool = cycles[target_cycle]

        sv = sigma_quat(verts[i])
        best_u = None
        best_score = None
        cands = []
        for u_idx in candidate_pool:
            score = trace_inner(sv, verts[u_idx])
            if best_score is None or score > best_score:
                best_score = score
                best_u = u_idx
                cands = [u_idx]
            elif score == best_score:
                cands.append(u_idx)
        images[i] = best_u
        if len(cands) > 1:
            tied += 1

    print(f"Boundary vertices with tied closest: {tied}/100")

    # Verify properties
    is_inv = all(images[images[i]] == i for i in range(n))
    fixed_v = sum(1 for i in range(n) if images[i] == i)
    dic5_fixed = all(images[v] == v for v in Dic5)

    print()
    print("Properties of VFD-canonical τ_σ:")
    print(f"  Involution: {is_inv}")
    print(f"  Fixed vertices: {fixed_v}")
    print(f"  Dic_5 fixed pointwise: {dic5_fixed}")

    # Coset preservation
    coset_violations = sum(1 for i in range(n) if coset_of[images[i]] != coset_of[i])
    print(f"  Coset preservation: {'YES' if coset_violations == 0 else f'NO ({coset_violations})'}")

    # Cycle action
    cycle_action_consistent = True
    cycle_action = {}
    for ci, c in enumerate(cycles):
        targets = {cycle_of[images[v]] for v in c}
        if len(targets) != 1:
            cycle_action_consistent = False
        cycle_action[ci] = sorted(targets)
    print(f"  Cycle preservation: {'YES' if cycle_action_consistent else 'NO'}")

    if cycle_action_consistent:
        n_fixed_cyc = 0
        n_paired = 0
        n_cross = 0
        seen_c = set()
        for ci in cycle_action:
            if ci in seen_c: continue
            tgt = cycle_action[ci][0]
            if tgt == ci:
                seen_c.add(ci); n_fixed_cyc += 1
            elif cycle_action[tgt][0] == ci:
                seen_c.add(ci); seen_c.add(tgt); n_paired += 1
                if K_of_cycle[ci] != K_of_cycle[tgt]:
                    n_cross += 1

        print(f"  Cycle structure: {n_fixed_cyc} fixed + {n_paired} paired ({n_cross} cross-K)")

    if not is_inv:
        # Diagnose
        print()
        print("Involution failures (τ_σ²(v) ≠ v):")
        bad = [(i, images[i], images[images[i]]) for i in range(n)
               if images[images[i]] != i]
        for i, ti, tti in bad[:5]:
            print(f"  v_{i} → v_{ti} → v_{tti} (should be {i})")

    # Additional symmetry checks
    if is_inv and dic5_fixed:
        antipodal_idx = [idx_of[qq_key(neg_quat(verts[i]))] for i in range(n)]
        antipodal_compat = all(images[antipodal_idx[i]] == antipodal_idx[images[i]]
                                for i in range(n))
        tau_equiv = all(images[T[i]] == T[images[i]] for i in range(n))
        conj_idx = [idx_of[qq_key(qq_conjugate(verts[i]))] for i in range(n)]
        conj_compat = all(images[conj_idx[i]] == conj_idx[images[i]] for i in range(n))

        print()
        print(f"  τ-equivariant (T_τ commute):    {tau_equiv}")
        print(f"  Antipodal-compatible:           {antipodal_compat}")
        print(f"  Conjugation-compatible:         {conj_compat}")

        # Save
        if cycle_action_consistent and n_fixed_cyc == 2 and n_cross == 5:
            print()
            print("=" * 60)
            print("✓ VFD-CANONICAL τ_σ CONSTRUCTED")
            print("Construction: τ_σ(v) := v if v ∈ Dic_5;")
            print("              else argmax_{u ∈ coset(v) ∩ K_opp(v)} ⟨σ(v), u⟩.")
            out = Path(__file__).parent / "tau_sigma_canonical_VFD.txt"
            with open(out, "w") as f:
                f.write("# VFD-canonical τ_σ\n")
                f.write("# τ_σ(v) := v if v ∈ Dic_5\n")
                f.write("# τ_σ(v) := argmax_{u ∈ coset(v) ∩ K_opp(v)} ⟨σ(v), u⟩ if v ∈ boundary\n")
                f.write("# Properties: involution, Dic_5 fixed, K=52↔K=20 within cosets\n")
                f.write("# vertex_index, image_index\n")
                for i in range(n):
                    f.write(f"{i},{images[i]}\n")
            print(f"Saved to {out}")


if __name__ == "__main__":
    main()
