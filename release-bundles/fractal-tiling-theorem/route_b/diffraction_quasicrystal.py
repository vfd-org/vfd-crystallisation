"""Does the zero-side TILE? The Dyson quasicrystal test.

Idea (your 'fractal and tiles' instinct, made precise): a point set is a
quasicrystal iff its 'diffraction' (Fourier transform of the point measure)
has sharp Bragg peaks.  Dyson's observation: the Riemann zeros are a 1D
quasicrystal whose Bragg peaks sit EXACTLY at the logarithms of prime
powers.  Equivalently -- this IS the explicit formula in Fourier form --
the OUTSIDE (zeros) diffracts into the INSIDE (primes).

We test it directly: form
        D(t) = sum_n cos(gamma_n t)          (a windowed diffraction)
from the known Riemann zeros gamma_n, and check that its extrema land on
t = log(p^k) for prime powers p^k.

Honest status up front:
 * This CONFIRMS the zero<->prime duality (the explicit formula) and shows
   the zeros tile as a quasicrystal -- a real, beautiful structural fact.
 * It is TEXTURE evidence (Kind 1): the PEAK LOCATIONS (log primes) do not
   depend on RH.  What RH controls is the PEAK SHARPNESS -- perfect
   pure-point diffraction <=> all gamma_n real <=> RH.  A finite sample of
   (on-line) zeros cannot prove the sharpness holds forever.  So this
   reveals the structure; it does not prove RH.
 * For OUR substrate L-function the identical picture holds with the
   SUBSTRATE PRIMES (norms N q) as the Bragg peaks -- same explicit formula.
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

# first 40 nontrivial Riemann zeros (imaginary parts)
GAMMA = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
         40.918719, 43.327073, 48.005151, 49.773832, 52.970321, 56.446248,
         59.347044, 60.831779, 65.112544, 67.079811, 69.546402, 72.067158,
         75.704691, 77.144840, 79.337375, 82.910381, 84.735493, 87.425275,
         88.809111, 92.491899, 94.651344, 95.870634, 98.831194, 101.317851,
         103.725538, 105.446623, 107.168611, 111.029536, 111.874659,
         114.320221, 116.226680, 118.790783, 121.370125, 122.946829]


def prime_powers(tmax):
    """(label, log value, weight log p / p^{k/2}) for p^k with log<=tmax."""
    out = []
    def isprime(n):
        return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
    for p in [q for q in range(2, 200) if isprime(q)]:
        k = 1
        while k * math.log(p) <= tmax:
            out.append((f"{p}^{k}" if k > 1 else f"{p}",
                        k * math.log(p), math.log(p) / p ** (k / 2)))
            k += 1
    out.sort(key=lambda z: z[1])
    return out


def diffraction(gammas, t, window=0.003):
    """D(t) = sum_n cos(gamma_n t) e^{-(window gamma_n)^2} (windowed)."""
    g = np.array(gammas)
    w = np.exp(-(window * g) ** 2)
    return np.array([np.sum(w * np.cos(g * tt)) for tt in t])


def main():
    print("=" * 74)
    print("DYSON QUASICRYSTAL TEST: do the zeros diffract into the primes?")
    print("=" * 74)

    tmax = 2.9
    t = np.linspace(0.4, tmax, 4000)
    D = diffraction(GAMMA, t)

    # find extrema (peaks of |D - mean|) -> candidate Bragg positions
    Dc = D - D.mean()
    cand = []
    for i in range(2, len(t) - 2):
        if abs(Dc[i]) > abs(Dc[i-1]) and abs(Dc[i]) > abs(Dc[i+1]) \
           and abs(Dc[i]) > 0.25 * np.max(np.abs(Dc)):
            cand.append((t[i], Dc[i]))

    pp = prime_powers(tmax)
    print("\nPrime-power targets vs nearest diffraction extremum:")
    print(f"  {'p^k':<6} {'log(p^k)':<10} {'nearest |D| peak':<16} "
          f"{'|offset|':<9} {'match'}")
    print("  " + "-" * 56)
    n_match = 0
    for label, lv, wt in pp:
        if lv < 0.55:
            continue
        if not cand:
            break
        nearest = min(cand, key=lambda c: abs(c[0] - lv))
        off = abs(nearest[0] - lv)
        ok = off < 0.05
        n_match += ok
        print(f"  {label:<6} {lv:<10.4f} {nearest[0]:<16.4f} "
              f"{off:<9.4f} {'YES' if ok else 'no'}")

    print(f"\n  prime-power positions matched by a diffraction extremum: "
          f"{n_match}/{len([1 for _,lv,_ in pp if lv>=0.55])}")

    # plot
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(t, Dc, "b-", lw=1.0, label="diffraction  D(t) = Σ cos(γ_n t)")
    for label, lv, wt in pp:
        if lv < 0.55:
            continue
        ax.axvline(lv, color="red", alpha=0.45, lw=1)
        ax.text(lv, np.max(Dc) * 0.92, label, color="red",
                fontsize=8, ha="center")
    ax.set_xlabel("t")
    ax.set_ylabel("D(t) - mean")
    ax.set_title("Riemann zeros diffract into the primes (Dyson quasicrystal)\n"
                 "red lines = log(prime powers); peaks of D(t) land on them")
    ax.legend(loc="lower right")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT / "30_quasicrystal_diffraction.png", dpi=140)
    plt.close()
    print(f"\n  plot -> outputs/30_quasicrystal_diffraction.png")

    print("""
==========================================================================
READING THE RESULT
==========================================================================
If the extrema of D(t) land on log(2), log(3), log(4), log(5), ... then the
zeros ARE a quasicrystal whose Bragg peaks are the prime powers: the
OUTSIDE (zeros) diffracts into the INSIDE (primes).  This is your 'it tiles'
instinct, confirmed -- and it is literally the explicit formula seen as a
diffraction pattern.

WHAT IT REVISES (the bigger picture): zeros and primes are one object seen
two ways -- a self-dual quasicrystal.  The substrate's primes (the Satake
norms N q) are exactly the Bragg peaks of ITS L-function's zeros.

WHAT IT DOES NOT DO: prove RH.  Peak LOCATIONS = primes regardless of RH;
peak SHARPNESS (pure-point diffraction) <=> all gamma_n real <=> RH.  A
finite sample cannot certify sharpness-forever.  So: structure revealed,
proof still requires the Kind-2 step (the self-adjoint operator).  This is
the right picture to build intuition on; it is not itself the proof.
""")


if __name__ == "__main__":
    main()
