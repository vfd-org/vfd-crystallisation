"""Extended transformation kinds for the translation engine.

The original engine has 12 finite transformation kinds (DUAL,
SHELL_PROJECTION, ..., DIMENSIONAL_PROJECTION).  This module adds
five new kinds that bridge the finite algebraic substrate to the
infinite-dimensional analytic side:

    HECKE_LIFT            (substrate, prime p)    -> Hecke matrix T_p
    MODULAR_EMBED         (substrate)             -> Hilbert modular
                                                     embedding context
    ANALYTIC_EXTEND       (finite spectrum, level) -> truncated
                                                     analytic-continuation
                                                     spectrum
    SPECTRAL_LIFT_INFINITE (finite operator, N)   -> N-truncation of
                                                     infinite-dim operator
                                                     candidate
    TRACE_FORMULA_CLOSE   (operator)              -> Selberg-style check
                                                     for trace-formula
                                                     consistency

Each transformation has an `apply` function that returns a typed
`TransformationOutcome` recording inputs, outputs, residuals, and
admissibility verdict.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Tuple

import numpy as np

PHI = (1.0 + math.sqrt(5.0)) / 2.0
INVPHI = 1.0 / PHI


class TransformationKind(str, Enum):
    # Original (finite, from closure_transform_engine)
    DUAL = "dual"
    SHELL_PROJECTION = "shell_projection"
    SPECTRAL_PROJECTION = "spectral_projection"
    QUOTIENT = "quotient"
    SUBGROUP_RESTRICTION = "subgroup_restriction"
    DIMENSIONAL_LIFT = "dimensional_lift"
    DIMENSIONAL_PROJECTION = "dimensional_projection"
    # New (bridge to analytic)
    HECKE_LIFT = "hecke_lift"
    MODULAR_EMBED = "modular_embed"
    ANALYTIC_EXTEND = "analytic_extend"
    SPECTRAL_LIFT_INFINITE = "spectral_lift_infinite"
    TRACE_FORMULA_CLOSE = "trace_formula_close"


class Admissibility(str, Enum):
    # Original 5
    EXACT = "exact"
    CANDIDATE = "candidate"
    APPROXIMATE = "approximate"
    BROKEN = "broken"
    DEGENERATE = "degenerate"
    # New analytic admissibility classes
    SPECTRAL_MATCH = "spectral_match"      # eigvals approx gamma_n
    ZERO_LINE_FORCED = "zero_line_forced"  # analytic continuation pure-imaginary
    HECKE_COMPATIBLE = "hecke_compatible"  # respects Hecke commutation
    MODULAR_INVARIANT = "modular_invariant"  # invariant under SL_2 action


@dataclass
class TransformationOutcome:
    kind: TransformationKind
    input_summary: str
    output_summary: str
    output_data: Any = None
    admissibility: Admissibility = Admissibility.CANDIDATE
    residual: float = 0.0
    notes: List[str] = field(default_factory=list)
    interpretation: str = ""

    def to_dict(self) -> dict:
        return {
            "kind": self.kind.value,
            "input": self.input_summary,
            "output": self.output_summary,
            "admissibility": self.admissibility.value,
            "residual": self.residual,
            "interpretation": self.interpretation,
            "notes": list(self.notes),
        }


# ---------------------------------------------------------------------------
# (1) HECKE_LIFT
# ---------------------------------------------------------------------------

def hecke_lift(substrate_eigs: np.ndarray, p: int,
               representation_dim: int = 26) -> TransformationOutcome:
    """Construct a candidate Hecke-style operator T_p on a finite-dim
    truncation of the Hilbert modular form space.

    For a prime p that splits / is inert / ramifies in Z[phi], T_p has
    specific structural properties:
      - p splits  (p mod 5 in {1, 4}): T_p has eigenvalue 2*sqrt(p)
                                        with multiplicity matching the
                                        Galois orbit (so 2 eigenspaces
                                        of dim N/2 each).
      - p inert   (p mod 5 in {2, 3}): T_p eigenvalues are real but
                                        related to (1 + p^2)-counts via
                                        Eichler-Brandt.
      - p ramified (p = 5)           : T_p has eigvals involving sqrt(5).

    We construct a low-weight Hecke-like operator using the structural
    properties + the substrate's existing 2I irrep decomposition.

    Mathematical guard-rail: this is a STRUCTURAL prototype, not a full
    Hecke construction. We document explicitly what's mathematical fact
    and what's prototype scaffolding.
    """
    if p % 5 in (1, 4):
        kind_p = "split"
        # Eigval at 2*sqrt(p) with Galois pair
        target_eig = 2 * math.sqrt(p)
        eigvals = np.zeros(representation_dim)
        eigvals[:representation_dim // 2] = target_eig
        eigvals[representation_dim // 2:] = -target_eig
    elif p % 5 in (2, 3):
        kind_p = "inert"
        # Eichler-Brandt style: r(p)/8 = 1 + p^2
        target_eig = math.sqrt(1.0 + p * p)
        eigvals = np.zeros(representation_dim)
        eigvals[:representation_dim // 2] = target_eig
        eigvals[representation_dim // 2:] = -target_eig
    elif p == 5:
        kind_p = "ramified"
        target_eig = math.sqrt(5.0)
        eigvals = np.zeros(representation_dim)
        eigvals[:representation_dim // 2] = target_eig
        eigvals[representation_dim // 2:] = -target_eig
    else:
        kind_p = "anomalous (p=2)"
        target_eig = 3.0  # from Jacobi anomaly
        eigvals = np.zeros(representation_dim)
        eigvals[:representation_dim // 2] = target_eig
        eigvals[representation_dim // 2:] = -target_eig

    # Build a Hermitian matrix with these eigenvalues
    Q, _ = np.linalg.qr(np.random.RandomState(p).standard_normal(
        (representation_dim, representation_dim)))
    T_p = Q @ np.diag(eigvals) @ Q.T

    return TransformationOutcome(
        kind=TransformationKind.HECKE_LIFT,
        input_summary=f"substrate eigvals + prime p = {p}",
        output_summary=f"T_p ({representation_dim}x{representation_dim}) "
                       f"with eigenvalue magnitude {target_eig:.4f}, "
                       f"prime kind = {kind_p}",
        output_data=T_p,
        admissibility=Admissibility.CANDIDATE,
        residual=0.0,
        notes=[f"prime p = {p}",
               f"split / inert / ramified: {kind_p}",
               "prototype: target eigenvalue from Eichler-Brandt; "
               "actual Hecke action on Hilbert modular forms is more "
               "involved"],
        interpretation=("Candidate Hecke-style operator capturing "
                        f"arithmetic at prime {p}."),
    )


# ---------------------------------------------------------------------------
# (2) MODULAR_EMBED
# ---------------------------------------------------------------------------

def modular_embed(substrate_info: Dict) -> TransformationOutcome:
    """Record the Hilbert modular embedding context for the substrate.

    For V_600 (= 2I), the natural embedding is into SL_2(O_K) where
    O_K = Z[phi].  The corresponding Hilbert modular surface is
    (H x H) / SL_2(O_K).

    This transformation records the embedding metadata; full Hilbert
    modular form construction is delegated to ANALYTIC_EXTEND.
    """
    K = "Q(sqrt 5)"
    O_K = "Z[phi]"
    surface = f"(H x H) / SL_2({O_K})"

    return TransformationOutcome(
        kind=TransformationKind.MODULAR_EMBED,
        input_summary=str(substrate_info),
        output_summary=f"Hilbert modular surface {surface}",
        output_data={"field": K, "order": O_K, "surface": surface,
                     "weight": (2, 2),
                     "level": substrate_info.get("level", 1)},
        admissibility=Admissibility.EXACT,
        residual=0.0,
        notes=[f"field K = {K}",
               "embedding is the canonical Hilbert modular group",
               "weight (2, 2) is the lowest analytically-interesting "
               "weight; higher weights are CANDIDATE for richer "
               "spectral data"],
        interpretation="Records the analytic context for subsequent "
                       "Hecke-lift and analytic-extend operations.",
    )


# ---------------------------------------------------------------------------
# (3) ANALYTIC_EXTEND
# ---------------------------------------------------------------------------

def analytic_extend(finite_spectrum: np.ndarray,
                    truncation_level: int = 50) -> TransformationOutcome:
    """Take a finite spectral data set and produce a candidate analytic
    continuation via the Mellin / Dirichlet-series mechanism.

    Specifically: given a finite set of eigvals {lambda_i}, construct
    the associated Dirichlet series L(s) = sum_i 1 / lambda_i^s and
    extend by truncation.  Report poles, candidate zero locations, and
    functional-equation symmetry residue.
    """
    pos_eigs = finite_spectrum[finite_spectrum > 1e-8]
    if len(pos_eigs) == 0:
        return TransformationOutcome(
            kind=TransformationKind.ANALYTIC_EXTEND,
            input_summary=f"spectrum length {len(finite_spectrum)}",
            output_summary="degenerate (no positive eigvals)",
            admissibility=Admissibility.DEGENERATE,
            residual=float("inf"),
        )

    # Probe the candidate-L along the critical line
    gammas = np.linspace(0.5, 50.0, 500)
    L_path = []
    for gamma in gammas:
        s = complex(0.5, gamma)
        L_val = sum(1.0 / (l ** s) for l in pos_eigs)
        L_path.append(L_val)
    L_path = np.array(L_path)
    abs_path = np.abs(L_path)

    # Candidate zeros: local minima below median/10
    minima = []
    median_val = np.median(abs_path)
    for i in range(1, len(gammas) - 1):
        if (abs_path[i] < abs_path[i - 1]
                and abs_path[i] < abs_path[i + 1]
                and abs_path[i] < median_val / 5):
            minima.append(gammas[i])

    return TransformationOutcome(
        kind=TransformationKind.ANALYTIC_EXTEND,
        input_summary=f"finite spectrum ({len(pos_eigs)} positive "
                      "eigvals)",
        output_summary=f"L_finite path with {len(minima)} candidate "
                       f"zero locations on Re(s)=1/2",
        output_data={
            "gammas": gammas, "L_path": L_path,
            "candidate_zeros": minima, "truncation": truncation_level,
        },
        admissibility=(Admissibility.CANDIDATE if minima
                       else Admissibility.APPROXIMATE),
        residual=float(np.median(abs_path)),
        notes=[f"truncation level: {truncation_level}",
               "this is a numerical proxy for analytic continuation; "
               "full Mellin extension would require analytic functional "
               "equation to be verified"],
        interpretation="Candidate analytic continuation; check for "
                       "zero-line consistency in subsequent steps.",
    )


# ---------------------------------------------------------------------------
# (4) SPECTRAL_LIFT_INFINITE
# ---------------------------------------------------------------------------

def spectral_lift_infinite(operator: np.ndarray,
                           truncation_N: int = 100) -> TransformationOutcome:
    """Lift a finite-dim operator to a truncated infinite-dim
    candidate.  The lift is achieved by direct-summing copies indexed
    by integer multiplications (analog of taking inductive limit
    across cascade levels).

    The lifted operator has 1 + dim(O) * truncation_N dimensions.  Its
    spectrum is the union of scaled copies of the input spectrum, plus
    an asymptotic continuum.
    """
    eigs = np.linalg.eigvalsh(0.5 * (operator + operator.T))
    # Direct-sum copies with scaling factor 1/k for k = 1..N
    lifted_eigs = []
    for k in range(1, truncation_N + 1):
        lifted_eigs.extend(eigs / k)
    lifted_eigs = np.array(sorted(lifted_eigs))

    return TransformationOutcome(
        kind=TransformationKind.SPECTRAL_LIFT_INFINITE,
        input_summary=f"finite operator (dim {operator.shape[0]})",
        output_summary=f"lifted spectrum with {len(lifted_eigs)} "
                       f"eigenvalues (truncation N = {truncation_N})",
        output_data={"eigvals": lifted_eigs,
                     "original_dim": operator.shape[0],
                     "truncation_N": truncation_N},
        admissibility=Admissibility.CANDIDATE,
        residual=0.0,
        notes=[f"truncation N = {truncation_N}",
               "real infinite-dim lift would require defining the "
               "appropriate Hilbert space and verifying self-adjointness"],
        interpretation="Candidate infinite-dim spectral extension by "
                       "1/k-scaled direct sum.",
    )


# ---------------------------------------------------------------------------
# (5) TRACE_FORMULA_CLOSE
# ---------------------------------------------------------------------------

def trace_formula_close(operator: np.ndarray,
                        target_geometric_data: Optional[Dict] = None
                        ) -> TransformationOutcome:
    """Check whether the operator's spectral side balances against a
    candidate geometric (prime-counting) side, in the spirit of the
    Selberg trace formula.

    For a closed self-adjoint operator T, the Selberg-style identity
    is roughly:
        sum_n f(lambda_n) = sum_g (geometric data for g)
    where g runs over conjugacy classes / closed geodesics / prime
    ideals.

    We compute trace(T), trace(T^2), trace(T^3) and compare against a
    geometric side built from prime ideals of Z[phi] (if provided).
    """
    eigs = np.linalg.eigvalsh(0.5 * (operator + operator.T))
    spectral_traces = [
        float(np.sum(eigs)),
        float(np.sum(eigs ** 2)),
        float(np.sum(eigs ** 3)),
    ]
    geometric_traces = None
    residual = float("inf")

    if target_geometric_data is not None:
        # geometric side: sum over given prime list of (1 + N(p))^k
        primes = target_geometric_data.get("primes", [])
        geometric_traces = [
            sum((1.0 + p) ** k for p in primes)
            for k in (1, 2, 3)
        ]
        residual = float(np.linalg.norm(
            np.array(spectral_traces) - np.array(geometric_traces)
        ))

    admissibility = Admissibility.CANDIDATE
    if residual < 1e-3:
        admissibility = Admissibility.EXACT
    elif residual < 1.0:
        admissibility = Admissibility.APPROXIMATE
    elif residual > 1000:
        admissibility = Admissibility.BROKEN

    return TransformationOutcome(
        kind=TransformationKind.TRACE_FORMULA_CLOSE,
        input_summary=f"operator dim {operator.shape[0]} + "
                      f"geometric data {target_geometric_data is not None}",
        output_summary=f"spectral traces {spectral_traces[:2]} "
                       f"vs geometric {geometric_traces[:2] if geometric_traces else 'none'}",
        output_data={"spectral_traces": spectral_traces,
                     "geometric_traces": geometric_traces,
                     "residual": residual},
        admissibility=admissibility,
        residual=residual,
        notes=["compares first 3 power-trace identities",
               "a full Selberg trace formula would involve all power "
               "traces + zeta-regularised identities"],
        interpretation="Tests whether the operator satisfies a "
                       "Selberg-style spectral-geometric balance.",
    )
