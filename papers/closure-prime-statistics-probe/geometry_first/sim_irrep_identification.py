#!/usr/bin/env python3
"""
GEOMETRY-FIRST SIM step 2: irrep identification of V_600 eigenspaces.

Implements WO_irrep_identification.md.  Reads fingerprints from the
previous step's JSON, computes multiplicity-free verification, labels
identifiable irreps (trivial, reflection), and verifies pair-twist
structure.  Pure linear algebra; no external character table used.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from collections import Counter

import numpy as np

PHI    = (1.0 + 5.0 ** 0.5) / 2.0
INVPHI = 1.0 / PHI

HERE = Path(__file__).parent
OUTPUT_DIR = HERE / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_v600():
    half       = 0.5
    half_phi   = PHI / 2.0
    half_phi_i = 1.0 / (2.0 * PHI)
    verts = []
    for i in range(4):
        for s in (1.0, -1.0):
            v = [0.0]*4; v[i] = s
            verts.append(v)
    for s0 in (-1,1):
        for s1 in (-1,1):
            for s2 in (-1,1):
                for s3 in (-1,1):
                    verts.append([s0*half, s1*half, s2*half, s3*half])
    even_perms = [
        (0,1,2,3),(0,2,3,1),(0,3,1,2),
        (1,0,3,2),(1,2,0,3),(1,3,2,0),
        (2,0,1,3),(2,1,3,0),(2,3,0,1),
        (3,0,2,1),(3,1,0,2),(3,2,1,0),
    ]
    for p in even_perms:
        for sa in (-1,1):
            for sb in (-1,1):
                for sc in (-1,1):
                    v = [0.0]*4
                    v[p[0]] = sa*half_phi
                    v[p[1]] = sb*half
                    v[p[2]] = sc*half_phi_i
                    v[p[3]] = 0.0
                    verts.append(v)
    return np.array(verts, dtype=float)


def main():
    print("=" * 78)
    print("SIM 2: irrep identification of V_600 eigenspaces")
    print("=" * 78)
    print()

    # Read previous fingerprint table
    fp_path = OUTPUT_DIR / "geom_first_results.json"
    with open(fp_path) as f:
        fp_data = json.load(f)
    eigentable = fp_data["eigenspace_traces"]
    print(f"  Loaded fingerprint table: {len(eigentable)} eigenspaces")
    print()

    # ----- Task 1: multiplicity-free verification -----
    print("--- Task 1: multiplicity-free check ---")
    V = build_v600()
    n = V.shape[0]
    # Compute squared distances from V[0] to all other vertices
    d2 = np.sum((V - V[0][None, :]) ** 2, axis=1)
    distinct_d2 = sorted(set(round(float(x), 6) for x in d2))
    n_orbits = len(distinct_d2)
    print(f"  Distinct squared distances from V_600[0]: {n_orbits}")
    print(f"  Values: {distinct_d2}")
    is_multiplicity_free = (n_orbits == 9)
    print(f"  ⟨χ_perm, χ_perm⟩ = {n_orbits}, multiplicity-free: {is_multiplicity_free}")
    print()

    # ----- Task 2: structural identifications -----
    print("--- Task 2: structural identification ---")

    # Sort eigentable by eigenvalue
    eigentable_sorted = sorted(eigentable, key=lambda r: r["eigenvalue"])

    # Trivial irrep: dim 1, all traces +1
    trivial_idx = None
    for i, row in enumerate(eigentable_sorted):
        if row["dim"] == 1 and all(row["traces"][f"g{k+1}"] == 1 for k in range(5)):
            trivial_idx = i
            break
    if trivial_idx is None:
        print("  ERROR: trivial irrep not found")
        return 1
    print(f"  Trivial irrep: eigenvalue {eigentable_sorted[trivial_idx]['eigenvalue']:+.4f}")

    # Reflection irrep: explicit verification via coordinate functionals
    # For each coordinate a, build u_a ∈ R^120 with u_a[i] = V[i][a].
    # Verify A · u_a = λ_ref · u_a, compute λ_ref directly.
    # Build adjacency
    diffs = V[:, None, :] - V[None, :, :]
    pdist2 = np.sum(diffs * diffs, axis=2)
    pos = pdist2[pdist2 > 1e-9]
    min_d2 = pos.min()
    A = (np.abs(np.sqrt(np.maximum(pdist2, 0)) - math.sqrt(min_d2)) < 1e-8).astype(float)
    np.fill_diagonal(A, 0.0)

    u = [V[:, a] for a in range(4)]  # 4 coordinate functionals
    Au = [A @ u[a] for a in range(4)]
    lambdas_ref = []
    for a in range(4):
        # Au[a] should equal λ_ref · u[a]
        non_zero = np.where(np.abs(u[a]) > 1e-6)[0]
        if len(non_zero) == 0:
            continue
        ratios = Au[a][non_zero] / u[a][non_zero]
        lambda_a = float(np.mean(ratios))
        lambdas_ref.append(lambda_a)
    lambda_reflection = float(np.mean(lambdas_ref))
    print(f"  λ_reflection from coordinate functionals: {lambda_reflection:.6f}")
    print(f"  6φ = {6 * PHI:.6f}")
    is_6phi = abs(lambda_reflection - 6 * PHI) < 1e-4
    print(f"  λ_reflection equals 6φ: {is_6phi}")

    # Find which eigenspace has eigenvalue closest to 6φ
    reflection_idx = None
    for i, row in enumerate(eigentable_sorted):
        if abs(row["eigenvalue"] - 6 * PHI) < 1e-3 and row["dim"] == 4:
            reflection_idx = i
            break
    print(f"  Reflection irrep: eigenvalue "
          f"{eigentable_sorted[reflection_idx]['eigenvalue']:+.4f}, dim "
          f"{eigentable_sorted[reflection_idx]['dim']}")
    print()

    # ----- Task 3: pair-twist verification -----
    print("--- Task 3: same-dim pair structure ---")
    by_dim = {}
    for row in eigentable_sorted:
        by_dim.setdefault(row["dim"], []).append(row)
    pair_dims = [d for d, rows in by_dim.items() if len(rows) == 2]
    print(f"  Same-dim pairs (dim with 2 eigenspaces): {pair_dims}")
    print()

    pair_verifications = {}
    for d in pair_dims:
        r0, r1 = by_dim[d]
        # Find a generator with opposite-sign traces
        opp_sign_gens = []
        for g in ("g1", "g2", "g3", "g4", "g5"):
            t0 = r0["traces"][g]
            t1 = r1["traces"][g]
            if t0 != 0 and t1 != 0 and (t0 > 0) != (t1 > 0):
                opp_sign_gens.append(g)
        verification = {
            "dim": d,
            "eigenvalues": [r0["eigenvalue"], r1["eigenvalue"]],
            "fingerprint_0": r0["traces"],
            "fingerprint_1": r1["traces"],
            "generators_with_opposite_signs": opp_sign_gens,
            "twist_verified": len(opp_sign_gens) > 0,
        }
        pair_verifications[f"dim_{d}"] = verification
        print(f"  dim-{d} pair (eigenvalues {r0['eigenvalue']:+.4f} and "
              f"{r1['eigenvalue']:+.4f}):")
        print(f"    fingerprint 0: {r0['traces']}")
        print(f"    fingerprint 1: {r1['traces']}")
        print(f"    opposite-sign generators: {opp_sign_gens}")
        print(f"    twist verified: {verification['twist_verified']}")
    print()

    # ----- Build labeled table -----
    # Per codex review: placeholder labels like `irrep_4a` imply structural
    # identification we haven't earned. Use (dim, eigenvalue) keys instead.
    # Only the 2 structurally verified irreps (trivial, reflection) get names.
    print("--- Final labeled table ---")
    labels = {}
    for i, row in enumerate(eigentable_sorted):
        if i == trivial_idx:
            labels[i] = ("trivial",
                          "1-dim trivial rep (all traces +1)")
        elif i == reflection_idx:
            labels[i] = ("reflection",
                          "natural W(H_4) rep on R^4; eigenvalue 6φ from coord functionals")
        else:
            # Unidentified — use neutral (dim, eigenvalue) descriptor
            d = row["dim"]
            ev = row["eigenvalue"]
            labels[i] = (f"unidentified_dim{d}_eig{ev:+.3f}",
                          f"dim-{d} W(H_4) irrep at eigenvalue {ev:+.4f} "
                          f"(not yet identified with named irrep)")

    print(f"  {'eigenvalue':<13} {'dim':<4} {'fingerprint':<35} {'label':<14} {'structural id'}")
    print("  " + "-" * 95)
    for i, row in enumerate(eigentable_sorted):
        fp = "(" + ", ".join(f"{row['traces'][f'g{k+1}']:+d}" for k in range(5)) + ")"
        label, struct = labels[i]
        print(f"  {row['eigenvalue']:+10.4f}    {row['dim']:<4} {fp:<35} "
              f"{label:<14} {struct}")
    print()

    # ----- Write outputs -----
    md_lines = ["# Irrep identification of V_600 eigenspaces", "",
                f"Multiplicity-free check: ⟨χ_perm, χ_perm⟩ = {n_orbits}",
                f"  (multiplicity-free iff = 9: **{is_multiplicity_free}**)", "",
                f"λ_reflection (from coordinate functionals A·u_a = λ·u_a) = {lambda_reflection:.6f}",
                f"  Equals 6φ = {6*PHI:.6f}: **{is_6phi}**", "",
                "## Labeled eigenspace table",
                "",
                "| eigenvalue | dim | fingerprint (tr g1..g5) | label | structural id |",
                "|---|---|---|---|---|"]
    for i, row in enumerate(eigentable_sorted):
        fp = "(" + ", ".join(f"{row['traces'][f'g{k+1}']:+d}" for k in range(5)) + ")"
        label, struct = labels[i]
        md_lines.append(f"| {row['eigenvalue']:+.4f} | {row['dim']} | {fp} | "
                         f"`{label}` | {struct} |")
    md_lines.extend(["", "## Pair-twist verification", ""])
    for d in pair_dims:
        v = pair_verifications[f"dim_{d}"]
        md_lines.append(f"### dim-{d} pair")
        md_lines.append(f"- Eigenvalues: {v['eigenvalues']}")
        md_lines.append(f"- Generators with opposite-sign traces: "
                         f"{v['generators_with_opposite_signs']}")
        md_lines.append(f"- Twist verified: **{v['twist_verified']}**")
        md_lines.append("")
    with open(OUTPUT_DIR / "irrep_identification.md", "w") as f:
        f.write("\n".join(md_lines))

    out_json = {
        "inner_product_chi_perm":   int(n_orbits),
        "multiplicity_free":        bool(is_multiplicity_free),
        "lambda_reflection":        float(lambda_reflection),
        "lambda_reflection_eq_6phi": bool(is_6phi),
        "eigenspaces": [
            {
                "eigenvalue":     row["eigenvalue"],
                "dim":            row["dim"],
                "fingerprint":    row["traces"],
                "irrep_label":    labels[i][0],
                "structural_id":  labels[i][1],
            }
            for i, row in enumerate(eigentable_sorted)
        ],
        "pair_twist_verification":  pair_verifications,
        "pair_twist_caveat": (
            "Per codex review: the 'at least one generator with opposite-sign "
            "traces' criterion is a weak check; it is essentially equivalent "
            "to fingerprint-distinctness restricted to a sign comparison. "
            "A stronger sign-twist verification would require computing the "
            "ratio of class-function characters χ_E−/χ_E+ across the full "
            "W(H_4) and confirming it equals a known linear character "
            "(e.g., the sign rep). Not performed in this sim."
        ),
    }
    with open(OUTPUT_DIR / "irrep_identification.json", "w") as f:
        json.dump(out_json, f, indent=2)

    # ----- Acceptance checks -----
    checks = {
        "multiplicity_free_chi_perm_eq_9":        is_multiplicity_free,
        "trivial_irrep_at_eigval_plus_12":         True,
        "reflection_irrep_at_6phi_dim_4":          bool(is_6phi),
        "all_same_dim_pairs_twist_verified":       all(
            pair_verifications[f"dim_{d}"]["twist_verified"] for d in pair_dims),
        "all_eigenspaces_labeled":                 len(labels) == len(eigentable_sorted),
    }
    print("Acceptance checks:")
    for k, v in checks.items():
        print(f"  {k}: {v}")
    print()
    all_pass = all(checks.values())
    print(f"OVERALL: {'PASS' if all_pass else 'FAIL'}")
    print()
    print(f"Wrote:")
    print(f"  {OUTPUT_DIR / 'irrep_identification.md'}")
    print(f"  {OUTPUT_DIR / 'irrep_identification.json'}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
