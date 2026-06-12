"""Route B, step 2: dimension at level (5phi-2) via the P^1 model.

Because the icosian ring I has class number 1, the space of quaternionic
modular forms of level p = (5phi-2) has a basis indexed by the orbits of
the unit group O^x = 2I acting on P^1(O_K / p) = P^1(F_31) (Voight,
Quaternion Algebras, Ch. 41; Dembele 2007).

  dim M(p) = number of O^x-orbits on P^1(F_31).

We compute this directly and exactly from the substrate's own arithmetic:
  1. reduce O_K = Z[phi] mod p:  phi -> 19  (the root with 5*19-2 = 0 mod 31)
  2. fix an explicit splitting  B (x) F_31 ~ M_2(F_31):
        i -> [[0,1],[-1,0]],  j -> [[5,6],[6,-5]],  k -> i j
     (i^2 = j^2 = -I, ij = -ji; det = reduced norm)
  3. reduce the 120 unit icosians to matrices in SL_2(F_31)
  4. act on the 32 points of P^1(F_31); count orbits.

ACCEPTANCE (gate G1): number of orbits == 2  (1 Eisenstein + 1 cuspidal),
which matches the genuine norm-31 newform being 1-dimensional (Route A).

This is substrate-intrinsic (no modular data) and fully verifiable.
"""
from __future__ import annotations

from fractions import Fraction

import icosian as ico

P = 31
PHI_MOD = 19          # root of x^2-x-1 mod 31 with 5*phi-2 == 0  (5*19-2=93=0)


def reduce_zphi(x):
    """Reduce a Z[phi] element (a,b)=a+b*phi (Fraction entries) to F_31."""
    a, b = x
    # entries may be half-integers; 2 is invertible mod 31
    inv2 = pow(2, P - 2, P)
    def red(fr):
        num = fr.numerator % P
        den = fr.denominator % P
        return (num * pow(den, P - 2, P)) % P
    return (red(a) + red(b) * PHI_MOD) % P


# explicit splitting B (x) F_31 -> M_2(F_31)
I2 = ((1, 0), (0, 1))
MI = ((0, 1), (P - 1, 0))            # i -> [[0,1],[-1,0]]
MJ = ((5, 6), (6, P - 5))            # j -> [[5,6],[6,-5]]


def matmul(A, B):
    return tuple(tuple(sum(A[r][k] * B[k][c] for k in range(2)) % P
                       for c in range(2)) for r in range(2))


def matadd(A, B):
    return tuple(tuple((A[r][c] + B[r][c]) % P for c in range(2))
                 for r in range(2))


def scal(s, A):
    return tuple(tuple((s * A[r][c]) % P for c in range(2)) for r in range(2))


MK = matmul(MI, MJ)                   # k = i j


def quat_to_matrix(q):
    """Reduce icosian quaternion q=(w,x,y,z) over Z[phi] to M_2(F_31)."""
    w, x, y, z = (reduce_zphi(c) for c in q)
    M = scal(w, I2)
    M = matadd(M, scal(x, MI))
    M = matadd(M, scal(y, MJ))
    M = matadd(M, scal(z, MK))
    return M


def det(M):
    return (M[0][0] * M[1][1] - M[0][1] * M[1][0]) % P


# P^1(F_31): 32 points.  Represent [x:y] by the value x*y^{-1}, or 'inf'.
def p1_points():
    pts = [("f", t) for t in range(P)]      # [t:1]
    pts.append(("i", None))                  # [1:0] = infinity
    return pts


def act(M, pt):
    a, b = M[0]
    c, d = M[1]
    if pt[0] == "f":
        t = pt[1]
        x, y = t, 1
    else:
        x, y = 1, 0
    nx = (a * x + b * y) % P
    ny = (c * x + d * y) % P
    if ny == 0:
        return ("i", None)
    return ("f", (nx * pow(ny, P - 2, P)) % P)


def main():
    print("=" * 74)
    print("ROUTE B step 2: dim M(level (5phi-2)) via P^1(F_31) orbits")
    print("=" * 74)

    units = ico.unit_icosians()
    mats = [quat_to_matrix(q) for q in units]

    # sanity: all reduced units have det = reduced norm = 1
    dets = set(det(M) for M in mats)
    print(f"\nReduced unit determinants (should be {{1}}): {dets}")

    # image group in PGL_2 acting on P^1: distinct permutations
    pts = p1_points()
    idx = {pt: n for n, pt in enumerate(pts)}
    perms = set()
    for M in mats:
        perm = tuple(idx[act(M, pt)] for pt in pts)
        perms.add(perm)
    print(f"P^1(F_31) has {len(pts)} points; distinct unit-permutations "
          f"= {len(perms)} (image in PGL_2; A_5 has order 60)")

    # orbits = connected components under all unit permutations
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
    for perm in perms:
        for i in range(len(pts)):
            union(i, perm[i])
    roots = {}
    for i in range(len(pts)):
        roots.setdefault(find(i), 0)
        roots[find(i)] += 1
    orbit_sizes = sorted(roots.values())
    n_orbits = len(orbit_sizes)
    print(f"\nOrbit sizes on P^1(F_31): {orbit_sizes}")
    print(f"Number of orbits = dim M(level) = {n_orbits}")

    g1 = (n_orbits == 2)
    print("\n" + "=" * 74)
    print(f"GATE G1: dim == 2 (1 Eisenstein + 1 cuspidal): "
          f"{'PASS' if g1 else 'FAIL'}")
    print("=" * 74)
    if g1:
        print(f"""
The substrate's own arithmetic gives a 2-dimensional space at level
(5phi-2): orbit sizes {orbit_sizes}.  One dimension is the Eisenstein
series (eigenvalue N(P)+1, already verified in short_vectors.py); the
other is a single cusp form -- exactly matching the genuine
1-dimensional norm-31 newform from Route A.

This confirms (from the substrate side, no modular data) that the
correct object exists and has the right dimension.  Step 3-4: build the
Hecke action on these 2 orbits and read off the cuspidal eigenvalues to
compare with H.
""")
    else:
        print(f"""
Orbit count {n_orbits} != 2.  Either the splitting/root choice needs
adjustment, or the level is not as expected.  Investigate before step 4.
""")


if __name__ == "__main__":
    main()
