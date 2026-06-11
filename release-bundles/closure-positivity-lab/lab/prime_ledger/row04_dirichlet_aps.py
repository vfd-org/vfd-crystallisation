"""Row 4 — Primes in arithmetic progressions: THEOREM ANCHOR.

Layer 1 (theorem, verified): primes equidistribute among the phi(q) admissible
residue classes mod q (Dirichlet 1837 + PNT in APs). The admissible classes are
exactly the residues coprime to q — the closure condition at the places dividing
q. Inadmissible classes contain at most the finitely many primes dividing q.

This row is a calibration anchor: the instrument's output must match proven
mathematics exactly, or the instrument is broken.

Layer 2 (the wall): the ERROR TERM. Square-root equidistribution error is GRH
for Dirichlet L-functions. Not claimed.
"""
import numpy as np

from . import core

MODULI = (4, 5, 12)


def run(s=None):
    s = core.sieve() if s is None else s
    P = core.primes_from(s)
    out, worst = [], 0.0
    for q in MODULI:
        admissible = [a for a in range(1, q) if np.gcd(a, q) == 1]
        Pq = P[P > q]  # exclude the primes dividing q themselves
        res = Pq % q
        counts = {a: int(np.count_nonzero(res == a)) for a in admissible}
        inadmissible = int(Pq.size - sum(counts.values()))
        mean = sum(counts.values()) / len(admissible)
        dev = max(abs(c / mean - 1.0) for c in counts.values())
        worst = max(worst, dev)
        out.append({"q": q, "class_counts": counts,
                    "inadmissible_class_primes": inadmissible,
                    "max_deviation_from_equidistribution": round(dev, 5)})
    gate = ("inadmissible classes empty above q; admissible classes within 1% "
            "of equidistribution")
    ok = worst < 0.01 and all(r["inadmissible_class_primes"] == 0 for r in out)
    return core.row_result(
        4, "primes in arithmetic progressions",
        "THEOREM: Dirichlet (1837); PNT in APs (de la Vallee Poussin)",
        "error term: square-root cancellation = GRH for Dirichlet L-functions",
        {"x": len(s), "moduli": out, "worst_deviation": round(worst, 5)},
        gate, "PASS" if ok else "FAIL",
        "Find a prime > q in a residue class not coprime to q, or persistent "
        "skew between admissible classes (beyond Chebyshev-bias scale, row 5).")


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
