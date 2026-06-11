"""Paper 3 verification — exact certificate for the τ_σ construction.

Run from the repo root:
    PYTHONPATH=papers/v600-programme/lib python3 papers/tau-sigma-construction/verify.py

Exits 0 iff every assertion holds. The certificate covers:

  1. Setup carrier: V_600 = 2I, |H| = 20 (= Dic_5), 24 = |V_24|.
  2. Right cosets Hg are the τ_σ construction carrier (Paper 1 Lemma):
     each non-bulk right coset is one whole K=52 cycle plus one whole
     K=20 cycle. Left cosets are NOT whole-cycle carriers — regression
     check that the 2-per-cycle distribution holds.
  3. Per non-bulk right coset, the symmetric σ-projection maximin
     score
        s(j) := min_{k ∈ Z/10} min(⟨σ(v_k), w_{(j+k) mod 10}⟩,
                                    ⟨σ(w_{(j+k) mod 10}), v_k⟩)
     under the icosian trace metric selects exactly two phases
     j ∈ {0, 5}, with s(0)=s(5)=0 and s(j)=-5/4 for all other phases.
  4. The Z_2^5 lift count is 2^5 = 32 canonical τ_σ candidates differing
     by independent phase choices per coset.
  5. The phase-(0,0,0,0,0) lift, rebuilt from scratch by Route K above,
     equals the loaded canonical map data/tau_sigma_canonical.txt
     vertex-by-vertex.
  6. The rebuilt map satisfies the four canonical properties P1–P4:
     P1 involution; P2 fixes Dic_5 pointwise; P3 swaps K=52 ↔ K=20 in
     each non-bulk right coset; P4 commutes with T_τ.
  7. Antipodal compatibility: τ_σ commutes with v ↦ −v.
"""
from __future__ import annotations

import sys
import itertools
from collections import Counter
from fractions import Fraction
from pathlib import Path

LIB = Path(__file__).resolve().parents[1] / "v600-programme" / "lib"
if str(LIB) not in sys.path:
    sys.path.insert(0, str(LIB))

from vfd_v600.icosian import (
    qq_mul, qq_conjugate, qq_key, qq_eq,
    q_zero, q_one, q5_sign, q5_lt,
)
from vfd_v600.group import build_state, left_cosets, right_cosets
from vfd_v600.sigma import sigma_quat, sigma_fixed_set
from vfd_v600.tau_sigma import load_tau_sigma, verify_tau_sigma


def assert_log(cond, msg):
    if not cond:
        print(f"  FAIL: {msg}")
        sys.exit(1)
    print(f"  ok    {msg}")


def trace_score(v, w):
    """Trace inner product ⟨v, w⟩_trace := Tr_{K/Q}(Re(v · conj(w))).

    For a Q(√5) element a + b√5, the K/Q trace is 2a (sum of a + b√5
    and σ(a+b√5) = a − b√5). This is the standard rational-valued
    trace bilinear form on the icosian/E_8 lattice (Conway–Sloane,
    Elkies); on the cross-Galois pairs used here values lie in
    (1/4)·Z and may be ±5/4 etc. Returns a Fraction.
    """
    p = qq_mul(v, qq_conjugate(w))[0]
    return 2 * p[0]


def neg_quat(v):
    return tuple((-c[0], -c[1]) for c in v)


def main() -> int:
    state = build_state()
    verts = state["verts"]
    idx_of = state["idx_of"]
    n = state["n"]
    cycles = state["cycles"]
    cycle_of = state["cycle_of"]
    K = state["K_of_cycle"]
    Dic5 = state["Dic5"]

    print("Paper 3 — τ_σ construction verification")
    print("=" * 64)

    # 1. Setup
    assert_log(n == 120, "|V_600| = 120")
    assert_log(len(Dic5) == 20, "|Dic_5| = 20")
    sf = sigma_fixed_set(state)
    assert_log(len(sf) == 24, "|V_24| = 24")

    # 2. Right cosets are the construction carrier (one whole K=52 + one whole K=20).
    R = right_cosets(state)
    assert_log(len(R) == 6, "exactly 6 right cosets")
    L = left_cosets(state)
    bad_R = []
    for ri, coset in enumerate(R):
        if coset == Dic5:
            continue
        cyc_in = sorted({cycle_of[v] for v in coset})
        # Each non-bulk right coset must contain exactly 2 cycles, both whole.
        if len(cyc_in) != 2:
            bad_R.append((ri, "wrong cycle count"))
            continue
        if not all(set(cycles[ci]).issubset(coset) for ci in cyc_in):
            bad_R.append((ri, "cycles not whole"))
            continue
        Ks = sorted(K[ci] for ci in cyc_in)
        if Ks != [20, 52]:
            bad_R.append((ri, f"K classes {Ks}"))
    assert_log(not bad_R,
               "every non-bulk right coset = one whole K=52 cycle + one whole K=20 cycle")

    # Regression check on left cosets: 2 per cycle, NOT whole.
    bad_L = []
    for ci_, coset in enumerate(L):
        if coset == Dic5:
            continue
        per_cycle = Counter(cycle_of[v] for v in coset)
        # Must hit all 10 non-bulk cycles, with 2 each.
        non_bulk = {ci for ci in range(12) if K[ci] in (52, 20)}
        if set(per_cycle.keys()) != non_bulk:
            bad_L.append((ci_, "missing non-bulk cycles"))
        if not all(c == 2 for c in per_cycle.values()):
            bad_L.append((ci_, "non-uniform 2/cycle"))
    assert_log(not bad_L,
               "left cosets are NOT whole-cycle carriers (2 vertices per non-bulk cycle)")

    # 3. Identify (K=52, K=20) cycle pairs per non-bulk right coset.
    coset_pairs = []  # list of (ri, K52_cycle_idx, K20_cycle_idx)
    for ri, coset in enumerate(R):
        if coset == Dic5:
            continue
        cyc_in = sorted({cycle_of[v] for v in coset})
        K52 = next(ci for ci in cyc_in if K[ci] == 52)
        K20 = next(ci for ci in cyc_in if K[ci] == 20)
        coset_pairs.append((ri, K52, K20))
    assert_log(len(coset_pairs) == 5, "exactly 5 non-bulk right cosets")

    # 4. Per coset: σ-projection maximin under the icosian trace
    #    metric selects exactly {0, 5} with score 0; all other phases
    #    have score -5/4 (FULL TABLE asserted, not just the maximin).
    print()
    print(f"  σ-projection score table per coset (icosian trace metric):")
    print(f"    {'coset':<8}{'K52':<6}{'K20':<6}phase 0..9 min-scores")
    canonical_phases_per_coset = []
    bad_table = []
    for ri, K52, K20 in coset_pairs:
        min_scores = []
        for j in range(10):
            scores_fwd, scores_back = [], []
            for k in range(10):
                v = verts[cycles[K52][k]]
                w = verts[cycles[K20][(j + k) % 10]]
                sv = sigma_quat(v)
                # Forward score: ⟨σ(v), w⟩
                scores_fwd.append(trace_score(sv, w))
                # Symmetric backward score: ⟨σ(w), v⟩
                sw = sigma_quat(w)
                scores_back.append(trace_score(sw, v))
            # Symmetric-maximin: min over k of min(forward, backward)
            mins_per_k = [min(f, b) for f, b in zip(scores_fwd, scores_back)]
            min_scores.append(min(mins_per_k))
        # Verify exact score table: phases {0, 5} score 0; all others -5/4.
        expected_table = [Fraction(0) if j in (0, 5) else Fraction(-5, 4)
                          for j in range(10)]
        if min_scores != expected_table:
            bad_table.append((ri, min_scores, expected_table))
        max_of_min = max(min_scores)
        winning_phases = [j for j in range(10) if min_scores[j] == max_of_min]
        canonical_phases_per_coset.append(winning_phases)
        print(f"    {ri:<8}{K52:<6}{K20:<6}{[str(s) for s in min_scores]}")
    assert_log(not bad_table,
               "exact score table per coset: phases {0,5}→0, "
               "all other phases→-5/4 (matches Theorem 4.1)")
    expected = [[0, 5]] * 5
    assert_log(canonical_phases_per_coset == expected,
               "every non-bulk right coset has maximin phases {0, 5} — Z_2^5 = 2^5 = 32 lifts")

    # 5. Rebuild τ_σ from scratch with phase (0,0,0,0,0); compare to canonical.
    rebuilt = list(range(n))
    for (ri, K52, K20), phases in zip(coset_pairs, canonical_phases_per_coset):
        j = 0  # canonical phase
        for k in range(10):
            v_idx = cycles[K52][k]
            w_idx = cycles[K20][(j + k) % 10]
            rebuilt[v_idx] = w_idx
            rebuilt[w_idx] = v_idx
    canonical_loaded = load_tau_sigma(n=n)
    assert_log(rebuilt == canonical_loaded,
               "rebuilt τ_σ (phase 0⁵) matches data/tau_sigma_canonical.txt vertex-by-vertex")

    # 6. P1-P4 properties of the rebuilt map.
    props = verify_tau_sigma(state, images=rebuilt)
    assert_log(props["p1"], "P1: τ_σ is an involution")
    assert_log(props["p2"], "P2: τ_σ fixes Dic_5 pointwise (20 vertices)")
    assert_log(props["p3"], "P3: τ_σ swaps K=52 ↔ K=20 in each non-bulk coset")
    assert_log(props["p4"], "P4: τ_σ ∘ T_τ = T_τ ∘ τ_σ (T_τ-equivariant)")

    # 7. Antipodal compatibility: τ_σ ∘ (−1) = (−1) ∘ τ_σ.
    antipodal_idx = [idx_of[qq_key(neg_quat(verts[i]))] for i in range(n)]
    antipodal_compat = all(rebuilt[antipodal_idx[i]] == antipodal_idx[rebuilt[i]]
                            for i in range(n))
    assert_log(antipodal_compat, "τ_σ commutes with antipodal map v ↦ −v")

    # 7b. Right-coset preservation (POST-BUILD assertion, not by construction).
    R_set = [frozenset(c) for c in R]
    coset_of_idx = {v: ci for ci, c in enumerate(R_set) for v in c}
    rc_pres = all(coset_of_idx[rebuilt[v]] == coset_of_idx[v] for v in range(n))
    assert_log(rc_pres, "τ_σ preserves right cosets setwise (post-build check)")

    # 8. Total number of canonical lifts: 2^5 = 32 by independent phase choices.
    n_lifts = 1
    for p in canonical_phases_per_coset:
        n_lifts *= len(p)
    assert_log(n_lifts == 32, f"Z_2^5 lift count: {n_lifts} = 2^5 = 32")

    # 9. Lift count by enumeration: build all 32 candidates, all are involutions
    #    fixing Dic_5 with K-swap.
    valid_lifts = 0
    for phase_combo in itertools.product(*canonical_phases_per_coset):
        cand = list(range(n))
        for (ri, K52, K20), j in zip(coset_pairs, phase_combo):
            for k in range(10):
                v_idx = cycles[K52][k]
                w_idx = cycles[K20][(j + k) % 10]
                cand[v_idx] = w_idx
                cand[w_idx] = v_idx
        cand_props = verify_tau_sigma(state, images=cand)
        if all(cand_props.values()):
            valid_lifts += 1
    assert_log(valid_lifts == 32,
               f"all 32 phase combinations yield valid τ_σ involutions")

    print("=" * 64)
    print("  EVERY ASSERTION PASS  ⇒  τ_σ canonical map rebuilt and verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
