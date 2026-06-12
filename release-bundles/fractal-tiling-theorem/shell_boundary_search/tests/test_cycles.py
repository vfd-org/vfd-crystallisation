"""Smoke test: parity-vector bijection + classifier outcomes."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "domains"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "core"))
import collatz_adapter as C
from shell_problem import classify_linear
import numpy as np

def test_terras():
    b = C.verify_terras_bijection(kmax=8)
    assert all(v["bijection"] for v in b.values())

def test_linear_modes():
    assert classify_linear(np.array([[0.5,0.0],[0.0,0.3]]))["outcome"] == "CLOSED"
    assert classify_linear(np.array([[1.3,0.0],[0.0,0.4]]))["outcome"] == "ESCAPING"
    assert classify_linear(np.array([[1.0,1.0],[0.0,1.0]]))["outcome"] == "CRITICAL"

if __name__ == "__main__":
    test_terras(); test_linear_modes(); print("tests PASS")
