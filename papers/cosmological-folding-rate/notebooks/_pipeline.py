"""Shared helpers for the four notebook scripts."""
from __future__ import annotations

import csv
import os
import sys
from typing import Dict, Iterable, List

import numpy as np

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from src.fitting import FitResult  # noqa: E402
from src.statistics import metrics_row  # noqa: E402

RESULTS_DIR = os.path.join(HERE, "results")
FIG_DIR = os.path.join(RESULTS_DIR, "figures")
TABLE_DIR = os.path.join(RESULTS_DIR, "tables")
DATA_PROC_DIR = os.path.join(HERE, "data", "processed")

for _d in (FIG_DIR, TABLE_DIR, DATA_PROC_DIR):
    os.makedirs(_d, exist_ok=True)


def write_csv(path: str, rows: Iterable[Dict[str, float]]) -> None:
    rows = list(rows)
    if not rows:
        return
    keys: List[str] = []
    for r in rows:
        for k in r.keys():
            if k not in keys:
                keys.append(k)
    with open(path, "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=keys)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


def fit_to_metrics(fit: FitResult) -> Dict[str, float]:
    row = metrics_row(fit.name, chi2=fit.chi2, n_params=fit.n_params, n_data=fit.n_data)
    row.update(fit.params)
    return row


def stamp(msg: str) -> None:
    print(f"[{os.path.basename(sys.argv[0])}] {msg}")
