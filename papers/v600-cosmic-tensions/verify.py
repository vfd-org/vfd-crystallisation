"""Paper 4 verification — exact certificate for the trace identities.

Run from the repo root:
    PYTHONPATH=papers/v600-programme/lib python3 papers/v600-cosmic-tensions/verify.py

Exits 0 iff every assertion holds. Covers:

  1. State construction: |V_600| = 120, 12 T_tau-cycles each of length
     10, K-multiset {72:1, 0:1, 52:5, 20:5}.
  2. K-class projector ranks match the K-multiset.
  3. Resolution of identity: P_72 + P_0 + P_52 + P_20 = I_C.
  4. tr(I_C + P_72) = 13 and tr(I_C - P_0) = 11 (Theorem 4.1).
  5. Trace ratios 13/12 and 11/12.
  6. Phase-independence: the canonical tau_sigma cycle action fixes
     K=72 and K=0 cycles and exchanges (K=52, K=20) cycles within
     each non-bulk right coset; the trace identities are unchanged.
  7. Ablation: rk-5 alternatives have traces 17 and 7.
"""
from __future__ import annotations

import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

LIB = Path(__file__).resolve().parents[1] / "v600-programme" / "lib"
if str(LIB) not in sys.path:
    sys.path.insert(0, str(LIB))

from vfd_v600.group import build_state, right_cosets
from vfd_v600.operators import (
    identity_12, K_class_projector, add_op, sub_op, trace, trace_ratio,
    H_VFD, C_VFD,
)
from vfd_v600.tau_sigma import load_tau_sigma


def assert_log(cond, msg):
    if not cond:
        print(f"  FAIL: {msg}")
        sys.exit(1)
    print(f"  ok    {msg}")


def cycle_perm(tau_sigma, cycles, cycle_of):
    """Cycle-level permutation induced by a vertex-level tau_sigma.

    Returns dict {cycle_index -> cycle_index} if tau_sigma descends to
    a well-defined cycle permutation (every vertex of cycle i maps to
    a single target cycle), else None.
    """
    out = {}
    for i, cycle in enumerate(cycles):
        targets = {cycle_of[tau_sigma[v]] for v in cycle}
        if len(targets) != 1:
            return None
        out[i] = targets.pop()
    return out


def main() -> int:
    state = build_state()
    n = state["n"]
    cycles = state["cycles"]
    K_of_cycle = state["K_of_cycle"]
    cycle_of = state["cycle_of"]

    print("Paper 4 — V_600 cosmic tensions: trace certificate")
    print("=" * 64)

    # 1. Setup
    assert_log(n == 120, "|V_600| = 120")
    assert_log(len(cycles) == 12, "exactly 12 T_tau-cycles")
    assert_log(all(len(c) == 10 for c in cycles), "every cycle has length 10")
    K_count = Counter(K_of_cycle)
    expected = {72: 1, 0: 1, 52: 5, 20: 5}
    assert_log(dict(K_count) == expected, f"K-multiset {expected}")

    # 2. K-class projector ranks
    P72 = K_class_projector(state, 72)
    P0  = K_class_projector(state, 0)
    P52 = K_class_projector(state, 52)
    P20 = K_class_projector(state, 20)
    assert_log(trace(P72) == 1, "rk P_72 = 1")
    assert_log(trace(P0)  == 1, "rk P_0  = 1")
    assert_log(trace(P52) == 5, "rk P_52 = 5")
    assert_log(trace(P20) == 5, "rk P_20 = 5")

    # 3. Resolution of identity
    sum_proj = add_op(add_op(P72, P0), add_op(P52, P20))
    assert_log(sum_proj == identity_12(),
               "resolution of identity: P_72 + P_0 + P_52 + P_20 = I_C")

    # 4. Trace identities
    H = H_VFD(state)
    C = C_VFD(state)
    assert_log(trace(H) == 13, "tr(I_C + P_72) = 13  (Theorem 4.1)")
    assert_log(trace(C) == 11, "tr(I_C - P_0)  = 11  (Theorem 4.1)")

    # 5. Trace ratios
    assert_log(trace_ratio(H) == Fraction(13, 12),
               "trace ratio: tr(H) / 12 = 13/12")
    assert_log(trace_ratio(C) == Fraction(11, 12),
               "trace ratio: tr(C) / 12 = 11/12")

    # 6. Phase-independence (Lemma 4.1).
    # We check the canonical lift directly, then enumerate all 32
    # phase combinations from Paper 3 and confirm the cycle-level
    # permutation in EVERY case (a) is well-defined, (b) fixes K=72
    # and K=0 cycles, (c) exchanges (K=52, K=20) cycles within each
    # non-bulk right coset, and hence (d) leaves Hhat and Chat
    # POINTWISE invariant (not just in trace).
    import itertools

    # First the canonical lift (sanity check).
    tau_sigma = load_tau_sigma(n=n)
    cycle_image = cycle_perm(tau_sigma, cycles, cycle_of)
    assert_log(cycle_image is not None,
               "canonical tau_sigma descends to a well-defined cycle permutation")

    R = right_cosets(state)
    bulk_cycles = [i for i in range(12) if K_of_cycle[i] in (72, 0)]

    def check_phase_independence(perm_dict):
        if perm_dict is None:
            return False
        # Bulk cycles fixed.
        if not all(perm_dict[i] == i for i in bulk_cycles):
            return False
        # Non-bulk right cosets pair K=52 with K=20.
        for coset in R:
            cyc_in = sorted({cycle_of[v] for v in coset})
            if any(K_of_cycle[c] in (72, 0) for c in cyc_in):
                continue
            if len(cyc_in) != 2:
                return False
            a, b = cyc_in
            if {K_of_cycle[a], K_of_cycle[b]} != {52, 20}:
                return False
            if perm_dict[a] != b or perm_dict[b] != a:
                return False
        # Pointwise invariance of H and C under the induced action.
        perm = [perm_dict[i] for i in range(12)]
        H_perm = [H[perm[i]] for i in range(12)]
        C_perm = [C[perm[i]] for i in range(12)]
        return H_perm == H and C_perm == C

    assert_log(check_phase_independence(cycle_image),
               "canonical tau_sigma: cycle action fixes K=72/K=0, swaps K=52<->K=20, and pointwise-fixes Hhat and Chat")

    # Enumerate all 32 phases.
    coset_pairs = []  # (K52_idx, K20_idx) per non-bulk right coset
    for coset in R:
        cyc_in = sorted({cycle_of[v] for v in coset})
        if any(K_of_cycle[c] in (72, 0) for c in cyc_in):
            continue
        K52 = next(c for c in cyc_in if K_of_cycle[c] == 52)
        K20 = next(c for c in cyc_in if K_of_cycle[c] == 20)
        coset_pairs.append((K52, K20))
    assert len(coset_pairs) == 5

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
        if check_phase_independence(cand_perm):
            n_passed += 1
    assert_log(n_passed == 32,
               f"all 2^5 = 32 phase lifts of tau_sigma leave Hhat and Chat pointwise invariant ({n_passed} passed)")

    # 7. Ablation: rk-5 alternatives.
    H52 = add_op(identity_12(), P52)
    C20 = sub_op(identity_12(), P20)
    assert_log(trace(H52) == 17, "ablation: tr(I_C + P_52) = 17")
    assert_log(trace(C20) == 7,  "ablation: tr(I_C - P_20) = 7")
    assert_log(trace_ratio(H52) == Fraction(17, 12),
               "ablation: tr(I_C + P_52)/12 = 17/12")
    assert_log(trace_ratio(C20) == Fraction(7, 12),
               "ablation: tr(I_C - P_20)/12 = 7/12")

    # Layer-2 numerical observation summary (no assertion — informational).
    H0_planck = Fraction(6736, 100)         # 67.36 km/s/Mpc
    H0_pred = float(H0_planck * Fraction(13, 12))
    H0_sh0es_central = 73.04
    H0_sh0es_sigma = 1.04
    H0_residual_sigma = abs(H0_sh0es_central - H0_pred) / H0_sh0es_sigma

    S8_planck = Fraction(832, 1000)          # 0.832 (Planck 2018)
    S8_pred = float(S8_planck * Fraction(11, 12))
    S8_kids_central = 0.766
    S8_kids_lower_sigma = 0.014   # KiDS asymmetric: -0.014 below central
    S8_kids_upper_sigma = 0.020
    # Predicted (0.7627) is BELOW central, so use the lower KiDS error
    if S8_pred < S8_kids_central:
        directional_err = S8_kids_lower_sigma
    else:
        directional_err = S8_kids_upper_sigma
    S8_residual_sigma_directional = abs(S8_kids_central - S8_pred) / directional_err

    print()
    print("  Layer-2 numerical observation (informational, not asserted):")
    print(f"    H_0:  {H0_pred:.4f} km/s/Mpc  vs SH0ES {H0_sh0es_central}±{H0_sh0es_sigma}")
    print(f"          residual ≈ {H0_residual_sigma:.3f}σ")
    print(f"    S_8:  {S8_pred:.4f}  vs KiDS-1000 {S8_kids_central} (+{S8_kids_upper_sigma}/-{S8_kids_lower_sigma})")
    print(f"          directional residual (below central, lower err {directional_err}):")
    print(f"          ≈ {S8_residual_sigma_directional:.3f}σ")

    print("=" * 64)
    print("  EVERY ASSERTION PASS  ⇒  Paper 4 trace certificate verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
