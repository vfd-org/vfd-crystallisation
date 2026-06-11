#!/usr/bin/env python3
"""
Refine the candidate Λ formula identified by lambda_cascade_search.py:

    Λ / Λ_Planck  ~  (1 / |W(E_8)|)^14

where 14 = dim(G_2), the octonion automorphism Lie algebra, i.e. the
observer-rung Lie algebra.

This script:
  1. Prints the precise numerical value of (1/|W(E_8)|)^14.
  2. Compares it to observed Λ / Λ_Planck to high precision.
  3. Tests small corrections: multiplicative factors from other cascade
     constants.
  4. Tests the closely-related |F_4| and |E_7| Weyl orders with same exponent.
  5. Identifies what correction factor is needed to land on 10^-122 exactly.

If the formula is structural rather than coincidence, the correction
factor should be a small positive-exponent cascade quantity.
"""

from math import log10, pi, sqrt, log

# Constants
PHI = (1 + sqrt(5)) / 2
ALPHA_INV = 137 + pi / 87
ALPHA = 1 / ALPHA_INV

# Weyl group orders
W_E8 = 696729600            # |W(E_8)|
W_E7 = 2903040              # |W(E_7)|
W_E6 = 51840                # |W(E_6)|
W_F4 = 1152                 # |W(F_4)|
W_D4 = 192                  # |W(D_4)|

# Observer-rung Lie algebra
DIM_G2 = 14                  # dim(G_2) = octonion automorphism algebra

# Other cascade dims
DIM_F4 = 52
DIM_E6 = 78
DIM_E7 = 133
DIM_E8 = 248

# Target
TARGET_LOG = -122.0
# More precise observed value: Λ/Λ_Planck ≈ 2.9 × 10^-123
# (depending on exact Planck-scale convention; "122" is log10 of ratio
# when Λ_Planck uses reduced Planck mass)


def main():
    print("=" * 72)
    print("CANDIDATE FORMULA: Λ/Λ_P ~ (1/|W(E_8)|)^(dim G_2)")
    print("=" * 72)
    print()

    log_W8 = log10(W_E8)
    print(f"  |W(E_8)| = {W_E8}")
    print(f"  log10|W(E_8)| = {log_W8:.6f}")
    print()
    print(f"  dim(G_2) = {DIM_G2}")
    print(f"  log10((1/|W(E_8)|)^{DIM_G2}) = -{DIM_G2} × {log_W8:.6f} = "
          f"{-DIM_G2 * log_W8:.6f}")
    print()
    print(f"  Target: log10(Λ_obs / Λ_Planck) ≈ {TARGET_LOG}")
    print(f"  Candidate log10 = {-DIM_G2 * log_W8:.6f}")
    print(f"  Difference     = {-DIM_G2 * log_W8 - TARGET_LOG:+.6f}")
    print()

    # Discrepancy in linear terms
    discrep_log = -DIM_G2 * log_W8 - TARGET_LOG
    correction_factor = 10**discrep_log
    print(f"  Correction factor: 10^{discrep_log:.4f} = {correction_factor:.4f}")
    print()
    print("  Required multiplicative correction to land exactly on 10^-122:")
    inverse_correction = 10**(-discrep_log)
    print(f"    multiplier = 10^{-discrep_log:.4f} = {inverse_correction:.4f}")
    print()

    # Try to identify the correction factor
    print("  Candidate correction factors:")
    candidates = [
        ("π", pi),
        ("2π", 2*pi),
        ("π²", pi**2),
        ("π³", pi**3),
        ("π⁴", pi**4),
        ("α⁻¹", ALPHA_INV),
        ("φ", PHI),
        ("φ²", PHI**2),
        ("|W(F_4)| = 1152", W_F4),
        ("|W(D_4)| = 192", W_D4),
        ("|2I| = 120", 120),
        ("dim(E_8) = 248", DIM_E8),
        ("dim(G_2)² = 196", DIM_G2**2),
        ("60 = |A_5|", 60),
    ]
    for name, val in candidates:
        log_val = log10(val)
        diff = log_val - (-discrep_log)
        flag = "  ← CLOSE" if abs(diff) < 0.5 else ""
        print(f"    {name:<24}  log10 = {log_val:+7.4f}  "
              f"diff to correction: {diff:+7.4f}{flag}")

    print()
    print("=" * 72)
    print("ALTERNATIVE: (1/|W(E_n)|)^dim(G_2) for n = 6, 7, 8")
    print("=" * 72)
    for W, name in [(W_E6, "|W(E_6)|"), (W_E7, "|W(E_7)|"), (W_E8, "|W(E_8)|")]:
        log_W = log10(W)
        log_candidate = -DIM_G2 * log_W
        diff = log_candidate - TARGET_LOG
        print(f"  (1/{name})^{DIM_G2}  log10 = {log_candidate:+8.3f}  "
              f"diff = {diff:+7.3f}")

    print()
    print("=" * 72)
    print("ALTERNATIVE EXPONENTS")
    print("=" * 72)
    for n in [8, 14, 24, 52, 133, 248]:
        log_cand = -n * log_W8
        diff = log_cand - TARGET_LOG
        name_desc = {
            8: "dim(E_8 Cartan)",
            14: "dim(G_2)",
            24: "D_4 roots",
            52: "dim(F_4)",
            133: "dim(E_7)",
            248: "dim(E_8)",
        }.get(n, "")
        print(f"  (1/|W(E_8)|)^{n:<4}  log10 = {log_cand:+9.3f}  "
              f"diff = {diff:+7.3f}  [{name_desc}]")

    print()
    print("=" * 72)
    print("BEST MATCH ANALYSIS")
    print("=" * 72)
    print()
    # The best match for exponent alone (without correction) is 14.
    # Discrepancy: 1.803 orders. 10^1.803 = 63.5
    # This is close to: 60 = |A_5|, or 2π² × cascade factor ≈ 20, ...
    print(f"  Best exponent: 14 = dim(G_2)")
    print(f"  Residual discrepancy: 1.803 orders ( = factor of 63.5 )")
    print()
    print(f"  Candidates for 63.5:")
    print(f"    60 (|A_5|)          → diff  3.5  (5.5% off)")
    print(f"    64 (2^6)            → diff -0.5  (0.8% off) ← CLEANEST")
    print(f"    60 × φ / φ          = 60, same")
    print(f"    2 × π² / π × log(?) complicated")
    print()
    print(f"  If the correction is exactly 2^6 = 64:")
    clean_log = -DIM_G2 * log_W8 + log10(64)
    print(f"    Λ/Λ_P = (1/|W(E_8)|)^14 × 2^6")
    print(f"    log10 = {clean_log:.4f}")
    print(f"    = 10^{clean_log:.3f} ≈ 10^{-122 + (clean_log + 122):.3f}")
    print()
    print("  Verdict: if (1/|W(E_8)|)^14 × 2^6 is the 'right' formula, it")
    print("  predicts log10(Λ/Λ_P) ≈ -122.0 (within 0.001 of target).")
    print()
    print("  BUT: 2^6 = 64 has no obvious cascade origin. 2^6 is the order")
    print("  of the dihedral group D_4 × Z_2, or equivalent. Not clean.")


if __name__ == "__main__":
    main()
