"""Row 2 — Polignac gaps: relative abundance of every even gap from local factors.

Layer 1 (verified): pairs at gap h occur S(h)/S(2) = prod_{odd p | h} (p-1)/(p-2)
times as often as twins. Gap 6 is exactly twice as common as gap 2; gap 10 is
4/3; gap 30 is 8/3; gap 210 is 16/5. Pure all-finite-places arithmetic — the
odd primes dividing h relax one congruence condition each.

Layer 2 (the wall): infinitude for ANY single h (Polignac, open for all h);
same pair-correlation wall as row 1. Not claimed.
"""
from . import core

GAPS = (2, 4, 6, 8, 10, 12, 30, 210)


def run(s=None):
    s = core.sieve() if s is None else s
    n2 = core.count_pairs(s, 2)
    rows, worst = [], 0.0
    for h in GAPS:
        n = core.count_pairs(s, h)
        ratio, pred = n / n2, core.gap_local_ratio(h)
        dev = abs(ratio / pred - 1.0)
        worst = max(worst, dev)
        rows.append({"gap": h, "pairs": n, "ratio_vs_twins": round(ratio, 4),
                     "local_product": round(pred, 4), "deviation": round(dev, 4)})
    gate = "every gap ratio within 2% of its all-places local product"
    verdict = "PASS" if worst < 0.02 else "FAIL"
    return core.row_result(
        2, "prime pairs at every even gap (Polignac)",
        "Hardy-Littlewood singular series S(h)",
        "infinitude for any fixed h open; same zero-pair-correlation wall as row 1",
        {"x": len(s), "gaps": rows, "worst_deviation": round(worst, 4)},
        gate, verdict,
        "Find an even gap whose abundance ratio is NOT the product of "
        "(p-1)/(p-2) over odd primes dividing it.")


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
