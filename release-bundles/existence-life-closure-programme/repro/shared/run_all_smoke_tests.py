#!/usr/bin/env python3
"""
Existence / Life / Closure Programme --- smoke-test runner.

Runs lightweight deterministic synthetic / structural demos at seed 42.
Real-data analyses (those requiring OpenNeuro downloads) are skipped
unless data paths are configured.

Exit codes:
    0 - all smoke tests passed.
    1 - one or more smoke tests failed.
    2 - required package missing.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def check_packages() -> bool:
    """Return True iff all required packages are importable."""
    required = ["numpy", "scipy", "matplotlib"]
    missing = []
    for pkg in required:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    if missing:
        print(f"  [FAIL] missing packages: {', '.join(missing)}")
        print(f"  install: pip install -r repro/shared/requirements.txt")
        return False
    print(f"  [OK]   all required packages present ({', '.join(required)})")
    return True


def print_environment() -> None:
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Repo root:      {REPO_ROOT}")


def run_demo(script_path: Path, label: str) -> bool:
    """Run a demo script as a subprocess; return True if exit 0."""
    if not script_path.exists():
        print(f"  [SKIP] {label}: script not found ({script_path.relative_to(REPO_ROOT)})")
        return True  # not a failure; skipped
    print(f"  ... running {label} ({script_path.relative_to(REPO_ROOT)})")
    # Force non-interactive matplotlib so demos do not block on plt.show()
    import os as _os
    env = _os.environ.copy()
    env["MPLBACKEND"] = "Agg"
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            cwd=script_path.parent,
            timeout=900,  # 15 minutes; WSL + OneDrive can be slow on chart generation
            env=env,
        )
    except subprocess.TimeoutExpired:
        print(f"  [FAIL] {label} timed out after 900s")
        return False
    if result.returncode == 0:
        print(f"  [OK]   {label} exit 0")
        return True
    else:
        print(f"  [FAIL] {label} exit {result.returncode}")
        # Show tail of stderr for diagnostics
        tail = result.stderr.strip().splitlines()[-8:]
        for line in tail:
            print(f"         {line}")
        return False


def main() -> int:
    quick = "--quick" in sys.argv
    print("=" * 70)
    print("Existence / Life / Closure Programme --- smoke tests")
    if quick:
        print("Mode: QUICK (structural-verification subset only; lightweight Note C audit)")
    else:
        print("Mode: FULL (all sim demos)")
    print("=" * 70)
    if not quick:
        print("Each subprocess can take 1-10 minutes (matplotlib chart generation")
        print("is the dominant cost; demos use numpy SVD + Hilbert + matplotlib).")
        print("On native Linux: typically ~3-5 min total.")
        print("On WSL + Windows-mounted filesystem (e.g., OneDrive): expect 10-25 min total.")
        print("For a fast structural check, use:  python run_all_smoke_tests.py --quick")
        print()
    print_environment()
    print()
    print("--- Package check ---")
    if not check_packages():
        return 2

    print()
    print("--- Deterministic synthetic / structural demos (seed 42) ---")

    if quick:
        # Quick mode: only the lightweight rung-tower demo + Note C audit
        demos = [
            ("papers/I-existence-as-closure/repro/rung_tower_demo.py",
             "Paper I C1 cascade rung tower (quick)"),
        ]
    else:
        demos = [
            # (relative path from repo root, label)
            ("papers/I-existence-as-closure/repro/closure_demo.py",
             "Paper I D1-D8 substrate facts"),
            ("papers/I-existence-as-closure/repro/rung_tower_demo.py",
             "Paper I C1 cascade rung tower"),
            ("papers/II-life-as-closure/repro/life_demo.py",
             "Paper II L1-L13 living-frame mechanics"),
            ("papers/III-processing-to-point-of-view/repro/bridges_demo.py",
             "Paper III B1-B3 consciousness bridges"),
        ]

    results = []
    for rel, label in demos:
        script = REPO_ROOT / rel
        results.append((label, run_demo(script, label)))

    print()
    print("--- Solution Lab synthetic demos (seed 42, no external data) ---")
    sl_demos = [
        ("notes/Note-A-bioelectric-closure/repro/synthetic_demo.py",
         "Note A synthetic regeneration"),
        ("notes/Note-C-closure-as-distance/repro/strict_vs_passleaning_audit.py",
         "Note C strict-vs-PASS-leaning audit"),
    ]
    for rel, label in sl_demos:
        script = REPO_ROOT / rel
        results.append((label, run_demo(script, label)))

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    passed = sum(1 for _, ok in results if ok)
    failed = sum(1 for _, ok in results if not ok)
    for label, ok in results:
        status = "OK  " if ok else "FAIL"
        print(f"  [{status}] {label}")
    print()
    print(f"  Passed: {passed}/{len(results)}")
    print(f"  Failed: {failed}/{len(results)}")
    print()
    if failed:
        print("Smoke tests FAILED. See diagnostics above.")
        return 1
    print("All smoke tests PASSED.")
    print()
    print("Real-data analyses require external data; see repro/shared/data_access.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
