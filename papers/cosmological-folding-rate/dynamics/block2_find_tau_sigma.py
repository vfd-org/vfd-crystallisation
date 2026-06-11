"""Block 2 — Find τ_σ: V_600 → V_600 producing 2-fixed + 5-paired cycle structure.

We have (Block 1):
  - 1 K=72 cycle, 1 K=0 cycle (bulk: must be τ_σ-fixed)
  - 5 K=52 cycles, 5 K=20 cycles (boundary: must form 5 pairs under τ_σ)

5 + 5 with each K-class odd-sized means τ_σ MUST cross K-classes
(K=52 ↔ K=20), giving 5 (K=52, K=20) pairs.

Test candidates (each as `R ∘ σ` or `R` directly), where σ is the
Galois twist on Q(√5):

  Candidate (a):  σ_Galois (alone) — already confirmed not closing on 2I
  Candidate (b):  conjugation v → v̄ (closes on 2I)
  Candidate (c):  antipodal v → −v (closes on 2I, equals T_τ⁵)
  Candidate (d):  σ ∘ conj (Galois then conjugation)
  Candidate (e):  σ ∘ antipodal
  Candidate (f):  conjugation ∘ σ followed by re-projection to 2I via norm-rescale
  Candidate (g):  left-multiplication by τ⁵ = −1 (same as antipodal)
  Candidate (h):  inner automorphism by τ²

For each candidate that DOES close on 2I, compute its action on cycles
and check whether it produces (2 fixed + 5 pairs across K-classes).
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


def main():
    verts = build_vertices()
    idx_of = vertex_index_map(verts)
    n = len(verts)
    one = (q_one(), q_zero(), q_zero(), q_zero())

    # Set up cycles + K-class (replicating Block 1)
    print("Setting up T_τ cycles + K-classes (Block 1 result)…")

    def order_of(g):
        result = one
        for k in range(1, 31):
            result = qq_mul(result, g)
            if qq_eq(result, one):
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

    # Euclidean shells from identity
    distance_sq = [qq_distance_sq(one, verts[j]) for j in range(n)]
    keys = [(float(d2[0]) + float(d2[1]) * (5 ** 0.5)) for d2 in distance_sq]
    unique = sorted(set(keys))
    d2_to_shell = {k: i for i, k in enumerate(unique)}
    shell = [d2_to_shell[k] for k in keys]
    K_of_cycle = [sum((shell[v] - 4) ** 2 for v in c) for c in cycles]
    print(f"K-class per cycle: {K_of_cycle}")

    # Helper: apply candidate involution to a vertex; return target idx, or None if outside 2I
    def apply_to_index(i, fn):
        result = fn(verts[i])
        return idx_of.get(qq_key(result))

    # Candidate involutions
    candidates = {
        "conj":           lambda q: conj_quat(q),
        "antipodal":      lambda q: neg_quat(q),
        "sigma":          lambda q: sigma_quat(q),
        "sigma+conj":     lambda q: sigma_quat(conj_quat(q)),
        "sigma+antipod":  lambda q: sigma_quat(neg_quat(q)),
        "conj+sigma":     lambda q: conj_quat(sigma_quat(q)),
    }

    print()
    print(f"{'candidate':<18} {'closes':>7} {'fixed_v':>9} {'cycle_orbits':>50}")
    print("-" * 90)

    for name, fn in candidates.items():
        # Check closure
        images = []
        all_in = True
        for i in range(n):
            j = apply_to_index(i, fn)
            if j is None:
                all_in = False
                break
            images.append(j)
        if not all_in:
            print(f"{name:<18} {'no':>7} {'-':>9}  -")
            continue

        # Count fixed vertices
        fixed_v = sum(1 for i in range(n) if images[i] == i)

        # Compute action on cycles
        cycle_action = {}
        cycle_action_consistent = True
        for ci, c in enumerate(cycles):
            target_cycles = {cycle_of[images[v]] for v in c}
            if len(target_cycles) != 1:
                cycle_action_consistent = False
                cycle_action[ci] = sorted(target_cycles)
            else:
                cycle_action[ci] = next(iter(target_cycles))

        if not cycle_action_consistent:
            print(f"{name:<18} {'yes':>7} {fixed_v:>9}  inconsistent: {cycle_action}")
            continue

        # Compute orbit structure
        seen = set()
        orbits = []
        for ci in range(len(cycles)):
            if ci in seen:
                continue
            orbit = [ci]
            cur = cycle_action[ci]
            seen.add(ci)
            if cur != ci and cur not in seen:
                orbit.append(cur)
                seen.add(cur)
                # Order 2: closure
                if cycle_action[cur] != ci:
                    orbits.append(("higher_order", orbit))
                    continue
            orbits.append(orbit)

        n_fixed = sum(1 for o in orbits if len(o) == 1)
        n_paired = sum(1 for o in orbits if len(o) == 2 and isinstance(o, list))

        # Cross-K vs within-K for the pairs
        cross_K_pairs = 0
        within_K_pairs = 0
        for o in orbits:
            if len(o) == 2 and isinstance(o, list):
                Ks = {K_of_cycle[ci] for ci in o}
                if len(Ks) == 2:
                    cross_K_pairs += 1
                else:
                    within_K_pairs += 1

        print(f"{name:<18} {'yes':>7} {fixed_v:>9}  "
              f"fixed={n_fixed} paired={n_paired} "
              f"(crossK={cross_K_pairs}, withinK={within_K_pairs})")

        if n_fixed == 2 and n_paired == 5 and cross_K_pairs == 5:
            print(f"   *** {name} GIVES THE TARGET STRUCTURE ***")
            print(f"       (2 σ-fixed cycles + 5 cross-K pairs)")
            for o in orbits:
                if len(o) == 1:
                    print(f"       fixed cycle: K={K_of_cycle[o[0]]}")
                elif len(o) == 2:
                    print(f"       pair: K={K_of_cycle[o[0]]} ↔ K={K_of_cycle[o[1]]}")


if __name__ == "__main__":
    main()
