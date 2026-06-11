"""Paper 1 verification — exact finite-arithmetic certificate.

Run from the repo root:
    PYTHONPATH=papers/v600-programme/lib python3 papers/bekenstein-incidence/verify.py

Exits 0 iff EVERY assertion holds. The certificate covers:

  1. |V_600| = 120 (exact enumeration).
  2. Every v ∈ V_600 has unit norm |v|² = 1 (exact, all 120).
  3. Group closure: every product v·w (all 14400 pairs) lies in V_600.
  4. T_τ-cycle decomposition for the canonical τ: 12 cycles of length 10,
     K-multiset {72:1, 0:1, 52:5, 20:5}.
  5. Bulk subgroup H = (K=72)∪(K=0): |H|=20, contains 1, closed under
     multiplication (all 400 pairs), and admits an explicit binary-dihedral
     presentation (a,b) with ⟨a,b⟩ = H verified by enumeration.
  6. H is self-normalizing: gH ≠ Hg for ALL g ∉ H (100 elements). Hence
     N_G(H) = H, and H is non-normal in G with index 6.
  7. V_24 = V_600 ∩ σ(V_600): the 24 σ-fixed vertices form the
     coordinate-rational sublattice.
  8. Per-coset incidence theorem (left and right cosets, both six each):
     |C| = 20, |C ∩ V_24| = 4, |C \\ V_24| = 16, with the four-element
     intersections printed explicitly.
  9. Aggregate boundary: S = 20, A = 80, S/A = 1/4.
 10. τ-independence: the same 4/16 incidence holds for every order-10
     τ ∈ 2I (all 24 candidates) and every resulting bulk subgroup H_τ.

Each verified claim corresponds to a numbered acceptance criterion in
papers/bekenstein-incidence/WO.md.
"""
from __future__ import annotations

import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

LIB = Path(__file__).resolve().parents[1] / "v600-programme" / "lib"
if str(LIB) not in sys.path:
    sys.path.insert(0, str(LIB))

from vfd_v600.icosian import (
    qq_mul, qq_eq, qq_key, qq_norm_sq, qq_distance_sq,
    q_zero, q_one, build_vertices, vertex_index_map,
)
from vfd_v600.group import (
    build_state, left_cosets, right_cosets, dic5_is_normal,
    find_dic5_presentation, _order_of,
)
from vfd_v600.sigma import sigma_fixed_set, sigma_quat


def assert_log(cond, msg):
    if not cond:
        print(f"  FAIL: {msg}")
        sys.exit(1)
    print(f"  ok    {msg}")


def main() -> int:
    state = build_state()
    verts = state["verts"]
    idx_of = state["idx_of"]
    n = state["n"]
    one = state["one"]
    Dic5 = state["Dic5"]

    print("Paper 1 — Bekenstein 1/4 incidence verification")
    print("=" * 64)

    # --- 1. Vertex count ---
    assert_log(n == 120, "|V_600| = 120")

    # --- 2. Unit norm (all 120) ---
    norm_one = (Fraction(1), Fraction(0))
    bad = [i for i in range(n) if qq_norm_sq(verts[i]) != norm_one]
    assert_log(not bad, f"every v ∈ V_600 has |v|² = 1 (checked all {n})")

    # --- 3. Exhaustive group closure (14400 products) ---
    nonclosed = []
    for i in range(n):
        for j in range(n):
            prod = qq_mul(verts[i], verts[j])
            if qq_key(prod) not in idx_of:
                nonclosed.append((i, j))
                break
        if nonclosed:
            break
    assert_log(not nonclosed, "exhaustive closure: all 14400 products lie in V_600")

    # --- 4. T_τ-cycles + K-multiset (canonical τ) ---
    assert_log(len(state["cycles"]) == 12 and all(len(c) == 10 for c in state["cycles"]),
               "T_τ: 12 cycles each of length 10")
    K_multi = Counter(state["K_of_cycle"])
    assert_log(dict(K_multi) == {72: 1, 0: 1, 52: 5, 20: 5},
               f"K-multiset = {dict(K_multi)}")

    # --- 5. Bulk subgroup H ---
    assert_log(len(Dic5) == 20, "|H| = 20")
    assert_log(idx_of[qq_key(one)] in Dic5, "1 ∈ H")
    nc_pairs = []
    for i in Dic5:
        for j in Dic5:
            prod_idx = idx_of[qq_key(qq_mul(verts[i], verts[j]))]
            if prod_idx not in Dic5:
                nc_pairs.append((i, j))
                break
        if nc_pairs:
            break
    assert_log(not nc_pairs, "H closed under multiplication (all 400 H×H pairs)")

    a_idx, b_idx = find_dic5_presentation(state)
    assert_log(a_idx in Dic5 and b_idx in Dic5,
               f"presentation: a (idx {a_idx}, order 10), b (idx {b_idx}); "
               "a^10=1, b²=a⁵, bab⁻¹=a⁻¹")

    # ⟨a, b⟩ = H equality check (closure of <a,b> equals H)
    a, b = verts[a_idx], verts[b_idx]
    gen_set = {qq_key(one)}
    frontier = [one]
    while frontier:
        new_frontier = []
        for g in frontier:
            for h in (a, b):
                p = qq_mul(g, h)
                k = qq_key(p)
                if k not in gen_set:
                    gen_set.add(k)
                    new_frontier.append(p)
        frontier = new_frontier
    gen_idx = {idx_of[k] for k in gen_set}
    assert_log(gen_idx == Dic5, "⟨a, b⟩ = H (generated subgroup equals bulk)")

    # --- 6. H is self-normalizing (N_G(H) = H) ---
    L = left_cosets(state)
    R = right_cosets(state)
    distinct_pairs = []
    for g in range(n):
        if g in Dic5:
            continue
        gH = {idx_of[qq_key(qq_mul(verts[g], verts[h]))] for h in Dic5}
        Hg = {idx_of[qq_key(qq_mul(verts[h], verts[g]))] for h in Dic5}
        if gH == Hg:
            distinct_pairs.append(g)
    assert_log(not distinct_pairs,
               f"all 100 g ∉ H satisfy gH ≠ Hg ⇒ N_G(H) = H, H self-normalizing")
    assert_log(not dic5_is_normal(state),
               "H is non-normal in G with index 6")

    # Direct check used by lem:cosetkpair (left-coset 2-per-cycle proof):
    # for every g ∉ H, g⁻¹ τ g ∉ H, so T_τ does not preserve any non-bulk gH.
    from vfd_v600.icosian import qq_conjugate
    a_idx_global = a_idx  # canonical τ for this state is verts[a_idx]
    tau_canon = verts[a_idx_global]
    bad_g = []
    for g in range(n):
        if g in Dic5:
            continue
        ginv = qq_conjugate(verts[g])
        conj = qq_mul(qq_mul(ginv, tau_canon), verts[g])
        if idx_of[qq_key(conj)] in Dic5:
            bad_g.append(g)
    assert_log(not bad_g,
               "for every g ∉ H, g⁻¹τg ∉ H ⇒ T_τ moves every non-bulk gH")

    # --- 7. V_24 = σ-fixed sublattice ---
    sf = sigma_fixed_set(state)
    assert_log(len(sf) == 24, "|V_24| = 24 (σ-fixed sublattice)")
    sigma_image = {qq_key(sigma_quat(verts[i])) for i in range(n)}
    intersect = sigma_image & set(idx_of.keys())
    assert_log({idx_of[k] for k in intersect} == sf,
               "V_600 ∩ σ(V_600) = V_24 (verified explicitly)")
    assert_log(len(sf & Dic5) == 4, "|H ∩ V_24| = 4")
    assert_log(len(sf - Dic5) == 20, "|V_24 \\ H| = 20 (4 per non-bulk coset × 5 cosets)")

    # --- 8. Per-coset incidence (left and right) with explicit 4-element intersections ---
    print()
    print(f"  Left cosets gH (with explicit σ-fixed elements):")
    print(f"    {'coset':<8}{'size':<6}{'σ-fixed':<10}{'σ-mobile':<11}{'S/A':<8}{'σ-fixed indices'}")
    coset_failures = []
    for ci, coset in enumerate(L):
        S_set = coset & sf
        A_set = coset - sf
        S, A = len(S_set), len(A_set)
        if not (len(coset) == 20 and S == 4 and A == 16):
            coset_failures.append(("left", ci, len(coset), S, A))
        print(f"    {ci:<8}{len(coset):<6}{S:<10}{A:<11}{Fraction(S,A)!s:<8}{sorted(S_set)}")
    assert_log(not coset_failures, "left coset incidence: 6×(20, 4, 16)")

    print(f"  Right cosets Hg (with explicit σ-fixed elements):")
    print(f"    {'coset':<8}{'size':<6}{'σ-fixed':<10}{'σ-mobile':<11}{'S/A':<8}{'σ-fixed indices'}")
    coset_failures_R = []
    for ci, coset in enumerate(R):
        S_set = coset & sf
        A_set = coset - sf
        S, A = len(S_set), len(A_set)
        if not (len(coset) == 20 and S == 4 and A == 16):
            coset_failures_R.append(("right", ci, len(coset), S, A))
        print(f"    {ci:<8}{len(coset):<6}{S:<10}{A:<11}{Fraction(S,A)!s:<8}{sorted(S_set)}")
    assert_log(not coset_failures_R, "right coset incidence: 6×(20, 4, 16)")

    # Coset partition: union of L is V_600, mutually disjoint.
    union_L = set().union(*L)
    assert_log(union_L == set(range(n)), "left cosets partition V_600")
    union_R = set().union(*R)
    assert_log(union_R == set(range(n)), "right cosets partition V_600")

    # --- 9. Aggregate boundary ratio ---
    boundary = set().union(*L[1:])
    S_agg, A_agg = len(boundary & sf), len(boundary - sf)
    assert_log(S_agg == 20 and A_agg == 80 and Fraction(S_agg, A_agg) == Fraction(1, 4),
               f"aggregate boundary S/A = {S_agg}/{A_agg} = 1/4")

    # --- 10. τ-independence sweep: full theorem-grade certificate ---
    order10 = [i for i in range(n) if _order_of(verts[i], one) == 10]
    assert_log(len(order10) == 24, f"|{{order-10 elements}}| = 24")

    distinct_Hs = set()
    bad_subgroup, bad_left, bad_right, bad_pres = [], [], [], []
    for ti in order10:
        tau = verts[ti]
        T_t = [idx_of[qq_key(qq_mul(tau, verts[i]))] for i in range(n)]
        visited = [False] * n
        cycles_t = []
        for s in range(n):
            if visited[s]:
                continue
            c = []
            cur = s
            while not visited[cur]:
                visited[cur] = True
                c.append(cur)
                cur = T_t[cur]
            cycles_t.append(c)
        shell = state["shell"]
        K_t = [sum((shell[v] - 4) ** 2 for v in c) for c in cycles_t]
        bulk = [ci for ci, K in enumerate(K_t) if K in (72, 0)]
        H_t = frozenset().union(*[frozenset(cycles_t[ci]) for ci in bulk])
        distinct_Hs.add(H_t)

        # |H_t| = 20 + identity in H_t + closure under multiplication.
        if len(H_t) != 20:
            bad_subgroup.append(ti); continue
        if idx_of[qq_key(one)] not in H_t:
            bad_subgroup.append(ti); continue
        closed = True
        for i in H_t:
            for j in H_t:
                if idx_of[qq_key(qq_mul(verts[i], verts[j]))] not in H_t:
                    closed = False
                    break
            if not closed:
                break
        if not closed:
            bad_subgroup.append(ti); continue

        # Dic_5 presentation: order-10 generator a in H_t (we have τ=verts[ti]
        # which is order 10 and lies in H_t by construction); search for b.
        a_t = tau
        r = one
        for _ in range(5):
            r = qq_mul(r, a_t)
        a5_t = r
        r = one
        for _ in range(9):
            r = qq_mul(r, a_t)
        ainv_t = r
        from vfd_v600.icosian import qq_conjugate
        b_found = False
        for jj in H_t:
            bq = verts[jj]
            if qq_norm_sq(bq) != (Fraction(1), Fraction(0)):
                continue
            if not qq_eq(qq_mul(bq, bq), a5_t):
                continue
            bab = qq_mul(qq_mul(bq, a_t), qq_conjugate(bq))
            if qq_eq(bab, ainv_t):
                b_found = True
                break
        if not b_found:
            bad_pres.append(ti); continue

        # Left and right coset partitions and 4/16 incidence on both sides.
        seenL = set(); cosets_L = []
        for i in range(n):
            if i in seenL:
                continue
            c_set = {idx_of[qq_key(qq_mul(verts[i], verts[h]))] for h in H_t}
            cosets_L.append(c_set); seenL.update(c_set)
        seenR = set(); cosets_R = []
        for i in range(n):
            if i in seenR:
                continue
            c_set = {idx_of[qq_key(qq_mul(verts[h], verts[i]))] for h in H_t}
            cosets_R.append(c_set); seenR.update(c_set)
        if not (len(cosets_L) == 6 and seenL == set(range(n)) and
                all(len(c) == 20 and len(c & sf) == 4 for c in cosets_L)):
            bad_left.append(ti); continue
        if not (len(cosets_R) == 6 and seenR == set(range(n)) and
                all(len(c) == 20 and len(c & sf) == 4 for c in cosets_R)):
            bad_right.append(ti); continue

    assert_log(not bad_subgroup,
               f"all 24 H_τ are subgroups of order 20 (closure + identity)")
    assert_log(not bad_pres,
               f"all 24 H_τ admit binary-dihedral presentation (a, b)")
    assert_log(not bad_left, "all 24 H_τ left cosets give 4/16 incidence")
    assert_log(not bad_right, "all 24 H_τ right cosets give 4/16 incidence")
    assert_log(len(distinct_Hs) == 6,
               f"24 τ-choices yield exactly 6 distinct H_τ subgroups")

    # G-conjugacy: every H_τ is conjugate to the canonical Dic_5 in G.
    canonical = frozenset(Dic5)
    conjugate_orbit = set()
    for g in range(n):
        ginv = qq_conjugate(verts[g])  # unit icosian inverse
        ghg_inv = frozenset(
            idx_of[qq_key(qq_mul(qq_mul(verts[g], verts[h]), ginv))]
            for h in canonical)
        conjugate_orbit.add(ghg_inv)
    assert_log(distinct_Hs <= conjugate_orbit,
               "all 6 distinct H_τ are G-conjugate to the canonical Dic_5")

    print("=" * 64)
    print("  EVERY ASSERTION PASS  ⇒  S/A = 1/4 exact, τ-independent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
