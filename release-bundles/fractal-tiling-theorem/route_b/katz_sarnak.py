"""Tier-1 step 2: the Katz-Sarnak symmetry type of the substrate L-function.

Two DIFFERENT statistics, both real, often confused:

  BULK (high zeros of ONE L-function):  always GUE = Unitary, for any fixed
        automorphic L-function (Montgomery / Rudnick-Sarnak). We verified
        this (quantum_chaos_test: level repulsion, <r>~0.62).

  FAMILY (low-lying zeros across a FAMILY): the Katz-Sarnak symmetry type
        -- Unitary (U), Orthogonal (O), or Symplectic (Sp) -- a property of
        the FAMILY's monodromy, governing the lowest zeros near s=1/2.

So 'the symmetry type' is a family question. We classify the natural family
of our object and verify what the data settles.

Discriminator (computable from our a_q):
  * a_q complex / not self-dual  -> Unitary (U)
  * a_q real / self-dual         -> Orthogonal (O) or Symplectic (Sp)
       - root numbers VARY in the family (can be +-1)  -> Orthogonal
       - root numbers all forced +1                    -> Symplectic
  weight-2 GL_2 cusp forms / elliptic curves: ORTHOGONAL (Iwaniec-Luo-
  Sarnak), split O+ / O- by the functional-equation sign.

Katz-Sarnak types are the three classical compact groups = the SAME ℝℂℍ
trichotomy as Dyson:  O <-> ℝ,  U <-> ℂ,  Sp <-> ℍ.
"""
from __future__ import annotations

import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"


def load_aq():
    rows = []
    with open(DATA / "genuine_newform_eigenvalues.csv") as f:
        for r in csv.DictReader(f):
            if r["status"] == "good":
                rows.append((int(r["norm_NP"]), r["kind"], int(r["a_P"])))
    return rows


def main():
    print("=" * 74)
    print("KATZ-SARNAK SYMMETRY TYPE of the substrate L-function")
    print("=" * 74)

    aq = load_aq()
    print(f"\nLoaded {len(aq)} Hecke eigenvalues a_q (norm <= 200).")

    # 1) self-duality: are all a_q real?  (they are integers here)
    all_real_int = all(isinstance(a, int) for _, _, a in aq)
    print(f"\n[1] Self-duality discriminator:")
    print(f"    all a_q real integers: {all_real_int}")
    print(f"    -> L-function is SELF-DUAL -> symmetry type is O or Sp "
          f"(NOT Unitary U).")
    print(f"    (sample a_q: {[a for _,_,a in aq[:8]]})")

    # 2) O vs Sp: does the root number vary across the family?
    print(f"\n[2] Orthogonal vs Symplectic:")
    print(f"    Our object is a weight-2 GL_2 cusp form / elliptic curve")
    print(f"    over Q(sqrt5).  Such families have root numbers that VARY")
    print(f"    (+-1) across twists  ->  ORTHOGONAL symmetry (Iwaniec-Luo-")
    print(f"    Sarnak; Katz-Sarnak).  [Symplectic would need all signs +1,")
    print(f"    as for quadratic-character or symmetric-square families.]")

    # 3) which orthogonal piece (O+ / O-): the functional-equation sign
    print(f"\n[3] O+ or O-?  Set by the functional-equation sign (root number):")
    print(f"    curve 31.1-a over Q(sqrt5) has analytic rank 0 (LMFDB)")
    print(f"    -> even functional equation, sign +1 -> O+ (SO-even).")

    print("\n" + "=" * 74)
    print("CLASSIFICATION")
    print("=" * 74)
    print("""
  FAMILY symmetry type : ORTHOGONAL  (specifically O+ / SO-even)
  BULK zero statistics : UNITARY / GUE  (verified: quantum_chaos_test)

Both are correct and not contradictory: the high zeros of any single
L-function are GUE (unitary); the low-lying zeros of its FAMILY are
orthogonal.

THE THREE-ALGEBRA PICTURE (full ℝℂℍ trichotomy, three roles):
  * substrate algebra        :  ℍ   (quaternionic icosian ring, Dyson β=4)
  * bulk zero statistics     :  ℂ   (Unitary / GUE, β=2)   [verified]
  * family symmetry type     :  ℝ   (Orthogonal / O, β=1)  [self-dual, here]

So all three division algebras appear, in three distinct roles. The object
is ℍ-built, has ℂ (unitary) bulk zeros, and sits in an ℝ (orthogonal)
family.  The missing self-adjoint operator lives on the ℂ/unitary (GL_2)
side (JACQUET_LANGLANDS.md); the ℝ/orthogonal type is the family-symmetry,
a different statistic.

HONEST STATUS
  * Self-duality (-> O or Sp, not U): VERIFIED from the data (a_q real).
  * Orthogonal (not Sp) and O+ (rank 0): THEOREM-grade classification
    (ILS / Katz-Sarnak) + the known rank.  A full NUMERICAL confirmation
    would require the one-level density over a family of quadratic twists
    (zeros of many L-functions) -- a larger computation, not done here.
  * Bulk GUE: verified earlier.
""")


if __name__ == "__main__":
    main()
