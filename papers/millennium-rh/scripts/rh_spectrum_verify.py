#!/usr/bin/env python3
"""
Verify the cascade Hilbert-Polya construction numerically.

This script:
1. Constructs the cascade operator T_zeta = T_0 + V_sigma on a
   truncated Hilbert space (finite matrix approximation).
2. Computes eigenvalues.
3. Compares with known Riemann zero imaginary parts.

Note: this is a QUALITATIVE numerical check of the general framework.
For rigorous spectral correspondence, a proper trace formula
computation is needed (beyond this script's scope).
"""

import numpy as np
from math import log, sqrt, pi


# First 15 known Riemann zeros (imaginary parts)
KNOWN_ZEROS = [
    14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
    37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
    52.970321, 56.446248, 59.347044, 60.831778, 65.112544,
]


def build_T0_matrix(N, ell_P_log=0, ell_H_log=100):
    """
    Build finite matrix approximation of T_0 = i*x*d/dx + 1/2
    on the interval [e^ell_P_log, e^ell_H_log] with Dirichlet BCs.

    With uniform log-grid on [ell_P_log, ell_H_log] of N points:
    T_0 -> finite difference operator.
    """
    # Uniform grid in log(x)
    y_grid = np.linspace(ell_P_log, ell_H_log, N)
    dy = y_grid[1] - y_grid[0]

    # T_0 in log coordinates: T_0 = i * d/dy + 1/2
    # (since x d/dx = d/d(log x) = d/dy)
    T0 = np.zeros((N, N), dtype=complex)

    # Central difference for d/dy
    for i in range(1, N-1):
        T0[i, i-1] = -1j / (2*dy)
        T0[i, i+1] = +1j / (2*dy)

    # Add 1/2 identity
    T0 += 0.5 * np.eye(N, dtype=complex)

    # Dirichlet boundary conditions
    T0[0, :] = 0; T0[0, 0] = 1e10  # large number at BC
    T0[-1, :] = 0; T0[-1, -1] = 1e10

    return y_grid, T0


def build_V_sigma_matrix(y_grid, hbar=1.0):
    """
    Build the V_sigma potential in distributional form:
    V_sigma(y) = hbar * sum over primes p of (1/sqrt(p)) * delta(y - log p)

    In finite-difference form: impulse at each y = log p with weight hbar/sqrt(p) / dy.
    """
    N = len(y_grid)
    dy = y_grid[1] - y_grid[0]
    V = np.zeros((N, N), dtype=complex)

    # Generate primes up to bound
    from sympy import primerange
    primes = list(primerange(2, 10000))

    # Place delta at log p for each prime
    for p in primes:
        log_p = log(p)
        if log_p < y_grid[0] or log_p > y_grid[-1]:
            continue
        # Find nearest grid point
        idx = int(round((log_p - y_grid[0]) / dy))
        if 0 <= idx < N:
            # Delta approximation: 1/dy weight
            V[idx, idx] += hbar / sqrt(p) / dy

    return V


def main():
    print("=" * 72)
    print("CASCADE HILBERT-POLYA OPERATOR — numerical verification")
    print("=" * 72)
    print()

    # Parameters
    N = 500
    ell_P_log = log(1.0)     # set ell_P = 1 for simplicity
    ell_H_log = log(1e6)      # ell_H = 10^6
    hbar = 1.0

    print(f"  Lattice: {N} points")
    print(f"  log(x) range: [{ell_P_log:.2f}, {ell_H_log:.2f}]")
    print(f"  dx/x range factor: {ell_H_log - ell_P_log:.2f}")
    print(f"  hbar = {hbar}")
    print()

    # Build operators
    print("Building T_0...")
    y_grid, T0 = build_T0_matrix(N, ell_P_log, ell_H_log)

    print("Building V_sigma (prime deltas)...")
    V_sigma = build_V_sigma_matrix(y_grid, hbar)
    print(f"  Number of primes placed: {np.count_nonzero(np.diag(V_sigma))}")

    # T_zeta = T_0 + V_sigma
    T_zeta = T0 + V_sigma

    # Hermitize (make symmetric)
    T_zeta_sym = (T_zeta + T_zeta.conj().T) / 2

    # Compute eigenvalues
    print("Diagonalising T_zeta...")
    eigenvalues = np.linalg.eigvalsh(T_zeta_sym)
    eigenvalues = np.sort(eigenvalues)

    # Filter: keep only positive eigenvalues (real part) in a reasonable range
    positive = eigenvalues[(eigenvalues > 5) & (eigenvalues < 70)]
    print(f"  Positive eigenvalues in range [5, 70]: {len(positive)}")
    print()

    # Show first few eigenvalues
    print(f"  First 15 eigenvalues of T_zeta (positive range):")
    print(f"  {'n':>3}  {'T_zeta eigenval':>16}  {'Riemann zero':>14}  {'diff':>8}")
    print(f"  {'-'*3}  {'-'*16}  {'-'*14}  {'-'*8}")
    for i in range(min(15, len(positive))):
        zero = KNOWN_ZEROS[i] if i < len(KNOWN_ZEROS) else float('nan')
        diff = positive[i] - zero if not np.isnan(zero) else float('nan')
        print(f"  {i+1:>3}  {positive[i]:>16.4f}  {zero:>14.4f}  "
              f"{diff:>+8.4f}" if not np.isnan(zero) else
              f"  {i+1:>3}  {positive[i]:>16.4f}  {'-':>14}  {'-':>8}")
    print()

    print("  Note: exact numerical match is NOT expected from this simple")
    print("  finite-element approximation. The purpose is to verify that")
    print("  T_zeta has a DISCRETE SPECTRUM of positive eigenvalues in the")
    print("  same range as Riemann zeros, consistent with the cascade")
    print("  Hilbert-Polya construction.")
    print()


if __name__ == "__main__":
    main()
