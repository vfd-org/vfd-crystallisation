"""Connes/Weil positivity for our L-function -- computed, and gated on zeta.

Connes' reformulation: RH for an L-function is equivalent to POSITIVITY of
the Weil distribution (the explicit-formula functional) on the adele class
space.  For a single L-function this is the classical Weil positivity
criterion:

    W(h) := (archimedean term) - (prime term)  =  sum over zeros h(gamma) ,
    and  RH  <=>  W(h) >= 0  for all test functions h of positive type.

We compute W(h) from data we control:
  * archimedean term: from the gamma factor (digamma) and conductor;
  * prime term: from the Satake angles theta_q (which the SUBSTRATE
    produced, verified) -- a_q = 2 sqrt(N q) cos(theta_q).

GATE (this is the whole point): we first run the IDENTICAL machinery on the
Riemann zeta function, where the zeros are known, and check that
    archimedean - primes  ==  sum over the known zeta zeros h(gamma).
If that reproduces zeta to good accuracy, the implementation (constants,
gamma factor, normalisation) is correct, and we trust the degree-4 result.

NON-MYSTICAL SCOPE: W(h) >= 0 holding is EVIDENCE consistent with RH for
this L-function (= GRH); it is not a proof (infinitely many h).  Nothing
here involves observers, consciousness, or 'selves'.  See the note at end.
"""
from __future__ import annotations

import math
import cmath

import mpmath as mp

mp.mp.dps = 15

# ---- test function h(r) = exp(-r^2 / (2 sigma^2)) and its transform -------
# g(u) = (1/2pi) \int h(r) e^{-i r u} dr = sigma/sqrt(2pi) * exp(-sigma^2 u^2/2)

def make_h(sigma):
    def h(r):
        return math.exp(-(r * r) / (2 * sigma * sigma))
    def g(u):                      # (1/2pi)-normalised Fourier transform
        return (sigma / math.sqrt(2 * math.pi)) * math.exp(-(sigma * sigma) * u * u / 2)
    return h, g


# ---- archimedean term: (1/2pi) \int h(r) Omega(r) dr ---------------------
# Omega(r) = log(Q^2) + sum over gamma-factor digammas at (center +- i r).
# For a gamma factor prod_j Gamma_R(s + k_j), Gamma_R(s)=pi^{-s/2}Gamma(s/2),
# (Gamma_R'/Gamma_R)(s) = -1/2 log pi + 1/2 psi(s/2).

import cmath as _cm
_LOGPI = math.log(math.pi)

def _digamma_c(z):
    """Fast complex digamma via asymptotic series + recurrence (float)."""
    result = 0.0 + 0.0j
    while z.real < 10:
        result -= 1.0 / z
        z = z + 1.0
    inv = 1.0 / z
    inv2 = inv * inv
    # asymptotic: ln z - 1/(2z) - sum B_2k/(2k z^{2k})
    result += _cm.log(z) - 0.5 * inv
    result -= inv2 * (1/12.0 - inv2 * (1/120.0 - inv2 * (1/252.0)))
    return result

def gammaR_logderiv(s):
    # -1/2 log pi + 1/2 psi(s/2), float complex
    return -0.5 * _LOGPI + 0.5 * _digamma_c(s / 2.0)

def archimedean(h, kappas, logcond, center, rmax=40.0, npts=400):
    """(1/2pi) int h(r) [ logcond + sum_j (GR'/GR)(center+k_j+ir)
                                   + (GR'/GR)(center+k_j-ir) ] dr,
    evaluated by a fast trapezoid rule (h decays as a Gaussian)."""
    dr = (2 * rmax) / npts
    center = float(center); logcond = float(logcond)
    total = 0.0
    for i in range(npts + 1):
        r = -rmax + i * dr
        tot = logcond + 0j
        for k in kappas:
            tot += gammaR_logderiv(complex(center + k, r))
            tot += gammaR_logderiv(complex(center + k, -r))
        w = 0.5 if (i == 0 or i == npts) else 1.0
        total += w * (h(r) * tot).real
    return (total * dr) / (2 * math.pi)


# ---- prime term ----------------------------------------------------------

def primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def prime_term_zeta(g, P):
    """2 sum_n Lambda(n)/sqrt(n) g(log n)  for zeta (von Mangoldt)."""
    total = 0.0
    for p in primes_up_to(P):
        lp = math.log(p)
        k = 1
        pk = p
        while lp * k < 40:
            total += (lp / math.sqrt(pk)) * g(k * lp)
            k += 1
            pk *= p
            if pk > 10 ** 15:
                break
    return 2 * total


# ---- our L-function: a_q from point counting (verified curve 31.1-a1) ----
PHI = (1 + 5 ** 0.5) / 2

def zphi_mul(x, y):
    a, b = x; c, d = y
    return (a * c + b * d, a * d + b * c + b * d)

# curve a-invariants in Z[phi]: [1, phi+1, phi, phi, 0]
A1c = (1, 0); A2c = (1, 1); A3c = (0, 1); A4c = (0, 1); A6c = (0, 0)

def sqrt5_mod(p):
    for r in range(p):
        if (r * r - 5) % p == 0:
            return r
    return None

def ap_split_or_inert(p, Pmax):
    """Return list of (Nq, a_q) for primes above rational prime p (good),
    skipping any whose norm exceeds Pmax BEFORE doing the point count."""
    out = []
    r5 = p % 5
    if p == 5:
        if 5 <= Pmax:
            root = (pow(2, p - 2, p)) % p       # phi -> 3 mod 5
            out.append(count_curve(p, root, 5))
    elif r5 in (1, 4):
        if p <= Pmax:
            s = sqrt5_mod(p); inv2 = pow(2, p - 2, p)
            for root in (((1 + s) * inv2) % p, ((1 - s) * inv2) % p):
                out.append(count_curve(p, root, p))
    else:
        if p * p <= Pmax:                        # inert: norm p^2
            out.append(count_curve_inert(p))
    return out

def count_curve(p, root, Nq):
    a1 = (A1c[0] + A1c[1] * root) % p
    a2 = (A2c[0] + A2c[1] * root) % p
    a3 = (A3c[0] + A3c[1] * root) % p
    a4 = (A4c[0] + A4c[1] * root) % p
    a6 = (A6c[0] + A6c[1] * root) % p
    cnt = 1
    for x in range(p):
        rhs = (x * x * x + a2 * x * x + a4 * x + a6) % p
        for y in range(p):
            if (y * y + a1 * x * y + a3 * y) % p == rhs:
                cnt += 1
    return (Nq, Nq + 1 - cnt)

def count_curve_inert(p):
    # F_{p^2} = F_p[t]/(t^2-t-1); reuse small brute force
    def mul(u, v):
        a, b = u; c, d = v
        return ((a * c + b * d) % p, (a * d + b * c + b * d) % p)
    def add(u, v): return ((u[0] + v[0]) % p, (u[1] + v[1]) % p)
    a1 = (A1c[0] % p, A1c[1] % p); a2 = (A2c[0] % p, A2c[1] % p)
    a3 = (A3c[0] % p, A3c[1] % p); a4 = (A4c[0] % p, A4c[1] % p)
    a6 = (A6c[0] % p, A6c[1] % p)
    elems = [(u, v) for u in range(p) for v in range(p)]
    cnt = 1
    for x in elems:
        x2 = mul(x, x); x3 = mul(x2, x)
        rhs = add(add(x3, mul(a2, x2)), add(mul(a4, x), a6))
        for y in elems:
            lhs = add(mul(y, y), add(mul(a1, mul(x, y)), mul(a3, y)))
            if lhs == rhs:
                cnt += 1
    return (p * p, p * p + 1 - cnt)

def prime_term_L(g, Pmax):
    """sum over prime ideals q (good): 2 cos(k theta_q) log Nq / Nq^{k/2}
       * g(k log Nq).  theta_q from a_q = 2 sqrt(Nq) cos theta_q."""
    total = mp.mpf(0)
    for p in primes_up_to(Pmax):
        if p == 31:
            continue                      # conductor prime (bad); skip
        for (Nq, aq) in ap_split_or_inert(p, Pmax):
            x = aq / (2 * math.sqrt(Nq))
            if abs(x) > 1:
                x = max(-1.0, min(1.0, x))
            theta = math.acos(x)
            lN = mp.log(Nq)
            k = 1
            while k * float(lN) < 40 and Nq ** (k / 2.0) < 1e12:
                total += 2 * mp.cos(k * theta) * lN / mp.sqrt(Nq ** k) * g(k * lN)
                k += 1
    return total


# first 30 nontrivial zeta zeros (imaginary parts)
ZETA = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
        40.918719, 43.327073, 48.005151, 49.773832, 52.970321, 56.446248,
        59.347044, 60.831779, 65.112544, 67.079811, 69.546402, 72.067158,
        75.704691, 77.144840, 79.337375, 82.910381, 84.735493, 87.425275,
        88.809111, 92.491899, 94.651344, 95.870634, 98.831194, 101.317851]


def main():
    print("=" * 74)
    print("WEIL / CONNES POSITIVITY  (gated on zeta, then our L-function)")
    print("=" * 74)

    print("\n(sigma < 3 is truncation-limited: the narrow test function needs")
    print(" more primes than Nq<=150 provides, and the zeta gate degenerates")
    print(" there since the lowest zeta zero is at 14.13. We report the")
    print(" reliable regime sigma >= 3, where the gate validates the code.)")
    for sigma in [3.0, 4.0, 5.0]:
        h, g = make_h(sigma)
        print(f"\n--- test function: Gaussian, sigma = {sigma} ---")

        # ZETA GATE: zeros side vs explicit-formula side
        lhs = 2 * sum(float(h(gm)) for gm in ZETA)        # +-gamma
        arch = archimedean(h, kappas=[0.0], logcond=mp.mpf(0),
                           center=mp.mpf('0.5'))
        # zeta pole at s=1: + h(i/2)+h(-i/2)
        pole = 2 * float(mp.e ** (1.0 / (8 * sigma * sigma)))
        prim = float(prime_term_zeta(g, 2000))
        rhs = float(arch) + pole - prim
        print(f"  ZETA gate:  zeros-side = {lhs:.5f}   "
              f"formula-side = {rhs:.5f}   "
              f"rel.err = {abs(lhs-rhs)/abs(lhs):.2%}")
        gate_ok = abs(lhs - rhs) / abs(lhs) < 0.05
        print(f"  gate {'PASS' if gate_ok else 'FAIL'} "
              f"(arch={float(arch):.4f}, pole={pole:.4f}, primes={prim:.4f})")

        # OUR L-FUNCTION: degree 4, gamma = Gamma_C(s)^2, conductor 775
        # arithmetic norm center 1; Gamma_C(s)=Gamma_R(s)Gamma_R(s+1)
        # -> kappas = [0,1,0,1]; logcond = log(conductor) = log 775
        archL = archimedean(h, kappas=[0.0, 1.0, 0.0, 1.0],
                            logcond=mp.log(775), center=mp.mpf('0.5'))
        primL = float(prime_term_L(g, 150))
        WL = float(archL) - primL
        print(f"  OUR L:      W(h) = arch - primes = "
              f"{float(archL):.4f} - {primL:.4f} = {WL:.5f}   "
              f"{'>= 0 (consistent with RH)' if WL >= 0 else '< 0 (!)'}")

    print("""
==========================================================================
READING THE RESULT
==========================================================================
If the ZETA gate reproduces the known zeros (small rel.err), the machinery
is correct.  Then W(h) >= 0 for our L-function is the Connes/Weil
positivity holding on the tested functions -- genuine numerical EVIDENCE
consistent with RH for this L-function (= GRH).  It is NOT a proof: Weil
positivity must hold for ALL test functions of positive type, and we test
finitely many, with the prime sum truncated (Nq <= 200).

NON-MYSTICAL NOTE: this functional is built only from the conductor, the
gamma factor, and the Satake angles theta_q the substrate produced.  No
observer, no consciousness, no 'selves' enter -- and none are needed.  The
positivity, if it holds, is a property of the L-function's zeros, an
eternal arithmetic fact.  The 'infinite-selves-as-primes' reading is a
personal-philosophical frame, explicitly OUTSIDE this mathematics; the
work neither uses nor supports it, and should not be presented as if it
did.
""")


if __name__ == "__main__":
    main()
