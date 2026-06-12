"""
WO-VFD-TRIAD-CLOSURE-CROSSDOMAIN-001  --  domain-agnostic closure-test engine.

ONE abstract object, reused verbatim across domains:

    ClosureProblem = (X, T, tau, theta, B, dX, Q)

      X      state space (described, not enumerated)
      T      transition / step / evolution rule        x -> T(x)
      tau    triad projection      tau: X -> {A,B,C}
      theta  phase map             theta: X -> S^1
      B      candidate measurement form (symmetrizer)  -- when T is a matrix
      dX     boundary / closure target
      Q      closure capacity along a trajectory   (Q = compression - expansion)

The engine supplies the four reusable diagnostics; each domain plugs in T/tau/theta
and emphasises whichever diagnostic is natural to it.  The DEFINITIONS never change.

    D_self  self-adjoint residual        ||B T - T^T B||      (does a hidden geometry balance the step?)
    D_phase phase-closure residual        dist(theta(T^k x), theta(x))  over closure window
    D_triad triad-cycle admissibility     tau-sequence obeys a 3-phase grammar
    D_Q     capacity drift                 mean of q_i = compression_i - expansion_i

Classification from the SAME rule everywhere:
    Qbar > 0   -> stable closure   (braid folds inward)
    Qbar = 0   -> critical boundary
    Qbar < 0   -> escape / leakage

NO domain is allowed to use its known answer (zeros, the number 1, blow-up time)
inside T/tau/theta/Q.  Known answers appear ONLY in validation.
This file proves NOTHING; it is a measurement instrument.
"""
import numpy as np


# --------------------------------------------------------------------------- #
#  D_self : self-adjoint residual + symmetrizer search                         #
# --------------------------------------------------------------------------- #
def symmetrizer(T, tol=1e-9):
    """
    Find a symmetric B with B T = T^T B  (i.e. BT symmetric), then report whether
    a *positive-definite* such B exists.

    Math fact (form-relativity of self-adjointness): a real matrix T admits a PD B
    with BT symmetric  <=>  T is real-diagonalizable with real spectrum (T is
    'symmetrizable').  So this is a genuine, non-circular structural test:
    it asks whether the step rule has a hidden measurement geometry that balances
    forward and reflected motion.

    Returns dict(B, residual, pd, real_spectrum, min_eig_B).
    """
    T = np.asarray(T, float)
    n = T.shape[0]
    # Solve for symmetric B in the nullspace of the linear map B |-> B T - T^T B.
    # Build the operator on the space of symmetric matrices.
    idx = [(i, j) for i in range(n) for j in range(i, n)]
    def vec_to_sym(v):
        M = np.zeros((n, n))
        for k, (i, j) in enumerate(idx):
            M[i, j] = v[k]; M[j, i] = v[k]
        return M
    A = np.zeros((n * n, len(idx)))
    for k, (i, j) in enumerate(idx):
        E = np.zeros((n, n)); E[i, j] = 1; E[j, i] = 1
        A[:, k] = (E @ T - T.T @ E).reshape(-1)
    # nullspace
    U, s, Vt = np.linalg.svd(A)
    null = Vt[np.sum(s > tol * max(1.0, s[0] if s.size else 1.0)):]
    # search the nullspace for a PD representative
    best = None
    if null.shape[0] > 0:
        # try each basis vector and a few random combos; keep the most-PD
        cands = list(null) + [null.sum(0)] + [null[0] - null[-1]] if null.shape[0] > 1 else list(null)
        for c in cands:
            B = vec_to_sym(c)
            if np.trace(B) < 0:
                B = -B
            ev = np.linalg.eigvalsh(B)
            mn = float(ev.min())
            if best is None or mn > best[1]:
                best = (B, mn)
    ev_T = np.linalg.eigvals(T)
    real_spec = float(np.max(np.abs(ev_T.imag))) < 1e-7
    if best is None:
        return dict(B=None, residual=None, pd=False, real_spectrum=real_spec,
                    min_eig_B=None, dim_null=int(null.shape[0]))
    B, mn = best
    res = float(np.max(np.abs(B @ T - T.T @ B)))
    return dict(B=B, residual=res, pd=bool(mn > 1e-9), real_spectrum=real_spec,
                min_eig_B=mn, dim_null=int(null.shape[0]))


def isometry_form(T, tol=1e-7):
    """
    Find a PD B with T^T B T = B  (T is a B-ISOMETRY: it preserves the form B).

    This is the OTHER closure mode, distinct from symmetrizer():
      - symmetrizer  (BT = T^T B): real spectrum -> monotone/contractive closure
      - isometry     (T^T B T = B): spectrum on the unit circle -> the phase RETURNS
    A triad 3-cycle / rotation closes via THIS test (not self-adjointness): its
    eigenvalues are on the unit circle, so it is B-orthogonal, not B-self-adjoint.

    Solve the linear system in symmetric B; report whether a PD solution exists.
    Returns dict(B, residual, pd, on_unit_circle, min_eig_B, dim_null).
    """
    T = np.asarray(T, float)
    n = T.shape[0]
    ev = np.linalg.eigvals(T)
    on_circle = float(np.max(np.abs(np.abs(ev) - 1.0))) < 1e-7
    # Weyl/unitarian construction: if T has finite order m, B = (1/m) sum (T^k)^T T^k
    # is guaranteed PD and exactly T-invariant.  This is the canonical invariant form.
    order = None
    Pk = np.eye(n)
    for m in range(1, 5000):
        Pk = Pk @ T
        if np.max(np.abs(Pk - np.eye(n))) < 1e-7:
            order = m; break
    if order is not None:
        B = np.zeros((n, n)); Q = np.eye(n)
        for _ in range(order):
            B += Q.T @ Q; Q = Q @ T
        B /= order
        mn = float(np.linalg.eigvalsh(B).min())
        res = float(np.max(np.abs(T.T @ B @ T - B)))
        return dict(B=B, residual=res, pd=bool(mn > 1e-9), on_unit_circle=on_circle,
                    min_eig_B=mn, finite_order=order)
    # infinite order: solve the linear system for a symmetric invariant form
    idx = [(i, j) for i in range(n) for j in range(i, n)]
    def vec_to_sym(v):
        M = np.zeros((n, n))
        for k, (i, j) in enumerate(idx):
            M[i, j] = v[k]; M[j, i] = v[k]
        return M
    A = np.zeros((n * n, len(idx)))
    for k, (i, j) in enumerate(idx):
        Ee = np.zeros((n, n)); Ee[i, j] = 1; Ee[j, i] = 1
        A[:, k] = (T.T @ Ee @ T - Ee).reshape(-1)
    U, s, Vt = np.linalg.svd(A)
    null = Vt[np.sum(s > tol * max(1.0, s[0] if s.size else 1.0)):]
    best = None
    for c in (list(null) + [null.sum(0)] if null.shape[0] else []):
        B = vec_to_sym(c)
        if np.trace(B) < 0:
            B = -B
        mn = float(np.linalg.eigvalsh(B).min())
        if best is None or mn > best[1]:
            best = (B, mn)
    if best is None:
        return dict(B=None, residual=None, pd=False, on_unit_circle=on_circle,
                    min_eig_B=None, finite_order=None)
    B, mn = best
    res = float(np.max(np.abs(T.T @ B @ T - B)))
    return dict(B=B, residual=res, pd=bool(mn > 1e-9), on_unit_circle=on_circle,
                min_eig_B=mn, finite_order=None)


# --------------------------------------------------------------------------- #
#  D_phase : phase-closure residual                                            #
# --------------------------------------------------------------------------- #
def phase_closure_residual(theta_seq, window):
    """Smallest angular distance between theta(x_0) and theta(x_k) for k in window.
    0 => the phase returns (closes); ~pi => maximal leakage."""
    t0 = theta_seq[0]
    best = np.pi
    for k in window:
        if k < len(theta_seq):
            d = abs((theta_seq[k] - t0 + np.pi) % (2 * np.pi) - np.pi)
            best = min(best, d)
    return float(best)


# --------------------------------------------------------------------------- #
#  D_triad : triad-cycle admissibility                                         #
# --------------------------------------------------------------------------- #
def triad_grammar_score(tau_seq):
    """Fraction of steps that advance the 3-phase cycle A->B->C->A (mod 3).
    1.0 => perfectly cyclic triad braid; ~0.33 => no triad structure (random)."""
    if len(tau_seq) < 2:
        return 0.0
    good = sum(1 for a, b in zip(tau_seq, tau_seq[1:]) if (b - a) % 3 == 1)
    return good / (len(tau_seq) - 1)


# --------------------------------------------------------------------------- #
#  D_Q : capacity drift  (the universal scalar)                                #
# --------------------------------------------------------------------------- #
def capacity_drift(q_steps):
    """Qbar = mean local capacity.  >0 stable, ~0 critical, <0 escape."""
    q = np.asarray(q_steps, float)
    return dict(Qbar=float(q.mean()), Qstd=float(q.std()),
                Qcum_final=float(q.sum()), n=int(q.size))


def classify(Qbar, eps=1e-3):
    if Qbar > eps:
        return "STABLE-CLOSURE"
    if Qbar < -eps:
        return "ESCAPE-LEAKAGE"
    return "CRITICAL-BOUNDARY"
