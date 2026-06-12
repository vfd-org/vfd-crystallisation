#!/usr/bin/env python3
"""
Note G --- T23 / T25 / T26: lattice + thermal + composite signatures.

  T23  MT lattice contact analysis from 3J6F (13-pf cryo-EM lattice).
       For each beta-tubulin residue, count inter-chain heavy-atom
       contacts within 5 A. High contact count = sits at a
       protofilament-protofilament or longitudinal alpha-beta-alpha-beta
       interface. Tests the H-CCN propagation claim.

  T25  Crystallographic B-factor distribution from 4O4H.
       Per-residue mean B-factor of CA atoms. Validates the T20
       cross-PDB mobility result at atomic resolution within one
       structure.

  T26  Composite CCN-Plus index combining all signatures.
       Normalised mean across CCN (T8/T14) + radical-pair partners
       (T17) + dewetting (T19) + ring-orientation coherence (T21)
       + isotype conservation (T22) + lattice contact (T23)
       + B-factor inverse (T25).

Outputs:
  output/T23_lattice_contacts.json
  output/T23_lattice_contact_map.png
  output/T25_b_factor_distribution.json
  output/T25_b_factor_top5.png
  output/T26_composite_index.json
  output/T26_composite_index.png
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
PDB_DIR = REPO_ROOT / "external_data" / "pdb"
OUTPUT_DIR = REPO_ROOT / "repro" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(REPO_ROOT / "repro"))
from chemistry_context import parse_mmcif_with_hetatm, TOP_5  # type: ignore


# ============================================================
# T23: MT lattice contact analysis
# ============================================================

def parse_mmcif_with_bfactor(path):
    """Parser that includes B-factor (B_iso_or_equiv column)."""
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
        if kind != "ATOM":
            i += 1
            continue
        try:
            rec = {
                "comp": parts[col["label_comp_id"]],
                "label_chain": parts[col["label_asym_id"]],
                "auth_chain": parts[col["auth_asym_id"]],
                "resnum": int(parts[col["auth_seq_id"]]),
                "atom": parts[col["label_atom_id"]],
                "x": float(parts[col["Cartn_x"]]),
                "y": float(parts[col["Cartn_y"]]),
                "z": float(parts[col["Cartn_z"]]),
            }
            if "B_iso_or_equiv" in col:
                try:
                    rec["b_factor"] = float(parts[col["B_iso_or_equiv"]])
                except (ValueError, IndexError):
                    rec["b_factor"] = None
            atoms.append(rec)
        except (ValueError, KeyError):
            pass
        i += 1
    return atoms


def t23_lattice_contacts():
    """For each beta-tubulin residue, count inter-chain heavy-atom
       contacts in 3J6F. Returns dict resnum -> contact_count."""
    path = PDB_DIR / "3J6F.cif"
    if not path.exists():
        return None
    atoms = parse_mmcif_with_bfactor(path)
    # Group by chain
    chains = {}
    for a in atoms:
        chains.setdefault(a["auth_chain"], []).append(a)
    print(f"  3J6F: {len(chains)} chains, {len(atoms)} atoms total")
    # Pick a reference beta-tubulin chain. Heuristic: chain B usually
    # carries beta-tubulin in tubulin PDBs. Use chain D if B is missing.
    ref_chain = None
    for candidate in ["B", "D", "F", "H"]:
        if candidate in chains:
            n_res = len(set(a["resnum"] for a in chains[candidate]))
            if n_res > 300:  # full beta-tubulin
                ref_chain = candidate
                break
    if ref_chain is None:
        print(f"  [WARN] no chain with > 300 residues found")
        return None
    print(f"  Reference beta-tubulin chain: {ref_chain}")
    # Collect ref-chain residues with their atoms
    ref_atoms_by_resnum = {}
    for a in chains[ref_chain]:
        ref_atoms_by_resnum.setdefault(a["resnum"], []).append(a)
    # For each ref residue, count atoms in OTHER chains within 5 A
    cutoff = 5.0
    contact_counts = {}
    contact_partners = {}
    # Pre-build other-chain atom array
    other_atoms = []
    for ch, alist in chains.items():
        if ch == ref_chain:
            continue
        for a in alist:
            if a["atom"].startswith("H"):
                continue
            other_atoms.append((ch, a["resnum"], a["comp"],
                                np.array([a["x"], a["y"], a["z"]])))
    print(f"  Other-chain atoms (heavy only): {len(other_atoms)}")
    # For efficiency, only check CA-only of ref residues against a
    # bounding-box-filtered set of other atoms
    other_positions = np.array([oa[3] for oa in other_atoms])
    for resnum in sorted(ref_atoms_by_resnum.keys()):
        # Get all heavy atoms of this residue
        res_atoms = [a for a in ref_atoms_by_resnum[resnum]
                     if not a["atom"].startswith("H")]
        if not res_atoms:
            continue
        # For each atom, check distance to all other_atoms within cutoff
        contacts = set()
        partners = []
        for a in res_atoms:
            pos = np.array([a["x"], a["y"], a["z"]])
            dists = np.linalg.norm(other_positions - pos, axis=1)
            in_range = np.where(dists < cutoff)[0]
            for idx in in_range:
                ch, rn, comp, _ = other_atoms[idx]
                key = (ch, rn)
                if key not in contacts:
                    contacts.add(key)
                    partners.append({
                        "chain": ch,
                        "resnum": rn,
                        "residue": comp,
                        "distance": float(dists[idx]),
                    })
        contact_counts[resnum] = len(contacts)
        if len(partners) > 0:
            contact_partners[resnum] = sorted(partners,
                                              key=lambda p: p["distance"])[:5]
    return contact_counts, contact_partners, ref_chain


# ============================================================
# T25: B-factor distribution
# ============================================================

def t25_b_factors():
    """Extract CA B-factors per residue from 4O4H chain B."""
    path = PDB_DIR / "4O4H.cif"
    if not path.exists():
        return None
    atoms = parse_mmcif_with_bfactor(path)
    bfactors = {}
    for a in atoms:
        if a["auth_chain"] == "B" and a["atom"] == "CA":
            bfactors[a["resnum"]] = a.get("b_factor")
    return bfactors


# ============================================================
# T26: Composite CCN-Plus index
# ============================================================

def t26_composite(ccn_t8, ccn_t14, radical_partners, dewetting,
                  ring_orientation, isotype_conservation, lattice_contacts,
                  bfactors):
    """Combine all signatures into a composite index per top-5 residue."""
    # For each top-5 residue, gather the 7 signals and normalise to [0,1]
    sigs_per_residue = {}
    for (comp, rn, _) in TOP_5:
        key = f"{comp}{rn}"
        sigs = {}
        # T8 (original CCN ranking; top-5 are by definition rank 1-5 of 42)
        # All top-5 get high CCN by construction; use the normalised score
        if ccn_t8 and rn in ccn_t8:
            sigs["t8_ccn_original"] = float(ccn_t8[rn]["ccn_score"])
        # T14 refined CCN
        if ccn_t14 and rn in ccn_t14:
            sigs["t14_ccn_refined"] = float(ccn_t14[rn]["ccn_refined_score"])
        # T17 radical-pair partners count (Y185 should be highest)
        sigs["t17_rp_partners"] = float(radical_partners.get(key, 0))
        # T19 dewetting score
        match = [d for d in dewetting if d["residue"] == key]
        if match:
            sigs["t19_dewetting"] = float(match[0]["dewetting_score"])
        # T21 ring orientation (mean of |cos| with other top-5)
        related = [p for p in ring_orientation["pairwise_cosines"]
                   if key in p["pair"].split("--")]
        if related:
            sigs["t21_ring_coherence_mean"] = float(np.mean([p["cosine_abs"] for p in related]))
        # T22 isotype conservation
        if rn in isotype_conservation:
            sigs["t22_isotype_conservation_pct"] = float(isotype_conservation[rn]["conservation_pct"])
        # T23 lattice contact
        if lattice_contacts and rn in lattice_contacts:
            sigs["t23_lattice_contacts"] = float(lattice_contacts[rn])
        # T25 B-factor (LOWER = more rigid = stronger signal; invert)
        if bfactors and rn in bfactors and bfactors[rn] is not None:
            sigs["t25_b_factor"] = float(bfactors[rn])  # we'll invert at compose time
        sigs_per_residue[key] = sigs

    # Normalise each signal across the top-5
    sig_names = ["t8_ccn_original", "t14_ccn_refined", "t17_rp_partners",
                 "t19_dewetting", "t21_ring_coherence_mean",
                 "t22_isotype_conservation_pct", "t23_lattice_contacts",
                 "t25_b_factor"]
    normalised = {}
    for sname in sig_names:
        vals = [sigs_per_residue[k].get(sname) for k in sigs_per_residue
                if sigs_per_residue[k].get(sname) is not None]
        if not vals:
            continue
        vmin, vmax = min(vals), max(vals)
        for k in sigs_per_residue:
            v = sigs_per_residue[k].get(sname)
            if v is None:
                continue
            if vmax > vmin:
                norm_val = (v - vmin) / (vmax - vmin)
            else:
                norm_val = 0.5
            # B-factor: lower is better (more rigid -> stronger signal)
            if sname == "t25_b_factor":
                norm_val = 1.0 - norm_val
            normalised.setdefault(k, {})[sname] = norm_val

    # Compute composite as the mean over available normalised signals
    composite = {}
    for k, vals in normalised.items():
        present = [v for v in vals.values() if v is not None]
        composite[k] = {
            "n_signals_present": len(present),
            "composite_mean": float(np.mean(present)) if present else 0.0,
            "raw_signals": sigs_per_residue[k],
            "normalised_signals": vals,
        }
    return composite


# ============================================================
# Main
# ============================================================

def main():
    print("=" * 70)
    print("Note G T23/T25/T26 --- lattice + thermal + composite")
    print("=" * 70)
    print()

    # T23
    print("T23: MT lattice contact analysis (3J6F)")
    result = t23_lattice_contacts()
    if result is None:
        print("  [SKIP] no lattice data available")
        lattice_contacts_dict = {}
        contact_partners = {}
    else:
        lattice_contacts_dict, contact_partners, ref_chain = result
        print(f"  Residues with at least one inter-chain contact: "
              f"{sum(1 for c in lattice_contacts_dict.values() if c > 0)}")
        # Stats
        counts_arr = np.array(list(lattice_contacts_dict.values()))
        print(f"  Contact-count distribution: mean = {counts_arr.mean():.1f}, "
              f"max = {counts_arr.max()}, median = {np.median(counts_arr):.1f}")
        print()
        print(f"  H-CCN top-5 lattice contacts (in 3J6F):")
        print(f"  {'residue':>8}  {'contacts':>8}  {'percentile':>10}  "
              f"{'top partners (chain/res)':<40}")
        counts_sorted = sorted(counts_arr)
        for (comp, rn, _) in TOP_5:
            if rn in lattice_contacts_dict:
                c = lattice_contacts_dict[rn]
                pctile = float(np.searchsorted(counts_sorted, c)) / len(counts_sorted) * 100
                partners_str = ", ".join(
                    f"{p['chain']}/{p['resnum']}({p['distance']:.1f}A)"
                    for p in contact_partners.get(rn, [])[:3]
                )
                print(f"  {comp}{rn:<5}  {c:>8}  {pctile:>9.0f}%  {partners_str:<40}")
            else:
                print(f"  {comp}{rn:<5}  not resolved in 3J6F chain {ref_chain}")
        # Save
        with open(OUTPUT_DIR / "T23_lattice_contacts.json", "w") as f:
            json.dump({
                "ref_chain": ref_chain,
                "n_residues": len(lattice_contacts_dict),
                "contact_counts": {str(k): v for k, v in lattice_contacts_dict.items()},
                "top_5_lattice_contacts": [
                    {
                        "residue": f"{c}{rn}",
                        "contacts": lattice_contacts_dict.get(rn),
                        "percentile": float(np.searchsorted(counts_sorted,
                                                             lattice_contacts_dict.get(rn, 0)))
                                     / len(counts_sorted) * 100,
                        "top_partners": contact_partners.get(rn, [])[:5],
                    }
                    for (c, rn, _) in TOP_5 if rn in lattice_contacts_dict
                ],
            }, f, indent=2)
        # Figure
        fig, ax = plt.subplots(figsize=(10, 4))
        resnums = sorted(lattice_contacts_dict.keys())
        counts = [lattice_contacts_dict[r] for r in resnums]
        ax.bar(resnums, counts, color="#999999", width=1.0, edgecolor="none")
        # Highlight top-5
        for (comp, rn, _) in TOP_5:
            if rn in lattice_contacts_dict:
                ax.bar(rn, lattice_contacts_dict[rn], color="#cd3a3a",
                       width=2, edgecolor="black", linewidth=0.5)
                ax.annotate(f"{comp}{rn}", (rn, lattice_contacts_dict[rn]),
                            textcoords="offset points", xytext=(0, 4),
                            fontsize=7, ha="center")
        ax.set_xlabel("β-tubulin residue number (3J6F chain " + ref_chain + ")")
        ax.set_ylabel("inter-chain heavy-atom contacts within 5 Å")
        ax.set_title("T23 MT lattice contacts per β-tubulin residue (top-5 in red)")
        ax.grid(alpha=0.3, axis="y")
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "T23_lattice_contact_map.png", dpi=120)
        plt.close()
        print(f"  saved T23_lattice_contacts.json + T23_lattice_contact_map.png")
    print()

    # T25
    print("T25: Crystallographic B-factor distribution (4O4H)")
    bfactors = t25_b_factors()
    if bfactors is None or not any(b is not None for b in bfactors.values()):
        print("  [SKIP] no B-factors available")
        bfactors = {}
    else:
        valid = [(r, b) for r, b in bfactors.items() if b is not None]
        b_arr = np.array([b for (_, b) in valid])
        print(f"  Residues with B-factor data: {len(valid)}")
        print(f"  B-factor distribution: mean = {b_arr.mean():.1f}, "
              f"SD = {b_arr.std():.1f}, range = [{b_arr.min():.1f}, {b_arr.max():.1f}]")
        print()
        print(f"  H-CCN top-5 B-factors (4O4H chain B CA):")
        print(f"  {'residue':>8}  {'B-factor':>8}  {'percentile':>10}")
        b_sorted = sorted(b_arr)
        for (comp, rn, _) in TOP_5:
            b = bfactors.get(rn)
            if b is not None:
                pctile = float(np.searchsorted(b_sorted, b)) / len(b_sorted) * 100
                print(f"  {comp}{rn:<5}  {b:>8.1f}  {pctile:>9.0f}%")
        # Save
        with open(OUTPUT_DIR / "T25_b_factor_distribution.json", "w") as f:
            json.dump({
                "n_residues": len(valid),
                "mean_b_factor": float(b_arr.mean()),
                "sd_b_factor": float(b_arr.std()),
                "top_5_b_factors": [
                    {
                        "residue": f"{c}{rn}",
                        "b_factor": bfactors.get(rn),
                        "percentile": (float(np.searchsorted(b_sorted, bfactors.get(rn)))
                                       / len(b_sorted) * 100) if bfactors.get(rn) is not None else None,
                    }
                    for (c, rn, _) in TOP_5
                ],
            }, f, indent=2)
        # Figure
        fig, ax = plt.subplots(figsize=(10, 4))
        resnums = sorted(r for r in bfactors if bfactors[r] is not None)
        bs = [bfactors[r] for r in resnums]
        ax.bar(resnums, bs, color="#999999", width=1.0, edgecolor="none")
        for (comp, rn, _) in TOP_5:
            if bfactors.get(rn) is not None:
                ax.bar(rn, bfactors[rn], color="#cd3a3a", width=2,
                       edgecolor="black", linewidth=0.5)
                ax.annotate(f"{comp}{rn}", (rn, bfactors[rn]),
                            textcoords="offset points", xytext=(0, 4),
                            fontsize=7, ha="center")
        ax.set_xlabel("β-tubulin residue number")
        ax.set_ylabel(r"CA B-factor (Å$^2$)")
        ax.set_title("T25 4O4H CA B-factor distribution (top-5 in red)")
        ax.grid(alpha=0.3, axis="y")
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "T25_b_factor_top5.png", dpi=120)
        plt.close()
        print(f"  saved T25_b_factor_distribution.json + T25_b_factor_top5.png")
    print()

    # T26 composite
    print("T26: Composite CCN-Plus index")
    # Load all the saved outputs
    def load_json(name):
        p = OUTPUT_DIR / name
        if p.exists():
            with open(p) as f:
                return json.load(f)
        return None

    t8 = load_json("T8_ccn_scores.json")
    t14 = load_json("T14_ccn_refined_scores.json")
    t17 = load_json("T17_radical_pair_signature.json")
    t19 = load_json("T19_dewetting_signature.json")
    t21 = load_json("T21_ring_orientation.json")
    t22 = load_json("T22_isotype_conservation.json")

    # Extract dicts in the format the composite expects
    ccn_t8 = t8.get("scores_by_resnum", {}) if t8 else {}
    ccn_t8_int_keys = {int(k): v for k, v in ccn_t8.items()}
    ccn_t14 = {}
    if t14:
        for s in t14.get("top_10_refined", []):
            ccn_t14[s["resnum"]] = s
    # Radical-pair partners count from T17
    radical_partners = {}
    if t17:
        for p in t17.get("top5_radical_pair_partners", []):
            for r in (p["residue_a"], p["residue_b"]):
                radical_partners[r] = radical_partners.get(r, 0) + 1
    # Dewetting from T19
    dewetting = t19.get("per_residue_dewetting", []) if t19 else []
    # Ring orientation
    ring_orient = t21 if t21 else {"pairwise_cosines": []}
    # Isotype conservation
    iso_cons = {}
    if t22:
        for pos, info in t22.get("per_position", {}).items():
            iso_cons[int(pos)] = info

    composite = t26_composite(ccn_t8_int_keys, ccn_t14, radical_partners,
                               dewetting, ring_orient, iso_cons,
                               lattice_contacts_dict, bfactors)

    # Sort and print
    sorted_comp = sorted(composite.items(), key=lambda x: -x[1]["composite_mean"])
    print(f"  Composite ranking of H-CCN top-5 (mean across 8 signals):")
    print(f"  {'residue':>8}  {'composite':>9}  {'n_signals':>10}  "
          f"{'strongest signal':<30}")
    for k, info in sorted_comp:
        # Identify strongest signal (highest normalised value)
        strongest = max(info["normalised_signals"].items(), key=lambda x: x[1])
        print(f"  {k:<8}  {info['composite_mean']:>9.3f}  "
              f"{info['n_signals_present']:>10}  {strongest[0]} ({strongest[1]:.2f})")
    print()

    # Verdict
    if sorted_comp:
        winner = sorted_comp[0]
        runner_up = sorted_comp[1] if len(sorted_comp) > 1 else None
        gap = (winner[1]['composite_mean'] - runner_up[1]['composite_mean']) if runner_up else 0.0
        print(f"  Top composite: {winner[0]} at {winner[1]['composite_mean']:.3f}")
        if gap > 0.1:
            verdict_t26 = f"{winner[0]} dominates the composite ranking ({gap:.2f} gap to runner-up). Robust convergence."
        else:
            verdict_t26 = f"Top-2 composite scores are within {gap:.2f}. Multiple converging signatures, no single dominant residue."
        print(f"  Interpretation: {verdict_t26}")

    with open(OUTPUT_DIR / "T26_composite_index.json", "w") as f:
        json.dump({
            "ranking": [{"residue": k, **v} for k, v in sorted_comp],
            "verdict": verdict_t26 if sorted_comp else "no data",
        }, f, indent=2)
    # Figure: composite by signal
    fig, ax = plt.subplots(figsize=(10, 5))
    residues = [k for k, _ in sorted_comp]
    sig_names = list(sorted({s for k, v in composite.items()
                              for s in v.get("normalised_signals", {})}))
    n_sigs = len(sig_names)
    width = 0.8 / max(n_sigs, 1)
    for i, sname in enumerate(sig_names):
        vals = [composite[r]["normalised_signals"].get(sname, 0) for r in residues]
        ax.bar([x + i * width for x in range(len(residues))], vals,
               width=width, label=sname.replace("_", " "))
    ax.set_xticks([x + n_sigs * width / 2 for x in range(len(residues))])
    ax.set_xticklabels(residues, rotation=0)
    ax.set_ylabel("normalised signal strength (0-1)")
    ax.set_title("T26 composite CCN-Plus index: per-signal contributions")
    ax.legend(fontsize=7, ncol=2)
    ax.grid(alpha=0.3, axis="y")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "T26_composite_index.png", dpi=120)
    plt.close()
    print(f"  saved T26_composite_index.json + T26_composite_index.png")
    print()
    print("=" * 70)
    print("T23/T25/T26 complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
