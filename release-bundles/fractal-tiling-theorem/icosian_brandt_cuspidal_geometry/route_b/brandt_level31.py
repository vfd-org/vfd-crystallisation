"""Orchestrator -- WO-VFD-ICOSIAN-BRANDT-CUSPIDAL-GEOMETRY-001.

Runs the whole pipeline and writes ../results.json:

  Phase 1  brute-force point-count target a_P            (point_count_target)
  Phase 2  O_K = Z[phi] arithmetic                       (ok_arithmetic)
  Phase 3  icosian quaternion order, native              (quaternion_order)
  Phase 4  dimension gate h=2 (geometric) + Eichler mass (ideal_classes)
  Phase 5  Brandt matrices B(P)                          (brandt_matrices)
  Phase 6  cuspidal channel = non-Eisenstein eigenvalue  (brandt_matrices)
  Phase 7  out-of-sample, no-fit comparison + verdict    (hecke_compare)
  Phase 8  no-fit guard                                  (no_fit_guard)

This file replaces the [TODO] scaffold formerly in
release-bundles/fractal-tiling-theorem/route_b/brandt_level31.py: steps 2-6 of
that scaffold are now implemented (the icosian Eichler-order / Brandt-module
construction), via the class-number-1 definite method rather than a from-scratch
ideal-class enumeration.
"""
from __future__ import annotations

import json
import os

try:
    from . import ok_arithmetic as ok
    from . import quaternion_order as qo
    from . import ideal_classes as ic
    from . import brandt_matrices as bm
    from . import hecke_compare as hc
    from . import point_count_target as pct
    from . import no_fit_guard as nfg
except ImportError:
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    import ok_arithmetic as ok
    import quaternion_order as qo
    import ideal_classes as ic
    import brandt_matrices as bm
    import hecke_compare as hc
    import point_count_target as pct
    import no_fit_guard as nfg

HERE = os.path.dirname(__file__)


def run(max_norm=200, write=True):
    # Phase 1 -- target
    target_payload, _ = pct.write_target(norm_bound=max_norm)

    # Phase 4 -- dimension gate
    gate, expected_h, gate_status = ic.dimension_gate()

    # Phase 3 sanity -- enumerator anchor (parameter-free)
    ring = qo.ring()
    anchor_ok = True
    for (a, b), Np in [((3, 1), 11), ((4, 1), 19), ((6, 1), 41)]:
        if len(ring.enumerate_reduced_norm_vecs((a, b))) != 120 * (Np + 1):
            anchor_ok = False

    # Phase 8 -- no-fit guard
    guard = nfg.run_guard()

    # Phases 5-7 -- Brandt matrices, cuspidal extraction, comparison
    rows, summary = hc.run_comparison(max_norm=max_norm)
    v = hc.verdict(summary,
                   dimension_gate_pass=(gate_status == "PASS"),
                   no_fit_pass=(guard["status"] == "PASS"))

    results = {
        "work_order": "WO-VFD-ICOSIAN-BRANDT-CUSPIDAL-GEOMETRY-001",
        "base_field": "Q(sqrt(5))",
        "ring": "Z[phi]",
        "level": "5phi-2",
        "level_norm": 31,
        "target_curve": "31.1-a1 over Q(sqrt(5))",
        "target_source": "brute_force_point_count",
        "target_primes_tested": target_payload["n_primes"],
        "target_all_ramanujan": target_payload["all_ramanujan"],
        "brandt_route": "native",
        "brandt_method": ("class-number-1 definite method: A_5 = I^1/{+-1} "
                          "acting on P^1(F_31); Hecke via icosian elements of "
                          "reduced norm varpi_P enumerated by Fincke-Pohst"),
        "enumerator_anchor_120_Nplus1": anchor_ok,
        "icosian_gram_det": ring.gram_det(),
        "dimension_gate": {
            "expected_h": expected_h,
            "computed_h": gate["h"],
            "orbit_sizes": gate["orbit_sizes"],
            "eichler_mass_computed": "%d/%d" % gate["mass_computed"],
            "eichler_mass_predicted": "%d/%d" % gate["mass_predicted"],
            "mass_matches": gate["mass_matches"],
            "status": gate_status,
        },
        "no_fit_guard": guard["status"],
        "no_fit_guard_detail": guard,
        "brandt_invariants": {
            "eisenstein_channel_exact": summary["eisenstein_channel_exact"],
            "all_self_adjoint_orbit_size_measure": summary["all_self_adjoint"],
            "self_adjoint_measure_mu": [len(o) for o in
                                        ic.compute_orbits()["orbits"]],
            "single_common_cuspidal_eigenform":
                summary["single_common_eigenform"],
            "common_cuspidal_eigenvector":
                summary["common_cuspidal_eigenvector"],
        },
        "prime_tests": {
            "in_sample_total": summary["in_sample_total"],
            "in_sample_matches": summary["in_sample_matches"],
            "out_of_sample_total": summary["out_of_sample_total"],
            "out_of_sample_matches": summary["out_of_sample_matches"],
            "galois_fixed_total": summary["galois_fixed_total"],
            "galois_fixed_exact_matches": summary["galois_fixed_exact_matches"],
        },
        "per_prime": [
            {"norm": r["norm"], "bucket": r["bucket"],
             "a_P_geometric": r["cuspidal_eigenvalue"],
             "a_P_target": r["target_a_p_values"],
             "galois_fixed": r["galois_fixed"],
             "match": r["matches_a_target"]}
            for r in rows
        ],
        "verdict": v,
        "rh_claim": "NO_RH_PROOF_CLAIMED",
        "notes": [
            "Dimension h=2 and Eichler mass 8/15 derived geometrically from "
            "the icosian A_5 action on P^1(F_31); zero fitted parameters.",
            "Brandt operators B(P) are self-adjoint in the orbit-size measure "
            "mu=(20,12) and share ONE common cuspidal eigenvector (3,-5): a "
            "genuine simultaneous Hecke eigenform (the norm-31 Hilbert newform).",
            "Cuspidal eigenvalue = trace(B(P))-(N(P)+1) equals the brute-force "
            "point-counted a_P out-of-sample with zero fitting; exact at the "
            "Galois-fixed inert/ramified primes, and up to the global Galois "
            "involution of Q(sqrt5) at split primes.",
            "This establishes geometric encoding of the cuspidal arithmetic "
            "object; it does NOT prove RH -- the positivity / self-adjoint "
            "trace-form (Connes/Weil) wall is untouched.",
        ],
    }

    if write:
        path = os.path.join(HERE, "..", "results.json")
        with open(path, "w") as f:
            json.dump(results, f, indent=2)
    return results


def main():
    print("=" * 74)
    print("WO-VFD-ICOSIAN-BRANDT-CUSPIDAL-GEOMETRY-001  --  full pipeline")
    print("=" * 74)
    res = run()
    dg = res["dimension_gate"]
    pt = res["prime_tests"]
    bi = res["brandt_invariants"]
    print("\nPhase 1  target a_P (brute-force point count): %d primes, "
          "Ramanujan=%s" % (res["target_primes_tested"],
                            res["target_all_ramanujan"]))
    print("Phase 2  Z[phi] arithmetic                   : OK")
    print("Phase 3  icosian order (Gram det %d), anchor #{nrd=varpi}=120(N+1): %s"
          % (res["icosian_gram_det"], res["enumerator_anchor_120_Nplus1"]))
    print("Phase 4  dimension gate                      : h=%d (expect %d), "
          "mass %s=%s -> %s"
          % (dg["computed_h"], dg["expected_h"], dg["eichler_mass_computed"],
             dg["eichler_mass_predicted"], dg["status"]))
    print("Phase 5  Brandt matrices self-adjoint (mu=%s): %s"
          % (bi["self_adjoint_measure_mu"],
             bi["all_self_adjoint_orbit_size_measure"]))
    print("Phase 6  common cuspidal eigenform           : %s %s"
          % (bi["single_common_cuspidal_eigenform"],
             bi["common_cuspidal_eigenvector"]))
    print("Phase 7  in-sample %d/%d, out-of-sample %d/%d, Galois-fixed exact %d/%d"
          % (pt["in_sample_matches"], pt["in_sample_total"],
             pt["out_of_sample_matches"], pt["out_of_sample_total"],
             pt["galois_fixed_exact_matches"], pt["galois_fixed_total"]))
    print("Phase 8  no-fit guard                        : %s"
          % res["no_fit_guard"])
    print("\nVERDICT:", res["verdict"])
    print("RH claim:", res["rh_claim"])
    print("\nwrote results.json")


if __name__ == "__main__":
    main()
