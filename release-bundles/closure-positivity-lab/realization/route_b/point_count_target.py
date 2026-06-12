"""Phase 1 -- the cuspidal target a_P, generated INDEPENDENTLY by brute-force
point counting.  No LMFDB eigenvalue table is read; the only external datum is
the Weierstrass equation of the curve (five field elements), exactly as in
sims/sim_genuine_eigenvalues.py.

Curve 31.1-a1 over K = Q(sqrt5):
    [a1,a2,a3,a4,a6] = [1, phi+1, phi, phi, 0],   conductor (5phi-2), norm 31.

For each good prime ideal P (P not dividing the conductor) we compute
    a_P = N(P) + 1 - #E(O_K / P)
by exhaustively counting points of E over the residue field O_K/P.  By
modularity over Q(sqrt5) these Frobenius traces ARE the Hecke eigenvalues of
the cuspidal Hilbert newform at level (5phi-2) -- the arithmetic target object.

Honesty checks built in:
  * Ramanujan  |a_P| <= 2 sqrt(N(P))  (must hold for a cusp form; an
    Eisenstein series with eigenvalue N(P)+1 violates it),
  * torsion  8 | #E(F_P)  (31.1-a1 has a rational 8-torsion point).
"""
from __future__ import annotations

import json
import math
import os

# a-invariants in Z[phi] pairs (a, b) = a + b phi
A1 = (1, 0)
A2 = (1, 1)        # phi + 1
A3 = (0, 1)        # phi
A4 = (0, 1)        # phi
A6 = (0, 0)


def _zm(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def _za(x, y):
    return (x[0] + y[0], x[1] + y[1])


def _zs(x, y):
    return (x[0] - y[0], x[1] - y[1])


def _zsm(k, x):
    return (k * x[0], k * x[1])


def _discriminant():
    b2 = _za(_zm(A1, A1), _zsm(4, A2))
    b4 = _za(_zsm(2, A4), _zm(A1, A3))
    b6 = _za(_zm(A3, A3), _zsm(4, A6))
    b8 = _zs(_za(_za(_zm(_zm(A1, A1), A6), _zsm(4, _zm(A2, A6))),
                 _zs(_zm(A2, _zm(A3, A3)), _zm(A1, _zm(A3, A4)))),
             _zm(A4, A4))
    t1 = _zsm(-1, _zm(_zm(b2, b2), b8))
    t2 = _zsm(-8, _zm(_zm(b4, b4), b4))
    t3 = _zsm(-27, _zm(b6, b6))
    t4 = _zsm(9, _zm(b2, _zm(b4, b6)))
    return _za(_za(t1, t2), _za(t3, t4))


DELTA = _discriminant()


def _primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def _sqrt5_mod(p):
    for r in range(p):
        if (r * r - 5) % p == 0:
            return r
    return None


def prime_ideals(norm_bound):
    ideals = []
    for p in _primes_up_to(norm_bound):
        r5 = p % 5
        if p == 5:
            inv2 = pow(2, p - 2, p)
            ideals.append((5, "ramified", p, (1 * inv2) % p))
        elif r5 in (1, 4):
            s = _sqrt5_mod(p)
            inv2 = pow(2, p - 2, p)
            ideals.append((p, "split", p, ((1 + s) * inv2) % p))
            ideals.append((p, "split", p, ((1 - s) * inv2) % p))
        else:
            if p * p <= norm_bound:
                ideals.append((p * p, "inert", p, None))
    ideals.sort(key=lambda t: (t[0], t[3] if t[3] is not None else -1))
    return ideals


def _reduce_scalar(x, root, p):
    return (x[0] + x[1] * root) % p


def _count_Fp(root, p):
    a1 = _reduce_scalar(A1, root, p)
    a2 = _reduce_scalar(A2, root, p)
    a3 = _reduce_scalar(A3, root, p)
    a4 = _reduce_scalar(A4, root, p)
    a6 = _reduce_scalar(A6, root, p)
    count = 1
    for x in range(p):
        rhs = (x * x * x + a2 * x * x + a4 * x + a6) % p
        for y in range(p):
            if (y * y + a1 * x * y + a3 * y) % p == rhs:
                count += 1
    return count


def _f2mul(x, y, p):
    a, b = x
    c, d = y
    return ((a * c + b * d) % p, (a * d + b * c + b * d) % p)


def _f2add(x, y, p):
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)


def _count_Fp2(p):
    a1 = (A1[0] % p, A1[1] % p)
    a2 = (A2[0] % p, A2[1] % p)
    a3 = (A3[0] % p, A3[1] % p)
    a4 = (A4[0] % p, A4[1] % p)
    a6 = (A6[0] % p, A6[1] % p)
    elems = [(u, v) for u in range(p) for v in range(p)]
    count = 1
    for x in elems:
        x2 = _f2mul(x, x, p)
        x3 = _f2mul(x2, x, p)
        rhs = _f2add(_f2add(x3, _f2mul(a2, x2, p), p),
                     _f2add(_f2mul(a4, x, p), a6, p), p)
        for y in elems:
            y2 = _f2mul(y, y, p)
            lhs = _f2add(y2, _f2add(_f2mul(a1, _f2mul(x, y, p), p),
                                    _f2mul(a3, y, p), p), p)
            if lhs == rhs:
                count += 1
    return count


import contextlib


@contextlib.contextmanager
def curve(a1, a2, a3, a4, a6):
    """Evaluate targets for an explicitly named curve (coefficients in (x, y)
    coordinates for x + y*phi), restoring the default curve afterwards.
    Explicit provenance: callers name the curve at the call site instead of
    mutating module globals by hand."""
    global A1, A2, A3, A4, A6, DELTA
    saved = (A1, A2, A3, A4, A6, DELTA)
    A1, A2, A3, A4, A6 = a1, a2, a3, a4, a6
    DELTA = _discriminant()
    try:
        yield
    finally:
        A1, A2, A3, A4, A6, DELTA = saved


def compute_target(norm_bound=200):
    """Return list of dicts for every good prime with N(P) <= norm_bound."""
    rows = []
    for norm, kind, p, root in prime_ideals(norm_bound):
        if kind == "inert":
            bad = (DELTA[0] % p, DELTA[1] % p) == (0, 0)
        else:
            bad = _reduce_scalar(DELTA, root, p) == 0
        if bad:
            continue
        if kind == "inert":
            npts = _count_Fp2(p)
        else:
            npts = _count_Fp(root, p)
        a_P = norm + 1 - npts
        bound = 2 * math.sqrt(norm)
        rows.append({
            "prime_label": "%s_p%d_r%s" % (kind, p, root),
            "kind": kind,
            "p": p,
            "phi_mod_p": root,
            "norm": norm,
            "n_points": npts,
            "a_p": a_P,
            "ramanujan_bound": round(bound, 4),
            "satisfies_ramanujan": abs(a_P) <= bound + 1e-9,
            "torsion_8_divides": npts % 8 == 0,
        })
    return rows


def write_target(path=None, norm_bound=200):
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "..", "data",
                            "target_a_p.json")
    rows = compute_target(norm_bound)
    payload = {
        "curve": "31.1-a1 over Q(sqrt5)",
        "a_invariants": "[1, phi+1, phi, phi, 0]",
        "level": "5phi-2",
        "level_norm": 31,
        "norm_bound": norm_bound,
        "source": "brute_force_point_count",
        "note": ("previously and herein generated by brute-force point-"
                 "counting of E(O_K/P); NOT from any LMFDB eigenvalue table"),
        "n_primes": len(rows),
        "all_ramanujan": all(r["satisfies_ramanujan"] for r in rows),
        "all_torsion8": all(r["torsion_8_divides"] for r in rows),
        "primes": rows,
    }
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    return payload, path


if __name__ == "__main__":
    payload, path = write_target()
    print("Brute-force cuspidal target a_P (curve 31.1-a1 over Q(sqrt5))")
    print("  good primes (N(P) <= %d): %d" % (payload["norm_bound"],
                                              payload["n_primes"]))
    print("  Ramanujan |a_P| <= 2 sqrt N(P) holds for ALL:",
          payload["all_ramanujan"])
    print("  torsion 8 | #E(F_P) holds for ALL:", payload["all_torsion8"])
    print("  wrote", os.path.relpath(path))
    print("\n  N(P)  kind       a_P   |a_P|/2sqrtN")
    for r in payload["primes"][:14]:
        print("  %4d  %-9s %4d   %.3f"
              % (r["norm"], r["kind"], r["a_p"],
                 abs(r["a_p"]) / r["ramanujan_bound"]))
