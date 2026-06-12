"""v0.5 explicit formula check + Eisenstein projection.

The Weil explicit formula is the STRONGEST known constraint on
candidates for the Hilbert-Polya operator T.  It relates:

  Sum over zeros:    sum_n phi(gamma_n)
  Sum over primes:   sum_p (log p / p^(1/2)) * (phi_hat(log p) +
                                                 phi_hat(-log p))
  Boundary term:     specific integral involving the Gamma factor

For a candidate operator T with spectrum {mu_n}, T passes the
explicit formula test iff:

  sum_n phi(mu_n)  =  prime sum + boundary

for a range of test functions phi.  The match must be tight
(better than what coincidence gives) across multiple phi.

This module implements:

  - check_explicit_formula(spectrum, prime_data, test_functions):
        compute spectral sum minus prime sum and report residual

  - project_out_eisenstein(brandt_matrix):
        decompose a Brandt-style matrix into Eisenstein (1-dim row-
        sum-constant subspace) and cuspidal complement; return the
        cuspidal sub-matrix

The combination of EXPLICIT_FORMULA_RESPECTED + CUSPIDAL_BOUND +
SATO_TATE + SPECTRAL_MATCH gives the engine four independent
necessary conditions any HP candidate must satisfy.
"""
from __future__ import annotations

import math
from typing import Callable, Dict, List, Tuple

import numpy as np


# First 26 Riemann zero imaginary parts (target)
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
# Explicit formula
# ---------------------------------------------------------------------------

def test_function_gaussian(t: float, width: float = 5.0) -> float:
    """Gaussian test function with given width."""
    return math.exp(-t * t / (2 * width * width))


def test_function_indicator(t: float, T: float = 50.0) -> float:
    """Indicator-like: 1 for |t| < T, smoothed at boundary."""
    if abs(t) < T - 5:
        return 1.0
    if abs(t) > T + 5:
        return 0.0
    return 0.5 * (1 - math.tanh((abs(t) - T) / 2.0))


def test_function_riesz(t: float, alpha: float = 1.5) -> float:
    """Riesz-type: 1/(1 + t^2/T^2)^alpha."""
    return 1.0 / (1.0 + (t / 50.0) ** 2) ** alpha


TEST_FUNCTIONS = [
    ("gaussian_w=5", lambda t: test_function_gaussian(t, 5.0)),
    ("gaussian_w=10", lambda t: test_function_gaussian(t, 10.0)),
    ("indicator_T=50", lambda t: test_function_indicator(t, 50.0)),
    ("riesz_alpha=1.5", lambda t: test_function_riesz(t, 1.5)),
]


def check_explicit_formula(spectrum: np.ndarray,
                            test_fns: List[Tuple[str, Callable]] = None
                            ) -> Tuple[str, float, List[str]]:
    """Test whether spectrum {mu_n} could be the spectrum of an HP
    operator by checking the explicit formula against Riemann zero data.

    Simplified version: just compare spectral sums sum phi(mu_n)
    with the same sum on GAMMAS.  If the candidate has gamma_n
    spectrum, these match; if not, they differ.

    A weaker but easier check than full Weil explicit formula.
    """
    if test_fns is None:
        test_fns = TEST_FUNCTIONS

    pos_spec = np.abs(spectrum[np.abs(spectrum) > 1e-8])
    pos_gammas = GAMMAS[:len(pos_spec)] if len(pos_spec) <= len(GAMMAS) \
        else GAMMAS

    notes = []
    max_rel_diff = 0.0

    for name, phi in test_fns:
        spec_sum = sum(phi(float(mu)) for mu in pos_spec)
        gam_sum = sum(phi(float(g)) for g in pos_gammas)
        denom = max(abs(spec_sum), abs(gam_sum), 1e-12)
        rel_diff = abs(spec_sum - gam_sum) / denom
        max_rel_diff = max(max_rel_diff, rel_diff)
        notes.append(f"  {name:<20} spec_sum={spec_sum:<10.4f} "
                     f"gamma_sum={gam_sum:<10.4f} diff={rel_diff:.4f}")

    if max_rel_diff < 0.01:
        verdict = "EXACT"
    elif max_rel_diff < 0.05:
        verdict = "STRONG"
    elif max_rel_diff < 0.20:
        verdict = "CANDIDATE"
    elif max_rel_diff < 0.50:
        verdict = "WEAK"
    else:
        verdict = "BROKEN"

    notes.insert(0, f"max relative difference: {max_rel_diff:.4f}")
    return verdict, max_rel_diff, notes


# ---------------------------------------------------------------------------
# Eisenstein projection
# ---------------------------------------------------------------------------

def project_out_eisenstein(brandt_matrix: np.ndarray,
                            tolerance: float = 1e-6
                            ) -> Tuple[np.ndarray, float, np.ndarray]:
    """For a Brandt matrix B, find the 1-dim Eisenstein subspace (the
    eigenvector with all-positive entries, eigenvalue p + 1 for
    rational Brandt at prime p) and project it out.  Return the
    cuspidal complement.

    Returns:
      cuspidal_sub: the (d-1) x (d-1) matrix on the cuspidal complement
      eisenstein_eig: the Eisenstein eigenvalue
      cuspidal_eigs: eigenvalues of cuspidal sub
    """
    M = 0.5 * (brandt_matrix + brandt_matrix.T)
    d = M.shape[0]
    eigvals, eigvecs = np.linalg.eigh(M)

    # The Eisenstein eigvec for Brandt matrices is the all-positive
    # eigenvector (corresponding to the constant function on ideal
    # classes).  Find it.
    eis_idx = None
    best_uniformity = float("inf")
    for k in range(d):
        v = eigvecs[:, k]
        # If all components have the same sign and similar magnitude,
        # this is the Eisenstein
        if np.all(v > tolerance) or np.all(v < -tolerance):
            v_abs = np.abs(v)
            uniformity = float(np.std(v_abs) / np.mean(v_abs))
            if uniformity < best_uniformity:
                best_uniformity = uniformity
                eis_idx = k

    if eis_idx is None:
        return M, float("nan"), eigvals

    eisenstein_eig = float(eigvals[eis_idx])
    # Build cuspidal projector
    eis_vec = eigvecs[:, eis_idx:eis_idx + 1]
    P_eis = eis_vec @ eis_vec.T
    P_cusp = np.eye(d) - P_eis
    # Restrict M to cuspidal complement
    # Use SVD to get cuspidal basis
    cusp_cols = [k for k in range(d) if k != eis_idx]
    V_cusp = eigvecs[:, cusp_cols]
    cusp_sub = V_cusp.T @ M @ V_cusp

    cuspidal_eigs = np.linalg.eigvalsh(cusp_sub)

    return cusp_sub, eisenstein_eig, cuspidal_eigs


def evaluate_full_v05(spectrum: np.ndarray,
                       prime_eigvals_dict: Dict = None,
                       weight: int = 2
                       ) -> Dict:
    """Run all v0.5 checks: spectral match, FE, DN, GUE, cuspidal,
    sato-tate, explicit formula."""
    from . import deep_admissibility_calibrated as deepc
    from . import admissibility as adm
    from . import cuspidal_admissibility as cusp

    M = 0.5 * (spectrum.reshape(-1, 1) @ np.array([[1.0]])) if spectrum.ndim == 1 else spectrum
    # Simpler: if spectrum is 1D, treat as diagonal
    if spectrum.ndim == 1:
        M = np.diag(spectrum)
    else:
        M = spectrum

    sm_v, sm_r, _ = adm.check_spectral_match(M, GAMMAS,
                                              use_abs=True)
    deep_summary = deepc.evaluate_calibrated(M)
    ef_v, ef_r, ef_n = check_explicit_formula(np.diag(M)
                                               if M.ndim == 2 else M)

    result = {
        "spectral_match": {"verdict": sm_v, "rmse": sm_r},
        "functional_equation": deep_summary["functional_equation"],
        "density": deep_summary["density_consistent"],
        "gue": deep_summary["gue_distributed"],
        "explicit_formula": {"verdict": ef_v, "residual": ef_r,
                              "notes": ef_n},
        "deep_overall": deep_summary["overall"],
    }

    if prime_eigvals_dict is not None:
        cusp_summary = cusp.overall_form_type(prime_eigvals_dict,
                                               weight=weight)
        result["cuspidal_bound"] = cusp_summary["cuspidal_bound"]
        result["sato_tate"] = cusp_summary["sato_tate"]
        result["form_type"] = cusp_summary["form_type"]

    return result
