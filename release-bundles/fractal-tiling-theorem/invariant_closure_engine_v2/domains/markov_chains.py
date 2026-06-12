"""Calibration domain: Markov chains.  Reversible (detailed balance) -> real spectrum
-> SELF_ADJOINT in the stationary-weighted inner product.  Non-reversible ergodic ->
complex spectrum, contracts to stationary on the mean-zero subspace -> DISSIPATIVE.
We classify the action on the mean-zero subspace (deviation from stationarity)."""
import numpy as np
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from closure_mode_classifier import classify_closure


def stationary(P):
    w, V = np.linalg.eig(P.T)
    i = int(np.argmin(np.abs(w - 1)))
    pi = np.real(V[:, i]); pi = pi / pi.sum()
    return pi


def meanzero_action(P):
    """Project P onto the subspace orthogonal to the stationary direction, in the
    pi-weighted inner product, and return that operator (its spectral radius < 1 for
    ergodic chains)."""
    n = P.shape[0]
    pi = stationary(P)
    D = np.diag(np.sqrt(pi)); Di = np.diag(1 / np.sqrt(pi))
    S = D @ P @ Di                      # similarity to symmetric iff reversible
    # remove the stationary mode (sqrt(pi) is its left/right vector)
    v = np.sqrt(pi); v = v / np.linalg.norm(v)
    Pperp = np.eye(n) - np.outer(v, v)
    return Pperp @ S @ Pperp, S


def reversible_chain():
    # birth-death chain: reversible by construction (detailed balance) -> real spectrum
    P = np.array([[0.5, 0.5, 0.0, 0.0],
                  [0.25, 0.5, 0.25, 0.0],
                  [0.0, 0.25, 0.5, 0.25],
                  [0.0, 0.0, 0.5, 0.5]])
    return P


def nonreversible_chain():
    # directed cycle with noise: ergodic, NOT reversible -> complex spectrum
    P = np.array([[0.1, 0.8, 0.05, 0.05],
                  [0.05, 0.1, 0.8, 0.05],
                  [0.05, 0.05, 0.1, 0.8],
                  [0.8, 0.05, 0.05, 0.1]])
    return P


def run():
    out = {}
    for name, P in [("reversible_birth_death", reversible_chain()),
                    ("nonreversible_cycle", nonreversible_chain())]:
        M, S = meanzero_action(P)
        c = classify_closure(M, label=name)
        # reversibility test: S symmetric?
        sym_err = float(np.max(np.abs(S - S.T)))
        out[name] = dict(mode=c["closure_mode"], rho=c["rho"], real_spectrum=c["real_spectrum"],
                         reversible=bool(sym_err < 1e-9), sym_err=sym_err, note=c["note"])
    return out


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2, default=str))
