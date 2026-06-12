"""What sits between the rungs? Break the cascade symmetry and watch the
spectrum cross from over-ordered (the rung) toward GUE (the generator).

Setup: the rung is a symmetric cascade operator (A_1 on V_600) -- we
measured it is over-ordered (93% degenerate).  'Between the rungs' is the
symmetry-BREAKING transition.  We add a Hermitian perturbation eps*H and
watch the level statistics move.

Unfolding-free diagnostic: the spacing-ratio statistic (Oganesyan-Huse)
  r_n = min(s_n,s_{n+1}) / max(s_n,s_{n+1}),   <r> :
     Poisson (integrable)            <r> ~ 0.386
     GOE  (chaotic, T-symmetric)     <r> ~ 0.531
     GUE  (chaotic, T-broken)        <r> ~ 0.600

Two kinds of breaking, on purpose:
  * REAL-symmetric perturbation  -> GOE  (T-symmetric breaking)
  * COMPLEX-Hermitian perturbation -> GUE (T-BROKEN -- the zeros' class)

The Riemann zeros are GUE, so reaching them needs T-broken breaking. We
also compute <r> for the actual Riemann zeros to compare.
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import icosian as ico

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "outputs"
OUT.mkdir(parents=True, exist_ok=True)
PHI = (1 + 5 ** 0.5) / 2
RNG = np.random.RandomState(12345)

GAMMA = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
         40.918719, 43.327073, 48.005151, 49.773832, 52.970321, 56.446248,
         59.347044, 60.831779, 65.112544, 67.079811, 69.546402, 72.067158,
         75.704691, 77.144840, 79.337375, 82.910381, 84.735493, 87.425275,
         88.809111, 92.491899, 94.651344, 95.870634, 98.831194, 101.317851,
         103.725538, 105.446623, 107.168611, 111.029536, 111.874659,
         114.320221, 116.226680, 118.790783, 121.370125, 122.946829]


def r_statistic(ev):
    ev = np.sort(np.real(ev))
    s = np.diff(ev)
    s = s[s > 1e-9]                       # drop exact degeneracies
    if len(s) < 3:
        return float("nan")
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(np.mean(r))


def A1():
    units = ico.unit_icosians()
    V = np.array([[float(c[0] + c[1] * PHI) for c in q] for q in units])
    n = len(V)
    d2 = np.zeros((n, n))
    for i in range(n):
        diff = V - V[i]; d2[i] = np.sum(diff * diff, axis=1)
    mind = np.min(d2[d2 > 1e-9])
    A = (np.abs(d2 - mind) < 1e-6).astype(float); np.fill_diagonal(A, 0)
    return A


def goe_matrix(n):
    G = RNG.standard_normal((n, n))
    return (G + G.T) / 2

def gue_matrix(n):
    G = RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))
    return (G + G.conj().T) / 2


def main():
    print("=" * 74)
    print("BETWEEN THE RUNGS: breaking the cascade symmetry -> the spectrum")
    print("crosses from over-ordered (rung) toward GUE (the generator)")
    print("=" * 74)

    A = A1(); n = A.shape[0]
    print(f"\nRung operator A_1 (V_600): r-stat at eps=0 = "
          f"{r_statistic(np.linalg.eigvalsh(A)):.3f} (degenerate / over-ordered)")

    # Riemann zeros r-statistic (unfolding-free, so raw spacings fine)
    sz = np.diff(GAMMA)
    rz = np.mean(np.minimum(sz[:-1], sz[1:]) / np.maximum(sz[:-1], sz[1:]))
    print(f"Riemann zeros r-stat = {rz:.3f}  (GUE ~ 0.600)")

    eps = [0.0, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0]
    print("\n  eps    <r> (GOE break, real)   <r> (GUE break, complex)")
    print("  " + "-" * 52)
    r_goe, r_gue = [], []
    Gr = goe_matrix(n); Gc = gue_matrix(n)
    for e in eps:
        evg = np.linalg.eigvalsh(A + e * Gr)
        evc = np.linalg.eigvalsh(A + e * Gc)
        rg, rc = r_statistic(evg), r_statistic(evc)
        r_goe.append(rg); r_gue.append(rc)
        print(f"  {e:<6} {rg:<22.3f} {rc:.3f}")

    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.plot(eps, r_goe, "o-", label="real (T-symmetric) breaking -> GOE")
    ax.plot(eps, r_gue, "s-", label="complex (T-broken) breaking -> GUE")
    ax.axhline(0.386, color="gray", ls=":", label="Poisson 0.386")
    ax.axhline(0.531, color="green", ls="--", label="GOE 0.531")
    ax.axhline(0.600, color="red", ls="--", label="GUE 0.600 (zeros' class)")
    ax.axhline(rz, color="purple", ls="-", lw=1,
               label=f"Riemann zeros {rz:.3f}")
    ax.set_xlabel("symmetry-breaking strength eps  (= 'distance between rungs')")
    ax.set_ylabel("<r> spacing-ratio statistic")
    ax.set_title("Between the rungs = symmetry breaking: the rung (over-ordered)\n"
                 "crosses to GUE only under T-BROKEN breaking -- the zeros' class")
    ax.legend(fontsize=8, loc="center right")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT / "70_between_the_rungs.png", dpi=140)
    plt.close()
    print(f"\n  plot -> outputs/70_between_the_rungs.png")

    print("""
==========================================================================
WHAT THIS SHOWS -- AND THE HONEST CORRECTION
==========================================================================
* The rung itself (eps=0) is over-ordered (degenerate). Breaking its
  symmetry moves the spectrum across the order->chaos gradient.
* COMPLEX (time-reversal-BROKEN) breaking drives it to GUE (<r> -> 0.60),
  the SAME class as the Riemann zeros. REAL breaking only reaches GOE.
  So the generator's class lives in the T-BROKEN breaking between rungs --
  matching 'GUE = T-broken = the spin/asymmetry'.

HONEST CORRECTIONS to 'RH sits between the rungs':
 1. The cascade's OWN 'between' (E8 -> H4 -> D4 -> ... subgroup descent) is a
    chain of SMALLER SYMMETRIC structures -- still over-ordered, NOT chaos.
    That is different from the GENERIC, T-broken breaking that reaches GUE.
 2. The cascade axis runs max-symmetry (E8) -> no-symmetry (0/Unity); the
    order->chaos axis runs Poisson -> GUE. These are DIFFERENT axes. The
    GUE generator is a THIRD thing, not at either cascade end.
 3. 'RH sits between the rungs' was a programme FRAMING (the Millennium-
    cascade association was demoted to honest scope), not an established
    result. What is now precise: the generator lives in T-broken symmetry
    breaking -- the right INSTINCT -- but the cascade's specific subgroup
    'between' is the wrong KIND of breaking.
 4. Breaking -> GUE is UNIVERSAL (any system). This shows the generator's
    CLASS, not the specific Riemann operator. Same wall: which T-broken
    breaking gives exactly the zeros is the open problem.
""")


if __name__ == "__main__":
    main()
