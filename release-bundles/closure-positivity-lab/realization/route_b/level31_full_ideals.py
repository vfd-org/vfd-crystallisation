"""Level 31, all prime ideals of norm <= 200: TRUE per-ideal comparison.

Convention (verified, not assumed, by this script): the engine's level
splitting sends phi to the root r0 = 13 of x^2 - x - 1 mod 31, so the
engine's level ideal is the kernel of (a, b) -> a + b*r0 — the GALOIS
CONJUGATE sigma(p31) of the conductor p31 = (5 phi - 2) of the reference
curve 31.1-a1. Consequently the geometric Hecke system is the
sigma-conjugate of the curve's system: for every good prime ideal P
(labeled in data/target_a_p.json by its root phi_mod_p), the Brandt
eigenvalue at a generator of sigma(P) equals the point-counted a_P.
ONE global involution, fixed once by the root choice, must explain every
assignment — the script verifies this per ideal and FAILS if any single
ideal needs its own adjustment.

Run:  python3 route_b/level31_full_ideals.py   (from realization/)
Writes data/level31_per_ideal.json (one row per prime ideal, 44 rows).
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brandt_level as bl       # noqa: E402
import brandt_matrices as bm    # noqa: E402
import ideal_classes as ic      # noqa: E402

LEVEL = 31
CONDUCTOR_GEN = (-2, 5)         # 5 phi - 2 in (a, b) coords for a + b*phi


def in_ideal(g, p, root):
    """g = a + b*phi lies in the prime over p with phi = root iff
    a + b*root = 0 mod p."""
    a, b = g
    return (a + b * root) % p == 0


def run():
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(here, "data", "target_a_p.json")) as fh:
        target = json.load(fh)

    spl = ic.LocalSplitting(LEVEL)
    r0 = spl.phi
    engine_level_is_conjugate = not in_ideal(CONDUCTOR_GEN, LEVEL, r0)

    eng = bl.engine_for(LEVEL)
    rows, all_match, n_ideals = [], True, 0
    buckets = {}
    for r in target["primes"]:
        buckets.setdefault(r["p"], []).append(r)

    for p in sorted(buckets):
        pair = buckets[p]
        kind = pair[0]["kind"]
        gen = bm.totally_positive_generator(pair[0]["norm"])
        if gen is None:
            rows.append({"p": p, "note": "no totally-positive generator"})
            all_match = False
            continue
        if kind != "split":
            # inert/ramified: Galois-stable ideal, no labeling subtlety
            a_geo = eng.brandt_matrix(gen)["cuspidal_eigenvalue"]
            t = pair[0]
            match = a_geo == t["a_p"]
            all_match &= match
            n_ideals += 1
            rows.append({"p": p, "norm": t["norm"], "kind": kind,
                         "phi_mod_p": None, "generator": list(gen),
                         "geometric_a": a_geo, "target_a_p": t["a_p"],
                         "match": match})
            continue
        # split: label each target ideal by its root; the geometric value AT
        # ideal P is the Brandt eigenvalue at a generator of sigma(P) — the
        # single global convention verified bucket-by-bucket here.
        for t in pair:
            root = t["phi_mod_p"]
            g_P = gen if in_ideal(gen, p, root) else bl.galois_conj(gen)
            g_sigmaP = bl.galois_conj(g_P)
            a_geo = eng.brandt_matrix(g_sigmaP)["cuspidal_eigenvalue"]
            ram = abs(a_geo) <= 2 * math.sqrt(t["norm"]) + 1e-9
            match = a_geo == t["a_p"]
            all_match &= match
            n_ideals += 1
            rows.append({"p": p, "norm": t["norm"], "kind": "split",
                         "phi_mod_p": root, "ideal_generator": list(g_P),
                         "evaluated_at_sigma_generator": list(g_sigmaP),
                         "geometric_a": a_geo, "target_a_p": t["a_p"],
                         "ramanujan": ram, "match": match})

    # Steinberg datum at the engine's own level ideal (kernel of the splitting)
    g31 = bm.totally_positive_generator(31)
    g31 = g31 if in_ideal(g31, 31, r0) else bl.galois_conj(g31)
    steinberg = eng.brandt_matrix(g31)["cuspidal_eigenvalue"]

    return {"level_norm": LEVEL,
            "curve": target["curve"],
            "engine_splitting_root": r0,
            "engine_level_ideal": "sigma(5phi-2)" if engine_level_is_conjugate
                                  else "(5phi-2)",
            "convention": "the geometry realizes the sigma-conjugate of the "
                          "reference Hecke system: geometric a at ideal P = "
                          "Brandt eigenvalue at a generator of sigma(P). One "
                          "global involution, fixed by the splitting root; "
                          "all_match=true certifies that no per-ideal "
                          "adjustment was needed anywhere.",
            "norm_bound": target["norm_bound"],
            "n_prime_ideals": n_ideals,
            "steinberg_at_engine_level_ideal": steinberg,
            "all_match": all_match, "rows": rows}


if __name__ == "__main__":
    out = run()
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(here, "data", "level31_per_ideal.json"), "w") as fh:
        json.dump(out, fh, indent=2)
    for r in out["rows"]:
        if "note" in r:
            print("  p=%3d %s" % (r["p"], r["note"]))
        else:
            print("  p=%3d N=%3d %-8s r=%-4s geom=%4d target=%4d  %s" % (
                r["p"], r["norm"], r["kind"], str(r.get("phi_mod_p")),
                r["geometric_a"], r["target_a_p"], r["match"]))
    print("engine level: %s (root %d); Steinberg at engine level ideal: %d" %
          (out["engine_level_ideal"], out["engine_splitting_root"],
           out["steinberg_at_engine_level_ideal"]))
    print("LEVEL 31: %d prime ideals, per-ideal ALL MATCH: %s "
          "-> data/level31_per_ideal.json" % (out["n_prime_ideals"],
                                              out["all_match"]))
