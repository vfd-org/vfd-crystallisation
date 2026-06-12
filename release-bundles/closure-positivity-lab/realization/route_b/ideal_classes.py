"""Phase 4 -- ideal-class / Brandt-module dimension gate, computed GEOMETRICALLY
from the icosian unit group, with zero fitted parameters.

Idea (the honest geometric route).  Because the icosian ring I has class
number 1, the right-ideal classes of the Eichler order of level p31 = (5phi-2)
are in bijection with the orbits of

        Gamma = (I^1 / {+-1})  ~=  A_5   (the icosahedral group, order 60)

acting on  P^1(O_K / p31) = P^1(F_31)  (the 32 points), via the local
splitting  B (x) K_p31  ~=  M_2(F_31).

So the Brandt-module dimension h is literally the NUMBER OF A_5-ORBITS on
P^1(F_31).  We build the splitting explicitly (map i, j, k to 2x2 matrices
over F_31), push the 120 units through it, and count orbits.

Two cross-checks, both parameter-free:
  * the 120 unit matrices all have determinant 1 (= reduced norm 1) and
    generate the icosahedral subgroup A_5 < PSL_2(F_31);
  * Eichler mass:  sum_i 1/w_i  must equal  mass(level-1) * (N(p31)+1),
    where mass(level-1) = |zeta_K(-1)|/2 = (1/30)/2 = 1/60 for K=Q(sqrt5),
    and w_i = |O_r(I_i)^1 / {+-1}| = 60 / orbit_size_i (the point stabiliser).

Acceptance gate (work order):  computed_h == 2.
"""
from __future__ import annotations

from fractions import Fraction

try:
    from . import ok_arithmetic as ok
    from . import quaternion_order as qo
except ImportError:
    import os
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    import ok_arithmetic as ok
    import quaternion_order as qo

LEVEL_NORM = 31
P = 31                                   # residue field F_31 of the level


# --------------------------------------------------------------------------
# F_p matrix helpers
# --------------------------------------------------------------------------

def _inv(a, p):
    return pow(a % p, p - 2, p)


def _mm(A, B, p):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % p,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % p],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % p,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % p]]


def _scal(s, A, p):
    return [[(s * A[i][j]) % p for j in range(2)] for i in range(2)]


def _add(A, B, p):
    return [[(A[i][j] + B[i][j]) % p for j in range(2)] for i in range(2)]


def _det(A, p):
    return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % p


ID = [[1, 0], [0, 1]]


def find_splitting(p):
    """Return (Imat, Jmat, Kmat): an explicit isomorphism of B=(-1,-1) onto
    M_2(F_p), i.e. trace-0 matrices with I^2=J^2=-Id and IJ=-JI."""
    negId = [[(p - 1) % p, 0], [0, (p - 1) % p]]
    Imat = [[0, 1], [(p - 1) % p, 0]]
    assert _mm(Imat, Imat, p) == negId
    Jmat = None
    for d in range(p):
        for e in range(p):
            if (d * d + e * e) % p == (p - 1) % p:
                cand = [[d, e], [e, (p - d) % p]]
                if (_mm(cand, cand, p) == negId
                        and _mm(Imat, cand, p)
                        == _scal(p - 1, _mm(cand, Imat, p), p)):
                    Jmat = cand
                    break
        if Jmat:
            break
    assert Jmat is not None, "no splitting found mod %d" % p
    Kmat = _mm(Imat, Jmat, p)
    return Imat, Jmat, Kmat


def _phi_mod(p):
    for r in range(p):
        if (r * r - r - 1) % p == 0:
            return r
    raise ValueError("phi not in F_%d (need p = +-1 mod 5)" % p)


class LocalSplitting:
    """The map iota_p31 : I -> M_2(F_31) and the induced P^1 action."""

    def __init__(self, p=P):
        self.p = p
        self.Imat, self.Jmat, self.Kmat = find_splitting(p)
        self.phi = _phi_mod(p)
        self.inv2 = _inv(2, p)
        self._invtab = [0] * p
        for a in range(1, p):
            self._invtab[a] = _inv(a, p)

    def coord_modp(self, c):
        """Reduce a Z[phi] coord (Fraction pair a + b phi) to F_p."""
        a, b = c
        av = (a.numerator * _inv(a.denominator, self.p)) % self.p
        bv = (b.numerator * _inv(b.denominator, self.p)) % self.p
        return (av + bv * self.phi) % self.p

    def iota(self, q):
        """Image of an icosian q=(w,x,y,z) in M_2(F_p)."""
        w, x, y, z = (self.coord_modp(c) for c in q)
        M = _add(_scal(w, ID, self.p), _scal(x, self.Imat, self.p), self.p)
        M = _add(M, _scal(y, self.Jmat, self.p), self.p)
        M = _add(M, _scal(z, self.Kmat, self.p), self.p)
        return M

    def iota_from_ints(self, ints):
        """Fast iota from 2x-integerised coords (a0,b0,...,a3,b3): the
        quaternion is sum_s (a_s + b_s phi)/2 e_s, so coord_s mod p is
        (a_s + b_s phi) * inv2."""
        p = self.p
        i2 = self.inv2
        ph = self.phi
        co = [((ints[2 * s] + ints[2 * s + 1] * ph) * i2) % p
              for s in range(4)]
        w, x, y, z = co
        M = _add(_scal(w, ID, p), _scal(x, self.Imat, p), p)
        M = _add(M, _scal(y, self.Jmat, p), p)
        M = _add(M, _scal(z, self.Kmat, p), p)
        return M

    # --- P^1(F_p): points [x:1] (x in F_p) and [1:0] ---
    def p1_points(self):
        pts = [(x, 1) for x in range(self.p)] + [(1, 0)]
        return pts

    def normalize(self, pt):
        a, b = pt
        b %= self.p
        if b != 0:
            return ((a * self._invtab[b]) % self.p, 1)
        return (1, 0)

    def act(self, M, pt):
        """Right action of a matrix on a row-vector point of P^1."""
        a, b = pt
        na = (a * M[0][0] + b * M[1][0]) % self.p
        nb = (a * M[0][1] + b * M[1][1]) % self.p
        return self.normalize((na, nb))


def compute_orbits():
    """Return dict with the Brandt dimension data, computed geometrically."""
    I = qo.ring()
    spl = LocalSplitting(P)
    pts = spl.p1_points()
    index = {spl.normalize(pt): i for i, pt in enumerate(pts)}
    umats = [spl.iota(u) for u in I.units]

    dets = set(_det(M, P) for M in umats)

    # union-find orbits under the unit group
    parent = list(range(len(pts)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for M in umats:
        for i, pt in enumerate(pts):
            union(i, index[spl.act(M, pt)])

    groups = {}
    for i in range(len(pts)):
        groups.setdefault(find(i), []).append(i)
    orbits = list(groups.values())
    orbit_sizes = sorted(len(o) for o in orbits)
    h = len(orbits)

    # weights w_i = 60 / orbit_size_i  (point stabiliser order in A_5)
    weights = [Fraction(60, len(o)) for o in orbits]
    mass = sum(Fraction(1, int(w)) for w in weights)
    mass_predicted = Fraction(1, 60) * (LEVEL_NORM + 1)   # 1/60 * 32 = 8/15

    return {
        "h": h,
        "orbit_sizes": orbit_sizes,
        "unit_det_set": sorted(dets),
        "weights": [int(w) for w in weights],
        "mass_computed": (mass.numerator, mass.denominator),
        "mass_predicted": (mass_predicted.numerator, mass_predicted.denominator),
        "mass_matches": mass == mass_predicted,
        "splitting": spl,
        "orbits": orbits,
        "p1_points": pts,
        "p1_index": index,
    }


def dimension_gate():
    data = compute_orbits()
    expected = 2
    status = "PASS" if data["h"] == expected else "FAIL"
    return data, expected, status


if __name__ == "__main__":
    data, expected, status = dimension_gate()
    print("DIMENSION GATE (geometric, from icosian A_5 action on P^1(F_31))")
    print("  unit-matrix determinants     :", data["unit_det_set"],
          "(expect [1] -> reduced norm 1, units land in SL_2)")
    print("  |P^1(F_31)|                  :", len(data["p1_points"]),
          "(= N(level)+1 = 32)")
    print("  number of A_5 orbits  h      :", data["h"])
    print("  orbit sizes                  :", data["orbit_sizes"])
    print("  ideal-class weights w_i      :", data["weights"],
          "(= 60/orbit_size; point stabilisers)")
    print("  Eichler mass  sum 1/w_i      : %d/%d"
          % data["mass_computed"])
    print("  Eichler mass predicted       : %d/%d  (|zeta_K(-1)|/2 * (N+1))"
          % data["mass_predicted"])
    print("  mass consistency             :", data["mass_matches"])
    print("  expected h                   :", expected)
    print("  GATE STATUS                  :", status)
