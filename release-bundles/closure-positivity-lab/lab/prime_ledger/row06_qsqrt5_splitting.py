"""Row 6 — Splitting in Q(sqrt 5): THEOREM ANCHOR, and our field.

Layer 1 (theorem, verified): a rational prime p splits in K = Q(sqrt 5) iff
p = +-1 mod 5, stays inert iff p = +-2 mod 5 (p = 5 ramifies). By Chebotarev,
split and inert primes each have density 1/2. This is the place-5 closure
condition of the field underneath the whole icosian programme — the Brandt
prime ideals of provenance_664.json live over exactly these primes.

Bonus place-5 fact (exact, not statistical): a twin pair (p, p+2) with
p = 3 mod 5 forces 5 | p+2, so the ONLY such pair is (3, 5). The ledger
checks this count is exactly 1 — a closure condition acting with no
statistics involved.

Layer 2 (the wall): the equidistribution error term = zeros of zeta_K
(equivalently the quadratic Dirichlet L mod 5). Not claimed.
"""
import numpy as np

from . import core


def run(s=None):
    s = core.sieve() if s is None else s
    P = core.primes_from(s)
    Pq = P[P > 5]
    res = Pq % 5
    split = int(np.count_nonzero((res == 1) | (res == 4)))
    inert = int(np.count_nonzero((res == 2) | (res == 3)))
    frac = split / (split + inert)

    twin_lo = np.nonzero(s[:-2] & s[2:])[0]  # lower members of twin pairs
    # twin pairs whose lower member is 3 mod 5 — closure at the place 5 says: only (3,5)
    n_forbidden = int(np.count_nonzero(twin_lo % 5 == 3))

    gate = ("split fraction within 1% of 1/2; exactly one twin pair with "
            "p = 3 mod 5 (namely (3,5))")
    ok = abs(frac - 0.5) < 0.005 and n_forbidden == 1
    return core.row_result(
        6, "splitting of primes in Q(sqrt 5) (the programme's base field)",
        "THEOREM: quadratic reciprocity / Chebotarev density",
        "error term = zeros of zeta_K / L(s, chi_5)",
        {"x": len(s), "split": split, "inert": inert,
         "split_fraction": round(frac, 5),
         "twin_pairs_with_p_eq_3_mod_5": n_forbidden,
         "note": "Brandt prime ideals in provenance_664.json lie over these primes"},
        gate, "PASS" if ok else "FAIL",
        "Find a prime p = +-2 mod 5 that splits (or +-1 that does not), or a "
        "second twin pair with p = 3 mod 5.")


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
