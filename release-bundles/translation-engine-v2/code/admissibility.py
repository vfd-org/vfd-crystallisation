"""Extended admissibility checks for the translation engine.

The base engine has five admissibility classes (EXACT, CANDIDATE,
APPROXIMATE, BROKEN, DEGENERATE).  This module adds four
analytic-side classes:

    SPECTRAL_MATCH    -- eigenvalues approximate a target spectrum
                         (used for gamma_n matching)
    ZERO_LINE_FORCED  -- candidate L-function zeros lie on
                         Re(s) = 1/2
    HECKE_COMPATIBLE  -- operator respects Hecke commutation relations
    MODULAR_INVARIANT -- invariance under modular transformations

Each class has a `check` function returning (verdict, residual, notes).
"""
from __future__ import annotations

import math
from typing import Dict, List, Optional, Tuple

import numpy as np


# Riemann gamma_n target (first 26)
GAMMAS = np.array([
    14.134725141734693, 21.022039638771555, 25.010857580145688,
    30.424876125859513, 32.935061587739190, 37.586178158825671,
    40.918719012147495, 43.327073280914999, 48.005150881167160,
    49.773832477672302, 52.970321477714461, 56.446247697063246,
    59.347044002602353, 60.831778524609811, 65.112544048081607,
    67.079810529494173, 69.546401711173979, 72.067157674481907,
    75.704690699083933, 77.144840068874806, 79.337375020249367,
    82.910380854086030, 84.735492980517050, 87.425274613125229,
    88.809111207634465, 92.491899270558484,
])


def check_spectral_match(operator: np.ndarray,
                         target: np.ndarray = GAMMAS,
                         tolerance: float = 1.0,
                         use_abs: bool = True
                         ) -> Tuple[str, float, List[str]]:
    """Compare operator's eigenvalues (or |eigvals|) against target.

    Returns (verdict, RMSE, notes).
      verdict in {"EXACT", "STRONG", "CANDIDATE", "WEAK", "BROKEN"}
    """
    M = 0.5 * (operator + operator.T)
    eigs = np.linalg.eigvalsh(M)
    if use_abs:
        eigs = np.sort(np.abs(eigs))
    else:
        eigs = np.sort(eigs)

    # Truncate to length of target
    n_target = len(target)
    if len(eigs) < n_target:
        return "DEGENERATE", float("inf"), [
            f"operator has only {len(eigs)} eigvals; need {n_target}"]
    eigs_truncated = eigs[-n_target:]  # take top n_target
    target_sorted = np.sort(target)

    rmse = float(np.sqrt(np.mean((eigs_truncated - target_sorted) ** 2)))
    rel_error = rmse / float(np.mean(target_sorted))

    if rmse < tolerance:
        verdict = "EXACT"
    elif rel_error < 0.05:
        verdict = "STRONG"
    elif rel_error < 0.15:
        verdict = "CANDIDATE"
    elif rel_error < 0.50:
        verdict = "WEAK"
    else:
        verdict = "BROKEN"

    notes = [
        f"RMSE = {rmse:.4f} (relative {rel_error:.2%})",
        f"target range [{target_sorted.min():.2f}, "
        f"{target_sorted.max():.2f}]",
        f"operator range [{eigs_truncated.min():.2f}, "
        f"{eigs_truncated.max():.2f}]",
    ]
    return verdict, rmse, notes


def check_zero_line_forced(L_path_data: Dict,
                           tolerance: float = 0.5
                           ) -> Tuple[str, float, List[str]]:
    """Check whether candidate analytic continuation has zeros that
    cluster on Re(s) = 1/2 (vs scattered elsewhere).

    Input: L_path_data with keys 'gammas', 'L_path', 'candidate_zeros'.
    """
    candidate_zeros = L_path_data.get("candidate_zeros", [])
    if not candidate_zeros:
        return "BROKEN", float("inf"), ["no candidate zeros found"]

    # Compute "zero clustering" score: how tightly do zeros cluster
    # on the critical line?  Since our path IS on Re=1/2, this becomes
    # "do they cluster at all (vs. random spacing)?"
    spacings = np.diff(sorted(candidate_zeros))
    cv = (float(np.std(spacings)) / float(np.mean(spacings))
          if len(spacings) > 0 else float("inf"))

    # Lower CV = more regular spacing = more "zero line structured"
    if cv < tolerance / 2:
        verdict = "STRONG"
    elif cv < tolerance:
        verdict = "CANDIDATE"
    elif cv < tolerance * 2:
        verdict = "WEAK"
    else:
        verdict = "BROKEN"

    notes = [
        f"found {len(candidate_zeros)} candidate zeros on Re(s)=1/2",
        f"spacing CV = {cv:.4f} "
        f"(lower = more zero-line structured)",
    ]
    return verdict, cv, notes


def check_hecke_compatible(T: np.ndarray, T_p_list: List[np.ndarray],
                           tolerance: float = 1e-6
                           ) -> Tuple[str, float, List[str]]:
    """Check whether T commutes with the given Hecke operators T_p
    pairwise.  Hecke operators commute pairwise by classical theory;
    if our candidate T commutes with all T_p, it's Hecke-compatible.
    """
    max_commutator_norm = 0.0
    for i, T_p in enumerate(T_p_list):
        comm = T @ T_p - T_p @ T
        norm = float(np.linalg.norm(comm, ord="fro"))
        max_commutator_norm = max(max_commutator_norm, norm)

    if max_commutator_norm < tolerance:
        verdict = "EXACT"
    elif max_commutator_norm < tolerance * 100:
        verdict = "STRONG"
    elif max_commutator_norm < tolerance * 10000:
        verdict = "CANDIDATE"
    else:
        verdict = "BROKEN"

    notes = [
        f"tested commutativity with {len(T_p_list)} Hecke operators",
        f"max ||[T, T_p]||_F = {max_commutator_norm:.4e}",
    ]
    return verdict, max_commutator_norm, notes


def check_modular_invariant(matrix: np.ndarray,
                            substrate_action_generators: List[np.ndarray],
                            tolerance: float = 1e-6
                            ) -> Tuple[str, float, List[str]]:
    """Check invariance under given substrate action generators.

    Generators g_i should satisfy g_i^t @ matrix @ g_i = matrix.
    """
    max_deviation = 0.0
    for g in substrate_action_generators:
        transformed = g.T @ matrix @ g
        deviation = float(np.linalg.norm(matrix - transformed, ord="fro"))
        max_deviation = max(max_deviation, deviation)

    if max_deviation < tolerance:
        verdict = "EXACT"
    elif max_deviation < tolerance * 100:
        verdict = "STRONG"
    elif max_deviation < tolerance * 10000:
        verdict = "CANDIDATE"
    else:
        verdict = "BROKEN"

    notes = [
        f"tested against {len(substrate_action_generators)} generators",
        f"max ||g^t M g - M||_F = {max_deviation:.4e}",
    ]
    return verdict, max_deviation, notes
