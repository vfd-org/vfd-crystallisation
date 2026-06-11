#!/usr/bin/env python3
"""
GEOMETRY-FIRST SIM step 9: generation operator 𝓖 (icosian norm → Z[φ]-primes).

Construction.
  - Z[φ] arithmetic: elements (a, b) represent a + bφ with a, b ∈ Z.
    Multiplication: (a+bφ)(c+dφ) = (ac+bd) + (ad+bc+bd)φ since φ² = φ+1.
    Galois σ: (a, b) ↦ (a+b, -b).
    Rational norm: N_{Q(√5)/Q}(a+bφ) = a² + ab - b².
  - Quaternion over Z[φ]: q = q_0 + q_1·i + q_2·j + q_3·k, each q_i ∈ Z[φ].
    Norm N_H(q) = q_0² + q_1² + q_2² + q_3² ∈ Z[φ].

Claim being tested.
  For every Z[φ]-prime π that is TOTALLY POSITIVE and has rational norm
  ≤ K, there exists a Z[φ]-quaternion q with N_H(q) = π. This is the
  classical theorem that the icosian ring is a maximal order whose norm
  form is universal for totally positive Z[φ]-primes.

Method.
  1. Enumerate totally positive Z[φ]-primes π with rational norm ≤ K.
  2. For each π, brute-force search over Z[φ]-quaternions q with bounded
     coefficients (|a|, |b| ≤ M) for one satisfying N_H(q) = π.
  3. Report coverage and witness quaternions.

Acceptance.
  - 100% coverage of totally positive Z[φ]-primes of rational norm ≤ 50.
  - Each witness q has integer Z[φ]-coordinates (Lipschitz lattice).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from itertools import product as iproduct

PHI = (1.0 + 5.0 ** 0.5) / 2.0

HERE = Path(__file__).parent
OUTPUT_DIR = HERE / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def zphi_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def zphi_neg(x):
    return (-x[0], -x[1])


def zphi_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def zphi_mul(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def zphi_sigma(x):
    a, b = x
    return (a + b, -b)


def zphi_norm_Q(x):
    a, b = x
    return a * a + a * b - b * b


def zphi_to_float(x):
    return x[0] + x[1] * PHI


def zphi_is_totally_positive(x):
    return zphi_to_float(x) > 0 and zphi_to_float(zphi_sigma(x)) > 0


def quat_norm(q):
    s = (0, 0)
    for qi in q:
        s = zphi_add(s, zphi_mul(qi, qi))
    return s


def quat_to_floats(q):
    return tuple(zphi_to_float(qi) for qi in q)


def zphi_str(x):
    a, b = x
    if b == 0: return f"{a}"
    if a == 0:
        if b == 1: return "φ"
        if b == -1: return "-φ"
        return f"{b}φ"
    sign = "+" if b > 0 else "-"
    bs = abs(b)
    bstr = "" if bs == 1 else str(bs)
    return f"{a}{sign}{bstr}φ"


def main():
    print("=" * 78)
    print("SIM 9: generation operator 𝓖 — icosian norm → Z[φ]-primes")
    print("=" * 78)
    print()

    K_NORM = 50
    M_COEF = 4   # search range for q_i coefficients

    print(f"  Search bound: rational norm ≤ {K_NORM}")
    print(f"  Quaternion coefficient range: |a|, |b| ≤ {M_COEF}")
    print()

    # ---- Enumerate target Z[φ]-primes (canonical small representatives) ----
    print("  Enumerating totally positive Z[φ]-primes with rational norm ≤", K_NORM)
    from sympy import isprime

    # For each rational prime p ≤ K_NORM, find canonical totally-positive Z[φ]-prime
    # representative(s) with small coefficients.
    SMALL = 10
    primes_list = []
    for p in range(2, K_NORM + 1):
        if not isprime(p):
            continue
        if p == 5:
            # Ramified: search for (a, b) with |N| = 5, smallest coefficients
            cands = []
            for a in range(-SMALL, SMALL + 1):
                for b in range(-SMALL, SMALL + 1):
                    x = (a, b)
                    if abs(zphi_norm_Q(x)) == 5 and zphi_is_totally_positive(x):
                        cands.append(x)
            if cands:
                # Pick smallest by sum |a|+|b|, then by float value
                chosen = min(cands, key=lambda x: (abs(x[0]) + abs(x[1]), zphi_to_float(x)))
                primes_list.append({"type": "ramified", "p": p, "x": chosen})
        elif p % 5 in (1, 4):
            # Split: find canonical π and σ(π), both totally positive, both small
            cands = []
            for a in range(-SMALL, SMALL + 1):
                for b in range(-SMALL, SMALL + 1):
                    x = (a, b)
                    if abs(zphi_norm_Q(x)) == p and zphi_is_totally_positive(x):
                        cands.append(x)
            if cands:
                # Pick the two smallest (one for π, one for σ(π))
                # σ(π) is the σ-image of π; both should appear as candidates
                cands_sorted = sorted(cands, key=lambda x: (abs(x[0]) + abs(x[1]),
                                                             zphi_to_float(x)))
                pi = cands_sorted[0]
                primes_list.append({"type": "split", "p": p, "x": pi})
                # σ(π): find its small representative
                sigma_pi = zphi_sigma(pi)
                if sigma_pi != pi and zphi_is_totally_positive(sigma_pi):
                    primes_list.append({"type": "split-σ", "p": p, "x": sigma_pi})
        elif p % 5 in (2, 3):
            # Inert: prime element is p itself
            primes_list.append({"type": "inert", "p": p, "x": (p, 0)})

    # Sort by rational norm
    primes_list.sort(key=lambda pi: (abs(zphi_norm_Q(pi["x"])), zphi_to_float(pi["x"])))
    print(f"  Found {len(primes_list)} target primes:")
    for pi in primes_list:
        x = pi["x"]
        nN = abs(zphi_norm_Q(x))
        print(f"    {pi['type']:<10}  p={pi['p']:<3}  π = {zphi_str(x):<8}  rational norm |N| = {nN}, "
              f"float = {zphi_to_float(x):.4f}")
    print()

    # ---- Search for icosian witness for each prime ----
    print(f"  Searching for icosian witnesses (Lipschitz lattice, |a|,|b| ≤ {M_COEF}) ...")
    print()

    # Pre-compute all q_i candidates
    zphi_candidates = [(a, b) for a in range(-M_COEF, M_COEF + 1) for b in range(-M_COEF, M_COEF + 1)]
    print(f"  |Z[φ]-candidates per slot|: {len(zphi_candidates)}")
    print(f"  Total search space: {len(zphi_candidates)**4} quaternions")
    print()

    # Precompute (q_0² + q_1²) for all (q_0, q_1) pairs, then complete with (q_2, q_3)
    # to speed up search.
    pair_norms = {}
    for q0 in zphi_candidates:
        for q1 in zphi_candidates:
            s = zphi_add(zphi_mul(q0, q0), zphi_mul(q1, q1))
            pair_norms.setdefault(s, []).append((q0, q1))

    results = []
    coverage = 0
    for pi in primes_list:
        target = pi["x"]
        witness = None
        # For each (q_2, q_3), compute residual = target - (q_2² + q_3²), look up in pair_norms
        for q2 in zphi_candidates:
            if witness is not None:
                break
            for q3 in zphi_candidates:
                qsum23 = zphi_add(zphi_mul(q2, q2), zphi_mul(q3, q3))
                resid = zphi_sub(target, qsum23)
                if resid in pair_norms:
                    q01_list = pair_norms[resid]
                    if q01_list:
                        q0, q1 = q01_list[0]
                        witness = (q0, q1, q2, q3)
                        break
        found = witness is not None
        if found:
            coverage += 1
            # Verify
            assert quat_norm(witness) == target
        results.append({
            "type":     pi["type"],
            "p":        pi["p"],
            "pi":       target,
            "witness":  witness,
            "found":    found,
        })
        if found:
            w_str = " + ".join([zphi_str(witness[i]) + ("·i" if i == 1 else "·j" if i == 2 else "·k" if i == 3 else "")
                                 for i in range(4) if witness[i] != (0, 0)])
            print(f"    [✓] {pi['type']:<10} π = {zphi_str(target):<8}  "
                  f"q = {w_str}")
        else:
            print(f"    [✗] {pi['type']:<10} π = {zphi_str(target):<8}  no witness in search range")

    print()
    print(f"  Coverage: {coverage}/{len(primes_list)} = {100*coverage/len(primes_list):.1f}%")
    print()

    # ---- Acceptance ----
    all_covered = (coverage == len(primes_list))
    checks = {
        "totally_positive_primes_enumerated":  (len(primes_list) > 0),
        "all_primes_have_icosian_witness":     all_covered,
        "witnesses_in_Lipschitz_lattice":      all_covered,  # by construction
    }
    print("Acceptance checks:")
    for k, v in checks.items():
        print(f"  {k}: {v}")
    overall = all(checks.values())
    print()
    print(f"OVERALL: {'PASS' if overall else 'FAIL'}")

    out = {
        "K_norm_bound":      K_NORM,
        "M_coef_bound":      M_COEF,
        "n_primes":          len(primes_list),
        "coverage":          coverage,
        "results":           [
            {
                "type":     r["type"],
                "p":        r["p"],
                "pi":       list(r["pi"]),
                "witness":  [list(qi) for qi in r["witness"]] if r["witness"] else None,
                "found":    r["found"],
            }
            for r in results
        ],
        "checks":            {k: bool(v) for k, v in checks.items()},
        "overall_pass":      bool(overall),
    }
    with open(OUTPUT_DIR / "generation_operator_results.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {OUTPUT_DIR / 'generation_operator_results.json'}")
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
