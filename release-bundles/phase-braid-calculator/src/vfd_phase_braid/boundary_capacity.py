"""Boundary / capacity model.

A single scalar Q decides which side of the closure boundary a process sits on:

    Q = compression - expansion.

Q > 0  -> closure-dominant   (process contracts toward its basin)
Q = 0  -> boundary-balanced  (critical line)
Q < 0  -> expansion-dominant (leakage / escape signature)

For Collatz the natural weighting is logarithmic: compression = (#halvings) *
log 2, expansion = (#tripling steps) * log 3, which is exactly the capacity sum
from `collatz_closure`.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from . import collatz_closure as cc


@dataclass
class CapacityVerdict:
    compression: float
    expansion: float
    Q: float
    classification: str


def classify(compression: float, expansion: float, tol: float = 1e-9) -> CapacityVerdict:
    """Classify a process by its compression-minus-expansion capacity."""
    Q = compression - expansion
    if Q > tol:
        cls = "closure-dominant"
    elif Q < -tol:
        cls = "expansion/leakage-dominant"
    else:
        cls = "critical/boundary-balanced"
    return CapacityVerdict(compression=compression, expansion=expansion, Q=Q, classification=cls)


def collatz_capacity(n: int, max_steps: int = 100_000) -> CapacityVerdict:
    """Capacity of the Collatz run from n, in logarithmic (nat) units."""
    analysis = cc.analyze(n, max_steps)
    total_a = sum(a for _, a, _ in analysis.odd_steps)
    k = len(analysis.odd_steps)
    compression = total_a * cc.LOG2
    expansion = k * cc.LOG3
    return classify(compression, expansion)
