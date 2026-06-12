#!/usr/bin/env python3
"""
Note G --- T27 / T28: cross-target + coevolution signatures.

  T27  Cross-target CCN validation on GLIC.
       GLIC (Gloeobacter ligand-gated ion channel, PDB 3P50 with
       propofol bound, 4HFI with desflurane bound) is a bacterial
       homologue of GABA-A / nicotinic ACh receptors with
       well-characterised volatile-anaesthetic binding sites.
       We compute a CCN-like score for GLIC's aromatic residues and
       check whether the ranking recovers the published anaesthetic
       sites. Generalises (or refutes) the CCN model beyond tubulin.

  T28  Coevolution / mutual information across the 8 fetched
       beta-tubulin isotypes. For each residue pair, compute the
       pairwise mutual information from the multiple sequence
       alignment. Identify residues that coevolve with the H-CCN
       top-5. Coevolving pairs => functionally coupled.

Outputs:
  output/T27_glic_cross_target.json
  output/T27_glic_ccn_score.png
  output/T28_coevolution.json
  output/T28_coevolution_network.png
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from collections import Counter, defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
PDB_DIR = REPO_ROOT / "external_data" / "pdb"
SEQ_DIR = REPO_ROOT / "external_data" / "isotype_sequences"
OUTPUT_DIR = REPO_ROOT / "repro" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(REPO_ROOT / "repro"))
from ccn_site_ranking import parse_mmcif, select_chain_ca, AROMATIC_RESIDUES  # type: ignore
from chemistry_context import get_ring_atoms, ring_centroid  # type: ignore


# ============================================================
# T27: Cross-target CCN on GLIC
# ============================================================

def find_ligand_atoms_in_pdb(pdb_id, ligand_codes):
    """Find HETATM atoms matching any ligand code in a PDB file.
       Returns list of (chain, resnum, code, position)."""
    from chemistry_context import parse_mmcif_with_hetatm
    path = PDB_DIR / f"{pdb_id}.cif"
    if not path.exists():
        return []
    atoms = parse_mmcif_with_hetatm(path)
    matches = []
    for a in atoms:
        if a.get("kind") == "HETATM" and a.get("comp") in ligand_codes:
            matches.append((a["auth_chain"], a["resnum"], a["comp"],
                           np.array([a["x"], a["y"], a["z"]])))
    return matches


def t27_glic_ccn():
    """Score GLIC aromatic residues by a CCN-like model and check
       whether the ranking matches known anaesthetic-binding sites."""
    # 3P50 = GLIC + propofol (ligand code: PFL or similar)
    # 4HFI = GLIC + desflurane (ligand code: DFL)
    propofol_codes = ["PFL", "PRO", "P9P", "P3F"]  # try common codes
    desflurane_codes = ["DSF", "DFL", "F4D"]  # try common codes
    glic_results = {}
    for pdb_id, ligand_codes, ligand_name in [
        ("3P50", propofol_codes, "propofol"),
        ("4HFI", desflurane_codes, "desflurane"),
    ]:
        path = PDB_DIR / f"{pdb_id}.cif"
        if not path.exists():
            print(f"  [SKIP] {pdb_id} not on disk")
            continue
        atoms = parse_mmcif(path)
        ligand_atoms = find_ligand_atoms_in_pdb(pdb_id, ligand_codes)
        if not ligand_atoms:
            print(f"  {pdb_id}: no ligand found with codes {ligand_codes}; "
                  f"trying to find anaesthetic-binding pocket via residue inventory")
            # Get HETATM inventory to find the actual ligand code
            from chemistry_context import parse_mmcif_with_hetatm
            all_atoms = parse_mmcif_with_hetatm(path)
            het_codes = Counter()
            for a in all_atoms:
                if a.get("kind") == "HETATM":
                    het_codes[a.get("comp")] += 1
            top_codes = het_codes.most_common(10)
            print(f"    Top HETATM codes in {pdb_id}: {top_codes}")
            # Skip if no clear anaesthetic ligand
            continue
        print(f"  {pdb_id} ({ligand_name}): {len(ligand_atoms)} ligand atoms found")
        # Get chains
        chains = sorted(set(a["auth_chain"] for a in atoms))
        # Pick the chain with most residues (canonical GLIC subunit)
        ref_chain = None
        max_residues = 0
        for ch in chains:
            ch_ca = [a for a in atoms if a["auth_chain"] == ch and a["atom"] == "CA"]
            if len(ch_ca) > max_residues:
                max_residues = len(ch_ca)
                ref_chain = ch
        if ref_chain is None:
            continue
        print(f"    reference chain: {ref_chain} ({max_residues} residues)")

        # Extract aromatic residues
        ca_data = select_chain_ca(atoms, ref_chain)
        aromatic_residues = [(rn, comp, pos) for (rn, comp, pos) in ca_data
                             if comp in AROMATIC_RESIDUES]
        print(f"    aromatic residues in chain {ref_chain}: {len(aromatic_residues)}")

        # Score each aromatic residue by:
        # (a) aromatic-network centrality
        # (b) distance to ligand atoms (binding-pocket proximity)
        # (c) surface-vs-buried proxy
        scores = {}
        for (rn, comp, pos) in aromatic_residues:
            # Aromatic neighbours within 8 A
            arom_n = sum(1 for (rn2, comp2, pos2) in aromatic_residues
                         if rn2 != rn and np.linalg.norm(pos - pos2) < 8.0)
            # Distance to nearest ligand atom
            ring = get_ring_atoms(atoms, ref_chain, comp, rn)
            if ring:
                centroid = ring_centroid(ring)
                ligand_dist = min(np.linalg.norm(centroid - la[3])
                                  for la in ligand_atoms)
            else:
                centroid = pos
                ligand_dist = float("inf")
            # Burial proxy
            n_neighbours = sum(1 for (rn2, c2, p2) in ca_data
                               if rn2 != rn and np.linalg.norm(pos - p2) < 8.0)
            scores[(rn, comp)] = {
                "ligand_distance_A": float(ligand_dist),
                "aromatic_neighbours_8A": int(arom_n),
                "ca_neighbours_8A": int(n_neighbours),
            }
        glic_results[pdb_id] = {
            "ligand_name": ligand_name,
            "ref_chain": ref_chain,
            "n_aromatic_residues": len(aromatic_residues),
            "scores": scores,
        }

    # Analysis: in each GLIC structure, rank aromatic residues by proximity
    # to ligand (the standard "this is the binding site" measure). Then
    # also rank by aromatic-network centrality. If the two rankings
    # CORRELATE, that's evidence the CCN-style aromatic-network metric
    # captures real anaesthetic-binding sites in a different protein.
    for pdb_id, info in glic_results.items():
        scores = info["scores"]
        if not scores:
            continue
        # Get ligand-pocket residues = within 10 A of ligand
        pocket = [(k, v) for k, v in scores.items()
                  if v["ligand_distance_A"] < 10.0]
        # Get high-aromatic-network residues = top 10 by aromatic neighbours
        sorted_by_arom = sorted(scores.items(),
                                key=lambda x: -x[1]["aromatic_neighbours_8A"])[:10]
        print(f"\n  {pdb_id} ({info['ligand_name']}):")
        print(f"    Pocket-lining aromatic residues (< 10 A from ligand): "
              f"{len(pocket)}")
        for k, v in sorted(pocket, key=lambda x: x[1]["ligand_distance_A"])[:5]:
            print(f"      {k[1]}{k[0]}: ligand dist {v['ligand_distance_A']:.1f} A, "
                  f"arom neighbours {v['aromatic_neighbours_8A']}")
        print(f"    Top-5 by aromatic-network centrality:")
        for k, v in sorted_by_arom[:5]:
            print(f"      {k[1]}{k[0]}: arom neighbours {v['aromatic_neighbours_8A']}, "
                  f"ligand dist {v['ligand_distance_A']:.1f} A")
        # Overlap: how many top-5-by-aromatic are also in pocket?
        pocket_resnums = {k for k, v in pocket}
        aromatic_top5_resnums = {k for k, v in sorted_by_arom[:5]}
        overlap = pocket_resnums & aromatic_top5_resnums
        info["pocket_size"] = len(pocket)
        info["top_5_aromatic"] = [{"residue": f"{k[1]}{k[0]}", **v}
                                   for k, v in sorted_by_arom[:5]]
        info["pocket_residues"] = [{"residue": f"{k[1]}{k[0]}", **v}
                                    for k, v in sorted(pocket, key=lambda x: x[1]["ligand_distance_A"])]
        info["overlap_aromatic_top5_with_pocket"] = len(overlap)
        info["recovery_rate"] = (len(overlap) / 5.0) * 100
        print(f"    OVERLAP: {len(overlap)}/5 top-aromatic residues are in pocket "
              f"({info['recovery_rate']:.0f}% recovery rate)")

    return glic_results


# ============================================================
# T28: Coevolution across isotypes
# ============================================================

def parse_fasta_file(path):
    """Parse a single FASTA file, return the sequence."""
    if not path.exists():
        return None
    text = path.read_text()
    seq = []
    for line in text.splitlines():
        if line.startswith(">"):
            continue
        seq.append(line.strip())
    return "".join(seq)


def t28_coevolution():
    """Compute mutual information across the 8 mammalian beta-tubulin
       isotype sequences. Identify residues coevolving with H-CCN top-5."""
    # Load sequences
    sequences = {}
    for path in SEQ_DIR.glob("*.fasta"):
        gene = path.stem.split("_", 1)[1] if "_" in path.stem else path.stem
        seq = parse_fasta_file(path)
        if seq:
            sequences[gene] = seq
    # Filter to mammalian isotypes only (exclude yeast, Arabidopsis)
    mammalian = ["TUBB", "TUBB2A", "TUBB2B", "TUBB3", "TUBB4A",
                 "TUBB4B", "TUBB6", "TUBB8"]
    seqs = {g: sequences[g] for g in mammalian if g in sequences}
    if len(seqs) < 4:
        print(f"  [SKIP] not enough mammalian sequences ({len(seqs)})")
        return None
    # All sequences should be similar length, but let's use a simple
    # offset alignment by anchoring on the NEALYDICF 9-mer
    anchor = "NEALYDICF"
    alignments = {}
    target_length = None
    for gene, seq in seqs.items():
        loc = seq.find(anchor)
        if loc < 0:
            continue
        # Use position 210 as the anchor: idx of Y in anchor = position 4
        offset = loc + 4 - 209  # Y in NEALYDICF is at index 4, which is PDB pos 210
        # We want a common range [50, 400] in PDB numbering
        start_pdb = 50
        end_pdb = 400
        start_idx = start_pdb - 1 + offset
        end_idx = end_pdb + offset
        if 0 <= start_idx < end_idx <= len(seq):
            aligned = seq[start_idx:end_idx]
            alignments[gene] = aligned
            target_length = end_idx - start_idx
    if not alignments or len(alignments) < 4:
        print(f"  [SKIP] couldn't align enough sequences")
        return None
    print(f"  Aligned {len(alignments)} mammalian isotypes (PDB positions 50-400)")

    # Build alignment matrix: rows = isotypes, columns = positions
    matrix = []
    isotypes_used = sorted(alignments.keys())
    for g in isotypes_used:
        matrix.append(list(alignments[g]))
    matrix = np.array(matrix)  # shape (n_isotypes, n_positions)
    n_isotypes, n_pos = matrix.shape
    print(f"  alignment shape: {matrix.shape}")

    # For each column, compute Shannon entropy
    entropy_per_col = []
    for c in range(n_pos):
        counts = Counter(matrix[:, c])
        ps = np.array(list(counts.values())) / n_isotypes
        h = -np.sum(ps * np.log2(ps + 1e-12))
        entropy_per_col.append(h)
    entropy_per_col = np.array(entropy_per_col)

    # Identify variable columns (entropy > 0)
    variable_cols = np.where(entropy_per_col > 0)[0]
    print(f"  variable positions (across all 8 isotypes): {len(variable_cols)}")

    # For each H-CCN top-5 position, compute mutual information with all
    # other variable positions
    top_5_pdb_positions = [210, 202, 185, 214, 53]
    top_5_offset_positions = [p - 50 for p in top_5_pdb_positions]  # convert to alignment index
    coevolution_per_top5 = {}
    for target_pdb_pos, target_idx in zip(top_5_pdb_positions, top_5_offset_positions):
        if not (0 <= target_idx < n_pos):
            continue
        target_col = matrix[:, target_idx]
        if entropy_per_col[target_idx] == 0:
            # Target is universally conserved -> mutual information will be 0 everywhere
            coevolution_per_top5[target_pdb_pos] = {
                "target_entropy": 0.0,
                "note": "universally conserved; no coevolution detectable",
                "partners": [],
            }
            continue
        # MI with every variable column
        mi_partners = []
        for other_idx in variable_cols:
            if other_idx == target_idx:
                continue
            other_col = matrix[:, other_idx]
            # MI = H(A) + H(B) - H(A,B)
            ha = entropy_per_col[target_idx]
            hb = entropy_per_col[other_idx]
            joint_counts = Counter(zip(target_col, other_col))
            ps = np.array(list(joint_counts.values())) / n_isotypes
            hab = -np.sum(ps * np.log2(ps + 1e-12))
            mi = ha + hb - hab
            other_pdb_pos = int(other_idx) + 50
            mi_partners.append({
                "target_pdb_position": target_pdb_pos,
                "partner_pdb_position": other_pdb_pos,
                "mi": float(mi),
                "target_entropy": float(ha),
                "partner_entropy": float(hb),
            })
        # Rank
        mi_partners.sort(key=lambda x: -x["mi"])
        coevolution_per_top5[target_pdb_pos] = {
            "target_entropy": float(entropy_per_col[target_idx]),
            "n_variable_partners": len(mi_partners),
            "top_partners": mi_partners[:5],
        }
    return coevolution_per_top5, variable_cols, isotypes_used


# ============================================================
# Main
# ============================================================

def main():
    print("=" * 70)
    print("Note G T27/T28 --- cross-target + coevolution")
    print("=" * 70)
    print()

    # T27
    print("T27: cross-target CCN validation on GLIC")
    glic_results = t27_glic_ccn()
    if glic_results:
        with open(OUTPUT_DIR / "T27_glic_cross_target.json", "w") as f:
            json.dump({
                "results": {
                    k: {kk: vv for kk, vv in v.items() if kk != "scores"}
                    for k, v in glic_results.items()
                },
            }, f, indent=2)
        # Figure
        fig, axes = plt.subplots(1, len(glic_results), figsize=(10, 4), sharey=True)
        if len(glic_results) == 1:
            axes = [axes]
        for ax, (pdb_id, info) in zip(axes, glic_results.items()):
            if not info.get("scores"):
                continue
            arom_n = [v["aromatic_neighbours_8A"] for v in info["scores"].values()]
            lig_d = [v["ligand_distance_A"] for v in info["scores"].values()]
            ax.scatter(lig_d, arom_n, color="#cd3a3a", alpha=0.6, edgecolor="black", linewidth=0.3)
            ax.set_xlabel("distance to ligand (Å)")
            ax.set_ylabel("aromatic neighbours within 8 Å")
            ax.set_title(f"{pdb_id} ({info['ligand_name']})\n"
                         f"recovery: {info.get('recovery_rate', 0):.0f}%")
            ax.axvline(10, linestyle=":", color="gray", linewidth=0.7)
            ax.grid(alpha=0.3)
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "T27_glic_ccn_score.png", dpi=120)
        plt.close()
        print(f"  saved T27_glic_cross_target.json + T27_glic_ccn_score.png")
    print()

    # T28
    print("T28: coevolution / mutual information across β-tubulin isotypes")
    result = t28_coevolution()
    if result is None:
        print("  [SKIP] could not compute coevolution")
    else:
        coevolution_per_top5, variable_cols, isotypes = result
        print(f"  Mammalian isotypes used: {isotypes}")
        print()
        # Report top coevolving partners for each top-5 residue
        for target_pdb_pos, info in coevolution_per_top5.items():
            print(f"  Top-5 residue at PDB pos {target_pdb_pos} "
                  f"(entropy = {info.get('target_entropy', 0):.3f} bits):")
            if "note" in info:
                print(f"    {info['note']}")
            else:
                for p in info.get("top_partners", [])[:5]:
                    print(f"    coevolves with pos {p['partner_pdb_position']}: "
                          f"MI = {p['mi']:.3f} bits (partner entropy "
                          f"= {p['partner_entropy']:.3f})")
        with open(OUTPUT_DIR / "T28_coevolution.json", "w") as f:
            json.dump({
                "isotypes": isotypes,
                "n_variable_positions": int(len(variable_cols)),
                "coevolution_per_top5": coevolution_per_top5,
            }, f, indent=2)
        # Figure: heatmap of top-5 vs top coevolving partners
        fig, ax = plt.subplots(figsize=(8, 5))
        max_partners = 5
        labels_y = []
        rows = []
        for target_pdb_pos, info in coevolution_per_top5.items():
            label = f"pos {target_pdb_pos}"
            labels_y.append(label)
            row = [p["mi"] for p in info.get("top_partners", [])[:max_partners]]
            row += [0.0] * (max_partners - len(row))
            rows.append(row)
        rows_arr = np.array(rows)
        if rows_arr.size > 0:
            im = ax.imshow(rows_arr, cmap="YlOrRd", aspect="auto")
            plt.colorbar(im, ax=ax, label="MI (bits)")
            ax.set_yticks(range(len(labels_y)))
            ax.set_yticklabels(labels_y)
            ax.set_xlabel("top-5 coevolving partner (by MI rank)")
            ax.set_title("T28 top coevolving partners per H-CCN top-5 residue")
            plt.tight_layout()
            plt.savefig(OUTPUT_DIR / "T28_coevolution_network.png", dpi=120)
            plt.close()
            print(f"  saved T28_coevolution.json + T28_coevolution_network.png")
    print()
    print("=" * 70)
    print("T27/T28 complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
