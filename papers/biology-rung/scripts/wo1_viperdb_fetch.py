"""WO-BIOLOGY-RUNG-001-CAPSID: VIPERdb observed-T-number fetcher.

This script obtains a table of observed icosahedral viral capsid
T-numbers for empirical comparison against the prediction emitted by
`wo1_capsid_predict.py`. Output: `data/wo1_viperdb_observed.csv`
with columns:

    id, species_or_genome, T, chirality, source_ref, notes

Data acquisition has TWO MODES:

--------------------------------------------------------------------
Mode 1: `--fetch` — query the VIPERdb public API
--------------------------------------------------------------------

VIPERdb (https://viperdb.org) is the canonical database of
icosahedral virus capsid structures. It tags each entry with a
triangulation number and chirality where applicable.

We do not hard-code a single endpoint because the VIPERdb API has
evolved across versions (v1 → v2 → v3). Instead, the fetcher tries
a short list of candidate endpoints in order and uses the first one
that returns a parseable response. If none responds, it exits with
a clear error pointing the user at:

    https://viperdb.org

where the current URL structure can be found and the endpoint list
below updated.

Candidate endpoints (tried in order):

    1.  https://viperdb.org/api/v1/virusList/
    2.  https://viperdb.org/api/virusList/
    3.  https://viperdb.org/api_v1/family_list
    4.  https://viperdb.org/api/capsid

Nothing is fabricated. If the endpoint fails, you get an empty
output and an explicit error — not a plausible-looking fake table.

--------------------------------------------------------------------
Mode 2: `--from-literature <path>` — load a curated literature CSV
--------------------------------------------------------------------

Use this when offline, or when VIPERdb endpoints are down. Expected
format for the literature CSV:

    id,species_or_genome,T,chirality,source_ref,notes
    1stm,Satellite tobacco necrosis,1,achiral,"Liljas et al. 1982 J Mol Biol 159 1","T=1 capsid"
    1ccv,Cowpea chlorotic mottle,3,achiral,"Speir et al. 1995 Structure 3 63",""
    ...

The source_ref field MUST point to a primary publication or the
VIPERdb entry id. Entries without a source are not accepted.

This template file lives at
`data/wo1_viperdb_observed_template.csv` and is created on first
run if not present. It is EMPTY by default — to be populated by
either the maintainer or the `--fetch` mode.

Usage:

    python wo1_viperdb_fetch.py --fetch              # API mode
    python wo1_viperdb_fetch.py --from-literature <path>
    python wo1_viperdb_fetch.py --init-template       # create template
"""

from __future__ import annotations

import argparse
import csv
import json
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent / "data"
OUT_PATH = DATA_DIR / "wo1_viperdb_observed.csv"
TEMPLATE_PATH = DATA_DIR / "wo1_viperdb_observed_template.csv"

COLUMNS = ["id", "species_or_genome", "T", "chirality", "source_ref", "notes"]

CANDIDATE_ENDPOINTS = [
    "https://viperdb.org/api/v1/virusList/",
    "https://viperdb.org/api/virusList/",
    "https://viperdb.org/api_v1/family_list",
    "https://viperdb.org/api/capsid",
]


def init_template() -> None:
    """Create an empty literature-mode CSV template."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if TEMPLATE_PATH.exists():
        print(f"Template already exists: {TEMPLATE_PATH}")
        return
    with TEMPLATE_PATH.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(COLUMNS)
        # One illustrative comment row, immediately followed by no data.
        # Users are to fill in rows from primary publications.
        writer.writerow([
            "# PDB_id",
            "# species (italics not needed)",
            "# integer Loeschian T-number",
            "# 'laevo' | 'dextro' | 'achiral'",
            "# primary publication citation",
            "# free-text",
        ])
    print(f"Template created (empty): {TEMPLATE_PATH}")
    print("Populate from primary publications or VIPERdb export, then:")
    print(f"  python wo1_viperdb_fetch.py --from-literature {TEMPLATE_PATH}")


def try_fetch(insecure: bool = False) -> list[dict[str, Any]]:
    """Try each candidate VIPERdb endpoint, return parsed entries if any work.

    If `insecure=True`, disables SSL certificate verification. This is a
    pragmatic development convenience for sandboxed environments with broken
    CA bundles; the data we fetch is public capsid metadata, so the security
    impact is low — but the default is secure.
    """
    last_error: Exception | None = None
    ctx: ssl.SSLContext | None = None
    if insecure:
        print("WARNING: SSL certificate verification DISABLED (--insecure).")
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

    for url in CANDIDATE_ENDPOINTS:
        try:
            print(f"Trying: {url}")
            req = urllib.request.Request(
                url,
                headers={"Accept": "application/json", "User-Agent": "vfd-wo1-fetch/1.0"},
            )
            with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
                raw = resp.read().decode("utf-8", errors="replace")
                data = json.loads(raw)
                print(f"  OK ({len(raw)} bytes)")
                return _normalise_viperdb_response(data)
        except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, TimeoutError) as e:
            last_error = e
            print(f"  failed: {type(e).__name__}: {e}")
            continue

    raise RuntimeError(
        "No VIPERdb endpoint returned a parseable response. Tried:\n"
        + "\n".join(f"  - {u}" for u in CANDIDATE_ENDPOINTS)
        + f"\nLast error: {last_error!r}\n"
        "Update CANDIDATE_ENDPOINTS in this script after checking https://viperdb.org "
        "for the current API URL, or use --from-literature with a curated CSV."
    )


def _normalise_viperdb_response(data: Any) -> list[dict[str, Any]]:
    """Normalise an arbitrary VIPERdb API response into rows for our CSV.

    Because the API schema may vary, this function is defensive: it looks
    for keys like 'T', 'triangulation_number', 't_number' on each entry,
    and fails LOUDLY if it can't find a T-number. No silent placeholders.
    """
    rows: list[dict[str, Any]] = []

    if isinstance(data, dict) and "entries" in data:
        entries = data["entries"]
    elif isinstance(data, dict) and "results" in data:
        entries = data["results"]
    elif isinstance(data, list):
        entries = data
    else:
        raise RuntimeError(
            f"Unrecognised VIPERdb response shape: top-level keys = "
            f"{list(data.keys()) if isinstance(data, dict) else type(data).__name__}"
        )

    for entry in entries:
        T = None
        for key in ("T", "triangulation_number", "t_number", "tnumber"):
            if key in entry and entry[key] is not None:
                T = entry[key]
                break
        if T is None:
            continue  # skip entries without a declared T; do not invent one

        try:
            T_int = int(T)
        except (TypeError, ValueError):
            continue  # skip unparseable

        row = {
            "id": entry.get("id", entry.get("pdb_id", "")),
            "species_or_genome": entry.get("virus_name", entry.get("species", "")),
            "T": T_int,
            "chirality": entry.get("chirality", entry.get("hand", "unknown")),
            "source_ref": entry.get("citation", "VIPERdb fetch"),
            "notes": "",
        }
        rows.append(row)

    if not rows:
        raise RuntimeError(
            "Response parsed but zero entries had a T-number field under any "
            "of: T, triangulation_number, t_number, tnumber. Schema check "
            "failed — either the endpoint changed, or the response was an "
            "index/metadata page without entry records."
        )

    return rows


def load_literature(path: Path) -> list[dict[str, Any]]:
    """Load a curated literature CSV. Reject rows without source_ref."""
    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist. Create via --init-template.")

    rows: list[dict[str, Any]] = []
    with path.open("r", newline="") as f:
        reader = csv.DictReader(f)
        for i, raw in enumerate(reader, start=2):
            # Skip comment rows (first column starts with '#')
            first = next(iter(raw.values()), "") or ""
            if first.startswith("#"):
                continue
            if not raw.get("source_ref", "").strip():
                raise ValueError(
                    f"Line {i}: source_ref is empty. Every capsid must cite a "
                    f"primary publication or VIPERdb entry id. No made-up data."
                )
            try:
                T = int(raw["T"])
            except (KeyError, ValueError) as e:
                raise ValueError(f"Line {i}: invalid T-number: {e}") from e
            rows.append({
                "id": raw.get("id", "").strip(),
                "species_or_genome": raw.get("species_or_genome", "").strip(),
                "T": T,
                "chirality": raw.get("chirality", "unknown").strip(),
                "source_ref": raw.get("source_ref", "").strip(),
                "notes": raw.get("notes", "").strip(),
            })
    return rows


def write_observed(rows: list[dict[str, Any]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    ap = argparse.ArgumentParser()
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--fetch", action="store_true",
                       help="Query the VIPERdb public API.")
    group.add_argument("--from-literature", type=Path,
                       help="Load from a curated literature CSV.")
    group.add_argument("--init-template", action="store_true",
                       help="Create an empty literature-mode CSV template.")
    ap.add_argument("--out", type=Path, default=OUT_PATH,
                    help=f"Output CSV path (default {OUT_PATH})")
    ap.add_argument("--insecure", action="store_true",
                    help="Disable SSL cert verification for --fetch. "
                         "Use only in dev environments with broken CA bundles.")
    args = ap.parse_args()

    if args.init_template:
        init_template()
        return 0

    if args.fetch:
        try:
            rows = try_fetch(insecure=args.insecure)
        except RuntimeError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 2
    else:
        rows = load_literature(args.from_literature)

    write_observed(rows, args.out)
    print(f"Wrote {len(rows)} observed-T rows to: {args.out}")

    # Quick histogram summary
    from collections import Counter
    counts = Counter(r["T"] for r in rows)
    print()
    print("Observed T-number histogram:")
    for T in sorted(counts):
        print(f"  T={T:3d}  count={counts[T]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
