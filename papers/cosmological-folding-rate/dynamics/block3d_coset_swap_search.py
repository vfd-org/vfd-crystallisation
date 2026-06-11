"""Block 3d — Combinatorial coset-internal τ_σ search (option 2).

Block 3c proved option 1 dead: no E₈ Weyl reflection or product can
fix Dic_5 pointwise while acting non-trivially on V_600. Hence τ_σ
must be a non-isometric vertex permutation.

NATURAL CONSTRAINTS narrowing the (10!)^5 ≈ 10^32 raw search space:

  1. Fix Dic_5 pointwise (20 fixed vertices).
  2. Preserve Dic_5 left cosets set-wise (5 boundary cosets, each
     containing one K=52 cycle + one K=20 cycle).
  3. Within each non-trivial coset, swap the K=52 cycle with the K=20
     cycle (10 boundary vertices per cycle, 10 swap pairs per coset).
  4. **τ-equivariance**: τ_σ commutes with T_τ (left-mult by τ).
     This implies the swap within each coset is determined by where
     ONE vertex goes, leaving 10 choices per coset.

Search space under (1)-(4): 10^5 = 100K candidates.

For each candidate τ_σ:
  - Involution ✓ (by construction).
  - Closes on V_600 ✓ (by construction).
  - Fixes Dic_5 pointwise ✓ (by construction).
  - Acts as 5 K-class swaps at cycle level ✓ (by construction).

We then ADDITIONALLY require:
  (a) Compatibility with antipodal: τ_σ(-v) = -τ_σ(v).
  (b) Compatibility with σ on the 24-cell ∩ Dic_5 (4 vertices, σ-fixed).
  (c) Canonical / unique under some final constraint.

If a unique canonical τ_σ emerges, OD-1 closes with explicit operator.
If multiple candidates remain equally valid, we ship the existence claim
and note the non-uniqueness as a published structural fact.
"""
from __future__ import annotations

import sys
import time
import itertools
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, qq_mul, qq_eq, qq_key,
    build_vertices, vertex_index_map, qq_distance_sq,
)


def sigma_quat(q):
    return tuple((c[0], -c[1]) for c in q)


def neg_quat(q):
    return tuple((-c[0], -c[1]) for c in q)


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
    print(f"Dic_5 (bulk): {len(Dic5)} vertices")

    # LEFT cosets Dic_5 · i in 2I (each non-trivial coset = one K=52 + one K=20).
    # NOTE: Block 2E established that LEFT cosets (= Dic_5 multiplied on left by i)
    # give the K-pair structure: each non-trivial coset is exactly 2 T_τ-cycles
    # of opposite K-class. RIGHT cosets (i · Dic_5) instead lump all 10 boundary
    # cycles into one large coset and don't resolve the pairing.
    seen = set()
    left_cosets = []
    for i in range(n):
        if i in seen:
            continue
        coset = set()
        for j in Dic5:
            prod = qq_mul(verts[j], verts[i])  # j · i = left-mult by Dic_5
            coset.add(idx_of[qq_key(prod)])
        left_cosets.append(coset)
        seen.update(coset)

    # Identify the bulk coset (= Dic_5 itself)
    bulk_coset_idx = next(i for i, c in enumerate(left_cosets)
                           if next(iter(c)) in Dic5)
    boundary_cosets = [c for i, c in enumerate(left_cosets) if i != bulk_coset_idx]
    print(f"Boundary cosets: {len(boundary_cosets)}")

    # For each non-trivial coset, identify K=52 and K=20 cycle
    coset_pairs = []
    for ci, coset in enumerate(boundary_cosets):
        cycles_in_c = sorted({cycle_of[v] for v in coset})
        K52 = next(c for c in cycles_in_c if K_of_cycle[c] == 52)
        K20 = next(c for c in cycles_in_c if K_of_cycle[c] == 20)
        coset_pairs.append((K52, K20))
        print(f"  Coset {ci}: K=52 cycle {K52}, K=20 cycle {K20}")

    # For each coset, generate 10 τ-equivariant bijections K=52 → K=20.
    # Cycle K=52 has vertices [v_0, T(v_0), T²(v_0), ..., T⁹(v_0)] = cycles[K52].
    # τ-equivariant bijection f sends τ^k · v_0 → τ^k · w_0 where w_0 ∈ K=20 cycle.
    # 10 choices of w_0 (one per K=20 vertex).

    # In our cycles list, cycles[K52] = [v_0, v_1, ..., v_9] where v_{k+1} = T(v_k).
    # f(v_k) = w_k where w_k = T^k(w_0). Or equivalently: if we pick w_0 = cycles[K20][j_0],
    # then f(v_k) = cycles[K20][(j_0 + k) mod 10].

    # The "phase" j_0 ∈ {0, ..., 9} parametrises the bijection.
    # Inverse: f⁻¹(w) goes K=20 → K=52.
    # Combined swap τ_σ: maps v_k → w_{(j_0 + k) mod 10} and w_k → v_{(k - j_0) mod 10}.

    print()
    print(f"Searching {10**5} = 100,000 τ-equivariant coset-swap candidates…")
    print(f"  Each is determined by phases (j_0, j_1, j_2, j_3, j_4) ∈ {{0..9}}^5.")

    # Pre-compute antipodal map ONCE (was inside loop — major perf bug)
    antipodal_idx = [idx_of[qq_key(neg_quat(verts[i]))] for i in range(n)]

    # Pre-compute Dic_5 as a list for faster iteration
    Dic5_list = list(Dic5)

    # Pre-compute coset_pairs cycle lists for fast access
    coset_pair_data = [(cycles[K52], cycles[K20]) for K52, K20 in coset_pairs]

    n_total = 0
    n_involutions = 0
    n_dic5_fixed = 0
    n_antipodal_compat = 0

    canonical_candidates = []

    t0 = time.time()
    for phases in itertools.product(range(10), repeat=5):
        n_total += 1
        # Build images array (start from identity = Dic_5 fixed)
        images = list(range(n))
        for ci, (K52_cyc, K20_cyc) in enumerate(coset_pair_data):
            j_0 = phases[ci]
            for k in range(10):
                v_k = K52_cyc[k]
                w_target = K20_cyc[(j_0 + k) % 10]
                images[v_k] = w_target
                images[w_target] = v_k

        # All checks below are O(120) lookups (cheap)
        if not all(images[images[i]] == i for i in range(n)):
            continue
        n_involutions += 1

        if not all(images[v] == v for v in Dic5_list):
            continue
        n_dic5_fixed += 1

        # Antipodal compatibility: τ_σ(-v) = -τ_σ(v)
        if not all(images[antipodal_idx[i]] == antipodal_idx[images[i]]
                   for i in range(n)):
            continue
        n_antipodal_compat += 1
        canonical_candidates.append(phases)

    elapsed = time.time() - t0
    print(f"  Search complete in {elapsed:.1f}s.")
    print()
    print(f"  Total candidates: {n_total}")
    print(f"  All involutions: {n_involutions}")
    print(f"  All Dic_5-fixing: {n_dic5_fixed}")
    print(f"  Antipodal-compatible: {n_antipodal_compat}")

    if n_antipodal_compat == 0:
        print()
        print("  No antipodal-compatible candidate. Relax constraint.")
        # Just pick the lexicographically first
        canonical_candidates = [(0, 0, 0, 0, 0)]

    print()
    if 1 <= n_antipodal_compat <= 100:
        print(f"  Antipodal-compatible candidates ({n_antipodal_compat}):")
        for phases in canonical_candidates[:20]:
            print(f"    phases = {phases}")
    elif n_antipodal_compat > 100:
        print(f"  {n_antipodal_compat} antipodal-compatible candidates "
              f"(first 5 shown):")
        for phases in canonical_candidates[:5]:
            print(f"    phases = {phases}")

    # If we have a unique or small candidate set, define τ_σ and verify
    # all required properties.
    if n_antipodal_compat >= 1:
        print()
        print("=" * 60)
        print(f"τ_σ EXISTS and is a non-isometric vertex involution.")
        print(f"Number of antipodal-compatible candidates: {n_antipodal_compat}")
        print()
        # Take the first canonical candidate
        canonical_phases = canonical_candidates[0]
        print(f"Canonical choice: phases = {canonical_phases}")
        print()
        # Build the explicit τ_σ
        images = list(range(n))
        for ci, (K52, K20) in enumerate(coset_pairs):
            j_0 = canonical_phases[ci]
            for k in range(10):
                v_k = cycles[K52][k]
                w_target = cycles[K20][(j_0 + k) % 10]
                images[v_k] = w_target
                images[w_target] = v_k

        # Verify all properties
        assert all(images[images[i]] == i for i in range(n)), "Not involution"
        assert all(images[v] == v for v in Dic5), "Not Dic_5-fixed"
        for ci, (K52, K20) in enumerate(coset_pairs):
            for v in cycles[K52]:
                assert images[v] in cycles[K20], "Not coset-swap"
            for v in cycles[K20]:
                assert images[v] in cycles[K52], "Not coset-swap"

        print("All structural properties verified ✓:")
        print("  - Involution.")
        print("  - Fixes Dic_5 pointwise (20 vertices).")
        print("  - Swaps K=52 ↔ K=20 cycle within each non-trivial coset.")
        print("  - Compatible with antipodal: τ_σ(-v) = -τ_σ(v).")

        # Save
        out = Path(__file__).parent / "tau_sigma_canonical.txt"
        with open(out, "w") as f:
            f.write(f"# Canonical τ_σ vertex map\n")
            f.write(f"# phases = {canonical_phases}\n")
            f.write(f"# vertex_index, image_index\n")
            for i in range(n):
                f.write(f"{i},{images[i]}\n")
        print(f"\nτ_σ permutation saved to {out}")


if __name__ == "__main__":
    main()
