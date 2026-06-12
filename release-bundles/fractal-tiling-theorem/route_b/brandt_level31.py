"""Route B, step 2 (SCAFFOLD): Brandt matrices at level (5phi-2).

STATUS UPDATE (WO-VFD-ICOSIAN-BRANDT-CUSPIDAL-GEOMETRY-001): the [TODO] steps
2-4 below (Eichler order, ideal-class enumeration, Brandt matrices over Z[phi])
are now IMPLEMENTED and the circle is CLOSED, in the sibling bundle
    ../icosian_brandt_cuspidal_geometry/
via the class-number-1 definite method (A_5 = I^1/{+-1} acting on P^1(F_31)),
not the Kneser-neighbour enumeration sketched here.  Result:
PASS_GEOMETRIC_CUSPIDAL_ENCODING -- the icosian Brandt cuspidal eigenvalues
equal the point-counted a_P out-of-sample with zero fitting (h=2, mass 8/15,
self-adjoint, common eigenform (3,-5)).  See that bundle's WORK_ORDER_RESULT.md.
This file is kept as the original scaffold/record.



GOAL: compute the substrate's OWN cuspidal Hecke eigenvalues -- the
icosian Brandt action at level p31 = (5phi-2) -- and compare them,
out-of-sample and WITHOUT fitting, to the genuine target H computed in
sims/sim_genuine_eigenvalues.py (data/genuine_newform_eigenvalues.csv).

This is the only honest way to close the circle (see CIRCLE_TEST.md).

STATUS: this file is a structured scaffold.  Steps marked [DONE] use the
exact icosian arithmetic from icosian.py.  Steps marked [TODO] are the
genuine remaining build (the quaternion ideal-class enumeration and the
Brandt entries) -- the part SCOPE.md estimates at 2-4 weeks.  Each TODO
has its algorithm spelled out and an acceptance check.

ALGORITHM (Dembele 2007; Voight, Quaternion Algebras, Ch. 41):

  B = (-1,-1 / K), K = Q(sqrt5), ramified at the two real places.
  I = icosian ring = maximal order (icosian.py).  Class number h(I) = 1.

  1. [DONE]  Build I explicitly (icosian.py): arithmetic, norm, 2I units.

  2. [TODO]  Build an Eichler order O of level p31 = (5phi-2):
        O = { x in I : x mod p31 is upper-triangular }
     under a fixed isomorphism I (x) O_{p31} ~ M_2(O_K / p31) = M_2(F_31).
     Concretely: p31 splits the local algebra (B is unramified at p31
     since p31 does not divide disc(B) = (1)); pick a splitting
     I (x) Z_{p31} ~ M_2(Z_{p31}), and O = preimage of upper-triangular
     mod p31.  [O : I-as-order] index = N(p31)+1 = 32 locally.

  3. [TODO]  Enumerate the right-ideal classes of O:
        Cl(O) = { [I_1], ..., [I_h] },  h = dim of the Brandt module.
     Method (Kneser p-neighbours / theta reduction):
        - start from O itself as a right ideal;
        - repeatedly form p-neighbour ideals for small split p and
          reduce each to a canonical (Minkowski-reduced) representative
          in its class via the rank-8 Z-lattice short-vector machinery;
        - collect inequivalent classes until the mass formula is met.
     ACCEPTANCE: sum_i 1/|O_i^x| must equal the Eichler mass
        mass(O) = (zeta_K(-1) / ...) * prod_{p | level} (N(p)+1)
     For B/Q(sqrt5) ram. at both infinities, zeta_K(-1) = 1/30, and the
     expected Brandt-module dimension at norm 31 is SMALL: h = 2
     (1 Eisenstein + 1 cuspidal).  <-- this is the key acceptance gate.

  4. [TODO]  Brandt matrices B(p), for each prime ideal p (p not | level):
        B(p)_{ij} = (1/ w_j) * #{ x in Hom(I_j, I_i) : nrd(x) = p * [norms] }
     computed as half the number of vectors of the right norm in the
     rank-8 Z-lattice  I_i I_j^{-1}  (a theta-series coefficient).
     This reuses the short-vector enumeration from step 3.

  5. [DONE-here] Given the Brandt matrices, extract the cuspidal Hecke
     eigenvalues and run the circle test (this file implements 5 fully;
     it consumes B(p) once steps 2-4 produce them).

The honest one-line summary: steps 2-4 are a real quaternion-arithmetic
build with no Python/Sage library support over Z[phi]; everything around
them (icosian arithmetic in, circle test out) is done and exact.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"

# Expected Brandt-module dimension at level (5phi-2) -- acceptance gate.
EXPECTED_DIM = 2          # 1 Eisenstein + 1 cuspidal (norm-31 newform)
LEVEL_NORM = 31


def load_genuine_target():
    """Load H = genuine newform eigenvalues (the fixed target)."""
    path = DATA / "genuine_newform_eigenvalues.csv"
    if not path.exists():
        raise SystemExit(
            "Run sims/sim_genuine_eigenvalues.py first to produce the "
            "genuine target H.")
    H = []
    with open(path) as f:
        for row in csv.DictReader(f):
            if row["status"] == "good":
                H.append({
                    "norm": int(row["norm_NP"]),
                    "kind": row["kind"],
                    "p": int(row["p"]),
                    "a_P": int(row["a_P"]),
                })
    return H


def build_eichler_order_level_p31():
    """[TODO step 2] Build the Eichler order of level (5phi-2).

    Returns None until implemented.  Implementation plan in module docstring.
    """
    return None


def enumerate_ideal_classes(order):
    """[TODO step 3] Right-ideal classes of the Eichler order.

    Returns list of ideal-class representatives, or None.
    ACCEPTANCE: len(result) == EXPECTED_DIM and the mass formula holds.
    """
    if order is None:
        return None
    raise NotImplementedError("ideal-class enumeration (Kneser neighbours)")


def brandt_matrix(classes, prime_ideal):
    """[TODO step 4] Brandt matrix B(p) on the ideal classes."""
    raise NotImplementedError("Brandt matrix via theta coefficients")


def cuspidal_eigenvalues(classes, primes):
    """[step 5, DONE] Given ideal classes + Brandt matrices, return the
    substrate cuspidal Hecke eigenvalues S = {a_P^sub}."""
    # B(p) are simultaneously diagonalisable; the Eisenstein eigenvector
    # is all-ones, the cuspidal eigenvector(s) span its complement.
    import numpy as np
    h = len(classes)
    # collect Brandt matrices
    Bs = {pi: brandt_matrix(classes, pi) for pi in primes}
    # Eisenstein direction
    ones = np.ones(h) / math.sqrt(h)
    # cuspidal subspace = orthogonal complement of ones in the common
    # eigenbasis; for h=2 it is a single vector v_cusp
    # (general h: simultaneous diagonalisation of {Bs})
    anyB = next(iter(Bs.values()))
    w, V = np.linalg.eigh(anyB)
    cusp_cols = [k for k in range(h)
                 if abs(abs(V[:, k] @ ones) - 1.0) > 1e-6]
    S = {}
    for pi, B in Bs.items():
        # eigenvalue of B on the cuspidal eigenvector
        vc = V[:, cusp_cols[0]]
        S[pi] = float(vc @ (B @ vc))
    return S


def circle_test(S, H):
    """[step 5, DONE] Out-of-sample, no-fit comparison of substrate S to
    genuine H.  Fit nothing; just check equality up to one global sign."""
    # match by prime norm/kind; report agreement on held-out primes.
    paired = []
    for h in H:
        key = (h["norm"], h["kind"], h["p"])
        if key in S:
            paired.append((key, h["a_P"], S[key]))
    if not paired:
        return {"status": "no substrate data yet"}
    # allow a single global sign convention (Hecke normalisation)
    import numpy as np
    g = np.array([p[1] for p in paired], dtype=float)
    s = np.array([p[2] for p in paired], dtype=float)
    sign = 1.0 if np.dot(g, s) >= 0 else -1.0
    rmse = float(np.sqrt(np.mean((g - sign * s) ** 2)))
    exact = int(np.sum(np.abs(g - sign * s) < 1e-6))
    return {"status": "tested", "n": len(paired), "rmse": rmse,
            "exact_matches": exact, "sign": sign}


def main():
    print("=" * 74)
    print("ROUTE B step 2-5: Brandt matrices at level (5phi-2) [SCAFFOLD]")
    print("=" * 74)

    H = load_genuine_target()
    print(f"\n[step 0] Loaded genuine target H: {len(H)} eigenvalues "
          f"(N(P) <= 200), the fixed pre-registered comparison set.")
    print(f"         e.g. a_P at N(P)=4,5,9,11: "
          f"{[h['a_P'] for h in H[:4]]}")

    print(f"\n[step 1] Icosian ring + 2I unit group: DONE (see icosian.py)")

    print(f"\n[step 2] Eichler order of level (5phi-2): ", end="")
    order = build_eichler_order_level_p31()
    print("TODO" if order is None else "built")

    print(f"[step 3] Ideal-class enumeration (target dim = "
          f"{EXPECTED_DIM}): ", end="")
    classes = enumerate_ideal_classes(order)
    print("TODO" if classes is None else f"{len(classes)} classes")

    print(f"[step 4] Brandt matrices B(p): TODO")
    print(f"[step 5] Circle test harness: DONE (waits for B(p))")

    if classes is not None:
        primes = [(h["norm"], h["kind"], h["p"]) for h in H]
        S = cuspidal_eigenvalues(classes, primes)
        result = circle_test(S, H)
        print(f"\nCIRCLE TEST RESULT: {result}")
    else:
        print("\n" + "-" * 74)
        print("Substrate side not yet computed -> circle test pending.")
        print("The target H is locked; once steps 2-4 land, this script")
        print("runs the out-of-sample comparison automatically.")
        print("-" * 74)
        print(f"""
ACCEPTANCE GATES (in order, each cheap relative to the next):
  G1  ideal-class count h == {EXPECTED_DIM}      (else geometry wrong)
  G2  mass formula satisfied               (else enumeration incomplete)
  G3  cuspidal a_P Ramanujan-bounded       (else not a cusp form)
  G4  circle_test exact_matches == {len(H)}     (THE result: S == H?)

If G4 passes with zero fitting -> the substrate's own arithmetic
reproduces the genuine newform: the circle closes, (O2) holds.
If G4 fails -> (O2) is false; the substrate eigenvalues are not these
Hecke eigenvalues.  Either outcome is decisive and honest.
""")


if __name__ == "__main__":
    main()
