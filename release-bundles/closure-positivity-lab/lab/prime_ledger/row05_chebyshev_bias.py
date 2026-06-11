"""Row 5 — Chebyshev bias: a diffraction asymmetry you can watch accumulate.

Layer 1 (verified): pi(x; 4, 3) > pi(x; 4, 1) for the overwhelming majority of x,
with the first lead change at exactly x = 26,861 (Leech 1957); mod 3, the
analogous bias never reverses below our sieve bound (first reversal known to be
~6.08e11). In explicit-formula terms the bias is interference: the prime-SQUARE
wave contributes wholly to the non-residue side, displacing the count by
~ sqrt(x)/log x — the same instrument as the paper's prime-wave reconstruction,
showing an asymmetric fringe.

Layer 2 (the wall): the logarithmic density of the lead set is 0.9959... under
GRH + linear independence of zeros (Rubinstein-Sarnak 1994). Unconditionally,
even "the lead set has a density" is open. Not claimed.
"""
import numpy as np

from . import core


def lead_stats(P, q, winner, loser):
    res = P % q
    sgn = np.zeros(P.size, dtype=np.int64)
    sgn[np.isin(res, winner)] = 1
    sgn[np.isin(res, loser)] = -1
    D = np.cumsum(sgn)
    neg = np.nonzero(D < 0)[0]
    first_cross = int(P[neg[0]]) if neg.size else None
    lead_frac = float(np.count_nonzero(D > 0) / D.size)
    return D, first_cross, lead_frac


def run(s=None):
    s = core.sieve() if s is None else s
    x = len(s)
    P = core.primes_from(s)

    D4, cross4, frac4 = lead_stats(P, 4, [3], [1])
    D3, cross3, frac3 = lead_stats(P, 3, [2], [1])

    # explicit-formula scale: D(x) ~ sqrt(x)/log x; report the O(1) coefficient
    checkpoints = []
    for xc in (1_000_000, 10_000_000, x - 1):
        i = int(np.searchsorted(P, xc, side="right")) - 1
        checkpoints.append({"x": xc, "D_mod4": int(D4[i]),
                            "coeff_vs_sqrtx_over_logx":
                                round(D4[i] * np.log(xc) / xc ** 0.5, 3)})

    gate = ("first mod-4 lead change at exactly 26,861; mod-3 bias never "
            "reverses below sieve bound; mod-4 lead fraction > 95%")
    ok = cross4 == 26_861 and cross3 is None and frac4 > 0.95
    return core.row_result(
        5, "Chebyshev bias (primes prefer non-residue classes)",
        "Chebyshev (1853); first crossing Leech (1957); density "
        "Rubinstein-Sarnak (1994) under GRH+LI",
        "unconditional existence of the lead-set density is open; the bias "
        "coefficient is explicit-formula interference from the prime-square wave",
        {"x": x, "mod4_first_lead_change": cross4,
         "mod4_lead_fraction_of_primes": round(frac4, 5),
         "mod3_first_lead_change": cross3,
         "mod3_lead_fraction_of_primes": round(frac3, 5),
         "checkpoints": checkpoints},
        gate, "PASS" if ok else "FAIL",
        "Re-sieve and find the first mod-4 crossing somewhere other than "
        "26,861, or a mod-3 reversal below the bound, or the bias decaying "
        "faster than sqrt(x)/log x.")


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
