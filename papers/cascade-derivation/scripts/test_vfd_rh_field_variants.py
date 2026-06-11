#!/usr/bin/env python3
"""
Test VARIANTS of the VFD-RH field Ψ(s) to see which (if any) match
ζ-zero behaviour empirically.

Variants tested:
  V1: Σ_{n=2}^∞ φ^(-n) (1/√n) sin(log(n)·t + arg(1-n^(-s)))   [A_n=1/√n]
  V2: Σ_{n=2}^∞ φ^(-n) (1/log(n)) sin(log(n)·t + arg(1-n^(-s)))  [A_n=1/log(n)]
  V3: Σ_{p prime} φ^(-p) (log(p)/√p) sin(log(p)·t + arg(1-p^(-s)))  [Weil-style]
  V4: Σ_{p prime, k≥1} φ^(-p^k) (log(p)/p^(k/2)) sin(...)  [full Weil]

For each variant, test whether the field shows the expected behavior:
  (a) |Ψ(0.5+iγ_n)| significantly smaller than |Ψ(σ+iγ_n)| for σ ≠ 0.5
  (b) E(σ) = Σ|Ψ(σ+iγ_k)|² minimized at σ = 0.5

If any variant shows the expected behavior, that's the right formula.
If none do, the VFD-RH framework needs fundamental rework.
"""

from __future__ import annotations

from mpmath import mp, mpf, mpc, sqrt, log, sin, arg, power, im


def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_up_to(N):
    return [n for n in range(2, N + 1) if is_prime(n)]


def vfd_field_v1(s, max_terms=200):
    """V1: A_n = 1/√n, sum over all n ≥ 2."""
    phi = (1 + sqrt(5)) / 2
    field = mpc(0)
    t = im(s)
    for n in range(2, max_terms + 1):
        scale = power(phi, -n)
        A_n = 1 / sqrt(n)
        omega_n = log(n)
        phase = arg(1 - power(n, -s))
        field += scale * A_n * sin(omega_n * t + phase)
    return field


def vfd_field_v2(s, max_terms=200):
    """V2: A_n = 1/log(n), sum over n ≥ 2."""
    phi = (1 + sqrt(5)) / 2
    field = mpc(0)
    t = im(s)
    for n in range(2, max_terms + 1):
        scale = power(phi, -n)
        A_n = 1 / log(n)
        omega_n = log(n)
        phase = arg(1 - power(n, -s))
        field += scale * A_n * sin(omega_n * t + phase)
    return field


def vfd_field_v3(s, max_n=200):
    """V3: Weil-style sum over primes only, A_p = log(p)/√p."""
    phi = (1 + sqrt(5)) / 2
    field = mpc(0)
    t = im(s)
    for p in primes_up_to(max_n):
        scale = power(phi, -p)
        A_p = log(p) / sqrt(p)
        omega_p = log(p)
        phase = arg(1 - power(p, -s))
        field += scale * A_p * sin(omega_p * t + phase)
    return field


def vfd_field_v4(s, max_n=200):
    """V4: full Weil with prime powers, A_{p^k} = log(p)/p^(k/2)."""
    phi = (1 + sqrt(5)) / 2
    field = mpc(0)
    t = im(s)
    for p in primes_up_to(max_n):
        pk = p
        k = 1
        while pk <= max_n:
            scale = power(phi, -pk)
            A = log(p) / power(p, k / 2)
            omega = k * log(p)
            phase = arg(1 - power(p, -s * k))  # k-th power
            field += scale * A * sin(omega * t + phase)
            pk *= p
            k += 1
    return field


def main():
    mp.dps = 40
    known_zeros = [
        14.134725141734693,
        21.022039638771554,
        25.010857580145688,
        30.424876125859513,
        37.586178158825671,
    ]

    variants = [
        ("V1 (1/√n, all n)",  vfd_field_v1),
        ("V2 (1/log n, all n)", vfd_field_v2),
        ("V3 (Weil primes)",   vfd_field_v3),
        ("V4 (Weil full)",     vfd_field_v4),
    ]

    print("=" * 78)
    print("VFD-RH field VARIANTS — empirical zero-correspondence test")
    print("Tests whether |Ψ(σ + iγ_n)| concentrates at σ = 0.5 (RH critical line)")
    print("=" * 78)

    for name, field_fn in variants:
        print(f"\n--- {name} ---")
        # Compute ratio |Ψ(0.5+iγ)| / max(|Ψ(0.4+iγ)|, |Ψ(0.6+iγ)|) for each γ_n
        # Lower ratio = stronger concentration at critical line
        avg_ratio = 0
        for gamma in known_zeros:
            psi_lo = abs(field_fn(mpc(mpf("0.4"), mpf(gamma))))
            psi_cr = abs(field_fn(mpc(mpf("0.5"), mpf(gamma))))
            psi_hi = abs(field_fn(mpc(mpf("0.6"), mpf(gamma))))
            denom = max(psi_lo, psi_hi)
            ratio = float(psi_cr / denom) if denom > 0 else float('inf')
            avg_ratio += ratio
            print(f"  γ={gamma:8.4f}: lo={float(psi_lo):.3e}  "
                  f"cr={float(psi_cr):.3e}  hi={float(psi_hi):.3e}  ratio={ratio:.4f}")
        avg_ratio /= len(known_zeros)
        print(f"  AVG ratio: {avg_ratio:.4f}  "
              f"({'CONCENTRATES at σ=0.5' if avg_ratio < 0.5 else 'no concentration'})")

        # Energy minimization test
        sigmas = [0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7]
        energies = {}
        for sigma in sigmas:
            E = mpf(0)
            for gamma in known_zeros:
                E += abs(field_fn(mpc(mpf(sigma), mpf(gamma)))) ** 2
            energies[sigma] = float(E)
        min_sigma = min(energies, key=energies.get)
        print(f"  Energy min at σ={min_sigma:.2f}  "
              f"(values: {[f'{s}:{energies[s]:.2e}' for s in sigmas]})")

    print()
    print("=" * 78)
    print("Verdict per variant:")
    print("  - 'CONCENTRATES at σ=0.5' (avg ratio < 0.5) is needed for RH-correspondence.")
    print("  - 'Energy min at σ=0.5' is needed for Theorem A (energy minimisation).")
    print("  - If neither holds for any variant, the VFD-RH formula needs rework.")
    print("=" * 78)


if __name__ == "__main__":
    main()
