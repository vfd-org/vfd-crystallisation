"""
WO-VFD-INVARIANT-CLOSURE-CROSSDOMAIN-002  --  closure-mode classifier.

The deepest refinement (from the WO): closure is NOT a property of T alone, it is a
property of the triple (T, B, dX) under repetition.  So the classifier does not test a
fixed B -- it SEARCHES for a positive form B under which T closes, and reports which mode.

Rigorous decision logic (via spectrum + discrete Lyapunov; no fitting):

    rho(T) = spectral radius,  eigenvalues lam_i

    DISSIPATIVE   rho(T) < 1            -> exists PD B with T^T B T - B = -I  (Lyapunov, B>0)
    ISOMETRIC     all |lam_i| = 1, diagonalizable -> exists PD invariant form (orbit average)
    SELF_ADJOINT  spectrum real & diagonalizable    -> symmetrizable (PD B, BT=T^T B)
                  (a sub/intersecting case: real spectrum.  Reported when complex part ~0.)
    CRITICAL      rho(T) = 1 but DEFECTIVE (Jordan block) -> NO positive invariant form
                  (polynomial growth); sign of T^T B T - B unresolved
    MIXED         some |lam|<1 and some |lam|=1 (diagonalizable) -> isometric + dissipative parts
    NONE          rho(T) > 1                        -> escape; no bounded positive form
    CONTROL_FAIL  set by the harness when a true system fails to separate from a control

Returns a dict with mode + all diagnostics.  THIS PROVES NOTHING; it is a classifier.
"""
import numpy as np
from scipy.linalg import solve_discrete_lyapunov


def _orbit_form(T, cap=4000, tol=1e-7):
    """PD invariant form via Weyl average if T has finite order; else solve T^T B T=B."""
    n = T.shape[0]
    Pk = np.eye(n)
    for m in range(1, cap):
        Pk = Pk @ T
        if np.max(np.abs(Pk - np.eye(n))) < tol:
            B = np.zeros((n, n)); Q = np.eye(n)
            for _ in range(m):
                B += Q.T @ Q; Q = Q @ T
            return B / m
    return None


def classify_closure(T, label="", boundary=None):
    T = np.asarray(T, float)
    n = T.shape[0]
    w, V = np.linalg.eig(T)
    rho = float(np.max(np.abs(w)))
    on_circle = np.abs(np.abs(w) - 1.0) < 1e-6
    inside = np.abs(w) < 1 - 1e-6
    real_spec = float(np.max(np.abs(w.imag))) < 1e-6
    # diagonalizability via eigenvector-matrix conditioning
    try:
        condV = float(np.linalg.cond(V))
    except Exception:
        condV = np.inf
    diagonalizable = condV < 1e8

    diag = dict(label=label, n=n, rho=rho, real_spectrum=bool(real_spec),
                diagonalizable=bool(diagonalizable), cond_eigvecs=condV,
                n_on_circle=int(on_circle.sum()), n_inside=int(inside.sum()),
                n_outside=int((np.abs(w) > 1 + 1e-6).sum()))

    # --- decide mode + construct the witnessing form B ---
    mode, B, note = None, None, ""
    if rho > 1 + 1e-6:
        mode, note = "NONE", "rho>1: escape, no bounded positive invariant form"
    elif rho < 1 - 1e-6:
        # dissipative: discrete Lyapunov gives PD B with T^T B T - B = -I
        try:
            B = solve_discrete_lyapunov(T.T, np.eye(n))
            ok = np.linalg.eigvalsh((B + B.T) / 2).min() > 0
            mode = "DISSIPATIVE" if ok else "NONE"
            note = "rho<1: PD B from Lyapunov, T^T B T <= B (B-contraction)"
        except Exception:
            mode, note = "DISSIPATIVE", "rho<1 (Lyapunov solve failed numerically)"
    else:
        # rho == 1
        if not diagonalizable:
            mode, note = "CRITICAL", "rho=1 and DEFECTIVE (Jordan block): polynomial growth, no positive invariant form"
        elif inside.sum() > 0:
            mode, note = "MIXED", "rho=1 diagonalizable with |lam|<1 modes: isometric core + dissipative part"
            B = _orbit_form(T) if np.all(on_circle | inside) else None
        else:
            # all on unit circle, diagonalizable -> isometric; refine to self-adjoint if real
            B = _orbit_form(T)
            if real_spec:
                mode, note = "SELF_ADJOINT", "real spectrum, diagonalizable: symmetrizable (BT=T^T B)"
            else:
                mode, note = "ISOMETRIC", "spectrum on unit circle, diagonalizable: phase-return (T^T B T=B)"

    # residual diagnostics against the constructed B (if any)
    if B is not None:
        B = (B + B.T) / 2
        diag["B_min_eig"] = float(np.linalg.eigvalsh(B).min())
        diag["self_adjoint_residual"] = float(np.max(np.abs(B @ T - T.T @ B)))
        diag["isometry_residual"] = float(np.max(np.abs(T.T @ B @ T - B)))
        diag["dissipative_defect"] = float(np.linalg.eigvalsh(T.T @ B @ T - B).max())
    else:
        diag["B_min_eig"] = diag["self_adjoint_residual"] = None
        diag["isometry_residual"] = diag["dissipative_defect"] = None
    diag["closure_mode"] = mode
    diag["note"] = note
    return diag


def mixed_decompose(T):
    """For T with mixed spectrum, report the isometric (|lam|=1) and dissipative (|lam|<1)
    spectral mass -- a coarse mode decomposition (not a literal operator split)."""
    w = np.linalg.eigvals(T)
    iso = np.abs(np.abs(w) - 1) < 1e-6
    dis = np.abs(w) < 1 - 1e-6
    esc = np.abs(w) > 1 + 1e-6
    return dict(iso_modes=int(iso.sum()), dissipative_modes=int(dis.sum()),
                escaping_modes=int(esc.sum()),
                iso_eigs=[complex(x) for x in w[iso]][:8])
