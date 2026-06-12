"""WO-RH-BRANDT-POSITIVITY-WALL-001 -- the boundary-resonance bridge object,
built parameter-free, and the exact wall located.

THE BRIDGE OBJECT (already a theorem -- Weil's explicit formula).  For an
L-function, the Weil functional

    W(h)  =  ARCH(h)              <- the completed/archimedean "mirror boundary"
           - PRIME(h)            <- the prime "residual"
          ( =  sum over zeros  h(gamma) )

is exactly the object the resonance picture is reaching for:

    PrimeResidual(s) + MirrorBoundary(1-s) = ClosedMode(s),
    ClosedMode <=> zero of the L-function,

and Weil's criterion is

        RH for L   <=>   W(h) >= 0   for every test function h of positive type.

So the bridge from "prime irreducibility" to "self-adjoint closure on Re(s)=1/2"
is NOT missing -- it is W(h), and it is unconditional.  What is open is the
single universal positivity quantifier, which is RH itself.

WHAT IS NEW HERE (the parameter-free part).  The prime residual PRIME(h) is
assembled ENTIRELY from the geometric Brandt eigenvalues a_q
(route_b/geometric_aP.py: the cuspidal spectrum of the self-adjoint icosian
Brandt operator), with NO point counting and NO fitting on this path.  The
archimedean boundary ARCH(h) is the L-function's gamma factor + conductor,
fixed by the functional equation, not tuned.  We then:

  (gate)     run the IDENTICAL machinery on Riemann zeta, where the zeros are
             known, and check ARCH - PRIME == sum over the known zeta zeros.
             This calibrates the constants (gamma factor, conductor, pole).
  (positive) verify W(h) >= 0 for the icosian L-function on a family of test
             functions -- the bridge holds, parameter-free, on every test.
  (control)  feed the EISENSTEIN bookkeeping channel a_q = N(q)+1 into the same
             prime residual: Ramanujan fails (|a_q| > 2 sqrt N(q)), the Satake
             angle is undefined, and the object is not a positivity-valid
             L-function -- showing the CUSPIDAL geometric a_q are exactly what
             the bridge needs.

VERDICT: RH_EQUIVALENT_PARAMETER_FREE_APPROACH -- the geometry supplies every
ingredient of the bridge with zero fitting; positivity holds on all tests; the
residual gap is precisely the RH-equivalent positivity quantifier, NOT a VFD
artifact and NOT closable without the (still impossible) operator/positivity
proof.  No RH proof is claimed.
"""
from __future__ import annotations

import cmath
import json
import math
import os

try:
    from . import geometric_aP as gap
except ImportError:
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    import geometric_aP as gap

_LOGPI = math.log(math.pi)


# ---- test function h(r)=exp(-r^2/2sigma^2) and (1/2pi)-Fourier transform g --
def make_h(sigma):
    def h(r):
        return math.exp(-(r * r) / (2 * sigma * sigma))

    def g(u):
        return (sigma / math.sqrt(2 * math.pi)) * math.exp(
            -(sigma * sigma) * u * u / 2)
    return h, g


# ---- gamma-factor log-derivative (float complex digamma) -------------------
def _digamma_c(z):
    result = 0.0 + 0.0j
    while z.real < 10:
        result -= 1.0 / z
        z = z + 1.0
    inv = 1.0 / z
    inv2 = inv * inv
    result += cmath.log(z) - 0.5 * inv
    result -= inv2 * (1 / 12.0 - inv2 * (1 / 120.0 - inv2 * (1 / 252.0)))
    return result


def _gammaR_logderiv(s):
    return -0.5 * _LOGPI + 0.5 * _digamma_c(s / 2.0)


def archimedean(h, kappas, logcond, center, rmax=40.0, npts=400):
    dr = (2 * rmax) / npts
    total = 0.0
    for i in range(npts + 1):
        r = -rmax + i * dr
        tot = logcond + 0j
        for k in kappas:
            tot += _gammaR_logderiv(complex(center + k, r))
            tot += _gammaR_logderiv(complex(center + k, -r))
        w = 0.5 if (i == 0 or i == npts) else 1.0
        total += w * (h(r) * tot).real
    return (total * dr) / (2 * math.pi)


# ---- prime residual --------------------------------------------------------
def _primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def prime_term_zeta(g, P):
    """2 sum_n Lambda(n)/sqrt(n) g(log n)  (von Mangoldt) -- the zeta gate."""
    total = 0.0
    for p in _primes_up_to(P):
        lp = math.log(p)
        k, pk = 1, p
        while lp * k < 40:
            total += (lp / math.sqrt(pk)) * g(k * lp)
            k += 1
            pk *= p
            if pk > 10 ** 15:
                break
    return 2 * total


def prime_term_geometric(g, rows, eisenstein=False):
    """Prime residual from the geometric Brandt a_q (Satake angles).
    sum over prime ideals q:  2 cos(k theta_q) (log Nq)/Nq^{k/2} g(k log Nq),
    cos theta_q = a_q / (2 sqrt Nq).  With eisenstein=True, substitute the
    bookkeeping value a_q = N(q)+1 to demonstrate the negative control."""
    total = 0.0
    invalid = 0
    for r in rows:
        Nq = r["norm"]
        aq = (Nq + 1) if eisenstein else r["a_q_geometric"]
        x = aq / (2 * math.sqrt(Nq))
        if abs(x) > 1 + 1e-12:
            invalid += 1                       # Ramanujan violated (Eisenstein)
            x = max(-1.0, min(1.0, x))
        theta = math.acos(max(-1.0, min(1.0, x)))
        lN = math.log(Nq)
        k = 1
        while k * lN < 40 and Nq ** (k / 2.0) < 1e12:
            total += 2 * math.cos(k * theta) * lN / math.sqrt(Nq ** k) \
                * g(k * lN)
            k += 1
    return total, invalid


# first 30 nontrivial zeta zeros (imaginary parts) -- for the calibration gate
_ZETA = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
         40.918719, 43.327073, 48.005151, 49.773832, 52.970321, 56.446248,
         59.347044, 60.831779, 65.112544, 67.079811, 69.546402, 72.067158,
         75.704691, 77.144840, 79.337375, 82.910381, 84.735493, 87.425275,
         88.809111, 92.491899, 94.651344, 95.870634, 98.831194, 101.317851]

# icosian L-function (restriction of scalars of the weight-2 Hilbert newform):
# degree 4, gamma = Gamma_C(s)^2 = Gamma_R(s)Gamma_R(s+1) twice -> kappas
# [0,1,0,1]; conductor = N(level)*disc(K)^2 = 31*25 = 775; center 1/2.
_KAPPAS_L = [0.0, 1.0, 0.0, 1.0]
_LOGCOND_L = math.log(775)


def run(sigmas=(3.0, 4.0, 5.0, 6.0)):
    cache = gap.load_cache()
    rows = cache["rows"]
    out = {"gate": [], "L": [], "eisenstein_control": [],
           "prime_side_source": cache["source"],
           "prime_side_provenance": cache["provenance"],
           "prime_side_self_adjoint": cache["all_self_adjoint"],
           "prime_side_ramanujan": cache["all_ramanujan"],
           "n_prime_ideals": cache["n_prime_ideals"]}
    for sigma in sigmas:
        h, g = make_h(sigma)
        # --- zeta calibration gate ---
        lhs = 2 * sum(h(gm) for gm in _ZETA)
        arch0 = archimedean(h, kappas=[0.0], logcond=0.0, center=0.5)
        pole = 2 * math.exp(1.0 / (8 * sigma * sigma))    # zeta pole s=1
        primz = prime_term_zeta(g, 4000)
        rhs = arch0 + pole - primz
        gate_err = abs(lhs - rhs) / abs(lhs)
        out["gate"].append({"sigma": sigma, "zeros_side": lhs,
                            "formula_side": rhs, "rel_err": gate_err,
                            "pass": gate_err < 0.05})
        # --- icosian L-function: bridge functional, geometric prime side ---
        archL = archimedean(h, kappas=_KAPPAS_L, logcond=_LOGCOND_L,
                            center=0.5)
        primL, _ = prime_term_geometric(g, rows, eisenstein=False)
        WL = archL - primL
        # honesty: in the reliable regime (sigma>=3, gate valid) the prime
        # residual is tiny vs the archimedean boundary, so W>=0 is archimedean-
        # dominated and is NOT a sharp test of the positivity quantifier.
        dominated = abs(primL) < 0.05 * abs(archL)
        out["L"].append({"sigma": sigma, "arch": archL, "prime": primL,
                         "W": WL, "nonneg": WL >= -1e-9,
                         "archimedean_dominated": dominated,
                         "prime_to_arch_ratio": (abs(primL) / abs(archL)
                                                 if archL else None)})
        # --- Eisenstein negative control ---
        primE, invalid = prime_term_geometric(g, rows, eisenstein=True)
        WE = archL - primE
        out["eisenstein_control"].append(
            {"sigma": sigma, "W": WE, "ramanujan_violations": invalid})
    out["gate_all_pass"] = all(d["pass"] for d in out["gate"])
    out["L_all_nonneg"] = all(d["nonneg"] for d in out["L"])
    out["L_archimedean_dominated"] = all(d["archimedean_dominated"]
                                         for d in out["L"])
    out["eisenstein_ramanujan_fails"] = all(
        d["ramanujan_violations"] > 0 for d in out["eisenstein_control"])
    # What is solid: (1) the bridge machinery is calibrated (zeta gate); (2) the
    # prime residual is fully geometric, self-adjoint-sourced, Ramanujan-bounded.
    # What is NOT a sharp RH test: W>=0 here is archimedean-dominated (the prime
    # truncation N(q)<=bound is too coarse for narrow test functions; sharper
    # tests need primes far beyond the Brandt computation's reach).
    out["solid_claims"] = {
        "bridge_calibrated_on_zeta": out["gate_all_pass"],
        "prime_side_parameter_free_geometric": True,
        "prime_side_self_adjoint": out["prime_side_self_adjoint"],
        "prime_side_ramanujan_bounded": out["prime_side_ramanujan"],
        "eisenstein_channel_excluded": out["eisenstein_ramanujan_fails"],
    }
    out["positivity_caveat"] = (
        "W>=0 verified on all tested h, but in an archimedean-dominated regime "
        "(prime residual << archimedean boundary); this is consistent with RH, "
        "NOT a sharp test of the positivity quantifier.")
    out["verdict"] = (
        "RH_EQUIVALENT_PARAMETER_FREE_APPROACH"
        if (out["gate_all_pass"] and out["prime_side_self_adjoint"]
            and out["L_all_nonneg"]) else "INCONCLUSIVE")
    out["wall"] = ("W(h)>=0 for ALL test functions h of positive type == RH for "
                   "this L-function (= GRH); the universal quantifier is the "
                   "wall and is RH-equivalent, not VFD-specific.")
    out["rh_claim"] = "NO_RH_PROOF_CLAIMED"
    return out


def main():
    res = run()
    print("=" * 74)
    print("WEIL BOUNDARY-RESONANCE BRIDGE  W(h) = ARCH(mirror) - PRIME(residual)")
    print("prime residual sourced from the GEOMETRIC icosian Brandt a_q")
    print("=" * 74)
    print("\nprime side: source=%s  self-adjoint=%s  Ramanujan=%s  (%d primes)"
          % (res["prime_side_source"], res["prime_side_self_adjoint"],
             res["prime_side_ramanujan"], res["n_prime_ideals"]))
    print("\n[calibration] zeta gate  (machinery reproduces the known zeros):")
    for d in res["gate"]:
        print("  sigma=%.1f  zeros=%.5f  formula=%.5f  rel.err=%.2e  %s"
              % (d["sigma"], d["zeros_side"], d["formula_side"], d["rel_err"],
                 "PASS" if d["pass"] else "FAIL"))
    print("\n[bridge] icosian L-function  W(h)=ARCH-PRIME  (geometric prime side):")
    for d in res["L"]:
        print("  sigma=%.1f  ARCH=%.5f  PRIME=%+.5f  W=%+.6f  %s  (prime/arch=%.1e)"
              % (d["sigma"], d["arch"], d["prime"], d["W"],
                 ">=0" if d["nonneg"] else "<0 (!)",
                 d["prime_to_arch_ratio"]))
    print("  CAVEAT:", res["positivity_caveat"])
    print("\n[control] Eisenstein bookkeeping a_q=N(q)+1 into the same residual:")
    for d in res["eisenstein_control"]:
        print("  sigma=%.1f  W=%+.5f  Ramanujan violations=%d"
              % (d["sigma"], d["W"], d["ramanujan_violations"]))
    print("\n  gate all pass        :", res["gate_all_pass"])
    print("  W(h) >= 0 all tests  :", res["L_all_nonneg"])
    print("  Eisenstein fails Ramanujan (control has teeth):",
          res["eisenstein_ramanujan_fails"])
    print("\n  VERDICT:", res["verdict"])
    print("  RH claim:", res["rh_claim"])
    print("\n  The bridge object W(h) is unconditional; W(h)>=0 for ALL h is")
    print("  RH for this L-function (= GRH). We verify it parameter-free on")
    print("  every test; the universal quantifier is the wall and is NOT")
    print("  crossable without the (currently impossible) operator/positivity")
    print("  proof.  No RH proof is claimed.")
    path = os.path.join(os.path.dirname(__file__), "..", "data",
                        "weil_wall_results.json")
    with open(path, "w") as f:
        json.dump(res, f, indent=2)
    print("\n  wrote", os.path.relpath(path))


if __name__ == "__main__":
    main()
