"""Phase 8 acceptance: the no-fit guard passes and emits NO_FIT_GUARD_PASS.

Also a positive control: planting a forbidden token in scanned source would be
detected (checked here against a synthetic string, not by editing real files).
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "route_b"))
import no_fit_guard as nfg


def test_guard_passes():
    g = nfg.run_guard()
    assert g["status"] == "PASS", g["findings"]
    assert g["message"] == "NO_FIT_GUARD_PASS"


def test_geometry_path_does_not_import_target():
    # the construction path must not import the point-count target module
    for fname in nfg.GEOMETRY_PATH:
        path = os.path.join(nfg.HERE, fname)
        code = nfg._strip_comments_and_docstrings(open(path).read())
        assert "point_count_target" not in code, fname
        assert "import point_count" not in code, fname


def test_positive_control_detects_fitting():
    # the forbidden-pattern list actually catches fitting tokens
    sample = "coeff = numpy.polyfit(x, target_a_p, 1)"
    hit_fit = any(re.search(p, sample, re.IGNORECASE)
                  for p in nfg.FORBIDDEN_FITTING)
    hit_tgt = any(re.search(p, sample, re.IGNORECASE)
                  for p in nfg.FORBIDDEN_TARGET)
    assert hit_fit and hit_tgt


def run():
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("  ok:", name)
    print("NO_FIT_GUARD_PASS")


if __name__ == "__main__":
    run()
