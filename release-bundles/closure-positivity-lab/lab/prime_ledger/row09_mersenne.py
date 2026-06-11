"""Row 9 — Mersenne primes: the honest BOUNDARY row.

This row marks the instrument's limit and says so. Shape-constrained primes
(2^p - 1) have NO L-function handle: the explicit-formula machinery that powers
every other row does not apply. What survives is:

Layer 1a (THEOREM, verified): every prime factor q of 2^p - 1 (p odd prime)
satisfies q = 1 (mod 2p) AND q = +-1 (mod 8) — a rigid local closure structure
on the factors, checked here against the actual smallest factors.

Layer 1b (HEURISTIC ONLY, verified at 1-sigma level): the Lenstra-Pomerance-
Wagstaff count — Mersenne-prime exponents up to y number about
(e^gamma / log 2) * log y. Unlike rows 1-3 this is NOT a singular-series
consequence; it is a probabilistic model with no theorem behind even its order
of growth. The ledger labels it accordingly.

Anchor (deterministic): the Lucas-Lehmer test recomputes from scratch the full
list of Mersenne exponents up to 3300 and must match the literature exactly.

Layer 2 (the wall, doubly open): infinitude of Mersenne primes AND infinitude
of Mersenne composites are BOTH unproven. Beyond the instrument. Not claimed.
"""
import math

from . import core

Y = 3300
KNOWN_EXPONENTS = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127,
                   521, 607, 1279, 2203, 2281, 3217]
EULER_GAMMA = 0.5772156649015329


def lucas_lehmer(p):
    if p == 2:
        return True
    m = (1 << p) - 1
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % m
    return s == 0


def smallest_factor(p, bound=2_000_000):
    """Smallest prime factor of 2^p - 1 by trial over q = 2kp+1 (theorem form)."""
    m = (1 << p) - 1
    q = 2 * p + 1
    while q <= bound:
        if m % q == 0:
            return q
        q += 2 * p
    return None


def run(s=None):
    sv = core.sieve(Y + 1) if s is None else s[:Y + 1]
    ps = [int(p) for p in core.primes_from(sv)]
    found = [p for p in ps if lucas_lehmer(p)]

    lpw = (math.exp(EULER_GAMMA) / math.log(2)) * math.log(Y)
    sigma = math.sqrt(lpw)  # Poisson-model fluctuation

    factor_checks = []
    factor_ok = True
    for p in (11, 23, 29, 37, 43, 47, 53):
        q = smallest_factor(p)
        if q is None:
            continue
        ok = (q % (2 * p) == 1) and (q % 8 in (1, 7))
        factor_ok &= ok
        factor_checks.append({"p": p, "smallest_factor": q,
                              "q_mod_2p": q % (2 * p), "q_mod_8": q % 8,
                              "theorem_holds": ok})

    gate = ("Lucas-Lehmer reproduces the literature exponent list exactly; "
            "every located factor obeys q=1 (mod 2p) and q=+-1 (mod 8); "
            "count within 3 sigma of Lenstra-Pomerance-Wagstaff")
    ok = (found == KNOWN_EXPONENTS and factor_ok
          and abs(len(found) - lpw) < 3 * sigma)
    return core.row_result(
        9, "Mersenne primes (boundary row: beyond the instrument)",
        "factor congruences: THEOREM (Fermat/Euler); count: "
        "Lenstra-Pomerance-Wagstaff HEURISTIC only",
        "no L-function handle exists - the explicit-formula instrument does "
        "not apply; infinitude of Mersenne primes AND of Mersenne composites "
        "both open",
        {"y": Y, "exponents_found": found, "n_found": len(found),
         "lpw_predicted": round(lpw, 2), "poisson_sigma": round(sigma, 2),
         "factor_checks": factor_checks,
         "boundary_row": True},
        gate, "PASS" if ok else "FAIL",
        "Find a Mersenne prime the Lucas-Lehmer sweep missed (or vice versa), "
        "or a factor of 2^p - 1 violating the congruences. The LPW count is "
        "falsified only asymptotically - that is exactly why this row is "
        "labelled a heuristic boundary, not an instrument result.")


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
