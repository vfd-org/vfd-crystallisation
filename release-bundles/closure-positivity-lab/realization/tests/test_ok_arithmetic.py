"""Phase 2 acceptance: O_K = Z[phi] arithmetic."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "route_b"))
import ok_arithmetic as ok


def test_phi_relation():
    assert ok.mul(ok.PHI, ok.PHI) == (1, 1)          # phi^2 = 1 + phi


def test_norm_trace_conj():
    assert ok.norm(ok.PHI) == -1
    assert ok.trace(ok.PHI) == 1
    assert ok.conj(ok.PHI) == (1, -1)                # 1 - phi
    # norm is multiplicative
    x, y = (2, 3), (-1, 4)
    assert ok.norm(ok.mul(x, y)) == ok.norm(x) * ok.norm(y)


def test_level_norm():
    assert ok.LEVEL == (-2, 5)                       # 5 phi - 2
    assert abs(ok.norm(ok.LEVEL)) == 31


def test_divisibility():
    x = ok.mul((3, 1), (2, -1))                      # exactly divisible
    assert ok.divides((3, 1), x)
    assert ok.quotient((3, 1), x) == (2, -1)
    assert not ok.divides((3, 1), (1, 0))


def test_totally_positive():
    assert ok.is_totally_positive((3, 1))            # 3 + phi
    assert not ok.is_totally_positive(ok.LEVEL)      # 5 phi - 2 (mixed signs)


def run():
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("  ok:", name)
    print("ALL OK_ARITHMETIC TESTS PASS")


if __name__ == "__main__":
    run()
