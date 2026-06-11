#!/usr/bin/env python3
"""
GEOMETRY-FIRST SIM step 6: tridiagonal intersection matrix L_1.

For a P-polynomial association scheme, the eigenvalues of the
tridiagonal matrix L_1 = tridiag(a_i; b_i, c_i) equal the 9 distinct
eigenvalues of A_1.  This is the standard Sturm-Liouville-style
confirmation of the P-polynomial structure.

Loads intersection-array data from sim_p_polynomial_structure.py's
output, builds L_1, computes its spectrum, compares.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
OUTPUT_DIR = HERE / "output"


def main():
    print("=" * 78)
    print("SIM 6: tridiagonal intersection matrix L_1 spectrum check")
    print("=" * 78)
    print()

    with open(OUTPUT_DIR / "p_polynomial_results.json") as f:
        d = json.load(f)

    b = d["intersection_array_b_seq"]   # b_0..b_7
    c = d["intersection_array_c_seq"]   # c_1..c_8
    a = d["intersection_array_a_seq"]   # a_0..a_8
    eigvals_A1 = d["eigenvalues_A1"]    # 9 distinct eigenvalues of A_1

    print(f"  Intersection array:")
    print(f"    b_0..b_7 = {b}")
    print(f"    c_1..c_8 = {c}")
    print(f"    a_0..a_8 = {a}")
    print(f"  A_1 eigenvalues: {[f'{x:+.4f}' for x in eigvals_A1]}")
    print()

    # Build L_1 as 9x9 tridiagonal. Standard convention:
    #   L_1 · e_i = c_i · e_{i-1} + a_i · e_i + b_i · e_{i+1}
    # In matrix form: L_1[k, i] = coefficient of e_k in L_1·e_i.
    #   L_1[i-1, i] = c_i  (super-diagonal, column i, row i-1)
    #   L_1[i, i]   = a_i  (diagonal)
    #   L_1[i+1, i] = b_i  (sub-diagonal, column i, row i+1)
    # Index translation: c = c_1..c_8 (indices 0..7); b = b_0..b_7 (indices 0..7).
    n = 9
    L1 = np.zeros((n, n))
    for i in range(n):
        L1[i, i] = a[i]
    for i in range(n - 1):
        # Super-diagonal at row i, col i+1: contribution is c_{i+1} = c[i]
        L1[i, i + 1] = c[i]
        # Sub-diagonal at row i+1, col i: contribution is b_i = b[i]
        L1[i + 1, i] = b[i]

    print(f"  L_1 matrix (tridiagonal, 9x9):")
    for i in range(n):
        row_str = "  "
        for j in range(n):
            if abs(L1[i, j]) > 1e-9:
                row_str += f"{int(L1[i, j]):3d} "
            else:
                row_str += "  · "
        print(row_str)
    print()

    # Compute eigenvalues of L_1
    eigvals_L1 = sorted(np.linalg.eigvals(L1).real.tolist(), reverse=True)
    print(f"  L_1 eigenvalues (sorted desc):")
    for j, lam in enumerate(eigvals_L1):
        print(f"    {lam:+10.6f}")
    print()

    # Compare to A_1 eigenvalues (already sorted desc)
    print(f"  Comparison L_1 vs A_1 spectra:")
    print(f"    {'j':<3} {'L_1 eigval':<14} {'A_1 eigval':<14} {'|diff|':<12}")
    print(f"    " + "-" * 46)
    max_dev = 0.0
    for j in range(n):
        l1_val = eigvals_L1[j]
        a1_val = eigvals_A1[j]
        dev = abs(l1_val - a1_val)
        max_dev = max(max_dev, dev)
        print(f"    {j:<3} {l1_val:+10.6f}    {a1_val:+10.6f}    {dev:.2e}")
    print()
    print(f"  Max deviation: {max_dev:.2e}")
    match = max_dev < 1e-8
    print(f"  L_1 eigenvalues match A_1 eigenvalues (to 1e-8): {match}")
    print()

    # Acceptance
    print(f"OVERALL: {'PASS' if match else 'FAIL'}")

    out = {
        "L_1_matrix":             L1.tolist(),
        "L_1_eigenvalues":        [float(x) for x in eigvals_L1],
        "A_1_eigenvalues":        eigvals_A1,
        "max_deviation":          float(max_dev),
        "spectra_match":          bool(match),
        "interpretation":         (
            "If L_1 (built from the intersection-array tridiagonal) and A_1 "
            "share the same spectrum, V_600's distance-regular structure is "
            "fully captured by the intersection array. This is the classical "
            "Sturm-Liouville-style verification of P-polynomial associativity."
        ),
    }
    with open(OUTPUT_DIR / "tridiagonal_L1_results.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"Wrote {OUTPUT_DIR / 'tridiagonal_L1_results.json'}")
    return 0 if match else 1


if __name__ == "__main__":
    sys.exit(main())
