"""Phase 4 acceptance (b): geometric Brandt-module dimension gate h == 2.

The dimension is the number of A_5 = I^1/{+-1} orbits on P^1(F_31).  We also
check the parameter-free supporting facts: the 120 icosian units land in
SL_2(F_31) (reduced norm 1), |P^1(F_31)| = 32 = N(level)+1, and the icosian
ring's trace-form Gram determinant is 5^4 = 625.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "route_b"))
import ideal_classes as ic
import quaternion_order as qo


def test_dimension_is_two():
    data, expected, status = ic.dimension_gate()
    assert expected == 2
    assert data["h"] == 2
    assert status == "PASS"


def test_orbit_sizes():
    data = ic.compute_orbits()
    assert data["orbit_sizes"] == [12, 20]


def test_units_in_sl2():
    data = ic.compute_orbits()
    assert data["unit_det_set"] == [1]               # reduced norm 1


def test_p1_size():
    data = ic.compute_orbits()
    assert len(data["p1_points"]) == 32              # N(level)+1


def test_icosian_gram_det():
    assert qo.ring().gram_det() == 625               # 5^4


def run():
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("  ok:", name)
    print("ALL BRANDT_DIMENSION_GATE TESTS PASS")


if __name__ == "__main__":
    run()
