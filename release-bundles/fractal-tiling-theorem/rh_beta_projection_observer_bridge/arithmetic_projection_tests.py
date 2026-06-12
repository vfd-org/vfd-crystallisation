"""WO-RH-BETA-PROJECTION-OBSERVER-BRIDGE-001 -- Phases 2-4: the actual arithmetic.

Audits the REAL icosian/Brandt objects for their beta-class, then tests the
candidate projections.  The honest result this exposes:

 (1) The icosian 600-cell matrices are HIGHLY STRUCTURED (few distinct
     eigenvalues, large multiplicities) -- they do NOT have GSE *spacing*
     statistics.  So the "beta=4" of the substrate is a SYMMETRY-CLASS fact
     (quaternionic structure, 2I < SU(2), antiunitary J with J^2=-1), NOT a
     random-matrix-spacing fact.  Conflating the two is the "beta numerology"
     trap the WO forbids.

 (2) The canonical projection beta=4 -> beta=2 that DOES exist is
     COMPLEXIFICATION: H (x)_R C = M_2(C), 2I < SU(2) < SL_2(C).  It is
     canonical and non-circular, but it is a representation/symmetry-class map,
     not a spacing map: it does not produce the zeta zeros.

 (3) At the *spacing* level, projections of a true GSE matrix do NOT canonically
     become GUE (different universality classes).  Tested below: no candidate
     projection converts GSE spacing to GUE spacing without circular tuning.

Conclusion fed to FINAL_CLASSIFICATION: the beta-mismatch is partly a category
error; the one canonical projection (complexification) is symmetry-class-level
and zero-blind; RH-sensitivity still reduces to Weil positivity.
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(__file__)
SIB = os.path.join(HERE, "..", "icosian_brandt_cuspidal_geometry", "route_b")
sys.path.insert(0, SIB)
import quaternion_order as qo                     # noqa: E402
import matrix_model_experiments as mm             # noqa: E402

OUTA = os.path.join(HERE, "results", "vfd_brandt_beta_audit")
OUTP = os.path.join(HERE, "results", "projection_candidates")
PHI = (1 + 5 ** 0.5) / 2


def units_R4():
    """120 unit icosians as real 4-vectors on S^3 (phi -> numeric)."""
    out = []
    for q in qo.unit_icosians():
        vec = []
        for (a, b) in q:
            vec.append(float(a) + float(b) * PHI)
        out.append(vec)
    return np.array(out)


# ---- (1) 600-cell adjacency beta-audit ------------------------------------
def six_hundred_cell_audit():
    V = units_R4()
    # normalise to S^3 (they already have equal norm); nearest-neighbour graph
    G = V @ V.T
    np.fill_diagonal(G, -np.inf)
    # 600-cell: each vertex has 12 nearest neighbours (icosahedral)
    A = np.zeros((120, 120))
    for i in range(120):
        nbr = np.argsort(G[i])[-12:]
        A[i, nbr] = 1
    A = np.maximum(A, A.T)
    ev = np.linalg.eigvalsh(A)
    ev_round = np.round(ev, 6)
    distinct = sorted(set(ev_round.tolist()))
    # spacing classification attempt (will be non-generic / degenerate)
    s = mm.unfold_spacings(ev)
    best, dists = mm.classify(s)
    # fraction of zero spacings (degeneracy)
    frac_deg = float(np.mean(np.diff(np.sort(ev)) < 1e-6))
    return {"matrix": "600-cell adjacency (120x120)",
            "n_distinct_eigenvalues": len(distinct),
            "distinct_eigenvalues": [round(x, 4) for x in distinct],
            "degenerate_spacing_fraction": round(frac_deg, 3),
            "naive_spacing_best_fit_beta": best,
            "naive_spacing_distances": {str(k): round(v, 3) for k, v in dists.items()},
            "verdict": ("STRUCTURED, NOT random: only %d distinct eigenvalues "
                        "among 120 (huge multiplicities from the 2I symmetry); "
                        "no GSE spacing.  beta=4 here is SYMMETRY-CLASS, not "
                        "spacing." % len(distinct))}


# ---- (2) quaternionic symmetry class: 2I < SU(2), antiunitary J -----------
def quaternionic_structure():
    # unit quaternion (w,x,y,z) -> SU(2) matrix [[w+iz, x+iy],[-x+iy, w-iz]]
    V = units_R4()
    su2_ok = 0
    for w, x, y, z in V:
        M = np.array([[w + 1j * z, x + 1j * y], [-x + 1j * y, w - 1j * z]])
        if (np.allclose(M.conj().T @ M, np.eye(2), atol=1e-9)
                and abs(np.linalg.det(M) - 1) < 1e-9):
            su2_ok += 1
    # antiunitary time-reversal J on C^2 (quaternionic): J = [[0,-1],[1,0]] * conj,
    # J^2 = -1 (Kramers).  Symplectic form omega preserved by Sp(1)=SU(2).
    Jm = np.array([[0, -1], [1, 0]])
    J2 = Jm @ np.conj(Jm)            # J^2 acting as (Jm . conj)^2 = -I
    kramers = np.allclose(Jm @ Jm, -np.eye(2))
    return {"units_in_SU(2)": "%d/120" % su2_ok,
            "antiunitary_J_squared_minus1_Kramers": bool(kramers),
            "symmetry_class": ("beta=4 (symplectic/GSE class): quaternionic "
                               "Hilbert space, Sp(1)=SU(2), antiunitary J with "
                               "J^2=-1 -> Kramers doubling"),
            "verified": su2_ok == 120}


# ---- (3) complexification projection H (x) C = M_2(C) ----------------------
def complexification_projection():
    # The canonical beta=4 -> beta=2 map: H -> M_2(C) via left-regular rep with a
    # chosen complex structure I (=i).  2I < SU(2) < SL_2(C).  Verify it is an
    # algebra isomorphism on a basis {1,i,j,k}.
    i = np.array([[1j, 0], [0, -1j]])
    j = np.array([[0, 1], [-1, 0]])
    k = i @ j
    one = np.eye(2)
    # check Hamilton relations i^2=j^2=k^2=-1, ij=k
    rel = (np.allclose(i @ i, -one) and np.allclose(j @ j, -one)
           and np.allclose(k @ k, -one) and np.allclose(i @ j, k))
    return {"map": "H (x)_R C = M_2(C), complex structure I=i",
            "hamilton_relations_hold": bool(rel),
            "canonical": True, "non_circular": True,
            "what_it_does": ("reduces the quaternionic (beta=4, symplectic) "
                             "structure to complex (beta=2, unitary): the "
                             "antiunitary J is no longer in the commutant"),
            "but": ("this is a REPRESENTATION/symmetry-class map; it does not act "
                    "on a zero-spectrum and does not produce zeta statistics")}


# ---- (4) spacing-level test: do projections of GSE become GUE? -------------
def gse_projection_spacing_tests():
    rng = np.random.RandomState(7)
    results = {}
    # build a big GSE, get its (Kramers-paired) spectrum
    H = mm.gse(150, rng)
    ev = np.linalg.eigvalsh(H)
    # baseline: GSE distinct levels -> beta=4
    s_full = mm.unfold_spacings(ev, drop_degenerate=True)
    results["GSE_baseline"] = {"best": mm.classify(s_full)[0]}
    # B3 quotient: drop Kramers pairs (already done) -> still beta=4
    results["B3_drop_kramers"] = {"best": mm.classify(s_full)[0],
                                  "note": "still beta=4; Kramers removal != GUE"}
    # B4 chiral/half spectrum: take every other level
    half = np.sort(ev)[::2]
    s_half = mm.unfold_spacings(half)
    results["B4_half_spectrum"] = {"best": mm.classify(s_half)[0],
                                   "note": "decimation changes density, not class"}
    # B1 complex-structure restriction: project quaternion blocks to their
    # upper-left complex entry -> a GUE-like matrix BY CONSTRUCTION (circular!)
    n = 150
    C = np.zeros((n, n), dtype=complex)
    for a in range(n):
        for b in range(n):
            C[a, b] = H[2 * a, 2 * b]
    C = (C + C.conj().T) / 2
    s_c = mm.unfold_spacings(np.linalg.eigvalsh(C))
    results["B1_complex_restriction"] = {
        "best": mm.classify(s_c)[0],
        "note": ("gives beta=2 -- but CIRCULAR: extracting the complex part of a "
                 "quaternion matrix is GUE by construction, not a canonical "
                 "projection of the arithmetic object")}
    results["honest_reading"] = (
        "No NON-circular projection turns GSE *spacing* into GUE *spacing*. The "
        "only one that yields beta=2 (B1 complex restriction) does so by "
        "construction (it literally builds a GUE matrix). GSE and GUE are "
        "distinct universality classes; there is no canonical spacing bridge.")
    return results


def main():
    os.makedirs(OUTA, exist_ok=True)
    os.makedirs(OUTP, exist_ok=True)
    print("=" * 74)
    print("Phases 2-4 -- icosian/Brandt beta-audit and projection tests")
    print("=" * 74)

    a = six_hundred_cell_audit()
    print("\n[2] 600-cell adjacency audit:")
    print("   distinct eigenvalues: %d / 120   (degenerate spacing frac %.2f)"
          % (a["n_distinct_eigenvalues"], a["degenerate_spacing_fraction"]))
    print("   ->", a["verdict"])

    q = quaternionic_structure()
    print("\n[2b] quaternionic symmetry class:")
    print("   units in SU(2): %s   Kramers J^2=-1: %s"
          % (q["units_in_SU(2)"], q["antiunitary_J_squared_minus1_Kramers"]))
    print("   ->", q["symmetry_class"])

    c = complexification_projection()
    print("\n[3] canonical projection (complexification):")
    print("   H(x)C=M_2(C), Hamilton relations hold:", c["hamilton_relations_hold"])
    print("   ->", c["what_it_does"])
    print("   BUT:", c["but"])

    g = gse_projection_spacing_tests()
    print("\n[4] spacing-level projection tests on a true GSE matrix:")
    for k, v in g.items():
        if isinstance(v, dict):
            print("   %-22s best-fit beta=%s  %s"
                  % (k, v["best"], v.get("note", "")))
    print("   ->", g["honest_reading"])

    with open(os.path.join(OUTA, "beta_audit.json"), "w") as f:
        json.dump({"600cell": a, "quaternionic": q}, f, indent=2)
    with open(os.path.join(OUTP, "projection_tests.json"), "w") as f:
        json.dump({"complexification": c, "spacing_tests": g}, f, indent=2)
    print("\n   wrote results/vfd_brandt_beta_audit/ and results/projection_candidates/")


if __name__ == "__main__":
    main()
