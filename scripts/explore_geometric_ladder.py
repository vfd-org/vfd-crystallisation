#!/usr/bin/env python3
"""
WO-SHELL-OFFSET-001 Phase C: the SIEVE hypothesis — intermediate geometry
and prime resonances as a generator of ALLOWED SHELL LEVELS.

The Phase A/B attack (explore_shell_rule.py) proved that no rule of the
form "shell = function of static quantum numbers + universal generation
dependence" can exist (curvature obstruction). This phase tests a
genuinely different class, proposed from the 5 x 24 Schlafli structure:
the geometry generates a SET of allowed levels (a sieve), and particles
occupy allowed levels. A sieve is not a function of quantum numbers, so
the curvature obstruction does not apply to it.

METHOD (fixed before judging). The observed distinct charged-fermion +
boson shells are S = {81, 82, 88, 90, 91, 96, 102, 104, 107} (9 values
in the span [81, 107], i.e. 9 of 27 integers). For each GEOMETRY-DERIVED
candidate level set L (each with its provenance stated), we score
hits = |S ∩ L| and compare against the exact null: the hypergeometric
probability that a random level set of the same density within the span
captures >= hits of the 9. Success bar (pre-registered): family-wise
p < 0.01 AFTER Bonferroni over the number of candidate sieves tested.
A sieve that is dense enough to hit everything trivially (density
> 2/3 in the span) is inadmissible (no compression).

Candidate sieves (all from structures the programme actually possesses):
  G1  multiples of 8 (rung-8 ladder: Observer rung)
  G2  multiples of 6 (D4 Coxeter number, 24-cell rung)
  G3  {24a + 5b : small a, b >= 0} restricted to the span (the user's
      5 x 24 intermediate-coset idea, coefficient-bounded)
  G4  Coxeter-degree ladder: numbers expressible as 30a + 20b + 12c + 2d
      with small coefficients (H4 degrees {2, 12, 20, 30})
  G5  E8-exponent shifts of 96: {96 +- e : e in E8 exponents
      {1,7,11,13,17,19,23,29}} union {96}
  G6  primes and prime powers in the span (the bare prime-resonance
      reading)
  G7  split-class resonances: integers n in the span with n or n/2 a
      prime ≡ ±1 (mod 5) (the icosian split primes of the
      prime-phenomena instrument)
  G8  pentagonal classes: n ≡ {0, ±1} (mod 5) (clock periodicity)

Every result, hit or null, is recorded; a PASS reproduces the recorded
conclusion.

Usage:
    python scripts/explore_geometric_ladder.py
"""
from __future__ import annotations

import numpy as np
from math import comb
from sympy import isprime

PASS = []
FAIL = []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


S = {81, 82, 88, 90, 91, 96, 102, 104, 107}
LO, HI = 81, 107
SPAN = set(range(LO, HI + 1))          # 27 integers
NS = len(S)


def hyper_p(level_set):
    """Exact null: P(random subset of the span with |L| elements captures
    >= |S ∩ L| of the 9 observed shells)."""
    L = level_set & SPAN
    k = len(S & L)
    m = len(L)
    Nn = len(SPAN)
    # hypergeometric upper tail: choose which span-integers are 'allowed'
    p = sum(comb(NS, j) * comb(Nn - NS, m - j) for j in range(k, min(NS, m) + 1)
            if m - j <= Nn - NS) / comb(Nn, m)
    return k, m, p


def density_ok(m):
    return m <= 18  # 2/3 of the span: denser sieves are inadmissible


SIEVES = {}

SIEVES["G1 multiples of 8"] = {n for n in SPAN if n % 8 == 0}
SIEVES["G2 multiples of 6"] = {n for n in SPAN if n % 6 == 0}
SIEVES["G3 24a+5b (a<=4, b<=5)"] = {24 * a + 5 * b for a in range(5)
                                    for b in range(6)} & SPAN
SIEVES["G4 H4 degrees 30a+20b+12c+2d (coeffs<=3,3,3,3)"] = {
    30 * a + 20 * b + 12 * c + 2 * d
    for a in range(4) for b in range(4) for c in range(4) for d in range(4)
} & SPAN
E8_EXP = {1, 7, 11, 13, 17, 19, 23, 29}
SIEVES["G5 96 +- E8 exponents"] = ({96} | {96 + e for e in E8_EXP}
                                   | {96 - e for e in E8_EXP}) & SPAN
SIEVES["G6 primes + prime powers"] = {
    n for n in SPAN if isprime(n)
    or any(round(n ** (1 / k)) ** k == n and isprime(round(n ** (1 / k)))
           for k in (2, 3, 4))}
SIEVES["G7 split-prime resonances (p or 2p, p=+-1 mod 5)"] = {
    n for n in SPAN
    if (isprime(n) and n % 5 in (1, 4))
    or (n % 2 == 0 and isprime(n // 2) and (n // 2) % 5 in (1, 4))}
SIEVES["G8 n = 0,+-1 mod 5"] = {n for n in SPAN if n % 5 in (0, 1, 4)}


def main():
    print("=" * 72)
    print("Phase C: the sieve hypothesis (intermediate geometry / prime")
    print("resonances as allowed-level generators) — null-model scored")
    print("=" * 72)
    print(f"observed distinct shells S = {sorted(S)}  (9 of 27 span integers)")
    print(f"success bar: Bonferroni-corrected p < 0.01 over "
          f"{len(SIEVES)} sieves; density <= 18/27")
    print("-" * 72)
    n_tests = len(SIEVES)
    results = {}
    for name, L in SIEVES.items():
        k, m, p = hyper_p(L)
        p_corr = min(1.0, p * n_tests)
        admissible = density_ok(m)
        results[name] = (k, m, p, p_corr, admissible)
        tag = "INADMISSIBLE (too dense)" if not admissible else (
            "SIGNIFICANT" if p_corr < 0.01 else "null")
        print(f"  {name:<46} hits {k}/9  density {m}/27  "
              f"p {p:.3f}  corrected {p_corr:.2f}  -> {tag}")
    print("-" * 72)

    any_sig = any(adm and pc < 0.01 for (_, _, _, pc, adm) in results.values())
    check("GL1 no admissible geometric/prime sieve clears the "
          "pre-registered bar (corrected p < 0.01): the sieve hypothesis, "
          "in the tested generator classes, is NULL", not any_sig)

    best = min(((pc, name) for name, (_, _, _, pc, adm) in results.items()
                if adm), default=(1.0, "none"))
    check("GL2 best admissible candidate recorded for the ledger",
          True, f"{best[1]} at corrected p = {best[0]:.2f}")

    # the quantitative target a future derived sieve must meet
    # (density d, all 9 hits): p = C(27-9, m-9)/C(27, m) * C(9,9)...
    for m in range(9, 19):
        p = comb(27 - 9, m - 9) / comb(27, m) * 1.0
        if p * n_tests < 0.01:
            check("GL3 target recorded: a DERIVED sieve capturing all 9 "
                  f"shells clears the bar iff its span-density <= {m}/27",
                  True, f"(at density {m}/27, corrected p = {p * n_tests:.4f})")
            break

    print("=" * 72)
    print(f"SUMMARY: {len(PASS)} PASS, {len(FAIL)} FAIL")
    for name in FAIL:
        print(f"  FAILED: {name}")
    print()
    print("Reading: the sieve CLASS survives the curvature obstruction and")
    print("remains the right shape for the 5x24/prime-resonance intuition,")
    print("but none of the eight geometry-derived generators tested here")
    print("beats chance after correction. The quantitative door (GL3) is")
    print("open: derive a level set from new intermediate geometry, hit all")
    print("nine shells at admissible density, and the hypothesis is alive.")
    return 0 if not FAIL else 1


if __name__ == "__main__":
    raise SystemExit(main())
