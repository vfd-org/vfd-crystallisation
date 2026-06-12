"""Cuspidal-dimension sequence at every split prime level (Table 1 of the
paper): geometry's h - 1 vs Dembele's published table, norms 11..89.

Run:  python3 route_b/multilevel_dimensions.py   (from realization/)
Writes data/dimension_sequence.json.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brandt_level as bl  # noqa: E402

# Dembele (2005), Tables/Examples: prime levels over Q(sqrt5).
# Split norms 11..29 carry no cusp form; 31 is the first.
DEMBELE = {11: 0, 19: 0, 29: 0, 31: 1, 41: 1, 59: 0, 61: 2, 71: 1, 79: 1, 89: 1}
DISPLAYED_RANGE = (31, 41, 59, 61, 71, 79, 89)  # the 7/7 table in the paper


def run():
    rows, ok = [], True
    for p in sorted(DEMBELE):
        dim = bl.cuspidal_dimension(p)
        match = dim == DEMBELE[p]
        ok &= match
        rows.append({"norm": p, "geometric_cuspidal_dim": dim,
                     "dembele_dim": DEMBELE[p], "match": match,
                     "in_displayed_table": p in DISPLAYED_RANGE})
    return {"description": "cuspidal dimension = Brandt h - 1 at split prime "
                           "levels, geometry vs Dembele (2005)",
            "displayed_table_levels": list(DISPLAYED_RANGE),
            "displayed_table_agreements": "%d/%d" % (
                sum(r["match"] for r in rows if r["in_displayed_table"]),
                len(DISPLAYED_RANGE)),
            "all_levels_tested": len(rows), "all_match": ok, "rows": rows}


if __name__ == "__main__":
    out = run()
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(here, "data", "dimension_sequence.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=2)
    for r in out["rows"]:
        print("norm %3d  geom %d  dembele %d  %s" % (
            r["norm"], r["geometric_cuspidal_dim"], r["dembele_dim"],
            "OK" if r["match"] else "MISMATCH"))
    print("displayed table: %s   all levels: %s" % (
        out["displayed_table_agreements"],
        "ALL MATCH" if out["all_match"] else "MISMATCH"))
