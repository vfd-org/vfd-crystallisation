"""Block 2C — Exhaustive (h, k) pair scan over 2I × 2I.

Block 2B's narrow inner-twist scan returned zero hits/near-misses. This
extends to ALL involutions of the form

    τ(v) = h · R(v) · k          for h, k ∈ 2I,  sign ∈ {+1, -1}

with R ∈ {id, conj, antipodal, σ, σ∘conj, σ∘antipod, conj∘σ}.

This subsumes:
  - inner automorphisms (k = h⁻¹ = h̄)
  - left-translates (k = 1)
  - right-translates (h = 1)
  - H₄ reflections through 2I-axes: τ(v) = −n v̄ n  (h=−n, R=conj, k=n)
  - any other 2I-bilinear vertex map

Search space: 7 R × 2 signs × 120² (h, k) = 201,600 candidates. Each test
needs O(120) closure + O(120) involution + O(120) cycle consistency, so
~7·10⁷ ops. Should complete in ~1 minute.

Honest expectation: the result of Block 2 already showed that only `id`,
`conj`, and `antipodal` outer ops close on 2I as plain unconjugated maps.
With h, k ≠ 1, more compositions may close; with σ involved, very few
are likely to close at all. We're casting a wide net to be definitive.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, qq_mul, qq_eq, qq_key,
    build_vertices, vertex_index_map, qq_distance_sq,
)


def sigma_quat(q):
    return tuple((c[0], -c[1]) for c in q)


def conj_quat(q):
    w, x, y, z = q
    neg = lambda c: (-c[0], -c[1])
    return (w, neg(x), neg(y), neg(z))


def neg_quat(q):
    return tuple((-c[0], -c[1]) for c in q)


OUTER_OPS = {
    "id":            lambda q: q,
    "conj":          conj_quat,
    "antipodal":     neg_quat,
    "sigma":         sigma_quat,
    "sigma+conj":    lambda q: sigma_quat(conj_quat(q)),
    "sigma+antipod": lambda q: sigma_quat(neg_quat(q)),
    "conj+sigma":   lambda q: conj_quat(sigma_quat(q)),
}


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
    print(f"K-multiset: {sorted(K_of_cycle)}")
    print(f"# cycles: {len(cycles)}")

    q_arr = list(verts)

    # Pre-compute R-images for each outer op (no h, k yet)
    R_images = {}
    for r_name, R in OUTER_OPS.items():
        imgs = []
        for i in range(n):
            r = R(q_arr[i])
            j = idx_of.get(qq_key(r))
            imgs.append(j)
        R_images[r_name] = imgs
        n_in_2I = sum(1 for j in imgs if j is not None)
        print(f"  R={r_name:<14} closes on 2I: {n_in_2I}/{n}")

    # Pre-compute all pairwise products in 2I for fast h·v·k lookup.
    # Build mul_table[i][j] = idx of v_i · v_j.
    print()
    print("Building 2I multiplication table…")
    t0 = time.time()
    mul_table = [[idx_of[qq_key(qq_mul(q_arr[i], q_arr[j]))] for j in range(n)]
                 for i in range(n)]
    print(f"  done in {time.time() - t0:.1f}s")

    # For each outer R, R is a permutation of 2I (or partial map).
    # We test τ(v) = h · R(v) · k for h, k ∈ 2I and sign ε ∈ {+1, -1}.
    # ε is implemented by left-multiplying the result by neg_quat (i.e., by −1).
    # Since −1 is in 2I (index of neg_quat(one)), ε just shifts h to (−h) or k to (−k).
    # So sign is absorbed into h. We don't need explicit sign loop.

    minus_one_idx = idx_of[qq_key(neg_quat(one))]

    def cycle_action_consistent(images):
        m = {}
        for ci, c in enumerate(cycles):
            tgt = {cycle_of[images[v]] for v in c}
            if len(tgt) != 1:
                return None
            m[ci] = next(iter(tgt))
        return m

    def classify_orbits(m):
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
                orbits.append(("higher", ci, cur, m.get(cur)))
                seen.add(ci)
                seen.add(cur)
        n_fixed = sum(1 for o in orbits if o[0] == "fix")
        pairs = [o for o in orbits if o[0] == "pair"]
        n_paired = len(pairs)
        n_cross = sum(1 for o in pairs if K_of_cycle[o[1]] != K_of_cycle[o[2]])
        n_within = n_paired - n_cross
        n_higher = sum(1 for o in orbits if o[0] == "higher")
        return n_fixed, n_paired, n_cross, n_within, n_higher, orbits

    print()
    print("Scanning τ(v) = h · R(v) · k over (h, k) ∈ 2I² × 7 R…")
    target_hits = []
    near_misses = []
    total_evaluated = 0
    total_closes = 0
    total_involutions = 0
    total_cycle_consistent = 0

    t0 = time.time()
    for r_name, R in OUTER_OPS.items():
        r_imgs = R_images[r_name]
        # Skip if R doesn't close on 2I — only useful R's are those closing.
        # But for h, k ≠ 1, h·R(v)·k may still close even if R alone doesn't,
        # because h, k can rotate σ(2I) back to 2I. That requires h ∈ σ(2I)·2I^-1 · 2I, etc.
        # In our case h, k ∈ 2I always, so h·X·k ∈ 2I iff X ∈ 2I. So if R(v) ∉ 2I,
        # then h·R(v)·k ∉ 2I either. Skip non-closing R's.
        if any(j is None for j in r_imgs):
            print(f"  R={r_name:<14}: doesn't close on 2I, skipping (no h,k can fix this)")
            continue

        for h_idx in range(n):
            # Pre-compute h · R(v) for all v
            hR = [mul_table[h_idx][r_imgs[v]] for v in range(n)]
            for k_idx in range(n):
                # Compute τ(v) = (h R(v)) · k = mul_table[hR[v]][k_idx]
                images = [mul_table[hR[v]][k_idx] for v in range(n)]
                total_evaluated += 1
                total_closes += 1  # always closes by construction

                # Check involution
                is_inv = True
                for i in range(n):
                    if images[images[i]] != i:
                        is_inv = False
                        break
                if not is_inv:
                    continue
                total_involutions += 1

                # Skip identity (all fixed)
                if all(images[i] == i for i in range(n)):
                    continue

                ca = cycle_action_consistent(images)
                if ca is None:
                    continue
                total_cycle_consistent += 1

                n_fixed, n_paired, n_cross, n_within, n_higher, orbits = classify_orbits(ca)
                if n_higher > 0:
                    continue  # not an involution at cycle level

                if n_fixed == 2 and n_paired == 5 and n_cross == 5:
                    fixed_cyc = [o[1] for o in orbits if o[0] == "fix"]
                    K_fixed = sorted(K_of_cycle[c] for c in fixed_cyc)
                    if K_fixed == [0, 72]:
                        target_hits.append((r_name, h_idx, k_idx, orbits))
                        print(f"\n*** TARGET HIT *** R={r_name}  h={h_idx}  k={k_idx}")
                        for o in orbits:
                            if o[0] == "fix":
                                print(f"      fixed cycle {o[1]}: K={K_of_cycle[o[1]]}")
                            elif o[0] == "pair":
                                print(f"      pair {o[1]} ↔ {o[2]}: "
                                      f"K={K_of_cycle[o[1]]} ↔ K={K_of_cycle[o[2]]}")
                elif n_cross >= 1 and n_fixed >= 1:
                    near_misses.append((r_name, h_idx, k_idx,
                                        n_fixed, n_paired, n_cross, n_within))

        print(f"  R={r_name:<14} done at t={time.time()-t0:.1f}s "
              f"(evaluated={total_evaluated}, involutions={total_involutions}, "
              f"cycle_consistent={total_cycle_consistent})")

    print()
    print(f"Total evaluated:        {total_evaluated}")
    print(f"Closes on 2I:           {total_closes}")
    print(f"Is involution:          {total_involutions}")
    print(f"Cycle-consistent:       {total_cycle_consistent}")
    print(f"Target hits:            {len(target_hits)}")
    print(f"Near misses:            {len(near_misses)}")

    if not target_hits and near_misses:
        print()
        print("Top 30 near-misses by (n_cross desc, n_fixed desc):")
        ranked = sorted(near_misses, key=lambda x: (-x[5], -x[3], x[6]))
        for r_name, h, k, nf, np_, nc, nw in ranked[:30]:
            print(f"  R={r_name:<14}  h={h:3d} k={k:3d}  "
                  f"fixed={nf} paired={np_} crossK={nc} withinK={nw}")

    if target_hits:
        print()
        print("=== Writing target hits to BLOCK2C_HITS.md ===")
        with open(Path(__file__).parent / "BLOCK2C_HITS.md", "w") as f:
            f.write("# Block 2C — Target hits\n\n")
            f.write(f"Found {len(target_hits)} involutions giving 2 σ-fixed (K=72⊔K=0) "
                    f"+ 5 cross-K paired (K=52↔K=20) cycle structure.\n\n")
            for r_name, h, k, orbits in target_hits:
                f.write(f"## τ(v) = q_{h} · {r_name}(v) · q_{k}\n\n")
                for o in orbits:
                    if o[0] == "fix":
                        f.write(f"- fixed cycle {o[1]}: K={K_of_cycle[o[1]]}\n")
                    elif o[0] == "pair":
                        f.write(f"- pair {o[1]} ↔ {o[2]}: "
                                f"K={K_of_cycle[o[1]]} ↔ K={K_of_cycle[o[2]]}\n")
                f.write("\n")


if __name__ == "__main__":
    main()
