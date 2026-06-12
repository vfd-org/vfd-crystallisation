"""The critical line ON the tiling: Satake parameters and the local zeros.

The user's reframe: stop chasing the global zeros; look for the critical
line realised geometrically on the closure/tiling itself, with primes
'passing energy to the next cell'.

This is CORRECT for the LOCAL critical line, and it is exactly what the
icosian closure realises.  For each prime q, the substrate's Hecke
eigenvalue a_q determines the Satake parameters

    alpha_q, alpha_q-bar  with  a_q = alpha_q + alpha_q-bar.

Ramanujan/temperedness (which the closure enforces -- verified: every a_q
satisfies |a_q| <= 2 sqrt(N(q))) says

    |alpha_q| = sqrt(N(q)),     i.e.  alpha_q = sqrt(N(q)) e^{i theta_q}

so the Satake parameters lie EXACTLY on the circle of radius sqrt(N(q)).
Equivalently, the local L-factor

    L_q(s)^{-1} = 1 - a_q N(q)^{-s} + N(q)^{1-2s} = (1-alpha z)(1-alpha-bar z),
    z = N(q)^{-s}

has its zeros at |z| = 1/sqrt(N(q)), i.e. N(q)^{-Re s} = N(q)^{-1/2}, i.e.

    Re(s) = 1/2     EXACTLY.

So: every local factor's zeros sit on the critical line Re(s)=1/2, and this
is the closure/tiling realising the critical line geometrically -- the
'critical circle' per prime.  The Sato-Tate angle theta_q is the position
on that circle; the Hecke operators (primes passing energy between cells)
move along it.

This is the geometric/LOCAL Riemann Hypothesis -- the number-field analogue
of the function-field RH that Deligne PROVED geometrically (Frobenius
eigenvalues on |alpha|=sqrt(q) via cohomology).  The substrate realises it
honestly.

THE GAP (honest): the GLOBAL zeros of the product L(s) = prod_q L_q(s) are
NOT forced onto Re(s)=1/2 by the local zeros being there.  Local->global
is exactly the transfer that works in Deligne's geometric (function-field)
world and has NO known number-field analogue.  That gap is RH.
"""
from __future__ import annotations

import math

# substrate-computed eigenvalues (route_b/step3_4_hecke.py), N(q) <= 41
DATA = [
    ("(2)", 4, -3), ("(sqrt5)", 5, -2), ("(3)", 9, 2),
    ("(11)a", 11, -4), ("(11)b", 11, 4),
    ("(19)a", 19, 4), ("(19)b", 19, -4),
    ("(29)a", 29, -2), ("(29)b", 29, -2),
    ("(41)a", 41, -6), ("(41)b", 41, -6),
]


def main():
    print("=" * 74)
    print("THE CRITICAL LINE ON THE TILING: Satake circle per prime")
    print("=" * 74)
    print("\n  prime     N(q)  a_q   x=a/2sqrtN  theta_q(deg)  |alpha|   "
          "local zero Re(s)")
    print("  " + "-" * 68)
    all_on = True
    for label, N, a in DATA:
        x = a / (2 * math.sqrt(N))
        theta = math.degrees(math.acos(x))
        alpha_mod = math.sqrt(N)              # |alpha| = sqrt(N) by Ramanujan
        # local zero: N^{-Re s} = 1/sqrt(N)  ->  Re s = 1/2
        re_s = 0.5
        on = abs(x) < 1.0                     # strict temperedness
        all_on = all_on and on
        print(f"  {label:<9} {N:<5} {a:<5} {x:<11.4f} {theta:<13.2f} "
              f"{alpha_mod:<9.4f} {re_s:.4f}")

    print("\n" + "=" * 74)
    print(f"  Every Satake parameter on its circle |alpha|=sqrt(N(q)): "
          f"{'YES' if all_on else 'NO'}")
    print(f"  => every LOCAL L-factor has its zeros EXACTLY on Re(s)=1/2.")
    print(f"  This is the closure/tiling realising the critical line")
    print(f"  geometrically (the Satake/temperedness circle).")
    print("=" * 74)
    print("""
WHAT THIS MEANS (the honest reframe)

  RIGHT (your intuition): there IS a critical line on the tiling itself.
  It is the per-prime Satake circle |alpha_q| = sqrt(N(q)).  The closure
  keeps the Hecke eigenvalues on it (Ramanujan), and the Hecke operators
  -- primes passing energy from cell to cell -- move the angle theta_q
  along that circle.  Each local factor's zeros lie on Re(s)=1/2 EXACTLY.
  This is a genuine geometric/LOCAL Riemann Hypothesis, and the substrate
  realises it.  It is the number-field shadow of the function-field RH
  that Deligne proved by geometry (Frobenius weights, |alpha|=sqrt q).

  THE REMAINING GAP: the GLOBAL zeros of L(s) = prod_q L_q(s) are a
  property of the whole product, and are NOT pinned to Re(s)=1/2 just
  because each factor's local zeros are.  Local-on-the-line does not imply
  global-on-the-line.  In Deligne's geometric world the transfer exists
  (the cohomology of a variety over a finite field IS the global object,
  and its weights give RH).  For number fields there is NO known geometry
  that performs this transfer -- and the icosian closure, which is a
  quaternionic LATTICE object rather than the cohomology of a variety,
  does not supply one either.

  So the reframe is genuinely better: the substrate does NOT fail to reach
  'a' critical line -- it fully realises the LOCAL/geometric one.  What is
  missing is the local->global transfer, which is the real content of RH
  and is open for everyone.  The substrate has put us in exactly the
  function-field picture; it has not provided the number-field bridge,
  because none is known.
""")


if __name__ == "__main__":
    main()
