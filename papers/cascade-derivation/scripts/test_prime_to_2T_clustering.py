#!/usr/bin/env python3
"""
Bridge sim for RH cascade reframing (task #115):
  Do classical primes empirically cluster on the 24-point σ-fixed
  locus 2T ⊂ 2I, vs the 96-point complement?

If YES (with statistical significance over null baseline AND over
composite control) → the Prime Detector L canonicity claim has
empirical support; the bridge from cascade-RH to classical RH is
viable.  If NO → the bridge is empirically dead at single cascade
level and we must be honest in the paper.

Tests three candidate maps p → vertex index in 2I:

  Map A — residue:    idx = (p mod 120)
                       (Dirichlet-biased; null = 24/120 = 20%)
  Map B — log-φ:      θ = log_φ(p) mod 1; idx = floor(120·θ)
                       (cascade-φ-shell address)
  Map C — Z[φ]-norm:  pick the "shell-rank" of p via its φ-adic
                       expansion; idx = (rank · g) mod 120
                       for g = closest-to-uniform stride

For each map, compare:
  (1) primes (n=168 primes ≤ 1000)        — target set
  (2) composites (same range)              — control
  (3) all integers in range                — null reference

Statistical test: binomial vs p_0 = 24/120 = 0.2.

If primes' fraction on 2T differs significantly from baseline AND
from composite control, the Prime Detector canonicity claim is
empirically alive.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path
from collections import Counter
from fractions import Fraction

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, qq_eq, qq_key,
    build_vertices, vertex_index_map,
)


PHI = (1 + math.sqrt(5)) / 2
LOG_PHI = math.log(PHI)


# --- σ-fixed locus identification ---------------------------------

def sigma_pair(x):
    return (x[0], -x[1])


def sigma_on_quat(q):
    return tuple(sigma_pair(c) for c in q)


def identify_sigma_fixed(verts):
    """Return set of vertex indices i with σ(verts[i]) = verts[i]."""
    fixed = set()
    for i, v in enumerate(verts):
        if qq_eq(sigma_on_quat(v), v):
            fixed.add(i)
    return fixed


# --- Prime utilities ----------------------------------------------

def sieve(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2, N + 1) if is_prime[i]]
    composites = [i for i in range(4, N + 1) if not is_prime[i]]
    return primes, composites


# --- Three candidate maps -----------------------------------------

def map_A_residue(n):
    """Residue map: idx = n mod 120."""
    return n % 120


def map_B_logphi(n):
    """log-φ phase map: idx = floor(120 · {log_φ(n)})."""
    if n < 2:
        return 0
    theta = (math.log(n) / LOG_PHI) % 1.0
    return int(120 * theta) % 120


def map_C_zphi_norm(n):
    """Z[φ]-shell-rank map: rank of n in the Lucas/Fibonacci ladder.

    The shell-rank uses the closest Fibonacci F_k such that
    F_k <= n < F_{k+1}.  Then position within the φ-shell is
    (n - F_k) / (F_{k+1} - F_k) ∈ [0, 1).
    Map: idx = (k * 7 + floor(10 * pos)) mod 120
    (stride 7 chosen as gcd(7, 120) = 1 to maximise spread).
    """
    if n < 2:
        return 0
    fibs = [1, 2]
    while fibs[-1] <= n:
        fibs.append(fibs[-1] + fibs[-2])
    # Now fibs[-1] > n >= fibs[-2]
    k = len(fibs) - 2
    F_lo, F_hi = fibs[k - 1], fibs[k]
    if F_hi == F_lo:
        pos = 0.0
    else:
        pos = (n - F_lo) / (F_hi - F_lo)
    return (k * 7 + int(10 * pos)) % 120


CANDIDATE_MAPS = [
    ("A: residue p mod 120",       map_A_residue),
    ("B: log_phi(p) mod 1",        map_B_logphi),
    ("C: Z[phi]-shell rank+pos",   map_C_zphi_norm),
]


# --- Statistical tests --------------------------------------------

def binomial_test_two_sided(k, n, p):
    """Approximate two-sided binomial test using normal approximation
    (n is large enough here)."""
    if n == 0:
        return float('nan'), float('nan')
    p_hat = k / n
    se = math.sqrt(p * (1 - p) / n)
    if se == 0:
        return p_hat, float('nan')
    z = (p_hat - p) / se
    # Two-sided p-value via standard normal
    # (we use erfc to avoid scipy dependency)
    p_value = math.erfc(abs(z) / math.sqrt(2))
    return z, p_value


def cluster_rate(numbers, map_fn, sigma_fixed_set):
    """Compute the 2T-clustering rate for a set of numbers under map_fn."""
    if not numbers:
        return 0, 0, float('nan')
    on_2T = sum(1 for n in numbers if map_fn(n) in sigma_fixed_set)
    total = len(numbers)
    rate = on_2T / total
    return on_2T, total, rate


def print_distribution(numbers, map_fn, label):
    """Show how many numbers land at each vertex (useful for spotting clusters)."""
    counts = Counter(map_fn(n) for n in numbers)
    top = counts.most_common(10)
    print(f"    {label}: top 10 vertex indices (count): "
          f"{', '.join(f'v{v}:{c}' for v, c in top)}")


# --- Main ----------------------------------------------------------

def main():
    print("=" * 76)
    print("BRIDGE SIM — do primes cluster on σ-fixed 2T locus of 2I?")
    print("Tests 3 candidate maps p → vertex index, vs primes/composites/all.")
    print("Null baseline: 24/120 = 20% (random vertex assignment).")
    print("=" * 76)

    # --- Build 2I and identify 2T (σ-fixed locus) ---
    print("\n[Setup] Building 2I (120 unit icosians) and 2T (σ-fixed)...")
    verts = build_vertices()
    sigma_fixed = identify_sigma_fixed(verts)
    print(f"        2I = {len(verts)} vertices")
    print(f"        2T = {len(sigma_fixed)} σ-fixed vertices "
          f"(expected 24, baseline = {len(sigma_fixed)/len(verts):.1%})")
    p_null = len(sigma_fixed) / len(verts)

    # --- Generate test sets ---
    N = 1000
    primes, composites = sieve(N)
    all_ints = list(range(2, N + 1))
    print(f"\n[Setup] Test sets in [2, {N}]:")
    print(f"        primes:     {len(primes)}")
    print(f"        composites: {len(composites)}")
    print(f"        all ints:   {len(all_ints)}")

    # --- Run each candidate map ---
    for map_name, map_fn in CANDIDATE_MAPS:
        print()
        print("=" * 76)
        print(f"Map {map_name}")
        print("=" * 76)

        for set_name, numbers in [
            ("PRIMES",     primes),
            ("composites", composites),
            ("all ints",   all_ints),
        ]:
            on_2T, total, rate = cluster_rate(numbers, map_fn, sigma_fixed)
            z, p_val = binomial_test_two_sided(on_2T, total, p_null)
            verdict = (
                "** CLUSTERS **" if (p_val < 0.01 and rate > p_null * 1.10)
                else "AVOIDS" if (p_val < 0.01 and rate < p_null * 0.90)
                else "uniform"
            )
            print(f"  {set_name:11s}: {on_2T:4d}/{total:4d} on 2T = "
                  f"{rate:.4f}  (z={z:+6.2f}, p={p_val:.3g})  {verdict}")
            print_distribution(numbers, map_fn, set_name)

        # Comparison: primes vs composites
        p_on, p_tot, p_rate = cluster_rate(primes, map_fn, sigma_fixed)
        c_on, c_tot, c_rate = cluster_rate(composites, map_fn, sigma_fixed)
        # Two-proportion z-test
        if p_tot > 0 and c_tot > 0:
            pooled = (p_on + c_on) / (p_tot + c_tot)
            se_diff = math.sqrt(pooled * (1 - pooled) *
                                (1 / p_tot + 1 / c_tot))
            if se_diff > 0:
                z_diff = (p_rate - c_rate) / se_diff
                p_diff = math.erfc(abs(z_diff) / math.sqrt(2))
                print(f"  → primes vs composites: Δrate = {p_rate - c_rate:+.4f}  "
                      f"(z={z_diff:+.2f}, p={p_diff:.3g})")

    # --- Verdict ---
    print()
    print("=" * 76)
    print("BRIDGE VERDICT:")
    print("  - If any map shows ** CLUSTERS ** for PRIMES but NOT for composites,")
    print("    AND primes-vs-composites Δrate is significant, the Prime Detector")
    print("    L canonicity claim has empirical support and the cascade→classical")
    print("    RH bridge is alive.")
    print("  - If all maps give 'uniform' for primes (rate ≈ baseline), the bridge")
    print("    is empirically dead at single cascade level. The cascade-RH theorem")
    print("    must be reported as a STANDALONE result, not a literal RH proxy.")
    print("=" * 76)


if __name__ == "__main__":
    main()
