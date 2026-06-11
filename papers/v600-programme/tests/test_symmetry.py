"""Symmetry orbit tests (Paper 2 — bilateral V_24 action on V_600)."""
from __future__ import annotations

from vfd_v600.symmetry import (
    is_bilateral_v24_transitive_on_mobile,
    bilateral_v24_orbits,
    sigma_commutes_with_left_mul,
)
from vfd_v600.sigma import sigma_fixed_set


def test_sigma_commutes_with_v24_left_mul(state):
    """σ(g·v) = g·σ(v) for every g ∈ V_24, v ∈ V_600."""
    sf = sorted(sigma_fixed_set(state))
    for g in sf:
        assert sigma_commutes_with_left_mul(state, g)


def test_bilateral_v24_orbits_partition_v600(state):
    orbits = bilateral_v24_orbits(state)
    union = set().union(*orbits)
    assert union == set(range(state["n"]))
    for i, o1 in enumerate(orbits):
        for o2 in orbits[i+1:]:
            assert o1.isdisjoint(o2)


def test_bilateral_v24_transitive_on_mobile(state):
    """The Hawking-quantum symmetry certificate (Paper 2)."""
    transitive, sizes = is_bilateral_v24_transitive_on_mobile(state)
    assert transitive, f"σ-mobile not single bilateral orbit; sizes: {sizes}"
    assert sizes == [24, 96]


def test_bilateral_v24_orbit_partition_aligns_with_sigma_fixed(state):
    """The size-24 orbit is V_24 itself; the size-96 orbit is σ-mobile."""
    sf = sigma_fixed_set(state)
    orbits = bilateral_v24_orbits(state)
    fixed_orbits = [o for o in orbits if o & sf]
    assert len(fixed_orbits) == 1
    assert fixed_orbits[0] == sf
    mobile_orbits = [o for o in orbits if not (o & sf)]
    assert len(mobile_orbits) == 1
    assert len(mobile_orbits[0]) == 96
