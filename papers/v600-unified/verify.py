"""Paper 5 verification — structural-spine cross-check.

Run from the repo root:
    PYTHONPATH=papers/v600-programme/lib python3 papers/v600-unified/verify.py

Exits 0 iff every assertion holds. This script does NOT prove
anything new; it computes Sigma_{V_600} from the shared library and
re-runs each foundation paper's headline number as a cross-check
that the synthesis paper imports nothing it cannot reproduce from
the shared exact infrastructure.

Cross-checks:
  1. State construction: |V_600| = 120, 12 T_tau-cycles each of
     length 10, K-multiset {72:1, 0:1, 52:5, 20:5}.
  2. Lemma 2.1 (V_24 / Dic_5 distinction): |Dic_5| = 20 and
     |V_24| = 24; Dic_5 != V_24.
  3. Bekenstein 1/4 (Paper 1): |gH cap V_24| = 4 for every coset
     of Dic_5 (both left and right tested for safety).
  4. Hawking quantum E_q = 5/2 (Paper 2): every sigma-mobile vertex
     has Euclidean |v - sigma(v)|^2 = 5/2.
  5. tau_sigma (Paper 3) properties P1-P4 plus antipodal
     compatibility hold for the canonical phase-0 lift.
  6. Operator-trace ratios (Paper 4):
     tr(I_C + P_72) = 13, tr(I_C - P_0) = 11.
  7. Phase-independence (Lemma 2.2): all 32 phase lifts of tau_sigma
     yield cycle permutations that pointwise fix Hhat and Chat.
"""
from __future__ import annotations

import itertools
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

LIB = Path(__file__).resolve().parents[1] / "v600-programme" / "lib"
if str(LIB) not in sys.path:
    sys.path.insert(0, str(LIB))

from vfd_v600.group import build_state, left_cosets, right_cosets
from vfd_v600.sigma import sigma_pair_energy, sigma_fixed_set, is_sigma_fixed
from vfd_v600.tau_sigma import load_tau_sigma, verify_tau_sigma
from vfd_v600.icosian import qq_key
from vfd_v600.operators import (
    identity_12, K_class_projector, add_op, sub_op, trace, trace_ratio,
    H_VFD, C_VFD,
)


def assert_log(cond, msg):
    if not cond:
        print(f"  FAIL: {msg}")
        sys.exit(1)
    print(f"  ok    {msg}")


def neg_quat(v):
    return tuple((-c[0], -c[1]) for c in v)


def cycle_perm(tau_sigma, cycles, cycle_of):
    out = {}
    for i, cycle in enumerate(cycles):
        targets = {cycle_of[tau_sigma[v]] for v in cycle}
        if len(targets) != 1:
            return None
        out[i] = targets.pop()
    return out


def main() -> int:
    state = build_state()
    verts = state["verts"]
    idx_of = state["idx_of"]
    n = state["n"]
    cycles = state["cycles"]
    cycle_of = state["cycle_of"]
    K_of_cycle = state["K_of_cycle"]
    Dic5 = state["Dic5"]

    print("Paper 5 — V_600 unified synthesis: structural-spine cross-check")
    print("=" * 64)

    # 1. State construction
    assert_log(n == 120, "|V_600| = 120")
    assert_log(len(cycles) == 12 and all(len(c) == 10 for c in cycles),
               "12 T_tau-cycles, each of length 10")
    K_count = Counter(K_of_cycle)
    expected_K = {72: 1, 0: 1, 52: 5, 20: 5}
    assert_log(dict(K_count) == expected_K,
               f"K-multiset {expected_K}")

    # 2. Lemma 2.1: V_24 / Dic_5 distinction
    V24 = sigma_fixed_set(state)
    assert_log(len(Dic5) == 20, "|Dic_5| = 20")
    assert_log(len(V24) == 24, "|V_24| = 24")
    assert_log(Dic5 != V24, "Dic_5 != V_24 (the two are NOT equal)")
    intersect = Dic5 & V24
    assert_log(len(intersect) == 4,
               f"|Dic_5 cap V_24| = {len(intersect)} = 4 (Bekenstein 4 σ-fixed in bulk)")

    # 2b. Dic_5 self-normalising / non-normal in 2I (Paper 1 spine fact).
    from vfd_v600.group import dic5_is_normal
    assert_log(not dic5_is_normal(state),
               "Dic_5 is NOT normal in 2I (Paper 1)")

    # 2c. Left cosets gH are NOT whole-cycle carriers (Paper 1 + Paper 3).
    # Each non-bulk left coset must (a) hit ALL 10 non-bulk cycles
    # and (b) contain exactly 2 vertices from each.
    from collections import Counter as _Counter
    L_pre = left_cosets(state)
    bad_L_cycle = []
    for ci_, coset in enumerate(L_pre):
        if coset == Dic5:
            continue  # bulk
        per_cycle = _Counter(cycle_of[v] for v in coset)
        non_bulk = {ci for ci in range(12) if K_of_cycle[ci] in (52, 20)}
        if set(per_cycle.keys()) != non_bulk:
            bad_L_cycle.append(("non-bulk-coverage", ci_))
        elif not all(c == 2 for c in per_cycle.values()):
            bad_L_cycle.append(("not 2 per cycle", ci_))
    assert_log(not bad_L_cycle,
               "non-bulk LEFT cosets gH are NOT whole-cycle carriers (cover all 10 non-bulk cycles with EXACTLY 2 vertices each)")

    # 3. Bekenstein 1/4 (Paper 1 cross-check)
    L = left_cosets(state)
    R = right_cosets(state)
    bad_L = [ci for ci, coset in enumerate(L) if len(coset & V24) != 4]
    bad_R = [ri for ri, coset in enumerate(R) if len(coset & V24) != 4]
    assert_log(not bad_L,
               "every left coset gH satisfies |gH cap V_24| = 4 (Paper 1)")
    assert_log(not bad_R,
               "every right coset Hg satisfies |Hg cap V_24| = 4 (Paper 1)")

    # 4. Hawking quantum (Paper 2 cross-check)
    energies_mobile = {sigma_pair_energy(verts[i]) for i in range(n)
                       if not is_sigma_fixed(verts[i])}
    energies_fixed = {sigma_pair_energy(verts[i]) for i in range(n)
                      if is_sigma_fixed(verts[i])}
    assert_log(energies_fixed == {Fraction(0)},
               "all 24 sigma-fixed vertices have |v - sigma(v)|^2 = 0")
    assert_log(energies_mobile == {Fraction(5, 2)},
               "all 96 sigma-mobile vertices have |v - sigma(v)|^2 = 5/2 (Paper 2)")

    # 5. tau_sigma (Paper 3 cross-check) — canonical phase-0 lift
    tau_sigma = load_tau_sigma(n=n)
    props = verify_tau_sigma(state, images=tau_sigma)
    assert_log(props["p1"], "tau_sigma is an involution (P1, Paper 3)")
    assert_log(props["p2"], "tau_sigma fixes Dic_5 pointwise (P2, Paper 3)")
    assert_log(props["p3"], "tau_sigma swaps K=52 ↔ K=20 within each non-bulk right coset (P3, Paper 3)")
    assert_log(props["p4"], "tau_sigma commutes with T_tau (P4, Paper 3)")

    antipodal_idx = [idx_of[qq_key(neg_quat(verts[i]))] for i in range(n)]
    antipodal_compat = all(tau_sigma[antipodal_idx[i]] == antipodal_idx[tau_sigma[i]]
                            for i in range(n))
    assert_log(antipodal_compat, "tau_sigma commutes with v |-> -v (Paper 3)")

    # 6. Operator-trace ratios (Paper 4 cross-check)
    P72 = K_class_projector(state, 72)
    P0  = K_class_projector(state, 0)
    P52 = K_class_projector(state, 52)
    P20 = K_class_projector(state, 20)
    assert_log(trace(P72) == 1 and trace(P0) == 1, "rk P_72 = rk P_0 = 1")
    assert_log(trace(P52) == 5 and trace(P20) == 5, "rk P_52 = rk P_20 = 5")
    sum_proj = add_op(add_op(P72, P0), add_op(P52, P20))
    assert_log(sum_proj == identity_12(),
               "P_72 + P_0 + P_52 + P_20 = I_C")
    H = H_VFD(state)
    Cop = C_VFD(state)
    assert_log(trace(H) == 13, "tr(I_C + P_72) = 13 (Paper 4 Theorem 4.1)")
    assert_log(trace(Cop) == 11, "tr(I_C - P_0)  = 11 (Paper 4 Theorem 4.1)")
    assert_log(trace_ratio(H) == Fraction(13, 12),
               "tr(I_C + P_72)/12 = 13/12")
    assert_log(trace_ratio(Cop) == Fraction(11, 12),
               "tr(I_C - P_0)/12 = 11/12")

    # 7. Phase-independence (Lemma 2.2 cross-check) — all 32 lifts.
    bulk_cycles = [i for i in range(12) if K_of_cycle[i] in (72, 0)]

    coset_pairs = []
    for coset in R:
        cyc_in = sorted({cycle_of[v] for v in coset})
        if any(K_of_cycle[c] in (72, 0) for c in cyc_in):
            continue
        K52 = next(c for c in cyc_in if K_of_cycle[c] == 52)
        K20 = next(c for c in cyc_in if K_of_cycle[c] == 20)
        coset_pairs.append((K52, K20))
    assert len(coset_pairs) == 5

    def check_phase(perm_dict):
        if perm_dict is None:
            return False
        if not all(perm_dict[i] == i for i in bulk_cycles):
            return False
        for coset in R:
            cyc_in = sorted({cycle_of[v] for v in coset})
            if any(K_of_cycle[c] in (72, 0) for c in cyc_in):
                continue
            a, b = cyc_in
            if {K_of_cycle[a], K_of_cycle[b]} != {52, 20}:
                return False
            if perm_dict[a] != b or perm_dict[b] != a:
                return False
        perm = [perm_dict[i] for i in range(12)]
        H_perm = [H[perm[i]] for i in range(12)]
        C_perm = [Cop[perm[i]] for i in range(12)]
        return H_perm == H and C_perm == Cop

    n_passed = 0
    for phase_combo in itertools.product([0, 5], repeat=5):
        cand = list(range(n))
        for (K52, K20), j in zip(coset_pairs, phase_combo):
            for k in range(10):
                v_idx = cycles[K52][k]
                w_idx = cycles[K20][(j + k) % 10]
                cand[v_idx] = w_idx
                cand[w_idx] = v_idx
        cand_perm = cycle_perm(cand, cycles, cycle_of)
        if check_phase(cand_perm):
            n_passed += 1
    assert_log(n_passed == 32,
               f"phase-independence: all 2^5 = 32 tau_sigma lifts pointwise fix Hhat and Chat")

    print("=" * 64)
    print("  EVERY ASSERTION PASS  ⇒  Sigma_{V_600} structural spine verified")
    print("                            (cross-checks for Papers 1, 2, 3, 4 all green)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
