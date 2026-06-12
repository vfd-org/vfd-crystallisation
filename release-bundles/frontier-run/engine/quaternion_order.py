"""Phase 3 -- the icosian quaternion order over O_K = Z[phi], native.

B = (-1, -1 / K),  K = Q(sqrt 5), the definite quaternion algebra ramified
at exactly the two real places.  Its maximal order is the *icosian ring* I;
its 120 reduced-norm-1 units are the vertices of the 600-cell (= 2I, the
binary icosahedral group).  Class number h(I) = 1.

This module is the substrate's OWN arithmetic.  NO modular / elliptic-curve
data is injected anywhere.  It provides

  * quaternion multiplication and reduced norm over K  (Fraction-exact),
  * the 120 unit icosians,
  * a rank-8 Z-basis of the icosian ring (HNF),
  * the integral, even trace-form Gram matrix  M  (det = 5^4 = 625),
  * a COMPLETE enumerator of icosians of a given totally-positive reduced
    norm varpi, via Fincke-Pohst short-vector enumeration.

Correctness anchor (parameter-free, no target data):
    #{ x in I : nrd(x) = varpi_P } = 120 * (N(P) + 1)
for a totally-positive prime element varpi_P.  This is the icosian analogue
of the Hurwitz identity #{nrd = p} = 24(p+1); it is the Eisenstein theta
coefficient and is checked in tests/.  It validates the enumerator with no
reference to the cuspidal target.
"""
from __future__ import annotations

import itertools
import math
from fractions import Fraction

try:
    from . import ok_arithmetic as ok
except ImportError:                       # run as a plain script
    import os
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    import ok_arithmetic as ok


# --------------------------------------------------------------------------
# quaternions over K:  q = (w, x, y, z), each coord a Z[phi] element stored
# as a pair of Fractions (a, b) meaning a + b phi.   B = (-1,-1): i^2=j^2=-1.
# --------------------------------------------------------------------------

def _km(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def _ka(x, y):
    return (x[0] + y[0], x[1] + y[1])


def _ks(x, y):
    return (x[0] - y[0], x[1] - y[1])


ZERO = (Fraction(0), Fraction(0))


def qmul(P, Q):
    w1, x1, y1, z1 = P
    w2, x2, y2, z2 = Q
    w = _ks(_ks(_ks(_km(w1, w2), _km(x1, x2)), _km(y1, y2)), _km(z1, z2))
    x = _ka(_ka(_ka(_km(w1, x2), _km(x1, w2)), _km(y1, z2)),
            _ks(ZERO, _km(z1, y2)))
    y = _ka(_ka(_ka(_km(w1, y2), _ks(ZERO, _km(x1, z2))), _km(y1, w2)),
            _km(z1, x2))
    z = _ka(_ka(_ka(_km(w1, z2), _km(x1, y2)), _ks(ZERO, _km(y1, x2))),
            _km(z1, w2))
    return (w, x, y, z)


def qnrd(P):
    """Reduced norm w^2 + x^2 + y^2 + z^2, returned as a Z[phi] pair."""
    w, x, y, z = P
    return _ka(_ka(_km(w, w), _km(x, x)), _ka(_km(y, y), _km(z, z)))


def qnrd_int(P):
    """Reduced norm as an integer pair (a, b); raises if not integral."""
    n = qnrd(P)
    a, b = n
    assert a.denominator == 1 and b.denominator == 1, "nrd not integral"
    return (int(a), int(b))


# --------------------------------------------------------------------------
# the 120 unit icosians (vertices of the 600-cell)
# --------------------------------------------------------------------------

def _F(a, b=0):
    return (Fraction(a), Fraction(b))


_PHI = _F(0, 1)
_INV_PHI = _F(-1, 1)          # 1/phi = phi - 1


def _even_perm(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s == 1


def unit_icosians():
    units = []
    half = Fraction(1, 2)
    for i in range(4):                        # 8: (+-1,0,0,0) & perms
        for s in (1, -1):
            q = [_F(0)] * 4
            q[i] = _F(s)
            units.append(tuple(q))
    for signs in itertools.product((1, -1), repeat=4):   # 16: (+-1.../2)
        units.append(tuple((Fraction(s) * half, Fraction(0)) for s in signs))
    base = [_F(0), _F(1), _INV_PHI, _PHI]                 # 96: even perms
    seen = set()
    for perm in itertools.permutations(range(4)):
        if not _even_perm(perm):
            continue
        for signs in itertools.product((1, -1), repeat=4):
            q = []
            for slot in range(4):
                a, b = base[perm[slot]]
                q.append((Fraction(signs[slot]) * a * half,
                          Fraction(signs[slot]) * b * half))
            key = tuple((c[0], c[1]) for c in q)
            if key in seen:
                continue
            seen.add(key)
            units.append(tuple(q))
    return units


# --------------------------------------------------------------------------
# rank-8 Z-basis of the icosian ring + trace-form Gram
# --------------------------------------------------------------------------

def _quat_to_vec8(q):
    out = []
    for c in q:
        out += [c[0], c[1]]            # Fractions
    return out


def _hnf_basis(rows):
    """Row-HNF of integer rows; return the nonzero basis rows.  Pure
    integer column-pivot reduction (deterministic, exact)."""
    M = [list(r) for r in rows]
    ncol = len(M[0])
    basis = []
    used = [False] * len(M)
    col = 0
    work = [r[:] for r in M]
    pivots = []
    r = 0
    # Gaussian elimination over Z to HNF-like echelon (sufficient for a basis)
    rowset = [list(map(int, x)) for x in work]
    # iterative gcd pivoting per column
    active = list(range(len(rowset)))
    result = []
    c = 0
    while c < ncol and active:
        nz = [i for i in active if rowset[i][c] != 0]
        if not nz:
            c += 1
            continue
        while len(nz) > 1:
            nz.sort(key=lambda i: abs(rowset[i][c]))
            piv = nz[0]
            for i in nz[1:]:
                q = rowset[i][c] // rowset[piv][c]
                if q:
                    rowset[i] = [rowset[i][k] - q * rowset[piv][k]
                                 for k in range(ncol)]
            nz = [i for i in active if rowset[i][c] != 0]
        piv = nz[0]
        if rowset[piv][c] < 0:
            rowset[piv] = [-v for v in rowset[piv]]
        result.append(rowset[piv][:])
        active.remove(piv)
        c += 1
    return result


class IcosianRing:
    def __init__(self):
        self.units = unit_icosians()
        assert len(self.units) == 120
        # generators: units and phi*units, integerised by x2
        gens = []
        for u in self.units:
            gens.append(u)
            gens.append(qmul((_PHI, _F(0), _F(0), _F(0)), u))
        rows = []
        for g in gens:
            v = _quat_to_vec8(g)
            rows.append([int(c * 2) for c in v])
        H = _hnf_basis(rows)
        assert len(H) == 8, "icosian ring is not rank 8: %d" % len(H)
        # H[k] is the k-th basis quaternion in 2x-integerised coords:
        # H[k] = (a0,b0,a1,b1,a2,b2,a3,b3),  quaternion = sum_s (a_s + b_s phi)/2 e_s.
        self.H = [tuple(int(c) for c in row) for row in H]
        # basis quaternions (divide the x2 integerisation back) -- exact, for tests
        self.basis = [self._vec8_to_quat([Fraction(c, 2) for c in row])
                      for row in H]
        self.gram = self._trace_gram()         # integral even Gram M
        self._chol = None

    @staticmethod
    def _vec8_to_quat(v):
        return tuple((v[2 * s], v[2 * s + 1]) for s in range(4))

    def _tr_nrd(self, q):
        n = qnrd(q)
        return ok.trace((n[0], n[1]))          # Tr_{K/Q}(nrd); rational

    def _trace_gram(self):
        n = len(self.basis)
        M = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    M[i][j] = int(2 * self._tr_nrd(self.basis[i]))
                else:
                    s = tuple(_ka(self.basis[i][t], self.basis[j][t])
                              for t in range(4))
                    val = (self._tr_nrd(s) - self._tr_nrd(self.basis[i])
                           - self._tr_nrd(self.basis[j]))
                    M[i][j] = int(val)
        return M

    def gram_det(self):
        import numpy as np
        return round(float(np.linalg.det(np.array(self.gram, float))))

    def coeffs_to_quat(self, c):
        qq = [ZERO, ZERO, ZERO, ZERO]
        for k in range(8):
            ck = c[k]
            if ck == 0:
                continue
            bk = self.basis[k]
            qq = [_ka(qq[t], (bk[t][0] * ck, bk[t][1] * ck)) for t in range(4)]
        return tuple(qq)

    # ----- complete short-vector enumeration (Fincke-Pohst) ---------------
    def _cholesky(self):
        if self._chol is not None:
            return self._chol
        import numpy as np
        # Q(c) = (1/2) c^T M c.  Use A = M/2 (positive definite) so Q=c^T A c.
        A = np.array(self.gram, float) / 2.0
        R = np.linalg.cholesky(A).T          # A = R^T R, R upper
        self._chol = R
        return R

    def enumerate_reduced_norm_vecs(self, varpi):
        """COMPLETE enumeration of icosians x in I with nrd(x) == varpi,
        returned as 2x-integerised coordinate 8-tuples (a0,b0,...,a3,b3) with
        quaternion = sum_s (a_s + b_s phi)/2 e_s.  Pure integer leaf check:
        nrd = (P + Q phi)/4,  P = sum(A_s^2+B_s^2),  Q = sum(2 A_s B_s + B_s^2),
        so the test is  P == 4 va  and  Q == 4 vb  for varpi = (va, vb)."""
        T = ok.trace(varpi)                  # target Q-value = Tr(nrd)
        if T <= 0:
            return []
        va, vb = varpi[0], varpi[1]
        fa, fb = 4 * va, 4 * vb
        R = self._cholesky()
        H = self.H
        n = 8
        sols = []
        c = [0] * n
        eps = 1e-7

        def leaf_ok():
            ints = [0] * 8
            for k in range(8):
                ck = c[k]
                if ck:
                    Hk = H[k]
                    for m in range(8):
                        ints[m] += ck * Hk[m]
            P = 0
            Q = 0
            for s in range(4):
                A = ints[2 * s]
                Bc = ints[2 * s + 1]
                P += A * A + Bc * Bc
                Q += 2 * A * Bc + Bc * Bc
            if P == fa and Q == fb:
                return tuple(ints)
            return None

        def recurse(i, remaining):
            if i < 0:
                v = leaf_ok()
                if v is not None:
                    sols.append(v)
                return
            partial = 0.0
            for j in range(i + 1, n):
                partial += R[i][j] * c[j]
            Rii = R[i][i]
            bound = math.sqrt(max(remaining, 0.0) + eps) / Rii
            center = -partial / Rii
            lo = int(math.floor(center - bound - eps))
            hi = int(math.ceil(center + bound + eps))
            for ci in range(lo, hi + 1):
                term = Rii * ci + partial
                used = term * term
                if used <= remaining + eps:
                    c[i] = ci
                    recurse(i - 1, remaining - used)
            c[i] = 0

        recurse(n - 1, float(T))
        return sols

    def enumerate_reduced_norm(self, varpi):
        """Same enumeration, returned as exact Fraction-quaternions."""
        out = []
        for ints in self.enumerate_reduced_norm_vecs(varpi):
            q = tuple((Fraction(ints[2 * s], 2), Fraction(ints[2 * s + 1], 2))
                      for s in range(4))
            out.append(q)
        return out


_RING = None


def ring():
    global _RING
    if _RING is None:
        _RING = IcosianRing()
    return _RING


if __name__ == "__main__":
    I = ring()
    print("icosian ring built: rank", len(I.basis),
          " trace-form Gram det =", I.gram_det(), "(expect 625 = 5^4)")
    # unit sanity: all 120 units have reduced norm 1
    bad = sum(1 for u in I.units if qnrd_int(u) != (1, 0))
    print("units of reduced norm 1:", 120 - bad, "/120")
    # enumerator anchor:  #{nrd = varpi_P} = 120 (N(P)+1)
    for (a, b), Np in [((3, 1), 11), ((4, 1), 19), ((5, 1), 29),
                       ((6, 1), 41), ((7, 2), 59)]:
        varpi = (a, b)
        assert ok.is_totally_positive(varpi) and abs(ok.norm(varpi)) == Np
        cnt = len(I.enumerate_reduced_norm(varpi))
        print("  N(P)=%2d  varpi=%s  #icosians(nrd=varpi)=%5d  "
              "expect 120*(N+1)=%5d  %s"
              % (Np, varpi, cnt, 120 * (Np + 1),
                 "OK" if cnt == 120 * (Np + 1) else "MISMATCH"))
