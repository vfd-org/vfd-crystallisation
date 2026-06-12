"""The refuter must kill wrong candidates and NEVER emit 'proved'."""
import math, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import refuter as R

def test_rh_fake_refuted_real_survives():
    assert R.refute_rh("fake").refuted
    assert R.refute_rh("none").refuted
    assert not R.refute_rh("real").refuted          # survives-truncations (NOT proved)

def test_collatz_local_lyapunov_refuted():
    assert R.refute_collatz_lyapunov(lambda n: math.log(n), name="logn", N=5000).refuted
    assert R.refute_collatz_lyapunov(lambda n: float(n), name="n", N=5000).refuted

def test_no_verdict_is_ever_proved():
    verdicts = [R.refute_rh("real").verdict,
                R.refute_collatz_numeric(N=2000).verdict,
                R.refute_ns_coercive(0.05).verdict]
    for v in verdicts:
        assert v in ("REFUTED", "SURVIVES-TRUNCATIONS")
        assert "PROV" not in v.upper()              # no path emits 'proved'

def test_survivor_carries_banner():
    v = R.refute_rh("real")
    assert "NOT a proof" in v.banner and "never certifies" in v.banner

if __name__ == "__main__":
    test_rh_fake_refuted_real_survives(); test_collatz_local_lyapunov_refuted()
    test_no_verdict_is_ever_proved(); test_survivor_carries_banner()
    print("refuter tests PASS")
