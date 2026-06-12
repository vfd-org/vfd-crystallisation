"""Cache the GEOMETRIC Hecke eigenvalues a_q (one per prime ideal q) produced by
the icosian Brandt operator -- the parameter-free output of brandt_matrices.py.

This is the bridge's "prime residual" source.  For each good prime ideal q of
norm <= bound (q != level), we take a totally-positive generator and read the
cuspidal eigenvalue of B(q).  At split primes BOTH primes above p are emitted
(the two Galois-conjugate generators).  Nothing is point-counted here and no
curve data enters: the values come from the geometry (verified in the prior WO
to equal the independent point counts, out-of-sample, with zero fitting).
"""
from __future__ import annotations

import json
import os

try:
    from . import ok_arithmetic as ok
    from . import brandt_matrices as bm
except ImportError:
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    import ok_arithmetic as ok
    import brandt_matrices as bm

LEVEL_NORM = 31


def _primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def prime_ideal_generators(p):
    """Totally-positive generators, one per prime ideal above the rational
    prime p (split -> 2, inert/ramified -> 1).  Grouped by the residue-field
    root so the two split primes are distinguished."""
    # which norm does a prime above p have?
    if p % 5 in (1, 4):
        target_norm = p              # split: two degree-1 primes
    elif p == 5:
        target_norm = 5              # ramified
    else:
        target_norm = p * p          # inert: one degree-2 prime, norm p^2
    gens = {}
    rng = 4 * p + 6
    for a in range(-rng, rng + 1):
        for b in range(-rng, rng + 1):
            e = (a, b)
            if abs(ok.norm(e)) != target_norm or not ok.is_totally_positive(e):
                continue
            # identify the prime ideal by the residue-field root it kills
            roots = [r for r in range(p) if (r * r - r - 1) % p == 0]
            if target_norm == p * p:           # inert: single prime (p)
                key = "inert"
            else:
                key = None
                for r in roots:
                    if (a + b * r) % p == 0:
                        key = r
                        break
                if key is None:
                    continue
            if key not in gens:
                gens[key] = e
    return list(gens.values())


def build_cache(bound=150, path=None):
    eng = bm.BrandtEngine()
    rows = []
    for p in _primes_up_to(bound):
        # need N(q) <= bound: split N=p<=bound; inert N=p^2<=bound
        if p % 5 in (1, 4) or p == 5:
            if p > bound or p == LEVEL_NORM:
                continue
        else:
            if p * p > bound:
                continue
        for varpi in prime_ideal_generators(p):
            Nq = abs(ok.norm(varpi))
            r = eng.brandt_matrix(varpi)
            rows.append({
                "rational_prime": p,
                "norm": Nq,
                "varpi": list(varpi),
                "a_q_geometric": r["cuspidal_eigenvalue"],
                "self_adjoint": r["self_adjoint"],
                "ramanujan_ok": abs(r["cuspidal_eigenvalue"]) <= 2 * (Nq ** 0.5)
                + 1e-9,
            })
    rows.sort(key=lambda d: (d["norm"], d["a_q_geometric"]))
    payload = {
        "source": "icosian_brandt_operator",
        "provenance": ("geometric: cuspidal eigenvalue of the self-adjoint "
                       "icosian Brandt operator B(q); no point-counting, no "
                       "curve data, no fitting in this path"),
        "bound": bound,
        "n_prime_ideals": len(rows),
        "all_self_adjoint": all(r["self_adjoint"] for r in rows),
        "all_ramanujan": all(r["ramanujan_ok"] for r in rows),
        "rows": rows,
    }
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "..", "data",
                            "geometric_aP.json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    return payload, path


def load_cache(path=None):
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "..", "data",
                            "geometric_aP.json")
    with open(path) as f:
        return json.load(f)


if __name__ == "__main__":
    payload, path = build_cache()
    print("geometric a_q cache (icosian Brandt operator)")
    print("  prime ideals (N(q) <= %d): %d" % (payload["bound"],
                                               payload["n_prime_ideals"]))
    print("  all self-adjoint:", payload["all_self_adjoint"])
    print("  all Ramanujan   :", payload["all_ramanujan"])
    print("  wrote", os.path.relpath(path))
    for r in payload["rows"][:12]:
        print("    N(q)=%4d  a_q=%4d" % (r["norm"], r["a_q_geometric"]))
