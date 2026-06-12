"""Linear/dynamical-systems adapter. Shell = log-norm; boundary = unbounded orbit.
Controls: a known-stable (rho<1), a known-escaping (rho>1), an isometric (rho=1)."""
import numpy as np, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "core"))
from shell_problem import classify_linear

def run():
    cases = {
        "stable_contraction": np.array([[0.5, 0.3], [0.0, 0.4]]),
        "escaping_rho>1":     np.array([[1.3, 0.0], [0.0, 0.6]]),
        "isometric_rotation": np.array([[0.0, -1.0], [1.0, 0.0]]),
        "critical_jordan":    np.array([[1.0, 1.0], [0.0, 1.0]]),
    }
    out = {k: classify_linear(M) for k, M in cases.items()}
    out["_controls_separate"] = (out["stable_contraction"]["outcome"] == "CLOSED"
        and out["escaping_rho>1"]["outcome"] == "ESCAPING"
        and out["critical_jordan"]["outcome"] == "CRITICAL")
    return out

if __name__ == "__main__":
    import json; print(json.dumps(run(), indent=2, default=str))
