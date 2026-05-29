"""Composition search engine: explore compositions of transformations
to find operators satisfying target admissibility classes.

The search loop is a structured BFS over compositions of allowed
transformations.  Each candidate is scored on each admissibility
class.  The search reports the best candidates found.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple

import numpy as np

try:
    from . import admissibility as adm
    from . import transformation_kinds as tk
except ImportError:
    import admissibility as adm
    import transformation_kinds as tk


@dataclass
class Candidate:
    operator: np.ndarray
    composition_steps: List[str]
    spectral_match_rmse: float = float("inf")
    spectral_match_verdict: str = "BROKEN"
    notes: List[str] = field(default_factory=list)


def evaluate_candidate(operator: np.ndarray,
                       composition_steps: List[str],
                       target_eigs: np.ndarray = adm.GAMMAS,
                       ) -> Candidate:
    """Score an operator on the SPECTRAL_MATCH class against target."""
    verdict, rmse, notes = adm.check_spectral_match(
        operator, target_eigs, use_abs=True)
    return Candidate(
        operator=operator,
        composition_steps=composition_steps,
        spectral_match_rmse=rmse,
        spectral_match_verdict=verdict,
        notes=notes,
    )


def search_compositions(base_operator: np.ndarray,
                        primes_to_try: List[int],
                        max_compositions: int = 4,
                        target_eigs: np.ndarray = adm.GAMMAS,
                        report_top_k: int = 10
                        ) -> List[Candidate]:
    """Systematic search.

    Strategy:
      1. Build a pool of Hecke operators T_p for each prime in
         primes_to_try.
      2. Build candidate compositions = linear combinations
         sum_i alpha_i T_{p_i} + beta * base_operator
         + gamma * base_operator^2 + ...
      3. For each candidate, do least-squares fit to target_eigs (if
         needed) and report.

    We explicitly cap the search at max_compositions to keep tractable.
    """
    candidates = []
    dim = base_operator.shape[0]

    # Build Hecke pool
    hecke_pool = []
    for p in primes_to_try:
        outcome = tk.hecke_lift(np.array([]), p, representation_dim=dim)
        T_p = outcome.output_data
        hecke_pool.append((p, T_p))

    # Step 1: try base_operator alone (and its powers)
    for k in range(1, 4):
        op_k = np.linalg.matrix_power(base_operator, k)
        op_k = 0.5 * (op_k + op_k.T)
        c = evaluate_candidate(op_k, [f"base^{k}"], target_eigs)
        candidates.append(c)

    # Step 2: each Hecke operator alone
    for p, T_p in hecke_pool:
        c = evaluate_candidate(T_p, [f"T_{p}"], target_eigs)
        candidates.append(c)

    # Step 3: pairwise sums (base + T_p)
    for p, T_p in hecke_pool:
        op = base_operator + T_p
        op = 0.5 * (op + op.T)
        c = evaluate_candidate(op, [f"base + T_{p}"], target_eigs)
        candidates.append(c)

    # Step 4: sums of two Hecke operators
    for i, (p1, T1) in enumerate(hecke_pool):
        for j, (p2, T2) in enumerate(hecke_pool):
            if i >= j:
                continue
            op = T1 + T2
            op = 0.5 * (op + op.T)
            c = evaluate_candidate(
                op, [f"T_{p1} + T_{p2}"], target_eigs)
            candidates.append(c)

    # Step 5: best-coefficient combination via least squares
    # against target eigenvalue ordering.
    feature_specs = [
        (np.linalg.matrix_power(base_operator, k)
         for k in (1, 2, 3))
    ]
    feature_specs = [base_operator,
                     np.linalg.matrix_power(base_operator, 2)]
    feature_specs += [T_p for _, T_p in hecke_pool]
    # Get spectrum from each
    spectra = []
    labels = []
    for k, M in enumerate(feature_specs):
        M_sym = 0.5 * (M + M.T)
        eigs = np.sort(np.abs(np.linalg.eigvalsh(M_sym)))
        spectra.append(eigs[-len(target_eigs):])
        if k < 2:
            labels.append(f"base^{k+1}")
        else:
            labels.append(f"T_{hecke_pool[k-2][0]}")

    F = np.vstack(spectra).T
    t = np.sort(target_eigs)
    coefs, _, _, _ = np.linalg.lstsq(F, t, rcond=None)
    pred = F @ coefs
    rmse_combined = float(np.sqrt(np.mean((pred - t) ** 2)))
    candidates.append(Candidate(
        operator=base_operator,  # placeholder
        composition_steps=[f"LS-fit({', '.join(labels)})"],
        spectral_match_rmse=rmse_combined,
        spectral_match_verdict=("EXACT" if rmse_combined < 1.0
                                else "CANDIDATE"),
        notes=[f"linear combination coefficients: "
               f"{dict(zip(labels, coefs.tolist()))}"],
    ))

    # Sort by RMSE
    candidates.sort(key=lambda c: c.spectral_match_rmse)
    return candidates[:report_top_k]
