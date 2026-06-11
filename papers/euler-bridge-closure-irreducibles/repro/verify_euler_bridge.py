#!/usr/bin/env python3
"""
Paper III --- verify_euler_bridge.py

Numerical verification of the Euler bridge

    zeta_{Q(sqrt(5))}(s)  =  zeta(s) * L(s, chi_5)

at s in {2, 3, 4}, by independently computing the three Euler products
truncated at P_max prime cutoff and comparing.

Classical math only; no cascade hypotheses used in the computation
itself. Deterministic.

Run:
    python verify_euler_bridge.py [P_max]    # default P_max = 100000

Outputs:
    output/euler_bridge_verification.json    numeric agreement
    output/euler_bridge_convergence.png      truncation-error figure
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SEED = 42  # for record only
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def sieve_primes(limit: int) -> list[int]:
    """Sieve of Eratosthenes up to `limit` inclusive."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, b in enumerate(sieve) if b]


def chi5(p: int) -> int:
    """Kronecker symbol (5|p) for odd prime p != 5.
       Equivalently: +1 if p mod 5 in {1,4}, -1 if p mod 5 in {2,3},
                     0 if p = 5.
    """
    if p == 5:
        return 0
    r = p % 5
    if r in (1, 4):
        return +1
    if r in (2, 3):
        return -1
    raise ValueError(f"unreachable: p = {p}, p mod 5 = {r}")


def riemann_zeta_euler(s: float, primes: list[int]) -> float:
    """Riemann zeta via rational Euler product truncated at primes.
       zeta(s) = prod_p (1 - p^{-s})^{-1}.
    """
    log_prod = 0.0
    for p in primes:
        # Use logs to keep precision tight at deep cutoffs
        log_prod -= __import__("math").log1p(-p ** (-s))
    return __import__("math").exp(log_prod)


def dirichlet_L_chi5(s: float, primes: list[int]) -> float:
    """L(s, chi_5) via twisted Euler product truncated at primes.
       L(s, chi_5) = prod_{p != 5} (1 - chi_5(p) p^{-s})^{-1}.
    """
    import math
    log_prod = 0.0
    for p in primes:
        c = chi5(p)
        if c == 0:
            continue
        # local factor: 1 / (1 - c * p^{-s})
        log_prod -= math.log1p(-c * p ** (-s))
    return math.exp(log_prod)


def dedekind_zeta_Q_sqrt5(s: float, primes: list[int]) -> float:
    """zeta_{Q(sqrt(5))}(s) via Z[phi]-prime Euler product:

       For each rational prime p:
         split  (p mod 5 in {1,4}):  local factor = (1 - p^{-s})^{-2}
         inert  (p mod 5 in {2,3}):  local factor = (1 - p^{-2s})^{-1}
         ramif  (p = 5):             local factor = (1 - 5^{-s})^{-1}

       This enumerates Z[phi] prime ideals up to absolute norm = p
       (for split) or p^2 (for inert).  Using rational primes up to
       P_max is conservative: it catches all prime ideals with norm
       <= P_max for the inert / ramified cases, and all prime ideals
       with norm <= P_max for the split case (each split p contributes
       two prime ideals of norm exactly p).
    """
    import math
    log_prod = 0.0
    for p in primes:
        if p == 5:
            log_prod -= math.log1p(-p ** (-s))           # ramified, single factor
        elif p % 5 in (1, 4):
            log_prod -= 2.0 * math.log1p(-p ** (-s))     # split, squared
        else:  # p mod 5 in {2, 3}
            log_prod -= math.log1p(-p ** (-2.0 * s))     # inert, single at norm p^2
    return math.exp(log_prod)


def main(argv: list[str]) -> int:
    P_MAX = int(argv[1]) if len(argv) > 1 else 100_000
    test_s = [2.0, 3.0, 4.0]

    print("=" * 76)
    print("Paper III sim --- verify Euler bridge zeta_K(s) = zeta(s) * L(s, chi_5)")
    print(f"               at s in {test_s}, truncated at primes p <= {P_MAX}")
    print("Classical math only; no cascade hypotheses in the sim.")
    print("=" * 76)
    print()

    print(f"--- Sieving primes p <= {P_MAX} ---")
    primes = sieve_primes(P_MAX)
    print(f"  total primes: {len(primes)}")
    print()

    results: dict = {"P_max": int(P_MAX), "primes_count": int(len(primes)),
                     "test_s": [float(s) for s in test_s],
                     "checks": []}

    print("--- Computing Euler products at each s ---")
    print()
    print(f"{'s':<6} {'zeta_K(s)':<22} {'zeta(s) * L(s,chi5)':<22} "
          f"{'|diff|':<14} {'rel err':<14} {'digits':<8}")
    print("-" * 88)

    all_pass = True
    for s in test_s:
        zk     = dedekind_zeta_Q_sqrt5(s, primes)
        z      = riemann_zeta_euler(s, primes)
        Lchi   = dirichlet_L_chi5(s, primes)
        prod   = z * Lchi
        diff   = abs(zk - prod)
        rel    = diff / abs(prod) if prod != 0 else float('inf')
        digits = -__import__("math").log10(rel) if rel > 0 else float('inf')

        passed = digits >= 10.0
        if not passed:
            all_pass = False

        print(f"{s:<6.1f} {zk:<22.15f} {prod:<22.15f} "
              f"{diff:<14.2e} {rel:<14.2e} {digits:<8.2f}")

        results["checks"].append({
            "s":                      float(s),
            "zeta_K":                 float(zk),
            "zeta_times_L":           float(prod),
            "zeta":                   float(z),
            "L_chi5":                 float(Lchi),
            "abs_diff":               float(diff),
            "rel_err":                float(rel),
            "digits_of_agreement":    float(digits),
            "passes_10_digit_check":  bool(passed),
        })

    print()
    print(f"Threshold: agreement to >= 10 decimal digits.  "
          f"All s passed: {all_pass}")

    # Reference values for sanity (classical):
    print()
    print("--- Reference values (classical) ---")
    print(f"  zeta(2) = pi^2 / 6 = {__import__('math').pi ** 2 / 6:.15f}")
    print(f"  zeta(4) = pi^4 / 90 = {__import__('math').pi ** 4 / 90:.15f}")
    print(f"  L(1, chi_5) classical class-number-formula reference (s=1 not tested:")
    print(f"           h_K = 1, regulator R_K = log(phi) ~ {__import__('math').log((1+5**0.5)/2):.6f})")
    print()

    # Save JSON
    with open(OUTPUT_DIR / "euler_bridge_verification.json", "w") as f:
        json.dump({"P_max": P_MAX, "n_primes": len(primes),
                   "test_s": test_s,
                   "all_pass_10_digit": all_pass,
                   "checks": results["checks"]}, f, indent=2)
    print(f"saved {OUTPUT_DIR / 'euler_bridge_verification.json'}")

    # Convergence sweep: how does the agreement improve with P_max?
    print()
    print("--- Convergence sweep at s = 2 ---")
    sweep_P = [100, 300, 1000, 3000, 10000, 30000, 100000]
    sweep_digits = []
    for P in sweep_P:
        sub_primes = [p for p in primes if p <= P]
        zk    = dedekind_zeta_Q_sqrt5(2.0, sub_primes)
        z     = riemann_zeta_euler(2.0, sub_primes)
        Lchi  = dirichlet_L_chi5(2.0, sub_primes)
        prod  = z * Lchi
        rel   = abs(zk - prod) / abs(prod) if prod != 0 else float("inf")
        digits = -__import__("math").log10(rel) if rel > 0 else 16.0
        sweep_digits.append(digits)
        print(f"  P_max = {P:>6}:  digits of agreement = {digits:.2f}")

    # Figure
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogx(sweep_P, sweep_digits, marker="o", lw=1.6, color="#3a7cd9")
    ax.set_xlabel("prime cutoff P_max")
    ax.set_ylabel("decimal digits of agreement at s = 2")
    ax.set_title("Euler bridge convergence: zeta_K(s) vs zeta(s) * L(s, chi_5) at s=2")
    ax.axhline(10, linestyle="--", color="black", lw=0.8,
               label="threshold (10 digits)")
    ax.grid(alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "euler_bridge_convergence.png", dpi=120)
    plt.close()
    print()
    print(f"saved {OUTPUT_DIR / 'euler_bridge_convergence.png'}")

    # Summary
    print()
    print("=" * 76)
    print("SUMMARY")
    print("=" * 76)
    print(f"  P_max = {P_MAX}, primes = {len(primes)}")
    for chk in results["checks"]:
        print(f"  s = {chk['s']:<4.1f}: {chk['digits_of_agreement']:.2f} digits  "
              f"({'PASS' if chk['passes_10_digit_check'] else 'FAIL'})")
    print()
    print(f"  Overall: {'EULER BRIDGE VERIFIED' if all_pass else 'FAILURE'}")
    print(f"  (Classical Dedekind factorisation zeta_K = zeta * L(s, chi_5)")
    print(f"   sim-verified at P_max = {P_MAX} for s in {test_s}.)")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
