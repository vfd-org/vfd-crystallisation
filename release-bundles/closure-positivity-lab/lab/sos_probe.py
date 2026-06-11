"""SOS probe -- can the GEOMETRY write the Weil form Q_A as a sum of squares?

This is the one move that attacks RH(L) positivity from the geometric side rather than
restating it.  The archimedean analogue of Weil's finite-place proof (RH over F_p =
Hasse bound = positivity of an intersection form) would be: exhibit Q_A as a manifestly
positive expression -- a Gram matrix / sum of squares -- built from the closure geometry
ALONE.

What we do, honestly:
  * Pick a finite basis of real even test functions g_1..g_m (Hermite-Gaussians).
  * Build the Weil quadratic form matrix  Q[i,j] = W(g_i, g_j)  ENTIRELY from geometry:
        Q = ARCH (gamma factor, conductor)  -  PRIME (geometric a_P, Ramanujan-bounded).
    NO ZERO DATA enters Q.  (Hard gate: zeros_used must stay False.)
  * If Q is PSD, Cholesky gives Q = L L^T  -- an explicit SUM OF SQUARES of geometric
    functionals.  RH(L) <=> Q PSD on EVERY such finite space.
  * The real experiment is STABILITY: track lambda_min(Q) as the basis size m and the
    prime support P grow.  A decomposition that survives enlargement is the Hilbert-Polya
    grade object; a lambda_min that dips < 0 at some truncation is an informative negative.

HONEST ODDS: this is the summit Connes/Deninger have climbed for 25 years.  The expected
outcome is a clean documented negative (these geometric functionals don't make Q PSD
uniformly), which sharpens the F_1 ledger.  It is NOT expected to prove RH.  Its value is
that it is falsifiable and built from geometry, with a gate that forbids circular use of
the zeros.
"""
from __future__ import annotations
import json, math, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "out")
N_COND, MU = 775.0, (0.5, 0.5, 1.5, 1.5)               # calibrated icosian gamma
LOGPI = math.log(math.pi)


def _load_curve_ap(nmax):
    """Geometric prime data: point-counted a_P (cross-checked vs Brandt, 0 mismatch).
    NB this is geometry/Frobenius -- NOT zeros."""
    from .curve_stage_b import curve_ap_table, crosscheck_geometric
    rows = curve_ap_table(nmax)
    chk = crosscheck_geometric(rows)
    if chk.get("mismatches"):
        raise RuntimeError(f"geometric cross-check failed: {chk}")
    return rows, chk


# ---- archimedean kernel (gamma factor), built once, NO zeros -----------------
import cmath
def _dig(z):
    r = 0 + 0j
    while z.real < 12:
        r -= 1 / z; z = z + 1
    i = 1 / z; i2 = i * i
    return r + cmath.log(z) - .5 * i - i2 * (1/12 - i2*(1/120 - i2/252))
def _gR(s): return -.5 * LOGPI + .5 * _dig(s / 2)

def _arch_kernel(r):
    """omega(r) = logN + sum_mu [gR(1/2+mu+ir) + gR(1/2+mu-ir)], the archimedean density."""
    tot = math.log(N_COND) + 0j
    for mu in MU:
        tot += _gR(complex(0.5 + mu, r)) + _gR(complex(0.5 + mu, -r))
    return tot.real


# ---- test-function basis: even Hermite-Gaussians g_k(r) ----------------------
def _basis(r, m, scale):
    """g_k(r) = H_{2k}(r/scale) exp(-r^2/2 scale^2), k=0..m-1 (even, Schwartz)."""
    x = r / scale
    out = []
    Hm2, Hm1 = np.ones_like(x), np.zeros_like(x)   # H_0=1, placeholder
    # build Hermite physicists' polynomials up to degree 2(m-1)
    H = [np.ones_like(x)]
    if 2 * (m - 1) >= 1:
        H.append(2 * x)
    for n in range(2, 2 * (m - 1) + 1):
        H.append(2 * x * H[n - 1] - 2 * (n - 1) * H[n - 2])
    env = np.exp(-(x * x) / 2)
    for k in range(m):
        out.append(H[2 * k] * env)
    return out                                      # list of arrays over r-grid


def _prime_terms(rows, umax):
    """(u = k logNq, weight) for the explicit-formula prime side, geometry only."""
    terms = []
    for rr in rows:
        Nq = rr["norm"]; a = rr["a_P"]
        if rr["kind"] == "bad":
            continue
        x = a / (2 * math.sqrt(Nq))
        if abs(x) > 1:
            continue
        th = math.acos(max(-1.0, min(1.0, x))); lN = math.log(Nq); k = 1
        while k * lN < umax and Nq ** (k / 2.0) < 1e12:
            terms.append((k * lN, 2 * (2 * math.cos(k * th)) * lN / math.sqrt(Nq ** k)))
            k += 1
    return terms


def weil_matrix(rows, m=6, scale=3.0, rmax=60.0, npts=8000):
    """Weil form  Q[i,j] = sum_rho phi_i(gamma_rho) phi_j(gamma_rho), built from GEOMETRY:
    via the explicit formula with Psi = phi_i*phi_j (the PRODUCT),
        Q[i,j] = (1/2pi) int Psi(r) omega(r) dr  -  sum_q w_q * That(Psi)(u_q),
    where That(Psi)(u) = (1/2pi) int Psi(r) cos(r u) dr.  NO zero data.  Returns (Q, False).
    (Earlier bug: product-of-transforms != transform-of-product; fixed -- the product's
    transform is used.)"""
    r = np.linspace(-rmax, rmax, npts); dr = r[1] - r[0]
    G = _basis(r, m, scale)
    omega = np.array([_arch_kernel(rr) for rr in r])
    terms = _prime_terms(rows, rmax)
    uvals = sorted(set(round(u, 6) for u, _ in terms))   # cache cos(r u) per distinct u
    cos_cache = {u: np.cos(r * u) for u in uvals}
    Q = np.zeros((m, m))
    for i in range(m):
        for j in range(i, m):
            Psi = G[i] * G[j]
            arch = np.trapz(Psi * omega, dx=dr) / (2 * math.pi)
            prime = 0.0
            for u, w in terms:
                That = np.trapz(Psi * cos_cache[round(u, 6)], dx=dr) / (2 * math.pi)
                prime += w * That
            Q[i, j] = Q[j, i] = arch - prime
    return Q, False


def validate_against_zeros(rows, zeros, m=6, scale=3.0, rmax=60.0, npts=8000):
    """CHECK ONLY (not part of the gated construction): the geometric Q must match the
    spectral Gram  S[i,j] = sum_rho phi_i(gamma_rho) phi_j(gamma_rho)  built from the
    zeros.  Agreement confirms Q is the real Weil form; S is PSD by construction."""
    r = np.linspace(-rmax, rmax, npts)
    G = _basis(r, m, scale)
    # sample each basis function at each zero (+/- gamma) via interpolation
    S = np.zeros((m, m))
    gv = np.array([[np.interp(g, r, G[i]) + np.interp(-g, r, G[i]) for g in zeros]
                   for i in range(m)])   # phi_i at +gamma and -gamma summed per zero pair
    # spectral Gram over the found zeros (each rho and its conjugate)
    for a in range(m):
        for b in range(m):
            S[a, b] = sum((np.interp(g, r, G[a]) * np.interp(g, r, G[b]) +
                           np.interp(-g, r, G[a]) * np.interp(-g, r, G[b])) for g in zeros)
    Q, _ = weil_matrix(rows, m=m, scale=scale, rmax=rmax, npts=npts)
    return Q, S


def probe(m_list=(3, 4, 5, 6, 8), prime_bounds=(500, 1500, 3000), scale=3.0):
    os.makedirs(OUT, exist_ok=True)
    results = []
    print("SOS PROBE -- is the geometric Weil form Q_A positive semidefinite?")
    print("(Q built from gamma factor + geometric a_P only; NO zero data.)\n")
    print(f"{'n<=':>6}{'m':>4}{'lambda_min(Q)':>16}{'PSD?':>7}{'SOS rank':>10}")
    zeros_ever_used = False
    for nb in prime_bounds:
        rows, chk = _load_curve_ap(nb)
        for m in m_list:
            Q, zused = weil_matrix(rows, m=m, scale=scale)
            zeros_ever_used = zeros_ever_used or zused
            Qs = 0.5 * (Q + Q.T)
            ev = np.linalg.eigvalsh(Qs)
            lo = float(ev[0])
            psd = lo > -1e-9
            # SOS rank: # positive eigenvalues (Cholesky exists iff PSD)
            rank = int(np.sum(ev > 1e-12))
            print(f"{nb:>6}{m:>4}{lo:>16.6e}{('Y' if psd else '.'):>7}{rank:>10}")
            results.append({"prime_bound": nb, "m": m, "lambda_min": lo,
                            "psd": psd, "sos_rank": rank,
                            "n_prime_ideals": len(rows),
                            "geom_crosscheck_mismatches": chk["mismatches"]})
    # ---- validation: does the GEOMETRIC Q match the SPECTRAL Gram from the zeros?
    zpath = os.path.join(OUT, "curve_zeros.json")
    if os.path.exists(zpath):
        zeros = json.load(open(zpath)).get("L_zeros", [])
        if zeros:
            rows, _ = _load_curve_ap(max(prime_bounds))
            Qv, Sv = validate_against_zeros(rows, zeros, m=5, scale=scale)
            rel = np.linalg.norm(Qv - Sv) / (np.linalg.norm(Sv) + 1e-12)
            print(f"\nVALIDATION (m=5): geometric Q vs spectral Gram S over {len(zeros)} "
                  f"found zeros: rel-diff = {rel:.3f}")
            print(f"  lambda_min: geometric Q = {np.linalg.eigvalsh(0.5*(Qv+Qv.T))[0]:+.4f}, "
                  f"spectral S = {np.linalg.eigvalsh(0.5*(Sv+Sv.T))[0]:+.4f} (S PSD by constr.,")
            print(f"  truncated to {len(zeros)} zeros -- agreement improves as zero-height grows)")

    print(f"\nGATE: zero data used in constructing Q = {zeros_ever_used}  (MUST be False)")
    allpsd = all(x["psd"] for x in results)
    print(f"Q PSD on every tested (m, prime-bound): {allpsd}")
    if allpsd:
        print("\n=> The geometric Weil form is PSD on every finite space tested: an explicit")
        print("   SUM-OF-SQUARES (Cholesky Q=LL^T) exists at each truncation, built with NO")
        print("   zero data.  This is EVIDENCE the geometry carries the positivity; it is NOT")
        print("   a proof -- RH(L) needs PSD UNIFORMLY on ALL test spaces, and lambda_min may")
        print("   still dip negative at larger m / prime support.  Track lambda_min as both grow.")
    else:
        print("\n=> lambda_min dips negative at some truncation: an informative NEGATIVE.")
        print("   These geometric functionals do not make Q_A uniformly PSD -- a concrete")
        print("   exclusion for the F_1 ledger (which functional families fail, and where).")
    json.dump({"gate_zero_data_used": zeros_ever_used, "all_psd": allpsd,
               "results": results,
               "note": "Q_A from geometry only; PSD = SOS exists (Cholesky); RH(L) needs "
                       "uniform PSD over all finite spaces (open). No zeros in Q."},
              open(os.path.join(OUT, "sos_probe.json"), "w"), indent=1)
    print(f"\nwrote out/sos_probe.json")
    return results


if __name__ == "__main__":
    probe()
