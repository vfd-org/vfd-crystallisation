"""Gate tests for the family claims: dimension sequence, level 41, level 61.

These rebuild the geometry from scratch (no cached data) and check the
paper's headline family claims. The full 44-ideal level-31 sweep lives in
route_b/level31_full_ideals.py (minutes); its committed artifact is
data/level31_per_ideal.json, spot-checked here.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "route_b"))

import brandt_level as bl                      # noqa: E402
import multilevel_dimensions as md             # noqa: E402
import second_form_level41 as l41              # noqa: E402
import genus2_form_level61 as l61              # noqa: E402


def test_dimension_sequence_all_levels():
    out = md.run()
    assert out["all_match"], out
    assert out["displayed_table_agreements"] == "7/7"


def test_level41_out_of_sample():
    out = l41.run()
    assert out["brandt_h"] == 2 and out["cuspidal_dim"] == 1
    assert out["n_norms_tested"] == 9
    assert out["all_match"], out["rows"]
    assert all(r["ramanujan"] for r in out["rows"])


def test_level61_genus2():
    out = l61.run()
    assert out["brandt_h"] == 3 and out["cuspidal_dim"] == 2
    assert out["all_rm_by_sqrt5"], out["rows"]
    assert out["all_ramanujan"]
    assert out["all_dembele_inert_match"]


def test_level31_per_ideal_artifact():
    path = os.path.join(HERE, "..", "data", "level31_per_ideal.json")
    d = json.load(open(path))
    assert d["all_match"] is True
    assert d["n_prime_ideals"] == 44
    assert all(r["match"] for r in d["rows"])
    assert d["engine_level_ideal"] == "sigma(5phi-2)"
    assert d["steinberg_at_engine_level_ideal"] == -1
    # every split ideal row is labeled and individually checked
    split_rows = [r for r in d["rows"] if r["kind"] == "split"]
    assert all(r["phi_mod_p"] is not None for r in split_rows)


def test_engine_p1_sizes():
    for p in (11, 31, 41):
        gate = bl.compute_orbits_p(p)
        assert len(gate["p1_points"]) == p + 1
