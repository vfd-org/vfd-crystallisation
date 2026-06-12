"""Level 31, all prime ideals of norm <= 200: geometry vs point counts.

For every good prime ideal in data/target_a_p.json (44 ideals over 24
rational-prime norm buckets, both Galois-conjugate ideals listed at each
split prime): build the geometric Hecke eigenvalue(s) at level 31 and
compare. At a split norm the two totally-positive generators varpi and
sigma(varpi) yield the two eigenvalues, and the geometric SET must equal
the point-counted set {a_P, a_P'} exactly; at inert and ramified norms
the single value must match. Nothing is fitted; the target file was
produced by brute-force point counting only.

Run:  python3 route_b/level31_full_ideals.py   (from realization/)
Writes data/level31_per_ideal.json.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brandt_level as bl       # noqa: E402
import brandt_matrices as bm    # noqa: E402

LEVEL = 31


def run():
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(here, "data", "target_a_p.json")) as fh:
        target = json.load(fh)

    buckets = {}
    for r in target["primes"]:
        buckets.setdefault(r["norm"], []).append(r)

    eng = bl.engine_for(LEVEL)
    rows, all_match, n_ideals = [], True, 0
    for norm in sorted(buckets):
        tgt_rows = buckets[norm]
        kind = tgt_rows[0]["kind"]
        tgt_set = sorted(r["a_p"] for r in tgt_rows)
        gen = bm.totally_positive_generator(norm)
        if gen is None:
            rows.append({"norm": norm, "kind": kind,
                         "note": "no totally-positive generator found"})
            all_match = False
            continue
        if norm == LEVEL:
            # The rational prime under the level: one of the two ideals IS the
            # level ideal (the kernel of (a,b) -> a + b*phi_root mod 31 fixed
            # by the level splitting -- a purely geometric criterion, no
            # target consulted). Its Brandt value is the Steinberg datum at
            # the level, not a good Hecke eigenvalue; only the conjugate
            # (good) ideal is compared against the point-count target.
            root = eng.spl.phi
            cands = [gen, bl.galois_conj(gen)]
            good = [g for g in cands if (g[0] + g[1] * root) % LEVEL != 0]
            lvl = [g for g in cands if (g[0] + g[1] * root) % LEVEL == 0]
            assert len(good) == 1 and len(lvl) == 1
            geo = [eng.brandt_matrix(good[0])["cuspidal_eigenvalue"]]
            steinberg = eng.brandt_matrix(lvl[0])["cuspidal_eigenvalue"]
        elif kind == "split":
            geo = sorted({eng.brandt_matrix(gen)["cuspidal_eigenvalue"],
                          eng.brandt_matrix(bl.galois_conj(gen))["cuspidal_eigenvalue"]})
        else:
            geo = [eng.brandt_matrix(gen)["cuspidal_eigenvalue"]]
        # a split bucket can have equal conjugate eigenvalues (a = a'):
        # the geometric set then collapses to one value, like the target set
        match = sorted(set(geo)) == sorted(set(tgt_set))
        ram = all(abs(a) <= 2 * math.sqrt(norm) + 1e-9 for a in geo)
        all_match &= match
        n_ideals += len(tgt_rows)
        row = {"norm": norm, "kind": kind, "n_ideals": len(tgt_rows),
               "geometric": geo, "point_count": tgt_set,
               "ramanujan": ram, "match": match}
        if norm == LEVEL:
            row["steinberg_at_level_ideal"] = steinberg
            row["note"] = ("level ideal excluded from good-prime comparison; "
                           "its Brandt value is the Steinberg datum used by "
                           "the Atkin-Lehner sign check (W = -a = +1)")
        rows.append(row)

    return {"level": LEVEL, "curve": target["curve"],
            "norm_bound": target["norm_bound"],
            "comparison": "per rational-prime norm bucket; at split norms the "
                          "geometric eigenvalue set {a(varpi), a(sigma varpi)} "
                          "must equal the point-counted set for the two ideals",
            "n_norm_buckets": len(rows), "n_prime_ideals": n_ideals,
            "all_match": all_match, "rows": rows}


if __name__ == "__main__":
    out = run()
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(here, "data", "level31_per_ideal.json"), "w") as fh:
        json.dump(out, fh, indent=2)
    for r in out["rows"]:
        if "note" in r:
            print("  N=%3d %s" % (r["norm"], r["note"]))
        else:
            print("  N=%3d %-8s ideals=%d  geom %-12s == target %-12s  %s" % (
                r["norm"], r["kind"], r["n_ideals"], r["geometric"],
                r["point_count"], r["match"]))
    print("LEVEL 31: %d ideals over %d norm buckets, ALL MATCH: %s "
          "-> data/level31_per_ideal.json" % (out["n_prime_ideals"],
                                              out["n_norm_buckets"],
                                              out["all_match"]))
