"""Deep admissibility checks: the actual constraints that any
Hilbert-Polya candidate must satisfy.

The basic SPECTRAL_MATCH admissibility (in admissibility.py) only
checks eigenvalue magnitudes against gamma_n.  It is too coarse to
narrow the search: many random Hermitians can game it with
parameters.

This module adds four sharper checks corresponding to known
structural properties of Riemann zeros:

  FUNCTIONAL_EQUATION_RESPECTED: spectrum is symmetric under
    s -> 1-s reflection, which for zeros at 1/2 + i*gamma means
    {gamma_i} = {-gamma_i} (sign-symmetric).

  DENSITY_CONSISTENT: spectrum follows Riemann-Hardy-Littlewood
    N(T) ~ (T/2*pi) log(T/2*pi) - T/(2*pi) zero-counting law.

  GUE_DISTRIBUTED: nearest-neighbor spacing distribution matches
    Wigner GUE form p(s) = (32/pi^2) s^2 exp(-4 s^2 / pi)
    (Montgomery-Odlyzko statistic).

  HECKE_MULTIPLICATIVE: spectrum corresponds to Hecke eigenvalues
    satisfying lambda(mn) = lambda(m) lambda(n) for gcd(m,n) = 1.

Each check returns (verdict, residual, notes).  A candidate operator
that passes ALL of these is in genuine Hilbert-Polya territory; the
substrate's prototype operators uniformly FAIL most of these, which
explains why they can't be T.
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


# ---------------------------------------------------------------------------
# (1) FUNCTIONAL_EQUATION_RESPECTED
# ---------------------------------------------------------------------------

def check_functional_equation(operator: np.ndarray,
                              tolerance: float = 0.01
                              ) -> Tuple[str, float, List[str]]:
    """Check whether the operator's spectrum is symmetric under
    eigenvalue negation (i.e. {lambda_i} = {-lambda_i}).

    Riemann zeros at 1/2 + i*gamma come in pairs {gamma, -gamma}
    by the functional equation Z(s) = Z(1-s) with the gamma factor.
    Any candidate spectral operator T whose eigenvalues realise
    gamma_n must have this sign-symmetric spectrum.
    """
    M = 0.5 * (operator + operator.T)
    eigs = np.linalg.eigvalsh(M)
    # For sign-symmetric spectrum, sum of eigvals should be close to 0
    # and the multiset should match its negative
    eigs_neg = -eigs
    eigs_sorted = np.sort(eigs)
    eigs_neg_sorted = np.sort(eigs_neg)
    diff = float(np.linalg.norm(eigs_sorted - eigs_neg_sorted, ord=np.inf))
    scale = float(np.max(np.abs(eigs))) + 1e-12
    rel_diff = diff / scale
    trace_residual = float(abs(np.sum(eigs))) / scale

    if rel_diff < tolerance and trace_residual < tolerance:
        verdict = "EXACT"
    elif rel_diff < tolerance * 10 and trace_residual < tolerance * 10:
        verdict = "STRONG"
    elif rel_diff < tolerance * 100:
        verdict = "CANDIDATE"
    else:
        verdict = "BROKEN"

    notes = [
        f"sign-symmetry max deviation: {rel_diff:.4e} (rel)",
        f"trace residual: {trace_residual:.4e} (rel)",
        f"functional equation s <-> 1-s requires "
        f"{{lambda_i}} = {{-lambda_i}}",
    ]
    return verdict, rel_diff, notes


# ---------------------------------------------------------------------------
# (2) DENSITY_CONSISTENT
# ---------------------------------------------------------------------------

def riemann_N_asymptotic(T: float) -> float:
    """Riemann-Hardy-Littlewood asymptotic for zero count.
       N(T) ~ (T/2*pi) log(T/2*pi) - T/(2*pi) + O(log T)
    """
    if T < 1.0:
        return 0.0
    return (T / (2 * math.pi)) * math.log(T / (2 * math.pi)) - T / (2 * math.pi)


def check_density_consistent(spectrum: np.ndarray,
                              tolerance: float = 0.20
                              ) -> Tuple[str, float, List[str]]:
    """Check whether the candidate spectrum's density matches
    Riemann-Hardy-Littlewood N(T) asymptotic.
    """
    pos = np.sort(np.abs(spectrum))
    if len(pos) < 5:
        return "DEGENERATE", float("inf"), [
            f"too few eigvals ({len(pos)}) to check density"]

    # Compare actual count <= each pos[k] against asymptotic prediction
    deviations = []
    for k in range(len(pos)):
        T = float(pos[k])
        predicted = riemann_N_asymptotic(T)
        actual = k + 1
        if predicted > 0.1:
            deviations.append(abs(actual - predicted) / predicted)
    rel_dev = float(np.median(deviations)) if deviations else float("inf")

    if rel_dev < tolerance / 4:
        verdict = "EXACT"
    elif rel_dev < tolerance / 2:
        verdict = "STRONG"
    elif rel_dev < tolerance:
        verdict = "CANDIDATE"
    elif rel_dev < tolerance * 4:
        verdict = "WEAK"
    else:
        verdict = "BROKEN"

    notes = [
        f"median relative density deviation: {rel_dev:.4f}",
        f"target asymptotic: N(T) ~ T/(2 pi) (log(T/2 pi) - 1)",
        f"checked {len(deviations)} eigvals at increasing magnitudes",
    ]
    return verdict, rel_dev, notes


# ---------------------------------------------------------------------------
# (3) GUE_DISTRIBUTED
# ---------------------------------------------------------------------------

def gue_density(s: float) -> float:
    """Wigner GUE nearest-neighbor spacing density.
       p(s) = (32/pi^2) s^2 exp(-4 s^2 / pi)
    """
    return (32.0 / (math.pi * math.pi)) * s * s * math.exp(
        -4.0 * s * s / math.pi)


def check_gue_distributed(spectrum: np.ndarray,
                           tolerance: float = 0.5,
                           bins: int = 8
                           ) -> Tuple[str, float, List[str]]:
    """Check whether nearest-neighbor spacings match GUE.

    The Montgomery-Odlyzko pair correlation conjecture predicts that
    normalised consecutive spacings of Riemann zeros follow the GUE
    density.  Any candidate operator whose spectrum models gamma_n
    must approximately satisfy this.

    We compare a histogram of normalised spacings against the GUE
    density via L2 norm on a discretisation.
    """
    pos = np.sort(np.abs(spectrum))
    pos = pos[pos > 1e-8]
    if len(pos) < 6:
        return "DEGENERATE", float("inf"), [
            f"too few eigvals ({len(pos)}) for spacing histogram"]

    spacings = np.diff(pos)
    if len(spacings) < 3:
        return "DEGENERATE", float("inf"), [
            "too few spacings for histogram"]
    # Normalise: divide by mean spacing
    mean_spacing = float(np.mean(spacings))
    if mean_spacing < 1e-8:
        return "DEGENERATE", float("inf"), [
            "mean spacing too small"]
    norm_spacings = spacings / mean_spacing

    # Compute histogram and compare to GUE
    hist, edges = np.histogram(norm_spacings, bins=bins,
                                range=(0, 4), density=True)
    # GUE density at bin centers
    centers = 0.5 * (edges[:-1] + edges[1:])
    gue_pred = np.array([gue_density(c) for c in centers])
    deviation = float(np.linalg.norm(hist - gue_pred)) / max(
        float(np.linalg.norm(gue_pred)), 1e-8)

    if deviation < tolerance / 4:
        verdict = "EXACT"
    elif deviation < tolerance / 2:
        verdict = "STRONG"
    elif deviation < tolerance:
        verdict = "CANDIDATE"
    elif deviation < tolerance * 2:
        verdict = "WEAK"
    else:
        verdict = "BROKEN"

    notes = [
        f"relative L2 deviation from GUE: {deviation:.4f}",
        f"histogram bins: {bins}, range [0, 4]",
        f"normalised by mean spacing {mean_spacing:.4f}",
    ]
    return verdict, deviation, notes


# ---------------------------------------------------------------------------
# (4) HECKE_MULTIPLICATIVE
# ---------------------------------------------------------------------------

def check_hecke_multiplicative(eigvalue_table: Dict[int, float],
                                tolerance: float = 1e-4
                                ) -> Tuple[str, float, List[str]]:
    """Check whether eigenvalue_table[n] satisfies Hecke
    multiplicativity: lambda(mn) = lambda(m) lambda(n) for
    gcd(m, n) = 1.

    Input: dict mapping integer index n (e.g. prime power) to
    eigenvalue.
    """
    if not eigvalue_table:
        return "DEGENERATE", float("inf"), [
            "empty eigenvalue table"]

    def coprime(a, b):
        return math.gcd(a, b) == 1

    deviations = []
    pairs_tested = 0
    for m in eigvalue_table:
        for n in eigvalue_table:
            if m == 1 or n == 1 or m == n:
                continue
            if not coprime(m, n):
                continue
            mn = m * n
            if mn not in eigvalue_table:
                continue
            predicted = eigvalue_table[m] * eigvalue_table[n]
            actual = eigvalue_table[mn]
            denom = max(abs(predicted), abs(actual), 1e-12)
            dev = abs(actual - predicted) / denom
            deviations.append(dev)
            pairs_tested += 1

    if pairs_tested == 0:
        return "DEGENERATE", float("inf"), [
            "no coprime pairs in table to test"]

    max_dev = max(deviations)
    median_dev = float(np.median(deviations))

    if max_dev < tolerance:
        verdict = "EXACT"
    elif max_dev < tolerance * 100:
        verdict = "STRONG"
    elif max_dev < tolerance * 10000:
        verdict = "CANDIDATE"
    else:
        verdict = "BROKEN"

    notes = [
        f"tested {pairs_tested} coprime pairs (m, n) -> mn",
        f"max relative deviation: {max_dev:.4e}",
        f"median relative deviation: {median_dev:.4e}",
    ]
    return verdict, max_dev, notes


# ---------------------------------------------------------------------------
# Composite check: passes all four
# ---------------------------------------------------------------------------

def check_hilbert_polya_candidate(operator: np.ndarray,
                                   eigvalue_table: Optional[Dict[int, float]]
                                   = None
                                   ) -> Dict:
    """Run all four deep admissibility checks on a candidate operator.

    Returns a summary dict with per-check verdicts and an overall
    HP-candidate verdict.
    """
    eigs = np.linalg.eigvalsh(0.5 * (operator + operator.T))

    fe_v, fe_r, fe_n = check_functional_equation(operator)
    dn_v, dn_r, dn_n = check_density_consistent(eigs)
    gue_v, gue_r, gue_n = check_gue_distributed(eigs)
    if eigvalue_table:
        hk_v, hk_r, hk_n = check_hecke_multiplicative(eigvalue_table)
    else:
        hk_v, hk_r, hk_n = ("N/A", float("nan"),
                            ["no eigenvalue table provided"])

    verdicts = [fe_v, dn_v, gue_v]
    if hk_v != "N/A":
        verdicts.append(hk_v)

    if all(v == "EXACT" for v in verdicts):
        overall = "HILBERT_POLYA_CANDIDATE_STRONG"
    elif all(v in ("EXACT", "STRONG") for v in verdicts):
        overall = "HILBERT_POLYA_CANDIDATE"
    elif any(v == "BROKEN" for v in verdicts):
        overall = "RULED_OUT"
    else:
        overall = "PARTIAL_PASS"

    return {
        "functional_equation": {
            "verdict": fe_v, "residual": fe_r, "notes": fe_n},
        "density_consistent": {
            "verdict": dn_v, "residual": dn_r, "notes": dn_n},
        "gue_distributed": {
            "verdict": gue_v, "residual": gue_r, "notes": gue_n},
        "hecke_multiplicative": {
            "verdict": hk_v, "residual": hk_r, "notes": hk_n},
        "overall": overall,
    }
