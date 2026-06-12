#!/usr/bin/env python3
"""
Note G --- T20 / T21: cross-PDB signatures supporting H-CCN.

  T20  Cross-PDB conformational mobility per beta-tubulin residue.
       For each residue with a CA atom resolved in two-or-more of
       the seven fetched PDB structures, compute the standard
       deviation of CA positions across structures after rigid-body
       superposition. Identify high-mobility residues and check
       whether the H-CCN top-5 (Y210, Y202, Y185, F214, Y53) sit
       at high-mobility positions.

  T21  Aromatic-ring orientation coherence for the H6 same-face
       cluster. Compute ring-plane normal vectors for the top-5
       residues. Cosine angle between ring normals tests whether
       Y210/F214/Y202 are coherently oriented (cooperative
       pi-stacking) or random.

Outputs:
  output/T20_cross_pdb_mobility.json
  output/T20_mobility_ranking.png
  output/T21_ring_orientation.json
  output/T21_ring_normals.png
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
PDB_DIR = REPO_ROOT / "external_data" / "pdb"
OUTPUT_DIR = REPO_ROOT / "repro" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(REPO_ROOT / "repro"))
from ccn_site_ranking import parse_mmcif, select_chain_ca  # type: ignore  # noqa: E402
from chemistry_context import get_ring_atoms, ring_centroid, TOP_5  # type: ignore

PDB_FILES = ["4O4H", "1JFF", "5SYC", "5SYE", "6E7B", "3J6F", "6DPV"]

# Candidate chains for beta-tubulin in each PDB
# (apparent from earlier parsing; many MT-lattice files have multiple
# beta-tubulin copies in different chains)
BETA_CHAIN_CANDIDATES = {
    "4O4H": ["B"],   # apo dimer
    "1JFF": ["B"],   # taxol-bound dimer
    "5SYC": ["B"],   # paclitaxel co-crystal
    "5SYE": ["B"],   # paclitaxel + epothilone co-crystal
    "6E7B": ["B"],   # colchicine-pocket complex
    "3J6F": ["B", "D", "F", "H", "J", "L", "N", "P", "R", "T", "V", "X", "Z"],
    "6DPV": ["B", "D"],
}


# ============================================================
# T20: Cross-PDB conformational mobility
# ============================================================

def superpose(ref_ca, mob_ca):
    """Kabsch algorithm: rigid-body superposition of mob_ca onto ref_ca.
       Returns rotated mob_ca."""
    ref = np.array(ref_ca)
    mob = np.array(mob_ca)
    if ref.shape != mob.shape:
        return None
    centroid_ref = ref.mean(axis=0)
    centroid_mob = mob.mean(axis=0)
    P = ref - centroid_ref
    Q = mob - centroid_mob
    H = Q.T @ P
    U, _, Vt = np.linalg.svd(H)
    d = np.sign(np.linalg.det(Vt.T @ U.T))
    D = np.diag([1, 1, d])
    R = Vt.T @ D @ U.T
    return (Q @ R) + centroid_ref


def collect_beta_ca_positions(pdb_id):
    """Return dict {resnum -> position} for beta-tubulin chain B
       (or first available candidate)."""
    path = PDB_DIR / f"{pdb_id}.cif"
    if not path.exists():
        return {}
    atoms = parse_mmcif(path)
    # Try chain B first (canonical for most tubulin PDBs)
    for ch in BETA_CHAIN_CANDIDATES.get(pdb_id, ["B"]):
        positions = {}
        for a in atoms:
            if a["auth_chain"] == ch and a["atom"] == "CA":
                positions[a["resnum"]] = np.array([a["x"], a["y"], a["z"]])
        if len(positions) > 100:
            return positions
    return {}


def t20_cross_pdb_mobility():
    """Compute per-residue CA-position SD across the 7 PDBs."""
    # Use 4O4H as reference (highest-res apo structure)
    ref_positions = collect_beta_ca_positions("4O4H")
    if not ref_positions:
        print("  [SKIP] 4O4H not loadable")
        return None

    # For each other PDB, get residues present in BOTH, superpose, and record offsets
    all_offsets = defaultdict(list)
    for pdb_id in PDB_FILES:
        if pdb_id == "4O4H":
            # Reference; mobility = 0 by construction
            continue
        mob_positions = collect_beta_ca_positions(pdb_id)
        common = sorted(set(ref_positions.keys()) & set(mob_positions.keys()))
        if len(common) < 50:
            print(f"  [SKIP] {pdb_id}: only {len(common)} common residues")
            continue
        ref_array = [ref_positions[r] for r in common]
        mob_array = [mob_positions[r] for r in common]
        rotated = superpose(ref_array, mob_array)
        if rotated is None:
            print(f"  [SKIP] {pdb_id}: superpose failed")
            continue
        for k, r in enumerate(common):
            offset = float(np.linalg.norm(rotated[k] - ref_positions[r]))
            all_offsets[r].append((pdb_id, offset))

    # Compute SD per residue
    sd_per_residue = {}
    for r, offsets in all_offsets.items():
        vals = [o for (_, o) in offsets]
        sd_per_residue[r] = {
            "n_structures": len(vals),
            "mean_offset_angstrom": float(np.mean(vals)),
            "max_offset_angstrom": float(np.max(vals)),
            "sd_offset_angstrom": float(np.std(vals)),
        }
    return sd_per_residue


# ============================================================
# T21: Aromatic-ring orientation coherence
# ============================================================

def ring_normal(ring_atoms):
    """Compute the ring-plane normal from 3+ ring atoms by SVD."""
    if len(ring_atoms) < 3:
        return None
    positions = np.array([p for (_, p) in ring_atoms])
    centroid = positions.mean(axis=0)
    centred = positions - centroid
    # SVD: smallest singular vector = ring-plane normal
    _, _, Vt = np.linalg.svd(centred)
    normal = Vt[-1]  # last row of Vt = smallest right-singular vector
    return normal / np.linalg.norm(normal)


def t21_ring_orientations(atoms):
    """Compute ring normals for top-5 residues and pairwise cosines."""
    normals = {}
    for (comp, rn, _) in TOP_5:
        ring = get_ring_atoms(atoms, "B", comp, rn)
        if ring:
            n = ring_normal(ring)
            normals[(comp, rn)] = n
    # Pairwise cosines (absolute value: parallel and anti-parallel are
    # the same physically because rings are planar two-sided objects)
    pairs = []
    keys = list(normals.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            n1 = normals[keys[i]]
            n2 = normals[keys[j]]
            cos_val = abs(float(np.dot(n1, n2)))
            angle_deg = float(np.degrees(np.arccos(min(cos_val, 1.0))))
            pairs.append({
                "pair": f"{keys[i][0]}{keys[i][1]}--{keys[j][0]}{keys[j][1]}",
                "cosine_abs": cos_val,
                "angle_deg": angle_deg,
                "orientation": ("parallel/coplanar" if cos_val > 0.8 else
                                "tilted" if cos_val > 0.5 else "perpendicular-ish"),
            })
    return normals, pairs


# ============================================================
# Main
# ============================================================

def main() -> int:
    print("=" * 70)
    print("Note G T20/T21 --- cross-PDB + ring-orientation signatures")
    print("=" * 70)
    print()

    # T20
    print("T20: cross-PDB conformational mobility per beta-tubulin residue")
    sd_per_residue = t20_cross_pdb_mobility()
    if sd_per_residue:
        # Identify high-mobility residues
        all_mobility = [(r, info["mean_offset_angstrom"], info["sd_offset_angstrom"])
                        for r, info in sd_per_residue.items()]
        all_mobility.sort(key=lambda x: -x[1])
        # Check top-5
        print(f"  Residues with cross-PDB CA-position data: {len(sd_per_residue)}")
        # Compute mean+SD of all mobilities for percentile reference
        mobilities = [info["mean_offset_angstrom"] for info in sd_per_residue.values()]
        mob_mean = float(np.mean(mobilities))
        mob_sd = float(np.std(mobilities))
        print(f"  Overall mobility: mean = {mob_mean:.2f} A, SD = {mob_sd:.2f} A")
        # Check top-5 H-CCN sites
        print(f"  H-CCN top-5 cross-PDB mobility:")
        print(f"  {'residue':>8}  {'mean_offset':>11}  {'max_offset':>10}  "
              f"{'SD':>5}  {'percentile':>10}")
        all_mobs_sorted = sorted(mobilities)
        for (comp, rn, _) in TOP_5:
            if rn in sd_per_residue:
                info = sd_per_residue[rn]
                mob = info["mean_offset_angstrom"]
                pctile = float(np.searchsorted(all_mobs_sorted, mob)) / len(all_mobs_sorted) * 100
                print(f"  {comp}{rn:<5}  {mob:>11.2f}  {info['max_offset_angstrom']:>10.2f}  "
                      f"{info['sd_offset_angstrom']:>5.2f}  {pctile:>9.0f}%")
            else:
                print(f"  {comp}{rn:<5}  not resolved in cross-PDB common set")
        # Interpretation
        top5_pcts = []
        for (comp, rn, _) in TOP_5:
            if rn in sd_per_residue:
                mob = sd_per_residue[rn]["mean_offset_angstrom"]
                pctile = float(np.searchsorted(all_mobs_sorted, mob)) / len(all_mobs_sorted) * 100
                top5_pcts.append(pctile)
        if top5_pcts:
            mean_top5_pct = float(np.mean(top5_pcts))
            print()
            print(f"  Mean percentile of H-CCN top-5 mobility: {mean_top5_pct:.0f}%")
            if mean_top5_pct > 75:
                verdict_t20 = ("H-CCN top-5 cluster at high cross-PDB mobility -- "
                               "these residues are conformationally responsive to "
                               "ligand binding. Supports CCN identification of "
                               "high-leverage sites.")
            elif mean_top5_pct > 50:
                verdict_t20 = ("H-CCN top-5 are above-median in cross-PDB mobility. "
                               "Weakly consistent with CCN claim.")
            else:
                verdict_t20 = ("H-CCN top-5 are not at high-mobility positions. "
                               "Honest finding: the CCN site-ranking is NOT "
                               "primarily about cross-PDB conformational mobility. "
                               "The mechanism is structural/electronic, not "
                               "rigid-body conformational.")
            print(f"  Interpretation: {verdict_t20}")
        with open(OUTPUT_DIR / "T20_cross_pdb_mobility.json", "w") as f:
            json.dump({
                "n_residues": len(sd_per_residue),
                "overall_mobility_mean_A": mob_mean,
                "overall_mobility_sd_A": mob_sd,
                "top_10_most_mobile": [
                    {"resnum": r, "mean_offset": m, "sd_offset": s}
                    for (r, m, s) in all_mobility[:10]
                ],
                "top_5_h_ccn_mobility": [
                    {"residue": f"{c}{rn}",
                     "mean_offset_angstrom": sd_per_residue.get(rn, {}).get("mean_offset_angstrom"),
                     "percentile": float(np.searchsorted(all_mobs_sorted,
                                                          sd_per_residue.get(rn, {}).get("mean_offset_angstrom", 0)))
                                   / len(all_mobs_sorted) * 100 if rn in sd_per_residue else None}
                    for (c, rn, _) in TOP_5
                ],
                "mean_top5_percentile": mean_top5_pct if top5_pcts else None,
                "interpretation": verdict_t20 if top5_pcts else "no top-5 resolved",
            }, f, indent=2)
        # T20 figure
        fig, ax = plt.subplots(figsize=(10, 4))
        resnums_sorted = sorted(sd_per_residue.keys())
        mobs_arr = [sd_per_residue[r]["mean_offset_angstrom"] for r in resnums_sorted]
        ax.bar(resnums_sorted, mobs_arr, color="#9999cc", width=1.0,
               edgecolor="none")
        # Highlight top-5
        for (comp, rn, _) in TOP_5:
            if rn in sd_per_residue:
                ax.bar(rn, sd_per_residue[rn]["mean_offset_angstrom"],
                       color="#cd3a3a", width=1.5, edgecolor="black", linewidth=0.5)
                ax.annotate(f"{comp}{rn}", (rn, sd_per_residue[rn]["mean_offset_angstrom"]),
                            textcoords="offset points", xytext=(0, 4),
                            fontsize=7, ha="center")
        ax.set_xlabel("β-tubulin residue number")
        ax.set_ylabel("mean CA-position offset across PDBs (Å)")
        ax.set_title("T20 cross-PDB conformational mobility (H-CCN top-5 in red)")
        ax.grid(alpha=0.3, axis="y")
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "T20_mobility_ranking.png", dpi=120)
        plt.close()
        print(f"  saved T20_cross_pdb_mobility.json + T20_mobility_ranking.png")
    print()

    # T21
    print("T21: aromatic-ring orientation coherence for top-5")
    atoms = parse_mmcif(PDB_DIR / "4O4H.cif")
    normals, pairs = t21_ring_orientations(atoms)
    print(f"  Ring normals computed for {len(normals)} top-5 residues")
    print(f"  Pairwise ring-normal cosines (|cos|; 1 = parallel, 0 = perpendicular):")
    for p in sorted(pairs, key=lambda x: -x["cosine_abs"]):
        marker = ""
        if "TYR210" in p["pair"] or "PHE214" in p["pair"] or "TYR202" in p["pair"]:
            if all(s in ["TYR210", "PHE214", "TYR202"] or s.startswith("TYR210") or s.startswith("PHE214") or s.startswith("TYR202") for s in p["pair"].split("--")):
                marker = " <- H6 cluster pair"
        print(f"    {p['pair']:<20}  |cos| = {p['cosine_abs']:.3f}  "
              f"({p['angle_deg']:>5.1f}°)  {p['orientation']}{marker}")
    # Focus on H6 cluster
    h6_pairs = [p for p in pairs
                if set(p["pair"].split("--")) <= {"TYR210", "PHE214", "TYR202"}]
    if h6_pairs:
        mean_h6_cos = float(np.mean([p["cosine_abs"] for p in h6_pairs]))
        print()
        print(f"  H6 same-face cluster (Y210/F214/Y202) pairs: "
              f"mean |cos| = {mean_h6_cos:.3f}")
        if mean_h6_cos > 0.8:
            verdict_t21 = ("H6 cluster rings are approximately parallel/coplanar -- "
                           "cooperative pi-stacking geometry. Strengthens the "
                           "same-face cluster claim with field-coherence support.")
        elif mean_h6_cos > 0.5:
            verdict_t21 = ("H6 cluster rings are tilted; partial coherence. "
                           "Consistent with same-face-on-helix but not fully "
                           "parallel-stacked.")
        else:
            verdict_t21 = ("H6 cluster rings are NOT coherently oriented despite "
                           "same-face helix geometry. Honest finding: the same-face "
                           "geometric pattern does not imply coherent pi-stacking.")
        print(f"  Interpretation: {verdict_t21}")
    with open(OUTPUT_DIR / "T21_ring_orientation.json", "w") as f:
        json.dump({
            "normals_per_residue": {
                f"{k[0]}{k[1]}": v.tolist() for k, v in normals.items()
            },
            "pairwise_cosines": pairs,
            "h6_cluster_mean_abs_cosine": mean_h6_cos if h6_pairs else None,
            "h6_cluster_pairs": h6_pairs,
            "interpretation": verdict_t21 if h6_pairs else "no H6 cluster pairs",
        }, f, indent=2)
    # T21 figure
    fig, ax = plt.subplots(figsize=(8, 5))
    labels = [p["pair"] for p in pairs]
    cosines = [p["cosine_abs"] for p in pairs]
    colors = ["#cd3a3a" if (set(p["pair"].split("--")) <= {"TYR210", "PHE214", "TYR202"})
              else "#6699cc" for p in pairs]
    ax.barh(range(len(labels)), cosines, color=colors, edgecolor="black", linewidth=0.4)
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=8)
    ax.axvline(0.8, color="green", linestyle=":", linewidth=0.8, label="0.8 = parallel/coplanar threshold")
    ax.axvline(0.5, color="orange", linestyle=":", linewidth=0.8, label="0.5 = tilted threshold")
    ax.set_xlabel("|cos| between ring-plane normals")
    ax.set_xlim(0, 1.05)
    ax.set_title("T21 ring-orientation coherence of H-CCN top-5 (red = H6 cluster pairs)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="x")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "T21_ring_normals.png", dpi=120)
    plt.close()
    print(f"  saved T21_ring_orientation.json + T21_ring_normals.png")
    print()

    print("=" * 70)
    print("T20/T21 complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
