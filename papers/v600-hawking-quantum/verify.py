"""Paper 2 verification — exact certificate for the σ-pair Hawking quantum.

Run from the repo root:
    PYTHONPATH=papers/v600-programme/lib python3 papers/v600-hawking-quantum/verify.py

Exits 0 iff every assertion holds. Certificate covers:

  1. |V_600| = 120, |V_24| = 24, |σ-mobile| = 96.
  2. E(v) := |v − σ(v)|²_Euclidean: σ-fixed → 0; σ-mobile → 5/2 EXACTLY,
     uniform across all 96 mobile vertices.
  3. Coordinate proof: for the icosian basis, the difference v − σ(v)
     has exactly two nonzero coordinates of magnitude √5/2 each, hence
     |v − σ(v)|² = 5/4 + 5/4 = 5/2.
  4. Symmetry certificate: bilateral V_24 action g·v·h commutes with σ
     and is transitive on the σ-mobile sector (single orbit of size 96).
  5. First-law identity per non-bulk Dic_5 coset:
     A = 16 (channels), S = 4 (anchors, by Paper 1),
     E = A · E_q = 40, T_H = E_q = 5/2,
     E = T_H · A, S = A/4, T_H · S = E/4.
  6. Aggregate over 5 boundary cosets:
     A_tot = 80, S_tot = 20, E_tot = 200, T_H · S_tot = E_tot/4.
"""
from __future__ import annotations

import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

LIB = Path(__file__).resolve().parents[1] / "v600-programme" / "lib"
if str(LIB) not in sys.path:
    sys.path.insert(0, str(LIB))

from vfd_v600.icosian import q_sub, qq_norm_sq
from vfd_v600.group import build_state, left_cosets, right_cosets
from vfd_v600.sigma import (
    sigma_fixed_set, sigma_pair_energy, sigma_quat, is_sigma_fixed,
)
from vfd_v600.symmetry import (
    is_bilateral_v24_transitive_on_mobile,
    bilateral_v24_orbits,
    sigma_commutes_with_left_mul,
    sigma_commutes_with_right_mul,
    sigma_commutes_with_bilateral,
)


def assert_log(cond, msg):
    if not cond:
        print(f"  FAIL: {msg}")
        sys.exit(1)
    print(f"  ok    {msg}")


def main() -> int:
    state = build_state()
    verts = state["verts"]
    n = state["n"]
    sf = sigma_fixed_set(state)

    print("Paper 2 — V_600 Hawking quantum verification")
    print("=" * 64)

    # 1. Cardinalities
    assert_log(n == 120, "|V_600| = 120")
    assert_log(len(sf) == 24, "|V_24| = 24 (σ-fixed sublattice)")
    mobile = set(range(n)) - sf
    assert_log(len(mobile) == 96, "|σ-mobile| = |V_600 \\ V_24| = 96")

    # 2. Energy spectrum: 0 on σ-fixed, 5/2 on σ-mobile (uniform)
    fixed_energies = {sigma_pair_energy(verts[i]) for i in sf}
    assert_log(fixed_energies == {Fraction(0)},
               "σ-fixed: E(v) = 0 for all 24 vertices")
    mobile_energies = {sigma_pair_energy(verts[i]) for i in mobile}
    assert_log(mobile_energies == {Fraction(5, 2)},
               f"σ-mobile: E(v) = 5/2 exactly for all 96 vertices "
               f"(uniform: {mobile_energies})")

    # 3. Coordinate proof: v - σ(v) has exactly two nonzero coordinates
    #    of squared magnitude 5/4 each (totaling |v-σ(v)|² = 5/2).
    bad = []
    # Coordinate proof: for each σ-mobile v, v − σ(v) has exactly TWO
    # nonzero coordinates, each in pure-√5 form (0, ±1/2) representing
    # ±√5/2. The squared real magnitude of (0, ±1/2) is (√5/2)² = 5/4,
    # so |v − σ(v)|² = 5/4 + 5/4 = 5/2 in exact rational arithmetic.
    for i in mobile:
        v = verts[i]
        sv = sigma_quat(v)
        diff = tuple(q_sub(v[k], sv[k]) for k in range(4))
        nonzero = [d for d in diff if d != (Fraction(0), Fraction(0))]
        if not (len(nonzero) == 2 and
                all(d[0] == 0 and abs(d[1]) == Fraction(1, 2)
                    for d in nonzero)):
            bad.append((i, nonzero))
    assert_log(not bad,
               "coordinate proof: v − σ(v) has exactly 2 nonzero coords "
               "of value ±√5/2 (verified all 96 mobile vertices)")

    # 4. Symmetry certificate: bilateral V_24 action commutes with σ
    #    and is transitive on σ-mobile.
    sf_list = sorted(sf)
    all_left = all(sigma_commutes_with_left_mul(state, g) for g in sf_list)
    assert_log(all_left,
               "σ commutes with left-mul by every g ∈ V_24 (24 generators)")
    all_right = all(sigma_commutes_with_right_mul(state, h) for h in sf_list)
    assert_log(all_right,
               "σ commutes with right-mul by every h ∈ V_24 (24 generators)")
    # Bilateral check: σ(g·v·h) = g·σ(v)·h for all g, h ∈ V_24, v ∈ V_600.
    # Combinatorially: 24 × 24 = 576 (g, h) pairs, each scanning 120 v.
    all_bilateral = all(sigma_commutes_with_bilateral(state, g, h)
                        for g in sf_list for h in sf_list)
    assert_log(all_bilateral,
               "σ commutes with bilateral action g·v·h for all 576 (g,h) ∈ V_24²")

    transitive, orbit_sizes = is_bilateral_v24_transitive_on_mobile(state)
    assert_log(transitive and orbit_sizes == [24, 96],
               f"bilateral V_24 action: σ-fixed is one orbit (size 24); "
               f"σ-mobile is one orbit (size 96).  Orbit sizes: {orbit_sizes}")

    # 5. First-law identity for ALL Dic_5 cosets (bulk + non-bulk),
    #    both left and right families. Note: even the bulk coset Dic_5
    #    has |Dic_5 ∩ V_24| = 4 (Paper 1, Lemma 24cell incidence with H),
    #    so A = 16 and S = 4 uniformly across all cosets.
    print()
    print(f"  First-law identity per Dic_5 coset (left + right):")
    print(f"    {'side':<8}{'coset':<6}{'kind':<10}"
          f"{'A':<5}{'S':<5}{'E':<6}{'T_H = E/A':<12}{'T_H · S = E/4':<14}")
    L = left_cosets(state)
    R = right_cosets(state)
    bad_law = []
    for coset_family, label in ((L, "left "), (R, "right")):
        for ci, coset in enumerate(coset_family):
            A_set = coset - sf
            S_set = coset & sf
            A, S = len(A_set), len(S_set)
            E = sum(sigma_pair_energy(verts[i]) for i in A_set)
            T_H = E / A
            kind = "bulk" if ci == 0 else "non-bulk"
            check = (A == 16 and S == 4 and E == Fraction(40)
                     and T_H == Fraction(5, 2)
                     and T_H * S == E / 4)
            if not check:
                bad_law.append((label, ci, A, S, E, T_H))
            print(f"    {label}   {ci:<6}{kind:<10}{A:<5}{S:<5}{E!s:<6}"
                  f"{str(T_H):<12}{str(T_H * S):<14}")
    assert_log(not bad_law,
               "first-law identity holds uniformly for ALL 12 cosets "
               "(A=16, S=4, E=40, T_H=5/2 — bulk coset has same incidence "
               "because |Dic_5 ∩ V_24| = 4 by Paper 1)")

    # 6. Aggregate
    boundary = set().union(*L[1:])
    S_tot = len(boundary & sf)
    A_tot = len(boundary - sf)
    E_tot = sum(sigma_pair_energy(verts[i]) for i in boundary - sf)
    T_H = Fraction(5, 2)
    assert_log(S_tot == 20 and A_tot == 80 and E_tot == Fraction(200),
               f"aggregate boundary: A = {A_tot}, S = {S_tot}, E = {E_tot}")
    assert_log(T_H * S_tot == E_tot / 4,
               f"aggregate first law: T_H · S = {T_H * S_tot} = E/4 = {E_tot/4}")

    print("=" * 64)
    print("  EVERY ASSERTION PASS  ⇒  E_q = 5/2 monochromatic + first law exact")
    return 0


if __name__ == "__main__":
    sys.exit(main())
