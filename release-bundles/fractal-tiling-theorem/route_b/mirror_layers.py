"""Modelling the mirror: the zeros are frequency layers; the primes are
the tune. And what happens if you tune a zero off the line.

The prime<->zero 'mirror' is the explicit formula. In one direction it
reads (Riemann/von Mangoldt):

    psi(x) = x - sum_rho x^rho / rho - log(2pi) - (1/2) log(1 - x^-2)

where psi(x) = sum_{p^k <= x} log p is the prime staircase, and the sum is
over the non-trivial zeros rho = 1/2 +- i gamma. EACH ZERO IS ONE FREQUENCY
LAYER: pairing rho with its conjugate,

    x^rho/rho + c.c. = 2 sqrt(x) [ (1/2) cos(gamma L) + gamma sin(gamma L) ]
                                  / (1/4 + gamma^2),     L = ln x.

So the staircase of the primes is literally a superposition of waves, one
per zero, of frequency gamma. The mirror IS layered as frequency components.

This script:
  (A) reconstructs psi(x) from the first N zeros, layer by layer, and shows
      the prime steps emerging as layers are added (the mirror, frequency
      by frequency);
  (B) TUNES a zero off the critical line (Re = 1/2 + beta) and shows the
      reconstruction error grows like x^{1/2+beta} -- i.e. RH is exactly the
      condition that keeps the prime fluctuation minimal (sqrt(x)). This is
      what the mirror looks like when distorted.

Honest status: (A) is the explicit formula (a theorem) made visual; it
CONFIRMS the layered duality but does NOT prove RH -- the reconstruction
uses the actual zeros wherever they are. (B) shows WHY on-line matters
(minimal error), not that the zeros are on the line. Kind-1 texture.
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


def psi_actual(x):
    """Chebyshev psi(x) = sum_{p^k <= x} log p."""
    total = 0.0
    n = int(math.floor(x))
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            for m in range(p * p, n + 1, p):
                sieve[m] = False
            pk = p
            while pk <= x:
                total += math.log(p)
                pk *= p
    return total


def psi_recon(x, gammas, betas=None):
    """psi reconstructed from zeros 1/2+beta_n + i gamma_n.
    betas=None means all on the line (beta=0)."""
    L = math.log(x)
    if betas is None:
        betas = [0.0] * len(gammas)
    s = 0.0
    for g, b in zip(gammas, betas):
        re = 0.5 + b
        # x^rho/rho + c.c., rho = re + i g
        # = 2 Re( x^{re} e^{i g L} / (re + i g) )
        num_r = (x ** re) * math.cos(g * L)
        num_i = (x ** re) * math.sin(g * L)
        den_r, den_i = re, g
        d2 = den_r * den_r + den_i * den_i
        # (num)/(den) real part:
        re_term = (num_r * den_r + num_i * den_i) / d2
        s += 2 * re_term
    return x - s - math.log(2 * math.pi) - 0.5 * math.log(1 - x ** -2)


def main():
    print("=" * 74)
    print("THE MIRROR AS FREQUENCY LAYERS: zeros -> primes (and off-line)")
    print("=" * 74)

    xs = np.linspace(2.0, 30.0, 1400)
    psi_true = np.array([psi_actual(x) for x in xs])

    # (A) layered reconstruction
    layers = [1, 5, 10, 40]
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.plot(xs, psi_true, "k-", lw=2.2, label="actual prime staircase ψ(x)")
    for N in layers:
        rec = np.array([psi_recon(x, GAMMA[:N]) for x in xs])
        ax.plot(xs, rec, lw=1.0, alpha=0.85,
                label=f"{N} zero-frequency layer{'s' if N>1 else ''}")
    ax.set_xlabel("x")
    ax.set_ylabel("ψ(x)")
    ax.set_title("The mirror is frequency-layered: the prime staircase\n"
                 "reconstructed as a superposition of zero-harmonics "
                 "(the 'music of the primes')")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT / "40_mirror_layers.png", dpi=140)
    plt.close()

    # convergence: RMS error vs number of layers
    errs = []
    for N in range(1, len(GAMMA) + 1):
        rec = np.array([psi_recon(x, GAMMA[:N]) for x in xs])
        errs.append(float(np.sqrt(np.mean((rec - psi_true) ** 2))))
    print("\n[A] Layered reconstruction (zeros = frequency components):")
    for N in [1, 5, 10, 20, 40]:
        print(f"  {N:>2} layers: RMS error vs true ψ(x) = {errs[N-1]:.3f}")
    print("  -> more zero-frequencies => sharper prime steps. The mirror is")
    print("     literally a sum of frequency layers, one per zero.")

    # (B) tune one zero off the line
    print("\n[B] Tuning the first zero OFF the critical line (Re = 1/2 + beta):")
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.plot(xs, psi_true, "k-", lw=2.2, label="actual ψ(x)")
    for beta in [0.0, 0.2, 0.4]:
        betas = [beta] + [0.0] * (len(GAMMA) - 1)
        rec = np.array([psi_recon(x, GAMMA, betas) for x in xs])
        err = float(np.sqrt(np.mean((rec - psi_true) ** 2)))
        ax.plot(xs, rec, lw=1.1, alpha=0.85,
                label=f"first zero at Re=1/2+{beta}  (RMS err {err:.2f})")
        print(f"  beta={beta}: reconstruction RMS error = {err:.3f}"
              + ("  (on line: minimal)" if beta == 0 else
                 "  (off line: error grows ~ x^{1/2+beta})"))
    ax.set_xlabel("x")
    ax.set_ylabel("ψ(x)")
    ax.set_title("Tuning a zero off the line distorts the mirror:\n"
                 "the prime fluctuation grows like x^(1/2+β). RH = the "
                 "on-line condition that keeps it minimal (√x).")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT / "41_mirror_offline.png", dpi=140)
    plt.close()

    print("""
==========================================================================
WHAT THE MIRROR LOOKS LIKE
==========================================================================
(A) The prime<->zero mirror IS layered as frequency components: each zero
    is one harmonic of frequency gamma, and the prime staircase is their
    superposition (the explicit formula). Adding layers sharpens the primes.
    Plots: outputs/40_mirror_layers.png.

(B) The mirror is NOT a flat reflection -- it is frequency-graded by Re(rho):
    a zero on the line contributes amplitude ~ sqrt(x); a zero at
    Re=1/2+beta contributes ~ x^{1/2+beta}, distorting the reconstruction.
    RH is exactly the statement that every layer has the SAME amplitude
    scale sqrt(x) -- the mirror is 'balanced', all harmonics at one depth.
    Off-line zeros are louder layers that would unbalance it.
    Plots: outputs/41_mirror_offline.png.

HONEST STATUS: this is the explicit formula (a theorem) made visual. It
shows the mirror's layered, frequency-graded structure and shows why RH is
the balance condition. It does NOT prove RH: (A) uses the actual zeros
wherever they are; (B) shows the consequence of off-line zeros, not that
none exist. Kind-1 texture -- structure revealed, not proved.

LAYERS-OF-REALITY note: the 'layers' here are precise mathematical
frequency components (one per zero). Reading them as 'layers of reality'
is interpretation, outside the mathematics; the math asserts only the
frequency decomposition, nothing about reality's strata.
""")


if __name__ == "__main__":
    main()
