#!/usr/bin/env python3
"""
Note G --- T22: beta-tubulin isotype variation at H-CCN top-5.

Fetch beta-tubulin isotype sequences from UniProt for the clinically
relevant human isotypes (and a representative non-mammalian + plant
sequence), then check the H-CCN top-5 positions (210, 202, 185, 214,
53) for conservation or variation.

  - High conservation => essential structural / functional role
    (supports H-CCN site assignment)
  - Variation in beta-III (taxane-resistant tumors) => clinical
    pharmacology angle
  - Variation across non-mammalian => evolutionary tunability

UniProt isotype list:
  P07437  TUBB    (beta-V, ubiquitous)
  Q13885  TUBB2A
  Q9BVA1  TUBB2B
  Q13509  TUBB3   (beta-III, neuronal, taxane-resistance)
  P04350  TUBB4A  (beta-IVa, brain)
  P68371  TUBB4B  (beta-IVb)
  Q9BUF5  TUBB6
  Q3ZCM7  TUBB8
  P09204  TUB2_YEAST (yeast beta-tubulin)
  P29512  TUB1_ARATH (Arabidopsis beta-tubulin)

Outputs:
  external_data/isotype_sequences/*.fasta    fetched sequences
  output/T22_isotype_conservation.json
  output/T22_isotype_alignment.md            human-readable summary
"""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PDB_DIR = REPO_ROOT / "external_data" / "pdb"
SEQ_DIR = REPO_ROOT / "external_data" / "isotype_sequences"
OUTPUT_DIR = REPO_ROOT / "repro" / "output"
SEQ_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ISOTYPES = [
    ("P07437", "TUBB",     "human beta-V (ubiquitous)"),
    ("Q13885", "TUBB2A",   "human beta-IIa"),
    ("Q9BVA1", "TUBB2B",   "human beta-IIb"),
    ("Q13509", "TUBB3",    "human beta-III (neuronal, taxane-resistance)"),
    ("P04350", "TUBB4A",   "human beta-IVa (brain)"),
    ("P68371", "TUBB4B",   "human beta-IVb"),
    ("Q9BUF5", "TUBB6",    "human beta-VI"),
    ("Q3ZCM7", "TUBB8",    "human beta-VIII (gonadal)"),
    ("P09204", "TUB2_YEAST", "yeast beta-tubulin"),
    ("P29512", "TUB1_ARATH", "Arabidopsis beta-tubulin"),
]

TOP_5_POSITIONS = [
    ("Y", 210, "vinca centroid; halothane direct-contact"),
    ("Y", 202, "novel; vinca-adjacent, 3 aromatic neighbours"),
    ("Y", 185, "novel; T5-loop, longitudinal contact"),
    ("F", 214, "novel; H6-helix close-vinca"),
    ("Y",  53, "novel; N-terminal-proximal"),
]


def fetch_uniprot_fasta(accession, dest):
    """Fetch a UniProt FASTA. Idempotent."""
    if dest.exists() and dest.stat().st_size > 0:
        return "exists"
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
    req = urllib.request.Request(url, headers={
        "User-Agent": "vfd-existence-programme/1.1.0 (research; contact@vibrationalfielddynamics.org)",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        dest.write_bytes(data)
        return "fetched"
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
        return f"error_{e}"


def parse_fasta(text):
    """Return (header, sequence) tuples for each FASTA entry."""
    lines = text.splitlines()
    entries = []
    header = None
    seq = []
    for l in lines:
        if l.startswith(">"):
            if header:
                entries.append((header, "".join(seq)))
            header = l[1:]
            seq = []
        else:
            seq.append(l.strip())
    if header:
        entries.append((header, "".join(seq)))
    return entries


def main():
    print("=" * 70)
    print("Note G T22 --- beta-tubulin isotype variation at H-CCN top-5")
    print("=" * 70)
    print()

    # Fetch sequences
    sequences = {}
    for accession, gene, desc in ISOTYPES:
        dest = SEQ_DIR / f"{accession}_{gene}.fasta"
        outcome = fetch_uniprot_fasta(accession, dest)
        print(f"  [{outcome:>14}] {accession}  {gene}  {desc}")
        if dest.exists() and dest.stat().st_size > 0:
            entries = parse_fasta(dest.read_text())
            if entries:
                sequences[gene] = {
                    "accession": accession,
                    "description": desc,
                    "sequence": entries[0][1],
                    "header": entries[0][0],
                }
        if outcome == "fetched":
            time.sleep(0.4)
    if not sequences:
        print("  [FAIL] No sequences fetched. Network or UniProt unavailable.")
        return 1
    print()
    print(f"Fetched {len(sequences)} isotype sequences")
    print()

    # Extract the actual 4O4H chain B sequence and use it as the alignment
    # anchor. Crystal structures often have different numbering than UniProt
    # due to species choice, leader processing, etc., so we use
    # sequence-context-based offset detection per isotype.
    pdb_4o4h_path = PDB_DIR / "4O4H.cif"
    if not pdb_4o4h_path.exists():
        print(f"  [SKIP] 4O4H.cif not found")
        return 1

    from ccn_site_ranking import parse_mmcif  # type: ignore
    AA_3TO1 = {
        "ALA": "A", "CYS": "C", "ASP": "D", "GLU": "E", "PHE": "F",
        "GLY": "G", "HIS": "H", "ILE": "I", "LYS": "K", "LEU": "L",
        "MET": "M", "ASN": "N", "PRO": "P", "GLN": "Q", "ARG": "R",
        "SER": "S", "THR": "T", "VAL": "V", "TRP": "W", "TYR": "Y",
    }
    atoms_4o4h = parse_mmcif(pdb_4o4h_path)
    crystal_seq_dict = {}
    for a in atoms_4o4h:
        if a["auth_chain"] == "B" and a["atom"] == "CA":
            crystal_seq_dict[a["resnum"]] = AA_3TO1.get(a["comp"], "X")
    if not crystal_seq_dict:
        print(f"  [SKIP] no chain B CA atoms in 4O4H")
        return 1
    min_resnum = min(crystal_seq_dict.keys())
    max_resnum = max(crystal_seq_dict.keys())
    crystal_seq = "".join(
        crystal_seq_dict.get(i, "X") for i in range(min_resnum, max_resnum + 1)
    )
    print(f"4O4H chain B crystal sequence: {len(crystal_seq)} aa, "
          f"resnum range {min_resnum}-{max_resnum}")

    # Verify top-5 in 4O4H
    print(f"  Top-5 residues in 4O4H chain B:")
    for (expected, pos, _) in TOP_5_POSITIONS:
        actual = crystal_seq_dict.get(pos, "MISSING")
        print(f"    Pos {pos}: expected {expected}, actual {actual}  "
              f"{'OK' if actual == expected else 'MISMATCH'}")

    # For each UniProt isotype, find the offset by locating a 9-residue
    # sequence context anchored on Y210 in the crystal sequence.
    anchor_pos = 210
    anchor_context = "".join(
        crystal_seq_dict.get(i, "X") for i in range(anchor_pos - 4, anchor_pos + 5)
    )
    print(f"\n  Anchor context (4O4H positions {anchor_pos-4}-{anchor_pos+4}): "
          f"{anchor_context}")
    print(f"  Searching each isotype for this 9-mer to determine offset...")

    isotype_offsets = {}
    for gene, rec in sequences.items():
        seq = rec["sequence"]
        # Find anchor_context in seq
        loc = seq.find(anchor_context)
        if loc < 0:
            # Try shorter 7-mer (residues -3 to +3 around anchor)
            short_context = anchor_context[1:8]
            loc7 = seq.find(short_context)
            if loc7 >= 0:
                offset = loc7 + 3 - anchor_pos + 1  # +1 for 1-based -> 0-based offset
                isotype_offsets[gene] = offset
                print(f"    {gene}: matched 7-mer '{short_context}', offset = {offset}")
            else:
                isotype_offsets[gene] = None
                print(f"    {gene}: anchor not found, sequence may be too divergent")
        else:
            # loc is 0-based position of the start of the 9-mer
            # The middle of the 9-mer (index 4) corresponds to anchor_pos
            offset = loc + 4 - (anchor_pos - 1)  # convert to 1-based offset
            isotype_offsets[gene] = offset
            print(f"    {gene}: offset = {offset} (anchor 9-mer found at index {loc})")

    # Compute variation per position using per-isotype offsets
    print()
    print("Top-5 H-CCN positions across all isotypes (after per-isotype offset alignment):")
    print(f"  {'isotype':<12}  ", end="")
    for (expected, pos, _) in TOP_5_POSITIONS:
        print(f"{pos:>4}  ", end="")
    print()
    per_position = {pos: [] for (_, pos, _) in TOP_5_POSITIONS}
    for gene, rec in sequences.items():
        seq = rec["sequence"]
        gene_offset = isotype_offsets.get(gene)
        if gene_offset is None:
            print(f"  {gene:<12}  [no offset]")
            continue
        print(f"  {gene:<12}  ", end="")
        for (expected, pos, _) in TOP_5_POSITIONS:
            idx = pos - 1 + gene_offset
            if 0 <= idx < len(seq):
                aa = seq[idx]
                marker = "*" if aa == expected else " "
                print(f"{aa}{marker}    ", end="")
                per_position[pos].append((gene, aa))
            else:
                print(f"-     ", end="")
        print()

    # Conservation summary
    print()
    print("Conservation per H-CCN top-5 position:")
    conservation_summary = {}
    for (expected, pos, role) in TOP_5_POSITIONS:
        residues_at_pos = [aa for (_, aa) in per_position[pos]]
        n_total = len(residues_at_pos)
        n_matching = sum(1 for aa in residues_at_pos if aa == expected)
        unique_aas = sorted(set(residues_at_pos))
        conservation_pct = (n_matching / n_total * 100) if n_total else 0
        variants = [(g, aa) for (g, aa) in per_position[pos] if aa != expected]
        print(f"  Pos {pos} ({expected}): {n_matching}/{n_total} = {conservation_pct:.0f}% "
              f"conserved across {n_total} isotypes; unique residues seen: {unique_aas}")
        if variants:
            print(f"    Variants:")
            for g, aa in variants:
                print(f"      {g}: {aa}")
        conservation_summary[pos] = {
            "expected": expected,
            "role": role,
            "n_isotypes": n_total,
            "n_matching": n_matching,
            "conservation_pct": conservation_pct,
            "unique_aas": unique_aas,
            "variants": [{"isotype": g, "residue": aa} for (g, aa) in variants],
            "all_residues": [{"isotype": g, "residue": aa} for (g, aa) in per_position[pos]],
        }

    # Overall verdict
    print()
    mean_conservation = sum(c["conservation_pct"] for c in conservation_summary.values()) / len(conservation_summary)
    print(f"  Mean conservation across H-CCN top-5: {mean_conservation:.1f}%")
    if mean_conservation > 90:
        verdict = ("H-CCN top-5 are nearly universally conserved across beta-tubulin "
                   "isotypes including non-mammalian (yeast, Arabidopsis). Strong "
                   "evolutionary functional importance.")
    elif mean_conservation > 70:
        verdict = ("H-CCN top-5 are mostly conserved with some variation in specific "
                   "isotypes. Functional importance + tunable mechanism.")
    else:
        verdict = ("H-CCN top-5 show substantial isotype variation; the predicted "
                   "sites are not all evolutionarily essential. Honest finding: "
                   "site-specific function is isotype-dependent.")
    print(f"  Interpretation: {verdict}")

    # Save results
    with open(OUTPUT_DIR / "T22_isotype_conservation.json", "w") as f:
        json.dump({
            "isotypes_fetched": list(sequences.keys()),
            "numbering_offset": offset,
            "per_position": conservation_summary,
            "mean_conservation_pct": mean_conservation,
            "interpretation": verdict,
        }, f, indent=2)
    print()
    print(f"  saved T22_isotype_conservation.json")

    # Write markdown summary
    md = ["# T22 β-tubulin isotype variation at H-CCN top-5\n"]
    md.append("Fetched from UniProt REST API. Position numbers match the "
              "4O4H crystal structure numbering.\n")
    md.append("\n## Isotype-by-position table\n")
    md.append(f"| Isotype | Description | " +
              " | ".join(f"Pos {p}" for (_, p, _) in TOP_5_POSITIONS) + " |")
    md.append("|---|---|" + "|".join(["---"] * 5) + "|")
    for gene in sequences:
        seq = sequences[gene]["sequence"]
        desc = sequences[gene]["description"]
        gene_offset = isotype_offsets.get(gene)
        if gene_offset is None:
            row = [gene, desc] + ["?"] * 5
        else:
            row = [gene, desc]
            for (expected, pos, _) in TOP_5_POSITIONS:
                idx = pos - 1 + gene_offset
                if 0 <= idx < len(seq):
                    aa = seq[idx]
                    mark = "**" + aa + "**" if aa != expected else aa
                    row.append(mark)
                else:
                    row.append("-")
        md.append("| " + " | ".join(row) + " |")
    md.append("\n*Bold = variation from the 4O4H reference residue.*\n")
    md.append("\n## Conservation per position\n")
    for (expected, pos, role) in TOP_5_POSITIONS:
        c = conservation_summary[pos]
        md.append(f"\n### Pos {pos} ({expected}) — {role}\n")
        md.append(f"- Conservation: **{c['conservation_pct']:.0f}%** "
                  f"({c['n_matching']}/{c['n_isotypes']} isotypes)")
        md.append(f"- Residues seen: {c['unique_aas']}")
        if c["variants"]:
            md.append(f"- **Variants:**")
            for v in c["variants"]:
                md.append(f"  - {v['isotype']}: {v['residue']}")
        else:
            md.append(f"- **No variants** — universally conserved")
    md.append(f"\n## Interpretation\n\n{verdict}\n")
    with open(OUTPUT_DIR / "T22_isotype_alignment.md", "w") as f:
        f.write("\n".join(md))
    print(f"  saved T22_isotype_alignment.md")

    return 0


if __name__ == "__main__":
    sys.exit(main())
