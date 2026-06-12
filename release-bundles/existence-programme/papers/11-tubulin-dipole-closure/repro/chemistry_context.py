#!/usr/bin/env python3
"""
Note G --- T16: PDB-derived chemistry microenvironment for the H-CCN top-5.

For each of betaY210, betaY202, betaY185, betaF214, betaY53:
  - extract aromatic ring centroid + atoms (chain B of 4O4H)
  - list all heavy atoms from any chain within 4 A of the ring centroid
  - classify the contacting residues by type (polar/charged/hydrophobic/aromatic)
  - compute approximate secondary-structure context from local Calpha geometry
  - measure minimum distance from each residue's ring centroid to
    paclitaxel (TA1) and epothilone (POU) ligand atoms in 1JFF and 5SYE

Outputs:
  output/T16_chemistry_context.json   per-residue chemistry summary
  output/T16_microenvironment.md       human-readable summary table

Run:
  python chemistry_context.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from collections import Counter, defaultdict

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
PDB_DIR = REPO_ROOT / "external_data" / "pdb"
OUTPUT_DIR = REPO_ROOT / "repro" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(REPO_ROOT / "repro"))
from ccn_site_ranking import parse_mmcif  # type: ignore  # noqa: E402

# H-CCN top-5
TOP_5 = [
    ("TYR", 210, "vinca centroid; halothane direct-contact (Craddock 2012)"),
    ("TYR", 202, "novel; vinca-adjacent, 3 aromatic neighbours"),
    ("TYR", 185, "novel; T5-loop, longitudinal contact, allosteric hinge"),
    ("PHE", 214, "novel; H6-helix close-vinca (6 A from centroid)"),
    ("TYR",  53, "novel; N-terminal-proximal, longitudinal contact face"),
]

# Aromatic ring atom names
RING_ATOMS = {
    "TYR": ["CG", "CD1", "CD2", "CE1", "CE2", "CZ"],
    "PHE": ["CG", "CD1", "CD2", "CE1", "CE2", "CZ"],
    "TRP": ["CG", "CD1", "CD2", "NE1", "CE2", "CE3", "CZ2", "CZ3", "CH2"],
}

# Residue chemical classification
POLAR = {"SER", "THR", "ASN", "GLN", "TYR", "HIS", "CYS"}  # H-bond donor/acceptor
CHARGED_POS = {"LYS", "ARG", "HIS"}  # His marginally
CHARGED_NEG = {"ASP", "GLU"}
HYDROPHOBIC = {"ALA", "VAL", "LEU", "ILE", "MET", "PRO", "GLY", "CYS"}
AROMATIC = {"PHE", "TYR", "TRP", "HIS"}


def classify(comp):
    """Return chemical category for a residue (multi-tag possible)."""
    tags = []
    if comp in AROMATIC:
        tags.append("aromatic")
    if comp in CHARGED_POS:
        tags.append("charged+")
    if comp in CHARGED_NEG:
        tags.append("charged-")
    if comp in POLAR and comp not in CHARGED_POS and comp not in CHARGED_NEG:
        tags.append("polar")
    if comp in HYDROPHOBIC:
        tags.append("hydrophobic")
    return tags if tags else ["other"]


def get_ring_atoms(atoms, auth_chain, comp, resnum):
    """Return positions of the aromatic ring atoms for a specific residue."""
    target = set(RING_ATOMS.get(comp, []))
    ring = []
    for a in atoms:
        if (a["auth_chain"] == auth_chain
                and a["comp"] == comp
                and a["resnum"] == resnum
                and a["atom"] in target):
            ring.append((a["atom"], np.array([a["x"], a["y"], a["z"]])))
    return ring


def ring_centroid(ring_atoms):
    """Centroid of the ring."""
    positions = np.array([p for (_, p) in ring_atoms])
    return positions.mean(axis=0)


def find_neighbours_of_centroid(atoms, centroid, exclude_chain_resnum, cutoff=6.0):
    """All heavy atoms (any chain) within cutoff of the centroid, excluding
       the target residue's own atoms."""
    contacts = []
    for a in atoms:
        if a["atom"].startswith("H"):
            continue  # skip hydrogens
        if (a["auth_chain"], a["resnum"]) == exclude_chain_resnum:
            continue
        d = np.linalg.norm(np.array([a["x"], a["y"], a["z"]]) - centroid)
        if d < cutoff:
            contacts.append({
                "chain": a["auth_chain"],
                "resnum": a["resnum"],
                "residue": a["comp"],
                "atom": a["atom"],
                "distance": float(d),
            })
    return contacts


def summarise_microenvironment(contacts):
    """Count contacting residues by chemical category."""
    seen_residues = {}
    for c in contacts:
        key = (c["chain"], c["resnum"])
        if key not in seen_residues or c["distance"] < seen_residues[key]["distance"]:
            seen_residues[key] = c
    by_class = Counter()
    for res_info in seen_residues.values():
        tags = classify(res_info["residue"])
        for tag in tags:
            by_class[tag] += 1
    return seen_residues, by_class


def approximate_secondary_structure(atoms, auth_chain, resnum, window=4):
    """Heuristic alpha-helix/beta-sheet detection from i, i+3 and i, i+4
       Calpha distances. Helix: typical Calpha(i)-Calpha(i+3) ~ 5.5 A,
       Calpha(i)-Calpha(i+4) ~ 6.2 A.  Sheet: Calpha(i)-Calpha(i+2) ~ 6-7 A
       in extended, Calpha(i)-Calpha(i+1) ~ 3.8 A always."""
    ca_window = {}
    for a in atoms:
        if a["auth_chain"] == auth_chain and a["atom"] == "CA":
            ca_window[a["resnum"]] = np.array([a["x"], a["y"], a["z"]])
    if resnum not in ca_window:
        return "unknown"
    # Get distances
    try:
        d3 = np.linalg.norm(ca_window[resnum + 3] - ca_window[resnum])
        d4 = np.linalg.norm(ca_window[resnum + 4] - ca_window[resnum])
        if 4.5 < d3 < 6.5 and 5.5 < d4 < 7.0:
            return "alpha-helix"
        elif d3 > 9.0:
            return "beta-sheet/extended"
        else:
            return "loop/other"
    except KeyError:
        return "unknown (terminus)"


def measure_ligand_distances(top_5_ring_centroids, ligand_atoms):
    """For each top-5 residue, minimum distance to any ligand atom."""
    out = {}
    for (comp, resnum, _), centroid in top_5_ring_centroids.items():
        if not ligand_atoms:
            out[(comp, resnum)] = None
        else:
            dists = [np.linalg.norm(np.array([a["x"], a["y"], a["z"]]) - centroid)
                     for a in ligand_atoms]
            out[(comp, resnum)] = float(min(dists))
    return out


def extract_ligand_atoms(atoms, ligand_code):
    """Extract HETATM positions for a specific ligand code."""
    out = []
    for a in atoms:
        if a.get("comp") == ligand_code:  # may not have "comp" in HETATM
            out.append(a)
    return out


def parse_mmcif_with_hetatm(path):
    """Variant of the parser that includes HETATM records."""
    with open(path) as f:
        lines = f.readlines()
    start = None
    for i, l in enumerate(lines):
        if l.startswith("_atom_site.group_PDB"):
            start = i
            break
    if start is None:
        return []
    header_cols = []
    i = start
    while i < len(lines) and lines[i].startswith("_atom_site."):
        header_cols.append(lines[i].strip().split(".")[1])
        i += 1
    col = {name: idx for idx, name in enumerate(header_cols)}
    atoms = []
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith("#") or line.startswith("loop_") or line.startswith("_"):
            break
        parts = line.split()
        if len(parts) < len(header_cols):
            i += 1
            continue
        kind = parts[col["group_PDB"]]
        if kind not in ("ATOM", "HETATM"):
            i += 1
            continue
        try:
            rec = {
                "kind": kind,
                "comp": parts[col["label_comp_id"]],
                "label_chain": parts[col["label_asym_id"]],
                "auth_chain": parts[col["auth_asym_id"]],
                "resnum": int(parts[col["auth_seq_id"]]) if parts[col["auth_seq_id"]] != "." else -1,
                "atom": parts[col["label_atom_id"]],
                "x": float(parts[col["Cartn_x"]]),
                "y": float(parts[col["Cartn_y"]]),
                "z": float(parts[col["Cartn_z"]]),
            }
            atoms.append(rec)
        except (ValueError, KeyError):
            pass
        i += 1
    return atoms


def main():
    print("=" * 70)
    print("Note G T16 --- chemistry microenvironment for H-CCN top-5")
    print("=" * 70)
    print()

    # Load 4O4H for the primary chain B microenvironment
    atoms = parse_mmcif(PDB_DIR / "4O4H.cif")
    print(f"4O4H atoms loaded: {len(atoms)}")

    # Compute ring centroids
    top_5_centroids = {}
    for (comp, resnum, role) in TOP_5:
        ring = get_ring_atoms(atoms, "B", comp, resnum)
        if not ring:
            print(f"  [SKIP] {comp}{resnum} ring atoms not found in 4O4H chain B")
            continue
        cent = ring_centroid(ring)
        top_5_centroids[(comp, resnum, role)] = cent
        print(f"  {comp}{resnum} ring centroid: {cent}")
    print()

    # Per-residue microenvironment
    chemistry_per_residue = {}
    for (comp, resnum, role), centroid in top_5_centroids.items():
        contacts_4A = find_neighbours_of_centroid(atoms, centroid, ("B", resnum), cutoff=4.0)
        contacts_6A = find_neighbours_of_centroid(atoms, centroid, ("B", resnum), cutoff=6.0)
        residues_4A, cats_4A = summarise_microenvironment(contacts_4A)
        residues_6A, cats_6A = summarise_microenvironment(contacts_6A)
        ss = approximate_secondary_structure(atoms, "B", resnum)
        chemistry_per_residue[f"{comp}{resnum}"] = {
            "role": role,
            "ring_centroid": centroid.tolist(),
            "secondary_structure_approx": ss,
            "contacts_within_4A": [
                {"chain": k[0], "resnum": k[1], "residue": v["residue"],
                 "closest_atom": v["atom"], "distance": v["distance"]}
                for k, v in sorted(residues_4A.items(), key=lambda x: x[1]["distance"])
            ],
            "contacts_within_6A": [
                {"chain": k[0], "resnum": k[1], "residue": v["residue"],
                 "closest_atom": v["atom"], "distance": v["distance"]}
                for k, v in sorted(residues_6A.items(), key=lambda x: x[1]["distance"])
            ],
            "neighbour_class_counts_4A": dict(cats_4A),
            "neighbour_class_counts_6A": dict(cats_6A),
        }

    # Distance to ligand atoms in other PDBs
    ligand_distances = {}
    for pdb_id, ligand_code, ligand_name in [
        ("1JFF", "TA1", "paclitaxel"),
        ("5SYE", "POU", "epothilone analogue"),
        ("5SYE", "TA1", "paclitaxel (5SYE)"),
        ("5SYC", "POU", "epothilone analogue (5SYC)"),
    ]:
        pdb_path = PDB_DIR / f"{pdb_id}.cif"
        if not pdb_path.exists():
            print(f"  [SKIP] {pdb_id}.cif not found for {ligand_name}")
            continue
        ligand_atoms_pdb = parse_mmcif_with_hetatm(pdb_path)
        ligands = [a for a in ligand_atoms_pdb if a["comp"] == ligand_code]
        if not ligands:
            print(f"  [SKIP] no {ligand_code} atoms in {pdb_id}")
            continue
        # Note: ring centroids were computed on 4O4H frame, not 1JFF/5SYE frame.
        # For accurate ligand-distance, we should compute distance to BOTH the
        # native-frame ring centroid AND the ligand atoms in the SAME pdb.
        # So we need to recompute ring centroid on this ligand-bearing pdb.
        local_centroids = {}
        for (comp, resnum, role) in TOP_5:
            ring = get_ring_atoms(ligand_atoms_pdb, "B", comp, resnum)
            if ring:
                local_centroids[(comp, resnum)] = ring_centroid(ring)
        if not local_centroids:
            print(f"  [INFO] {pdb_id} chain B doesn't have top-5 residues at same numbering")
            continue
        # Distance from each local-frame centroid to nearest ligand atom
        for (comp, resnum), centroid in local_centroids.items():
            dists = [np.linalg.norm(np.array([a["x"], a["y"], a["z"]]) - centroid)
                     for a in ligands]
            min_d = float(min(dists))
            ligand_distances.setdefault(f"{comp}{resnum}", {})[f"{pdb_id}_{ligand_code}"] = min_d
            print(f"  {comp}{resnum} -> {pdb_id} {ligand_code} (n={len(ligands)} atoms): "
                  f"min dist = {min_d:.2f} A")
    print()

    # Inject ligand distances into the chemistry record
    for resname, ld in ligand_distances.items():
        if resname in chemistry_per_residue:
            chemistry_per_residue[resname]["ligand_distances_angstrom"] = ld

    # Save JSON
    with open(OUTPUT_DIR / "T16_chemistry_context.json", "w") as f:
        json.dump(chemistry_per_residue, f, indent=2)
    print(f"Saved T16_chemistry_context.json")
    print()

    # Build human-readable markdown summary
    md = ["# T16 Chemistry microenvironment for H-CCN top-5 residues\n"]
    md.append("Generated from 4O4H (apo alpha-beta tubulin dimer, chain B) "
              "and ligand-bound PDBs (1JFF paclitaxel, 5SYC/5SYE epothilone).\n")
    md.append("\n## Per-residue chemistry summary\n")
    for (comp, resnum, role) in TOP_5:
        key = f"{comp}{resnum}"
        if key not in chemistry_per_residue:
            continue
        rec = chemistry_per_residue[key]
        md.append(f"\n### {key} — {role}\n")
        md.append(f"- **Secondary structure (approximate):** {rec['secondary_structure_approx']}")
        md.append(f"- **Heavy-atom contacts within 4 Å (immediate neighbours):**")
        if rec["contacts_within_4A"]:
            for c in rec["contacts_within_4A"]:
                md.append(f"  - {c['residue']}{c['resnum']} (chain {c['chain']}) atom {c['closest_atom']} at {c['distance']:.2f} Å")
        else:
            md.append("  - none (solvent-exposed ring)")
        md.append(f"- **Chemical environment within 6 Å (neighbour-class counts):**")
        for cls, n in sorted(rec["neighbour_class_counts_6A"].items(), key=lambda x: -x[1]):
            md.append(f"  - {cls}: {n}")
        if "ligand_distances_angstrom" in rec:
            md.append(f"- **Distance to drug ligands (other PDBs):**")
            for lname, dist in sorted(rec["ligand_distances_angstrom"].items()):
                bucket = ("in-pocket" if dist < 6 else
                          "pocket-rim" if dist < 10 else
                          "distant")
                md.append(f"  - {lname}: {dist:.2f} Å ({bucket})")
    md.append("\n## Chemistry-context interpretation\n")
    md.append("**Direct pocket-lining:** residues whose ring centroid is < 6 Å "
              "from any drug ligand atom in any structural snapshot.")
    md.append("**Aromatic-cluster propagator:** residues with multiple aromatic "
              "neighbours within 6 Å but no direct ligand contact in any PDB.")
    md.append("**Lattice-propagation hinge:** residues at T5-loop or longitudinal "
              "contact positions with low pocket proximity but high CCN score.\n")
    with open(OUTPUT_DIR / "T16_microenvironment.md", "w") as f:
        f.write("\n".join(md))
    print(f"Saved T16_microenvironment.md")
    print()

    # Print summary table to stdout
    print(" " + "=" * 70)
    print(" Chemistry context (4 A contacts + 6 A class composition)")
    print(" " + "=" * 70)
    for (comp, resnum, role) in TOP_5:
        key = f"{comp}{resnum}"
        if key not in chemistry_per_residue:
            continue
        rec = chemistry_per_residue[key]
        print(f"\n {key}  ({rec['secondary_structure_approx']})")
        if rec["contacts_within_4A"]:
            print(f"   nearest contacts (<4 A): " +
                  ", ".join(f"{c['residue']}{c['resnum']}({c['distance']:.1f}A)"
                            for c in rec["contacts_within_4A"][:5]))
        else:
            print(f"   nearest contacts (<4 A): none — solvent-exposed")
        cls_str = ", ".join(f"{k}={v}" for k, v in
                            sorted(rec["neighbour_class_counts_6A"].items(),
                                   key=lambda x: -x[1]))
        print(f"   neighbour-class (6 A): {cls_str}")
        if "ligand_distances_angstrom" in rec:
            ld = rec["ligand_distances_angstrom"]
            print(f"   ligand dists: " +
                  ", ".join(f"{n}={d:.1f}A" for n, d in sorted(ld.items())))
    print()
    print("=" * 70)
    print("T16 complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
