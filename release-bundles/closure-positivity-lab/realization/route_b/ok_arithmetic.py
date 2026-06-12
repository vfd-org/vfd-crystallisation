"""Phase 2 -- exact arithmetic in O_K = Z[phi], the ring of integers of
K = Q(sqrt 5).

An element a + b*phi is stored as the integer pair (a, b), where
phi = (1 + sqrt 5)/2 satisfies phi^2 = phi + 1.  Everything here is exact
integer arithmetic; no floating point enters the ring operations.

Conventions
-----------
  conjugation:  bar(a + b phi) = a + b*phibar = (a + b) - b*phi   since
                phibar = 1 - phi  (the second root of x^2 - x - 1).
  trace:        Tr(a + b phi) = (a + b phi) + (a + b phibar) = 2a + b.
  norm:         N(a + b phi)  = (a + b phi)(a + b phibar)
                              = a^2 + a b - b^2.

The element 5*phi - 2 has norm N = 25 - 10 - 4 ... computed exactly below;
its *absolute* norm is 31, the level of the work order.

This module is deliberately free of any modular-forms / elliptic-curve data:
it is pure base-ring arithmetic, the foundation everything else stands on.
"""
from __future__ import annotations

import math

# phi numeric values of the two real embeddings (used ONLY for the
# totally-positive predicate; never for ring arithmetic).
_PHI = (1.0 + math.sqrt(5.0)) / 2.0          # ~ 1.6180339887
_PHIBAR = (1.0 - math.sqrt(5.0)) / 2.0       # ~ -0.6180339887


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def neg(x):
    return (-x[0], -x[1])


def mul(x, y):
    a, b = x
    c, d = y
    # (a+b phi)(c+d phi) = ac + (ad+bc) phi + bd phi^2,  phi^2 = phi+1
    #                    = (ac + bd) + (ad + bc + bd) phi
    return (a * c + b * d, a * d + b * c + b * d)


def smul(k, x):
    return (k * x[0], k * x[1])


def conj(x):
    a, b = x
    # bar(a + b phi) = a + b(1 - phi) = (a + b) - b phi
    return (a + b, -b)


def trace(x):
    return 2 * x[0] + x[1]


def norm(x):
    a, b = x
    return a * a + a * b - b * b


def embeddings(x):
    """Return the two real images (phi-embedding, phibar-embedding)."""
    a, b = x
    return (a + b * _PHI, a + b * _PHIBAR)


def is_totally_positive(x):
    e1, e2 = embeddings(x)
    return e1 > 1e-9 and e2 > 1e-9


def divides(d, x):
    """True if d | x in Z[phi] (exact)."""
    if d == (0, 0):
        return x == (0, 0)
    # x / d = x * conj(d) / N(d); integral iff N(d) | both components.
    num = mul(x, conj(d))
    nd = norm(d)
    return num[0] % nd == 0 and num[1] % nd == 0


def quotient(d, x):
    """Exact x // d when d | x; raises if it does not divide."""
    num = mul(x, conj(d))
    nd = norm(d)
    if num[0] % nd != 0 or num[1] % nd != 0:
        raise ValueError("not divisible in Z[phi]")
    return (num[0] // nd, num[1] // nd)


def reduce_mod_p(x, root, p):
    """Reduce a + b phi to F_p via phi -> root (root a root of x^2-x-1)."""
    a, b = x
    return (a + b * root) % p


PHI = (0, 1)              # phi
ONE = (1, 0)              # 1
LEVEL = (-2, 5)           # 5 phi - 2  (work-order level generator)


if __name__ == "__main__":
    print("O_K = Z[phi] arithmetic self-report")
    print("  phi^2            =", mul(PHI, PHI), " (expect (1,1) = 1 + phi)")
    print("  N(phi)           =", norm(PHI), " (expect -1)")
    print("  Tr(phi)          =", trace(PHI), " (expect 1)")
    print("  conj(phi)        =", conj(PHI), " (expect (1,-1) = 1 - phi)")
    print("  level 5phi-2     =", LEVEL)
    print("  N(5phi-2)        =", norm(LEVEL), " |N| =", abs(norm(LEVEL)),
          " (expect 31)")
    print("  Tr(5phi-2)       =", trace(LEVEL))
    print("  5phi-2 tot.pos.? =", is_totally_positive(LEVEL))
