"""Phase maps: the number-theoretic primitives that lift an integer into its
phase-braid coordinates.

Everything here is ordinary, verifiable arithmetic — parity, modular residues,
p-adic valuations, factorisation, primality, and the golden-ratio log phase.
No VFD interpretation lives in this module; it is pure bookkeeping that the
higher layers read from.
"""

from __future__ import annotations

import math
from typing import Dict, Iterable, Tuple

# Golden ratio — the natural base for the cascade's logarithmic phase.
PHI = (1.0 + math.sqrt(5.0)) / 2.0

# Default moduli reported in the residue vector.  12 is included because the
# VFD programme treats lambda = 12 as the canonical lift modulus.
DEFAULT_MODULI: Tuple[int, ...] = (2, 3, 5, 7, 12)

# Braid legs are read straight off the triad phase n mod 3.
_BRAID_LEGS = {0: "A", 1: "B", 2: "C"}


def parity(n: int) -> int:
    """Return n mod 2 (0 = even, 1 = odd)."""
    return n % 2


def triad_phase(n: int) -> int:
    """Return the triad phase n mod 3."""
    return n % 3


def braid_label(n: int) -> str:
    """Map the triad phase to a braid leg: 0->A, 1->B, 2->C."""
    return _BRAID_LEGS[n % 3]


def residues(n: int, moduli: Iterable[int] = DEFAULT_MODULI) -> Dict[int, int]:
    """Return {k: n mod k} for each requested modulus k >= 1."""
    return {k: n % k for k in moduli if k >= 1}


def p_adic_valuation(n: int, p: int) -> int:
    """Return v_p(n): the exponent of the largest power of p dividing n.

    v_p(0) is conventionally infinite; we return -1 as a sentinel so callers
    can detect it without raising.
    """
    if p < 2:
        raise ValueError("p-adic valuation requires a prime base p >= 2")
    if n == 0:
        return -1
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def _is_probable_prime(n: int) -> bool:
    """Deterministic Miller-Rabin for n < 3.3e24 using the first 12 primes."""
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in small:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def is_prime(n: int) -> bool:
    """Return True iff n is a prime integer."""
    return _is_probable_prime(n)


def _pollard_rho(n: int) -> int:
    """Return a non-trivial factor of composite n (no randomness — fixed seeds
    so the engine stays fully reproducible)."""
    if n % 2 == 0:
        return 2
    for c in range(1, 64):
        x = y = 2
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d
    return n  # give up; caller treats n as an irreducible block


def factorize(n: int) -> Dict[int, int]:
    """Return the prime factorisation of n >= 1 as {prime: exponent}.

    factorize(1) == {}.  Trial division handles everything up to ~1e12 quickly;
    Pollard rho backs it up for larger composites.
    """
    if n < 1:
        raise ValueError("factorize requires n >= 1")
    factors: Dict[int, int] = {}
    # Strip small primes by trial division.
    for p in (2, 3, 5, 7, 11, 13):
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
    if n == 1:
        return factors

    stack = [n]
    while stack:
        m = stack.pop()
        if m == 1:
            continue
        if is_prime(m):
            factors[m] = factors.get(m, 0) + 1
            continue
        # Trial division up to a bound before falling back to rho.
        f = 0
        bound = min(int(math.isqrt(m)) + 1, 1_000_000)
        d = 17
        while d <= bound:
            if m % d == 0:
                f = d
                break
            d += 2
        if f == 0:
            f = _pollard_rho(m)
        if f == m:  # irreducible block we could not split
            factors[m] = factors.get(m, 0) + 1
            continue
        stack.append(f)
        stack.append(m // f)
    return factors


def phi_log_phase(n: int) -> float:
    """Return the fractional part of log_phi(|n|), the golden-ratio log phase.

    Returns 0.0 for n in {0} since log is undefined there.
    """
    if n == 0:
        return 0.0
    val = math.log(abs(n)) / math.log(PHI)
    return val - math.floor(val)
