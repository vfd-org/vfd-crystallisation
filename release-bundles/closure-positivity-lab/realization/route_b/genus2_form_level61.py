"""Level 61: the genus-2 form with real multiplication by Q(sqrt5).

Geometry side: Brandt module at level 61 via brandt_level.py (h = 3,
cuspidal dim 2). The 2x2 cuspidal block of each Brandt operator has an
eigenvalue pair a, sigma(a) in Z[phi]; we read off its rational invariants
Tr(a) and N(a) from the trace and determinant of the Brandt matrix, and
check (i) the discriminant Tr^2 - 4N is 5 x (perfect square), i.e. the
eigenvalues generate Q(sqrt5) — real multiplication; (ii) Ramanujan on
both embeddings; (iii) at the inert primes 4, 9, 49, agreement with the
(Tr, N) of Dembele's published level-61 coefficients. Tested at the six
primes listed in TEST_NORMS; no claim is made beyond them.

Run:  python3 route_b/genus2_form_level61.py   (from realization/)
Writes data/level61_results.json.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brandt_level as bl       # noqa: E402
import brandt_matrices as bm    # noqa: E402

LEVEL = 61
TEST_NORMS = (4, 9, 11, 19, 29, 49)
INERT = {4, 9, 49}
# Dembele level-61 column (genus-2 form, RM by Q(sqrt5)); a in Z[phi];
# rational invariants (Tr, N) over Q at the inert (Galois-unambiguous) primes:
#   a_4 = 2w-2 -> (-2,-4);  a_9 = -w-2 -> (-5,5);  a_49 = -4w+2 -> (0,-20)
DEMBELE = {4: ("2w-2", -2, -4), 9: ("-w-2", -5, 5), 49: ("-4w+2", 0, -20)}


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def run():
    gate = bl.compute_orbits_p(LEVEL)
    eng = bl.engine_for(LEVEL)
    assert gate["h"] == 3, "level 61 must have Brandt h = 3 (cuspidal dim 2)"

    rows, all_rm, all_ram, all_dembele = [], True, True, True
    for nq in TEST_NORMS:
        gen = bm.totally_positive_generator(nq)
        if gen is None:
            rows.append({"norm": nq, "note": "no totally-positive generator"})
            continue
        B = eng.brandt_matrix(gen)["matrix"]
        tr, dt = sum(B[i][i] for i in range(3)), det3(B)
        tr_a = tr - (nq + 1)          # cuspidal-block trace
        n_a = dt / (nq + 1)           # cuspidal-block determinant
        tr_a = int(tr_a) if getattr(tr_a, "denominator", 1) == 1 else float(tr_a)
        n_a = int(n_a) if getattr(n_a, "denominator", 1) == 1 else float(n_a)
        disc = tr_a * tr_a - 4 * n_a
        rm = (isinstance(disc, int) and disc > 0 and disc % 5 == 0
              and math.isqrt(disc // 5) ** 2 == disc // 5)
        rt = math.sqrt(float(disc)) if float(disc) > 0 else 0.0
        e1, e2 = (float(tr_a) + rt) / 2, (float(tr_a) - rt) / 2
        ram = max(abs(e1), abs(e2)) <= 2 * math.sqrt(nq) + 1e-9
        row = {"norm": nq, "kind": "inert" if nq in INERT else "split",
               "trace_a": tr_a, "norm_a": n_a, "disc": disc,
               "rm_by_sqrt5": rm, "ramanujan_both_embeddings": ram}
        if nq in DEMBELE:
            label, t_exp, n_exp = DEMBELE[nq]
            row["dembele_a"] = label
            row["dembele_match"] = (tr_a == t_exp and n_a == n_exp)
            all_dembele &= row["dembele_match"]
        all_rm &= rm
        all_ram &= ram
        rows.append(row)

    return {"level": LEVEL, "brandt_h": gate["h"],
            "cuspidal_dim": gate["h"] - 1, "orbit_sizes": gate["orbit_sizes"],
            "n_norms_tested": len(TEST_NORMS),
            "scope": "claims hold at the six tested primes only",
            "all_rm_by_sqrt5": all_rm, "all_ramanujan": all_ram,
            "all_dembele_inert_match": all_dembele, "rows": rows}


if __name__ == "__main__":
    out = run()
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(here, "data", "level61_results.json"), "w") as fh:
        json.dump(out, fh, indent=2)
    print("LEVEL 61: h=%d, cuspidal dim %d (genus-2)" % (out["brandt_h"],
                                                         out["cuspidal_dim"]))
    for r in out["rows"]:
        print("  N(q)=%3d %-6s Tr=%-4s N=%-5s disc=%-5s RM(sqrt5)=%-5s %s" % (
            r["norm"], r.get("kind", "?"), r.get("trace_a"), r.get("norm_a"),
            r.get("disc"), r.get("rm_by_sqrt5"),
            ("Dembele " + ("MATCH" if r.get("dembele_match") else "MISMATCH"))
            if "dembele_a" in r else ""))
    print("RM at all tested: %s | Ramanujan: %s | Dembele inert: %s "
          "-> data/level61_results.json" % (out["all_rm_by_sqrt5"],
                                            out["all_ramanujan"],
                                            out["all_dembele_inert_match"]))
