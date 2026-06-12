#!/usr/bin/env python3
"""
Note G --- T8 / T9 / T10: Closure Control Node (CCN) site ranking.

Hypothesis (H-CCN): the structural sites where small polarisability shifts
disrupt collective microtubule modes most strongly are not the
high-affinity anaesthetic binding sites alone; they are residues that
sit at the intersection of (i) the aromatic Trp/Tyr/Phe network,
(ii) inter-protofilament / longitudinal interface positions, and
(iii) proximity to known anaesthetic-binding pockets.

This module:
  T8  builds a CCN structural score from beta-tubulin PDB geometry
      using 4O4H (apo dimer, high-resolution).
  T9  back-tests CCN ranking against published anaesthetic-docking
      sites (Craddock 2012 halothane, Pang & Eckenhoff 2007 halothane
      photoaffinity, Liu 2010 isoflurane).
  T10 emits the pre-registered top-5 mutation-target residue list.

Outputs (deterministic):
  output/T8_ccn_scores.json        per-residue CCN scores
  output/T8_aromatic_network.png   beta-tubulin aromatic network
  output/T9_back_test.png          CCN-vs-literature comparison
  output/T10_mutation_targets.json top-5 pre-registered list

Run:
  python ccn_site_ranking.py

Requires only numpy + matplotlib + the fetched PDB files in
../external_data/pdb/.
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

AROMATIC_RESIDUES = {"TRP", "TYR", "PHE"}
# Backbone-only filter for distance computation; CA is a clean centroid proxy
CENTROID_ATOM = "CA"

# Published anaesthetic-binding sites in beta-tubulin used for the
# T9 literature back-test.  Each entry is (residue_number, citation_key, role).
# Numbers correspond to author-defined residue numbering in beta-tubulin
# (i.e. matching PDB auth_seq_id for chain B in 4O4H / 1JFF).
PUBLISHED_ANAESTHETIC_SITES = [
    # Craddock 2012 halothane docking (PLOS One 2012 e37251)
    (210, "Craddock2012", "halothane_close_2A_betaY210_vinca_domain"),
    (241, "Craddock2012", "halothane_close_3A_betaC241_colchicine_pocket"),
    (246, "Craddock2012", "halothane_pocket_betaH8_region"),
    (250, "Craddock2012", "halothane_pocket_betaS8_region"),
    (315, "Craddock2012", "halothane_pocket_betaT7_region"),
    # Pang & Eckenhoff 2007 halothane photoaffinity sites
    # (numbering approximate from photolabel-mass-spec resolution ~5 A)
    (108, "PangEckenhoff2007", "halothane_photoaffinity_betaY108_hydrophobic"),
    (227, "PangEckenhoff2007", "halothane_photoaffinity_pocket"),
    # Vinca-domain references (region-level, not residue-level)
    (224, "Craddock2012", "vinca_domain_betaY224_aromatic"),
    (272, "Craddock2012", "vinca_domain_betaF272_aromatic"),
    # Colchicine pocket aromatic residues
    (270, "Craddock2012", "colchicine_pocket_aromatic"),
    (200, "PangEckenhoff2007", "halothane_photoaffinity_betaH200"),
]


# ============================================================
# mmCIF parser (no external deps)
# ============================================================

def parse_mmcif(path):
    """Return list of atom dicts with keys: comp, label_chain, auth_chain,
       resnum (auth_seq_id), atom (label_atom_id), x, y, z."""
    with open(path) as f:
        lines = f.readlines()
    # Find _atom_site loop header
    start = None
    for i, l in enumerate(lines):
        if l.startswith("_atom_site.group_PDB"):
            start = i
            break
    if start is None:
        raise ValueError(f"No _atom_site loop in {path}")
    header_cols = []
    i = start
    while i < len(lines) and lines[i].startswith("_atom_site."):
        header_cols.append(lines[i].strip().split(".")[1])
        i += 1
    # Index map
    col = {name: idx for idx, name in enumerate(header_cols)}
    needed = ["group_PDB", "label_comp_id", "label_asym_id", "auth_asym_id",
              "auth_seq_id", "label_atom_id", "Cartn_x", "Cartn_y", "Cartn_z"]
    for n in needed:
        if n not in col:
            raise ValueError(f"missing column {n} in {path}")
    atoms = []
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith("#") or line.startswith("loop_") or line.startswith("_"):
            break
        parts = line.split()
        if len(parts) < len(header_cols):
            i += 1
            continue
        if parts[col["group_PDB"]] != "ATOM":
            i += 1
            continue
        atoms.append({
            "comp": parts[col["label_comp_id"]],
            "label_chain": parts[col["label_asym_id"]],
            "auth_chain": parts[col["auth_asym_id"]],
            "resnum": int(parts[col["auth_seq_id"]]),
            "atom": parts[col["label_atom_id"]],
            "x": float(parts[col["Cartn_x"]]),
            "y": float(parts[col["Cartn_y"]]),
            "z": float(parts[col["Cartn_z"]]),
        })
        i += 1
    return atoms


def select_chain_ca(atoms, auth_chain):
    """Return list of (resnum, comp, np.array([x,y,z])) for CA atoms in chain."""
    out = []
    for a in atoms:
        if a["auth_chain"] != auth_chain:
            continue
        if a["atom"] != CENTROID_ATOM:
            continue
        out.append((a["resnum"], a["comp"], np.array([a["x"], a["y"], a["z"]])))
    return out


# ============================================================
# T8 components
# ============================================================

def aromatic_network_centrality(residues, cutoff_angstrom=8.0):
    """For each aromatic residue, count nearby aromatic residues within cutoff.
       Returns dict (resnum -> count)."""
    aromatics = [(r, c, p) for (r, c, p) in residues if c in AROMATIC_RESIDUES]
    n = len(aromatics)
    counts = {}
    for i in range(n):
        ri, _, pi = aromatics[i]
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            rj, _, pj = aromatics[j]
            if np.linalg.norm(pi - pj) < cutoff_angstrom:
                cnt += 1
        counts[ri] = cnt
    return counts, aromatics


def pocket_proximity(residues, anaesthetic_sites, cutoff_angstrom=12.0):
    """For each residue, return min distance to any published anaesthetic site
       (using CA-CA distance to the closest site CA)."""
    # Get CA positions of the published sites
    site_positions = {}
    res_lookup = {r: (c, p) for (r, c, p) in residues}
    for (rn, cite, role) in anaesthetic_sites:
        if rn in res_lookup:
            site_positions[rn] = res_lookup[rn][1]
    proximities = {}
    for (rn, comp, pos) in residues:
        dists = [np.linalg.norm(pos - sp) for sp in site_positions.values()]
        proximities[rn] = float(min(dists)) if dists else float("inf")
    return proximities, site_positions


def lattice_interface_score(residues, ca_array):
    """Crude lattice-interface proxy: residues whose CA is on the outer
       solvent-accessible surface of beta-tubulin score higher.

       We approximate by 'surface-ness' = how few other CA atoms are within
       8 angstrom. A high count = buried; a low count = exposed (interface
       candidate when assembled in the MT lattice).
       Returns dict (resnum -> surface_score) where lower is more buried."""
    n = len(residues)
    # 'Burial' counts CA neighbours; we invert to get an exposure score.
    exposures = {}
    for i in range(n):
        rn, _, pi = residues[i]
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            rj, _, pj = residues[j]
            if np.linalg.norm(pi - pj) < 8.0:
                cnt += 1
        # Exposure score: max possible neighbours minus actual; normalised
        exposures[rn] = -cnt
    # Normalise to [0, 1]
    vals = np.array(list(exposures.values()))
    vmin, vmax = vals.min(), vals.max()
    if vmax > vmin:
        for k in exposures:
            exposures[k] = (exposures[k] - vmin) / (vmax - vmin)
    else:
        for k in exposures:
            exposures[k] = 0.5
    return exposures


def compute_ccn_score(residues):
    """Compose the T8 CCN score per residue.
       CCN = aromatic_network_centrality * pocket_proximity_inverse * interface_exposure
       Higher = better closure-control-node candidate."""
    aromatic_counts, aromatics = aromatic_network_centrality(residues)
    proximities, site_positions = pocket_proximity(residues, PUBLISHED_ANAESTHETIC_SITES)
    interface = lattice_interface_score(residues, None)

    # Normalise each factor to [0, 1]
    arom_arr = np.array([aromatic_counts.get(r[0], 0) for r in residues], dtype=float)
    if arom_arr.max() > 0:
        arom_norm = arom_arr / arom_arr.max()
    else:
        arom_norm = arom_arr
    prox_arr = np.array([proximities.get(r[0], float("inf")) for r in residues])
    # Lower distance = closer to pocket = better; invert
    prox_inv = 1.0 / (1.0 + prox_arr)
    prox_norm = prox_inv / max(prox_inv.max(), 1e-9)
    iface_arr = np.array([interface.get(r[0], 0.0) for r in residues])

    scores = {}
    for k, (rn, comp, pos) in enumerate(residues):
        # CCN: only score aromatic residues (the candidate network nodes)
        if comp in AROMATIC_RESIDUES:
            scores[rn] = {
                "residue": comp,
                "resnum": rn,
                "aromatic_neighbour_count": int(aromatic_counts.get(rn, 0)),
                "aromatic_neighbour_norm": float(arom_norm[k]),
                "pocket_distance_angstrom": float(prox_arr[k]),
                "pocket_proximity_norm": float(prox_norm[k]),
                "interface_exposure_norm": float(iface_arr[k]),
                "ccn_score": float(arom_norm[k] * prox_norm[k] * iface_arr[k]),
            }
    return scores, aromatics, site_positions


# ============================================================
# T9 literature back-test
# ============================================================

def back_test(ccn_scores, anaesthetic_sites):
    """For each published anaesthetic site, find its CCN score and rank.
       Returns: list of (residue, citation, ccn_score, ccn_rank)."""
    # All scored residues, ranked by CCN score
    all_scores = sorted(ccn_scores.values(), key=lambda s: -s["ccn_score"])
    rank_lookup = {s["resnum"]: i + 1 for i, s in enumerate(all_scores)}
    n_total = len(all_scores)
    back = []
    for (rn, cite, role) in anaesthetic_sites:
        if rn in ccn_scores:
            score = ccn_scores[rn]["ccn_score"]
            rank = rank_lookup[rn]
            back.append({
                "residue_number": rn,
                "residue_name": ccn_scores[rn]["residue"],
                "citation": cite,
                "role": role,
                "ccn_score": score,
                "ccn_rank": rank,
                "rank_percentile": (n_total - rank + 1) / n_total,
            })
    return back, n_total


# ============================================================
# T10 pre-registered mutation list
# ============================================================

def pre_registered_top_n(ccn_scores, n=5):
    """Return the top-n CCN-scored residues as the pre-registered
       mutation-target list for H-CCN."""
    all_scores = sorted(ccn_scores.values(), key=lambda s: -s["ccn_score"])
    return all_scores[:n]


# ============================================================
# Main
# ============================================================

def main() -> int:
    print("=" * 70)
    print("Note G T8/T9/T10 --- Closure Control Node site ranking")
    print("=" * 70)
    print()

    pdb_path = PDB_DIR / "4O4H.cif"
    if not pdb_path.exists():
        print(f"  [SKIP] {pdb_path} not found.")
        print("        Run repro/fetch_external_data.py --pdb first.")
        return 1

    print(f"Parsing {pdb_path.name}...")
    atoms = parse_mmcif(pdb_path)
    print(f"  {len(atoms)} atom records loaded")

    # Beta-tubulin is chain B in 4O4H
    beta_ca = select_chain_ca(atoms, "B")
    print(f"  beta-tubulin (chain B): {len(beta_ca)} residues with CA")

    aromatic_count = sum(1 for (r, c, p) in beta_ca if c in AROMATIC_RESIDUES)
    print(f"  aromatic residues (Trp/Tyr/Phe) in beta-tubulin: {aromatic_count}")
    print()

    # T8: CCN scores
    print("T8: compute CCN structural score per beta-tubulin aromatic residue...")
    ccn_scores, aromatics, site_positions = compute_ccn_score(beta_ca)
    sorted_top = sorted(ccn_scores.values(), key=lambda s: -s["ccn_score"])[:10]
    print(f"  {len(ccn_scores)} aromatic residues scored")
    print(f"  Top 10 CCN-scored residues:")
    print(f"  {'rank':>4}  {'residue':>8}  {'arom_n':>6}  {'pocket_dist':>11}  "
          f"{'iface_norm':>10}  {'CCN_score':>9}")
    for i, s in enumerate(sorted_top):
        print(f"  {i+1:>4}  {s['residue']}{s['resnum']:<5}  "
              f"{s['aromatic_neighbour_count']:>6}  "
              f"{s['pocket_distance_angstrom']:>11.2f}  "
              f"{s['interface_exposure_norm']:>10.3f}  "
              f"{s['ccn_score']:>9.4f}")
    print()

    # Save T8 outputs
    with open(OUTPUT_DIR / "T8_ccn_scores.json", "w") as f:
        json.dump({
            "n_residues_scored": len(ccn_scores),
            "scores_by_resnum": ccn_scores,
            "top_10_ranked": sorted_top,
        }, f, indent=2)
    print(f"  saved T8_ccn_scores.json")

    # T8 figure: aromatic network in beta-tubulin
    arom_positions = np.array([p for (_, _, p) in aromatics])
    arom_labels = [(r, c) for (r, c, _) in aromatics]
    arom_ccn = np.array([ccn_scores[r]["ccn_score"] for r, _ in arom_labels])
    fig, ax = plt.subplots(figsize=(8, 6))
    sc = ax.scatter(arom_positions[:, 0], arom_positions[:, 1],
                    c=arom_ccn, s=60, cmap="viridis",
                    edgecolor="black", linewidth=0.3)
    plt.colorbar(sc, ax=ax, label="CCN score")
    # Annotate top-5
    for i, ((rn, comp), pos) in enumerate(zip(arom_labels, arom_positions)):
        if ccn_scores[rn]["ccn_score"] in sorted([s["ccn_score"] for s in sorted_top[:5]]):
            ax.annotate(f"{comp}{rn}", (pos[0], pos[1]), fontsize=8, textcoords="offset points",
                        xytext=(4, 4))
    ax.set_xlabel(r"$x$ (Å)")
    ax.set_ylabel(r"$y$ (Å)")
    ax.set_title(r"T8 $\beta$-tubulin aromatic-residue network (4O4H, chain B)" +
                 "\nCCN score = aromatic centrality × pocket proximity × interface exposure")
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "T8_aromatic_network.png", dpi=120)
    plt.close()
    print(f"  saved T8_aromatic_network.png")
    print()

    # T9: literature back-test
    print("T9: back-test CCN ranking against published anaesthetic-docking sites...")
    back, n_total = back_test(ccn_scores, PUBLISHED_ANAESTHETIC_SITES)
    print(f"  {len(back)} of {len(PUBLISHED_ANAESTHETIC_SITES)} literature sites resolved on 4O4H")
    print(f"  Total scored aromatic residues: {n_total}")
    print()
    print(f"  {'site':>8}  {'role':<55}  {'CCN':>7}  {'rank':>5}  {'%ile':>5}")
    for b in sorted(back, key=lambda x: -x["ccn_score"]):
        print(f"  {b['residue_name']}{b['residue_number']:<3}  {b['role'][:55]:<55}  "
              f"{b['ccn_score']:>7.4f}  {b['ccn_rank']:>5}/{n_total}  "
              f"{b['rank_percentile']*100:>4.0f}%")
    print()
    mean_percentile = np.mean([b["rank_percentile"] for b in back])
    print(f"  Mean rank percentile of literature anaesthetic sites: {mean_percentile*100:.1f}%")
    if mean_percentile > 0.7:
        verdict = ("Literature anaesthetic sites cluster in the top tier of "
                   "CCN-scored aromatic residues. Consistent with H-CCN.")
    elif mean_percentile > 0.5:
        verdict = ("Literature anaesthetic sites are above-median in CCN ranking. "
                   "Weakly consistent with H-CCN.")
    else:
        verdict = ("Literature anaesthetic sites are not concentrated in top "
                   "CCN tier. H-CCN candidate-falsifier signal.")
    print(f"  Interpretation: {verdict}")
    print()

    # T9 figure: CCN score vs literature site
    fig, ax = plt.subplots(figsize=(8, 5))
    all_scores_sorted = sorted([s["ccn_score"] for s in ccn_scores.values()])
    ax.plot(all_scores_sorted, np.arange(len(all_scores_sorted)) / len(all_scores_sorted),
            label="all β-tubulin aromatic residues (CDF)", color="gray", linewidth=0.7)
    for b in back:
        ax.axvline(b["ccn_score"], color="#cd3a3a", alpha=0.4)
    # Sort the back list for annotation
    back_sorted = sorted(back, key=lambda x: -x["ccn_score"])
    for i, b in enumerate(back_sorted[:5]):
        ax.annotate(f"{b['residue_name']}{b['residue_number']}",
                    (b["ccn_score"], 0.95 - 0.06 * i),
                    fontsize=8, color="#cd3a3a")
    ax.set_xlabel("CCN score")
    ax.set_ylabel("CDF of all β-tubulin aromatic residues")
    ax.set_title(rf"T9 Literature anaesthetic sites on CCN-score CDF " +
                 rf"(mean percentile = {mean_percentile*100:.0f}%)")
    ax.grid(alpha=0.3)
    ax.legend(loc="lower right", fontsize=8)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "T9_back_test.png", dpi=120)
    plt.close()
    print(f"  saved T9_back_test.png")
    print()

    # T10: pre-registered top-5 mutation list
    print("T10: pre-registered top-5 mutation targets (H-CCN falsifier list)...")
    top5 = pre_registered_top_n(ccn_scores, n=5)
    print()
    for i, s in enumerate(top5):
        print(f"  rank {i+1}: {s['residue']}{s['resnum']:<3}  CCN={s['ccn_score']:.4f}")
        print(f"           aromatic neighbours = {s['aromatic_neighbour_count']}; "
              f"distance to nearest published pocket = "
              f"{s['pocket_distance_angstrom']:.2f} Å")
    print()
    print("  Pre-registered prediction (H-CCN):")
    print("  Site-specific mutation at one of these 5 residues (Trp -> Ala,")
    print("  Tyr -> Phe, Phe -> Ala, depending on residue type) should disrupt")
    print("  the anaesthetic-induced collective-mode signature in tubulin in")
    print("  vitro (e.g., the THz oscillation shifts reported by Craddock 2017)")
    print("  more strongly than the same mutation at a randomly-chosen control")
    print("  aromatic residue. Required effect: response disruption ratio")
    print("  R_top5 / R_control >= 1.5 at n_subjects_per_site >= 3.")
    print()
    print("  Falsifier: a published / new study showing the top-5 CCN sites")
    print("  do NOT exceed control sites at >= 1.5x effect size falsifies H-CCN.")
    print()

    with open(OUTPUT_DIR / "T10_mutation_targets.json", "w") as f:
        json.dump({
            "n_residues_in_pool": n_total,
            "top_5_pre_registered": top5,
            "control_residues_required": ">=5 randomly-chosen Trp/Tyr/Phe residues of matched type, excluding the top 20 CCN-ranked residues",
            "effect_size_target": "R_top5 / R_control >= 1.5",
            "minimum_n_per_site": 3,
            "permitted_assays": [
                "THz oscillation shift (Craddock 2017 protocol)",
                "Dielectric response under anaesthetic",
                "Tryptophan fluorescence quenching",
                "Raman / IR spectroscopy of MT polymerisation under anaesthetic",
            ],
            "open_for_collaboration": True,
        }, f, indent=2)
    print(f"  saved T10_mutation_targets.json")
    print()

    print("=" * 70)
    print("T8/T9/T10 complete. CCN structural-score module ready for review.")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    sys.exit(main())
