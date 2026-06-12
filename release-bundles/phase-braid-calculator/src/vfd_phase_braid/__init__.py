"""VFD Phase-Braid Calculator — phase-braid arithmetic and boundary-closure engine.

Ordinary numbers are bookkeeping labels; this engine lifts each integer into a
structured phase-braid object and studies whether arithmetic, Collatz dynamics,
prime structure, and finite-window self-adjointness share one computational
grammar.

Phase 1: Python CLI (`vfdcalc`).
"""

from __future__ import annotations

__version__ = "0.1.0"

from . import (  # noqa: F401
    boundary_capacity,
    collatz_closure,
    lifted_arithmetic,
    phase_maps,
    prime_trace,
    report_generator,
    self_adjoint,
)
from .vfd_number import VFDNumber  # noqa: F401

__all__ = [
    "VFDNumber",
    "phase_maps",
    "lifted_arithmetic",
    "collatz_closure",
    "prime_trace",
    "self_adjoint",
    "boundary_capacity",
    "report_generator",
    "__version__",
]
