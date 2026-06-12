"""V_600 group structure: T_τ-cycles, K-classes, Dic_5 bulk subgroup.

All operations are exact (no floating point). The 12 T_τ-cycles, the
K-multiset {72:1, 0:1, 52:5, 20:5}, and the bulk subgroup
Dic_5 = (K=72) ∪ (K=0) are computed deterministically from build_vertices().
"""

from __future__ import annotations

from .icosian import (
    q_zero, q_one, qq_mul, qq_eq, qq_key,
    build_vertices, vertex_index_map, qq_distance_sq,
    q5_sign, q5_lt,
)


def _order_of(g, one):
    r = one
    for k in range(1, 31):
        r = qq_mul(r, g)
        if qq_eq(r, one):
            return k
    return -1


def build_state():
    """Return a frozen V_600 state dict with everything downstream needs.

    Keys:
        verts        — list of 120 icosian quaternions.
        idx_of       — dict qq_key(v) -> index in verts.
        n            — 120.
        one          — quaternion identity.
        tau          — order-10 element used to generate T_τ.
        T            — list[120] of permutation T[i] = idx(τ * verts[i]).
        cycles       — list of cycles (each a list of vertex indices, length 10).
        cycle_of     — dict vertex_idx -> cycle_idx.
        shell        — list[120] of integer shell index (0..8) for each vertex.
        K_of_cycle   — list[12] of K-class integer per cycle.
        Dic5         — set of 20 vertex indices forming the bulk subgroup.
        bulk_cycle_idx — list of 2 cycle indices (K=72 + K=0).
    """
    verts = build_vertices()
    idx_of = vertex_index_map(verts)
    n = len(verts)
    one = (q_one(), q_zero(), q_zero(), q_zero())

    tau = next(v for v in verts if _order_of(v, one) == 10)
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

    # Shell index by EXACT comparison on Q(√5) — q5_sign / q5_lt from
    # vfd_v600.icosian; never float-compare.
    distance_sq = [qq_distance_sq(one, verts[j]) for j in range(n)]

    # Insertion-sort distance² values to a unique list using exact comparator.
    unique_d2 = []
    for d2 in distance_sq:
        if not any(d2 == u for u in unique_d2):
            placed = False
            for i, u in enumerate(unique_d2):
                if q5_lt(d2, u):
                    unique_d2.insert(i, d2)
                    placed = True
                    break
            if not placed:
                unique_d2.append(d2)
    shell = [next(i for i, u in enumerate(unique_d2) if u == d2) for d2 in distance_sq]

    K_of_cycle = [sum((shell[v] - 4) ** 2 for v in c) for c in cycles]

    bulk_cycle_idx = [ci for ci, K in enumerate(K_of_cycle) if K in (72, 0)]
    Dic5 = set()
    for ci in bulk_cycle_idx:
        Dic5.update(cycles[ci])

    return {
        "verts": verts,
        "idx_of": idx_of,
        "n": n,
        "one": one,
        "tau": tau,
        "T": T,
        "cycles": cycles,
        "cycle_of": cycle_of,
        "shell": shell,
        "K_of_cycle": K_of_cycle,
        "Dic5": Dic5,
        "bulk_cycle_idx": bulk_cycle_idx,
    }


def left_cosets(state):
    """Return list of left cosets gH (g varying, H=Dic_5) as sets of vertex indices.

    First coset is Dic_5 itself; the remaining 5 are non-bulk cosets.
    Non-bulk left cosets contain 2 vertices from each of the 10 non-bulk
    T_τ-cycles (10 K=52 + 10 K=20 in aggregate, NOT whole cycle unions —
    see right_cosets for the whole-cycle decomposition). Dic_5 is non-normal
    in 2I, so left and right coset families are distinct.
    """
    verts = state["verts"]
    idx_of = state["idx_of"]
    Dic5 = state["Dic5"]
    n = state["n"]

    seen = set()
    cosets = []
    bulk_first = None
    for i in range(n):
        if i in seen:
            continue
        coset = set()
        for h in Dic5:
            prod = qq_mul(verts[i], verts[h])  # gH: g first, then h ∈ H
            coset.add(idx_of[qq_key(prod)])
        if bulk_first is None and i in Dic5:
            cosets.insert(0, coset)
            bulk_first = True
        else:
            cosets.append(coset)
        seen.update(coset)
    return cosets


def right_cosets(state):
    """Return list of right cosets Hg (g varying) as sets of vertex indices.

    Distinct from left cosets when H is non-normal; the load-bearing 4/16
    incidence holds for BOTH families and Paper 1 verifies both explicitly.
    """
    verts = state["verts"]
    idx_of = state["idx_of"]
    Dic5 = state["Dic5"]
    n = state["n"]

    seen = set()
    cosets = []
    bulk_first = None
    for i in range(n):
        if i in seen:
            continue
        coset = set()
        for h in Dic5:
            prod = qq_mul(verts[h], verts[i])  # Hg: h ∈ H first, then g
            coset.add(idx_of[qq_key(prod)])
        if bulk_first is None and i in Dic5:
            cosets.insert(0, coset)
            bulk_first = True
        else:
            cosets.append(coset)
        seen.update(coset)
    return cosets


def dic5_is_normal(state):
    """Return True iff Dic_5 is normal in 2I. (It is not.)"""
    return left_cosets(state) == right_cosets(state)


def find_dic5_presentation(state):
    """Search for a, b ∈ Dic_5 with the binary dihedral presentation
        a^10 = 1, b^2 = a^5, b a b^{-1} = a^{-1}.
    Returns (idx(a), idx(b)) on success, raises ValueError on failure.
    """
    from .icosian import qq_conjugate, qq_norm_sq
    verts = state["verts"]
    idx_of = state["idx_of"]
    Dic5 = state["Dic5"]
    one = state["one"]

    def power(g, k):
        r = one
        for _ in range(k):
            r = qq_mul(r, g)
        return r

    def order(g):
        for k in range(1, 21):
            if qq_eq(power(g, k), one):
                return k
        return -1

    # Find a of order 10
    a_idx = None
    for i in Dic5:
        if order(verts[i]) == 10:
            a_idx = i
            break
    if a_idx is None:
        raise ValueError("no order-10 element in Dic_5")
    a = verts[a_idx]
    a5 = power(a, 5)              # a^5 = -1 (the unique non-identity order-2 element)
    a_inv = power(a, 9)            # a^{-1} = a^9 since a^10 = 1

    # Find b in Dic_5 with b^2 = a^5 and b a b^{-1} = a^{-1}.
    for j in Dic5:
        b = verts[j]
        if not qq_eq(qq_mul(b, b), a5):
            continue
        # b^{-1}: since b is in 2I (unit icosian quaternion), b^{-1} = conjugate(b).
        # Verify |b|² = 1 (rational, no √5 part); skip if not unit.
        nsq = qq_norm_sq(b)
        if nsq != (1, 0):
            continue
        b_inv = qq_conjugate(b)
        bab = qq_mul(qq_mul(b, a), b_inv)
        if qq_eq(bab, a_inv):
            return a_idx, j
    raise ValueError("no b ∈ Dic_5 satisfying binary-dihedral presentation")
