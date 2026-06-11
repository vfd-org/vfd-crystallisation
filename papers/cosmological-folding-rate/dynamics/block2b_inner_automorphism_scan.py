"""Block 2B — Broad scan for τ_σ via inner-twists and translations.

Block 2 ruled out 6 standard candidates. This script extends the search:

For each outer operation R ∈ {id, conj, antipodal, σ, σ∘conj, σ∘antipod,
conj∘σ} and each h ∈ 2I, test these vertex maps τ:

  family A: τ(v) = h · R(v) · h⁻¹       (inner-twist of R)
  family B: τ(v) = h · R(v)              (left-translate after R)
  family C: τ(v) = R(v) · h              (right-translate after R)
  family D: τ(v) = h · R(v) · k          (two-sided, with k = conj(h))

For each that (a) closes on 2I and (b) is an involution, compute the cycle
action and report cases that approach (2 fixed + 5 cross-K paired).

Pure inner automorphisms (R=id) preserve K-class — they cannot produce
cross-K pairing. Reported anyway for completeness.

Composing inner with σ never closes (σ doesn't close, and inner of a non-
closing map doesn't close). So families A,D with R involving σ are SKIPPED
unless the closure check passes empirically.
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


def conj_quat(q):
    """Quaternion conjugation: w + xi + yj + zk → w − xi − yj − zk."""
    w, x, y, z = q
    neg = lambda c: (-c[0], -c[1])
    return (w, neg(x), neg(y), neg(z))


def neg_quat(q):
    """Antipodal: q → −q."""
    return tuple((-c[0], -c[1]) for c in q)


def inv_quat(q):
    """Inverse of a unit quaternion: q⁻¹ = q̄ / |q|² = q̄ (norm 1)."""
    return conj_quat(q)


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

    # Build T_τ cycles + K-classes.
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
    print(f"K-multiset confirmation: {sorted(K_of_cycle)}")
    print(f"K=72 cycles: {[i for i, K in enumerate(K_of_cycle) if K == 72]}")
    print(f"K=0 cycles:  {[i for i, K in enumerate(K_of_cycle) if K == 0]}")
    print(f"K=52 cycles: {[i for i, K in enumerate(K_of_cycle) if K == 52]}")
    print(f"K=20 cycles: {[i for i, K in enumerate(K_of_cycle) if K == 20]}")

    K72 = next(i for i, K in enumerate(K_of_cycle) if K == 72)
    K0 = next(i for i, K in enumerate(K_of_cycle) if K == 0)
    K52 = sorted(i for i, K in enumerate(K_of_cycle) if K == 52)
    K20 = sorted(i for i, K in enumerate(K_of_cycle) if K == 20)

    # Pre-compute quaternion array and inverse table for fast access.
    q_arr = list(verts)
    inv_idx = [idx_of[qq_key(inv_quat(verts[i]))] for i in range(n)]

    def apply_map(fn):
        """Apply vertex→quaternion fn; return image-index list or None if escapes 2I."""
        out = [None] * n
        for i in range(n):
            r = fn(q_arr[i])
            j = idx_of.get(qq_key(r))
            if j is None:
                return None
            out[i] = j
        return out

    def is_involution(images):
        return all(images[images[i]] == i for i in range(n))

    def cycle_action(images):
        """Return (consistent, mapping cycle_index → cycle_index) or None if not consistent."""
        m = {}
        for ci, c in enumerate(cycles):
            tgt = {cycle_of[images[v]] for v in c}
            if len(tgt) != 1:
                return None
            m[ci] = next(iter(tgt))
        return m

    def classify_orbits(m):
        """Return (n_fixed, n_paired, n_cross_K_paired, n_within_K_paired, orbits)."""
        seen = set()
        orbits = []
        for ci in range(len(cycles)):
            if ci in seen:
                continue
            cur = m[ci]
            if cur == ci:
                orbits.append([ci])
                seen.add(ci)
            elif m[cur] == ci:
                orbits.append([ci, cur])
                seen.add(ci)
                seen.add(cur)
            else:
                # higher-order orbit; not an involution at cycle level
                orbits.append(("higher", ci, cur, m[cur]))
                seen.add(ci)
                seen.add(cur)
                seen.add(m[cur])
        n_fixed = sum(1 for o in orbits if isinstance(o, list) and len(o) == 1)
        pairs = [o for o in orbits if isinstance(o, list) and len(o) == 2]
        n_cross = sum(1 for o in pairs if K_of_cycle[o[0]] != K_of_cycle[o[1]])
        n_within = len(pairs) - n_cross
        return n_fixed, len(pairs), n_cross, n_within, orbits

    print()
    print("Scanning families A/B/C/D over h ∈ 2I and outer R ∈ {id, conj, "
          "antipodal, σ, σ∘conj, σ∘antipod, conj∘σ}…")
    print()

    target_hits = []
    near_misses = []

    families = ["A_inner", "B_left", "C_right", "D_two_sided_conj"]

    for r_name, R in OUTER_OPS.items():
        for family in families:
            for h_idx in range(n):
                h = q_arr[h_idx]
                h_inv = inv_quat(h)
                if family == "A_inner":
                    fn = lambda v, h=h, h_inv=h_inv, R=R: qq_mul(qq_mul(h, R(v)), h_inv)
                elif family == "B_left":
                    fn = lambda v, h=h, R=R: qq_mul(h, R(v))
                elif family == "C_right":
                    fn = lambda v, h=h, R=R: qq_mul(R(v), h)
                elif family == "D_two_sided_conj":
                    k = conj_quat(h)
                    fn = lambda v, h=h, k=k, R=R: qq_mul(qq_mul(h, R(v)), k)

                images = apply_map(fn)
                if images is None:
                    continue
                if not is_involution(images):
                    continue
                # Skip identity map
                if all(images[i] == i for i in range(n)):
                    continue
                ca = cycle_action(images)
                if ca is None:
                    continue
                n_fixed, n_paired, n_cross, n_within, orbits = classify_orbits(ca)

                # Filter to interesting structures
                if n_fixed == 2 and n_paired == 5 and n_cross == 5:
                    # TARGET STRUCTURE
                    fixed_cycles = [o[0] for o in orbits if isinstance(o, list) and len(o) == 1]
                    if {K_of_cycle[c] for c in fixed_cycles} == {72, 0}:
                        target_hits.append((r_name, family, h_idx, orbits))
                        print(f"*** TARGET HIT: R={r_name}, family={family}, h_idx={h_idx} ***")
                        for o in orbits:
                            if isinstance(o, list) and len(o) == 1:
                                print(f"    fixed cycle {o[0]}: K={K_of_cycle[o[0]]}")
                            elif isinstance(o, list) and len(o) == 2:
                                print(f"    pair {o[0]} ↔ {o[1]}: K={K_of_cycle[o[0]]} ↔ K={K_of_cycle[o[1]]}")
                        print()
                elif n_fixed >= 1 and n_cross >= 1:
                    near_misses.append((r_name, family, h_idx, n_fixed, n_paired, n_cross, n_within))

    print()
    print(f"Target hits: {len(target_hits)}")
    print(f"Near misses (any fixed and any cross-K pair): {len(near_misses)}")

    if not target_hits:
        # Show top near-misses by (n_fixed × n_cross)
        print()
        print("Top 20 near-misses by structure score:")
        ranked = sorted(near_misses,
                        key=lambda x: (x[5], x[3], -x[6]),  # cross, fixed, -within
                        reverse=True)
        for r_name, family, h_idx, nf, np_, nc, nw in ranked[:20]:
            print(f"  R={r_name:<14} family={family:<18} h={h_idx:3d}  "
                  f"fixed={nf} paired={np_} crossK={nc} withinK={nw}")

    print()
    print("Scan complete.")


if __name__ == "__main__":
    main()
