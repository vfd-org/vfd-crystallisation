"""Canonical τ_σ involution loader.

The map V_600 → V_600 is supplied as a static text file
(papers/v600-programme/data/tau_sigma_canonical.txt) that pairs vertex
indices i, τ_σ(i). This module loads it and provides verification.

The construction itself lives in Paper 3 (tau-sigma-construction);
verify scripts here only check the loaded map satisfies its properties.
"""

from __future__ import annotations

from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "tau_sigma_canonical.txt"


def load_tau_sigma(n=120, path=None):
    """Load τ_σ as a length-n list where images[i] = τ_σ(i).

    Raises if the file is missing or the loaded map is not an involution.
    """
    p = Path(path) if path else DATA_PATH
    images = [None] * n
    with open(p) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            i, j = (int(x) for x in line.split(","))
            images[i] = j
    if any(im is None for im in images):
        missing = [i for i, im in enumerate(images) if im is None]
        raise ValueError(f"τ_σ map incomplete: missing indices {missing[:8]}…")
    if any(images[images[i]] != i for i in range(n)):
        raise ValueError("τ_σ map is not an involution")
    return images


def verify_tau_sigma(state, images=None):
    """Check the four canonical properties of τ_σ:

      P1. Involution:    τ_σ(τ_σ(v)) = v for all v.
      P2. Fixes Dic_5:   τ_σ(v) = v for all v ∈ Dic_5 (20 verts).
      P3. K-swap:        for v in non-trivial coset, τ_σ swaps K=52 ↔ K=20.
      P4. T_τ-equivariant: τ_σ ∘ T_τ = T_τ ∘ τ_σ.

    Returns a dict {p1, p2, p3, p4: bool}.
    """
    if images is None:
        images = load_tau_sigma(n=state["n"])

    n = state["n"]
    Dic5 = state["Dic5"]
    cycle_of = state["cycle_of"]
    K_of_cycle = state["K_of_cycle"]
    T = state["T"]

    p1 = all(images[images[i]] == i for i in range(n))
    p2 = all(images[v] == v for v in Dic5)

    # Cross-K swap: for any v not in Dic_5, K(cycle of v) and K(cycle of τ_σ(v))
    # should be {52, 20}.
    p3 = True
    for v in range(n):
        if v in Dic5:
            continue
        K_v = K_of_cycle[cycle_of[v]]
        K_t = K_of_cycle[cycle_of[images[v]]]
        if {K_v, K_t} != {52, 20}:
            p3 = False
            break

    p4 = all(images[T[i]] == T[images[i]] for i in range(n))

    return {"p1": p1, "p2": p2, "p3": p3, "p4": p4}
