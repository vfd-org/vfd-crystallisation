"""
hecke_response_analyser.py
Grade D/E engine: map split primes to the level-31 Hilbert form's Hecke
eigenvalues a_q, group by base-2 order sector (5 | ord_q(2)), and test for
any Sato-Tate bias.

Result (Test 6 / prior Test A): NO bias -- the cyclotomic-order address is
DECOUPLED from the Hecke/spectral layer. The address map stops at splitting.
"""
import os, sys, math, statistics as st

# locate the icosian point-counter (independent target generator; no fitting)
_HERE = os.path.dirname(os.path.abspath(__file__))
_RB = os.path.join(_HERE, "..", "icosian_brandt_cuspidal_geometry", "route_b")


def _load_pct():
    sys.path.insert(0, _RB)
    import point_count_target as pct  # noqa
    return pct


def hecke_by_order_sector(norm_bound=2000):
    from sympy import n_order
    pct = _load_pct()
    rows = pct.compute_target(norm_bound=norm_bound)
    split = [r for r in rows if r["kind"] == "split" and r["norm"] != 31]
    G, NG = [], []
    table = []
    for r in split:
        q = r["p"]
        o = int(n_order(2, q))
        x = r["a_p"] / (2 * math.sqrt(r["norm"]))
        (G if o % 5 == 0 else NG).append(x)
        table.append({"q": q, "a_q": r["a_p"], "ord_q2": o,
                      "golden_order": o % 5 == 0, "sato_tate_x": round(x, 4)})
    summary = {
        "golden_n": len(G), "golden_mean": round(st.mean(G), 4),
        "golden_std": round(st.pstdev(G), 4),
        "control_n": len(NG), "control_mean": round(st.mean(NG), 4),
        "control_std": round(st.pstdev(NG), 4),
    }
    se = math.sqrt(st.pvariance(G) / len(G) + st.pvariance(NG) / len(NG))
    summary["mean_diff"] = round(st.mean(G) - st.mean(NG), 4)
    summary["sigma"] = round(abs(summary["mean_diff"]) / se, 2)
    summary["verdict"] = ("NO bias (decoupled): address stops at splitting"
                          if summary["sigma"] < 2 else "POSSIBLE bias -- investigate")
    return summary, table


if __name__ == "__main__":
    s, _ = hecke_by_order_sector()
    print("Hecke response by base-2 order sector (level-31 form):")
    for k, v in s.items():
        print(f"  {k}: {v}")
