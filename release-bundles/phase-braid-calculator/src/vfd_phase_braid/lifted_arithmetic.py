"""Lifted arithmetic: ordinary operations that also report the phase-braid
state transition.

The standard result is *always* the plain arithmetic answer — the lift never
alters correctness.  Alongside it we report the triad/braid transition and a
closure residual that checks the phase homomorphism:

    triad_phase(a + b) == (triad_phase(a) + triad_phase(b)) mod 3
    triad_phase(a * b) == (triad_phase(a) * triad_phase(b)) mod 3

A residual of 0 confirms the operation respects the triad grading; a non-zero
residual would flag a broken lift.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import List, Optional, Union

from .vfd_number import VFDNumber

Number = Union[int, Fraction]


@dataclass
class VFDOperationResult:
    operation: str
    inputs: List[VFDNumber]
    ordinary_result: Number
    lifted_result: Optional[VFDNumber]
    phase_transition: str
    compression_delta: Optional[int]
    closure_residual: Optional[int]
    notes: List[str] = field(default_factory=list)

    def describe(self) -> str:
        lines = [f"{self.operation}", ""]
        for vn in self.inputs:
            lines.append(f"{vn.value}:")
            lines.append(f"    triad phase: {vn.triad_phase}  (leg {vn.braid_label})")
            lines.append(f"    parity:      {'even' if vn.parity == 0 else 'odd'}")
            lines.append(f"    v2:          {vn.v2}")
            lines.append("")
        lines.append(f"= {self.ordinary_result}")
        lines.append("")
        if self.lifted_result is not None:
            r = self.lifted_result
            lines.append(f"{r.value}:")
            lines.append(f"    triad phase: {r.triad_phase}  (leg {r.braid_label})")
            lines.append(f"    parity:      {'even' if r.parity == 0 else 'odd'}")
            lines.append(f"    factors:     {r.factor_string()}")
            lines.append("")
        lines.append(f"phase transition: {self.phase_transition}")
        if self.compression_delta is not None:
            lines.append(f"compression delta (v2): {self.compression_delta:+d}")
        if self.closure_residual is not None:
            verdict = "preserves" if self.closure_residual == 0 else "DISRUPTS"
            lines.append(f"triad homomorphism: {verdict} (residual {self.closure_residual})")
        for note in self.notes:
            lines.append(f"note: {note}")
        return "\n".join(lines)


def lift(n: int) -> VFDNumber:
    return VFDNumber.lift(n)


def _binary(op_symbol: str, a: int, b: int, result: Number,
            expected_triad: Optional[int]) -> VFDOperationResult:
    va, vb = VFDNumber.lift(a), VFDNumber.lift(b)
    lifted = None
    compression_delta = None
    closure_residual = None
    notes: List[str] = []

    if isinstance(result, int) or (isinstance(result, Fraction) and result.denominator == 1):
        rv = int(result)
        if rv >= 1:
            lifted = VFDNumber.lift(rv)
            compression_delta = lifted.v2 - (va.v2 + vb.v2)
            if expected_triad is not None:
                closure_residual = (lifted.triad_phase - expected_triad) % 3
            if lifted.triad_phase == 0:
                notes.append("result lands on triad boundary phase 0")
            if lifted.is_prime:
                notes.append("result is a prime generator")
        else:
            notes.append("result <= 0; lift not defined (sign/zero outside braid)")
    else:
        notes.append("non-integer result; remains a rational bookkeeping label")

    left = va.braid_label
    right = vb.braid_label
    out = lifted.braid_label if lifted is not None else "?"
    phase_transition = f"{left} {op_symbol} {right} -> {out}"

    return VFDOperationResult(
        operation=f"{a} {op_symbol} {b}",
        inputs=[va, vb],
        ordinary_result=result,
        lifted_result=lifted,
        phase_transition=phase_transition,
        compression_delta=compression_delta,
        closure_residual=closure_residual,
        notes=notes,
    )


def add(a: int, b: int) -> VFDOperationResult:
    return _binary("+", a, b, a + b, (a + b) % 3)


def subtract(a: int, b: int) -> VFDOperationResult:
    return _binary("-", a, b, a - b, (a - b) % 3)


def multiply(a: int, b: int) -> VFDOperationResult:
    return _binary("*", a, b, a * b, (a * b) % 3)


def divide(a: int, b: int) -> VFDOperationResult:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    result: Number = Fraction(a, b)
    expected = (a * pow(b, -1, 3)) % 3 if (b % 3 != 0 and result.denominator == 1) else None
    return _binary("/", a, b, result, expected)


def power(a: int, b: int) -> VFDOperationResult:
    if b < 0:
        result: Number = Fraction(1, a ** (-b))
        expected = None
    else:
        result = a ** b
        expected = pow(a % 3, b, 3)
    return _binary("^", a, b, result, expected)
