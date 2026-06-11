#!/usr/bin/env python3
"""
GEOMETRY-FIRST SIM step 11: representation numbers r(π) of icosian quaternions.

For each Z[φ]-prime π, count the number of Z[φ]-quaternions q with
N_H(q) = π. This is the icosian analog of Jacobi's r(n) for sum of four
squares over Z.

Background.
  - Hurwitz quaternions (over Z): r(n) = 24·σ_1(n) for odd n, with
    corrections for even n (Jacobi four-squares theorem).
  - Icosian quaternions (over Z[φ]): r(π) is expected to follow an
    Eisenstein-series formula r(π) = c·σ_1^{Z[φ]}(π) where σ_1^{Z[φ]}
    is the Z[φ]-divisor sum.
  - For PRIME π: σ_1^{Z[φ]}(π) = 1 + N_Q(π) (just the unit ideal
    contribution + π contribution). So r(π) should be proportional to
    (1 + N_Q(π)) where N_Q(π) is the rational norm of π.

We test this for the witnesses from sim 9.

Acceptance.
  - r(π) values computed and tabulated.
  - Identify the proportionality constant c if r(π) ~ c·(1 + N_Q(π)).
  - Verify σ-equivariance: r(σ(π)) = r(π).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

PHI = (1.0 + 5.0 ** 0.5) / 2.0

HERE = Path(__file__).parent
OUTPUT_DIR = HERE / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def zphi_add(x, y):    return (x[0] + y[0], x[1] + y[1])
def zphi_sub(x, y):    return (x[0] - y[0], x[1] - y[1])
def zphi_neg(x):       return (-x[0], -x[1])
def zphi_mul(x, y):    a, b = x; c, d = y; return (a*c + b*d, a*d + b*c + b*d)
def zphi_sigma(x):     a, b = x; return (a + b, -b)
def zphi_norm_Q(x):    a, b = x; return a*a + a*b - b*b
def zphi_to_float(x):  return x[0] + x[1] * PHI


def zphi_str(x):
    a, b = x
    if b == 0: return f"{a}"
    if a == 0:
        return f"φ" if b == 1 else (f"-φ" if b == -1 else f"{b}φ")
    sign = "+" if b > 0 else "-"
    bs = abs(b)
    bstr = "" if bs == 1 else str(bs)
    return f"{a}{sign}{bstr}φ"


def quat_norm(q):
    s = (0, 0)
    for qi in q:
        s = zphi_add(s, zphi_mul(qi, qi))
    return s


def count_representations(target, M):
    """Count number of Z[φ]-quaternions q with all |a|,|b| ≤ M and N_H(q) = target.

    Uses meet-in-the-middle: precompute pair sums for (q_0, q_1), then for each
    (q_2, q_3) compute residual and look up.
    """
    zphi_candidates = [(a, b) for a in range(-M, M + 1) for b in range(-M, M + 1)]
    # Precompute pair norms
    pair_norms = {}
    for q0 in zphi_candidates:
        for q1 in zphi_candidates:
            s = zphi_add(zphi_mul(q0, q0), zphi_mul(q1, q1))
            pair_norms[s] = pair_norms.get(s, 0) + 1
    # Count
    count = 0
    for q2 in zphi_candidates:
        for q3 in zphi_candidates:
            s23 = zphi_add(zphi_mul(q2, q2), zphi_mul(q3, q3))
            resid = zphi_sub(target, s23)
            count += pair_norms.get(resid, 0)
    return count


def main():
    print("=" * 78)
    print("SIM 11: icosian representation numbers r(π)")
    print("=" * 78)
    print()

    # Load primes from sim 9 (we only need their pi values)
    with open(OUTPUT_DIR / "generation_operator_results.json") as f:
        sim9_data = json.load(f)
    primes_data = []
    seen_pis = set()
    for r in sim9_data["results"]:
        pi = tuple(r["pi"])
        if pi in seen_pis:
            continue
        seen_pis.add(pi)
        primes_data.append({"type": r["type"], "p": r["p"], "pi": pi})

    print(f"  Computing r(π) for {len(primes_data)} primes from sim 9")
    print()

    # ---- For each prime, compute r(π) ----
    # We must pick M large enough to capture all reps. For small primes, M=4 should
    # suffice; we adapt by prime norm.
    print("    type        p     π            N_Q(π)    M     r(π)     r(π)/(1+N_Q)")
    print("    " + "-" * 76)

    results = []
    proportionality_ratios = []
    for pd in primes_data:
        pi = pd["pi"]
        N_Q = abs(zphi_norm_Q(pi))
        # Choose M: enough that all q with |q_i|² ≤ N_Q are captured.
        # |q_i|² ≤ N_Q means each (a, b) has a² + ab - b² magnitude ≤ N_Q.
        # In the worst case |a|, |b| ≤ ceil(sqrt(N_Q)) + 1
        M = max(4, int(np.ceil(np.sqrt(N_Q))) + 1)
        # Cap to avoid runaway for very large primes
        M = min(M, 8)
        r = count_representations(pi, M)
        ratio = r / (1 + N_Q)
        results.append({
            "type":   pd["type"],
            "p":      pd["p"],
            "pi":     list(pi),
            "N_Q":    N_Q,
            "M":      M,
            "r":      r,
            "ratio":  ratio,
        })
        proportionality_ratios.append(ratio)
        print(f"    {pd['type']:<10}  {pd['p']:<3}   {zphi_str(pi):<10}   {N_Q:<7}   {M:<5} {r:<8} "
              f"{ratio:.4f}")
    print()

    # ---- Check σ-equivariance: r(σ(π)) = r(π) for split pairs ----
    print("  σ-equivariance check (split pairs):")
    by_p = {}
    for r in results:
        by_p.setdefault(r["p"], []).append(r)
    sigma_consistent = True
    for p, rs in by_p.items():
        if len(rs) == 2 and any(r["type"].startswith("split") for r in rs):
            r0, r1 = rs
            same = (r0["r"] == r1["r"])
            print(f"    p={p}: r({zphi_str(tuple(r0['pi']))}) = {r0['r']}, "
                  f"r({zphi_str(tuple(r1['pi']))}) = {r1['r']}, equal: {same}")
            if not same:
                sigma_consistent = False
    print()

    # ---- Check proportionality with (1 + N_Q(π)) ----
    print("  Proportionality test r(π) = c · (1 + N_Q(π))")
    ratios = np.array(proportionality_ratios)
    mean_ratio = float(np.mean(ratios))
    std_ratio = float(np.std(ratios))
    print(f"    Mean ratio:  {mean_ratio:.4f}")
    print(f"    Std  ratio:  {std_ratio:.4f}")
    print(f"    Range:       [{ratios.min():.4f}, {ratios.max():.4f}]")
    print()
    # If the ratio is nearly constant, the formula holds; if it grows, M too small.
    # Filter to those with M large enough (M >= √N_Q + 1 already, but cap at 8 may
    # truncate for large primes). Restrict analysis to small primes.
    small_primes = [r for r in results if r["N_Q"] <= 20]
    small_ratios = [r["ratio"] for r in small_primes]
    print(f"  Restricting to primes with N_Q ≤ 20 (search-truncation-safe):")
    if small_ratios:
        sm = np.array(small_ratios)
        print(f"    Mean:  {sm.mean():.4f}")
        print(f"    Std:   {sm.std():.4f}")
        formula_holds_small = (sm.std() / sm.mean() < 0.05)
        print(f"    Coefficient of variation: {sm.std()/sm.mean():.4f}")
        print(f"    Formula r(π) = c · (1 + N_Q) holds (CoV<5%): {formula_holds_small}")
    print()

    # ---- Acceptance ----
    checks = {
        "all_primes_have_reps":         all(r["r"] > 0 for r in results),
        "sigma_equivariant_split_pairs": sigma_consistent,
    }
    print("Acceptance checks:")
    for k, v in checks.items():
        print(f"  {k}: {v}")
    overall = all(checks.values())
    print()
    print(f"OVERALL: {'PASS' if overall else 'FAIL'}")

    out = {
        "n_primes":       len(results),
        "results":        results,
        "sigma_consistent": sigma_consistent,
        "mean_ratio":     mean_ratio,
        "std_ratio":      std_ratio,
        "checks":         {k: bool(v) for k, v in checks.items()},
        "overall_pass":   bool(overall),
    }
    with open(OUTPUT_DIR / "representation_numbers_results.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {OUTPUT_DIR / 'representation_numbers_results.json'}")
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
