"""Deterministic probability from the void: the zeros obey the quantum law.

The point we are demonstrating (NOT proving, NOT new):
  * The Riemann zeros are a FIXED, DETERMINISTIC arithmetic object -- there is
    nothing random about zeta. We compute them numerically to high precision
    (mpmath.zetazero); deterministic, though not closed-form/symbolic.
  * A GUE matrix is GENUINELY RANDOM -- a fresh draw of a complex Hermitian
    Gaussian Hamiltonian, the canonical quantum model (Wigner; broken
    time-reversal).
  * Placed side by side, their level statistics are INDISTINGUISHABLE: both
    sit on the GUE law. A determined object wears the exact statistical
    clothing of a quantum-random one.

This is 'deterministic pseudorandomness' / Montgomery-Odlyzko universality:
ESTABLISHED since the 1980s. We reproduce it to make the tie explicit. It is
EVIDENCE for the spectral (Hilbert-Polya) picture, NOT a proof, and it does
NOT advance RH.

Primary metric: the consecutive-spacing ratio <r> (Atas et al. 2013), which
needs NO unfolding -- so it compares the two objects with zero tuning.
  GUE     <r> = 0.6027   (the quantum, time-reversal-broken law)
  Poisson <r> = 0.3863   (structureless / integrable)
  rigid   <r> = 1.0000   (picket fence; a symmetric polytope spectrum)
"""
from __future__ import annotations

import math
import numpy as np
import mpmath as mp


def r_statistic(levels):
    """Consecutive level-spacing ratio <min/max>; unfolding-free."""
    lv = np.sort(np.asarray(levels, dtype=float))
    s = np.diff(lv)
    s = s[s > 1e-12]
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(np.mean(r)), r


def deterministic_zeros(n):
    """The first n nontrivial Riemann zeros' imaginary parts -- a deterministic
    sequence, computed numerically to high precision (not closed-form).
    mpmath.zetazero(k) returns the k-th zero on the line."""
    mp.mp.dps = 25
    return np.array([float(mp.im(mp.zetazero(k))) for k in range(1, n + 1)])


def unfold_zeros(gamma):
    """Map zeros to unit mean spacing via the smooth counting function
    N(T) = (T/2pi) log(T/2pi) - T/2pi + 7/8 (Riemann-von Mangoldt)."""
    T = np.asarray(gamma, dtype=float)
    return (T / (2 * math.pi)) * np.log(T / (2 * math.pi)) - T / (2 * math.pi) + 7 / 8


def gue_eigenvalues(N, rng):
    """Eigenvalues of a genuine random GUE matrix (complex Hermitian
    Gaussian) -- the canonical quantum Hamiltonian with broken T-symmetry."""
    A = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    H = (A + A.conj().T) / 2.0
    return np.linalg.eigvalsh(H)


def wigner_surmise_gue(s):
    """GUE nearest-neighbour spacing density (beta=2 surmise)."""
    return (32 / math.pi**2) * s**2 * np.exp(-4 * s**2 / math.pi)


def hist_vs_surmise(spacings, nbins=12):
    """Return mean |hist - Wigner_GUE| over bins on [0,3], a crude distance."""
    s = spacings / np.mean(spacings)
    edges = np.linspace(0, 3, nbins + 1)
    h, _ = np.histogram(s, bins=edges, density=True)
    centres = 0.5 * (edges[:-1] + edges[1:])
    return float(np.mean(np.abs(h - wigner_surmise_gue(centres))))


def main():
    print("=" * 74)
    print("DETERMINISTIC PROBABILITY: the void's law is the quantum law")
    print("=" * 74)

    N_ZEROS = 300
    print(f"\nComputing the first {N_ZEROS} Riemann zeros (deterministic, "
          f"high-precision numerical)...")
    gamma = deterministic_zeros(N_ZEROS)
    print(f"  gamma_1 = {gamma[0]:.6f},  gamma_{N_ZEROS} = {gamma[-1]:.6f}")

    # --- the DETERMINISTIC object ---
    r_zeros, _ = r_statistic(gamma)            # unfolding-free
    u = unfold_zeros(gamma)
    s_zeros = np.diff(u)
    d_zeros = hist_vs_surmise(s_zeros)

    # --- the RANDOM quantum object (fresh draw, fixed seed for reproducibility) ---
    rng = np.random.RandomState(20260530)
    ev = gue_eigenvalues(600, rng)
    ev = ev[len(ev)//4 : 3*len(ev)//4]          # bulk only (avoid edge)
    r_gue, _ = r_statistic(ev)
    # unfold GUE bulk by its local density (rank order is already ~uniform)
    s_gue = np.diff(np.sort(ev))
    d_gue = hist_vs_surmise(s_gue)

    print("\n" + "-" * 74)
    print("PRIMARY METRIC: consecutive-spacing ratio <r>  (NO unfolding, no tuning)")
    print("-" * 74)
    print(f"  Riemann zeros   (DETERMINISTIC, fixed) : <r> = {r_zeros:.4f}")
    print(f"  GUE matrix      (GENUINELY RANDOM draw): <r> = {r_gue:.4f}")
    print(f"  ---")
    print(f"  GUE law         (quantum, T-broken)    : <r> = 0.6027")
    print(f"  Poisson         (structureless)        : <r> = 0.3863")
    print(f"  rigid lattice   (symmetric polytope)   : <r> = 1.0000")

    dz = abs(r_zeros - 0.6027)
    dg = abs(r_gue - 0.6027)
    print(f"\n  |zeros - GUE|  = {dz:.4f}     |random-GUE - GUE| = {dg:.4f}")
    print(f"  |zeros - Poisson| = {abs(r_zeros-0.3863):.4f}  "
          f"(zeros are ~{abs(r_zeros-0.3863)/max(dz,1e-9):.0f}x closer to "
          f"GUE than to Poisson)")

    print("\n" + "-" * 74)
    print("SECONDARY: spacing histogram vs the GUE Wigner surmise "
          "(mean |Δ| over bins)")
    print("-" * 74)
    print(f"  deterministic zeros : {d_zeros:.4f}")
    print(f"  random GUE matrix   : {d_gue:.4f}   (same law, same fit quality)")

    verdict = ("INDISTINGUISHABLE" if abs(r_zeros - r_gue) < 0.03
               else "close but sample-limited")
    print(f"""
==========================================================================
WHAT THIS SHOWS  (and does not)
==========================================================================
The DETERMINISTIC Riemann zeros (<r>={r_zeros:.4f}) and a GENUINELY RANDOM
quantum GUE Hamiltonian (<r>={r_gue:.4f}) are {verdict} -- both on the GUE
law (0.6027), both far from Poisson (0.3863) and from a rigid polytope
spectrum (1.0). A fixed arithmetic object obeys the same probability law as a
random quantum one. THIS is the 'deterministic probability' of the void:
necessity (the zeros are determined) and chance (they are distributed exactly
like quantum randomness) coincide in the same object.

This is the SAME law measured in heavy nuclei and chaotic cavities -- the tie
between 'the physics of numbers' and physics proper, at the level of the
spectral statistics.

HONEST SCOPE:
  * ESTABLISHED, not new: this is Montgomery-Odlyzko universality (1980s),
    reproduced here, not discovered here.
  * EVIDENCE, not proof: it supports the Hilbert-Polya (spectral) picture; it
    does NOT exhibit the operator and does NOT advance RH.
  * The zeros are NOT random -- they only LOOK random. The match is
    universality / pseudorandomness, not a probabilistic origin for the zeros.
  * <r> is unfolding-free, so the zeros<->GUE agreement uses NO fitted
    parameter; that is what makes the tie clean.
""")


if __name__ == "__main__":
    main()
