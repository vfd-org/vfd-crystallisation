"""τ_σ involution properties (Paper 3)."""
from __future__ import annotations

from vfd_v600.tau_sigma import load_tau_sigma, verify_tau_sigma


def test_tau_sigma_loads(state):
    images = load_tau_sigma(n=state["n"])
    assert len(images) == 120


def test_tau_sigma_properties(state):
    props = verify_tau_sigma(state)
    assert props["p1"], "τ_σ must be an involution"
    assert props["p2"], "τ_σ must fix Dic_5 pointwise"
    assert props["p3"], "τ_σ must swap K=52 ↔ K=20 in non-bulk cosets"
    assert props["p4"], "τ_σ must commute with T_τ"
