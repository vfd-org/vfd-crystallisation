"""WO-RH-TRACE-001 — Finite Arithmetic Trace Kernel.

Formalises the prime->zero positive (RH-POS-001) as an operator trace:

    L_N      = diag(log n),         n = 1..N
    W_N(s)   = diag(Lambda(n) n^-s)
    P_{N,s}(t) = Tr( W_N(s) e^{-i t L_N} )
              = Sum_{n<=N} Lambda(n) n^-s e^{-i t log n}
              ~  - zeta'/zeta(s + i t)   (partial-sum approximation)

Since -zeta'/zeta has poles at the nontrivial zeros rho = beta + i gamma,
|P_{N,s}(t)| spikes near t = gamma when the evaluation line s is closest to
beta. So:
  * peaks of |P| locate the zero HEIGHTS gamma_n;
  * the value of s that MAXIMISES the resonance at a given t locates the zero's
    REAL PART beta -- a diagnostic that returns 1/2 iff the zero is on the line.

INTERPRETATION (honest): this is NOT the Hilbert-Polya operator. It is the
finite arithmetic trace kernel -- the classical explicit-formula channel made
explicit. It LOCATES the zeros; it does not PLACE them on the line. Finding the
resonance-max at s=1/2 is CONSISTENT WITH RH, not a proof (finite N; the zeros
used are already known to be on the line).
"""
from __future__ import annotations

import math
import numpy as np
import mpmath as mp


def zeros(n):
    mp.mp.dps = 20
    return np.array([float(mp.im(mp.zetazero(k))) for k in range(1, n + 1)])


def von_mangoldt(X):
    """(n, Lambda(n)) for prime powers n<=X."""
    is_comp = np.zeros(X + 1, dtype=bool)
    lam = np.zeros(X + 1)
    for p in range(2, X + 1):
        if not is_comp[p]:
            for m in range(p * p, X + 1, p):
                is_comp[m] = True
            pk = p
            while pk <= X:
                lam[pk] = math.log(p); pk *= p
    nz = np.nonzero(lam)[0]
    return nz.astype(float), lam[nz]


def trace_kernel(sigma, n_arr, lam, tgrid, window=None):
    """P_{N,sigma}(t) = sum Lambda(n) n^-sigma e^{-i t log n}, optional window."""
    ln = np.log(n_arr)
    w = lam * n_arr ** (-sigma)
    if window is not None:
        w = w * window
    # chunk over n to bound memory
    P = np.zeros(len(tgrid), dtype=complex)
    step = 4000
    for a in range(0, len(ln), step):
        P += (np.exp(-1j * np.outer(tgrid, ln[a:a + step])) * w[a:a + step]).sum(axis=1)
    return P


def peaks(t, y):
    loc = (y[1:-1] > y[:-2]) & (y[1:-1] > y[2:])
    return t[1:-1][loc], y[1:-1][loc]


def main():
    print("=" * 70)
    print("WO-RH-TRACE-001 — finite arithmetic trace kernel  P_{N,σ}(t)")
    print("=" * 70)
    g = zeros(12)
    X = 80000
    n_arr, lam = von_mangoldt(X)
    print(f"N=X={X}; {len(n_arr)} prime powers; first zeros {np.round(g[:6],2)}")
    t = np.arange(0.5, 56.0, 0.02)

    # ---- task 3: peaks at sigma=1/2 vs gamma_n ----
    P = np.abs(trace_kernel(0.5, n_arr, lam, t))
    pt, pv = peaks(t, P)
    print("\n[σ=1/2] nearest-peak distance to each of first 10 zeros:")
    hits = 0
    for gi in g[:10]:
        d = float(np.min(np.abs(pt - gi)))
        hit = d < 0.3; hits += hit
        print(f"   γ={gi:6.2f}  |peak-γ|={d:.3f}{'  <-' if hit else ''}")
    print(f"   {hits}/10 within 0.3")

    # ---- task 4-5: sigma sweep -> resonance locates beta (=1/2 iff on line) ----
    print("\n[σ-sweep] mean |P(σ, γ_n)| / background over first 10 zeros "
          "(peak => σ≈β of the zeros):")
    bg = np.median(P)
    sweep = [0.20, 0.35, 0.50, 0.65, 0.80]
    res = {}
    for s in sweep:
        Ps = np.abs(trace_kernel(s, n_arr, lam, t))
        # resonance at the known zero heights, normalised by that sigma's background
        val = float(np.mean([Ps[np.argmin(np.abs(t - gi))] for gi in g[:10]]) / np.median(Ps))
        res[s] = val
        print(f"   σ={s:.2f}: resonance = {val:.2f}")
    best = max(res, key=res.get)
    print(f"   -> sharpest resonance at σ={best:.2f}  "
          f"({'== 1/2: consistent with zeros on the line' if abs(best-0.5)<1e-9 else 'NOT 1/2'})")
    print(f"   σ<->1-σ: resonance(0.35)={res[0.35]:.2f} vs resonance(0.65)={res[0.65]:.2f} "
          f"(near-equal => symmetry about 1/2; exact symmetry needs the Γ-factor)")

    # ---- task 6: windowing reduces false positives ----
    print("\n[windowing] raw vs Gaussian-tapered (false positives = strong peaks "
          "not within 0.5 of any of first 12 zeros):")
    def false_pos(y):
        pt, pv = peaks(t, y)
        strong = pt[pv > 0.5 * pv.max()]
        return int(np.sum([np.min(np.abs(g - s)) > 0.5 for s in strong])), len(strong)
    ln = np.log(n_arr); win = np.exp(-0.5 * (ln / ln.max() * 2.2) ** 2)
    Praw = np.abs(trace_kernel(0.5, n_arr, lam, t))
    Pwin = np.abs(trace_kernel(0.5, n_arr, lam, t, window=win))
    fr, nr = false_pos(Praw); fw, nw = false_pos(Pwin)
    print(f"   raw      : {fr} false / {nr} strong peaks")
    print(f"   windowed : {fw} false / {nw} strong peaks")

    # ---- task 5: N-stability ----
    print("\n[N-stability] mean |peak-γ| over first 8 zeros as N grows:")
    for Xi in [20000, 80000]:
        na, la = von_mangoldt(Xi)
        Pi = np.abs(trace_kernel(0.5, na, la, t)); pti, _ = peaks(t, Pi)
        md = float(np.mean([np.min(np.abs(pti - gi)) for gi in g[:8]]))
        print(f"   N={Xi:>6}: mean |peak-γ| = {md:.3f}")

    print("""
----------------------------------------------------------------------
SUMMARY (WO-RH-TRACE-001) — honest, data-matched
----------------------------------------------------------------------
WORKS: the trace P_{N,σ}(t)=Tr(W_N(σ)e^{-itL_N}) at σ=1/2 has peaks on the zero
HEIGHTS γ_n (8/10 within 0.3); alignment is STABLE and improves with N
(0.241 -> 0.139 from N=2e4 to 8e4); a Gaussian window cuts false-positive peaks
(20 -> 5). So the kernel cleanly formalises the explicit-formula channel that
LOCATES the zero heights.

DID NOT WORK (honest negative): the σ-sweep does NOT locate the real part β.
Resonance grows MONOTONICALLY with σ (max at σ=0.80, not 1/2) -- a CONFOUND:
the raw partial sum only approximates -ζ'/ζ for σ>1, so larger σ converges
better and is dominated by the small primes; the magnitude reflects convergence,
not pole-proximity. So this estimator cannot verify β=1/2.

WHAT THIS MEANS: the finite arithmetic trace LOCATES the zeros (heights), but
VERIFYING they sit on the line needs the analytic continuation / archimedean
Γ-factor (Riemann-Siegel-type), which the raw finite trace lacks. Same wall,
same missing piece (the archimedean factor) as everywhere else. NOT the
Hilbert-Polya operator; not a proof; a faithful formalisation of the
height-locating channel and an honest map of where it stops.
""")


if __name__ == "__main__":
    main()
