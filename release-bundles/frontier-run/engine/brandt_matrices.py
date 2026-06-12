"""Phase 5/6 -- Brandt matrices B(P) and the cuspidal-channel extraction,
built ONLY from icosian geometry (no elliptic-curve / modular data).

Construction (definite method, class number 1).  For a Hecke prime P (with
totally-positive generator varpi_P, P not dividing the level), enumerate the
120*(N(P)+1) icosians of reduced norm varpi_P, push each through the level
splitting iota_31, and accumulate the induced correspondence on the two
A_5-orbits of P^1(F_31):

    S[I][J] = #{ (gamma, v) : nrd(gamma)=varpi_P, v in orbit_I,
                              v * iota_31(gamma) in orbit_J }
    B(P)[I][J] = S[I][J] / (120 * |orbit_I|)          # orbit-averaged

Four INTRINSIC invariants are checked, NONE of which references the arithmetic
target -- they certify B(P) is a genuine self-adjoint Hecke operator before any
comparison is made:

  (E)  row sums  sum_J B[I][J] = N(P)+1        -- the Eisenstein/degree channel
  (Z)  integrality  B[I][J] in Z
  (S)  self-adjointness in the natural (orbit-size) measure mu_I = |orbit_I|:
            mu_I B[I][J] = mu_J B[J][I]
       (the Brandt/Hecke operator is self-adjoint for the mass inner product;
        the counting measure on P^1 pushes to the orbit sizes mu = (20, 12))
  (C)  the cuspidal eigenvector (the non-Eisenstein eigenvector) is the SAME
       vector for every prime P  ->  a genuine simultaneous Hecke eigenform.

The cuspidal eigenvalue is  a_P = trace(B(P)) - (N(P)+1)  (the eigenvalue on
the cuspidal eigenvector; the Eisenstein eigenvalue N(P)+1 sits on (1,...,1)).

RESULT (see WORK_ORDER_RESULT.md).  All four invariants hold for every prime.
B(P) is self-adjoint in mu = (20,12); the cuspidal eigenvector is the fixed
vector (3, -5) (orthogonal to Eisenstein (1,1) under mu: 20*3 - 12*5 = 0); and
the cuspidal eigenvalue equals the brute-force point-counted a_P, exactly,
out-of-sample, with zero fitting -- at split primes up to the global Galois
involution of Q(sqrt5) (which permutes the two primes above p), and EXACTLY at
the Galois-fixed inert/ramified primes.  So the icosian geometry encodes the
cuspidal arithmetic object.  This is NOT a proof of RH: the positivity /
trace-form wall is untouched (see WORK_ORDER_RESULT.md, "what this does NOT do").
"""
from __future__ import annotations

from fractions import Fraction

try:
    from . import ok_arithmetic as ok
    from . import quaternion_order as qo
    from . import ideal_classes as ic
except ImportError:
    import os
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    import ok_arithmetic as ok
    import quaternion_order as qo
    import ideal_classes as ic


def totally_positive_generator(target_norm, search=60):
    """A totally-positive a+b phi with absolute norm = target_norm, or None."""
    best = None
    for a in range(-search, search + 1):
        for b in range(-search, search + 1):
            e = (a, b)
            if abs(ok.norm(e)) == target_norm and ok.is_totally_positive(e):
                # prefer the smallest-trace generator (deterministic choice)
                t = ok.trace(e)
                if best is None or t < best[0]:
                    best = (t, e)
    return best[1] if best else None


class BrandtEngine:
    def __init__(self):
        self.ring = qo.ring()
        self.gate = ic.compute_orbits()
        self.spl = self.gate["splitting"]
        self.orbits = self.gate["orbits"]
        self.h = self.gate["h"]
        self.weights = self.gate["weights"]          # w_i = 60/orbit_size
        # natural self-adjointness measure: the orbit sizes (counting measure
        # on P^1 pushed to the classes).  mu = (20, 12) here.
        self.mu = [len(o) for o in self.orbits]
        self.pts = self.gate["p1_points"]
        self.index = self.gate["p1_index"]
        # orbit id of each P^1 point
        self.orbit_of = [None] * len(self.pts)
        for oi, o in enumerate(self.orbits):
            for i in o:
                self.orbit_of[i] = oi

    def brandt_matrix(self, varpi):
        """Candidate Brandt matrix B(P) (rational h x h) and invariants."""
        Np = abs(ok.norm(varpi))
        vecs = self.ring.enumerate_reduced_norm_vecs(varpi)
        assert len(vecs) == 120 * (Np + 1), \
            "norm-element count %d != 120*(N+1)=%d" % (len(vecs),
                                                       120 * (Np + 1))
        # group elements by their reduction image mod p31 (a GL_2(F_31) matrix);
        # each distinct image acts the same way on P^1, so accumulate once.
        img_count = {}
        for ints in vecs:
            M = self.spl.iota_from_ints(ints)
            key = (M[0][0], M[0][1], M[1][0], M[1][1])
            img_count[key] = img_count.get(key, 0) + 1
        S = [[0] * self.h for _ in range(self.h)]
        for key, mult in img_count.items():
            M = [[key[0], key[1]], [key[2], key[3]]]
            for i, v in enumerate(self.pts):
                I = self.orbit_of[i]
                J = self.orbit_of[self.index[self.spl.act(M, v)]]
                S[I][J] += mult
        B = [[Fraction(S[I][J], 120 * len(self.orbits[I]))
              for J in range(self.h)] for I in range(self.h)]
        # invariants
        row_sums = [sum(B[I]) for I in range(self.h)]
        eisenstein_ok = all(r == Np + 1 for r in row_sums)
        integral = all(B[I][J].denominator == 1
                       for I in range(self.h) for J in range(self.h))
        mu = self.mu
        self_adjoint = all(mu[I] * B[I][J] == mu[J] * B[J][I]
                           for I in range(self.h) for J in range(self.h))
        trace = sum(B[I][I] for I in range(self.h))
        cuspidal = trace - (Np + 1)
        cusp_vec = self._cuspidal_eigenvector(B, cuspidal)
        return {
            "norm": Np,
            "varpi": varpi,
            "matrix": [[B[I][J] for J in range(self.h)] for I in range(self.h)],
            "row_sums": row_sums,
            "eisenstein_ok": eisenstein_ok,
            "integral": integral,
            "self_adjoint": self_adjoint,
            "measure_mu": list(mu),
            "cuspidal_eigenvector": cusp_vec,
            "eisenstein_eigenvalue": Np + 1,
            "cuspidal_eigenvalue": (cuspidal.numerator
                                    if cuspidal.denominator == 1
                                    else float(cuspidal)),
            # back-compat alias
            "cuspidal_candidate": (cuspidal.numerator
                                   if cuspidal.denominator == 1
                                   else float(cuspidal)),
        }

    def _cuspidal_eigenvector(self, B, eigval):
        """Integer cuspidal eigenvector of the 2x2 B (non-Eisenstein)."""
        from math import gcd
        if self.h != 2:
            return None
        a = B[0][0] - eigval
        b = B[0][1]
        # (B - eigval I) v = 0  ->  v = (b, -a)
        L = b.denominator * a.denominator // gcd(b.denominator, a.denominator)
        x0 = int(b * L)
        x1 = int(-a * L)
        g = gcd(abs(x0), abs(x1)) or 1
        x0 //= g
        x1 //= g
        if x0 < 0 or (x0 == 0 and x1 < 0):
            x0, x1 = -x0, -x1
        return (x0, x1)


if __name__ == "__main__":
    eng = BrandtEngine()
    print("Brandt matrices B(P) from icosian geometry  (mu = %s)" % eng.mu)
    print("(intrinsic invariants only -- no arithmetic target used)\n")
    print("  N(P)  matrix                rowsum  int  self-adj  cusp-eigvec"
          "  a_P")
    print("  " + "-" * 72)
    all_sa = True
    vecs = set()
    for Np in [11, 19, 29, 41, 59, 61, 71, 199]:
        varpi = totally_positive_generator(Np)
        if varpi is None:
            continue
        r = eng.brandt_matrix(varpi)
        mat = [[str(x) for x in row] for row in r["matrix"]]
        all_sa = all_sa and r["self_adjoint"]
        vecs.add(r["cuspidal_eigenvector"])
        print("  %3d   %-20s  %-6s  %-3s  %-8s  %-11s  %s"
              % (Np, mat, r["eisenstein_ok"], r["integral"],
                 r["self_adjoint"], r["cuspidal_eigenvector"],
                 r["cuspidal_eigenvalue"]))
    print("\n  Eisenstein channel exact (rowsum=N+1) on all primes: structural.")
    print("  All B(P) self-adjoint in measure mu =", eng.mu, ":", all_sa)
    print("  Common cuspidal eigenvector across all primes:", vecs,
          "->", "genuine simultaneous Hecke eigenform"
          if len(vecs) == 1 else "NOT common")
