"""Row 7 — Sato-Tate for OUR cuspidal L-function: THEOREM ANCHOR.

Layer 1 (theorem, verified): the normalized eigenvalue angles of the icosian
cuspidal form (= curve 31.1-a1/Q(sqrt5), non-CM Hilbert modular) equidistribute
under the Sato-Tate measure (2/pi) sin^2(theta). THEOREM: Barnet-Lamb-Geraghty-
Harris-Taylor. We test the geometric Brandt eigenvalues a_q from
out/a_q_extended.json (the same 664-ideal dataset behind provenance_664.json),
dropping the Steinberg prime at the level (norm 31), leaving 663 angles.

Statistical design: under the ST null the moment estimators have known
fluctuation sigma ~ c/sqrt(n); gates are set at 3 sigma BEFORE looking at the
data, so a pass is a calibrated agreement, not a tuned one.

Layer 2 (the wall): the RATE of equidistribution (effective Sato-Tate, the
discrepancy decay) is governed by symmetric-power L-functions — the
sqrt-cancellation regime is the GRH signature. The limit law is proven; the
rate is the open, RH-adjacent content. Not claimed.
"""
import json
import os

import numpy as np

from . import core

AQ_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "out",
                       "a_q_extended.json")

# Sato-Tate moments of x = cos(theta): E[x^{2k}] = Catalan(k)/4^k, odd = 0
ST_M2, ST_M4 = 0.25, 0.125


def run(s=None):  # signature kept uniform; the sieve is unused here
    with open(os.path.abspath(AQ_PATH)) as fh:
        d = json.load(fh)
    # drop ONLY the Steinberg prime at the level: 31 splits in Q(sqrt5), and
    # just one of the two norm-31 ideals is the level (a_q = -1, |a_q| = 1);
    # the other (a_q = 8) is a good prime and stays. 664 -> 663 angles.
    rows = [r for r in d["rows"]
            if not (r["norm"] == 31 and abs(r["a_q_geometric"]) == 1)]
    n = len(rows)
    a = np.array([r["a_q_geometric"] for r in rows], dtype=float)
    nq = np.array([r["norm"] for r in rows], dtype=float)
    x = a / (2.0 * np.sqrt(nq))  # = cos(theta_q), Ramanujan => |x| <= 1
    ramanujan_ok = bool(np.all(np.abs(x) <= 1.0 + 1e-12))

    m1, m2 = float(np.mean(x)), float(np.mean(x ** 2))
    m3, m4 = float(np.mean(x ** 3)), float(np.mean(x ** 4))

    # 3-sigma gates under the ST null (variances of x, x^2, x^3, x^4 moments)
    sd = {k: float(np.sqrt(v / n)) for k, v in
          {"m1": ST_M2, "m2": ST_M4 - ST_M2 ** 2,
           "m3": 5 / 64, "m4": 14 / 256 - ST_M4 ** 2}.items()}
    checks = {
        "m1": (m1, 0.0, 3 * sd["m1"]), "m2": (m2, ST_M2, 3 * sd["m2"]),
        "m3": (m3, 0.0, 3 * sd["m3"]), "m4": (m4, ST_M4, 3 * sd["m4"]),
    }
    ok = ramanujan_ok and all(abs(v - t) < tol for v, t, tol in checks.values())

    # Kolmogorov-Smirnov distance vs the ST CDF (reported, not gated)
    theta = np.sort(np.arccos(np.clip(x, -1, 1)))
    # ST CDF on [0, pi]: (2/pi) * int_0^t sin^2 = (t - sin t cos t) / pi
    st_cdf = (theta - np.sin(theta) * np.cos(theta)) / np.pi
    emp = np.arange(1, n + 1) / n
    ks = float(np.max(np.abs(emp - st_cdf)))

    gate = "all four moments within 3 sigma of Sato-Tate; Ramanujan bound exact"
    return core.row_result(
        7, "Sato-Tate for the icosian cuspidal L (our object)",
        "THEOREM: Barnet-Lamb-Geraghty-Harris-Taylor (non-CM Hilbert modular)",
        "the RATE (effective ST / discrepancy decay) = symmetric-power "
        "L-functions; sqrt-cancellation is the GRH-regime signature — open",
        {"n_angles": n, "dropped": "norm-31 Steinberg prime",
         "moments": {k: round(v, 4) for k, (v, _, _) in checks.items()},
         "st_targets": {"m1": 0.0, "m2": ST_M2, "m3": 0.0, "m4": ST_M4},
         "three_sigma": {k: round(3 * v, 4) for k, v in sd.items()},
         "ks_distance": round(ks, 4), "ramanujan_exact": ramanujan_ok},
        gate, "PASS" if ok else "FAIL",
        "Recompute the Brandt eigenvalues to a higher norm bound: ST is a "
        "theorem for this object, so a persistent moment deviation means the "
        "GEOMETRIC eigenvalues are wrong — this row audits our own data.")


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
