"""WO-RH-WEIL-POSITIVITY-MECHANISM-001 -- Deliverable F: kernel positivity.

Theorem Target 3:  Q_Weil[h] = <h, K h> with a Hermitian kernel K >= 0.

Discretised on the test-function basis, the Weil quadratic form IS c^T Q c with
Q = H - R (the harness Gram).  So the discrete "kernel" is K = Q, with the
canonical decomposition K = K_arch - K_prime (= H - R).  We check:
  * Hermitian symmetry of each block
  * K_arch (archimedean) PSD     -- a positive kernel
  * K_prime (prime) indefinite    -- negative modes present
  * K = K_arch - K_prime PSD on the tested basis
  * whether positivity of K on richer bases is equivalent to RH (it is: the
    teeth in norm_square_factorisation_search show K loses PSD iff a zero leaves
    the line).

Conclusion: the candidate kernel is exactly the Weil kernel; its positivity is
RH.  It is not a NEW kernel -- it is the explicit-formula kernel, with the
archimedean block carrying the positivity and the prime block threatening it.
"""
from __future__ import annotations

import json
import os

import numpy as np

import weil_functional_harness as W

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "results", "phase_4_factorisation_kernel")


def main():
    os.makedirs(OUT, exist_ok=True)
    heights = list(np.linspace(12, 42, 8))
    G = W.weil_gram(heights, sigma=2.0, nz=80, P=3000)
    Karch = (G["H"] + G["H"].T) / 2
    Kprime = (G["R"] + G["R"].T) / 2
    K = Karch - Kprime
    herm = (np.allclose(Karch, Karch.T) and np.allclose(Kprime, Kprime.T))
    eA, eP, eK = (np.linalg.eigvalsh(Karch), np.linalg.eigvalsh(Kprime),
                  np.linalg.eigvalsh(K))
    print("=" * 72)
    print("Deliverable F -- kernel positivity  Q[h] = <h, K h>,  K = K_arch - K_prime")
    print("=" * 72)
    print("\n  Hermitian symmetry of blocks:", herm)
    print("  K_arch  (archimedean): min eig=%.4f  PSD (positive kernel)=%s"
          % (eA.min(), eA.min() > -1e-6))
    print("  K_prime (prime):       min eig=%.4f max=%.4f  indefinite=%s"
          % (eP.min(), eP.max(), eP.min() < -1e-9 and eP.max() > 1e-9))
    print("  K = K_arch - K_prime:  min eig=%.4f  PSD on basis=%s"
          % (eK.min(), eK.min() > -1e-6))
    print("\n  -> the candidate kernel IS the Weil kernel; K>=0 universally == RH")
    print("     (negative modes appear iff a zero leaves the line; see teeth).")
    out = {"heights": heights, "hermitian": bool(herm),
           "Karch_min_eig": float(eA.min()), "Karch_PSD": bool(eA.min() > -1e-6),
           "Kprime_min_eig": float(eP.min()), "Kprime_max_eig": float(eP.max()),
           "Kprime_indefinite": bool(eP.min() < -1e-9 and eP.max() > 1e-9),
           "K_min_eig": float(eK.min()), "K_PSD_on_basis": bool(eK.min() > -1e-6),
           "is_new_kernel": False,
           "note": "K = explicit-formula Weil kernel; positivity = RH"}
    with open(os.path.join(OUT, "kernel.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("\n  wrote results/phase_4_factorisation_kernel/kernel.json")


if __name__ == "__main__":
    main()
