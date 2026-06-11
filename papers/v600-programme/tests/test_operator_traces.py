"""Operator-trace identity tests (Paper 4)."""
from __future__ import annotations

from fractions import Fraction

from vfd_v600.operators import (
    H_VFD, C_VFD, K_class_projector, identity_12, trace, trace_ratio,
)
from vfd_v600.sigma import sigma_pair_energy, sigma_fixed_set, is_sigma_fixed


def test_trace_identity_is_12(state):
    assert trace(identity_12()) == 12


def test_K_projector_ranks(state):
    assert trace(K_class_projector(state, 72)) == 1
    assert trace(K_class_projector(state, 0)) == 1
    assert trace(K_class_projector(state, 52)) == 5
    assert trace(K_class_projector(state, 20)) == 5


def test_H_VFD_trace_is_13(state):
    assert trace(H_VFD(state)) == 13


def test_C_VFD_trace_is_11(state):
    assert trace(C_VFD(state)) == 11


def test_H_VFD_trace_ratio(state):
    assert trace_ratio(H_VFD(state)) == Fraction(13, 12)


def test_C_VFD_trace_ratio(state):
    assert trace_ratio(C_VFD(state)) == Fraction(11, 12)


def test_sigma_fixed_have_zero_pair_energy(state):
    verts = state["verts"]
    sf = sigma_fixed_set(state)
    for i in sf:
        assert sigma_pair_energy(verts[i]) == 0


def test_sigma_mobile_have_uniform_pair_energy(state):
    """The Hawking-quantum monochromatic-spectrum result (Paper 2)."""
    verts = state["verts"]
    n = state["n"]
    energies = {sigma_pair_energy(verts[i]) for i in range(n) if not is_sigma_fixed(verts[i])}
    assert energies == {Fraction(5, 2)}


def test_first_law_per_coset(state):
    """Per non-bulk coset: T_H · S = E_total / 4."""
    from vfd_v600.group import left_cosets
    verts = state["verts"]
    sf = sigma_fixed_set(state)

    E_q = Fraction(5, 2)
    coset_S = 4
    coset_A = 16
    E_per_coset = coset_A * E_q

    for coset in left_cosets(state)[1:]:
        S = len(coset & sf)
        A = len(coset - sf)
        E = sum(sigma_pair_energy(verts[i]) for i in coset - sf)
        assert S == coset_S
        assert A == coset_A
        assert E == E_per_coset
        T_H = E / A
        assert T_H == E_q
        assert T_H * S == E / 4
