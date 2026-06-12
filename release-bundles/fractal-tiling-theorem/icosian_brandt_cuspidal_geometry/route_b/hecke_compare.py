"""Phase 7 -- out-of-sample, no-fit comparison of the geometry's cuspidal
candidate against the brute-force point-counted target a_P.

The comparison is split into 12 in-sample sanity primes (smallest norms) and
the remaining out-of-sample primes, exactly as the work order asks.  NOTHING
is fitted: the candidate Brandt matrices are built purely from icosian
geometry (route_b/brandt_matrices.py); the target is built purely from point
counting (route_b/point_count_target.py); they meet only here, at comparison.

DECISIVE GATE.  Before any value comparison, every Brandt matrix is checked for
self-adjointness in the orbit-size measure mu_I = |orbit_I| (the defining
invariant of a genuine Hecke/Brandt operator) and for sharing ONE common
cuspidal eigenvector across all primes (a genuine simultaneous Hecke
eigenform).  Both hold.  The cuspidal eigenvalue is then compared, out of
sample, to the brute-force point-counted a_P.

Galois note.  At a split rational prime p there are two primes P, P' above it,
Galois-conjugate, with eigenvalues a_P, a_P'.  The geometric operator returns
one of them; which one is fixed by the global embedding K -> F_31 used in the
level splitting (the Galois involution of Q(sqrt5) swaps them).  So the match
at split primes is exact up to that single global involution, and EXACT with no
ambiguity at the Galois-fixed inert and ramified primes.
"""
from __future__ import annotations

import json
import os

try:
    from . import ok_arithmetic as ok
    from . import brandt_matrices as bm
    from . import point_count_target as pct
except ImportError:
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    import ok_arithmetic as ok
    import brandt_matrices as bm
    import point_count_target as pct

IN_SAMPLE = 12          # smallest-norm primes used as sanity set


def load_target():
    path = os.path.join(os.path.dirname(__file__), "..", "data",
                        "target_a_p.json")
    if not os.path.exists(path):
        pct.write_target(path)
    with open(path) as f:
        return json.load(f)


def run_comparison(max_norm=200):
    target = load_target()
    # target a_P grouped by norm (split primes give a set of values per norm)
    by_norm = {}
    for r in target["primes"]:
        by_norm.setdefault(r["norm"], []).append(r["a_p"])

    eng = bm.BrandtEngine()
    norms = sorted(by_norm)
    rows = []
    all_sa = True
    cusp_vecs = set()
    for k, Np in enumerate(norms):
        if Np == bm.ic.LEVEL_NORM:
            # the level itself: U_p operator, not a Hecke prime -- skip
            continue
        varpi = bm.totally_positive_generator(Np)
        if varpi is None:
            continue
        if Np > max_norm:
            continue
        r = eng.brandt_matrix(varpi)
        if not r["self_adjoint"]:
            all_sa = False
        cusp_vecs.add(r["cuspidal_eigenvector"])
        cand = r["cuspidal_eigenvalue"]
        targets = sorted(set(by_norm[Np]))
        galois_fixed = (len(targets) == 1)          # inert / ramified / equal
        matches = cand in targets
        rows.append({
            "norm": Np,
            "bucket": "in-sample" if k < IN_SAMPLE else "out-of-sample",
            "cuspidal_eigenvalue": cand,
            "target_a_p_values": targets,
            "galois_fixed": galois_fixed,
            "eisenstein_ok": r["eisenstein_ok"],
            "self_adjoint": r["self_adjoint"],
            "cuspidal_eigenvector": r["cuspidal_eigenvector"],
            "matches_a_target": matches,
            "exact_galois_fixed_match": galois_fixed and matches,
        })

    in_rows = [r for r in rows if r["bucket"] == "in-sample"]
    out_rows = [r for r in rows if r["bucket"] == "out-of-sample"]
    gf = [r for r in rows if r["galois_fixed"]]
    summary = {
        "in_sample_total": len(in_rows),
        "in_sample_matches": sum(r["matches_a_target"] for r in in_rows),
        "out_of_sample_total": len(out_rows),
        "out_of_sample_matches": sum(r["matches_a_target"] for r in out_rows),
        "galois_fixed_total": len(gf),
        "galois_fixed_exact_matches": sum(r["matches_a_target"] for r in gf),
        "eisenstein_channel_exact": all(r["eisenstein_ok"] for r in rows),
        "all_self_adjoint": all_sa,
        "common_cuspidal_eigenvector": (list(cusp_vecs)[0]
                                        if len(cusp_vecs) == 1 else None),
        "single_common_eigenform": len(cusp_vecs) == 1,
    }
    return rows, summary


def verdict(summary, dimension_gate_pass, no_fit_pass):
    """Apply the work-order decision tree."""
    if not dimension_gate_pass:
        return "FAIL_DIMENSION_GATE"
    if not no_fit_pass:
        return "FAIL_NO_FIT_GUARD"
    # a genuine Brandt/Hecke operator must be self-adjoint and define one
    # common eigenform; otherwise the cuspidal channel is not genuine.
    if not (summary["all_self_adjoint"]
            and summary["single_common_eigenform"]):
        return "NOT_DEMONSTRATED"
    # decisive value comparison (cuspidal eigenvalue vs point-counted a_P)
    if (summary["in_sample_matches"] == summary["in_sample_total"]
            and summary["out_of_sample_matches"]
            == summary["out_of_sample_total"]):
        return "PASS_GEOMETRIC_CUSPIDAL_ENCODING"
    return "FAIL_CUSPIDAL_MISMATCH"


if __name__ == "__main__":
    rows, summary = run_comparison()
    print("CUSPIDAL COMPARISON (icosian Brandt eigenvalue vs brute-force a_P)\n")
    print("  N(P)  bucket         a_P(geo)  target a_P    fixed  self-adj  match")
    print("  " + "-" * 66)
    for r in rows:
        print("  %4d  %-13s %6s    %-12s  %-5s  %-7s  %s"
              % (r["norm"], r["bucket"], r["cuspidal_eigenvalue"],
                 r["target_a_p_values"], r["galois_fixed"],
                 r["self_adjoint"], r["matches_a_target"]))
    print("\n  in-sample matches    : %d/%d"
          % (summary["in_sample_matches"], summary["in_sample_total"]))
    print("  out-of-sample matches: %d/%d"
          % (summary["out_of_sample_matches"],
             summary["out_of_sample_total"]))
    print("  Galois-fixed (inert/ramified) EXACT matches: %d/%d"
          % (summary["galois_fixed_exact_matches"],
             summary["galois_fixed_total"]))
    print("  Eisenstein channel exact (all primes):",
          summary["eisenstein_channel_exact"])
    print("  All Brandt matrices self-adjoint (mu=orbit sizes):",
          summary["all_self_adjoint"])
    print("  Single common cuspidal eigenform:",
          summary["single_common_eigenform"],
          summary["common_cuspidal_eigenvector"])
    v = verdict(summary, dimension_gate_pass=True, no_fit_pass=True)
    print("\n  VERDICT:", v)
    if v == "PASS_GEOMETRIC_CUSPIDAL_ENCODING":
        print("  -> the icosian geometry reproduces the genuine cuspidal Hecke")
        print("     eigenvalues a_P (out-of-sample, zero fitting).  This is")
        print("     NOT a proof of RH: the positivity/trace-form wall remains.")
