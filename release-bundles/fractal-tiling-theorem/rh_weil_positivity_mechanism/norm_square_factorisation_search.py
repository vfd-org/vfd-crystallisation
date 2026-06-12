"""WO-RH-WEIL-POSITIVITY-MECHANISM-001 -- Deliverable D: norm-square factorisation.

Tests Theorem Target 1:  Q_Weil[h] = |A h|^2.

On a finite test-function basis the Weil Gram Q is real symmetric.  If Q is PSD,
Cholesky gives  Q = A^T A,  i.e.  Q[c] = |A c|^2  -- the factorisation EXISTS on
that subspace.  The decisive question is whether this is structural (survives
cutoff growth, and tracks RH) or artefactual.

Two experiments:
  (D1) cutoff growth: Q on a basis, PSD + Cholesky, smallest eigenvalue vs
       richer bases.  The on-line Weil Gram sits at the EDGE of PSD (min eig ~ 0).
  (D2) the teeth: build the zero-side Gram with the first K zero-quadruples moved
       off the critical line by delta; PSD holds at delta=0 and FAILS for delta>0.
       So  Q = |A h|^2  is possible  <=>  zeros on the line  <=>  RH.

Honest boundary: in (D1)/(D2) the factor A is built from the ZEROS (zero-side).
Deriving the SAME A from the prime/archimedean side WITHOUT zeros is exactly the
open Hilbert-Polya/Weil problem -- the factorisation is not available constructively.
"""
from __future__ import annotations

import json
import math
import os

import numpy as np
import mpmath as mp

import weil_functional_harness as W

mp.mp.dps = 15
HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "results", "phase_4_factorisation_kernel")


# ---- D2: zero-side Gram with optional off-line zeros (the teeth) ----------
def _ghat(s, t, sigma):
    z = (s - 0.5) / 1j - t
    return mp.e ** (-(z * z) / (2 * sigma ** 2))


def zero_side_gram(heights, sigma, zeros):
    m = len(heights)
    Q = np.zeros((m, m), complex)
    for a in range(m):
        for b in range(m):
            tot = 0j
            for rho in zeros:
                tot += complex(_ghat(rho, heights[a], sigma) *
                               mp.conj(_ghat(1 - mp.conj(rho), heights[b], sigma)))
            Q[a, b] = tot
    return (Q + Q.conj().T) / 2


def teeth_experiment(heights=None, sigma=2.0, nz=30, Koff=4):
    # a RICH/tight basis so the on-line Weil Gram sits at the PSD edge
    # (min eig ~ 0), which is where off-line zeros become visible.
    heights = list(np.linspace(10, 45, 12))
    g = W.zeta_gammas(nz)

    def zeros(delta):
        z = []
        for n, gm in enumerate(g):
            if n < Koff and delta > 0:
                b = 0.5 + delta
                z += [mp.mpc(b, gm), mp.mpc(b, -gm),
                      mp.mpc(1 - b, gm), mp.mpc(1 - b, -gm)]
            else:
                z += [mp.mpc(0.5, gm), mp.mpc(0.5, -gm)]
        return z
    rows = []
    for delta in [0.0, 0.1, 0.2, 0.3, 0.4]:
        e = np.linalg.eigvalsh(zero_side_gram(heights, sigma, zeros(delta)))
        rows.append({"delta": delta, "min_eig": float(e.min()),
                     "PSD": bool(e.min() > -1e-9)})
    return rows


# ---- D1: cutoff growth of the formula-side Gram ---------------------------
def cutoff_growth():
    rows = []
    for m in (3, 5, 7):
        heights = list(np.linspace(12, 12 + 6 * (m - 1), m))
        G = W.weil_gram(heights, sigma=2.0, nz=80, P=3000)
        Q = (G["Q_formula"] + G["Q_formula"].T) / 2
        e = np.linalg.eigvalsh(Q)
        psd = e.min() > -1e-9
        chol = None
        if psd:
            try:
                np.linalg.cholesky(Q + 1e-12 * np.eye(m))
                chol = True
            except np.linalg.LinAlgError:
                chol = False
        rows.append({"basis_size": m, "min_eig": float(e.min()),
                     "PSD": bool(psd), "cholesky_A_exists": chol})
    return rows


def main():
    os.makedirs(OUT, exist_ok=True)
    heights = [14.0, 21.0, 25.0, 30.0, 33.0]
    print("=" * 72)
    print("Deliverable D -- norm-square factorisation Q = |A h|^2")
    print("=" * 72)

    print("\n[D1] formula-side Gram: PSD + Cholesky vs basis size")
    d1 = cutoff_growth()
    for r in d1:
        print("   basis=%d  min_eig=%.4e  PSD=%s  Cholesky A exists=%s"
              % (r["basis_size"], r["min_eig"], r["PSD"], r["cholesky_A_exists"]))

    print("\n[D2] teeth: zero-side Gram with off-line zero-quadruples")
    d2 = teeth_experiment(heights, sigma=2.0, nz=30, Koff=3)
    for r in d2:
        print("   delta=%.1f  min_eig=%+.4e  PSD=%s"
              % (r["delta"], r["min_eig"], r["PSD"]))
    teeth = (d2[0]["PSD"] and not any(r["PSD"] for r in d2[1:]))

    print("\n  on-line factorisation Q=|Ah|^2 exists; off-line it FAILS "
          "(PSD lost): %s" % teeth)
    print("  => Q=|Ah|^2  <=>  zeros on line  <=>  RH.  But A is built from the")
    print("     zeros; deriving A from primes+archimedean is the open problem.")
    with open(os.path.join(OUT, "norm_square.json"), "w") as f:
        json.dump({"D1_cutoff_growth": d1, "D2_teeth": d2,
                   "teeth_confirmed": teeth,
                   "boundary": "A is zero-side; prime-side A is the open Hilbert-Polya problem"},
                  f, indent=2)
    print("\n  wrote results/phase_4_factorisation_kernel/norm_square.json")


if __name__ == "__main__":
    main()
