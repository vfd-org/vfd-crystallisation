"""Self-adjoint finite-window test — the deeper mode.

For a finite transition system on states 1..N we build the deterministic
transition matrix T and search for a symmetric bilinear form B making T
self-adjoint:

    B T = T^T B          (equivalently  T^T B - B T = 0).

Vectorising B, this is the linear system

    (T^T (x) I  -  I (x) T^T) vec(B) = 0,

whose null space, intersected with the symmetric subspace, gives every
admissible B.  We return the residual ||B T - T^T B||, the signature of B, and
a verdict on whether the system admits a balanced hidden geometry.

Because the vectorised operator is N^2 x N^2, this is a dense O(N^6) solve; the
default guard caps N to keep it tractable (a 4-2-1 closed system is tiny).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, List, Optional

import numpy as np

from .collatz_closure import collatz_next

# Dense cap: the vectorised solve is O(N^6), so keep N small.  A closed
# finite Collatz window is tiny; 24 stays sub-second on commodity BLAS.
DEFAULT_MAX_SIZE = 24


@dataclass
class SelfAdjointResult:
    domain: str
    matrix_size: int
    residual_norm: float
    B_signature: str
    positive_definite: bool
    eigenvalues_B: List[float]
    verdict: str
    notes: List[str] = field(default_factory=list)


def collatz_transition_matrix(limit: int) -> np.ndarray:
    """Deterministic Collatz transition on states 1..limit.

    State i (0-indexed value i+1) maps to collatz_next(i+1).  Successors that
    leave the window are made absorbing (self-loop) so T stays square and
    every row has exactly one 1.
    """
    T = np.zeros((limit, limit), dtype=float)
    for i in range(limit):
        v = i + 1
        nxt = collatz_next(v)
        j = nxt - 1 if nxt <= limit else i  # clip escapes to a self-loop
        T[i, j] = 1.0
    return T


def _symmetric_self_adjoint_form(T: np.ndarray) -> Optional[np.ndarray]:
    """Return a non-trivial symmetric B with B T = T^T B, or None."""
    n = T.shape[0]
    I = np.eye(n)
    # M vec(B) = 0  where  M = kron(T^T, I) - kron(I, T^T)
    M = np.kron(T.T, I) - np.kron(I, T.T)
    # Constrain B symmetric: append rows enforcing vec(B - B^T) = 0.
    rows = []
    for i in range(n):
        for j in range(i + 1, n):
            r = np.zeros(n * n)
            r[i * n + j] = 1.0
            r[j * n + i] = -1.0
            rows.append(r)
    if rows:
        M = np.vstack([M, np.array(rows)])

    # Null space via SVD.
    _, s, vh = np.linalg.svd(M)
    tol = max(M.shape) * (s[0] if s.size else 1.0) * np.finfo(float).eps
    null_mask = np.concatenate([s <= tol, np.ones(vh.shape[0] - s.size, dtype=bool)])
    null_basis = vh[null_mask]
    if null_basis.shape[0] == 0:
        return None

    # Prefer a basis vector that is not (numerically) a scalar multiple of I.
    best = None
    for vec in null_basis:
        B = vec.reshape(n, n)
        B = 0.5 * (B + B.T)  # enforce symmetry exactly
        if np.linalg.norm(B) < 1e-12:
            continue
        off = np.linalg.norm(B - np.diag(np.diag(B)))
        if best is None or off > best[1]:
            best = (B, off)
    return best[0] if best is not None else None


def analyze(domain: str = "collatz", limit: int = 16,
            max_size: int = DEFAULT_MAX_SIZE) -> SelfAdjointResult:
    """Run the self-adjoint test on the named finite-window domain."""
    notes: List[str] = []
    if limit > max_size:
        notes.append(
            f"limit {limit} exceeds dense cap {max_size}; reduced to {max_size} "
            f"(vectorised solve is O(N^6))"
        )
        limit = max_size

    if domain == "collatz":
        T = collatz_transition_matrix(limit)
    else:
        raise ValueError(f"unknown domain '{domain}'")

    B = _symmetric_self_adjoint_form(T)

    if B is None:
        # No non-trivial symmetric form: report the identity baseline residual.
        residual = float(np.linalg.norm(T - T.T))
        return SelfAdjointResult(
            domain=domain,
            matrix_size=limit,
            residual_norm=residual,
            B_signature="none",
            positive_definite=False,
            eigenvalues_B=[],
            verdict="no non-trivial self-adjoint form found",
            notes=notes + ["||T - T^T|| reported as B=I baseline"],
        )

    residual = float(np.linalg.norm(B @ T - T.T @ B))
    eig = np.linalg.eigvalsh(B)
    eig_r = [round(float(e), 8) for e in eig]
    n_pos = int(np.sum(eig > 1e-9))
    n_neg = int(np.sum(eig < -1e-9))
    n_zero = len(eig) - n_pos - n_neg
    pos_def = n_neg == 0 and n_zero == 0

    if pos_def:
        signature = "positive-definite"
        verdict = "balanced geometry: T is self-adjoint w.r.t. a positive-definite B"
    elif n_zero > 0 and n_neg == 0:
        signature = "positive-semidefinite (singular)"
        verdict = "degenerate balanced form (B singular)"
    elif n_pos and n_neg:
        signature = f"indefinite ({n_pos}+, {n_neg}-, {n_zero}0)"
        verdict = "self-adjoint only under an indefinite (Krein) form"
    else:
        signature = "negative"
        verdict = "self-adjoint under a negative-definite form"

    return SelfAdjointResult(
        domain=domain,
        matrix_size=limit,
        residual_norm=residual,
        B_signature=signature,
        positive_definite=pos_def,
        eigenvalues_B=eig_r,
        verdict=verdict,
        notes=notes,
    )


def describe(r: SelfAdjointResult) -> str:
    eigs = r.eigenvalues_B
    if len(eigs) > 8:
        eig_str = ", ".join(f"{e:g}" for e in eigs[:8]) + ", ..."
    else:
        eig_str = ", ".join(f"{e:g}" for e in eigs)
    lines = [
        f"domain:        {r.domain}",
        f"matrix size:   {r.matrix_size} x {r.matrix_size}",
        f"residual ||BT - T^T B||: {r.residual_norm:.3e}",
        f"B signature:   {r.B_signature}",
        f"positive-def:  {r.positive_definite}",
        f"eig(B):        [{eig_str}]",
        f"verdict:       {r.verdict}",
    ]
    for n in r.notes:
        lines.append(f"note: {n}")
    return "\n".join(lines)
