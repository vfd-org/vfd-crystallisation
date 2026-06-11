"""Run all Phase A ledger rows against one shared sieve.

    python3 -m lab.prime_ledger            # X = 5e7 default
    PRIME_LEDGER_X=10000000 python3 -m lab.prime_ledger

Writes out/prime_ledger.json and prints the verdict table. Exit code 0 only
if every row passes its gate.
"""
import json
import os
import sys
import time

from . import core
from . import row01_twin_primes, row02_polignac_gaps
from . import row04_dirichlet_aps, row06_qsqrt5_splitting

ROWS = (row01_twin_primes, row02_polignac_gaps,
        row04_dirichlet_aps, row06_qsqrt5_splitting)

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "out",
                   "prime_ledger.json")


def main():
    t0 = time.time()
    print("sieving to %d ..." % core.DEFAULT_X)
    s = core.sieve()
    results = []
    for mod in ROWS:
        r = mod.run(s)
        results.append(r)
        print("row %2d  %-52s %s" % (r["row"], r["phenomenon"], r["verdict"]))

    doc = {
        "work_order": "WO-VFD-PRIME-LEDGER-001",
        "phase": "A",
        "x": core.DEFAULT_X,
        "thesis": ("every prime-distribution phenomenon factors as "
                   "(all-finite-places closure product, decidable) x "
                   "(zero-correlation interference, the single open wall)"),
        "scope": ("layer-1 results are classical (verified, not discovered); "
                  "layer-2 is open in every conjectural row; nothing here "
                  "proves RH, GRH, or any infinitude conjecture"),
        "rows": results,
        "runtime_seconds": round(time.time() - t0, 1),
    }
    with open(os.path.abspath(OUT), "w") as fh:
        json.dump(doc, fh, indent=2)

    n_pass = sum(1 for r in results if r["verdict"] == "PASS")
    print("\n%d/%d rows PASS  (%.0fs)  -> out/prime_ledger.json"
          % (n_pass, len(results), doc["runtime_seconds"]))
    return 0 if n_pass == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
