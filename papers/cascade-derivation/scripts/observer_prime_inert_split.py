#!/usr/bin/env python3
"""Inert/split prime classification over Z[phi] — first empirical test
of P5 (geometric closure-locus) in the observer-as-prime programme.

Conjecture P5 (refined): sigma-fixed primes in the icosian ring I =
Z[phi] + Z[phi]*i + Z[phi]*j + Z[phi]*k correspond to rational primes
that are inert in Z[phi]. The sigma-action is the golden Galois twist
sqrt(5) -> -sqrt(5); its fixed sub-lattice inside I is the rational
icosian sub-lattice Z^4 (no phi-components).

By classical algebraic number theory, a rational prime p factors in
Z[phi] as:
  - ramified (p = 5): single prime above, norm 5
  - inert (p == 2 or 3 mod 5, i.e. (5/p) = -1): stays prime, norm p^2
  - split (p == 1 or 4 mod 5, i.e. (5/p) = +1): = pi * sigma(pi)

Inert primes are sigma-fixed as PRIMES of Z[phi]. Split primes come in
sigma-pairs {pi, sigma(pi)}. Ramified prime p = 5 is its own sigma-image
up to unit.

This script counts primes in each class up to N and compares to the
Chebotarev density 1/2 prediction.

No deep cascade content in this script alone. Its purpose is to
(a) establish the baseline count any cascade-native zeta must reproduce,
and (b) give the sigma-orbit structure that downstream empirical tests
of P3/P4 will use.

Run:
    python3 papers/cascade-derivation/scripts/observer_prime_inert_split.py
"""
from __future__ import annotations

import math
from collections import Counter


def sieve(n: int) -> list[int]:
    """Primes up to n (Eratosthenes)."""
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(math.isqrt(n)) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [i for i, x in enumerate(s) if x]


def legendre_5(p: int) -> int:
    """Legendre symbol (5/p) for odd prime p != 5.

    By quadratic reciprocity and the fact 5 == 1 mod 4:
    (5/p) = (p/5) = +1 iff p == 1 or 4 mod 5, else -1.
    """
    r = p % 5
    if r in (1, 4):
        return +1
    return -1


def classify(p: int) -> str:
    """Inert / split / ramified classification in Z[phi]."""
    if p == 5:
        return "ramified"
    if p == 2:
        # 2 mod 5 = 2, (5/2) = -1 by the formula, so inert.
        return "inert"
    if legendre_5(p) == +1:
        return "split"
    return "inert"


def main(N: int = 10_000) -> None:
    primes = sieve(N)
    cat = Counter(classify(p) for p in primes)

    total = len(primes)
    print(f"Classification of rational primes up to N = {N}")
    print(f"  total primes pi({N}) = {total}")
    print()
    for key in ("ramified", "inert", "split"):
        n = cat[key]
        frac = n / total if total else 0.0
        print(f"  {key:10s}: {n:5d}    fraction {frac:.4f}")
    print()
    print("Chebotarev density prediction: inert ~ 1/2, split ~ 1/2.")
    print("Observed inert/split ratio     :",
          f"{cat['inert'] / max(1, cat['split']):.4f}")
    print()

    # sigma-orbit structure:
    # ramified: self-sigma-conjugate (size-1 orbit, p = 5)
    # inert:    self-sigma-conjugate as ideal (size-1 orbit in Spec Z[phi])
    # split:    non-self-conjugate (size-2 orbit {pi, sigma(pi)} in Spec)
    sigma_fixed_count = cat["ramified"] + cat["inert"]
    sigma_orbit_2_count = 2 * cat["split"]  # ideal count, not rational prime count
    print("sigma-orbit structure on Spec(Z[phi]) prime-ideals above rationals <= N:")
    print(f"  orbit-size 1 (sigma-fixed) : {sigma_fixed_count}")
    print(f"  orbit-size 2 (split pair)  : {sigma_orbit_2_count}")
    print(f"  total prime ideals         : {sigma_fixed_count + sigma_orbit_2_count}")
    print()

    # Distribution on mod-5 classes:
    mod5 = Counter(p % 5 for p in primes if p != 5)
    print("Distribution on p mod 5 (excluding p=5):")
    for r in (1, 2, 3, 4):
        print(f"  p == {r} mod 5: {mod5[r]:5d}   fraction {mod5[r] / (total - 1):.4f}")
    print()
    print("(Dirichlet: asymptotic density 1/4 in each residue class.)")


if __name__ == "__main__":
    import sys
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000
    main(N)
