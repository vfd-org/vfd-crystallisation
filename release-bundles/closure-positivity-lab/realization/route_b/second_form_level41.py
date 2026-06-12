"""Level 41: the second rational eigenform, geometry vs point counts.

Geometry side: Brandt module of the icosian order at level 41 via
brandt_level.py (h = 2, cuspidal dim 1). Target side: brute-force point
counts of Dembele's E_41 = [0, -phi, phi, 0, 0], named explicitly at the
call site. The two sides meet only at the comparison below; nothing is
fitted.

Run:  python3 route_b/second_form_level41.py   (from realization/)
Writes data/level41_results.json.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brandt_level as bl           # noqa: E402
import brandt_matrices as bm        # noqa: E402
import point_count_target as pct    # noqa: E402

LEVEL = 41
TEST_NORMS = (11, 19, 29, 31, 59, 61, 71, 79, 89)  # split, coprime to 41


def run():
    gate = bl.compute_orbits_p(LEVEL)
    eng = bl.engine_for(LEVEL)
    assert len(gate["p1_points"]) == LEVEL + 1

    # target: Dembele's E_41 (Table 4), named explicitly
    with pct.curve((0, 0), (0, -1), (0, 1), (0, 0), (0, 0)):
        target = {}
        for r in pct.compute_target(norm_bound=100):
            if r["norm"] != LEVEL:
                target.setdefault(r["norm"], set()).add(r["a_p"])

    rows, all_match = [], True
    for q in TEST_NORMS:
        g = bm.totally_positive_generator(q)
        if g is None or q not in target:
            continue
        geo = sorted({eng.brandt_matrix(g)["cuspidal_eigenvalue"],
                      eng.brandt_matrix(bl.galois_conj(g))["cuspidal_eigenvalue"]})
        tgt = sorted(target[q])
        ram = all(abs(a) <= 2 * math.sqrt(q) + 1e-9 for a in geo)
        match = geo == tgt
        all_match &= match
        rows.append({"norm": q, "geometric_set": geo, "point_count_set": tgt,
                     "ramanujan": ram, "match": match})

    return {"level": LEVEL, "curve": "E_41 = [0,-phi,phi,0,0] (Dembele Table 4)",
            "brandt_h": gate["h"], "cuspidal_dim": gate["h"] - 1,
            "orbit_sizes": gate["orbit_sizes"],
            "comparison": "geometric eigenvalue set {a(varpi), a(sigma varpi)} "
                          "vs point-counted {a_q, a_q'} per split norm",
            "n_norms_tested": len(rows), "all_match": all_match, "rows": rows}


if __name__ == "__main__":
    out = run()
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(here, "data", "level41_results.json"), "w") as fh:
        json.dump(out, fh, indent=2)
    print("LEVEL 41: h=%d, cuspidal dim %d" % (out["brandt_h"], out["cuspidal_dim"]))
    for r in out["rows"]:
        print("  N(q)=%3d  geom %-12s == target %-12s  %s" % (
            r["norm"], r["geometric_set"], r["point_count_set"], r["match"]))
    print("ALL MATCH (no fit): %s  -> data/level41_results.json" % out["all_match"])
