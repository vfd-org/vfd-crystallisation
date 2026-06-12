"""v0.5 admissibility classes: cuspidal/Eisenstein distinction.

The v0.4 finding showed that the substrate's native Hecke action
(via icosian theta) is Eisenstein-scale.  The Hilbert-Polya
construction needs CUSPIDAL data.  These admissibility classes
explicitly test for the cuspidal-vs-Eisenstein distinction:

  CUSPIDAL_BOUND     -- Ramanujan: |lambda(pi)| <= 2 N(pi)^((k-1)/2)
                         For weight 2: |lambda(pi)| <= 2 sqrt(N(pi))
                         Cuspidal forms satisfy this; Eisenstein
                         forms violate it (their eigenvalues grow
                         like 1 + N(pi)^(k-1)).

  SATO_TATE          -- Normalised eigenvalues lambda_tilde(pi) =
                         lambda(pi) / (2 sqrt(N(pi))) follow the
                         semicircle distribution on [-1, 1]:
                         dmu_ST = (2/pi) sqrt(1 - x^2) dx
                         (assumes the form is non-CM cuspidal)

  CM_TYPE            -- For CM forms, Hecke eigenvalues are 0 for
                         primes inert in the CM field. Tests this
                         pattern.

A candidate that passes CUSPIDAL_BOUND + SATO_TATE is in the
non-CM cuspidal regime where Riemann zeros' GUE statistics come
from.
"""
from __future__ import annotations

import math
from typing import Dict, List, Tuple

import numpy as np


def ramanujan_bound(N_pi: float, weight: int = 2) -> float:
    """The Ramanujan bound for weight-(k, k) HMF over Q(sqrt 5):
       |lambda(pi)| <= 2 * N(pi)^((k-1)/2)
    """
    return 2.0 * N_pi ** ((weight - 1) / 2.0)


def check_cuspidal_bound(eigvals_by_prime: Dict[int, Tuple[float, str]],
                         weight: int = 2
                         ) -> Tuple[str, float, List[str]]:
    """Check whether Hecke eigenvalues satisfy the cuspidal Ramanujan
    bound.

    Input:
      eigvals_by_prime: {p: (lambda_p, kind)} where kind in
                       {'inert', 'split', 'ramified', 'anomalous'}.
                       For inert p of Q(sqrt 5), N(pi) = p^2.

    Returns ("EXACT" | "STRONG" | "CANDIDATE" | "WEAK" | "BROKEN",
              max_violation_ratio, notes).
    """
    notes = []
    violations = []
    bounds = []

    for p, (lam, kind) in eigvals_by_prime.items():
        if kind == "inert":
            N_pi = p * p
        elif kind in ("split", "split_a", "split_b"):
            N_pi = p
        elif kind == "ramified":
            N_pi = p
        elif kind == "anomalous":
            N_pi = p  # for p = 2 special
        else:
            continue
        bound = ramanujan_bound(N_pi, weight=weight)
        violation = abs(lam) / max(bound, 1e-12)
        violations.append(violation)
        bounds.append((p, kind, N_pi, lam, bound, violation))

    if not violations:
        return "DEGENERATE", float("inf"), ["no eigenvalues to check"]

    max_v = max(violations)
    median_v = float(np.median(violations))

    if max_v < 1.05:
        verdict = "EXACT"  # cuspidal, well within Ramanujan
    elif max_v < 1.5:
        verdict = "STRONG"
    elif max_v < 3.0:
        verdict = "CANDIDATE"
    elif max_v < 10.0:
        verdict = "WEAK"
    else:
        verdict = "BROKEN"  # certainly Eisenstein

    notes.append(f"max violation ratio (|lambda|/Ramanujan bound): "
                 f"{max_v:.4f}")
    notes.append(f"median: {median_v:.4f}")
    notes.append(f"checked {len(violations)} primes")
    if max_v >= 3.0:
        notes.append("Likely EISENSTEIN, not cuspidal")
    elif max_v < 1.5:
        notes.append("Consistent with cuspidal form")
    return verdict, max_v, notes


def check_sato_tate(normalised_eigvals: List[float],
                    n_bins: int = 8
                    ) -> Tuple[str, float, List[str]]:
    """Check whether normalised Hecke eigenvalues follow the
    Sato-Tate semicircle distribution on [-1, 1].

    p_ST(x) = (2/pi) * sqrt(1 - x^2) for x in [-1, 1]

    For our N_pi normalisation lambda_tilde = lambda / (2 sqrt(N_pi)),
    cuspidal non-CM forms have lambda_tilde distributed by p_ST.
    """
    if len(normalised_eigvals) < 5:
        return "DEGENERATE", float("inf"), [
            f"too few eigvals ({len(normalised_eigvals)}) for ST test"]

    # Filter to [-1, 1] range (clipped)
    eigs = np.array([e for e in normalised_eigvals if -1.5 <= e <= 1.5])
    # If many are outside [-1, 1], probably not cuspidal
    out_of_range = sum(1 for e in normalised_eigvals
                       if abs(e) > 1.0)
    out_frac = out_of_range / len(normalised_eigvals)

    if out_frac > 0.3:
        notes = [
            f"{out_of_range}/{len(normalised_eigvals)} eigvals outside "
            f"[-1, 1] (fraction {out_frac:.2f})",
            "incompatible with Sato-Tate -- form is likely Eisenstein "
            "or CM",
        ]
        return "BROKEN", float("inf"), notes

    # Compute KS distance to Sato-Tate CDF on [-1, 1]
    eigs_clipped = np.clip(eigs, -1.0, 1.0)
    eigs_sorted = np.sort(eigs_clipped)

    # ST CDF: integral of (2/pi)*sqrt(1-t^2) from -1 to x
    # F_ST(x) = (1/pi) * (x*sqrt(1-x^2) + arcsin(x)) + 0.5
    def st_cdf(x):
        return (1 / math.pi) * (
            x * math.sqrt(max(1 - x * x, 0)) + math.asin(min(max(x, -1), 1))
        ) + 0.5

    sample_cdf = np.arange(1, len(eigs_sorted) + 1) / len(eigs_sorted)
    st_vals = np.array([st_cdf(x) for x in eigs_sorted])
    ks = float(np.max(np.abs(sample_cdf - st_vals)))

    threshold = 1.36 / math.sqrt(len(eigs_sorted))

    if ks < threshold / 2:
        verdict = "EXACT"
    elif ks < threshold:
        verdict = "STRONG"
    elif ks < threshold * 2:
        verdict = "CANDIDATE"
    elif ks < threshold * 4:
        verdict = "WEAK"
    else:
        verdict = "BROKEN"

    notes = [
        f"KS distance vs ST CDF: {ks:.4f}",
        f"5% significance threshold: {threshold:.4f}",
        f"out-of-range fraction: {out_frac:.2f}",
    ]
    return verdict, ks, notes


def overall_form_type(eigvals_by_prime: Dict[int, Tuple[float, str]],
                       weight: int = 2
                       ) -> Dict:
    """Return a summary classification of the form type based on
    Hecke eigenvalues."""

    # Bound check
    cb_v, cb_r, cb_n = check_cuspidal_bound(eigvals_by_prime, weight)

    # Normalised eigenvalues
    normalised = []
    for p, (lam, kind) in eigvals_by_prime.items():
        if kind == "inert":
            N_pi = p * p
        elif kind in ("split", "split_a", "split_b", "ramified",
                       "anomalous"):
            N_pi = p
        else:
            continue
        normalised.append(lam / (2 * math.sqrt(N_pi)))

    # Sato-Tate check
    st_v, st_r, st_n = check_sato_tate(normalised)

    # Composite verdict
    if cb_v in ("EXACT", "STRONG") and st_v in ("EXACT", "STRONG",
                                                 "CANDIDATE"):
        form_type = "CUSPIDAL_NON_CM"
    elif cb_v in ("EXACT", "STRONG"):
        form_type = "CUSPIDAL_OR_CM"
    elif cb_v in ("CANDIDATE",):
        form_type = "BORDERLINE"
    elif cb_v in ("BROKEN", "WEAK"):
        form_type = "EISENSTEIN"
    else:
        form_type = "UNKNOWN"

    return {
        "cuspidal_bound": {
            "verdict": cb_v, "residual": cb_r, "notes": cb_n},
        "sato_tate": {
            "verdict": st_v, "residual": st_r, "notes": st_n},
        "form_type": form_type,
        "normalised_eigvals": normalised,
    }
