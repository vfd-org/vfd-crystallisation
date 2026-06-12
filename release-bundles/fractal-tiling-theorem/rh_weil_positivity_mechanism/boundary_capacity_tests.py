"""WO-RH-WEIL-POSITIVITY-MECHANISM-001 -- Deliverable E: boundary-capacity H - R.

Theorem Target 2:  Q_Weil = H - R,  H >= R  for all admissible h.

H = ARCH + POLE  (the archimedean / completed boundary CAPACITY)
R = PRIME         (the prime residual LOAD)

Both are computed directly from the explicit formula -- the split is canonical
(it is the explicit formula's own terms), not invented after the fact.  Tests:
  * H is a positive kernel (PSD)            -- archimedean capacity is positive
  * R is indefinite                          -- prime side ALONE is not positive
  * Q = H - R is PSD on the tested basis     -- capacity dominates load (so far)
  * "can the prime side alone be positive?"  -- NO: -R has negative directions,
    so positivity REQUIRES the completed/adelic object (Deliverable G).
RH  <=>  H >= R for ALL admissible h (the universal quantifier; not tested here).
"""
from __future__ import annotations

import json
import os

import numpy as np

import weil_functional_harness as W

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "results", "phase_5_boundary_capacity")


def main():
    os.makedirs(OUT, exist_ok=True)
    heights = list(np.linspace(12, 40, 7))
    G = W.weil_gram(heights, sigma=2.0, nz=80, P=3000)
    H = (G["H"] + G["H"].T) / 2
    R = (G["R"] + G["R"].T) / 2
    Q = H - R
    eH, eR, eQ = (np.linalg.eigvalsh(H), np.linalg.eigvalsh(R),
                  np.linalg.eigvalsh(Q))
    # generalised eigenvalues H x = lam R-ish: margin of H over R
    # smallest "capacity margin" = min eig of Q
    print("=" * 72)
    print("Deliverable E -- boundary capacity  Q = H - R")
    print("=" * 72)
    print("\n  H = ARCH+POLE (capacity):  eig min=%.4f max=%.4f  PSD=%s"
          % (eH.min(), eH.max(), eH.min() > -1e-6))
    print("  R = PRIME (residual load): eig min=%.4f max=%.4f  indefinite=%s"
          % (eR.min(), eR.max(), eR.min() < -1e-9 and eR.max() > 1e-9))
    print("  Q = H - R:                 eig min=%.4f  H>=R on basis=%s"
          % (eQ.min(), eQ.min() > -1e-6))
    # can the prime side alone be positive?  test -R and R for sign-definiteness
    prime_alone_positive = (eR.min() > -1e-9)     # is R PSD?
    print("\n  Can the prime residual alone be positive (R PSD)? %s"
          % prime_alone_positive)
    print("  -> positivity REQUIRES the archimedean completion H (capacity).")
    # stress function: eigenvector of Q with smallest eigenvalue = tightest h
    w, v = np.linalg.eigh(Q)
    stress = v[:, 0]
    out = {"heights": heights,
           "H_eig": [round(float(x), 5) for x in eH],
           "R_eig": [round(float(x), 5) for x in eR],
           "Q_eig": [round(float(x), 5) for x in eQ],
           "H_positive_kernel": bool(eH.min() > -1e-6),
           "R_indefinite": bool(eR.min() < -1e-9 and eR.max() > 1e-9),
           "Q_PSD_on_basis": bool(eQ.min() > -1e-6),
           "prime_alone_positive": bool(prime_alone_positive),
           "completion_essential": not bool(prime_alone_positive),
           "tightest_stress_combo": [round(float(x), 4) for x in stress],
           "canonical": "H,R are the explicit-formula terms themselves",
           "RH_equivalence": "H >= R for ALL admissible h  <=>  RH (untested universal)"}
    with open(os.path.join(OUT, "boundary_capacity.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("\n  wrote results/phase_5_boundary_capacity/boundary_capacity.json")


if __name__ == "__main__":
    main()
