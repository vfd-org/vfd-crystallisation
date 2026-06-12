"""Prime-trace analysis over a range 1..N.

Sieves primes, computes gaps, and reports the triad-phase / residue
distribution of both the primes and the gaps.  This is the export hook for
downstream RH / zeta experiments — the data structures are deliberately flat
and serialisable.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from typing import Dict, List


def sieve(limit: int) -> List[int]:
    """Return all primes <= limit via the sieve of Eratosthenes."""
    if limit < 2:
        return []
    flags = bytearray([1]) * (limit + 1)
    flags[0] = flags[1] = 0
    i = 2
    while i * i <= limit:
        if flags[i]:
            flags[i * i :: i] = bytearray(len(flags[i * i :: i]))
        i += 1
    return [i for i in range(2, limit + 1) if flags[i]]


@dataclass
class PrimeTrace:
    limit: int
    primes: List[int]
    count: int
    gaps: List[int]
    triad_distribution: Dict[int, int]      # phase -> #primes
    residue_distribution: Dict[int, int]     # residue mod `modulus` -> #primes
    modulus: int
    gap_phase_distribution: Dict[int, int]   # gap mod 3 -> count
    max_gap: int
    imbalance: Dict[int, float]              # phase -> deviation from uniform


def analyze(limit: int, modulus: int = 6) -> PrimeTrace:
    """Compute the prime trace up to `limit`, bucketing residues mod `modulus`."""
    primes = sieve(limit)
    count = len(primes)
    gaps = [primes[i + 1] - primes[i] for i in range(count - 1)]

    triad = Counter(p % 3 for p in primes)
    residue = Counter(p % modulus for p in primes)
    gap_phase = Counter(g % 3 for g in gaps)

    # Imbalance: fraction in each triad phase minus the 1/2 expected for the
    # two coprime classes (phase 0 only ever holds the prime 3).
    imbalance: Dict[int, float] = {}
    coprime_total = sum(v for k, v in triad.items() if k != 0)
    for phase in (1, 2):
        share = triad.get(phase, 0) / coprime_total if coprime_total else 0.0
        imbalance[phase] = share - 0.5

    return PrimeTrace(
        limit=limit,
        primes=primes,
        count=count,
        gaps=gaps,
        triad_distribution=dict(sorted(triad.items())),
        residue_distribution=dict(sorted(residue.items())),
        modulus=modulus,
        gap_phase_distribution=dict(sorted(gap_phase.items())),
        max_gap=max(gaps) if gaps else 0,
        imbalance=imbalance,
    )


def describe(t: PrimeTrace, preview: int = 20) -> str:
    head = ", ".join(str(p) for p in t.primes[:preview])
    if t.count > preview:
        head += ", ..."
    lines = [
        f"range:        1..{t.limit}",
        f"primes:       {t.count}",
        f"first primes: {head}",
        f"triad phases (p mod 3):   {t.triad_distribution}",
        f"residues (p mod {t.modulus}):       {t.residue_distribution}",
        f"gap phases (gap mod 3):   {t.gap_phase_distribution}",
        f"max gap:      {t.max_gap}",
        "Chebyshev-bias imbalance (share - 0.5):",
        f"    phase 1: {t.imbalance.get(1, 0.0):+.5f}",
        f"    phase 2: {t.imbalance.get(2, 0.0):+.5f}",
    ]
    return "\n".join(lines)
