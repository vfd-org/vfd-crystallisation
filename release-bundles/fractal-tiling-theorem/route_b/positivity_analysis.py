"""Route B, step 7: does the substrate's positivity reach the zeros?

The honest question behind the Li/Weil-positivity route: RH for L(f,s) is
equivalent to positivity of the Li coefficients lambda_n (a statement about
the ZEROS).  The substrate has its own positivity: the closure operator
C_phi = (12 + phi^-2) I - A_1 is positive definite.  Does the substrate
positivity feed the zero-side positivity?

This script computes C_phi's spectrum exactly and then states precisely
why the two positivities live in different categories -- so that the
'positivity' angle does NOT give a substrate-side route to RH, any more
than the explicit-formula angle did.
"""
from __future__ import annotations

import math

import numpy as np

import icosian as ico

PHI = (1 + math.sqrt(5)) / 2
INVPHI2 = PHI ** -2


def build_A1():
    units = ico.unit_icosians()
    V = np.array([[float(c[0] + c[1] * PHI) for c in q] for q in units])
    n = len(V)
    # nearest-neighbour (600-cell) adjacency by minimal squared distance
    d2 = np.zeros((n, n))
    for i in range(n):
        diff = V - V[i]
        d2[i] = np.sum(diff * diff, axis=1)
    mind = np.min(d2[d2 > 1e-9])
    A = ((np.abs(d2 - mind) < 1e-6)).astype(float)
    np.fill_diagonal(A, 0.0)
    return A


def main():
    print("=" * 74)
    print("ROUTE B step 7: substrate positivity (C_phi) vs zero positivity (Li)")
    print("=" * 74)

    A1 = build_A1()
    deg = int(A1[0].sum())
    print(f"\nV_600 adjacency A_1: 120 vertices, regular degree {deg}")
    C = (12 + INVPHI2) * np.eye(120) - A1
    ev = np.linalg.eigvalsh(C)
    ev_sorted = np.sort(ev)
    print(f"C_phi = (12 + phi^-2) I - A_1")
    print(f"  smallest eigenvalue: {ev_sorted[0]:.6f}  "
          f"(phi^-2 = {INVPHI2:.6f})")
    print(f"  largest  eigenvalue: {ev_sorted[-1]:.6f}")
    print(f"  C_phi positive definite: {ev_sorted[0] > 1e-9}")
    # distinct eigenvalues
    distinct = sorted(set(round(float(x), 4) for x in ev))
    print(f"  distinct eigenvalues ({len(distinct)}): {distinct}")
    mult_min = int(np.sum(np.abs(ev - ev_sorted[0]) < 1e-6))
    print(f"  multiplicity of the minimum (the witness V_min): {mult_min}")

    print("""
==========================================================================
WHY THIS POSITIVITY DOES NOT REACH THE ZEROS
==========================================================================

C_phi >= 0 is positivity of a FINITE 120x120 operator built from the
600-cell geometry.  It certifies that the witness eigenvector V_min EXISTS
(the smallest-eigenvalue eigenspace).  That is a COEFFICIENT/GEOMETRY-side
fact: it lives in the same place as the Hecke eigenvalues a_q, which the
substrate genuinely computes (steps 2-5).

The Li criterion is positivity of the coefficients

    lambda_n = sum over zeros rho of [ 1 - (1 - 1/rho)^n ]   (>= 0  <=>  RH),

i.e. positivity of an explicit-formula functional on the ZEROS of L(f,s).

The substrate's influence on L(f,s) factors entirely through the VALUES
a_q -> Dirichlet series -> analytic continuation -> zeros -> lambda_n.
C_phi >= 0 is used only at the FIRST arrow (the eigenform exists); it does
not constrain the analytic continuation or the zero locations.  There is
no theorem -- and no plausible mechanism -- by which positivity of the
finite operator C_phi implies lambda_n >= 0.  They are positivity in
different categories:

    C_phi >= 0           lives on   finite-dim geometry / coefficients
    lambda_n >= 0 (RH)   lives on   the zeros of an analytic L-function

CONCRETE CHECK: the C_phi spectrum is the multiset
    { (12 + phi^-2) - mu : mu in spec(A_1) },
a finite set of algebraic numbers in Q(sqrt5) determined by the 600-cell.
The lambda_n are transcendental-looking analytic invariants of L(f,s).
There is no arithmetic map taking one to the other; matching them would be
numerology, not a derivation.

CONCLUSION (honest): the 'positivity' route is in the same position as the
explicit-formula route.  The substrate supplies a genuine eigenform and a
genuine finite positivity (C_phi), but neither reaches the zero-side
positivity that IS RH.  Computing lambda_n for L(f,s) is a well-defined
numerical task (evidence, not proof) using the standard Bessel-K_0
approximate functional equation for the degree-4 gamma factor
Gamma_C(s)^2; but its positivity, if it holds, would be a property of
L(f,s), NOT a substrate output -- exactly as RH for L(f,s) is GRH.
""")


if __name__ == "__main__":
    main()
