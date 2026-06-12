"""Arithmetic closure energy: where  Q[f] = |A f|^2 >= 0  is REAL in our
geometry, and where it becomes RH.

The request: exhibit the arithmetic "closure energy" form Q[f] = |A f|^2 (a
positive geometric/spectral quadratic form, not physical joules), derived from
the geometry, whose positivity would be RH-grade.

The honest map, as a ladder of three rungs that are TRUE, then the wall:

  RUNG 1 (true, finite, exact).  The icosian trace form
        Q(x) = Tr_{K/Q}( nrd(x) )
  is a positive-definite integral quadratic form on the icosian ring (Gram
  det 5^4 = 625).  It factors as Q(x) = |A x|^2 with A a real Cholesky factor,
  so Q(x) >= 0 manifestly; minimal nonzero energy = 2 (the 120 unit icosians).
  This is exactly the requested Q = |A f|^2 -- realised, not metaphorical.

  RUNG 2 (true, finite, exact).  The Brandt/Hecke operators B(P) are
  SELF-ADJOINT for the orbit-size inner product mu = (20,12) (verified in
  brandt_matrices.py).  A self-adjoint operator has real spectrum: the "modes"
  have real energy, and those energies are exactly the Hecke eigenvalues a_P.
  So the arithmetic resonator has a real spectrum -- the finite Hilbert-Polya
  picture holds at the level of the Hecke spectrum.

  RUNG 3 (the same SHAPE, but now the open one).  The RH closure energy is the
  Weil functional  W(h) = ARCH(h) - PRIME(h)  (route_b/weil_wall.py), whose
  positivity  W(h) >= 0 for all h  is RH for the L-function.  This is the
  infinite-dimensional analogue of rungs 1-2.

THE WALL (why rung 3 does not follow from rungs 1-2).  Rungs 1-2 give a finite
positive form and a finite self-adjoint operator on the COEFFICIENT/Hecke side.
RH is positivity on the ZERO side.  There is no theorem carrying finite
arithmetic positivity to the Weil/Li positivity -- they are different
categories (see POSITIVITY_AND_RH.md).  Writing W(h) = |A_inf h|^2 with a
geometrically-derived A_inf IS the Hilbert-Polya operator, and that is exactly
the open problem.  We can write A explicitly at rungs 1-2; we cannot derive
A_inf for rung 3.  No RH proof is claimed.
"""
from __future__ import annotations

import os

import numpy as np

try:
    from . import quaternion_order as qo
    from . import brandt_matrices as bm
except ImportError:
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    import quaternion_order as qo
    import brandt_matrices as bm


def rung1_trace_form_energy():
    """Q(x)=Tr(nrd x) = |A x|^2, positive arithmetic energy; Cholesky factor."""
    I = qo.ring()
    M = np.array(I.gram, float)        # even integral Gram of the trace form
    GQ = M / 2.0                       # Q(x) = x^T GQ x
    A = np.linalg.cholesky(GQ).T       # GQ = A^T A  ->  Q(x) = |A x|^2
    factor_ok = bool(np.allclose(A.T @ A, GQ))
    # minimal nonzero energy and its multiplicity (the kissing number)
    import itertools
    mn = None
    count = 0
    for c in itertools.product(range(-1, 2), repeat=8):
        if any(c):
            v = np.array(c, float)
            q = float(v @ GQ @ v)
            if q > 0 and (mn is None or q < mn - 1e-9):
                mn = q
                count = 1
            elif mn is not None and abs(q - mn) < 1e-9:
                count += 1
    return {
        "gram_det": round(float(np.linalg.det(M))),
        "factors_as_square": factor_ok,
        "positive_definite": bool(np.all(np.linalg.eigvalsh(GQ) > 0)),
        "min_energy": round(mn),
        "min_energy_multiplicity_in_{-1,0,1}^8": count,
        "A_shape": list(A.shape),
    }


def rung2_brandt_selfadjoint(norms=(11, 19, 41)):
    """B(P) self-adjoint in mu=(20,12); real spectrum = a_P."""
    eng = bm.BrandtEngine()
    mu = eng.mu
    out = []
    for Np in norms:
        v = bm.totally_positive_generator(Np)
        r = eng.brandt_matrix(v)
        B = np.array([[float(x) for x in row] for row in r["matrix"]])
        # self-adjoint in mu: D^{1/2} B D^{-1/2} symmetric, D=diag(mu)
        D = np.diag([float(m) for m in mu])
        Bsym = np.sqrt(D) @ B @ np.linalg.inv(np.sqrt(D))
        symmetric = bool(np.allclose(Bsym, Bsym.T))
        eig = sorted(np.linalg.eigvals(B).real.round(6))
        all_real = bool(np.all(np.abs(np.linalg.eigvals(B).imag) < 1e-9))
        out.append({"norm": Np, "self_adjoint": symmetric,
                    "spectrum_real": all_real, "eigenvalues": eig,
                    "cuspidal_a_P": r["cuspidal_eigenvalue"]})
    return {"measure_mu": list(mu), "operators": out}


def main():
    print("=" * 74)
    print("ARITHMETIC CLOSURE ENERGY  Q[f] = |A f|^2  --  where it is real,")
    print("and where it becomes RH")
    print("=" * 74)

    r1 = rung1_trace_form_energy()
    print("\nRUNG 1  icosian trace-form energy  Q(x) = Tr(nrd x) = |A x|^2")
    print("  Gram det                 :", r1["gram_det"], "(= 5^4)")
    print("  factors as a square |Ax|^2:", r1["factors_as_square"],
          "  (A is", "x".join(map(str, r1["A_shape"])) + ", real)")
    print("  positive definite        :", r1["positive_definite"])
    print("  minimal nonzero energy   :", r1["min_energy"],
          "(kissing norm; full kissing number = 120 unit icosians,",
          r1["min_energy_multiplicity_in_{-1,0,1}^8"],
          "of them inside {-1,0,1}^8 in this basis)")
    print("  -> Q = |A f|^2 is REAL here: a positive arithmetic energy form.")

    r2 = rung2_brandt_selfadjoint()
    print("\nRUNG 2  Brandt/Hecke operators self-adjoint (mu = %s)"
          % r2["measure_mu"])
    for o in r2["operators"]:
        print("  N(P)=%2d  self-adjoint=%s  spectrum-real=%s  eig=%s  a_P=%s"
              % (o["norm"], o["self_adjoint"], o["spectrum_real"],
                 o["eigenvalues"], o["cuspidal_a_P"]))
    print("  -> the arithmetic resonator has a REAL spectrum = the a_P.")

    print("\nRUNG 3  the RH closure energy  W(h) = ARCH(h) - PRIME(h)")
    print("  (route_b/weil_wall.py)  same SHAPE; W(h) >= 0 for ALL h  ==  RH.")
    print("  We supply ARCH, PRIME parameter-free from the geometry; positivity")
    print("  on the tested h holds but is archimedean-dominated (not sharp).")

    print("\n" + "-" * 74)
    print("THE WALL")
    print("-" * 74)
    print("""  Rungs 1-2 give Q = |A f|^2 and a self-adjoint operator EXPLICITLY,
  but on the coefficient / Hecke side (finite, algebraic).  RH is positivity
  on the ZERO side.  Writing the RH energy as W(h) = |A_inf h|^2 with a
  geometric A_inf IS the Hilbert-Polya operator -- the open problem.  We can
  write A at rungs 1-2; we cannot derive A_inf for rung 3.  Different
  categories (POSITIVITY_AND_RH.md); no theorem bridges them, and none is
  claimed.  Arithmetic energy = positive geometric/spectral form (real here),
  NOT physical joules, and NOT yet a proof of RH.""")


if __name__ == "__main__":
    main()
