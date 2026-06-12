"""WO-007 Schläfli-decomposition runner.

Runs every certificate for the decomposition of V_600 = 2I into five
right cosets of V_24 = 2T, and writes the frozen output artifacts
under the docs outputs directory.

Run:
    python closure_transform_engine/examples/run_wo007_schlafli_decomposition.py
"""
from __future__ import annotations

import csv
import datetime
import json
import os
import platform
import subprocess
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve()
_REPO = _HERE.parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from closure_transform_engine.decomposition import run_decomposition


def _resolve_out_dir() -> Path:
    """Locate the docs outputs directory in either repo layout.

    Main VFD research repo: docs/schlafli_24_600/outputs/.
    Standalone reproduction bundle: docs/outputs/.
    """
    candidates = [
        _REPO / "docs" / "schlafli_24_600" / "outputs",
        _REPO / "docs" / "outputs",
    ]
    for c in candidates:
        if c.parent.exists():
            return c
    return candidates[0]


OUT_DIR = _resolve_out_dir()


def emit(line: str, log_lines):
    print(line)
    log_lines.append(line)


def _versions() -> dict:
    versions = {"python": sys.version.split()[0]}
    for pkg in ("numpy", "sympy"):
        try:
            mod = __import__(pkg)
            versions[pkg] = getattr(mod, "__version__", "unknown")
        except Exception:
            versions[pkg] = "(not installed)"
    return versions


def main(argv=None) -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    log_lines = []

    t0 = time.time()
    emit("=== WO-007 Schläfli decomposition of the 600-cell ===", log_lines)
    emit("", log_lines)
    emit("Constructing V_600 = 2I (exact Q(sqrt 5) icosian quaternions)...", log_lines)
    emit("Identifying sigma-fixed V_24 = 2T...", log_lines)
    emit("Computing five right cosets of V_24...", log_lines)
    emit("Verifying each coset carries the 24-cell distance structure...", log_lines)
    emit("Enumerating the induced 2I action on five cosets and descent to A_5...", log_lines)
    emit("", log_lines)

    result = run_decomposition()

    emit("Certificates:", log_lines)
    emit(f"  V_600 construction (Section 2):     "
         f"{'PASS' if result.v600_construction.get('passed') else 'FAIL'}", log_lines)
    emit(f"  V_24 subgroup       (Section 3):     "
         f"{'PASS' if result.v24_subgroup.get('passed') else 'FAIL'}", log_lines)
    emit(f"  Five right cosets   (Section 4):     "
         f"{'PASS' if result.right_cosets_certificate.get('passed') else 'FAIL'}", log_lines)
    emit(f"  24-cell structure   (Section 5):     "
         f"{'PASS' if result.each_coset_is_24cell.get('passed') else 'FAIL'}", log_lines)
    emit(f"  A_5 coset action    (Section 6):     "
         f"{'PASS' if result.a5_action.get('passed') else 'FAIL'}", log_lines)
    emit("", log_lines)
    emit(f"Coset sizes: {result.coset_sizes}", log_lines)
    if result.a5_action.get("passed"):
        emit(f"A_5 conjugacy-class sizes: {result.a5_action['class_sizes']}", log_lines)
    emit("", log_lines)
    emit(f"Verdict:  {result.verdict}", log_lines)
    emit("", log_lines)

    # --- summary JSON ---
    summary_path = OUT_DIR / "wo007_summary.json"
    summary = result.to_dict()
    with summary_path.open("w") as f:
        json.dump(summary, f, indent=2, default=str)
    emit(f"Wrote: {summary_path.relative_to(_REPO)}", log_lines)

    # --- cosets JSON ---
    cosets_path = OUT_DIR / "wo007_cosets.json"
    with cosets_path.open("w") as f:
        json.dump({f"C_{i}": coset for i, coset in enumerate(result.cosets)},
                  f, indent=2)
    emit(f"Wrote: {cosets_path.relative_to(_REPO)}", log_lines)

    # --- coset action table CSV ---
    csv_path = OUT_DIR / "wo007_coset_action_table.csv"
    with csv_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "h_index", "coset_permutation", "cycle_structure",
            "is_identity", "is_even",
        ])
        for row in result.coset_action_table:
            w.writerow([
                row["h_index"],
                "->".join(str(x) for x in row["coset_permutation"]),
                "+".join(str(x) for x in row["cycle_structure"]),
                row["is_identity"],
                row["is_even"],
            ])
    emit(f"Wrote: {csv_path.relative_to(_REPO)}", log_lines)

    # --- distance shells CSV ---
    shells_path = OUT_DIR / "wo007_distance_shells.csv"
    with shells_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["shell", "d2_rational", "d2_float",
                    "pair_count_directed", "edges_undirected"])
        for s in result.distance_shells:
            w.writerow([s["shell"], s["d2_rational"], f"{s['d2_float']:.6f}",
                        s["pair_count_directed"], s["edges_undirected"]])
    emit(f"Wrote: {shells_path.relative_to(_REPO)}", log_lines)

    # --- reproducibility log ---
    log_path = OUT_DIR / "wo007_reproducibility_log.txt"
    run_utc = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        commit_hash = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=str(_REPO),
            capture_output=True, text=True, timeout=5,
        ).stdout.strip() or "(no git repo / no commits)"
    except Exception:
        commit_hash = "(git unavailable)"
    try:
        dirty = subprocess.run(
            ["git", "status", "--porcelain"], cwd=str(_REPO),
            capture_output=True, text=True, timeout=5,
        ).stdout.strip()
    except Exception:
        dirty = ""
    dirty_flag = " (uncommitted changes present)" if dirty else ""

    with log_path.open("w") as f:
        f.write("# WO-007 Schläfli decomposition run log\n")
        f.write(f"# run_utc:   {run_utc}\n")
        f.write(f"# elapsed:   {time.time() - t0:.2f} s\n")
        f.write(f"# python:    {sys.version.splitlines()[0]}\n")
        vs = _versions()
        f.write(f"# numpy:     {vs.get('numpy')}\n")
        f.write(f"# sympy:     {vs.get('sympy')}\n")
        f.write(f"# platform:  {platform.platform()}\n")
        f.write(f"# repo:      {_REPO}\n")
        f.write(f"# commit:    {commit_hash}{dirty_flag}\n\n")
        f.write("# Certificate states:\n")
        for name, key in [
            ("V_600 construction",       "v600_construction"),
            ("V_24 = 2T subgroup",       "v24_subgroup"),
            ("Five right cosets",        "right_cosets_certificate"),
            ("Each coset is a 24-cell",  "each_coset_is_24cell"),
            ("A_5 coset action",         "a5_action"),
        ]:
            status = "PASS" if summary[key].get("passed") else "FAIL"
            f.write(f"#   {name:32s} {status}\n")
        f.write(f"#   verdict                          {result.verdict}\n\n")
        for line in log_lines:
            f.write(line + "\n")
    print(f"Wrote: {log_path.relative_to(_REPO)}")

    return 0 if result.verdict == "SCHLAEFLI_DECOMPOSITION_CERTIFIED" else 1


if __name__ == "__main__":
    sys.exit(main())
