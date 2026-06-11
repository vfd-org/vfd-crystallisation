"""Block 3h — Filter Block 3d's 100K candidates by σ-projection compatibility.

Block 3d: 10⁵ τ-equivariant Dic_5-fixing involutions on V_600 with 5 cross-K
swaps.

Block 3g: VFD σ-projection criterion gives the right structure (2 fixed + 5
cross-K pairs, Dic_5 fixed, coset-preserving) but NOT an involution — because
σ-projection isn't symmetric (forward != backward direction).

This block: among Block 3d's 100K involutions, find those where EVERY swap
pair (v, τ_σ(v)) satisfies "τ_σ(v) is in the σ-projection-max set of v
restricted to the K-opposite cycle in v's coset" — i.e., where the
involution agrees with VFD σ-projection bidirectionally.

For each coset, σ-projection of v_0 (one K=52 representative) onto the
K=20 cycle gives a tied max set of size k_0 (= 3 typically). The
τ-equivariant swap parameterised by phase j ∈ {0..9} pairs v_0 with
w_j = K20_cycle[j].  Phase j is σ-projection-consistent iff w_j is in
the tied max set.

If exactly k_0 phases are consistent per coset, we get k_0^5 = 3^5 = 243
fully-VFD-canonical involutions.

Also filter for SYMMETRIC: σ-projection of w_j onto K=52 cycle should
give v_0 in its tied max set. This may further reduce the candidates.
"""
from __future__ import annotations

import sys
import itertools
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
    bulk_coset_idx = next(i for i, c in enumerate(left_cosets)
                           if next(iter(c)) in Dic5)

    boundary_cosets = [(i, c) for i, c in enumerate(left_cosets) if i != bulk_coset_idx]
    coset_pairs = []
    for ci, coset in boundary_cosets:
        cyc_in_c = sorted({cycle_of[v] for v in coset})
        K52 = next(c for c in cyc_in_c if K_of_cycle[c] == 52)
        K20 = next(c for c in cyc_in_c if K_of_cycle[c] == 20)
        coset_pairs.append((K52, K20))

    # For each coset (K52, K20), find σ-projection-consistent phases.
    # τ-equivariant swap: v_k = K52[k] ↔ w_{j+k} = K20[(j+k) mod 10].
    # σ-projection-consistent for v_0: K20[j] ∈ argmax_{u ∈ K20} ⟨σ(v_0), u⟩.
    # Symmetric: K52[0] ∈ argmax_{u ∈ K52} ⟨σ(K20[j]), u⟩.

    print("σ-projection-consistent phases per coset:")
    consistent_phases_per_coset = []
    for ci, (K52, K20) in enumerate(coset_pairs):
        v_0 = cycles[K52][0]
        sv = sigma_quat(verts[v_0])
        # Compute scores for all K=20 cycle members
        scores = [(j, trace_inner(sv, verts[cycles[K20][j]])) for j in range(10)]
        max_score = max(s for _, s in scores)
        max_phases = [j for j, s in scores if s == max_score]
        # SYMMETRIC: for each candidate j, check σ-projection of K20[j] onto K52 gives v_0
        symm_phases = []
        for j in max_phases:
            w_j = cycles[K20][j]
            swj = sigma_quat(verts[w_j])
            scores_back = [(k, trace_inner(swj, verts[cycles[K52][k]])) for k in range(10)]
            max_back = max(s for _, s in scores_back)
            max_back_phases = [k for k, s in scores_back if s == max_back]
            if 0 in max_back_phases:  # K52[0] = v_0 is in the back-projection max set
                symm_phases.append(j)
        consistent_phases_per_coset.append(symm_phases)
        print(f"  coset {ci}: {len(max_phases)} forward-max, "
              f"{len(symm_phases)} symmetric: {symm_phases}")

    if any(len(p) == 0 for p in consistent_phases_per_coset):
        print("  Some coset has no symmetric σ-projection-consistent phase.")
        print("  Relaxing to forward-only…")
        consistent_phases_per_coset = []
        for ci, (K52, K20) in enumerate(coset_pairs):
            v_0 = cycles[K52][0]
            sv = sigma_quat(verts[v_0])
            scores = [(j, trace_inner(sv, verts[cycles[K20][j]])) for j in range(10)]
            max_score = max(s for _, s in scores)
            max_phases = [j for j, s in scores if s == max_score]
            consistent_phases_per_coset.append(max_phases)
            print(f"  coset {ci}: {max_phases}")

    n_total_canonical = 1
    for p in consistent_phases_per_coset:
        n_total_canonical *= len(p)
    print()
    print(f"Total VFD-canonical candidates: {n_total_canonical}")

    # Test each combination
    antipodal_idx = [idx_of[qq_key(neg_quat(verts[i]))] for i in range(n)]
    conj_idx = [idx_of[qq_key(qq_conjugate(verts[i]))] for i in range(n)]

    print()
    print("Testing all VFD-canonical combinations…")
    n_passed = 0
    canonical_list = []
    for phase_combo in itertools.product(*consistent_phases_per_coset):
        # Build images
        images = list(range(n))
        for ci, (K52, K20) in enumerate(coset_pairs):
            j_0 = phase_combo[ci]
            for k in range(10):
                v_k = cycles[K52][k]
                w_target = cycles[K20][(j_0 + k) % 10]
                images[v_k] = w_target
                images[w_target] = v_k

        is_inv = all(images[images[i]] == i for i in range(n))
        if not is_inv:
            continue
        n_passed += 1

        antipodal_compat = all(images[antipodal_idx[i]] == antipodal_idx[images[i]]
                                for i in range(n))
        conj_compat = all(images[conj_idx[i]] == conj_idx[images[i]] for i in range(n))
        canonical_list.append((phase_combo, antipodal_compat, conj_compat))

    print(f"Involution candidates: {n_passed}")
    if n_passed > 0:
        a_count = sum(1 for _, a, _ in canonical_list if a)
        c_count = sum(1 for _, _, c in canonical_list if c)
        ac_count = sum(1 for _, a, c in canonical_list if a and c)
        print(f"  Antipodal-compatible: {a_count}")
        print(f"  Conjugation-compatible: {c_count}")
        print(f"  Both: {ac_count}")
        print()
        if ac_count >= 1:
            both_list = [pc for pc, a, c in canonical_list if a and c]
            print(f"VFD-canonical fully-symmetric τ_σ candidates ({ac_count}):")
            for phases in both_list[:10]:
                print(f"  {phases}")

            # Take first as canonical
            canonical_phases = both_list[0]
            images = list(range(n))
            for ci, (K52, K20) in enumerate(coset_pairs):
                j_0 = canonical_phases[ci]
                for k in range(10):
                    v_k = cycles[K52][k]
                    w_target = cycles[K20][(j_0 + k) % 10]
                    images[v_k] = w_target
                    images[w_target] = v_k

            print()
            print("=" * 60)
            print("✓ VFD-CANONICAL τ_σ FOUND")
            print(f"  Phases: {canonical_phases}")
            print(f"  Properties: involution, fixes Dic_5, 5 cross-K coset swaps,")
            print(f"              σ-projection-consistent, antipodal-compat,")
            print(f"              conjugation-compat.")
            out = Path(__file__).parent / "tau_sigma_VFD_canonical.txt"
            with open(out, "w") as f:
                f.write("# VFD-canonical τ_σ\n")
                f.write(f"# Phases per coset: {canonical_phases}\n")
                f.write(f"# Total fully-symmetric candidates: {ac_count}\n")
                f.write("# vertex_index, image_index\n")
                for i in range(n):
                    f.write(f"{i},{images[i]}\n")
            print(f"  Saved to {out}")
        else:
            print("No fully-symmetric (antipodal + conjugation) candidate.")
            print("Show involution-only candidates:")
            for pc, a, c in canonical_list[:10]:
                print(f"  {pc}  antipodal={a} conj={c}")


if __name__ == "__main__":
    main()
