"""WO-RH-WEIL-POSITIVITY-MECHANISM-001 -- core harness for the Weil functional.

Riemann-Weil explicit formula (ζ), even test function h with cosine transform
g(u) = (1/2π) ∫ h(r) cos(r u) dr :

    Σ_ρ h(γ_ρ)  =  h(i/2) + h(-i/2)                      [POLE: poles of ξ at 0,1]
                +  (1/2π) ∫ h(r) [ Re ψ(1/4 + i r/2) - log π ] dr   [ARCH]
                -  2 Σ_{n≥1} Λ(n) n^{-1/2} g(log n)        [PRIME]

Weil criterion: RH  ⇔  Σ_ρ h(γ_ρ) ≥ 0 for every h of positive type (h = φ⋆φ̃,
ĥ = |φ̂|² ≥ 0).  We evaluate BOTH sides:

  * zero-side   Z(h)  = Σ_ρ h(γ_ρ)            (γ_ρ from mpmath.zetazero; VALIDATION)
  * formula-side F(h) = ARCH + POLE - PRIME    (no zeros; the construction side)

and build the Hermitian Weil GRAM on a finite test-function basis, then split it
into the boundary-capacity term H = ARCH + POLE and the prime residual R = PRIME:
    Q = H - R.
The split is canonical (it is literally the explicit formula's terms), not chosen.

Everything here is for the Riemann zeta function itself (classical RH). Known
zeros are used ONLY to validate F == Z and to demonstrate the off-line teeth;
they never enter the definition of F, H, R.
"""
from __future__ import annotations

import json
import math
import os

import numpy as np
import mpmath as mp

mp.mp.dps = 15
HERE = os.path.dirname(__file__)


# ---- basis test functions: even Gaussians at heights t_a, width sigma ------
def psi(r, t, sigma):
    return np.exp(-(r - t) ** 2 / (2 * sigma ** 2))


def h_even(r, t, sigma):
    """even building block centred at +/- t."""
    return psi(r, t, sigma) + psi(-r, t, sigma)


def h_product(r, ta, tb, sigma):
    """even, positive-type-style product h_{ab}(r) = ψ_a ψ_b (even-symmetrised)."""
    return (psi(r, ta, sigma) * psi(r, tb, sigma)
            + psi(-r, ta, sigma) * psi(-r, tb, sigma))


# ---- the three explicit-formula terms (numerical, validated vs zeros) ------
def _digamma_re(r):
    # Re psi(1/4 + i r/2)
    return float(mp.re(mp.digamma(mp.mpf('0.25') + 1j * (r / 2))))


_LOGPI = math.log(math.pi)


def arch_term(hvals, rgrid):
    Omega = np.array([_digamma_re(r) - _LOGPI for r in rgrid])
    return np.trapz(hvals * Omega, rgrid) / (2 * math.pi)


def pole_term(ta, tb, sigma):
    """h_{ab}(i/2) + h_{ab}(-i/2), analytic (sum of Gaussians at complex arg)."""
    def g(r):  # h_product evaluated at complex r (analytic continuation)
        return (mp.e ** (-(r - ta) ** 2 / (2 * sigma ** 2)) *
                mp.e ** (-(r - tb) ** 2 / (2 * sigma ** 2)) +
                mp.e ** (-(-r - ta) ** 2 / (2 * sigma ** 2)) *
                mp.e ** (-(-r - tb) ** 2 / (2 * sigma ** 2)))
    return float(mp.re(g(mp.mpc(0, 0.5)) + g(mp.mpc(0, -0.5))))


def _primes(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = b"\x00" * len(s[i * i::i])
    return [i for i in range(2, n + 1) if s[i]]


def g_transform(ta, tb, sigma, u):
    """g(u) = (1/2π) ∫ h_{ab}(r) cos(r u) dr, analytic for Gaussians.
    h_{ab} = sum of Gaussians centred at +/-(stuff); use the closed form
    (1/2π)∫ exp(-(r-c)^2/2w^2) cos(ru) dr = (w/2π√(2π))... we just do it
    numerically-stably via the Gaussian FT: ∫exp(-(r-c)^2/2w^2)e^{-iru}dr
    = √(2π) w exp(-iuc) exp(-w^2 u^2/2)."""
    # h_product = ψ_a ψ_b + (mirror). ψ_a ψ_b = exp(-[(r-ta)^2+(r-tb)^2]/2σ^2)
    # = exp(-((r-m)^2)/ (σ^2) ) * const, with m=(ta+tb)/2, plus Gaussian width.
    # Combine: (r-ta)^2+(r-tb)^2 = 2(r-m)^2 + (ta-tb)^2/2, m=(ta+tb)/2.
    m = (ta + tb) / 2
    w2 = sigma ** 2 / 2.0            # effective variance of the product Gaussian
    amp = math.exp(-((ta - tb) ** 2) / (4 * sigma ** 2))
    # FT of amp*exp(-(r-m)^2/(2 w2)) -> centred terms at +/- m (from the mirror)
    def ft(center):
        return amp * math.sqrt(2 * math.pi * w2) * math.cos(u * center) * \
            math.exp(-w2 * u * u / 2)
    return (ft(m) + ft(-m)) / (2 * math.pi)


def prime_term(ta, tb, sigma, P=2000):
    tot = 0.0
    for p in _primes(P):
        lp = math.log(p)
        k, pk = 1, p
        while k * lp < 60:
            tot += lp / math.sqrt(pk) * g_transform(ta, tb, sigma, k * lp)
            k += 1
            pk *= p
            if pk > 10 ** 14:
                break
    return 2 * tot


# ---- zero side (validation) ------------------------------------------------
_ZCACHE = {}


def zeta_gammas(n):
    if n not in _ZCACHE:
        _ZCACHE[n] = [float(mp.im(mp.zetazero(k))) for k in range(1, n + 1)]
    return _ZCACHE[n]


def zero_side(ta, tb, sigma, nz=80):
    g = zeta_gammas(nz)
    rgrid = None
    tot = 0.0
    for gm in g:
        tot += h_product(gm, ta, tb, sigma) + h_product(-gm, ta, tb, sigma)
    return tot


# ---- the Weil Gram and its H - R split ------------------------------------
def weil_gram(heights, sigma=2.0, nz=80, rmax=80, npts=1600, P=2000):
    rgrid = np.linspace(-rmax, rmax, npts)
    m = len(heights)
    H = np.zeros((m, m))      # boundary capacity = ARCH + POLE
    R = np.zeros((m, m))      # prime residual
    Z = np.zeros((m, m))      # zero-side (validation)
    for a in range(m):
        for b in range(m):
            hv = h_product(rgrid, heights[a], heights[b], sigma)
            arch = arch_term(hv, rgrid)
            pole = pole_term(heights[a], heights[b], sigma)
            H[a, b] = arch + pole
            R[a, b] = prime_term(heights[a], heights[b], sigma, P)
            Z[a, b] = zero_side(heights[a], heights[b], sigma, nz)
    Q = H - R
    return {"H": H, "R": R, "Q_formula": Q, "Q_zero": Z}


def main():
    heights = [14.0, 21.0, 25.0, 30.0, 33.0]
    sigma = 2.0
    print("=" * 72)
    print("Weil functional harness (zeta) -- formula-side vs zero-side")
    print("=" * 72)
    G = weil_gram(heights, sigma=sigma, nz=80)
    Q, Z, H, R = G["Q_formula"], G["Q_zero"], G["H"], G["R"]
    # symmetrise
    Q = (Q + Q.T) / 2
    Z = (Z + Z.T) / 2
    rel = np.max(np.abs(Q - Z)) / (np.max(np.abs(Z)) + 1e-12)
    print("\n  basis heights:", heights, " sigma=", sigma)
    print("  max|Q_formula - Q_zero| / max|Q_zero| = %.2e  (consistency)" % rel)
    eQ = np.linalg.eigvalsh(Q)
    eH = np.linalg.eigvalsh((H + H.T) / 2)
    eR = np.linalg.eigvalsh((R + R.T) / 2)
    print("  Q = H - R  eigenvalues: min=%.4e  -> PSD=%s" % (eQ.min(),
                                                            eQ.min() > -1e-6))
    print("  H (ARCH+POLE) eigenvalues: min=%.4e  -> positive kernel=%s"
          % (eH.min(), eH.min() > -1e-6))
    print("  R (PRIME) eigenvalues: min=%.4e max=%.4e -> indefinite=%s"
          % (eR.min(), eR.max(), eR.min() < -1e-9 and eR.max() > 1e-9))
    os.makedirs(os.path.join(HERE, "results", "phase_2_weil_harness"),
                exist_ok=True)
    with open(os.path.join(HERE, "results", "phase_2_weil_harness",
                           "harness.json"), "w") as f:
        json.dump({"heights": heights, "sigma": sigma,
                   "consistency_rel_err": rel,
                   "Q_min_eig": float(eQ.min()), "Q_PSD": bool(eQ.min() > -1e-6),
                   "H_min_eig": float(eH.min()),
                   "H_positive_kernel": bool(eH.min() > -1e-6),
                   "R_min_eig": float(eR.min()), "R_max_eig": float(eR.max()),
                   "R_indefinite": bool(eR.min() < -1e-9 and eR.max() > 1e-9)},
                  f, indent=2)
    print("\n  wrote results/phase_2_weil_harness/harness.json")


if __name__ == "__main__":
    main()
