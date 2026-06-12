# Repro outputs

This folder is for reproducibility outputs that are small enough to
commit alongside the repository (deterministic JSON result dumps, small
diagnostic plots). It is not for raw experimental data.

## Expected hashes

`../shared/expected_hashes.json` records SHA-256 hashes of:

- All committed PDFs (`papers/*/paper.pdf`, `notes/*/note.pdf`).
- Key source files (`papers/*/source/main.tex`, `notes/*/source/main.tex`).
- All deterministic sim scripts (`papers/*/repro/*.py`, `notes/*/repro/*.py`).
- Deterministic JSON result dumps from each demo (if committed).

A reviewer can verify by running:

```bash
python -c "
import json, hashlib
from pathlib import Path

with open('repro/shared/expected_hashes.json') as f:
    expected = json.load(f)

for rel_path, expected_hash in expected.items():
    p = Path(rel_path)
    if not p.exists():
        print(f'  [MISSING] {rel_path}')
        continue
    actual = hashlib.sha256(p.read_bytes()).hexdigest()
    if actual == expected_hash:
        print(f'  [OK]      {rel_path}')
    else:
        print(f'  [MISMATCH] {rel_path}')
        print(f'             expected: {expected_hash}')
        print(f'             actual:   {actual}')
"
```

## What is NOT committed

- External data (OpenNeuro datasets, BETSE simulation outputs, HCP data) — see `../shared/data_access.md`.
- Large per-subject CSVs from real-data analyses — generated locally when data is available.
- Figure PNGs > 1 MB unless they are load-bearing for a paper.

## What IS committed

- All deterministic synthetic-demo JSON outputs.
- Small per-paper result summaries.
- Programme-level audit results (e.g., `notes/Note-C-closure-as-distance/repro/output/strict_vs_passleaning_summary.json`).
