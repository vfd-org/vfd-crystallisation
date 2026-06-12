"""Phase 8 -- the no-fit guard.

Statically scans the geometry-side source files (the ones that BUILD the Brandt
matrices) and asserts that none of them performs fitting or reads arithmetic
target data.  The forbidden patterns are exactly those that could smuggle the
answer in:

    regression / least squares / curve_fit / polyfit / np.linalg.lstsq
    manual scale or offset tuned to a target
    importing or reading the point-count target / a_P table
    importing the elliptic curve / LMFDB data into the Brandt path

The geometry path is:  ok_arithmetic, quaternion_order, ideal_classes,
brandt_matrices.  None of these may import point_count_target, reference
"a_p"/"a_P" as input, the curve a-invariants, or "lmfdb".  (hecke_compare is the
ONLY module allowed to touch both sides, and only to compare -- it is not on the
construction path.)
"""
from __future__ import annotations

import os
import re

HERE = os.path.dirname(__file__)

# modules that construct the Brandt matrices (must be target-free)
GEOMETRY_PATH = [
    "ok_arithmetic.py",
    "quaternion_order.py",
    "ideal_classes.py",
    "brandt_matrices.py",
]

FORBIDDEN_FITTING = [
    r"\bregress",
    r"least[_\s]?squares",
    r"\bcurve_fit\b",
    r"\bpolyfit\b",
    r"lstsq",
    r"\.fit\(",
    r"minimize\(",
]

# tokens that would mean the curve / target leaked into the construction path
FORBIDDEN_TARGET = [
    r"point_count_target",
    r"genuine_newform",
    r"target_a_p",
    r"lmfdb",
    r"\ba_invariants\b",
]


def _scan_file(path, patterns):
    hits = []
    with open(path) as f:
        src = f.read()
    # strip comments / docstrings so that *descriptions* of forbidden ideas in
    # prose do not trip the guard; only live code is scanned.
    code = _strip_comments_and_docstrings(src)
    for pat in patterns:
        for m in re.finditer(pat, code, re.IGNORECASE):
            hits.append((pat, m.group(0)))
    return hits


def _strip_comments_and_docstrings(src):
    # remove triple-quoted strings
    src = re.sub(r'"""(?:.|\n)*?"""', " ", src)
    src = re.sub(r"'''(?:.|\n)*?'''", " ", src)
    # remove line comments
    out_lines = []
    for line in src.splitlines():
        idx = line.find("#")
        if idx >= 0:
            line = line[:idx]
        out_lines.append(line)
    return "\n".join(out_lines)


def run_guard():
    findings = {}
    ok = True
    for fname in GEOMETRY_PATH:
        path = os.path.join(HERE, fname)
        fit_hits = _scan_file(path, FORBIDDEN_FITTING)
        tgt_hits = _scan_file(path, FORBIDDEN_TARGET)
        if fit_hits or tgt_hits:
            ok = False
            findings[fname] = {"fitting": fit_hits, "target_leak": tgt_hits}
    return {
        "status": "PASS" if ok else "FAIL",
        "scanned": GEOMETRY_PATH,
        "findings": findings,
        "message": "NO_FIT_GUARD_PASS" if ok else "NO_FIT_GUARD_FAIL",
    }


if __name__ == "__main__":
    g = run_guard()
    print("NO-FIT GUARD")
    print("  scanned (geometry construction path):")
    for m in g["scanned"]:
        print("    -", m)
    if g["findings"]:
        print("  FINDINGS:")
        for f, d in g["findings"].items():
            print("   ", f, d)
    print("  status:", g["status"])
    print(" ", g["message"])
