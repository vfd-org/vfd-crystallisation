"""Phase 4 acceptance (a): Eichler mass-formula consistency.

mass(level p31) = mass(level 1) * (N(p31)+1) = (1/60) * 32 = 8/15,
and it must equal  sum_i 1/w_i  over the geometric ideal classes, with
w_i = 60/orbit_size_i the point-stabiliser orders in A_5.
"""
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "route_b"))
import ideal_classes as ic


def test_mass_consistency():
    data = ic.compute_orbits()
    assert data["mass_matches"], data
    assert data["mass_computed"] == (8, 15)
    assert data["mass_predicted"] == (8, 15)


def test_weights_are_stabilisers():
    data = ic.compute_orbits()
    # each weight = 60 / orbit_size, and sum of orbit sizes = N(level)+1 = 32
    assert sum(data["orbit_sizes"]) == 32
    inferred = sorted(60 // s for s in data["orbit_sizes"])
    assert inferred == sorted(data["weights"])
    # mass = sum orbit_size / 60
    mass = sum(Fraction(s, 60) for s in data["orbit_sizes"])
    assert mass == Fraction(8, 15)


def run():
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("  ok:", name)
    print("ALL MASS_FORMULA_GATE TESTS PASS")


if __name__ == "__main__":
    run()
