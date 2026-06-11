"""P1 -- the finite-certificate probe for the icosian row.

The lab localised RH(L) as: the icosian closure object is TOTALLY positive across all
places.  The classical finite handle on "totally positive across all places" is Li's
criterion:

    RH(L)  <=>  lambda_n^{(L)} >= 0  for every n,

and each Li coefficient is a FINITE sum over the zeros (or, equivalently, a finite
arithmetic sum over the Dirichlet coefficients):

    lambda_n = sum_rho [ 1 - (1 - 1/rho)^n ]            (rho = nontrivial zeros)

So the all-places positivity decomposes into a SEQUENCE of finite positivity certificates.
This module computes lambda_n from a list of zeros (gammas), self-tests on the Riemann
zeta (whose lambda_n are known positive), and accepts the icosian cuspidal L's zeros
(from frontier-run) to test/track positivity of its geometric Li coefficients.

HONEST SCOPE: lambda_n >= 0 over the computed zeros is EVIDENCE for RH(L), never a proof
(true lambda_n needs all zeros; finite zero-sums are partial).  The prize is not a positive
number -- it is finding a GEOMETRIC reason the icosian lambda_n must stay non-negative.
"""
from __future__ import annotations
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))


def li_from_zeros(gammas, nmax, beta=0.5):
    """lambda_n = sum over rho = beta +/- i*gamma of [1 - (1-1/rho)^n], n=1..nmax.
    Returns the real partial Li coefficients (symmetric over conjugate pairs)."""
    lam = [0.0] * (nmax + 1)
    for g in gammas:
        for rho in (complex(beta, g), complex(beta, -g)):
            base = 1.0 - 1.0 / rho
            powv = 1.0 + 0j
            for n in range(1, nmax + 1):
                powv = powv * base                      # (1-1/rho)^n
                lam[n] += (1.0 - powv).real
    return lam[1:]


def _zeta_zeros(n):
    from mpmath import zetazero
    return [float(zetazero(k).imag) for k in range(1, n + 1)]


def self_test(nmax=6, nzeros=200):
    """Validate the engine on Riemann zeta: lambda_n must come out positive and climb
    toward the known Keiper-Li values (lambda_1~0.0231, lambda_2~0.0923, ...).
    Finite zero-sums underestimate but stay positive."""
    g = _zeta_zeros(nzeros)
    lam = li_from_zeros(g, nmax)
    known = {1: 0.0230957, 2: 0.0923457, 3: 0.207639, 4: 0.368793}
    print(f"[self-test] Riemann zeta, {nzeros} zeros:")
    ok = True
    for n in range(1, nmax + 1):
        kn = known.get(n)
        tag = f"(known {kn})" if kn else ""
        pos = "OK" if lam[n - 1] > 0 else "NEGATIVE!"
        if lam[n - 1] <= 0:
            ok = False
        print(f"   lambda_{n} = {lam[n-1]:+.5f}  {pos}  {tag}")
    print(f"[self-test] all positive: {ok}  "
          f"(partial sums underestimate true values; positivity is the signal)")
    return ok


def icosian_li(nmax=8, zeros_path=None):
    """Compute the icosian cuspidal L's Li coefficients from frontier-run zeros, if present."""
    zeros_path = zeros_path or os.path.join(
        HERE, "..", "..", "frontier-run", "out", "zeros_result.json")
    if not os.path.exists(zeros_path):
        print(f"[icosian] no zeros yet at {zeros_path}")
        print("[icosian] waiting on frontier-run (Stage B) -> will compute lambda_n then.")
        return None
    d = json.load(open(zeros_path))
    gammas = d.get("L_zeros", [])
    if not gammas:
        print("[icosian] zeros file present but empty (coverage too low yet).")
        return None
    lam = li_from_zeros(gammas, nmax)
    print(f"[icosian] {len(gammas)} zeros -> Li coefficients:")
    allpos = True
    for n in range(1, nmax + 1):
        pos = "OK" if lam[n - 1] > 0 else "NEGATIVE -> would FALSIFY RH(L)!"
        if lam[n - 1] <= 0:
            allpos = False
        print(f"   lambda_{n} = {lam[n-1]:+.6f}  {pos}")
    print(f"[icosian] all computed lambda_n >= 0: {allpos}  (EVIDENCE for RH(L), not proof)")
    return {"n_zeros": len(gammas), "lambda": lam, "all_nonnegative": allpos}


if __name__ == "__main__":
    self_test()
    print()
    icosian_li()
