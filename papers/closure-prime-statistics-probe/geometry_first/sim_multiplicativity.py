#!/usr/bin/env python3
"""
GEOMETRY-FIRST SIM step 12: multiplicativity of r(π) on composite Z[φ]-numbers.

Sim 11 found r(π) = 8·(1 + N_Q(π)) for odd Z[φ]-primes. The next question
is whether r is multiplicative as an arithmetic function on Z[φ]:

  Claim: r(α·β) / 8 = σ_1^{Z[φ]}(α·β) where σ_1^{Z[φ]} is the Z[φ]-divisor
         sum function. For coprime α, β: σ_1(α·β) = σ_1(α) · σ_1(β).
         So r(α·β) / 8 = σ_1(α) · σ_1(β) = (r(α)/8) · (r(β)/8).

  Equivalently: r(α·β) = r(α)·r(β) / 8 for coprime Z[φ]-elements.

We test this for small composite Z[φ]-elements.

If multiplicativity holds, then the icosian theta series

  Θ_𝓘(s) := Σ_α r(α) · N_Q(α)^{-s}

has an Euler product:

  Θ_𝓘(s) = 8 · Π_π  (1 - N_Q(π)^{-s})^{-1}·(1 - N_Q(π)^{1-s})^{-1}
         = 8 · ζ_K(s) · ζ_K(s-1)

This is the classical Eichler/Hecke result for the icosian quadratic form.
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


def count_representations(target, M):
    zphi_candidates = [(a, b) for a in range(-M, M + 1) for b in range(-M, M + 1)]
    pair_norms = {}
    for q0 in zphi_candidates:
        for q1 in zphi_candidates:
            s = zphi_add(zphi_mul(q0, q0), zphi_mul(q1, q1))
            pair_norms[s] = pair_norms.get(s, 0) + 1
    count = 0
    for q2 in zphi_candidates:
        for q3 in zphi_candidates:
            s23 = zphi_add(zphi_mul(q2, q2), zphi_mul(q3, q3))
            resid = zphi_sub(target, s23)
            count += pair_norms.get(resid, 0)
    return count


def main():
    print("=" * 78)
    print("SIM 12: multiplicativity of r(π) on composite Z[φ]")
    print("=" * 78)
    print()

    # Compute r(π) for selected coprime pairs
    # Format: (α_pair, β_pair, α·β, name)
    test_cases = [
        # (α, β, α·β, label_α, label_β, label_αβ)
        ((3, 0), (2, 1), (6, 3),  "3",     "2+φ",   "6+3φ"),     # 3·(2+φ) = 6+3φ
        ((2, 0), (2, 1), (4, 2),  "2",     "2+φ",   "4+2φ"),     # 2·(2+φ) = 4+2φ
        ((3, 0), (3, 1), (9, 3),  "3",     "3+φ",   "9+3φ"),     # 3·(3+φ)
        # split * split (distinct primes above different rational primes)
        ((3, 1), (4, 1), (13, 8), "3+φ",   "4+φ",   "13+8φ"),    # (3+φ)(4+φ) = 13+8φ
        # split * split-conjugate = rational integer
        ((3, 1), (4, -1), (11, 0), "3+φ", "4-φ",   "11"),         # (3+φ)(4-φ) = 11
        # 2 · 3 = 6 (coprime inerts)
        ((2, 0), (3, 0), (6, 0), "2",     "3",     "6"),
    ]

    # Verify all products
    print("  Verifying product correctness:")
    for alpha, beta, prod, la, lb, lab in test_cases:
        actual = zphi_mul(alpha, beta)
        if actual != prod:
            print(f"    {la} · {lb} = {actual} != {prod} (expected {lab}) — error")
        else:
            print(f"    {la} · {lb} = {lab} ✓")
    print()

    # Compute r(α), r(β), r(α·β) for each test case
    print("  Computing r(α), r(β), r(α·β) ...")
    print()
    results = []
    for alpha, beta, prod, la, lb, lab in test_cases:
        N_alpha = abs(zphi_norm_Q(alpha))
        N_beta  = abs(zphi_norm_Q(beta))
        N_prod  = abs(zphi_norm_Q(prod))
        M_a = max(4, int(np.ceil(np.sqrt(N_alpha))) + 1)
        M_b = max(4, int(np.ceil(np.sqrt(N_beta))) + 1)
        M_p = max(4, int(np.ceil(np.sqrt(N_prod))) + 1)
        # Cap M for performance (raise cap to support norm-209 case)
        M_a = min(M_a, 8)
        M_b = min(M_b, 8)
        M_p = min(M_p, 16)
        print(f"    α={la} (N_Q={N_alpha}, M={M_a}), β={lb} (N_Q={N_beta}, M={M_b}), "
              f"αβ={lab} (N_Q={N_prod}, M={M_p})")
        r_a = count_representations(alpha, M_a)
        r_b = count_representations(beta,  M_b)
        r_p = count_representations(prod,  M_p)
        # Multiplicativity test:
        # If r/8 is multiplicative: r(αβ)/8 = r(α)/8 · r(β)/8 => r(αβ) = r(α)·r(β)/8
        predicted = r_a * r_b // 8
        match = (r_p == predicted)
        results.append({
            "alpha":    list(alpha),
            "beta":     list(beta),
            "prod":     list(prod),
            "label":    f"{la} · {lb}",
            "r_alpha":  r_a,
            "r_beta":   r_b,
            "r_prod":   r_p,
            "predicted": predicted,
            "match":    bool(match),
        })
        print(f"      r(α) = {r_a}, r(β) = {r_b}, r(αβ) = {r_p}, predicted r(α)·r(β)/8 = {predicted}, "
              f"{'✓' if match else '✗'}")
        print()

    # Try divisor-sum formula directly for the simplest composite: 6 = 2·3
    # σ_1^{Z[φ]}(6) = sum over Z[φ]-ideal divisors of (6). For 6 = 2·3 with 2, 3 both inert:
    # divisors are (1), (2), (3), (6). Norms: 1, 4, 9, 36. Sum: 50.
    # Predicted: r(6) = 8 · 50 = 400.
    sigma_1_6 = 1 + 4 + 9 + 36
    pred_r6 = 8 * sigma_1_6
    print(f"  Direct σ_1 check for 6 = 2·3:")
    print(f"    Z[φ]-ideal divisors of (6): (1), (2), (3), (6)")
    print(f"    Rational norms: 1, 4, 9, 36 → σ_1 = {sigma_1_6}")
    print(f"    Predicted r(6) = 8·σ_1 = {pred_r6}")
    # Find r(6) from results
    r6_actual = next((r["r_prod"] for r in results if r["label"] == "2 · 3"), None)
    print(f"    Actual r(6)    = {r6_actual}")
    print(f"    Match: {r6_actual == pred_r6}")
    print()

    # ---- σ_1-multiplicativity overall ----
    print("  σ_1-multiplicativity summary:")
    all_match = all(r["match"] for r in results)
    print(f"    r(αβ) = r(α)·r(β)/8 for all coprime test cases: {all_match}")
    print()

    # ---- Acceptance ----
    checks = {
        "multiplicativity_holds":  all_match,
    }
    print("Acceptance checks:")
    for k, v in checks.items():
        print(f"  {k}: {v}")
    overall = all(checks.values())
    print()
    print(f"OVERALL: {'PASS' if overall else 'FAIL'}")

    out = {
        "n_test_cases":   len(results),
        "results":        results,
        "checks":         {k: bool(v) for k, v in checks.items()},
        "overall_pass":   bool(overall),
    }
    with open(OUTPUT_DIR / "multiplicativity_results.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {OUTPUT_DIR / 'multiplicativity_results.json'}")
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
