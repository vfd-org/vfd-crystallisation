"""V_600 construction sanity checks."""
from __future__ import annotations

from collections import Counter


def test_120_vertices(state):
    assert state["n"] == 120
    assert len(state["verts"]) == 120


def test_12_cycles_of_length_10(state):
    assert len(state["cycles"]) == 12
    assert all(len(c) == 10 for c in state["cycles"])


def test_K_multiset(state):
    assert Counter(state["K_of_cycle"]) == {72: 1, 0: 1, 52: 5, 20: 5}


def test_unique_max_K_class(state):
    K_of_cycle = state["K_of_cycle"]
    assert sum(1 for K in K_of_cycle if K == 72) == 1


def test_unique_zero_K_class(state):
    K_of_cycle = state["K_of_cycle"]
    assert sum(1 for K in K_of_cycle if K == 0) == 1
