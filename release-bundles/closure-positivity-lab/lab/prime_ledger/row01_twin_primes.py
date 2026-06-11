"""Row 1 — Twin primes: the local closure product predicts the count.

Layer 1 (verified): pi_2(x) ~ 2*C2 * integral_2^x dt/log^2 t  (Hardy-Littlewood
1923, conjectural asymptotic; verified numerically here). C2 is the product
over all odd places p of (1 - 1/(p-1)^2): the twin pattern {0,2} is admissible
at every finite place, and each place contributes a definite local factor.
The wheels fix admissibility and the constant; the asymptotic itself is open.

Layer 2 (the wall): infinitude. Dual, via the explicit formula, to pair
correlations of zeros (Goldston); best unconditional: gaps <= 246 infinitely
often (Zhang/Maynard/Polymath8). Not claimed.
"""
from . import core


def run(s=None, checkpoints=(10_000_000, 25_000_000, None)):
    s = core.sieve() if s is None else s
    x_full = len(s)
    rows = []
    worst = 0.0
    for x in checkpoints:
        x = x_full if x is None else min(x, x_full)
        counted = core.count_pairs(s[:x], 2)
        predicted = 2.0 * core.C2 * core.hl_pair_integral(x)
        ratio = counted / predicted
        worst = max(worst, abs(ratio - 1.0))
        rows.append({"x": x, "counted": counted,
                     "hl_predicted": round(predicted, 1),
                     "ratio": round(ratio, 6)})
    gate = "abs(counted/predicted - 1) < 0.005 at every checkpoint"
    verdict = "PASS" if worst < 0.005 else "FAIL"
    return core.row_result(
        1, "twin primes (gap 2)",
        "Hardy-Littlewood (1923) conjecture B; constant C2",
        "infinitude open; sharpest analytic connection: pair correlation of "
        "zeros (Goldston); unconditional frontier: bounded gaps <= 246 "
        "(Maynard, Polymath8b)",
        {"checkpoints": rows, "C2": core.C2, "worst_deviation": round(worst, 6)},
        gate, verdict,
        "Sieve further and find the count drifting from the HL integral; or "
        "exhibit a finite place at which the pattern {0,2} is inadmissible.")


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
