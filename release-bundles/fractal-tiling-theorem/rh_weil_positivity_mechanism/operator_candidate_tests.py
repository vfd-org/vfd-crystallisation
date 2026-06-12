"""WO-RH-WEIL-POSITIVITY-MECHANISM-001 -- Deliverable H: self-adjoint operator.

Theorem Target 4:  Q_Weil[h] = <h, K h> with K self-adjoint, K >= 0.

On the finite test-function basis, K is just the Weil Gram Q (symmetric).  We
verify: (i) symmetry <f,Kg>=<Kf,g>; (ii) positivity <h,Kh> >= 0 on the basis;
(iii) that K is NOT a new operator -- it is the Weil functional represented as a
matrix.  The theorem that would make K>=0 universally (for the full admissible
test-function class) is RH; and a CANONICAL self-adjoint K acting on the actual
zeros would be the archimedean-adelic Hilbert-Polya operator -- open.
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
    heights = list(np.linspace(12, 40, 6))
    G = W.weil_gram(heights, sigma=2.0, nz=80, P=3000)
    K = (G["Q_formula"] + G["Q_formula"].T) / 2
    rng = np.random.RandomState(0)
    f = rng.standard_normal(len(heights))
    g = rng.standard_normal(len(heights))
    sym = abs(f @ (K @ g) - (K @ f) @ g) < 1e-9
    pos = all((c @ (K @ c)) > -1e-6 for c in rng.standard_normal((200, len(heights))))
    eK = np.linalg.eigvalsh(K)
    print("=" * 72)
    print("Deliverable H -- self-adjoint operator candidate K,  Q[h]=<h,K h>")
    print("=" * 72)
    print("\n  symmetric <f,Kg>=<Kf,g>:", bool(sym))
    print("  positive <h,Kh> >= 0 on 200 random h:", bool(pos))
    print("  spectrum of K: min=%.4f  max=%.4f" % (eK.min(), eK.max()))
    print("\n  Is K a NEW operator?  No -- it is the Weil functional as a matrix.")
    print("  K >= 0 for ALL admissible h  ==  RH (open universal quantifier).")
    print("  A canonical self-adjoint K acting on the ZEROS = the archimedean-")
    print("  adelic Hilbert-Polya operator -- open (see ARCHIMEDEAN_ADELIC...md).")
    out = {"heights": heights, "symmetric": bool(sym),
           "positive_on_random": bool(pos),
           "spectrum_min": float(eK.min()), "spectrum_max": float(eK.max()),
           "is_new_operator": False,
           "universal_positivity_equals": "RH",
           "canonical_zero_operator": "archimedean-adelic Hilbert-Polya (open)"}
    with open(os.path.join(OUT, "operator.json"), "w") as f2:
        json.dump(out, f2, indent=2)
    print("\n  wrote results/phase_4_factorisation_kernel/operator.json")


if __name__ == "__main__":
    main()
