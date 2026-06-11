"""24-cell incidence: the load-bearing 4 σ-fixed per coset → S/A = 1/4 fact."""
from __future__ import annotations

from fractions import Fraction

from vfd_v600.sigma import sigma_fixed_set
from vfd_v600.group import left_cosets, right_cosets


def test_24cell_size(state):
    sf = sigma_fixed_set(state)
    assert len(sf) == 24


def test_24cell_intersect_dic5_is_4(state):
    sf = sigma_fixed_set(state)
    assert len(sf & state["Dic5"]) == 4


def test_24cell_outside_dic5_is_20(state):
    sf = sigma_fixed_set(state)
    assert len(sf - state["Dic5"]) == 20


def test_each_left_coset_contains_exactly_4_sigma_fixed(state):
    """The Bekenstein-1/4 main theorem (Paper 1) — left coset side."""
    sf = sigma_fixed_set(state)
    for coset in left_cosets(state):
        assert len(coset & sf) == 4


def test_each_right_coset_contains_exactly_4_sigma_fixed(state):
    """The Bekenstein-1/4 main theorem (Paper 1) — right coset side.

    Required because Dic_5 is non-normal: the result must hold on both
    sides for the paper's main claim to be hostile-review robust.
    """
    sf = sigma_fixed_set(state)
    for coset in right_cosets(state):
        assert len(coset & sf) == 4


def test_each_non_bulk_coset_S_over_A_is_one_quarter(state):
    """Per non-bulk coset: 4 σ-fixed / 16 σ-mobile = 1/4."""
    sf = sigma_fixed_set(state)
    cosets = left_cosets(state)
    for coset in cosets[1:]:  # skip bulk = Dic_5 itself
        S = len(coset & sf)
        A = len(coset - sf)
        assert S == 4
        assert A == 16
        assert Fraction(S, A) == Fraction(1, 4)


def test_aggregate_boundary_S_over_A_is_one_quarter(state):
    sf = sigma_fixed_set(state)
    cosets = left_cosets(state)
    boundary = set().union(*cosets[1:])
    S = len(boundary & sf)
    A = len(boundary - sf)
    assert S == 20
    assert A == 80
    assert Fraction(S, A) == Fraction(1, 4)
