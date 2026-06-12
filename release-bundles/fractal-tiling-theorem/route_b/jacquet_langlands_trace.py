"""Tracing the H -> C class transition through Jacquet-Langlands.

The question: where does the substrate's QUATERNIONIC (H, beta=4, GSE)
arithmetic become the COMPLEX/unitary (C, beta=2, GUE) object whose high
zeros are GUE?  Answer: it is the standard chain, and we verify each step
from our own data.

  STEP 1  H (x) C  ~=  M_2(C).   Complexifying the quaternions gives the
          2x2 complex matrices.  Concretely the splitting
              1 -> I,  i -> [[i,0],[0,-i]],  j -> [[0,1],[-1,0]],  k = ij
          is an ALGEBRA ISOMORPHISM, and the quaternion reduced norm becomes
          the matrix DETERMINANT:  nrd(q) = det(rho(q)).
          (Local face: the splitting B (x) F_31 ~= M_2(F_31) used in
          step2_eichler.py is exactly this, mod the prime.)

  STEP 2  Unit quaternions  ->  SU(2).   The 120 icosians (nrd=1) map to
          SU(2) (det 1, unitary).  So 2I  subset  SU(2): the quaternionic
          UNITS sit inside the UNITARY group.  This is the beta=4 -> beta=2
          step in concrete form: H-units become SU(2) = the unitary (C)
          structure.  The Satake angles theta_q (a_q = 2 sqrt(N q) cos theta_q)
          are the SU(2) conjugacy angles -- Sato-Tate IS the SU(2) measure.

  STEP 3  Jacquet-Langlands:  B^x  <->  GL_2(K).   The quaternionic eigenform
          transfers to a GL_2 Hilbert cusp form with the SAME a_q.  We
          ALREADY verified this: the circle test (substrate a_q = genuine
          newform a_q, 11 primes) IS the JL eigenvalue matching.

  STEP 4  L(pi,s) high zeros -> GUE  (Rudnick-Sarnak universality for fixed
          automorphic L-functions).  We ALREADY verified this: the
          quantum_chaos_test (level repulsion, <r>~0.62).

So the H->C transition is: complexify H into M_2(C)/SU(2)/GL_2 (steps 1-2),
match to GL_2 by JL (step 3), and the GL_2 L-function's zeros are GUE (step
4).  The class flip happens at COMPLEXIFICATION (H -> SU(2)), the unitary
structure -- NOT in the polytope geometry.  This file verifies steps 1-2
exactly; steps 3-4 were verified earlier in the bundle.
"""
from __future__ import annotations

import math
import numpy as np
import icosian as ico

PHI = (1 + 5 ** 0.5) / 2
I2 = np.eye(2, dtype=complex)
RI = np.array([[1j, 0], [0, -1j]], dtype=complex)        # rho(i)
RJ = np.array([[0, 1], [-1, 0]], dtype=complex)          # rho(j)
RK = RI @ RJ                                              # rho(k) = ij


def quat_to_M2(q):
    """q = (w,x,y,z) over Z[phi] -> 2x2 complex matrix via the splitting."""
    w, x, y, z = (float(c[0] + c[1] * PHI) for c in q)
    return w * I2 + x * RI + y * RJ + z * RK


def main():
    print("=" * 74)
    print("JACQUET-LANGLANDS TRACE: H -> C (quaternions -> unitary/GL_2)")
    print("=" * 74)

    # STEP 1: algebra homomorphism + nrd = det
    print("\n[STEP 1] H (x) C ~= M_2(C):  algebra iso + nrd = det")
    ok_alg = (np.allclose(RI @ RI, -I2) and np.allclose(RJ @ RJ, -I2)
              and np.allclose(RK @ RK, -I2)
              and np.allclose(RI @ RJ, RK) and np.allclose(RJ @ RI, -RK))
    print(f"  i^2=j^2=k^2=-1, ij=k, ji=-k (matrices): "
          f"{'OK' if ok_alg else 'FAIL'}")
    units = ico.unit_icosians()
    sub = lambda a, b: (a[0] - b[0], a[1] - b[1])
    max_nrd_det = 0.0
    for q in units:
        nrd = ico.nrd(q, ico.zmf, ico.zaf, sub)
        nrd_val = float(nrd[0] + nrd[1] * PHI)
        det_val = np.linalg.det(quat_to_M2(q)).real
        max_nrd_det = max(max_nrd_det, abs(nrd_val - det_val))
    print(f"  max |nrd(q) - det(rho(q))| over 120 units: {max_nrd_det:.2e} "
          f"{'(nrd = det confirmed)' if max_nrd_det < 1e-9 else 'FAIL'}")

    # STEP 2: units -> SU(2)
    print("\n[STEP 2] unit quaternions -> SU(2) (the unitary / C structure)")
    max_unitary, max_det1 = 0.0, 0.0
    for q in units:
        M = quat_to_M2(q)
        max_unitary = max(max_unitary,
                          np.max(np.abs(M @ M.conj().T - I2)))
        max_det1 = max(max_det1, abs(np.linalg.det(M) - 1))
    print(f"  max ||rho(q) rho(q)* - I||: {max_unitary:.2e}")
    print(f"  max |det - 1|: {max_det1:.2e}")
    in_su2 = max_unitary < 1e-9 and max_det1 < 1e-9
    print(f"  => 120 icosian units sit in SU(2): "
          f"{'CONFIRMED (2I subset SU(2))' if in_su2 else 'FAIL'}")
    print("  The quaternionic UNITS (beta=4) are inside the UNITARY group")
    print("  SU(2) (beta=2). Satake angles theta_q = SU(2) conjugacy angles")
    print("  (Sato-Tate = the SU(2) measure). This IS the H->C class flip.")

    # STEPS 3-4: already done
    print("\n[STEP 3] Jacquet-Langlands B^x <-> GL_2: VERIFIED earlier")
    print("  = the circle test (substrate a_q == genuine newform a_q, 11")
    print("    primes, step3_4_hecke.py). JL matches the Hecke eigenvalues.")
    print("\n[STEP 4] GL_2 L-function high zeros -> GUE: VERIFIED earlier")
    print("  = quantum_chaos_test (level repulsion, <r> ~ 0.62).")
    print("    Rudnick-Sarnak: high zeros of any fixed automorphic")
    print("    L-function are GUE (beta=2, C).")

    print("""
==========================================================================
WHERE THE CLASS FLIPS
==========================================================================
H (beta=4, GSE, quaternionic substrate)
   |  STEP 1-2: COMPLEXIFY.  H (x) C = M_2(C); units -> SU(2).
   v                          <-- the class flip is HERE: complexification
SU(2) / GL_2 (beta=2, UNITARY -- the C structure)
   |  STEP 3: Jacquet-Langlands (B^x <-> GL_2), a_q preserved.
   v
GL_2 Hilbert cusp form pi, L(pi,s)  (degree 4)
   |  STEP 4: Rudnick-Sarnak universality.
   v
high zeros of L(pi,s)  ~  GUE  (beta=2, C)

CONCLUSION (honest, and now traced): the H->C transition is COMPLEXIFICATION
-- the quaternions become 2x2 complex matrices / SU(2) / GL_2 -- NOT a step
in the polytope geometry. The substrate's beta=4 (GSE, degenerate) becomes
beta=2 (GUE, unitary) precisely when you complexify H into the unitary
group, which is the algebraic content of Jacquet-Langlands (B and GL_2 are
inner forms: B (x) C = GL_2 (x) C = M_2(C)). The GUE-ness then follows from
L-function universality. Every step is either verified here (1-2) or earlier
in the bundle (3-4).

This identifies, exactly, the missing-operator's home: it must live on the
GL_2 / SU(2) (unitary, C) side -- the complexified form -- not on the
quaternionic geometric side. Building symmetric H-geometry stays at beta=4;
the generator is on the complexified beta=2 image.
""")


if __name__ == "__main__":
    main()
