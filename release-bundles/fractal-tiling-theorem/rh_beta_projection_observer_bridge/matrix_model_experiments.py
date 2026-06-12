"""WO-RH-BETA-PROJECTION-OBSERVER-BRIDGE-001 -- Phase 1 baseline + zeta zeros.

Build a spacing-statistics harness that DISTINGUISHES the three Dyson classes
(beta=1 GOE, beta=2 GUE, beta=4 GSE) and the Riemann zeta zeros, so that later
phases can make honest beta-class claims.

Method: nearest-neighbour spacing distribution (NNSD) after unfolding to mean
spacing 1, compared to the Wigner surmises
    beta=1: p(s) = (pi/2) s exp(-pi s^2/4)
    beta=2: p(s) = (32/pi^2) s^2 exp(-4 s^2/pi)
    beta=4: p(s) = (2^18/(3^6 pi^3)) s^4 exp(-64 s^2/(9 pi))
by L1 histogram distance, plus the level-repulsion exponent (small-s slope).

Zeta zeros (validation only): the high zeros are GUE/beta=2 (Montgomery-Odlyzko).
"""
from __future__ import annotations

import json
import math
import os

import numpy as np

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "results", "beta_baseline")
TAB = os.path.join(HERE, "results", "tables")


def wigner(s, beta):
    if beta == 1:
        return (math.pi / 2) * s * np.exp(-math.pi * s * s / 4)
    if beta == 2:
        return (32 / math.pi ** 2) * s * s * np.exp(-4 * s * s / math.pi)
    if beta == 4:
        return (2 ** 18 / (3 ** 6 * math.pi ** 3)) * s ** 4 * \
            np.exp(-64 * s * s / (9 * math.pi))
    raise ValueError


# ---- ensembles ------------------------------------------------------------
def goe(n, rng):
    A = rng.standard_normal((n, n))
    return (A + A.T) / math.sqrt(2)


def gue(n, rng):
    A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    return (A + A.conj().T) / math.sqrt(2)


def gse(n, rng):
    """2n x 2n quaternion self-dual Hermitian (Kramers-degenerate)."""
    # quaternion entries q = a + b i + c j + d k -> 2x2 complex block
    def qblock(a, b, c, d):
        return np.array([[a + 1j * b, c + 1j * d],
                         [-c + 1j * d, a - 1j * b]])
    H = np.zeros((2 * n, 2 * n), dtype=complex)
    for i in range(n):
        for j in range(i, n):
            if i == j:
                a = rng.standard_normal()
                H[2 * i:2 * i + 2, 2 * i:2 * i + 2] = qblock(a, 0, 0, 0)
            else:
                a, b, c, d = rng.standard_normal(4) / math.sqrt(2)
                B = qblock(a, b, c, d)
                H[2 * i:2 * i + 2, 2 * j:2 * j + 2] = B
                H[2 * j:2 * j + 2, 2 * i:2 * i + 2] = B.conj().T
    return H


def eigs_real(H):
    if np.iscomplexobj(H):
        return np.sort(np.linalg.eigvalsh(H))
    return np.sort(np.linalg.eigvalsh(H))


def unfold_spacings(ev, drop_degenerate=False):
    """Unfold eigenvalues to mean spacing 1 (polynomial fit of the staircase),
    return the nearest-neighbour spacings."""
    ev = np.sort(np.real(ev))
    if drop_degenerate:
        # collapse Kramers pairs: keep every other distinct level
        uniq = [ev[0]]
        for x in ev[1:]:
            if abs(x - uniq[-1]) > 1e-6:
                uniq.append(x)
        ev = np.array(uniq)
    n = len(ev)
    idx = np.arange(n)
    # smooth staircase via polynomial fit of the cumulative count
    coef = np.polyfit(ev, idx, min(7, n - 1))
    unf = np.polyval(coef, ev)
    s = np.diff(unf)
    s = s[s > 0]
    return s / s.mean()


def nnsd_distance(spacings, beta, nbins=40, smax=4.0):
    hist, edges = np.histogram(spacings, bins=nbins, range=(0, smax),
                               density=True)
    centers = 0.5 * (edges[:-1] + edges[1:])
    model = wigner(centers, beta)
    return float(np.mean(np.abs(hist - model)) * smax)


def classify(spacings):
    d = {b: nnsd_distance(spacings, b) for b in (1, 2, 4)}
    best = min(d, key=d.get)
    return best, d


def repulsion_exponent(spacings):
    """small-s slope: p(s) ~ s^beta near 0 -> log-log slope estimate."""
    small = spacings[spacings < 0.6]
    if len(small) < 20:
        return None
    hist, edges = np.histogram(small, bins=8, range=(0, 0.6), density=True)
    c = 0.5 * (edges[:-1] + edges[1:])
    m = hist > 0
    if m.sum() < 3:
        return None
    slope = np.polyfit(np.log(c[m]), np.log(hist[m]), 1)[0]
    return float(slope)


def zeta_zero_spacings(n=300):
    import mpmath as mp
    g = np.array([float(mp.im(mp.zetazero(k))) for k in range(1, n + 1)])
    # unfold by the Riemann-von Mangoldt density N(T) ~ (T/2pi) log(T/2pi e)
    def Nbar(T):
        return T / (2 * math.pi) * np.log(T / (2 * math.pi)) - \
            T / (2 * math.pi) + 7.0 / 8.0
    unf = Nbar(g)
    s = np.diff(unf)
    return s / s.mean()


def main():
    rng = np.random.RandomState(1)
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(TAB, exist_ok=True)
    print("=" * 74)
    print("Phase 1 -- beta baseline: can the harness tell GOE/GUE/GSE/zeta apart?")
    print("=" * 74)
    report = {}
    # ensembles
    runs = {
        "GOE_beta1": lambda: np.concatenate([unfold_spacings(eigs_real(goe(200, rng)))
                                             for _ in range(15)]),
        "GUE_beta2": lambda: np.concatenate([unfold_spacings(eigs_real(gue(200, rng)))
                                             for _ in range(15)]),
        "GSE_beta4": lambda: np.concatenate([unfold_spacings(eigs_real(gse(120, rng)),
                                             drop_degenerate=True)
                                             for _ in range(15)]),
    }
    for name, fn in runs.items():
        s = fn()
        best, dists = classify(s)
        slope = repulsion_exponent(s)
        report[name] = {"best_fit_beta": best,
                        "distances": {str(k): round(v, 4) for k, v in dists.items()},
                        "repulsion_exponent": round(slope, 2) if slope else None}
        print("  %-10s  best-fit beta=%d  dists=%s  repulsion s^%.2f"
              % (name, best, report[name]["distances"],
                 slope if slope else float("nan")))
    # zeta zeros
    print("\n  computing zeta-zero spacings (mpmath.zetazero, 300 zeros)...")
    sz = zeta_zero_spacings(300)
    bestz, dz = classify(sz)
    slopez = repulsion_exponent(sz)
    report["zeta_zeros"] = {"best_fit_beta": bestz,
                            "distances": {str(k): round(v, 4) for k, v in dz.items()},
                            "repulsion_exponent": round(slopez, 2) if slopez else None}
    print("  %-10s  best-fit beta=%d  dists=%s  repulsion s^%.2f"
          % ("zeta", bestz, report["zeta_zeros"]["distances"],
             slopez if slopez else float("nan")))

    harness_ok = (report["GOE_beta1"]["best_fit_beta"] == 1 and
                  report["GUE_beta2"]["best_fit_beta"] == 2 and
                  report["GSE_beta4"]["best_fit_beta"] == 4)
    report["harness_distinguishes_classes"] = harness_ok
    report["zeta_is_beta2"] = (bestz == 2)
    print("\n  harness distinguishes GOE/GUE/GSE:", harness_ok)
    print("  zeta zeros classified as beta=2 (GUE):", bestz == 2)
    with open(os.path.join(OUT, "beta_baseline.json"), "w") as f:
        json.dump(report, f, indent=2)
    print("  wrote results/beta_baseline/beta_baseline.json")


if __name__ == "__main__":
    main()
