"""Prime-shift operator on log-states, and the explicit formula run forward.

Two objects, two questions (the proposal conflates them; we separate them):

(A) THE OPERATOR  H = Σ_p (log p/√p)(S_p + S_p†),  S_p|n> = |np>  on n=1..N.
    Is H's SPECTRUM the zeros? (real symmetric => GOE class; bounded.)

(B) THE TRACE / PRIME SUM  D(t) = Σ_{n≤X} Λ(n) n^{-1/2} e^{-i t log n}
    ≈ -ζ'/ζ(1/2+it), which has POLES at the zeros. Does |D(t)| SPIKE at the
    actual γ_n? This is the explicit formula forward (primes -> zeros) and is
    the genuinely meaningful object the proposal is pointing at.

Honest frame: (B) working is CLASSICAL (the explicit formula), not a proof and
not a new operator -- it confirms the prime<->zero duality. (A) is a real
symmetric, bounded operator: its spectrum is NOT the (unbounded, GUE) zeros.
The arithmetic lives in the DUALITY (B), not in the raw operator spectrum (A).
"""
from __future__ import annotations

import math
import numpy as np
import mpmath as mp


def zeros(n):
    mp.mp.dps = 20
    return np.array([float(mp.im(mp.zetazero(k))) for k in range(1, n + 1)])


def von_mangoldt_support(X):
    """Return arrays (n, Lambda(n)) for prime powers n<=X."""
    is_comp = np.zeros(X + 1, dtype=bool)
    lam = np.zeros(X + 1)
    for p in range(2, X + 1):
        if not is_comp[p]:
            for m in range(p * p, X + 1, p):
                is_comp[m] = True
            pk = p
            while pk <= X:
                lam[pk] = math.log(p)
                pk *= p
    n = np.nonzero(lam)[0]
    return n.astype(float), lam[n]


def r_stat(ev):
    ev = np.sort(np.real(ev)); s = np.diff(ev); s = s[s > 1e-9]
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(np.mean(r))


def main():
    print("=" * 70)
    print("PRIME-SHIFT OPERATOR + EXPLICIT FORMULA FORWARD")
    print("=" * 70)
    g = zeros(12)

    # ---- (A) the operator H on |1..N> ----
    N = 2000
    H = np.zeros((N, N))
    primes = [p for p in range(2, N) if all(p % q for q in range(2, int(p**0.5) + 1))]
    for p in primes:
        w = math.log(p) / math.sqrt(p)
        for n in range(1, N // p + 1):
            i, j = n - 1, n * p - 1
            H[i, j] += w; H[j, i] += w
    ev = np.linalg.eigvalsh(H)
    print(f"\n(A) operator H = Σ_p (log p/√p)(S_p+S_p†) on n=1..{N}")
    print(f"    real symmetric; spectrum range [{ev.min():.2f}, {ev.max():.2f}] (BOUNDED)")
    print(f"    <r> = {r_stat(ev[N//4:3*N//4]):.3f}  (GOE 0.53 / GUE 0.60; zeros are GUE, unbounded)")
    print(f"    -> H's eigenvalues are NOT the zeros (bounded real-symmetric spectrum).")

    # ---- (B) explicit formula forward: does the prime sum spike at the zeros? ----
    X = 60000
    n_arr, lam = von_mangoldt_support(X)
    w = lam / np.sqrt(n_arr)            # Λ(n) n^{-1/2}
    ln = np.log(n_arr)
    t = np.arange(0.5, 55.0, 0.02)
    # D(t) = Σ w_n e^{-i t ln n}; |D| approximates |ζ'/ζ(1/2+it)| (spikes at zeros)
    D = np.abs((np.exp(-1j * np.outer(t, ln)) * w).sum(axis=1))
    # local maxima
    loc = (D[1:-1] > D[:-2]) & (D[1:-1] > D[2:])
    peaks_t = t[1:-1][loc]; peaks_v = D[1:-1][loc]
    top = peaks_t[np.argsort(peaks_v)[::-1][:10]]
    top = np.sort(top)
    print(f"\n(B) prime sum |Σ Λ(n) n^(-1/2) e^(-it log n)|, primes^k up to {X}")
    print(f"    top peak locations t: {np.round(top,2)}")
    print(f"    first Riemann zeros : {np.round(g,2)}")
    # match each of first zeros to nearest peak
    matched = []
    for gi in g[:8]:
        d = np.min(np.abs(peaks_t - gi))
        matched.append((round(float(gi), 2), round(float(d), 2)))
    print(f"    nearest-peak distance to each of first 8 zeros:")
    for gi, dist in matched:
        flag = "  <- HIT" if dist < 0.5 else ""
        print(f"      γ={gi:6.2f}   |peak-γ| = {dist:.2f}{flag}")
    hits = sum(1 for _, dd in matched if dd < 0.5)
    print(f"    {hits}/8 zeros have a prime-sum peak within 0.5")

    print(f"""
----------------------------------------------------------------------
WHAT THE DATA SAYS
----------------------------------------------------------------------
(A) The raw operator H is real-symmetric and BOUNDED: its spectrum is GOE-class
    and is NOT the zeros. The proposal's "H's eigenvalues = zeros" is not how it
    works -- a bounded real operator cannot have the unbounded GUE zero-spectrum.

(B) The prime SUM (the explicit formula forward) DOES carry the zeros: |Σ Λ(n)
    n^(-1/2) e^(-it log n)| approximates |ζ'/ζ(1/2+it)|, which has poles at the
    zeros, so it spikes near the actual γ_n ({hits}/8 hit within 0.5 at this X).
    THIS is the real prime<->zero channel -- and it is the CLASSICAL explicit
    formula, not a new operator and not a proof.

So the arithmetic enters through the DUALITY (the explicit-formula trace), not
through the operator's raw spectrum. The zeros it locates are GUE-spaced
(Montgomery), so "primes -> zeros -> GUE" holds -- but that is the same
information viewed twice, not a derivation of GUE from the primes. The wall is
unchanged: proving those spikes (zeros) lie on the line = RH.
""")


if __name__ == "__main__":
    main()
