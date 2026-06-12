"""WO-007 Schläfli decomposition tests.

Each test exercises one observable claim of the foundation note
`schlafli_decomposition.tex`.  All claims are reproduced by the exact
ℚ(√5) certificates in `closure_transform_engine.decomposition`.
"""
from __future__ import annotations

import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]

# docs/schlafli_24_600/ (main repo) or docs/ (standalone bundle).
_DOCS_CANDIDATES = [REPO / "docs" / "schlafli_24_600", REPO / "docs"]
DOCS = next((d for d in _DOCS_CANDIDATES
             if (d / "schlafli_decomposition.md").exists()),
            _DOCS_CANDIDATES[0])
OUTPUTS = DOCS / "outputs"

if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from closure_transform_engine.decomposition import (  # noqa: E402
    run_decomposition,
    right_cosets,
    distance_shells_v600,
)

# Reuse vfd_v600 directly for low-level sanity checks
import os
for _cand in (REPO, REPO / "papers" / "v600-programme" / "lib"):
    if (_cand / "vfd_v600").is_dir() and str(_cand) not in sys.path:
        sys.path.insert(0, str(_cand))
        break

from vfd_v600.group import build_state  # type: ignore  # noqa: E402
from vfd_v600.sigma import sigma_fixed_set  # type: ignore  # noqa: E402
from vfd_v600.icosian import (  # type: ignore  # noqa: E402
    qq_norm_sq, qq_mul, qq_key, qq_conjugate,
)


@pytest.fixture(scope="module")
def state():
    return build_state()


@pytest.fixture(scope="module")
def result():
    return run_decomposition()


# --- 1-3. V_600 construction ------------------------------------------

def test_v600_has_120_vertices(state):
    assert state["n"] == 120
    assert len({qq_key(v) for v in state["verts"]}) == 120


def test_v600_vertices_are_unit_norm(state):
    for v in state["verts"]:
        assert qq_norm_sq(v) == (Fraction(1), Fraction(0))


def test_v600_closes_under_quaternion_multiplication(state):
    verts = state["verts"]
    idx_of = state["idx_of"]
    for u in verts:
        for v in verts:
            assert qq_key(qq_mul(u, v)) in idx_of


# --- 4-5. V_24 subgroup -----------------------------------------------

def test_sigma_fixed_subset_has_24_vertices(state):
    sf = sigma_fixed_set(state)
    assert len(sf) == 24


def test_sigma_fixed_subset_is_subgroup(state):
    verts = state["verts"]
    sf = sigma_fixed_set(state)
    sf_verts = [verts[i] for i in sf]
    sf_keys = {qq_key(v) for v in sf_verts}
    # closure
    for u in sf_verts:
        for v in sf_verts:
            assert qq_key(qq_mul(u, v)) in sf_keys
    # inverses (since unit norm, v^-1 = conj(v))
    for v in sf_verts:
        assert qq_key(qq_conjugate(v)) in sf_keys


# --- 6-10. Five right cosets ------------------------------------------

def test_right_cosets_count_is_5(state):
    cosets = right_cosets(state)
    assert len(cosets) == 5


def test_right_cosets_each_have_24_vertices(state):
    cosets = right_cosets(state)
    assert all(len(c) == 24 for c in cosets)


def test_right_cosets_are_disjoint(state):
    cosets = right_cosets(state)
    seen = set()
    for c in cosets:
        s = set(c)
        assert s.isdisjoint(seen)
        seen |= s


def test_right_cosets_cover_v600(state):
    cosets = right_cosets(state)
    union = set()
    for c in cosets:
        union |= set(c)
    assert union == set(range(state["n"]))


def test_each_vertex_belongs_to_exactly_one_coset(state):
    cosets = right_cosets(state)
    counts = {v: 0 for v in range(state["n"])}
    for c in cosets:
        for v in c:
            counts[v] += 1
    assert set(counts.values()) == {1}


# --- 11-14. 24-cell structure on each coset --------------------------

def test_each_coset_has_24_cell_distance_structure(result):
    pc = result.each_coset_is_24cell["per_coset"]
    for entry in pc:
        assert entry["passed"], entry
        assert entry["regular_degree"] == 8
        assert entry["edges"] == 96


def test_each_coset_shell_graph_is_8_regular(result):
    pc = result.each_coset_is_24cell["per_coset"]
    for entry in pc:
        assert entry["regular_degree"] == 8


def test_each_coset_shell_graph_has_96_edges(result):
    pc = result.each_coset_is_24cell["per_coset"]
    for entry in pc:
        assert entry["edges"] == 96


def test_no_intra_coset_pair_is_v600_edge(result):
    pc = result.each_coset_is_24cell["per_coset"]
    for entry in pc:
        assert entry["v600_edges_inside"] == 0


# --- 15-18. Coset action on five letters -----------------------------

def test_coset_action_has_60_distinct_permutations(result):
    assert result.a5_action["n_distinct_permutations"] == 60


def test_coset_action_kernel_is_plus_minus_one(result):
    assert result.a5_action["kernel_size"] == 2
    assert result.a5_action["kernel_is_plus_minus_one"] is True


def test_coset_action_image_is_A5(result):
    assert result.a5_action["image_is_A5"] is True
    assert result.a5_action["all_even"] is True
    assert result.a5_action["class_sizes"] == {
        "1A": 1, "2A": 15, "3A": 20, "5A": 12, "5B": 12,
    }


def test_coset_action_is_transitive(result):
    assert result.a5_action["transitive"] is True


# --- 19-20. Reproducibility artifacts --------------------------------

def test_reproducibility_artifacts_are_written():
    """The runner should have written all five output artifacts."""
    # If the runner hasn't been run yet in this layout, run it.
    if not (OUTPUTS / "wo007_summary.json").exists():
        script = REPO / "closure_transform_engine" / "examples" / "run_wo007_schlafli_decomposition.py"
        proc = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True, text=True, cwd=str(REPO),
        )
        assert proc.returncode == 0, proc.stderr
    for fname in (
        "wo007_summary.json", "wo007_cosets.json",
        "wo007_coset_action_table.csv", "wo007_distance_shells.csv",
        "wo007_reproducibility_log.txt",
    ):
        assert (OUTPUTS / fname).exists(), f"missing: {OUTPUTS / fname}"


def test_summary_json_matches_claims_in_note():
    p = OUTPUTS / "wo007_summary.json"
    if not p.exists():
        pytest.skip("summary.json missing — run the runner first")
    with p.open() as f:
        data = json.load(f)
    assert data["verdict"] == "SCHLAEFLI_DECOMPOSITION_CERTIFIED"
    assert data["n_vertices"] == 120
    assert data["coset_sizes"] == [24] * 5
    for key in ("v600_construction", "v24_subgroup",
                "right_cosets_certificate", "each_coset_is_24cell",
                "a5_action"):
        assert data[key]["passed"], f"{key} did not pass: {data[key]}"


# --- Extra: paper presence + no overclaim ---------------------------

def test_paper_tex_present():
    p = DOCS / "schlafli_decomposition.tex"
    assert p.exists(), f"missing: {p}"
    txt = p.read_text()
    assert "\\documentclass" in txt
    assert "24-cell" in txt and "600-cell" in txt


def test_paper_md_present():
    p = DOCS / "schlafli_decomposition.md"
    assert p.exists(), f"missing: {p}"
    txt = p.read_text().lower()
    # no overclaim
    for phrase in (
        "proves consciousness",
        "derives the standard model",
        "proves cosmology",
        "proves the universe is a hypersphere",
        "final theory",
        "impossible to refute",
        "undeniable proof",
    ):
        assert phrase not in txt, f"overclaim in md: {phrase}"


def test_runner_script_exits_zero():
    """Running the script end-to-end exits 0 and produces a positive verdict."""
    script = REPO / "closure_transform_engine" / "examples" / "run_wo007_schlafli_decomposition.py"
    proc = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True, text=True, cwd=str(REPO),
    )
    assert proc.returncode == 0, f"stderr:\n{proc.stderr}"
    assert "SCHLAEFLI_DECOMPOSITION_CERTIFIED" in proc.stdout
