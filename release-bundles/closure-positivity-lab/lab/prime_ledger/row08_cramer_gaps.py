"""Row 8 — Prime gaps at large (Cramer): theorem-grade mean, conjectural extremes.

Layer 1 (verified): the MEAN gap near x is log x (PNT — theorem); the largest
gap below 5e7 is 220, following the prime 47,326,693 (a documented maximal-gap
record, reproduced deterministically here like Leech's constant in row 5); the
Cramer ratio max_gap / log^2(p) stays O(1) (observed ~0.7).

Honesty note: the pure exponential (Cramer random) model is a HEURISTIC and is
known to be wrong in fine detail — Hardy-Littlewood pair correlations (rows 1-2)
are exactly the corrections it misses. We gate only the theorem-grade mean and
the deterministic record; tail shape is reported, not gated.

Layer 2 (the wall): Cramer's conjecture max_gap = O(log^2 p) is open; even RH
only gives O(sqrt(p) log p); best unconditional gap bound is x^{0.525}
(Baker-Harman-Pintz). Not claimed.
"""
import numpy as np

from . import core

WINDOWS = ((500_000, 1_000_000), (5_000_000, 10_000_000),
           (25_000_000, 50_000_000))


def run(s=None):
    s = core.sieve() if s is None else s
    P = core.primes_from(s)
    gaps = np.diff(P)

    win_rows, worst = [], 0.0
    for a, b in WINDOWS:
        i, j = np.searchsorted(P, a), np.searchsorted(P, b)
        g = gaps[i:j - 1]
        mean, target = float(np.mean(g)), float(np.log((a + b) / 2.0))
        dev = abs(mean / target - 1.0)
        worst = max(worst, dev)
        u = g / mean
        win_rows.append({"window": [a, b], "mean_gap": round(mean, 3),
                         "log_midpoint": round(target, 3),
                         "deviation": round(dev, 4),
                         "tail_P(u>2)": round(float(np.mean(u > 2.0)), 4),
                         "exp_model_says": round(float(np.exp(-2)), 4)})

    k = int(np.argmax(gaps))
    max_gap, at_p = int(gaps[k]), int(P[k])
    cramer_ratio = max_gap / np.log(at_p) ** 2

    gate = ("mean gap within 3% of log(midpoint) in every window; largest gap "
            "below 5e7 is exactly 220 after 47,326,693")
    ok = worst < 0.03 and max_gap == 220 and at_p == 47_326_693
    return core.row_result(
        8, "prime gaps at large (Cramer)",
        "mean gap = log x is PNT (THEOREM); maximal-gap record from "
        "Nicely/Young-Potler tables; Cramer model is heuristic",
        "Cramer's max-gap = O(log^2 p) open; RH gives only O(sqrt(p) log p); "
        "unconditional: gaps << x^0.525 (Baker-Harman-Pintz)",
        {"x": len(s), "windows": win_rows, "max_gap": max_gap,
         "after_prime": at_p, "cramer_ratio": round(float(cramer_ratio), 3),
         "note": "tail shape reported not gated: HL correlations (rows 1-2) "
                 "are the known corrections to the pure exponential model"},
        gate, "PASS" if ok else "FAIL",
        "Re-sieve: a different maximal gap below 5e7, or mean gaps drifting "
        "from log x, kills the row.")


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
