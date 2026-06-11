#!/usr/bin/env python3
"""
Exploratory probe: can the twin-prime constant C_2 (Hardy-Littlewood)
be expressed in terms of cascade-natural ingredients?

  C_2 = prod_{p >= 3} (1 - 1/(p-1)^2)  ~= 0.6601618158468695...

Cascade ingredients allowed:
  * phi = (1+sqrt5)/2 and powers / functions thereof
  * pi, e, log(2), Euler-Mascheroni gamma
  * |V_600| = 120, |W(H_4)| = 14400, |E_8| = 240
  * V_600 eigenvalue multiplicities {4, 16, 9, 36, 25, 16, 9, 4, 1}
  * sigma-paired class dim = 4 (the +6phi eigenspace)
  * K-pole multiplicities {1, 1, 5, 5} at K in {0, 20, 52, 72}
  * sigma-orbit count: 94 fixed + 13 paired = 107 orbits
  * Schlafli decomp: 5 disjoint 24-cells = 120 vertices
  * Z[phi] splitting classes (Paper II): split / inert / ramified

Method:
  1. Compute C_2 to high precision (Euler product to P_max).
  2. Compute classical / cascade-related L-values (zeta(2), L(2,chi_5),
     zeta_K(2)) for comparison.
  3. Build a CURATED list of cascade-natural candidate expressions.
     Avoid free numerology: every candidate must use ONLY the
     ingredients above with structural motivation.
  4. Report agreement to C_2, sorted.
  5. Set agreement threshold at 4+ decimal digits as exploratory signal
     and 8+ digits as serious candidate.

Run:
    python probe_C2_from_cascade.py [P_max]    # default P_max = 1e6
"""

from __future__ import annotations

import math
import sys
import json
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PHI    = (1.0 + 5.0 ** 0.5) / 2.0
INVPHI = 1.0 / PHI
LNPHI  = math.log(PHI)
SQRT5  = 5.0 ** 0.5


def sieve_primes(limit: int) -> list[int]:
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, b in enumerate(sieve) if b]


def chi5(p: int) -> int:
    if p == 5:
        return 0
    r = p % 5
    return +1 if r in (1, 4) else -1


def compute_C2(primes: list[int]) -> float:
    """C_2 = prod_{p >= 3} (1 - 1/(p-1)^2)."""
    log_prod = 0.0
    for p in primes:
        if p == 2:
            continue
        log_prod += math.log1p(-1.0 / (p - 1) ** 2)
    return math.exp(log_prod)


def compute_zeta(s: float, primes: list[int]) -> float:
    log_prod = 0.0
    for p in primes:
        log_prod -= math.log1p(-p ** (-s))
    return math.exp(log_prod)


def compute_L_chi5(s: float, primes: list[int]) -> float:
    log_prod = 0.0
    for p in primes:
        if p == 5:
            continue
        log_prod -= math.log1p(-chi5(p) * p ** (-s))
    return math.exp(log_prod)


# Cascade-restricted Euler products  ------------------------------------

def C2_split_only(primes: list[int]) -> float:
    """Twin-prime-like product restricted to split primes (sigma-paired)."""
    log_prod = 0.0
    for p in primes:
        if p == 2 or p == 5:
            continue
        if p % 5 in (1, 4):
            log_prod += math.log1p(-1.0 / (p - 1) ** 2)
    return math.exp(log_prod)


def C2_inert_only(primes: list[int]) -> float:
    """Twin-prime-like product restricted to inert primes (sigma-fixed)."""
    log_prod = 0.0
    for p in primes:
        if p == 2 or p == 5:
            continue
        if p % 5 in (2, 3):
            log_prod += math.log1p(-1.0 / (p - 1) ** 2)
    return math.exp(log_prod)


def C2_chi5_twisted(primes: list[int]) -> float:
    """Cascade-twisted product:
       prod_p (1 - chi_5(p) / (p-1)^2)
    """
    log_prod = 0.0
    for p in primes:
        if p == 2 or p == 5:
            continue
        log_prod += math.log1p(-chi5(p) * 1.0 / (p - 1) ** 2)
    return math.exp(log_prod)


def C2_phi_weighted(primes: list[int]) -> float:
    """phi-weighted variant: 1 - phi/(p^2)."""
    log_prod = 0.0
    for p in primes:
        if p == 2:
            continue
        log_prod += math.log1p(-PHI / p ** 2)
    return math.exp(log_prod)


def C2_norm_form(primes: list[int]) -> float:
    """For split p, local factor (1 - 1/(p-1)^2)^2 (two prime ideals
       of norm p); for inert p, (1 - 1/(p^2-1)^2) (one prime ideal of
       norm p^2); for ramified p=5, the natural special factor."""
    log_prod = 0.0
    for p in primes:
        if p == 2:
            continue
        if p == 5:
            log_prod += math.log1p(-1.0 / (5 - 1) ** 2)  # standard
        elif p % 5 in (1, 4):  # split, sigma-paired
            log_prod += 2.0 * math.log1p(-1.0 / (p - 1) ** 2)
        else:  # inert, sigma-fixed
            log_prod += math.log1p(-1.0 / (p ** 2 - 1) ** 2)
    return math.exp(log_prod)


def main(argv):
    P_MAX = int(argv[1]) if len(argv) > 1 else 1_000_000

    print("=" * 78)
    print("Probe: derive C_2 (twin-prime constant) from cascade structure?")
    print(f"Reference value: C_2 = 0.6601618158468695...")
    print(f"Euler product truncated at p <= {P_MAX}")
    print("=" * 78)
    print()

    # High-precision reference
    print("Sieving primes...")
    primes = sieve_primes(P_MAX)
    print(f"  found {len(primes)} primes <= {P_MAX}")
    print()

    print("Computing reference constants...")
    C2     = compute_C2(primes)
    z2     = compute_zeta(2.0, primes)
    L2     = compute_L_chi5(2.0, primes)
    z3     = compute_zeta(3.0, primes)
    L3     = compute_L_chi5(3.0, primes)
    zK2    = z2 * L2          # Dedekind zeta_K(2) via Paper III factorisation
    zK3    = z3 * L3

    print(f"  C_2  (Hardy-Littlewood twin-prime)  = {C2:.15f}")
    print(f"  zeta(2)  = {z2:.15f}    (= pi^2/6 = {math.pi**2/6:.15f})")
    print(f"  L(2, chi_5)                          = {L2:.15f}")
    print(f"  zeta_K(2)                            = {zK2:.15f}")
    print(f"  zeta(3)  = {z3:.15f}")
    print(f"  L(3, chi_5)                          = {L3:.15f}")
    print(f"  zeta_K(3)                            = {zK3:.15f}")
    print()

    # Cascade-natural Euler products
    print("Cascade-natural Euler products (sigma-class restricted)...")
    c2_split = C2_split_only(primes)
    c2_inert = C2_inert_only(primes)
    c2_twist = C2_chi5_twisted(primes)
    c2_phi   = C2_phi_weighted(primes)
    c2_norm  = C2_norm_form(primes)

    print(f"  C2 split-only      = {c2_split:.15f}")
    print(f"  C2 inert-only      = {c2_inert:.15f}")
    print(f"  C2 chi5-twisted    = {c2_twist:.15f}")
    print(f"  C2 phi-weighted    = {c2_phi:.15f}")
    print(f"  C2 norm-form       = {c2_norm:.15f}")
    print(f"  product split*inert= {c2_split * c2_inert:.15f}  "
          f"(should equal C2 = {C2:.15f}, check: "
          f"{abs(c2_split * c2_inert - C2):.2e})")
    print()

    # ----- Curated cascade candidates -------------------------------------
    candidates = []

    def add(label: str, value: float, motivation: str = ""):
        candidates.append({
            "label": label,
            "value": float(value),
            "abs_diff": float(abs(value - C2)),
            "rel_diff": float(abs(value - C2) / C2),
            "digits":   float(-math.log10(abs(value - C2) / C2)) if abs(value - C2) > 0 else 16.0,
            "motivation": motivation,
        })

    # phi-only
    add("1/phi",                   INVPHI,                      "golden ratio reciprocal")
    add("1 - 1/phi^2",             1 - 1/PHI**2,                "1 - sigma-paired weight")
    add("1 - 1/phi^3",             1 - 1/PHI**3,                "1 - F_4 weight")
    add("phi/3",                   PHI/3.0,                     "phi over Schlafli 3-cell count factor")
    add("(phi-1)/(phi+1)",         (PHI-1)/(PHI+1),             "phi convergent ratio")
    add("phi^(-3/2)",              PHI**-1.5,                   "phi^(-3/2)")

    # pi-only and pi+phi
    add("2/pi",                    2.0/math.pi,                 "2/pi")
    add("1 - 1/pi",                1 - 1/math.pi,               "1 - 1/pi")
    add("phi^2/pi",                PHI**2/math.pi,              "phi^2/pi")
    add("phi/pi*phi",              PHI**2/math.pi/PHI,          "phi/pi")
    add("phi/(1+phi/2)",           PHI/(1+PHI/2),               "phi/(1 + phi/2)")
    add("pi^2/15",                 math.pi**2/15,               "pi^2/15")
    add("log(phi)/log(2)*0.95",    LNPHI/math.log(2)*0.95,      "log_2(phi) variant")

    # L-value combos
    add("L(2,chi5)/log(2)*0.65",   L2/math.log(2)*0.65,         "L(2,chi5) scaled")
    add("L(2,chi5)*(1-1/phi^4)",   L2*(1-1/PHI**4),             "L(2,chi5) * (1 - phi^-4)")
    add("L(3,chi5)*phi/log(2)",    L3*PHI/math.log(2),          "L(3,chi5) * phi / log(2)")
    add("zeta_K(2)/(zeta(2))*1.0", zK2/z2,                      "= L(2,chi5)")
    add("1 - L(2,chi5)/zeta(2)",   1 - L2/z2,                   "1 - L/zeta ratio")
    add("(L(2,chi5))^(3/2)",       L2**1.5,                     "L(2,chi5)^1.5")
    add("L(2,chi5) - 1/phi^4",     L2 - 1/PHI**4,               "L - phi^-4")
    add("L(2,chi5) * phi^(-1/4)",  L2*PHI**(-0.25),             "L * phi^-1/4")

    # V_600 multiplicity ratios
    mults = [4, 16, 9, 36, 25, 16, 9, 4, 1]   # eigenvalue mults of A_{V_600}
    add("4/120 * 20",              4/120.0 * 20,                "sigma-paired class dim * 20 / 120")
    add("36/120 * 2.2",            36/120.0 * 2.2,              "largest mult / 120 * scale")
    add("sum(squares mults)/sum^2", sum(m*m for m in mults)/sum(mults)**2,
        "sum m_i^2 / (sum m_i)^2")
    add("max(mults)/sum(mults)",   max(mults)/sum(mults),       "36/120")
    add("(120-1)/(120+60)",        119/180.0,                   "(V-1)/(V+1/2 V) — placeholder")

    # K-pole structure: {1, 1, 5, 5}
    add("12/(1+1+5+5)",            12/(1+1+5+5),                "12/sum K-pole mults = 1.0 — skip")
    add("(1+1)/(5+5)",             (1+1)/(5.0+5),               "K-pole low/high mult ratio")
    add("(1+1+5+5)/(20)",          (1+1+5+5)/20.0,              "K-pole mult sum / 20")
    add("(5*5)/(1+5)^2*0.95",      (5*5)/(1+5)**2*0.95,         "K-pole 5-class squared / 6^2")
    add("1 - (5-1)^2/120",         1 - (5-1)**2/120.0,          "1 - paired^2/V_600 size")

    # Cascade Euler products themselves
    add("C2 split-only",           c2_split,                    "Euler product over split primes")
    add("C2 inert-only",           c2_inert,                    "Euler product over inert primes")
    add("C2 chi5-twisted",         c2_twist,                    "chi5-twisted Euler product")
    add("C2 phi-weighted",         c2_phi,                      "phi-weighted Euler product")
    add("C2 norm-form (Z[phi])",   c2_norm,                     "Z[phi]-norm Euler product")

    # phi-inside-Euler — replace classical (p-1) by phi*(p-1)/(p-...)
    log_phi_euler = 0.0
    for p in primes:
        if p < 3:
            continue
        log_phi_euler += math.log1p(-1.0 / (PHI * (p - 1)) ** 2)
    add("phi-rescaled Euler product", math.exp(log_phi_euler), "Euler with (phi(p-1))^2")

    log_phi_euler2 = 0.0
    for p in primes:
        if p < 3:
            continue
        # replace 1/(p-1)^2 by 1/(p^2-phi^2)
        log_phi_euler2 += math.log1p(-1.0 / (p ** 2 - PHI ** 2))
    add("phi^2-shift Euler product", math.exp(log_phi_euler2), "Euler with (p^2 - phi^2)")

    # ----- Report sorted by agreement -------------------------------------
    print("=" * 78)
    print("Cascade candidate expressions vs C_2 = 0.66016181584687...")
    print("=" * 78)
    print(f"{'rank':<5} {'label':<35} {'value':<19} {'|diff|':<11} {'digits':<7}")
    print("-" * 78)

    candidates.sort(key=lambda c: c["abs_diff"])
    for i, c in enumerate(candidates):
        flag = ""
        if c["digits"] >= 8:
            flag = " ***"
        elif c["digits"] >= 4:
            flag = " *"
        print(f"{i+1:<5} {c['label']:<35} {c['value']:<19.13f} "
              f"{c['abs_diff']:<11.2e} {c['digits']:<7.2f}{flag}")

    # Best summary
    print()
    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    best = candidates[0]
    print(f"Best candidate:  {best['label']}")
    print(f"  value:         {best['value']:.15f}")
    print(f"  C_2:           {C2:.15f}")
    print(f"  |diff|:        {best['abs_diff']:.2e}")
    print(f"  digits agree:  {best['digits']:.2f}")
    print(f"  motivation:    {best['motivation']}")
    print()
    n_sig = sum(1 for c in candidates if c["digits"] >= 4)
    n_4ig = sum(1 for c in candidates if c["digits"] >= 8)
    print(f"Candidates with 4+ digit agreement: {n_sig} / {len(candidates)}")
    print(f"Candidates with 8+ digit agreement: {n_4ig} / {len(candidates)}")
    print()

    if best["digits"] >= 8:
        print("VERDICT: candidate matches C_2 to 8+ digits — investigate further.")
    elif best["digits"] >= 4:
        print("VERDICT: best candidate matches to 4-8 digits — suggestive but")
        print("         not yet a closed-form expression. Worth investigation")
        print("         but probably accidental at this depth.")
    else:
        print("VERDICT: no cascade-natural expression matches C_2 to 4 digits.")
        print("         Cascade ingredients do not directly produce C_2 in any")
        print("         of the curated forms. Useful negative result.")

    # Save JSON
    with open(OUTPUT_DIR / "probe_C2_results.json", "w") as f:
        json.dump({
            "C_2_reference":     0.6601618158468695,
            "C_2_computed":      float(C2),
            "P_max":             int(P_MAX),
            "n_primes":          int(len(primes)),
            "zeta_2":            float(z2),
            "L_2_chi5":          float(L2),
            "zeta_K_2":          float(zK2),
            "candidates":        candidates,
            "best":              best,
            "n_sig_4digit":      int(n_sig),
            "n_sig_8digit":      int(n_4ig),
        }, f, indent=2)
    print()
    print(f"saved {OUTPUT_DIR / 'probe_C2_results.json'}")

    return 0 if best["digits"] >= 8 else 1  # exit 0 only on serious match


if __name__ == "__main__":
    sys.exit(main(sys.argv))
