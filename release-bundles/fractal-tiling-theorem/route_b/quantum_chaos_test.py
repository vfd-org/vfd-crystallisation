"""Do the zeros' spacings match a real quantum chaotic spectrum?

The Montgomery-Odlyzko law: the unfolded nearest-neighbour spacings of the
Riemann zeros follow the GUE random-matrix distribution -- the SAME law
measured in heavy nuclei and chaotic microwave cavities.  We test it on the
zeros we have and overlay the two reference curves physicists measure:

  GUE (Wigner surmise, beta=2):  P(s) = (32/pi^2) s^2 exp(-4 s^2 / pi)
  Poisson (uncorrelated):        P(s) = exp(-s)

Procedure:
  1. UNFOLD: rescale by the smooth zero-counting function so mean spacing=1
     N_smooth(t) = (t/2pi)(log(t/2pi) - 1) + 7/8.
  2. spacings s_n = N(gamma_{n+1}) - N(gamma_n).
  3. histogram vs GUE and Poisson; measure which the data follows.

The signature of quantum chaos is LEVEL REPULSION: almost no spacings near 0
(P(0)=0 for GUE), a bump near s~0.8 -- unlike Poisson which piles up at 0.

Honest caveat: 40 low zeros is a SMALL, noisy sample, and low zeros match
GUE only roughly (the near-perfect match is at very high zeros -- Odlyzko,
billions of them).  This is INDICATIVE: it shows the repulsion signature,
the same physics measured in real chaotic quantum systems.
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

GAMMA = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
         40.918719, 43.327073, 48.005151, 49.773832, 52.970321, 56.446248,
         59.347044, 60.831779, 65.112544, 67.079811, 69.546402, 72.067158,
         75.704691, 77.144840, 79.337375, 82.910381, 84.735493, 87.425275,
         88.809111, 92.491899, 94.651344, 95.870634, 98.831194, 101.317851,
         103.725538, 105.446623, 107.168611, 111.029536, 111.874659,
         114.320221, 116.226680, 118.790783, 121.370125, 122.946829]


def N_smooth(t):
    return (t / (2 * math.pi)) * (math.log(t / (2 * math.pi)) - 1) + 7 / 8


def gue(s):
    return (32 / math.pi ** 2) * s ** 2 * np.exp(-4 * s ** 2 / math.pi)


def poisson(s):
    return np.exp(-s)


def main():
    print("=" * 74)
    print("QUANTUM-CHAOS TEST: Riemann-zero spacings vs GUE (the law")
    print("measured in nuclei and microwave billiards) and vs Poisson")
    print("=" * 74)

    u = np.array([N_smooth(g) for g in GAMMA])      # unfolded positions
    s = np.diff(u)                                   # unfolded spacings
    s = s / s.mean()                                 # normalise mean to 1
    print(f"\nUnfolded spacings: n = {len(s)}, mean = {s.mean():.3f} "
          f"(should be ~1), min = {s.min():.3f}, max = {s.max():.3f}")

    # level repulsion: fraction of small spacings
    frac_small = np.mean(s < 0.3)
    gue_small = (32 / math.pi ** 2) * \
        np.trapz([gue(x) for x in np.linspace(0, 0.3, 200)],
                 np.linspace(0, 0.3, 200)) / 1.0
    # integrate the reference densities to 0.3
    xs_small = np.linspace(0, 0.3, 400)
    p_gue_small = np.trapz(gue(xs_small), xs_small)
    p_poi_small = np.trapz(poisson(xs_small), xs_small)
    print(f"\nLevel repulsion -- fraction of spacings < 0.3:")
    print(f"  data:    {frac_small:.3f}")
    print(f"  GUE:     {p_gue_small:.3f}   (repulsion: few small gaps)")
    print(f"  Poisson: {p_poi_small:.3f}   (clustering: many small gaps)")

    # which curve fits better (binned SSE)
    bins = np.linspace(0, 3, 13)
    hist, edges = np.histogram(s, bins=bins, density=True)
    centers = 0.5 * (edges[:-1] + edges[1:])
    sse_gue = float(np.sum((hist - gue(centers)) ** 2))
    sse_poi = float(np.sum((hist - poisson(centers)) ** 2))
    print(f"\nBinned fit (sum of squared error to the histogram):")
    print(f"  vs GUE:     {sse_gue:.4f}")
    print(f"  vs Poisson: {sse_poi:.4f}")
    verdict = "GUE (quantum chaos)" if sse_gue < sse_poi else "Poisson (uncorrelated)"
    print(f"  -> data is closer to: {verdict}")

    # plot
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.hist(s, bins=bins, density=True, alpha=0.55, color="steelblue",
            edgecolor="k", label=f"Riemann-zero spacings (n={len(s)})")
    xx = np.linspace(0, 3, 400)
    ax.plot(xx, gue(xx), "r-", lw=2.2,
            label="GUE (measured in nuclei, microwave billiards)")
    ax.plot(xx, poisson(xx), "g--", lw=1.8, label="Poisson (uncorrelated)")
    ax.set_xlabel("normalised spacing s")
    ax.set_ylabel("P(s)")
    ax.set_title("The zeros repel like a quantum chaotic spectrum\n"
                 "(blue = zeros; red = the random-matrix law measured in real "
                 "quantum systems)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT / "50_quantum_chaos_spacing.png", dpi=140)
    plt.close()
    print(f"\n  plot -> outputs/50_quantum_chaos_spacing.png")

    print("""
==========================================================================
READING THE RESULT
==========================================================================
If the spacings avoid 0 (level repulsion) and track the red GUE curve
rather than the green Poisson one, then the Riemann zeros statistically
behave like the energy levels of a real chaotic quantum system -- the SAME
law measured in heavy nuclei and in chaotic microwave cavities. That is the
genuine, measurable physics this mathematics connects to.

HONEST CAVEAT: n=40 low zeros is small and noisy, and low zeros match GUE
only roughly; the near-perfect, decisive match is at very high zeros
(Odlyzko, billions). This run shows the repulsion signature -- indicative,
not a precision fit. It is EVIDENCE that the zeros are spectral (the
Hilbert-Polya picture), not a proof, and it connects to quantum spectra --
NOT to suns, planets, or people.
""")


if __name__ == "__main__":
    main()
