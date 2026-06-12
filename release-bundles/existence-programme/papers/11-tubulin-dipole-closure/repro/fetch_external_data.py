#!/usr/bin/env python3
"""
Note G --- external-data fetcher.

Downloads tubulin and tubulin-ligand structural data into
external_data/pdb/ and external_data/emdb/. Idempotent; skips
existing files. Mirrors the WO-1 capsid VIPERdb-fetch pattern.

Usage:
    python fetch_external_data.py            # fetch all
    python fetch_external_data.py --pdb      # PDB only
    python fetch_external_data.py --emdb     # EMDB only
    python fetch_external_data.py --dry-run  # report URLs without downloading

The script only uses urllib (no extra dependencies). External data
is gitignored (see ../external_data/README.md).
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

EXTERNAL_DATA = (Path(__file__).resolve().parent.parent / "external_data").resolve()
PDB_DIR = EXTERNAL_DATA / "pdb"
EMDB_DIR = EXTERNAL_DATA / "emdb"

# ---------------------------------------------------------------
# Curated structure list
# ---------------------------------------------------------------

# (pdb_id, description, ligand_class, notes)
PDB_TARGETS = [
    ("1JFF", "alpha-beta tubulin dimer + taxol (electron crystallography)", "taxol", "Nogales 1998; canonical tubulin structure"),
    ("4O4H", "alpha-beta tubulin dimer high-resolution", "apo", "Prota 2014; high-res reference geometry"),
    ("5SYC", "tubulin + paclitaxel co-crystal", "paclitaxel", "Taxane binding pocket structure"),
    ("5SYE", "tubulin + epothilone co-crystal", "epothilone", "Alternative MT-stabiliser pocket"),
    ("6E7B", "tubulin + colchicine site complex", "colchicine", "Different binding pocket; comparator"),
    ("3J6F", "13-protofilament microtubule cryo-EM model", "lattice", "Lattice-level model; 13-pf B-lattice"),
    ("6DPV", "microtubule + kinesin lattice cryo-EM", "lattice", "Functional MT with motor-protein contact"),
    # Cross-target: GLIC bacterial homologue with bound volatile anaesthetic
    ("3P50", "GLIC + propofol co-crystal", "propofol", "Cross-target T27: GLIC anaesthetic-bound structure"),
    ("4HFI", "GLIC + desflurane co-crystal", "desflurane", "Cross-target T27: GLIC volatile-anaesthetic-bound structure"),
]

# Microtubule cryo-EM maps (EMDB IDs)
EMDB_TARGETS = [
    ("EMD-13770", "13-protofilament MT cryo-EM map", "Manka & Moores 2018-era 13-pf reference"),
    ("EMD-22388", "MT + tubulin-binding agent map", "Steinmetz lab MT-drug complex"),
]

PDB_FETCH_URL = "https://files.rcsb.org/download/{pdb_id}.cif"
EMDB_FETCH_URL = "https://files.wwpdb.org/pub/emdb/structures/{emdb_id}/map/{lower_id}.map.gz"
USER_AGENT = "vfd-existence-life-closure-programme/1.0.0-rc1 (research; contact@vibrationalfielddynamics.org)"
TIMEOUT_SECONDS = 60


# ---------------------------------------------------------------
# Fetcher
# ---------------------------------------------------------------

def fetch_url(url: str, dest: Path, dry_run: bool = False) -> dict:
    """Fetch url to dest. Skip if dest exists and is nonempty."""
    if dest.exists() and dest.stat().st_size > 0:
        return {"status": "exists", "url": url, "dest": str(dest)}
    if dry_run:
        return {"status": "dry-run", "url": url, "dest": str(dest)}
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            data = resp.read()
        dest.write_bytes(data)
        return {"status": "fetched", "url": url, "dest": str(dest), "bytes": len(data)}
    except urllib.error.HTTPError as e:
        return {"status": f"http_error_{e.code}", "url": url, "dest": str(dest)}
    except (urllib.error.URLError, TimeoutError) as e:
        return {"status": f"network_error", "url": url, "dest": str(dest), "error": str(e)}


def fetch_pdb(dry_run: bool) -> list:
    PDB_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    for pdb_id, desc, lig, notes in PDB_TARGETS:
        url = PDB_FETCH_URL.format(pdb_id=pdb_id.lower())
        dest = PDB_DIR / f"{pdb_id}.cif"
        outcome = fetch_url(url, dest, dry_run=dry_run)
        outcome.update({"pdb_id": pdb_id, "description": desc, "ligand": lig, "notes": notes})
        results.append(outcome)
        print(f"  [{outcome['status']:>14}] {pdb_id}  {desc}")
        if outcome["status"] == "fetched":
            time.sleep(0.5)  # be polite to RCSB
    return results


def fetch_emdb(dry_run: bool) -> list:
    EMDB_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    for emdb_id, desc, notes in EMDB_TARGETS:
        # EMDB ID format: "EMD-13770" -> URL uses "EMD-13770" subdir, file "emd_13770.map.gz"
        numeric = emdb_id.split("-")[1]
        url = f"https://files.wwpdb.org/pub/emdb/structures/{emdb_id}/map/emd_{numeric}.map.gz"
        dest = EMDB_DIR / f"emd_{numeric}.map.gz"
        outcome = fetch_url(url, dest, dry_run=dry_run)
        outcome.update({"emdb_id": emdb_id, "description": desc, "notes": notes})
        results.append(outcome)
        print(f"  [{outcome['status']:>14}] {emdb_id}  {desc}")
        if outcome["status"] == "fetched":
            time.sleep(0.5)
    return results


# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch Note G external data")
    parser.add_argument("--pdb", action="store_true", help="Fetch PDB structures only")
    parser.add_argument("--emdb", action="store_true", help="Fetch EMDB maps only")
    parser.add_argument("--dry-run", action="store_true", help="Report URLs without downloading")
    args = parser.parse_args()
    do_all = not (args.pdb or args.emdb)
    print("=" * 70)
    print("Note G external-data fetch")
    print(f"  external_data: {EXTERNAL_DATA}")
    if args.dry_run:
        print("  DRY RUN -- no files written")
    print("=" * 70)
    print()

    summary = {"pdb": [], "emdb": []}

    if do_all or args.pdb:
        print("PDB structures (RCSB):")
        summary["pdb"] = fetch_pdb(dry_run=args.dry_run)
        print()

    if do_all or args.emdb:
        print("EMDB maps:")
        summary["emdb"] = fetch_emdb(dry_run=args.dry_run)
        print()

    # Save manifest
    manifest_path = EXTERNAL_DATA / "fetch_manifest.json"
    manifest_path.write_text(json.dumps(summary, indent=2))
    print(f"Wrote manifest: {manifest_path}")

    # Report network errors as warnings (don't fail; the structural sim
    # is independent of the fetched files, which are illustrative).
    net_errors = [r for kind in ("pdb", "emdb") for r in summary[kind]
                  if r["status"].startswith("network_error") or r["status"].startswith("http_error")]
    if net_errors:
        print()
        print(f"WARN: {len(net_errors)} download(s) failed; structural sim still runs without them.")
        for r in net_errors:
            print(f"  {r.get('pdb_id', r.get('emdb_id'))}: {r['status']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
