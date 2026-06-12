"""
Candidate-Certificate Refuter  --  WO-VFD-CANDIDATE-CERTIFICATE-REFUTER-001

An honest REFUTER for proposed closure certificates at the infinity wall (RH / Collatz /
Navier-Stokes). It is skeptical by construction:

  * given a candidate certificate, it tries HARD to break it on finite truncations;
  * if it finds a failure -> REFUTED, with a concrete witness;
  * if it cannot -> SURVIVES-TRUNCATIONS, under a hard banner that this is EVIDENCE on
    finite cutoffs, NOT a proof. The infinite-limit step is the open problem.

It can REFUTE. It cannot CERTIFY any open conjecture. There is no code path that returns
"proved". (For Collatz we even have a theorem -- the rung grammar is the full shift -- that
no finite local certificate can exist, so every purely-local candidate SHOULD be refuted.)
"""
from __future__ import annotations

import math
import os
import sys
from dataclasses import dataclass, field
from typing import Any, Callable

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "positive_witness_operator", "src"))

BANNER = ("SURVIVES-TRUNCATIONS = evidence on finite cutoffs ONLY, NOT a proof. "
          "The infinite-limit step is the open problem and is not decidable by this "
          "finite harness. This tool refutes candidates; it never certifies a conjecture.")


@dataclass
class Verdict:
    candidate: str
    domain: str
    verdict: str                       # "REFUTED" | "SURVIVES-TRUNCATIONS"
    witness: Any = None                # the failing point, if refuted
    truncations: list = field(default_factory=list)
    detail: str = ""
    banner: str = BANNER

    @property
    def refuted(self) -> bool:
        return self.verdict == "REFUTED"


# --------------------------------------------------------------------------- #
#  generic predicate refuter                                                   #
# --------------------------------------------------------------------------- #
def refute_over(candidate: str, domain: str, items, predicate: Callable[[Any], tuple]):
    """predicate(item) -> (ok: bool, value). Refute on the first item where ok is False."""
    tested = []
    for it in items:
        ok, value = predicate(it)
        tested.append({"item": it, "value": value, "ok": bool(ok)})
        if not ok:
            return Verdict(candidate, domain, "REFUTED", witness={"item": it, "value": value},
                           truncations=tested,
                           detail=f"failed at {it!r} (value={value}).")
    return Verdict(candidate, domain, "SURVIVES-TRUNCATIONS", truncations=tested,
                   detail="no failure found on the tested truncations (NOT a proof).")


# --------------------------------------------------------------------------- #
#  RH: refute a Weil-positivity certificate                                    #
# --------------------------------------------------------------------------- #
def refute_rh(candidate: str = "real", cutoffs=((8, 1000), (12, 2000), (16, 3000)),
              tol: float = 1e-3) -> Verdict:
    """Candidate: 'the Weil explicit-formula quadratic form is PSD via this completion'.
    candidate in {'real' (correct arch), 'fake' (Gamma(s/3)), 'none' (no arch)}.
    Refuter: min eigenvalue of the finite Weil form D=A+P-R across (NC, P) truncations;
    REFUTED if D becomes indefinite (min eig < -tol) at any tested cutoff."""
    import witness_core as W
    arch = {"real": "real", "fake": "fake", "none": "none"}.get(candidate, "real")

    def pred(cut):
        NC, P = cut
        me = W.weil_form(NC=NC, P=P, arch=arch, primes="real")["min_eig"]
        return (me > -tol, round(me, 6))

    v = refute_over(f"RH:Weil-positivity[{candidate}]", "Riemann", list(cutoffs), pred)
    if not v.refuted:
        v.detail += (" The real completion stays PSD with a near-null mode (lambda_min -> 0+); "
                     "proving D>=0 for ALL admissible test functions in the limit IS RH "
                     "(Connes arithmetic site). Not decided here.")
    return v


# --------------------------------------------------------------------------- #
#  Collatz: refute a Lyapunov / monotone certificate                           #
# --------------------------------------------------------------------------- #
def _collatz_odd_step(n: int):
    m = 3 * n + 1
    a = (m & -m).bit_length() - 1
    return m >> a, a


def refute_collatz_lyapunov(V: Callable[[int], float], name: str = "V",
                            N: int = 200000, strict: bool = True) -> Verdict:
    """Candidate: 'V is a (strict) Lyapunov function for the 3n+1 odd-step map'
    i.e. V(T(n)) < V(n) for every odd n>1. Refuter: scan odd n in [3, N]; REFUTED on the
    first step where V does not strictly decrease (a concrete counterexample)."""
    def pred(n):
        nxt, _a = _collatz_odd_step(n)
        dv = V(nxt) - V(n)
        ok = (dv < 0) if strict else (dv <= 1e-12)
        return (ok, {"n": n, "next": nxt, "dV": round(float(dv), 6)})

    items = range(3, N, 2)
    v = refute_over(f"Collatz:Lyapunov[{name}]", "Collatz", items, pred)
    if not v.refuted:
        v.detail += (" NOTE: even a strict-decrease survivor on [3,N] is NOT a certificate: "
                     "the rung grammar is the full shift (Terras), so no FINITE-local Lyapunov "
                     "can settle the aperiodic infinite braid = the conjecture.")
    return v


def refute_collatz_numeric(N: int = 100000, max_steps: int = 100000) -> Verdict:
    """Candidate: 'every n <= N reaches 1' (pure numeric verification). Refuter: iterate;
    REFUTED if any n fails to reach 1 within max_steps. (Survives = verification, NOT proof.)"""
    def reaches_one(n0):
        n, s = n0, 0
        while n != 1 and s < max_steps:
            n = n // 2 if n % 2 == 0 else 3 * n + 1
            s += 1
        return (n == 1, s)

    def pred(n):
        ok, s = reaches_one(n)
        return (ok, {"n": n, "steps": s})

    v = refute_over("Collatz:all-reach-1", "Collatz", range(1, N + 1), pred)
    if not v.refuted:
        v.detail += (" This is NUMERIC VERIFICATION up to N, explicitly NOT a proof for all n.")
    return v


# --------------------------------------------------------------------------- #
#  Navier-Stokes (dyadic shell): refute a coercive-control certificate         #
# --------------------------------------------------------------------------- #
def _shell_capacity(nu, N=18, T=8.0, dt=2e-4):
    k = 2.0 ** np.arange(N); u = np.zeros(N); u[0] = 1.0; u[1] = 0.3; qs = []
    for _ in range(int(T / dt)):
        En = u * u; f = min(int(np.argmax(En)) + 1, N - 1)
        qs.append(2 * nu * k[f] ** 2 - abs(k[f] * u[f] * u[min(f + 1, N - 1)]) / (abs(u[f]) + 1e-30))
        du = np.zeros(N)
        du[1:-1] = k[1:-1] * (u[:-2] * u[1:-1] - u[1:-1] * u[2:]) - nu * k[1:-1] ** 2 * u[1:-1]
        du[0] = -k[0] * u[0] * u[1] - nu * k[0] ** 2 * u[0]
        du[-1] = k[-1] * u[-2] * u[-1] - nu * k[-1] ** 2 * u[-1]
        u = u + dt * du
        if not np.all(np.isfinite(u)) or np.max(np.abs(u)) > 1e6:
            break
    return float(np.mean(qs))


def refute_ns_coercive(nu_floor: float = 0.05,
                       nus=(0.2, 0.1, 0.05, 0.02, 0.01), tol: float = 1e-3) -> Verdict:
    """Candidate: 'for viscosity nu >= nu_floor the dyadic-shell capacity stays >= 0
    (dissipation dominates transfer)'. Refuter: test nus >= nu_floor; REFUTED if any has
    capacity < -tol."""
    def pred(nu):
        if nu < nu_floor:
            return (True, "below floor (not claimed)")
        q = _shell_capacity(nu)
        return (q > -tol, round(q, 4))

    v = refute_over(f"NS:coercive[nu>={nu_floor}]", "Navier-Stokes", list(nus), pred)
    if not v.refuted:
        v.detail += (" Survival on this caricature does NOT address 3D supercriticality, "
                     "where the controlled norm's sign is genuinely undetermined.")
    return v
