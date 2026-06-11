#!/usr/bin/env python3
"""Experiment (C): classical Dedekind zeta_K for K = Q(phi), verifying
the factorisation zeta_K(s) = zeta(s) * L(s, chi_5) at the Dirichlet-
coefficient level.

This experiment is CLASSICAL — it does not construct a cascade-native
zeta. It establishes that Dedekind zeta_K is the leading external
comparison target for any intrinsic zeta_F that a future derivation
might define from F-iteration on the capstone category C. Whether any
such intrinsic zeta_F exists (open item O2) and whether it coincides
with Dedekind zeta_K (part of open item O7) is NOT settled here.

  (A) bare-rung F     — finite Dirichlet support, NOT a zeta.
  (B) F1 scalar shadow — Fibonacci-supported series, NOT Riemann zeta.
  (C) Dedekind zeta_K — classical factorisation zeta_K = zeta * L(chi_5)
                        verified at n <= 100 (this script).

RH for zeta and GRH for L(s, chi_5) are both open conjectures; neither
is settled by this experiment.

Run:
    python3 papers/cascade-derivation/scripts/observer_zeta_dedekind.py
"""
from __future__ import annotations

import math
from collections import Counter


# ---------------------------------------------------------------------
# Number-theoretic primitives
# ---------------------------------------------------------------------

def sieve(n: int) -> list[int]:
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(math.isqrt(n)) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [i for i, x in enumerate(s) if x]


def chi_5(n: int) -> int:
    """Kronecker character chi_5 = (n/5). 0 if 5|n, +1 if QR mod 5, -1 otherwise."""
    r = n % 5
    if r == 0:
        return 0
    if r in (1, 4):
        return +1
    return -1


def splitting(p: int) -> str:
    """Classify rational prime p in Z[phi]. Returns 'ramified' / 'split' / 'inert'."""
    if p == 5:
        return "ramified"
    return "split" if chi_5(p) == +1 else "inert"


# ---------------------------------------------------------------------
# Dedekind a_n via direct ideal-counting
# ---------------------------------------------------------------------

def ideal_count_at_prime_power(p: int, k: int) -> int:
    """Number of ideals of O_K of norm p^k, for rational prime p."""
    s = splitting(p)
    if s == "ramified":
        # (5) = P^2 with N(P) = 5. Unique ideal of norm 5^k: P^k.
        return 1
    if s == "split":
        # (p) = P1 * P2, N(Pi) = p. Ideals of norm p^k: P1^i P2^(k-i), i=0..k.
        return k + 1
    # inert: (p) = P with N(P) = p^2. Ideals of norm p^k: P^(k/2) if k even, else none.
    return 1 if k % 2 == 0 else 0


def factorise(n: int, primes: list[int]) -> dict[int, int]:
    """Rational prime factorisation of n."""
    f = {}
    for p in primes:
        if p * p > n:
            break
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def a_dedekind(n: int, primes: list[int]) -> int:
    """Dedekind a_n: number of ideals of O_K of norm n (multiplicative from
    prime-power case)."""
    if n == 1:
        return 1
    f = factorise(n, primes)
    prod = 1
    for p, k in f.items():
        prod *= ideal_count_at_prime_power(p, k)
    return prod


# ---------------------------------------------------------------------
# Convolution a_n = (1 * chi_5)(n)
# ---------------------------------------------------------------------

def a_convolution(n: int) -> int:
    """(1 * chi_5)(n) = sum_{d | n} chi_5(d). Should equal a_dedekind(n)."""
    total = 0
    for d in range(1, n + 1):
        if n % d == 0:
            total += chi_5(d)
    return total


# ---------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------

def main(N: int = 100, primes_upper: int = 2000):
    primes = sieve(primes_upper)

    print("=" * 72)
    print(f"EXPERIMENT (C) — Dedekind zeta_K for K = Q(phi), O_K = Z[phi]")
    print("=" * 72)
    print(f"Testing the factorisation zeta_K(s) = zeta(s) * L(s, chi_5)")
    print(f"at the Dirichlet-coefficient level for n <= {N}.")
    print()

    # Per-n table
    print(f"{'n':>4} {'a_n (dedekind)':>16} {'(1*chi_5)(n)':>14} {'match':>6}  "
          f"{'zeta coef':>10} {'L(chi_5) coef':>14}")
    print("-" * 72)
    matches = 0
    mismatches = []
    for n in range(1, N + 1):
        a_d = a_dedekind(n, primes)
        a_c = a_convolution(n)
        ok = a_d == a_c
        if ok:
            matches += 1
        else:
            mismatches.append((n, a_d, a_c))
        if n <= 30:
            zeta_coef = 1  # Riemann zeta a_n = 1 for all n
            L_coef = chi_5(n)  # L(s, chi_5) a_n = chi_5(n)
            marker = "YES" if ok else "*** NO ***"
            print(f"{n:>4} {a_d:>16} {a_c:>14} {marker:>6}  "
                  f"{zeta_coef:>10} {L_coef:>14}")

    print("-" * 72)
    print(f"Matches for n=1..{N}: {matches} / {N}")
    if mismatches:
        print(f"Mismatches: {mismatches[:5]}{' ...' if len(mismatches) > 5 else ''}")
    else:
        print("No mismatches. zeta_K = zeta * L(chi_5) VERIFIED at Dirichlet-")
        print("coefficient level.")
    print()

    # Distribution of a_n: how often is a_n = k for small k
    counts = Counter(a_dedekind(n, primes) for n in range(1, N + 1))
    print(f"Distribution of a_n for n=1..{N}:")
    for k in sorted(counts.keys()):
        print(f"  a_n = {k}: {counts[k]} values")
    print()

    # Numerical check at s = 2: zeta_K(2) = zeta(2) * L(2, chi_5)
    # zeta_K(2) = sum a_n / n^2
    # Known: zeta(2) = pi^2 / 6. L(2, chi_5) is a specific constant.
    s = 2.0
    zeta_K_partial = sum(a_dedekind(n, primes) / n**s for n in range(1, N + 1))
    zeta_partial   = sum(1.0 / n**s for n in range(1, N + 1))
    L_chi5_partial = sum(chi_5(n) / n**s for n in range(1, N + 1))
    product = zeta_partial * L_chi5_partial
    print(f"Numerical check at s = {s}:")
    print(f"  zeta_K(2) approx (truncated N={N})  = {zeta_K_partial:.10f}")
    print(f"  zeta(2) * L(2, chi_5) approx        = {product:.10f}")
    print(f"  zeta(2) exact (pi^2 / 6)            = {math.pi**2 / 6:.10f}")
    print(f"  ratio zeta_K(2) / product            = "
          f"{zeta_K_partial / product:.10f}  (should -> 1)")
    print()

    # Sigma-orbit decomposition of prime ideals
    print("sigma-orbit decomposition of prime ideals of Z[phi] (up to norm N):")
    sigma_fixed = 0    # ramified + inert (as ideals)
    sigma_orbit2 = 0   # split ideals come in sigma-orbit pairs
    for p in primes:
        if p > N:
            break
        s = splitting(p)
        if s == "ramified":
            sigma_fixed += 1  # (5) ramified, P with N(P) = 5
        elif s == "inert" and p * p <= N:
            sigma_fixed += 1  # (p) stays prime, N(P) = p^2
        elif s == "split":
            # two primes of norm p, sigma swaps them
            sigma_orbit2 += 2
    print(f"  sigma-fixed prime ideals (ramified + inert, norm <= {N}): {sigma_fixed}")
    print(f"  sigma-orbit-2 prime ideals (split pairs, norm <= {N}):    {sigma_orbit2}")
    print()
    print("Correct Euler-factor reading (NOT what an earlier draft of this")
    print("script claimed):")
    print("  ramified p=5:")
    print("    zeta_K local = (1 - 5^-s)^-1")
    print("    zeta  local = (1 - 5^-s)^-1,   L(chi_5) local = 1")
    print("  split p (chi_5(p) = +1, e.g. p = 11, 19, 29, 31):")
    print("    zeta_K local = (1 - p^-s)^-2  (two prime ideals above p)")
    print("    zeta  local = (1 - p^-s)^-1,   L(chi_5) local = (1 - p^-s)^-1")
    print("  inert p (chi_5(p) = -1, e.g. p = 2, 3, 7, 13):")
    print("    zeta_K local = (1 - p^-2s)^-1  (one prime ideal of norm p^2)")
    print("    zeta  local = (1 - p^-s)^-1,   L(chi_5) local = (1 + p^-s)^-1")
    print("    factorisation: (1 - p^-2s)^-1 = (1 - p^-s)^-1 (1 + p^-s)^-1")
    print()
    print("So EVERY rational prime contributes to BOTH zeta and L(chi_5).")
    print("The sigma-orbit class of the primes above p determines the SHAPE")
    print("of the zeta_K local factor, not which of zeta / L(chi_5) it lives in.")
    print()
    print("Riemann zeta counts the rational-prime contribution; L(chi_5) counts")
    print("the Galois-twist. Both factors together encode the same prime ideals")
    print("of Z[phi]. GRH (conjectural) would place all non-trivial zeros of")
    print("both on Re(s) = 1/2.")


if __name__ == "__main__":
    import sys
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    main(N)
