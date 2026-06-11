"""Generate embedded data for the explorables from the same sieve as the ledger.

Run from the bundle root:  python3 explorables/make_data.py
Writes explorables/gap_data.js and explorables/race_data.js
"""
import json
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from lab.prime_ledger import core  # noqa: E402

OUT = os.path.dirname(os.path.abspath(__file__))


def gap_data(s):
    """Counts for every even gap 2..210 + per-gap odd prime factors."""
    n2 = core.count_pairs(s, 2)
    rows = []
    for h in range(2, 212, 2):
        rows.append({
            "h": h,
            "pairs": core.count_pairs(s, h),
            "factors": core.odd_prime_factors(h),
            "predicted": round(core.gap_local_ratio(h), 6),
        })
    return {"x": len(s), "twin_pairs": n2, "gaps": rows}


def race_data(s):
    """Chebyshev D(x) = pi(x;4,3) - pi(x;4,1) at log-sampled primes + dense
    slice around the first crossing at 26,861."""
    P = core.primes_from(s)
    res = P % 4
    sgn = np.where(res == 3, 1, np.where(res == 1, -1, 0))
    D = np.cumsum(sgn)
    idx = np.unique(np.logspace(np.log10(2), np.log10(P.size - 1), 4000).astype(int))
    series = [[int(P[i]), int(D[i])] for i in idx]
    lo, hi = np.searchsorted(P, 25_500), np.searchsorted(P, 28_500)
    zoom = [[int(P[i]), int(D[i])] for i in range(lo, hi)]
    return {"x": len(s), "series": series, "zoom": zoom, "first_crossing": 26861}


def main():
    print("sieving to %d ..." % core.DEFAULT_X)
    s = core.sieve()
    with open(os.path.join(OUT, "gap_data.js"), "w") as fh:
        fh.write("const GAP_DATA = %s;\n" % json.dumps(gap_data(s)))
    print("wrote gap_data.js")
    with open(os.path.join(OUT, "race_data.js"), "w") as fh:
        fh.write("const RACE_DATA = %s;\n" % json.dumps(race_data(s)))
    print("wrote race_data.js")


if __name__ == "__main__":
    main()
