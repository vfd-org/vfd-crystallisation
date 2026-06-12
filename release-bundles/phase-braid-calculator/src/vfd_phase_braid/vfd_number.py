"""VFDNumber: an integer lifted into its phase-braid coordinates.

The principle of the engine: ordinary numbers are bookkeeping labels; a
VFDNumber carries the same value plus the structural coordinates the rest of
the calculator reasons over.  Nothing here changes arithmetic — `value` is
always the plain integer — it only annotates it.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable

from . import phase_maps as pm


def closure_class(value: int, factors: Dict[int, int], prime: bool) -> str:
    """Classify the structural / closure role of an integer.

    The taxonomy is read off the factor signature:
      * the unit 1 is the root of the Collatz 4-2-1 basin;
      * primes are irreducible generators;
      * pure powers of 2 are compression nodes (all v_2);
      * pure powers of 3 are triadic expansion nodes (all v_3);
      * numbers supported on {2,3} alone are braid-balanced;
      * other composites are split by parity into compression- vs
        expansion-dominant.
    """
    if value <= 0:
        return "degenerate"
    if value == 1:
        return "closure unit"
    if prime:
        return "prime generator"
    primes = set(factors)
    if primes == {2}:
        return "pure compression node"
    if primes == {3}:
        return "triadic expansion node"
    if primes <= {2, 3}:
        return "braid-balanced node"
    if 2 in primes:
        return "compression-dominant composite"
    return "expansion-dominant composite"


@dataclass
class VFDNumber:
    """An integer lifted to its phase-braid state."""

    value: int
    parity: int
    triad_phase: int
    residues: Dict[int, int]
    factors: Dict[int, int]
    is_prime: bool
    v2: int
    v3: int
    phi_log_phase: float
    braid_label: str
    closure_class: str

    @classmethod
    def lift(cls, value: int, moduli: Iterable[int] = pm.DEFAULT_MODULI) -> "VFDNumber":
        """Lift a plain integer into a VFDNumber."""
        value = int(value)
        prime = pm.is_prime(value) if value >= 2 else False
        factors = pm.factorize(value) if value >= 1 else {}
        return cls(
            value=value,
            parity=pm.parity(value),
            triad_phase=pm.triad_phase(value),
            residues=pm.residues(value, moduli),
            factors=factors,
            is_prime=prime,
            v2=pm.p_adic_valuation(value, 2) if value != 0 else -1,
            v3=pm.p_adic_valuation(value, 3) if value != 0 else -1,
            phi_log_phase=pm.phi_log_phase(value),
            braid_label=pm.braid_label(value),
            closure_class=closure_class(value, factors, prime),
        )

    def factor_string(self) -> str:
        """Human-readable factorisation, e.g. '3^3' or '2 x 7'."""
        if self.value < 1:
            return "n/a"
        if not self.factors:
            return "1"
        parts = []
        for p in sorted(self.factors):
            e = self.factors[p]
            parts.append(f"{p}^{e}" if e > 1 else f"{p}")
        return " x ".join(parts)

    def describe(self) -> str:
        """Multi-line inspection report for the CLI `inspect` command."""
        parity = "even" if self.parity == 0 else "odd"
        kind = "prime" if self.is_prime else ("unit" if self.value == 1 else "composite")
        res = ", ".join(f"{k}:{v}" for k, v in self.residues.items())
        lines = [
            f"value:        {self.value}",
            f"parity:       {parity}",
            f"triad phase:  {self.triad_phase} mod 3   (braid leg {self.braid_label})",
            f"residues:     {res}",
            f"factorisation:{self.factor_string()}",
            f"prime/comp:   {kind}",
            f"v2 (2-adic):  {self.v2}",
            f"v3 (3-adic):  {self.v3}",
            f"phi-log phase:{self.phi_log_phase:.6f}",
            f"closure role: {self.closure_class}",
        ]
        return "\n".join(lines)
