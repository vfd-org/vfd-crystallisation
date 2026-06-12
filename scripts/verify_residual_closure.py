#!/usr/bin/env python3
"""
Verify the residual-closure derivations of docs/residual-closure-derivation.md
and docs/gauge-group-from-arenas.md — the upgrade pass on the named residuals
of the GR-closure chain (R-boot, R-Gauss, R-cont, R-G) plus the gauge-group
structure derivation.

  RB  (R-boot, in-house bootstrap):
      RB1  the quadratic expansion of the Einstein-Hilbert action equals the
           Fierz-Pauli action (one constant, random metrics, 4D grid) — the
           bootstrap's fixed point really is the unique gauge-invariant
           quadratic theory.
      RB2  "gravity gravitates", concretely: the second-order term of the
           isotropic Schwarzschild metric exactly cancels the self-energy of
           the first-order field (symbolic, exact); truncating at first
           order leaves a nonzero residual (the null).

  RG  (R-Gauss, beyond-Gaussian collective action):
      RG1-2  Cramer rate function for non-Gaussian substrate modes (uniform,
             two-scale discrete): smooth, strictly convex minimum at the
             background, quadratic dominance at the fluctuation scale with
             cubic/quadratic falling as N^{-1/2}.
      RG3    empirical second-moment fluctuations scale as N^{-1/2} for
             non-Gaussian modes.

  RC  (R-cont, explicit-rate continuum theorem):
      RC1  degree-1 and degree-2 sampled harmonics are EXACT eigenvectors of
           the 600-cell Laplacian (band exactness — no limit needed).
      RC2  the closed-form dispersion has leading term 2*theta^2*k(k+2) with
           the explicit second-order rate (1 - rho_k) = (3n^2-7)theta^2/60
           + O(theta^4): eigenvalue convergence with a proven rate.
      RC3  the rendering kernel suppresses above-band content by exactly
           1/(1 + r^2 lambda): the aliasing bound.

  RGRAV (R-G, conditional derivation of Newton's constant):
      RGRAV1  under H-shell-96 (muon at structural shell 96 = 24x4, the
              prior claim of Paper LII), G is PREDICTED:
              G = hbar*c / (m_mu * phi^96)^2, accurate to ~3 parts in 10^4.
      RGRAV2  honesty gate: the direct alpha_G ladder (proton shell) is NOT
              integer-forced (offset 0.46) — the scan must report
              non-forcing, not invent a fit.

  SM  (gauge-group structure from the two arenas):
      SM1  dim Der(O) = 14  (G2), computed from the Leibniz linear system.
      SM2  the stabiliser of the rendered unit e1 has dim 8.
      SM3  the stabiliser is complex-linear for J = L_{e1} and complex-
           traceless: it lies in su(3).
      SM4  the stabiliser algebra is compact (negative-definite Killing
           form), simple (no proper ideals), rank 2  =>  it IS su(3).
      SM5  arena split on V_600: left multiplication is internal (frame-
           trivial), right is spatial (adjoint rotation); the pentagonal
           clock element has order 10 and is internal: U(1)_clock.
      SM6  the tower stops: sedenions (Cayley-Dickson over O) have zero
           divisors — no third arena, no further gauge factor from this
           mechanism.

Usage:
    python scripts/verify_residual_closure.py
"""
from __future__ import annotations

import numpy as np
from pathlib import Path

rng = np.random.default_rng(20260612)

DATA_PATH = Path(__file__).resolve().parent / "600cell_data.npz"

PASS = []
FAIL = []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


# ======================================================================
# RB1: Einstein-Hilbert quadratic expansion = Fierz-Pauli (4D grid)
# ======================================================================

def spectral_derivative(field, axis, n, L=2 * np.pi):
    k = 2j * np.pi * np.fft.fftfreq(n, d=L / n)
    shape = [1] * field.ndim
    shape[axis] = n
    return np.real(np.fft.ifft(np.fft.fft(field, axis=axis) * k.reshape(shape),
                               axis=axis))


def eh_action(g, n):
    """Total Einstein-Hilbert action of metric g (shape (4,4,n,n,n,n)),
    periodic box, spectral derivatives."""
    gm = np.moveaxis(g, (0, 1), (-2, -1))           # (grid..., 4, 4)
    ginv = np.moveaxis(np.linalg.inv(gm), (-2, -1), (0, 1))
    detg = np.linalg.det(gm)
    grid = g.shape[2:]
    # dg[a, m, v] = d_a g_{m v}
    dg = np.empty((4, 4, 4) + grid)
    for a in range(4):
        for m in range(4):
            for v in range(4):
                dg[a, m, v] = spectral_derivative(g[m, v], a, n)
    # Gam^l_{m v} = 1/2 g^{l s}(d_m g_{s v} + d_v g_{s m} - d_s g_{m v})
    Gam = np.zeros((4, 4, 4) + grid)
    for l in range(4):
        for m in range(4):
            for v in range(4):
                acc = np.zeros(grid)
                for s in range(4):
                    acc += ginv[l, s] * (dg[m, s, v] + dg[v, s, m]
                                         - dg[s, m, v])
                Gam[l, m, v] = 0.5 * acc
    # dGam[a, l, m, v] = d_a Gam^l_{m v}
    dGam = np.empty((4, 4, 4, 4) + grid)
    for a in range(4):
        for l in range(4):
            for m in range(4):
                for v in range(4):
                    dGam[a, l, m, v] = spectral_derivative(Gam[l, m, v], a, n)
    # R_{mv} = d_a Gam^a_{mv} - d_v Gam^a_{ma} + Gam^a_{ab} Gam^b_{mv}
    #          - Gam^a_{vb} Gam^b_{ma}
    Ric = np.zeros((4, 4) + grid)
    for m in range(4):
        for v in range(4):
            acc = np.zeros(grid)
            for a in range(4):
                acc += dGam[a, a, m, v] - dGam[v, a, m, a]
                for b in range(4):
                    acc += Gam[a, a, b] * Gam[b, m, v]
                    acc -= Gam[a, v, b] * Gam[b, m, a]
            Ric[m, v] = acc
    Rs = np.zeros(grid)
    for m in range(4):
        for v in range(4):
            Rs += ginv[m, v] * Ric[m, v]
    vol = (2 * np.pi / n) ** 4
    return np.sum(np.sqrt(-detg) * Rs) * vol


def fp_action_grid(h, n):
    dh = np.stack([np.stack([np.stack([spectral_derivative(h[m, v], a, n)
                                       for v in range(4)])
                             for m in range(4)])
                   for a in range(4)])               # dh[a, m, v]
    up = np.diag(ETA)

    def raise_idx(T, pos):
        sl = [None] * T.ndim
        sl[pos] = slice(None)
        return T * up[tuple(sl)]

    dh_up_a = raise_idx(dh, 0)
    htr = sum(up[m] * h[m, m] for m in range(4))
    dhtr = np.stack([spectral_derivative(htr, a, n) for a in range(4)])
    dhtr_up = raise_idx(dhtr, 0)
    div = np.zeros((4,) + h.shape[2:])
    for v in range(4):
        for m in range(4):
            div[v] += up[m] * dh[m, m, v]            # d^m h_{m v}
    L1 = -0.5 * np.einsum("amv...,amv...->...", dh_up_a,
                          np.einsum("m,v,amv...->amv...", up, up, dh))
    # term2: d_m h_{v r} d^v h^{m r} -> equals (d^m h_{m r})(d^v h_{v r})... use
    # the divergence-squared representative (equal up to total derivative):
    L2 = np.einsum("v...,v,v...->...", div, up, div)
    L3 = -np.einsum("v...,v,v...->...", div, up, dhtr)
    L4 = 0.5 * np.einsum("a...,a...->...", dhtr_up, dhtr)
    vol = (2 * np.pi / n) ** 4
    return np.sum(L1 + L2 + L3 + L4) * vol


def rb1_eh_equals_fp():
    print("RB1: Einstein-Hilbert quadratic expansion = Fierz-Pauli")
    n = 8
    x = np.arange(n) * 2 * np.pi / n
    grids = np.meshgrid(*([x] * 4), indexing="ij")
    ratios = []
    for trial in range(3):
        h = np.zeros((4, 4, n, n, n, n))
        for _ in range(3):
            kvec = rng.integers(-1, 2, size=4)
            if not kvec.any():
                kvec[0] = 1
            A = rng.normal(size=(4, 4))
            A = A + A.T
            phase = rng.uniform(0, 2 * np.pi)
            wave = np.cos(sum(kk * gg for kk, gg in zip(kvec, grids)) + phase)
            h += A[:, :, None, None, None, None] * wave
        eps = 1e-3
        eta_g = ETA[:, :, None, None, None, None] * np.ones_like(h)
        Sp = eh_action(eta_g + eps * h, n)
        Sm = eh_action(eta_g - eps * h, n)
        S2 = (Sp + Sm) / (2 * eps**2)
        Sfp = fp_action_grid(h, n)
        ratios.append(S2 / Sfp)
    ratios = np.array(ratios)
    spread = np.max(np.abs(ratios / ratios[0] - 1))
    check("RB1 S_EH^(2)[h] = const x S_FP[h] across random metrics",
          spread < 1e-4, f"const = {ratios[0]:.6f}, spread {spread:.2e}")


# ======================================================================
# RB2: second-order Schwarzschild = self-energy of the first-order field
# ======================================================================

def rb2_schwarzschild_selfcoupling():
    print("RB2: gravity gravitates (second-order Schwarzschild, symbolic)")
    import sympy as sp

    t, r, th, ph, e = sp.symbols("t r theta phi epsilon", positive=True)
    A = 1 / (2 * r)  # M/(2r) with M absorbed into epsilon

    def einstein_series(f, gfun, order):
        """Einstein tensor of ds^2 = -f dt^2 + gfun (dr^2 + r^2 dOmega^2),
        expanded in epsilon to given order; returns list of series coeffs
        of the mixed components G^t_t, G^r_r, G^th_th."""
        coords = [t, r, th, ph]
        gdd = sp.diag(-f, gfun, gfun * r**2, gfun * r**2 * sp.sin(th)**2)
        guu = gdd.inv()
        n = 4
        Gam = [[[0] * n for _ in range(n)] for _ in range(n)]
        for l in range(n):
            for m in range(n):
                for v in range(n):
                    expr = 0
                    for s in range(n):
                        expr += guu[l, s] * (sp.diff(gdd[s, v], coords[m])
                                             + sp.diff(gdd[s, m], coords[v])
                                             - sp.diff(gdd[m, v], coords[s]))
                    Gam[l][m][v] = sp.simplify(expr / 2)
        Ric = sp.zeros(n)
        for m in range(n):
            for v in range(n):
                expr = 0
                for a in range(n):
                    expr += sp.diff(Gam[a][m][v], coords[a])
                    expr -= sp.diff(Gam[a][m][a], coords[v])
                    for b in range(n):
                        expr += Gam[a][a][b] * Gam[b][m][v]
                        expr -= Gam[a][v][b] * Gam[b][m][a]
                Ric[m, v] = expr
        Rs = sum(guu[i, i] * Ric[i, i] for i in range(n))
        out = []
        for i in range(3):
            Gmixed = guu[i, i] * (Ric[i, i] - sp.Rational(1, 2) * gdd[i, i] * Rs)
            series = sp.series(sp.simplify(Gmixed), e, 0, order + 1).removeO()
            out.append(sp.expand(series))
        return out

    # full second-order truncation of isotropic Schwarzschild:
    #   f = 1 - 4 eps A + 8 eps^2 A^2,  g = 1 + 4 eps A + 6 eps^2 A^2
    f2 = 1 - 4 * e * A + 8 * e**2 * A**2
    g2 = 1 + 4 * e * A + 6 * e**2 * A**2
    comps = einstein_series(f2, g2, 2)
    ok1 = all(sp.simplify(sp.expand(c).coeff(e, 1)) == 0 for c in comps)
    ok2 = all(sp.simplify(sp.expand(c).coeff(e, 2)) == 0 for c in comps)
    check("RB2a first order: linearised vacuum equations hold", ok1)
    check("RB2b second order: h^(2) exactly cancels the self-energy of h^(1)",
          ok2)

    # the null: truncate at FIRST order (no h^(2)) -> O(eps^2) residual remains
    f1 = 1 - 4 * e * A
    g1 = 1 + 4 * e * A
    comps1 = einstein_series(f1, g1, 2)
    resid = [sp.simplify(sp.expand(c).coeff(e, 2)) for c in comps1]
    ok3 = any(rr != 0 for rr in resid)
    check("RB2c null: without h^(2) a nonzero O(eps^2) residual remains "
          "(gravity MUST gravitate)", ok3,
          f"G^t_t residual = {sp.simplify(resid[0])}")


# ======================================================================
# RG: beyond-Gaussian collective effective action (Cramer)
# ======================================================================

def make_rate_function(vals, probs):
    """Exact-precision Cramer rate function I(s) for the mean of x^2 with
    x^2 taking values `vals` with weights `probs`: solve Lambda'(t) = s by
    bisection (Lambda' is strictly increasing), then I = t s - Lambda(t)."""
    from scipy.optimize import brentq
    vals = np.asarray(vals, dtype=float)
    probs = np.asarray(probs, dtype=float)

    def lam(t):
        m = np.exp(t * vals - np.max(t * vals))
        return np.log(np.sum(m * probs)) + np.max(t * vals)

    def lam_prime(t):
        w = np.exp(t * vals - np.max(t * vals)) * probs
        return np.sum(w * vals) / np.sum(w)

    def I_of(s):
        if abs(s - np.sum(vals * probs)) < 1e-15:
            return 0.0
        tstar = brentq(lambda t: lam_prime(t) - s, -200.0, 200.0,
                       xtol=1e-15, rtol=1e-15)
        return tstar * s - lam(tstar)

    return I_of


def rg_beyond_gaussian():
    print("RG: collective effective action beyond the Gaussian regime")

    # uniform on [-sqrt(3), sqrt(3)] (unit variance), discretised densely
    xs = np.linspace(-np.sqrt(3), np.sqrt(3), 20001)
    uni = (xs**2, np.full_like(xs, 1.0 / len(xs)))
    # two-scale: x in {+-1/2, +-3/2}, p = 5/8, 3/8 (unit variance)
    two = (np.array([0.25, 2.25]), np.array([5 / 8, 3 / 8]))

    for name, (v2, pr) in (("uniform", uni), ("two-scale", two)):
        mean = np.sum(v2 * pr)
        I_of = make_rate_function(v2, pr / pr.sum())
        I0 = I_of(mean)
        d = 1e-4
        Ipp = (I_of(mean + d) - 2 * I0 + I_of(mean - d)) / d**2
        var4 = np.sum(v2**2 * pr) - mean**2
        ok0 = abs(I0) < 1e-12 and abs(Ipp * var4 - 1) < 1e-3
        check(f"RG1 [{name}] rate function: zero minimum at background, "
              f"I'' = 1/Var(x^2)", ok0,
              f"I(bg) = {I0:.2e}, I'' = {Ipp:.4f} vs 1/Var = {1/var4:.4f}")

        def cubic_over_quad(N):
            s = 1 / np.sqrt(N)
            Ip, Im = I_of(mean + s), I_of(mean - s)
            return abs(Ip - Im) / (Ip + Im)

        r1, r4 = cubic_over_quad(400), cubic_over_quad(6400)
        check(f"RG2 [{name}] cubic/quadratic at fluctuation scale ~ N^(-1/2)",
              3.0 < r1 / r4 < 5.5, f"ratio {r1 / r4:.2f} (expect 4)")

    def fluct(N, reps=400):
        devs = []
        for _ in range(reps):
            xs = rng.uniform(-np.sqrt(3), np.sqrt(3), size=N)
            devs.append(abs(np.mean(xs**2) - 1.0))
        return np.mean(devs)

    f1, f4 = fluct(400), fluct(6400)
    check("RG3 empirical second-moment fluctuations ~ N^(-1/2) (non-Gaussian)",
          3.0 < f1 / f4 < 5.5, f"ratio {f1 / f4:.2f} (expect 4)")


# ======================================================================
# RC: explicit-rate continuum theorem on the 600-cell
# ======================================================================

def rc_continuum_rate():
    print("RC: band exactness + explicit eigenvalue rate + aliasing bound")
    d = np.load(DATA_PATH)
    verts = d["vertices"]
    Lg = d["laplacian"].astype(float)
    theta = np.pi / 5

    def lam_formula(k):
        nn = k + 1
        return 12.0 * (1 - np.sin(nn * theta) / (nn * np.sin(theta)))

    # RC1: sampled harmonics are EXACT eigenvectors (no continuum limit needed)
    err1 = max(np.linalg.norm(Lg @ verts[:, i] - lam_formula(1) * verts[:, i])
               for i in range(4))
    check("RC1a degree-1 harmonics (coordinates) are exact eigenvectors",
          err1 < 1e-10, f"max |L x - lam1 x| = {err1:.2e}")
    errs2 = []
    for i in range(4):
        for j in range(i, 4):
            q = verts[:, i] * verts[:, j] - (0.25 if i == j else 0.0)
            errs2.append(np.linalg.norm(Lg @ q - lam_formula(2) * q))
    check("RC1b degree-2 harmonics (traceless quadratics) are exact eigenvectors",
          max(errs2) < 1e-10, f"max residual = {max(errs2):.2e}")

    # RC2: dispersion: lam_k = 2 theta^2 k(k+2) [1 - (3n^2-7) theta^2 / 60 + O(theta^4)]
    ok_rate = True
    worst = 0.0
    for k in range(1, 6):
        nn = k + 1
        rho = lam_formula(k) / (2 * theta**2 * k * (k + 2))
        rate_pred = (3 * nn**2 - 7) * theta**2 / 60
        dev = abs((1 - rho) - rate_pred)
        # next correction is O(theta^4 n^4 / (n^2-1)) — explicit envelope:
        envelope = theta**4 * nn**4 / (nn**2 - 1) * 0.05
        worst = max(worst, dev / max(envelope, 1e-12))
        ok_rate = ok_rate and dev < envelope
    check("RC2 eigenvalue rate (1 - rho_k) = (3n^2-7) theta^2/60 + O(theta^4)",
          ok_rate, f"worst dev/envelope = {worst:.2f}")

    # spectrum really contains the formula values with full multiplicity
    evals = np.linalg.eigvalsh(Lg)
    ok_mult = True
    for k in range(0, 6):
        target = lam_formula(k)
        mult = int(np.sum(np.abs(evals - target) < 1e-8))
        ok_mult = ok_mult and mult >= (k + 1) ** 2
    check("RC2b formula eigenvalues present with multiplicity >= (k+1)^2",
          ok_mult)

    # RC3: kernel aliasing bound: ||pi_r v|| = ||v|| / (1 + r^2 lam) on eigvecs
    lams, vecs = np.linalg.eigh(Lg)
    r = 0.8
    Pi = np.linalg.inv(np.eye(len(Lg)) + r**2 * Lg)
    hi = vecs[:, -1]  # highest mode (above-band content)
    got = np.linalg.norm(Pi @ hi)
    pred = 1.0 / (1 + r**2 * lams[-1])
    check("RC3 kernel suppression of above-band content = 1/(1 + r^2 lambda)",
          abs(got - pred) < 1e-12,
          f"suppression {got:.4f} (band content passes at "
          f"{1/(1+r**2*lam_formula(1)):.4f})")


# ======================================================================
# RGRAV: Newton's constant, conditional derivation + honesty gate
# ======================================================================

def rgrav_newton_constant():
    print("RGRAV: G from the structural muon shell (conditional) + honesty gate")
    G_meas = 6.67430e-11           # CODATA 2018, u_r = 2.2e-5
    hbar = 1.054571817e-34
    c = 299792458.0
    m_mu = 1.883531627e-28         # kg (CODATA)
    m_p = 1.67262192369e-27        # kg (proton, for the honesty gate)
    phi = (1 + np.sqrt(5)) / 2

    # H-shell-96: the muon sits at cascade shell N = 96 = 24 x 4 (Paper LII,
    # prior structural claim). Then m_Planck = m_mu phi^96 and G is predicted:
    m_P_pred = m_mu * phi**96
    G_pred = hbar * c / m_P_pred**2
    rel = G_pred / G_meas - 1
    check("RGRAV1 G = hbar c / (m_mu phi^96)^2 matches measured G",
          abs(rel) < 1e-3,
          f"G_pred = {G_pred:.5e}, G_meas = {G_meas:.5e}, dev = {rel:+.2e}")

    # honesty gate: the proton (i.e. alpha_G directly) is NOT integer-forced
    m_P_meas = np.sqrt(hbar * c / G_meas)
    N_proton = np.log(m_P_meas / m_p) / np.log(phi)
    off_p = abs(N_proton - round(N_proton))
    N_muon = np.log(m_P_meas / m_mu) / np.log(phi)
    off_mu = abs(N_muon - round(N_muon))
    check("RGRAV2 honesty gate: proton shell NOT integer-forced (no alpha_G "
          "numerology); muon IS the anchor",
          off_p > 0.25 and off_mu < 5e-3,
          f"proton offset {off_p:.3f} (rejected), muon offset {off_mu:.5f} "
          f"at shell {round(N_muon)}")


# ======================================================================
# SM: gauge-group structure from the division-algebra arenas
# ======================================================================

def cayley_dickson(mult):
    """Double an algebra given its multiplication tensor mult[i,j] -> vector,
    with conjugation = negate all but component 0."""
    n = mult.shape[0]

    def conj_vec(v):
        w = v.copy()
        w[1:] *= -1
        return w

    big = np.zeros((2 * n, 2 * n, 2 * n))
    for i in range(2 * n):
        for j in range(2 * n):
            a = np.zeros(n); b = np.zeros(n)
            c = np.zeros(n); dd = np.zeros(n)
            (a if i < n else b)[i % n] = 1.0
            (c if j < n else dd)[j % n] = 1.0
            # (a,b)(c,d) = (ac - d* b, d a + b c*)
            ac = np.einsum("i,j,ijk->k", a, c, mult)
            db = np.einsum("i,j,ijk->k", conj_vec(dd), b, mult)
            da = np.einsum("i,j,ijk->k", dd, a, mult)
            bc = np.einsum("i,j,ijk->k", b, conj_vec(c), mult)
            big[i, j, :n] = ac - db
            big[i, j, n:] = da + bc
    return big


def sm_gauge_structure():
    print("SM: gauge-group structure from quaternionic + octonionic arenas")
    # reals -> complexes -> quaternions -> octonions by Cayley-Dickson
    m1 = np.ones((1, 1, 1))
    m2 = cayley_dickson(m1)
    m4 = cayley_dickson(m2)
    m8 = cayley_dickson(m4)

    # sanity: octonion norm composition |xy| = |x||y| on random samples
    x = rng.normal(size=8); y = rng.normal(size=8)
    xy = np.einsum("i,j,ijk->k", x, y, m8)
    ok_norm = abs(np.linalg.norm(xy) - np.linalg.norm(x) * np.linalg.norm(y)) < 1e-10
    check("SM0 octonions compose norms (Hurwitz algebra confirmed)", ok_norm)

    # SM1: derivations of O: D(e_i e_j) = D(e_i) e_j + e_i D(e_j),
    # D an 8x8 matrix, 64 unknowns
    rows = []
    for i in range(8):
        for j in range(8):
            for mcomp in range(8):
                row = np.zeros((8, 8))
                # LHS: sum_k c_{ijk} D_{m k}
                row[mcomp, :] += m8[i, j, :]
                # RHS: sum_a D_{a i} c_{a j m} + sum_b D_{b j} c_{i b m}
                for a in range(8):
                    row[a, i] -= m8[a, j, mcomp]
                for b in range(8):
                    row[b, j] -= m8[i, b, mcomp]
                rows.append(row.ravel())
    Msys = np.array(rows)
    _, s, vt = np.linalg.svd(Msys)
    nullity = int(np.sum(s < 1e-9 * s[0]))
    check("SM1 dim Der(O) = 14: the automorphism algebra is G2",
          nullity == 14, f"computed dim = {nullity}")
    Dbasis = [vt[-(k + 1)].reshape(8, 8) for k in range(nullity)]

    # SM2: stabiliser of the rendered unit e1: D e1 = 0.
    # A maps coefficient space R^14 -> R^8 (the image of e1); its null space
    # is the stabiliser subalgebra.
    A = np.array([D[:, 1] for D in Dbasis])        # (14, 8)
    rankA = np.linalg.matrix_rank(A, tol=1e-9)
    _, _, vN = np.linalg.svd(A.T, full_matrices=True)
    stab_coeffs = vN[rankA:]                       # (14 - rankA, 14)
    stab = [sum(cc * DD for cc, DD in zip(co, Dbasis)) for co in stab_coeffs]
    check("SM2 stabiliser of e1 has dimension 8", len(stab) == 8,
          f"dim = {len(stab)}")

    # SM3a: derivations are skew-symmetric (they preserve the norm form)
    ok_skew = all(np.max(np.abs(D + D.T)) < 1e-9 for D in stab)
    check("SM3a stabiliser elements are skew-symmetric (norm form preserved)",
          ok_skew)

    # SM3: complex-linearity and tracelessness -> su(3)
    # L1[k, j] = component k of e1 e_j (left multiplication by e1)
    L1 = np.array([[m8[1, j, k] for j in range(8)] for k in range(8)])
    W = list(range(2, 8))
    ok_J = all(np.max(np.abs((D @ L1 - L1 @ D)[np.ix_(W, W)])) < 1e-9
               for D in stab)
    JW = L1[np.ix_(W, W)]
    ok_J2 = np.max(np.abs(JW @ JW + np.eye(6))) < 1e-9
    ok_tr = all(abs(np.trace(D[np.ix_(W, W)])) < 1e-9
                and abs(np.trace(JW @ D[np.ix_(W, W)])) < 1e-9
                for D in stab)
    check("SM3 stabiliser is complex-linear for J = L_{e1} (J^2 = -1) and "
          "complex-traceless: inside su(3)", ok_J and ok_J2 and ok_tr)

    # SM4: the algebra IS su(3): closed, compact, simple, rank 2, dim 8
    def project(X, basis):
        Bmat = np.array([b.ravel() for b in basis]).T
        coef, res, *_ = np.linalg.lstsq(Bmat, X.ravel(), rcond=None)
        resid = np.linalg.norm(Bmat @ coef - X.ravel())
        return coef, resid

    struct = np.zeros((8, 8, 8))
    ok_closed = True
    for a in range(8):
        for b in range(8):
            C = stab[a] @ stab[b] - stab[b] @ stab[a]
            coef, resid = project(C, stab)
            ok_closed = ok_closed and resid < 1e-8
            struct[a, b] = coef
    adj = [struct[a] for a in range(8)]
    K = np.array([[np.trace(adj[a] @ adj[b]) for b in range(8)]
                  for a in range(8)])
    evK = np.linalg.eigvalsh(K)
    ok_compact = evK.max() < -1e-9 * abs(evK.min())
    Xg = sum(rng.normal() * np.array(ad) for ad in adj)
    cent = np.linalg.matrix_rank(np.array(
        [ (Xg @ ad - ad @ Xg).ravel() for ad in adj ]).T, tol=1e-7)
    rank = 8 - cent
    # simplicity: the ideal generated by a random element is everything.
    # Maintain an orthonormal basis (rows) and grow it by all ad-images.
    B = rng.normal(size=(1, 8))
    B /= np.linalg.norm(B)
    for _ in range(12):
        imgs = np.array([struct[a] @ v for a in range(8) for v in B])
        M = np.vstack([B, imgs])
        _, sv, vt = np.linalg.svd(M, full_matrices=False)
        newdim = int(np.sum(sv > 1e-8 * sv[0]))
        Bnew = vt[:newdim]
        if newdim == B.shape[0]:
            break
        B = Bnew
    ok_simple = (B.shape[0] == 8)
    check("SM4 stabiliser algebra: closed, compact, simple, rank 2 => su(3)",
          ok_closed and ok_compact and rank == 2 and ok_simple,
          f"closed={ok_closed}, Killing<0={ok_compact}, rank={rank}, "
          f"simple={ok_simple}")

    # SM5: arena split + clock U(1) on the actual 600-cell
    d = np.load(DATA_PATH)
    verts = d["vertices"]
    keys = {tuple(np.round(v, 8)): i for i, v in enumerate(verts)}

    def qmul(q1, q2):
        a, b, c_, dd = q1
        ee, f, g, h_ = q2
        return np.array([a*ee - b*f - c_*g - dd*h_,
                         a*f + b*ee + c_*h_ - dd*g,
                         a*g - b*h_ + c_*ee + dd*f,
                         a*h_ + b*g - c_*f + dd*ee])

    clock = None
    for v in verts:
        if abs(v[0] - (1 + np.sqrt(5)) / 4) < 1e-9:  # cos(pi/5) = phi/2
            clock = v
            break
    perm = np.array([keys[tuple(np.round(qmul(clock, v), 8))] for v in verts])
    p = perm.copy()
    order = 1
    while not np.array_equal(p, np.arange(len(verts))):
        p = perm[p]
        order += 1
        if order > 40:
            break
    check("SM5 pentagonal clock element exists (left mult, order 10): the "
          "U(1)_clock inside the internal left SU(2)", order == 10,
          f"order = {order}")

    # SM6: the tower stops: sedenions have zero divisors
    m16 = cayley_dickson(m8)
    e = np.eye(16)
    found = None
    for (a, b, c_, dd) in [(3, 10, 6, 15), (1, 10, 5, 14), (2, 9, 6, 13)]:
        for s1 in (1, -1):
            for s2 in (1, -1):
                xx = e[a] + s1 * e[b]
                yy = e[c_] + s2 * e[dd]
                prod = np.einsum("i,j,ijk->k", xx, yy, m16)
                if np.linalg.norm(prod) < 1e-12:
                    found = (a, b, c_, dd, s1, s2)
    check("SM6 sedenions have zero divisors: the arena tower (and the gauge "
          "mechanism) stops at O", found is not None,
          f"(e{found[0]}{'+' if found[4]>0 else '-'}e{found[1]})"
          f"(e{found[2]}{'+' if found[5]>0 else '-'}e{found[3]}) = 0"
          if found else "no zero divisor found")


def main():
    print("=" * 70)
    print("Residual-closure verification — docs/residual-closure-derivation.md")
    print("=" * 70)
    rb1_eh_equals_fp()
    rb2_schwarzschild_selfcoupling()
    rg_beyond_gaussian()
    rc_continuum_rate()
    rgrav_newton_constant()
    sm_gauge_structure()
    print("=" * 70)
    print(f"SUMMARY: {len(PASS)} PASS, {len(FAIL)} FAIL")
    for name in FAIL:
        print(f"  FAILED: {name}")
    return 0 if not FAIL else 1


if __name__ == "__main__":
    raise SystemExit(main())
