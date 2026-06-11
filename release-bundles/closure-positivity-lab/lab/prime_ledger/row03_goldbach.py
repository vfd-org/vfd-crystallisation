"""Row 3 — Goldbach: per-N representation counts from the same local product.

Layer 1 (verified): the number of ordered representations N = p + q (both prime)
tracks  R(N) = 2*C2 * prod_{odd p | N} (p-1)/(p-2) * integral_2^{N-2} dt/(ln t ln(N-t))
(Hardy-Littlewood conjecture A). The SAME singular-series machinery as rows 1-2,
in additive form: the local factor varies with N's odd prime divisors, so N
divisible by 3 has ~2x the representations of its neighbours — a per-N
prediction, not just an average.

Layer 2 (the wall): that R(N) > 0 for every even N > 2 (binary Goldbach) is open;
the circle-method minor arcs are controlled by zeros of Dirichlet L-functions.
Ternary Goldbach is a THEOREM (Helfgott 2013). Not claimed.
"""
import numpy as np

from . import core

BAND_START = 1_000_000
BAND_COUNT = 200  # even N in [BAND_START, BAND_START + 2*BAND_COUNT)


def predicted(n):
    s = 1.0
    for p in core.odd_prime_factors(n):
        s *= (p - 1) / (p - 2)
    t = np.linspace(2.0, float(n - 2), 20_001)
    return 2.0 * core.C2 * s * float(np.trapz(1.0 / (np.log(t) * np.log(n - t)), t))


def run(s=None):
    x_need = BAND_START + 2 * BAND_COUNT + 2
    s = core.sieve(x_need) if s is None else s[:x_need]
    P = core.primes_from(s)
    rows, devs = [], []
    for k in range(BAND_COUNT):
        n = BAND_START + 2 * k
        pn = P[P <= n - 2]
        counted = int(np.count_nonzero(s[n - pn]))  # ordered pairs (p, n-p)
        pred = predicted(n)
        dev = counted / pred - 1.0
        devs.append(dev)
        if k < 6 or n % 3 == 0 and len(rows) < 12:
            rows.append({"N": n, "counted": counted, "predicted": round(pred, 1),
                         "ratio": round(counted / pred, 4)})
    devs = np.array(devs)
    mean_abs, worst = float(np.mean(np.abs(devs))), float(np.max(np.abs(devs)))
    gate = "mean |ratio-1| < 2% and max < 6% over 200 consecutive even N near 1e6"
    verdict = "PASS" if (mean_abs < 0.02 and worst < 0.06) else "FAIL"
    return core.row_result(
        3, "Goldbach representation counts",
        "Hardy-Littlewood (1923) conjecture A; ternary case THEOREM (Helfgott 2013)",
        "binary Goldbach (R(N) > 0 for all even N) open; minor arcs = zeros of "
        "Dirichlet L-functions",
        {"band": [BAND_START, BAND_START + 2 * BAND_COUNT - 2],
         "n_tested": BAND_COUNT, "mean_abs_deviation": round(mean_abs, 4),
         "max_abs_deviation": round(worst, 4), "samples": rows},
        gate, verdict,
        "Pick any even N in range: count representations and compare to the "
        "local product x integral; a structural miss (not sqrt-N noise) kills "
        "the row. The 3|N doubling is the sharpest sub-test.")


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
