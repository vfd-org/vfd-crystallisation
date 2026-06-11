"""Block 3f — σ-projection with Dic_5-coset constraint.

Block 3e showed σ-projection has 3-way ties for σ-mobile vertices.
This refinement: among the 3 (or k) nearest V_600 vertices to σ(v), choose
the one in v's left Dic_5-coset.

If this gives a unique canonical τ_σ that is:
  1. an involution,
  2. fixes Dic_5 pointwise,
  3. preserves cosets,
  4. swaps K=52 ↔ K=20 within each non-trivial coset,
  5. (possibly) antipodal-compatible / τ-equivariant,
then this IS the VFD-geometric canonical τ_σ.

The coset-constraint is itself VFD-geometric: cosets are intrinsic to
the icosian/Dic_5 structure, not to coordinate choices.
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

    print(f"Dic_5: {len(Dic5)} verts; cosets: {len(left_cosets)}")
    print()
    print("Computing constrained σ-projection: τ_σ(v) := argmax_{u ∈ coset(v)} ⟨σ(v), u⟩.")

    images = [None] * n
    multiplicities = []  # ties within coset

    for i in range(n):
        sv = sigma_quat(verts[i])
        v_coset = coset_of[i]
        best_u = None
        best_score = None
        candidates = []
        for u_idx in left_cosets[v_coset]:  # only search within coset
            score = trace_inner(sv, verts[u_idx])
            if best_score is None or score > best_score:
                best_score = score
                best_u = u_idx
                candidates = [u_idx]
            elif score == best_score:
                candidates.append(u_idx)
        images[i] = best_u
        multiplicities.append(len(candidates))

    n_unique = sum(1 for m in multiplicities if m == 1)
    n_tied = sum(1 for m in multiplicities if m > 1)
    print(f"  Unique closest-in-coset: {n_unique}/{n}")
    print(f"  Tied: {n_tied}/{n}")

    # Verify properties
    is_inv = all(images[images[i]] == i for i in range(n))
    fixed_v = sum(1 for i in range(n) if images[i] == i)
    dic5_fixed = all(images[v] == v for v in Dic5)

    print()
    print("Properties of the canonical τ_σ candidate:")
    print(f"  Involution: {is_inv}")
    print(f"  Fixed vertices: {fixed_v}")
    print(f"  Dic_5 fixed pointwise: {dic5_fixed}")

    # Coset preservation
    coset_violations = sum(1 for i in range(n) if coset_of[images[i]] != coset_of[i])
    print(f"  Coset preservation: {'YES' if coset_violations == 0 else f'NO ({coset_violations} viol)'}")

    # Cycle action
    cycle_action_consistent = True
    cycle_action = {}
    for ci, c in enumerate(cycles):
        targets = {cycle_of[images[v]] for v in c}
        if len(targets) != 1:
            cycle_action_consistent = False
        cycle_action[ci] = sorted(targets)
    print(f"  Cycle preservation: {'YES' if cycle_action_consistent else 'NO (scattered)'}")

    if cycle_action_consistent and is_inv and dic5_fixed:
        print()
        print("Cycle structure:")
        n_fixed_cyc = 0
        n_paired = 0
        n_cross = 0
        seen_c = set()
        for ci in cycle_action:
            if ci in seen_c: continue
            tgt = cycle_action[ci][0]
            if tgt == ci:
                seen_c.add(ci)
                n_fixed_cyc += 1
                print(f"  cycle {ci} (K={K_of_cycle[ci]}) FIXED")
            elif cycle_action[tgt][0] == ci:
                seen_c.add(ci); seen_c.add(tgt)
                n_paired += 1
                if K_of_cycle[ci] != K_of_cycle[tgt]:
                    n_cross += 1
                print(f"  cycle {ci}↔{tgt}  K={K_of_cycle[ci]}↔{K_of_cycle[tgt]}")

        print()
        print("=" * 60)
        if n_fixed_cyc == 2 and n_paired == 5 and n_cross == 5:
            print("✓ CANONICAL τ_σ FOUND via VFD-geometric σ-projection!")
            print(f"  Construction: τ_σ(v) := argmax_{{u ∈ coset(v)}} ⟨σ(v), u⟩_trace")
            print(f"  Properties: involution, fix Dic_5, swap K=52↔K=20 within cosets.")

            # Save
            out = Path(__file__).parent / "tau_sigma_canonical_VFD.txt"
            with open(out, "w") as f:
                f.write("# Canonical τ_σ via VFD-geometric σ-projection\n")
                f.write("# τ_σ(v) := argmax_{u ∈ coset(v)} ⟨σ(v), u⟩_trace\n")
                f.write("# vertex_index, image_index\n")
                for i in range(n):
                    f.write(f"{i},{images[i]}\n")
            print(f"  Saved to {out}")

            # Additional checks
            antipodal_idx = [idx_of[qq_key(neg_quat(verts[i]))] for i in range(n)]
            antipodal_compat = all(images[antipodal_idx[i]] == antipodal_idx[images[i]]
                                    for i in range(n))
            tau_equiv = all(images[T[i]] == T[images[i]] for i in range(n))
            conj_compat = True  # placeholder
            conj_idx = []
            for i in range(n):
                cv = qq_conjugate(verts[i])
                ci = idx_of.get(qq_key(cv))
                conj_idx.append(ci if ci is not None else -1)
            conj_compat = all(conj_idx[i] != -1 for i in range(n))
            if conj_compat:
                conj_compat = all(images[conj_idx[i]] == conj_idx[images[i]]
                                   for i in range(n))
            print()
            print(f"  τ-equivariant (commutes with T_τ): {tau_equiv}")
            print(f"  antipodal-compatible: {antipodal_compat}")
            print(f"  conjugation-compatible: {conj_compat}")
        else:
            print(f"τ_σ partial: {n_fixed_cyc} fixed, {n_paired} paired, {n_cross} cross-K.")
            print("Not the target 2-fixed + 5-cross-K structure.")


if __name__ == "__main__":
    main()
