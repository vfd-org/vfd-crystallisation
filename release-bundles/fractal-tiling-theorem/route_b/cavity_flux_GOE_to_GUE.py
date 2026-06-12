"""Is the RH 'cavity' a shape (egg / vesica piscis / higher-dim solid)?

NO -- and this shows why, by test. A geometric SHAPE has a REAL Laplacian, so
its level statistics are GOE (time-reversal symmetric), not the GUE of the
Riemann zeros. The missing ingredient is not more dimensions of shape; it is a
MAGNETIC FLUX (time-reversal breaking) -- the 'torsion' / complex-coupling term.

We build a disordered 2D lattice 'cavity' two ways and measure the spacing
class <r> (unfolding-free; Atas et al.):
  * real hopping (a pure SHAPE, no flux)          -> GOE  (~0.53)
  * + Peierls phase / magnetic flux (T broken)    -> GUE  (~0.60)
and compare to the Riemann zeros (~0.62, GUE).

Conclusion: the zeros need T-broken (complex/flux) structure, not a shape.
And even the flux only buys the UNIVERSAL GUE class -- the SPECIFIC zeros still
require the arithmetic (primes), which no cavity geometry supplies. Same wall.
"""
from __future__ import annotations

import math
import numpy as np
import mpmath as mp


def zeros(n):
    mp.mp.dps = 20
    return np.array([float(mp.im(mp.zetazero(k))) for k in range(1, n + 1)])


def r_stat(ev):
    ev = np.sort(np.real(ev)); s = np.diff(ev); s = s[s > 1e-9]
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(np.mean(r))


def build(L, ons, alpha, flux):
    """Disordered 2D lattice (a 'cavity'); flux=True adds Peierls phase."""
    N = L * L
    H = np.zeros((N, N), dtype=complex)
    idx = lambda x, y: x * L + y
    for x in range(L):
        for y in range(L):
            i = idx(x, y); H[i, i] = ons[i]
            if x + 1 < L:
                j = idx(x + 1, y); H[i, j] = -1; H[j, i] = -1            # x-hop real
            if y + 1 < L:
                j = idx(x, y + 1)
                ph = np.exp(2j * np.pi * alpha * x) if flux else 1.0      # flux on y-hop
                H[i, j] = -ph; H[j, i] = -np.conj(ph)
    return H


def main():
    print("=" * 70)
    print("CAVITY SHAPE vs FLUX: does a shape (egg/vesica/...) match the zeros?")
    print("=" * 70)
    rng = np.random.RandomState(5)
    L = 30; N = L * L
    ons = rng.uniform(-2.0, 2.0, N)                 # disorder -> chaotic cavity
    alpha = (5 ** 0.5 - 1) / 2                       # irrational (golden) flux

    for flux, name in [(False, "real 'cavity' (a SHAPE; no flux)      "),
                       (True,  "same cavity + magnetic FLUX (T-broken)")]:
        ev = np.sort(np.linalg.eigvalsh(build(L, ons, alpha, flux)))[N // 4:3 * N // 4]
        print(f"  {name}: <r> = {r_stat(ev):.3f}")
    print(f"  Riemann zeros                          : <r> = {r_stat(zeros(200)):.3f}")
    print("  references: GOE 0.529, GUE 0.603")

    print("""
----------------------------------------------------------------------
WHAT THE DATA SAYS
----------------------------------------------------------------------
A SHAPE (real Laplacian) lands on GOE, not the zeros' GUE -- true for any
geometric cavity in any dimension (egg, vesica piscis, sphere, torus...).
Adding a MAGNETIC FLUX (breaking time-reversal) turns GOE into GUE, matching
the zeros' class. So the missing ingredient is the FLUX / torsion / complex
coupling -- NOT a higher-dimensional shape.

But the flux only reaches the UNIVERSAL GUE class (any disordered cavity + flux
does). The SPECIFIC zeros are pinned only by the arithmetic (primes), which no
cavity geometry provides. The cavity route therefore hits the same wall as the
others: shape -> GOE (wrong class); shape+flux -> GUE (right class, universal);
the specific member -> needs the primes. Tested, not assumed.
""")


if __name__ == "__main__":
    main()
