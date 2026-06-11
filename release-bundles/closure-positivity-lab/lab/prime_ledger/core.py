"""Shared instruments for the prime ledger: sieve, singular series, HL integral."""
import os

import numpy as np

# Hardy-Littlewood twin-prime constant C2 = prod_{p>2} (1 - 1/(p-1)^2)
C2 = 0.66016181584686957392781211001455577843

DEFAULT_X = int(os.environ.get("PRIME_LEDGER_X", 50_000_000))


def sieve(x=DEFAULT_X):
    """Boolean array s with s[n] = n is prime, n < x."""
    s = np.ones(x, dtype=bool)
    s[:2] = False
    for i in range(2, int(x ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return s


def primes_from(s):
    return np.nonzero(s)[0]


def odd_prime_factors(h):
    """Distinct odd prime factors of h by trial division."""
    out, d = [], 3
    h = h // (h & -h)  # strip powers of 2
    while d * d <= h:
        if h % d == 0:
            out.append(d)
            while h % d == 0:
                h //= d
        d += 2
    if h > 1:
        out.append(h)
    return out


def gap_local_ratio(h):
    """Singular-series ratio S(h)/S(2) = prod over odd p | h of (p-1)/(p-2).

    This is the all-finite-places product: each odd prime p dividing h doubles
    nothing and forbids nothing extra, contributing (p-1)/(p-2) relative to the
    twin pattern. h must be even (odd gaps have at most one pair: (2, 2+h)).
    """
    assert h % 2 == 0
    r = 1.0
    for p in odd_prime_factors(h):
        r *= (p - 1) / (p - 2)
    return r


def hl_pair_integral(x, n=4_000_001):
    """integral_2^x dt / log(t)^2 (the HL density integral, trapezoidal)."""
    t = np.linspace(2.0, float(x), n)
    return float(np.trapz(1.0 / np.log(t) ** 2, t))


def count_pairs(s, h):
    """Number of n < len(s)-h with n and n+h both prime."""
    return int(np.count_nonzero(s[:-h] & s[h:]))


def row_result(row_id, phenomenon, classical_source, wall, computed, gate, verdict,
               falsifier):
    return {
        "row": row_id,
        "phenomenon": phenomenon,
        "layer1_classical_source": classical_source,
        "layer2_wall": wall,
        "computed": computed,
        "gate": gate,
        "verdict": verdict,
        "falsifier": falsifier,
    }
