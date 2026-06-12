"""Operators on the 12-dimensional T_τ-cycle space C ≅ Q^12.

Provides:
    K_class_projector(state, K) — diagonal projector onto cycles with K-class K.
    H_VFD(state)                — I_12 + P_72 (expansion observable).
    C_VFD(state)                — I_12 - P_0  (clustering observable).
    trace_ratio(op, baseline=12) — return Fraction of tr(op) over baseline.

Operators are returned as length-12 diagonal coefficient lists (Fraction)
because all entries are rational. No numpy dependency.
"""

from __future__ import annotations

from fractions import Fraction


def identity_12():
    return [Fraction(1)] * 12


def K_class_projector(state, K):
    """Diagonal length-12 projector onto cycles with K_of_cycle == K."""
    K_of_cycle = state["K_of_cycle"]
    return [Fraction(1) if K_of_cycle[i] == K else Fraction(0) for i in range(12)]


def add_op(a, b):
    return [a[i] + b[i] for i in range(12)]


def sub_op(a, b):
    return [a[i] - b[i] for i in range(12)]


def trace(op):
    return sum(op, Fraction(0))


def H_VFD(state):
    """Ĥ = I_12 + P_72.  tr(Ĥ) = 13."""
    return add_op(identity_12(), K_class_projector(state, 72))


def C_VFD(state):
    """Ĉ = I_12 - P_0.  tr(Ĉ) = 11."""
    return sub_op(identity_12(), K_class_projector(state, 0))


def trace_ratio(op, baseline=12):
    """Return Fraction tr(op) / baseline."""
    return Fraction(trace(op), baseline)
