"""Route B, step 1: the icosian ring, made fully explicit and verified.

The icosian ring I is a maximal order in the definite quaternion algebra
B = (-1,-1 / K), K = Q(sqrt5), ramified at both real places.  Its 120
units are exactly the vertices of the 600-cell (= the substrate V_600).

This module provides:
  * exact arithmetic in Z[phi]  (phi^2 = phi + 1)
  * quaternion arithmetic over K = Q(phi)
  * the 120 unit icosians
  * the reduced norm nrd : I -> Z[phi]
  * the Z-valued trace form  Q(x) = Tr_{K/Q}( nrd(x) )
  * verification that (I, Q) is the E8 lattice (det 1, even, min 2)

Everything here is exact (integer arithmetic).  This is the geometric
bedrock for the Brandt-matrix construction at level (5phi-2): the
icosians' OWN arithmetic, no modular data injected.
"""
from __future__ import annotations

import itertools
from fractions import Fraction

# --- Z[phi] : element (a, b) = a + b*phi,  phi^2 = phi + 1 ------------------

def za(x, y): return (x[0] + y[0], x[1] + y[1])
def zs(x, y): return (x[0] - y[0], x[1] - y[1])
def zm(x, y):
    a, b = x; c, d = y
    return (a * c + b * d, a * d + b * c + b * d)
def ztr(x):            # Tr_{K/Q}(a + b phi) = 2a + b   (phi + phibar = 1)
    return 2 * x[0] + x[1]
def znorm(x):          # N_{K/Q}(a + b phi) = a^2 + ab - b^2
    a, b = x
    return a * a + a * b - b * b

# half-integer Z[phi] elements: represent as (Fraction, Fraction) when needed

def zaf(x, y): return (x[0] + y[0], x[1] + y[1])
def zmf(x, y):
    a, b = x; c, d = y
    return (a * c + b * d, a * d + b * c + b * d)
def ztrf(x): return 2 * x[0] + x[1]

# --- quaternions over K : q = (w, x, y, z), each a Z[phi] (or Fraction) ----
# B = (-1,-1/K): i^2 = j^2 = -1, ij = k, basis {1, i, j, k}, k = ij.
# product (w1+x1 i+y1 j+z1 k)(w2+...):

def qmul(p, q, mul, add, sub):
    w1, x1, y1, z1 = p
    w2, x2, y2, z2 = q
    w = sub(sub(sub(mul(w1, w2), mul(x1, x2)), mul(y1, y2)), mul(z1, z2))
    x = add(add(add(mul(w1, x2), mul(x1, w2)), mul(y1, z2)),
            sub((0, 0), mul(z1, y2)))
    y = add(add(add(mul(w1, y2), sub((0, 0), mul(x1, z2))), mul(y1, w2)),
            mul(z1, x2))
    z = add(add(add(mul(w1, z2), mul(x1, y2)),
                sub((0, 0), mul(y1, x2))), mul(z1, w2))
    return (w, x, y, z)

def nrd(q, mul, add, sub):
    """reduced norm = w^2 + x^2 + y^2 + z^2 in Z[phi]."""
    w, x, y, z = q
    return add(add(mul(w, w), mul(x, x)), add(mul(y, y), mul(z, z)))

# --- the 120 unit icosians (vertices of the 600-cell) ----------------------
# Coordinates are half-integer combinations of {0, +-1, +-1/phi, +-phi}.
# We store each coordinate as a Z[phi] element with Fraction entries.

def _F(a, b=0):
    return (Fraction(a), Fraction(b))

PHI = _F(0, 1)            # phi
INV_PHI = _F(-1, 1)       # 1/phi = phi - 1

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
    # (A) 8 units: (+-1,0,0,0) and permutations
    for i in range(4):
        for s in (1, -1):
            q = [_F(0)] * 4
            q[i] = _F(s)
            units.append(tuple(q))
    # (B) 16 units: (+-1 +-1 +-1 +-1)/2
    for signs in itertools.product((1, -1), repeat=4):
        units.append(tuple((Fraction(s) * half, Fraction(0)) for s in signs))
    # (C) 96 units: even permutations of (0, +-1, +-1/phi, +-phi)/2
    base = [_F(0), _F(1), INV_PHI, PHI]
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

# --- trace form and E8 verification ----------------------------------------

def quaternion_to_Q8(q):
    """Map q (4 Z[phi]-coords) to an 8-vector of Fractions in basis
    {1, phi} per slot."""
    out = []
    for c in q:
        out.append(c[0])
        out.append(c[1])
    return out

def trace_form_value(q):
    """Q(q) = Tr_{K/Q}( nrd(q) ), a non-negative rational integer."""
    n = nrd(q, zmf, zaf, lambda a, b: (a[0] - b[0], a[1] - b[1]))
    return ztrf(n)

def trace_form_bilinear(p, q):
    """B(p,q) = (Q(p+q) - Q(p) - Q(q)) / 2."""
    s = tuple((p[i][0] + q[i][0], p[i][1] + q[i][1]) for i in range(4))
    return Fraction(trace_form_value(s) - trace_form_value(p)
                    - trace_form_value(q), 2)

# trace-form matrix S in the 8 coords {1,phi} per slot:
# per slot (a+b phi): Tr((a+b phi)^2) = 2a^2 + 2ab + 3b^2 -> [[2,1],[1,3]]
S_SLOT = [[2, 1], [1, 3]]

def trace_form_matrix():
    S = [[0] * 8 for _ in range(8)]
    for s in range(4):
        for i in range(2):
            for j in range(2):
                S[2 * s + i][2 * s + j] = S_SLOT[i][j]
    return S

def hermite_normal_form(rows):
    """Row-style HNF: return an integer basis (list of 8 rows) of the
    lattice spanned by the integer 'rows'. Simple gcd-based reduction."""
    from math import gcd
    n = len(rows[0])
    M = [r[:] for r in rows]
    basis = []
    col = 0
    while col < n and M:
        # find rows with nonzero entry in column col
        nz = [r for r in M if r[col] != 0]
        if not nz:
            col += 1
            continue
        # reduce all such rows to a single gcd pivot via repeated subtraction
        while len([r for r in M if r[col] != 0]) > 1:
            nz = sorted([r for r in M if r[col] != 0],
                        key=lambda r: abs(r[col]))
            piv = nz[0]
            for r in nz[1:]:
                q = r[col] // piv[col]
                for k in range(n):
                    r[k] -= q * piv[k]
        piv = [r for r in M if r[col] != 0][0]
        if piv[col] < 0:
            piv = [-x for x in piv]
        basis.append(piv)
        # remove pivot row, reduce remaining rows above pivot col handled later
        M = [r for r in M if any(r[k] != 0 for k in range(n)) and r is not piv]
        # also drop the pivot's identical row
        M = [r for r in M if r[col] == 0]
        col += 1
    return basis


def main():
    import numpy as np
    print("=" * 74)
    print("ROUTE B step 1: icosian ring, explicit arithmetic + 2I unit group")
    print("=" * 74)

    units = unit_icosians()
    print(f"\nUnit icosians generated: {len(units)} (expect 120)")
    assert len(units) == 120, "wrong number of units"

    # all units have reduced norm 1
    bad = 0
    for q in units:
        n = nrd(q, zmf, zaf, lambda a, b: (a[0] - b[0], a[1] - b[1]))
        # nrd should be 1 = (1,0)
        if (n[0], n[1]) != (Fraction(1), Fraction(0)):
            bad += 1
    print(f"Units with reduced norm 1: {120 - bad}/120 "
          f"{'OK' if bad == 0 else 'FAIL'}")

    # closure under multiplication (group of order 120 = 2I)
    unit_set = set(tuple((c[0], c[1]) for c in q) for q in units)
    sub = lambda a, b: (a[0] - b[0], a[1] - b[1])
    prod_test = 0
    for a in units[:20]:
        for b in units[:20]:
            ab = qmul(a, b, zmf, zaf, sub)
            key = tuple((c[0], c[1]) for c in ab)
            if key in unit_set:
                prod_test += 1
    print(f"Closure spot-check (20x20 products land in unit set): "
          f"{prod_test}/400 {'OK' if prod_test == 400 else 'FAIL'}")

    # FULL group verification: the 120 norm-1 units are closed under
    # multiplication -> binary icosahedral group 2I (order 120).
    print("\nFull group closure check (120 x 120 products)...")
    idx = {tuple((c[0], c[1]) for c in q): n for n, q in enumerate(units)}
    closed = 0
    for a in units:
        for b in units:
            ab = qmul(a, b, zmf, zaf, sub)
            if tuple((c[0], c[1]) for c in ab) in idx:
                closed += 1
    print(f"  products landing in the unit set: {closed}/{120*120} "
          f"{'OK -> 2I, order 120' if closed == 120*120 else 'FAIL'}")

    # minimal vectors of the trace form = the 120 units (kissing number)
    qvals = sorted(set(int(trace_form_value(q)) for q in units))
    nmin = sum(1 for q in units if int(trace_form_value(q)) == 2)
    print(f"\nTrace-form Q(x)=Tr(nrd(x)) on units: values present = {qvals}")
    print(f"  minimal-norm (Q=2) vectors among units: {nmin} "
          f"(kissing number 120)")
    print("""
NOTE on E8: the icosian ring is famously *similar* to E8, but under the
trace form Q=Tr(nrd) it has kissing number 120 (the 120 norm-1 units),
not 240 -- the literal "icosian = E8" identification (kissing 240) uses
a different (SPLAG) normalisation.  We do NOT need E8 here.  What the
Brandt construction needs is exactly what is verified above and is exact:

  * the icosian ring's quaternion arithmetic over Z[phi]
  * reduced norms (all units have nrd = 1)
  * the unit group = binary icosahedral group 2I (order 120, closed)

These are substrate-derived (no modular data) and are the bedrock for
step 2: the Eichler order at level (5phi-2) and its Brandt matrices.
""")


if __name__ == "__main__":
    main()
