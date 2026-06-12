"""Test suite for the VFD Phase-Braid Calculator.

Covers the acceptance criteria from WO-VFD-PHASE-BRAID-CALCULATOR-001:
number inspection, lifted arithmetic, Collatz closure, prime trace, and the
self-adjoint finite-window sanity check.
"""

from __future__ import annotations

import math
from fractions import Fraction

import pytest

from vfd_phase_braid import (
    boundary_capacity as bc,
    collatz_closure as cc,
    lifted_arithmetic as la,
    phase_maps as pm,
    prime_trace as pt,
    self_adjoint as sa,
)
from vfd_phase_braid.vfd_number import VFDNumber


# --------------------------------------------------------------------------
# Number inspection  (>= 50 cases via the 1..60 sweep + specific checks)
# --------------------------------------------------------------------------

def _reference_factorize(n: int) -> dict:
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


@pytest.mark.parametrize("n", range(1, 61))
def test_inspection_factorisation_round_trips(n):
    vn = VFDNumber.lift(n)
    assert vn.factors == _reference_factorize(n)
    prod = 1
    for p, e in vn.factors.items():
        prod *= p ** e
    assert prod == n
    assert vn.parity == n % 2
    assert vn.triad_phase == n % 3
    assert vn.braid_label == {0: "A", 1: "B", 2: "C"}[n % 3]


def test_inspection_examples_from_work_order():
    # 27 = 3^3, odd, v2=0, v3=3, triadic expansion node
    vn = VFDNumber.lift(27)
    assert vn.factors == {3: 3}
    assert vn.parity == 1
    assert vn.v2 == 0 and vn.v3 == 3
    assert vn.closure_class == "triadic expansion node"
    # 12 = 2^2 * 3, even, v2=2, phase 0
    vn12 = VFDNumber.lift(12)
    assert vn12.v2 == 2
    assert vn12.triad_phase == 0 and vn12.braid_label == "A"


def test_inspection_large_value():
    # acceptance: inspection must work for integers up to at least 1e9
    n = 1_000_000_007  # prime
    vn = VFDNumber.lift(n)
    assert vn.is_prime
    assert vn.factors == {n: 1}
    n2 = 999_999_937  # prime
    assert VFDNumber.lift(n2).is_prime


def test_p_adic_and_phi_phase():
    assert pm.p_adic_valuation(48, 2) == 4   # 48 = 16 * 3
    assert pm.p_adic_valuation(54, 3) == 3   # 54 = 2 * 27
    assert pm.p_adic_valuation(7, 2) == 0
    phase = pm.phi_log_phase(pm.PHI ** 5)
    assert phase == pytest.approx(0.0, abs=1e-9) or phase == pytest.approx(1.0, abs=1e-9)


# --------------------------------------------------------------------------
# Lifted arithmetic  (>= 50 cases) — standard result correct + triad homomorphism
# --------------------------------------------------------------------------

@pytest.mark.parametrize("a", range(1, 11))
@pytest.mark.parametrize("b", range(1, 11))
def test_lifted_add_multiply_correct_and_homomorphic(a, b):
    r_add = la.add(a, b)
    assert r_add.ordinary_result == a + b
    assert r_add.closure_residual == 0          # triad phase is additive
    r_mul = la.multiply(a, b)
    assert r_mul.ordinary_result == a * b
    assert r_mul.closure_residual == 0          # triad phase is multiplicative


def test_lifted_subtract_and_divide():
    r = la.subtract(13, 5)
    assert r.ordinary_result == 8
    assert r.lifted_result.value == 8
    rd = la.divide(8, 13)
    assert rd.ordinary_result == Fraction(8, 13)
    assert rd.lifted_result is None             # non-integer stays a label
    rd2 = la.divide(12, 4)
    assert rd2.ordinary_result == Fraction(3, 1)
    assert rd2.lifted_result.value == 3


def test_lifted_power_correct():
    r = la.power(3, 3)
    assert r.ordinary_result == 27
    assert r.lifted_result.factors == {3: 3}
    assert r.closure_residual == 0


def test_work_order_phase_transition_string():
    # 8 (leg C) + 13 (leg B) -> 21 (leg A)
    r = la.add(8, 13)
    assert r.phase_transition == "C + B -> A"
    assert r.lifted_result.factors == {3: 1, 7: 1}


# --------------------------------------------------------------------------
# Collatz closure  (>= 100 cases via 1..120 sweep)
# --------------------------------------------------------------------------

def _reference_steps(n: int) -> int:
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps


@pytest.mark.parametrize("n", range(1, 121))
def test_collatz_reaches_closure(n):
    a = cc.analyze(n)
    assert a.trajectory[0] == n
    assert a.trajectory[-1] == 1
    assert a.steps_to_closure == _reference_steps(n)
    assert a.escape_flags == []                 # all converge


def test_collatz_known_trajectories():
    a27 = cc.analyze(27)
    assert a27.steps_to_closure == 111
    assert a27.max_value == 9232
    assert a27.regime == "closure-dominant"     # it does reach 1
    a871 = cc.analyze(871)
    assert a871.steps_to_closure == 178
    assert a871.max_value == 190996


def test_collatz_capacity_positive_for_convergent():
    # converging runs must have net positive log-capacity (compression wins)
    for n in (3, 7, 27, 97, 871):
        v = bc.collatz_capacity(n)
        assert v.Q > 0
        assert v.classification == "closure-dominant"


# --------------------------------------------------------------------------
# Prime trace  (acceptance: primes up to 10,000)
# --------------------------------------------------------------------------

def test_prime_count_to_10000():
    trace = pt.analyze(10_000)
    assert trace.count == 1229                  # pi(10000)
    assert trace.primes[:5] == [2, 3, 5, 7, 11]
    assert trace.max_gap == 36                  # gap before 9587


def test_prime_is_prime_matches_sieve():
    primes = set(pt.sieve(2000))
    for n in range(2, 2000):
        assert pm.is_prime(n) == (n in primes)


def test_prime_triad_distribution():
    trace = pt.analyze(1000)
    # only the prime 3 sits in triad phase 0
    assert trace.triad_distribution.get(0, 0) == 1


# --------------------------------------------------------------------------
# Self-adjoint finite-window sanity
# --------------------------------------------------------------------------

def test_self_adjoint_runs_small():
    for limit in (4, 8, 16):
        r = sa.analyze("collatz", limit)
        assert r.matrix_size == limit
        assert math.isfinite(r.residual_norm)
        # a discovered form must actually satisfy BT = T^T B
        if r.B_signature != "none":
            assert r.residual_norm < 1e-6


def test_self_adjoint_caps_large_limit():
    r = sa.analyze("collatz", 500)
    assert r.matrix_size <= sa.DEFAULT_MAX_SIZE
    assert any("exceeds dense cap" in n for n in r.notes)


def test_transition_matrix_is_functional():
    T = sa.collatz_transition_matrix(16)
    # every row has exactly one 1 (deterministic map)
    assert (T.sum(axis=1) == 1).all()
