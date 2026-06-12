"""Exact Q(sqrt(5)) arithmetic + icosian quaternion routines.

Vendored unmodified from papers/paper-xxii/scripts/run_icosian_exact.py.
The mathematical content is identical; module structure is reorganised
so the V_600 programme has a single source of truth.

Q(sqrt(5)) is represented as pairs (a, b) with a, b in Fraction, standing
for a + b*sqrt(5). Quaternions are 4-tuples of such pairs. All arithmetic
is exact; no floating-point.
"""

from __future__ import annotations

import itertools
from fractions import Fraction


# --- Q(sqrt(5)) as (a, b) -> a + b*sqrt(5) ------------------------------

def q_add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def q_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])

def q_neg(x):
    return (-x[0], -x[1])

def q_mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

def q_scale(x, s):
    return (x[0] * s, x[1] * s)

def q_zero():
    return (Fraction(0), Fraction(0))

def q_one():
    return (Fraction(1), Fraction(0))

def q_half():
    return (Fraction(1, 2), Fraction(0))

def phi():
    return (Fraction(1, 2), Fraction(1, 2))

def inv_phi():
    return q_sub(phi(), q_one())

def phi_half():
    return (Fraction(1, 4), Fraction(1, 4))

def inv_2phi():
    return q_scale(inv_phi(), Fraction(1, 2))


# --- Quaternion = 4-tuple of Q(sqrt(5)) entries -------------------------

def quat(w, x, y, z):
    return (w, x, y, z)

def qq_eq(a, b):
    return a[0] == b[0] and a[1] == b[1] and a[2] == b[2] and a[3] == b[3]

def qq_key(a):
    return tuple((v[0], v[1]) for v in a)

def qq_mul(a, b):
    aw, ax, ay, az = a
    bw, bx, by, bz = b
    w = q_sub(q_mul(aw, bw),
              q_add(q_add(q_mul(ax, bx), q_mul(ay, by)), q_mul(az, bz)))
    x = q_add(q_add(q_mul(aw, bx), q_mul(ax, bw)),
              q_sub(q_mul(ay, bz), q_mul(az, by)))
    y = q_add(q_sub(q_mul(aw, by), q_mul(ax, bz)),
              q_add(q_mul(ay, bw), q_mul(az, bx)))
    z = q_add(q_add(q_mul(aw, bz), q_mul(ax, by)),
              q_sub(q_mul(az, bw), q_mul(ay, bx)))
    return (w, x, y, z)

def qq_conjugate(a):
    w, x, y, z = a
    return (w, q_neg(x), q_neg(y), q_neg(z))

def qq_norm_sq(a):
    w, x, y, z = a
    return q_add(q_add(q_mul(w, w), q_mul(x, x)),
                 q_add(q_mul(y, y), q_mul(z, z)))

def qq_distance_sq(a, b):
    diff = tuple(q_sub(a[i], b[i]) for i in range(4))
    return qq_norm_sq(diff)

def trace_inner(a, b):
    """Trace inner product on icosian quaternions: Re(a * conj(b))."""
    bc = qq_conjugate(b)
    prod = qq_mul(a, bc)
    return prod[0]


def parity(perm):
    s = 1
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                s = -s
    return s


def q5_sign(p):
    """Exact sign of a + b√5 with a, b ∈ Q. Returns -1, 0, +1 by exact arithmetic.
    Used wherever a Q(√5)-valued quantity must be ordered as a real number
    without floating-point. For mixed signs of (a, b), squares both sides
    to compare |a|² vs 5|b|² and determines which dominates."""
    a, b = p
    if a == 0 and b == 0:
        return 0
    if a == 0:
        return 1 if b > 0 else -1
    if b == 0:
        return 1 if a > 0 else -1
    if (a > 0) and (b > 0):
        return 1
    if (a < 0) and (b < 0):
        return -1
    # Mixed signs: compare |a|² vs 5|b|².
    a2 = a * a
    b2 = 5 * b * b
    if a2 > b2:
        return 1 if a > 0 else -1
    if a2 < b2:
        return 1 if b > 0 else -1
    return 0


def q5_lt(p, q):
    """p < q in R when both are in Q(√5)."""
    return q5_sign((p[0] - q[0], p[1] - q[1])) < 0


# --- Build the 120 V_600 vertices ---------------------------------------

def build_vertices():
    """Return the 120 vertices of V_600 as a list of icosian quaternions."""
    verts = []

    # Set 1: 8 of (+-1, 0, 0, 0) permutations
    for i in range(4):
        for s in (1, -1):
            v = [q_zero(), q_zero(), q_zero(), q_zero()]
            v[i] = q_scale(q_one(), Fraction(s))
            verts.append(tuple(v))

    # Set 2: 16 of (+-1/2, +-1/2, +-1/2, +-1/2)
    for signs in itertools.product((1, -1), repeat=4):
        v = tuple(q_scale(q_one(), Fraction(s, 2)) for s in signs)
        verts.append(v)

    # Set 3: 96 even permutations of (0, +-1/(2 phi), +-1/2, +-phi/2)
    base = [q_zero(), inv_2phi(), q_scale(q_one(), Fraction(1, 2)), phi_half()]
    for perm in itertools.permutations(range(4)):
        if parity(perm) != 1:
            continue
        permuted = tuple(base[p] for p in perm)
        zero_slot = None
        for idx, elt in enumerate(permuted):
            if elt == q_zero():
                zero_slot = idx
                break
        for signs in itertools.product((1, -1), repeat=3):
            v = list(permuted)
            j = 0
            for k in range(4):
                if k == zero_slot:
                    continue
                v[k] = q_scale(v[k], Fraction(signs[j]))
                j += 1
            verts.append(tuple(v))

    seen = {}
    unique_verts = []
    for v in verts:
        k = qq_key(v)
        if k not in seen:
            seen[k] = len(unique_verts)
            unique_verts.append(v)
    assert len(unique_verts) == 120
    return unique_verts


def vertex_index_map(verts):
    return {qq_key(v): i for i, v in enumerate(verts)}
