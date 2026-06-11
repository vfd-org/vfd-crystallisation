#!/usr/bin/env python3
"""Candidate cascade-zeta vs Riemann-zeta — first empirical pass.

Tests whether self-referential crystallisation (the F-functor of the
capstone, or its scalar shadow F1) admits a natural Dirichlet series
zeta_F(s) = sum_n a_n n^(-s) whose coefficients match Riemann's
zeta(s) = sum_n n^(-s) (where every a_n = 1).

Two experiments:
  (A) Bare rung-subset F: F(S) = up-closure(S union {O}) on subsets of
      Rungs = {U_0, E_8, H_4, D_4, O, F_16, L_40}. Enumerate F-fixed
      subsets, compute basin sizes, and form Dirichlet series under
      multiple norm choices.
  (B) F1 scalar shadow: x -> 1 + 1/x has fixed point phi = (1+sqrt 5)/2.
      Iterates from any rational converge through Fibonacci ratios
      F_{n+1}/F_n. Build zeta_F1(s) = sum_n F_n^(-s) and compare to
      Riemann zeta and to known reciprocal-Fibonacci constants.

Honest expected outcome: bare-rung F is too coarse (only 32 fixed
structures, finite Dirichlet support) to mimic an infinite zeta. F1
scalar shadow gives the Fibonacci-zeta, which is irrational but NOT
Riemann's zeta. Both results inform the next move.

Run:
    python3 papers/cascade-derivation/scripts/observer_zeta_candidate.py
"""
from __future__ import annotations

from collections import Counter, defaultdict
from itertools import chain, combinations


# ---------------------------------------------------------------------
# Experiment (A): bare rung-subset F
# ---------------------------------------------------------------------

# Rungs and their (Z-)dimensions per cascade-completeness-audit memory:
RUNG_DIM = {
    "U_0": 0,
    "E_8": 8,
    "H_4": 4,
    "D_4": 4,
    "O":   8,
    "F16": 16,
    "L40": 40,
}
RUNGS = frozenset(RUNG_DIM.keys())

# Partial order: E_8 is the top (everything <= E_8); the six leaves
# (H_4, D_4, O, F16, L40, U_0) are pairwise incomparable.
def is_below(r: str, rprime: str) -> bool:
    if r == rprime:
        return True
    if rprime == "E_8":
        return True
    return False


def up_closure(S: frozenset) -> frozenset:
    out = set(S)
    for r in S:
        for r2 in RUNGS:
            if is_below(r, r2):
                out.add(r2)
    return frozenset(out)


def F(S: frozenset) -> frozenset:
    """Self-inquiry: adjoin Observer rung and up-close."""
    return up_closure(S | {"O"})


def all_subsets(s: frozenset):
    return [
        frozenset(c)
        for r in range(len(s) + 1)
        for c in combinations(s, r)
    ]


def experiment_A():
    print("=" * 72)
    print("EXPERIMENT (A) — Bare rung-subset F")
    print("=" * 72)
    all_S = all_subsets(RUNGS)
    print(f"|2^Rungs| = {len(all_S)}")

    fixed = [S for S in all_S if F(S) == S]
    print(f"F-fixed rung-subsets: {len(fixed)}")
    print()

    # Group fixed structures by image and basin
    image_to_preimages = defaultdict(list)
    for S in all_S:
        image_to_preimages[F(S)].append(S)
    print("F-orbit structure (every initial S terminates in F(S) at depth 1):")
    print(f"  distinct images of F = {len(image_to_preimages)}")
    print(f"  all images are F-fixed = {all(F(im) == im for im in image_to_preimages)}")
    print()

    # Norm choices
    def norm_card(S):
        return len(S)

    def norm_dim(S):
        return sum(RUNG_DIM[r] for r in S)

    def norm_basin(S):
        return len(image_to_preimages[S])

    print("Norm-choice tabulation (counts of F-fixed structures by norm value):")
    for name, norm_fn in [("cardinality", norm_card),
                          ("Z-dimension", norm_dim),
                          ("basin size",  norm_basin)]:
        cnt = Counter(norm_fn(S) for S in fixed)
        print(f"  {name:14s}: {dict(sorted(cnt.items()))}")
    print()

    # Dirichlet coefficients a_n with norm = Z-dimension, for n = 1..80
    print("Dirichlet series zeta_F^A(s) under norm = Z-dimension")
    print("(coefficient a_n = #{F-fixed S : dim(S) = n})")
    a = Counter(norm_dim(S) for S in fixed)
    print(f"  support = {sorted(a.keys())}")
    print(f"  first 25 coefficients (n = 1..25): "
          f"{[a[n] for n in range(1, 26)]}")
    print(f"  Riemann zeta coefficients (n = 1..25): {[1] * 25}")
    print()
    print("  Verdict (A): bare-rung F has finite Dirichlet support starting "
          "at n=16. NOT Riemann zeta. Confirms bare-rung is too coarse.")
    print()


# ---------------------------------------------------------------------
# Experiment (B): F1 scalar shadow, Fibonacci convergents
# ---------------------------------------------------------------------

def experiment_B(N: int = 30):
    print("=" * 72)
    print("EXPERIMENT (B) — F1 scalar shadow, Fibonacci convergents")
    print("=" * 72)

    # Fibonacci sequence: F_1 = 1, F_2 = 1, F_3 = 2, ...
    fib = [0, 1]
    while len(fib) < N + 1:
        fib.append(fib[-1] + fib[-2])

    print(f"First {N} Fibonacci numbers F_1..F_{N}:")
    print("  ", fib[1:N + 1])
    print()

    # Convergents x_n = F_{n+1}/F_n -> phi
    print("F1 convergents x_n = F_{n+1}/F_n (approach phi = 1.6180...):")
    for n in range(1, min(11, N)):
        x = fib[n + 1] / fib[n]
        print(f"  x_{n:2d} = {fib[n+1]:>4d}/{fib[n]:<4d} = {x:.10f}")
    print()

    # Fibonacci-zeta: zeta_F1(s) = sum_{n>=1} F_n^(-s)
    # Coefficients in Dirichlet form: a_m = #{n : F_n = m}
    a = Counter(fib[1:N + 1])
    print(f"zeta_F1(s) = sum_n F_n^(-s) — Dirichlet coefficient a_m:")
    print(f"  support (first 25 m's): {sorted(a.keys())[:25]}")
    print(f"  a_1 = {a[1]} (since F_1 = F_2 = 1)")
    print(f"  a_m for m in F_n image, m <= 100: "
          f"{ {m: a[m] for m in sorted(a.keys()) if m <= 100} }")
    print()

    # First 25 Dirichlet coefficients
    coeffs = [a.get(n, 0) for n in range(1, 26)]
    print(f"  zeta_F1 first 25 coefficients (n = 1..25):")
    print(f"    {coeffs}")
    print(f"  Riemann zeta first 25 coefficients:")
    print(f"    {[1] * 25}")
    print()

    # Reciprocal-Fibonacci constant: sum_n 1/F_n
    rfc = sum(1.0 / fib[n] for n in range(1, N + 1))
    print(f"Reciprocal-Fibonacci constant zeta_F1(1) (truncated at N={N}):")
    print(f"  approx = {rfc:.10f}  (Erdos: irrational, known value 3.35988566...)")
    print(f"  Riemann zeta(1) diverges (harmonic series).")
    print()

    print("  Verdict (B): F1-shadow zeta has support exactly on the Fibonacci")
    print("  numbers {1,2,3,5,8,13,21,34,...}, with a_1 = 2 and a_m = 1 elsewhere.")
    print("  This is NOT Riemann zeta. zeta_F1(1) converges; zeta(1) diverges.")
    print("  The F1 shadow recovers the reciprocal-Fibonacci constant, an Erdos-")
    print("  irrational object distinct from Riemann zeta.")
    print()


# ---------------------------------------------------------------------
# Cross-comparison and summary
# ---------------------------------------------------------------------

def summary():
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print("Both bare-rung F (experiment A) and F1 scalar-shadow (experiment B)")
    print("produce Dirichlet series structurally distinct from Riemann zeta:")
    print()
    print("  (A) zeta_F^A: finite support of size 12 starting at n=16.")
    print("                Cannot equal Riemann zeta (which has infinite support).")
    print()
    print("  (B) zeta_F1:  infinite support concentrated on Fibonacci numbers.")
    print("                a_1=2 (since F_1=F_2=1), a_m=1 on Fibonacci m's, 0 elsewhere.")
    print("                Equals reciprocal-Fibonacci-zeta, NOT Riemann zeta.")
    print()
    print("Interpretation:")
    print("  - Neither natural F-counting reproduces zeta(s) directly.")
    print("  - Route (D) (cascade zeta = Riemann zeta) is NOT supported by these")
    print("    norm choices and these counting structures.")
    print("  - Three exits:")
    print("    (i)  Use a richer F whose image carries the Z[phi]-arithmetic")
    print("         (icosian primes -> Hecke L-functions, not Riemann zeta).")
    print("    (ii) Reframe: cascade zeta is Hecke-L for K=Q(phi), not Riemann.")
    print("         Then 'Riemann zeta = cascade zeta' is replaced by 'Riemann")
    print("         zeta is a FACTOR of the cascade zeta', via")
    print("         zeta_K(s) = zeta(s) * L(s, chi_5) for K = Q(phi).")
    print("    (iii) Conclude route (D) is dead and pivot back to (A) or (C).")
    print()
    print("The most informative refinement: build a third experiment that counts")
    print("PRIMES OF Z[phi] up to norm N and compares the resulting Dedekind")
    print("zeta-K coefficients to zeta * L(chi_5). If the cascade-native counting")
    print("matches Dedekind zeta-K, we've found the right zeta — it's Hecke, not")
    print("Riemann.")


if __name__ == "__main__":
    experiment_A()
    experiment_B()
    summary()
