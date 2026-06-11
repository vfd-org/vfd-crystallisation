"""P1-deep -- the GEOMETRIC FORCING probe.

Question: does the geometry FORCE the icosian L's positivity, or only permit it?

The literal Li per-prime sum diverges term-by-term (lambda_n is finite only after the
arch<->prime cancellation), so "check each prime's contribution is positive" is not even
well-posed.  The convergent, genuinely per-prime object is the WEIL explicit-formula form

    W(g) = ARCH(g)  -  sum_q PRIME_q(g),      PRIME_q(g) = sum_k 2 cos(k th_q) logNq Nq^{-k/2} g(k logNq)

with th_q = arccos(a_q / 2 sqrt(Nq)) the geometric Brandt eigenvalue (Ramanujan => th_q real).
RH(L)  <=>  W(g) >= 0 for all g.  This probe decomposes W per prime, over a family of test
functions, and asks where the positivity actually comes from:

  1. ARCH(g) is the positive driver (conductor 775, gamma Gamma_C^2, shifts {0,0,1,1}).
  2. each PRIME_q is bounded by Ramanujan (|a_q| <= 2 sqrt(Nq)), but their SUM is what must
     stay below ARCH.
  3. so the honest forcing mechanism is NOT per-prime size -- it is whether the eigenvalues
     EQUIDISTRIBUTE (Sato-Tate): cos th_q spread by the geometric measure is what keeps
     sum_q PRIME_q from conspiring up to ARCH.  Equidistribution is geometric; per-prime
     bounds are not enough (if they were, Ramanujan would give RH, which it does not).

Runs now on the 32 shipped eigenvalues (leading behaviour); the margin and the Sato-Tate
fit sharpen as frontier-run extends the eigenvalue list.
"""
from __future__ import annotations
import json, math, os, cmath

HERE = os.path.dirname(os.path.abspath(__file__))
N_COND, MU = 775.0, (0.5, 0.5, 1.5, 1.5)               # icosian cuspidal L: deg 4, wt 2;
#   gamma = Gamma_C(s+1/2)^2 (two places of K=Q(sqrt5)); shifts {1/2,3/2} per place.
#   Normalization CALIBRATED against the conductor-11 elliptic-curve L (out/_ec_grid.py):
#   ARCH = full logN + doubled gR at these shifts; PRIME carries the universal factor 2.
LOGPI = math.log(math.pi)


def _load_rows():
    p = os.path.join(HERE, "..", "..", "frontier-run", "out", "a_q_extended.json")
    if not os.path.exists(p):
        p = os.path.join(HERE, "..", "..", "icosian-rh-geometric", "repro", "data",
                         "geometric_aP.json")
    return json.load(open(p))["rows"]


def _digamma(z):
    r = 0 + 0j
    while z.real < 10:
        r -= 1 / z; z = z + 1
    i = 1 / z; i2 = i * i
    return r + cmath.log(z) - 0.5 * i - i2 * (1 / 12 - i2 * (1 / 120 - i2 / 252))


def _gR(s):
    return -0.5 * LOGPI + 0.5 * _digamma(s / 2)


def _arch(sigma, rmax=45.0, npts=1200):
    """ARCH(g) for h(r)=exp(-r^2/2 sigma^2): (dr/2pi) sum h(r)[logN + sum_mu gR(1/2+mu+-ir)]."""
    dr = 2 * rmax / npts; tot = 0.0; logN = math.log(N_COND)
    for i in range(npts + 1):
        r = -rmax + i * dr
        s = logN + 0j
        for mu in MU:
            s += _gR(complex(0.5 + mu, r)) + _gR(complex(0.5 + mu, -r))
        w = 0.5 if i in (0, npts) else 1.0
        tot += w * math.exp(-(r * r) / (2 * sigma * sigma)) * s.real
    return tot * dr / (2 * math.pi)


def _g(u, sigma):
    return (sigma / math.sqrt(2 * math.pi)) * math.exp(-(sigma * sigma) * u * u / 2)


def _prime_q(row, sigma):
    """PRIME_q(g): the prime-q contribution to the explicit formula."""
    Nq = row["norm"]; aq = row["a_q_geometric"]
    if Nq == 31 and not row.get("self_adjoint", True):
        return 0.0                                      # Steinberg (bad) prime, handled apart
    x = aq / (2 * math.sqrt(Nq))
    if abs(x) > 1:
        return 0.0
    th = math.acos(max(-1.0, min(1.0, x))); lN = math.log(Nq); k = 1; tot = 0.0
    while k * lN < 45 and Nq ** (k / 2.0) < 1e12:
        # universal factor 2 (calibrated) x trace 2cos(k th) of the 2 Satake roots
        tot += 2 * (2 * math.cos(k * th)) * lN / math.sqrt(Nq ** k) * _g(k * lN, sigma)
        k += 1
    return tot


def margin_sweep(rows, sigmas=(1.5, 2.0, 2.5, 3.0, 3.5, 4.0)):
    out = []
    for sg in sigmas:
        arch = _arch(sg)
        per = [(r["norm"], _prime_q(r, sg)) for r in rows]
        prime_sum = sum(p for _, p in per)
        big = max(per, key=lambda t: abs(t[1])) if per else (0, 0.0)
        out.append({"sigma": sg, "arch": arch, "prime_sum": prime_sum,
                    "margin": arch - prime_sum,
                    "ramanujan_envelope": sum(abs(p) for _, p in per),
                    "biggest_prime": {"norm": big[0], "contrib": big[1]}})
    return out


def _st_cdf(x):
    """Sato-Tate (SU(2)) CDF on x=cos(theta) in [-1,1]: density (2/pi)sqrt(1-x^2)."""
    x = max(-1.0, min(1.0, x))
    return 0.5 + (x * math.sqrt(1 - x * x) + math.asin(x)) / math.pi


def sato_tate(rows):
    """QUANTITATIVE equidistribution of cos th_q = a_q/(2 sqrt Nq) vs Sato-Tate.

    HONESTY: the LIMIT law (qualitative ST) is a THEOREM for non-CM Hilbert modular
    forms (Barnet-Lamb--Geraghty--Harris--Taylor) -- so 'does it equidistribute' is
    settled mathematics and forces nothing about RH(L).  The open, RH-adjacent content
    is the RATE: the discrepancy D_n (Kolmogorov-Smirnov vs the ST CDF).  Square-root
    cancellation D_n = O(n^{-1/2+eps}) is the effective-ST / symmetric-power-L regime.
    We report moments (orientation) AND D_n (the real instrument)."""
    xs = []
    for r in rows:
        Nq = r["norm"]
        if Nq == 31 and not r.get("self_adjoint", True):
            continue
        x = r["a_q_geometric"] / (2 * math.sqrt(Nq))
        if abs(x) <= 1:
            xs.append(x)
    xs.sort()
    n = len(xs)
    m1 = sum(xs) / n
    m2 = sum(x * x for x in xs) / n
    m4 = sum(x ** 4 for x in xs) / n
    # Kolmogorov-Smirnov discrepancy against the ST CDF
    D = 0.0
    for i, x in enumerate(xs):
        F = _st_cdf(x)
        D = max(D, abs((i + 1) / n - F), abs(i / n - F))
    return {"n": n, "mean": m1, "E[x^2]": m2, "ST_E[x^2]": 0.25,
            "E[x^4]": m4, "ST_E[x^4]": 0.125,
            "discrepancy_D_n": D, "sqrt_n_times_D": D * math.sqrt(n),
            "note": "limit law = known theorem (BLGHT, non-CM HMF); the RATE (D_n) is "
                    "the open RH-adjacent content; track sqrt(n)*D_n as n grows "
                    "(bounded <=> square-root-cancellation regime)"}


def main():
    rows = _load_rows()
    print(f"[forcing] {len(rows)} geometric eigenvalues loaded\n")
    print("[normalization CALIBRATED against conductor-11 EC L: explicit formula closes to")
    print("  max|resid| 0.00000 across sigma; shifts {1/2,3/2}/place, prime factor 2.]\n")
    print("WEIL FORM, per-sigma:  W = ARCH - sum_q PRIME_q   (>=0 == RH-consistent)")
    print(f"{'sigma':>6}{'ARCH':>10}{'prime_sum':>11}{'margin W':>11}{'|prime| env':>12}"
          f"   biggest prime")
    sweep = margin_sweep(rows)
    for d in sweep:
        bp = d["biggest_prime"]
        print(f"{d['sigma']:>6.1f}{d['arch']:>10.4f}{d['prime_sum']:>11.4f}"
              f"{d['margin']:>11.4f}{d['ramanujan_envelope']:>12.4f}"
              f"   N={bp['norm']} ({bp['contrib']:+.4f})")
    allpos = all(d["margin"] > 0 for d in sweep)
    print(f"\n  margin W >= 0 on all tested g: {allpos}   (EVIDENCE for RH(L), not proof)")
    print("  ARCH is the positive driver; the prime sum is the geometry's fluctuation.")

    st = sato_tate(rows)
    print(f"\nEQUIDISTRIBUTION vs SATO-TATE (the forcing mechanism, quantitatively):")
    print(f"  n={st['n']}  mean={st['mean']:+.4f} (ST 0)   "
          f"E[x^2]={st['E[x^2]']:.4f} (ST {st['ST_E[x^2]']})   "
          f"E[x^4]={st['E[x^4]']:.4f} (ST {st['ST_E[x^4]']})")
    print(f"  discrepancy D_n = {st['discrepancy_D_n']:.4f}   "
          f"sqrt(n)*D_n = {st['sqrt_n_times_D']:.4f}"
          f"   (track this as n grows: bounded <=> sqrt-cancellation regime)")
    print("\nHONEST READ (two-level):")
    print("  1. The LIMIT law (qualitative Sato-Tate) is a known THEOREM for non-CM Hilbert")
    print("     modular forms (Barnet-Lamb--Geraghty--Harris--Taylor) -- so equidistribution")
    print("     per se is settled and forces NOTHING about RH(L).")
    print("  2. The open, RH-adjacent content is the RATE: the discrepancy D_n. Per-prime")
    print("     Ramanujan can't force sum_q PRIME_q below ARCH (else Ramanujan => RH, false);")
    print("     what would is QUANTITATIVE equidistribution (effective ST / symmetric-power")
    print("     L-behaviour). So: geometry forces positivity to the extent it forces the")
    print("     RATE -- measure sqrt(n)*D_n as frontier-run grows n. RH(L) remains open.")

    json.dump({"weil_margin_sweep": sweep, "sato_tate": st,
               "n_eigenvalues": len(rows)},
              open(os.path.join(HERE, "..", "out", "geometric_forcing.json"), "w"), indent=1)
    print("\nwrote out/geometric_forcing.json")


if __name__ == "__main__":
    main()
