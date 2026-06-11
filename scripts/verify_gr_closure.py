#!/usr/bin/env python3
"""
Verify the GR-closure chain of docs/gr-closure-derivation.md.

  T1  Fierz-Pauli uniqueness: the 6-parameter quadratic action for a
      symmetric rank-2 field has a 1-dimensional gauge-invariant null
      space with ratios (-1/2, 1, -1, 1/2) and no mass terms.
  T2  Polarisations: at null momentum the FP kinetic operator has a
      6-dim kernel containing the 4-dim gauge orbit -> 2 physical.
  T3a Variation of the FP action = linearised Einstein tensor.
  T3  Grid solve with a dust blob: trace reversal gives
      h_00 = h_ii = 2GM/(r c^2), h_0i = 0 (factor 2 + isotropy), and
      the harmonic-gauge solution satisfies the full gauge-unfixed
      linearised Einstein equation mode by mode.
  T4  Light bending through the solved metric: 4GM/(b c^2); the
      scalar-only (h_00 only) control gives exactly half.
  T5  Exact tick-energy conservation of the leapfrog substrate
      dynamics on the actual 600-cell graph.
  T6  Exact local continuity de_v/dt + sum_w J_vw = 0 on the graph.
  T7  Canonical stress tensor: symmetry, on-shell conservation with
      O(d^2) convergence, positivity, dust limit |T_ij|/T_00 = O(eps^2).
  T8  Chart redescription shifts h by -(d_mu xi_nu + d_nu xi_mu)
      (+ Lie terms), with O(xi^2) convergence.
  T9  TT waves solve the FP equation iff omega = c|k|.
  T10 Second-difference -> d_t^2 at O(tau^2); leapfrog eigenmode
      frequency converges to the continuum value at O(tau^2).
  T11 Klein-Gordon envelope -> Schrodinger with error O(eps^2)
      (the massive end of the C_phi family).
  T12 Equivalence principle: inertial mass (momentum/group velocity)
      = gravitating mass (energy/charge) on one simulated packet.
  T13 Maxwell uniqueness (rank-1 analogue): null space (1, -1, 0),
      photon has 2 polarisations.
  T14 Substrate rank-2 tensoriality: the coarse gradient bilinear on
      V_600 is 2I x 2I equivariant (left: scalar transport; right:
      adjoint SO(3) rotation of frame indices).
  T15 Collective-field effective action (Wishart): quadratic term
      matches (N/4) tr((Sigma0^-1 dh)^2); cubic/quadratic ratio at the
      fluctuation scale falls as N^{-1/2}; empirical fluctuations of
      the sample second moment scale as N^{-1/2}.

Usage:
    python scripts/verify_gr_closure.py
"""
from __future__ import annotations

import numpy as np
from pathlib import Path

rng = np.random.default_rng(20260611)

DATA_PATH = Path(__file__).resolve().parent / "600cell_data.npz"

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])

PASS = []
FAIL = []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


# ----------------------------------------------------------------------
# momentum-space machinery for quadratic actions of a symmetric rank-2 h
# (all index placement lower; raising explicit with ETA)
# ----------------------------------------------------------------------

def raise2(h):
    return ETA @ h @ ETA


def tr_eta(h):
    return float(np.sum(ETA * h)) if np.isrealobj(h) else complex(np.sum(ETA * h))


def bilinears(h1, h2, k):
    """The four 2-derivative contractions and two mass contractions,
    as symmetric bilinear forms at momentum k (lower components)."""
    kup = ETA @ k
    kk = k @ ETA @ k
    B1 = kk * np.sum(raise2(h1) * h2)
    B2 = (k @ raise2(h1)) @ (kup @ h2)
    s1 = kup @ h1 @ kup
    s2 = kup @ h2 @ kup
    B3 = 0.5 * (s1 * tr_eta(h2) + s2 * tr_eta(h1))
    B4 = kk * tr_eta(h1) * tr_eta(h2)
    M1 = np.sum(raise2(h1) * h2)
    M2 = tr_eta(h1) * tr_eta(h2)
    return np.array([B1, B2, B3, B4, M1, M2])


FP = np.array([-0.5, 1.0, -1.0, 0.5, 0.0, 0.0])  # claimed unique ratios


def fp_form(h1, h2, k):
    return FP @ bilinears(h1, h2, k)


def sym_basis():
    basis = []
    for mu in range(4):
        for nu in range(mu, 4):
            E = np.zeros((4, 4))
            E[mu, nu] = 1.0
            E[nu, mu] = 1.0
            basis.append(E)
    return basis  # 10 elements


def gauge_dir(xi, k):
    return np.outer(k, xi) + np.outer(xi, k)


def fp_operator_matrix(k):
    """10x10 matrix Q_IJ = fp_form(E_I, E_J; k); ker Q = solutions."""
    B = sym_basis()
    Q = np.zeros((10, 10))
    for i, Ei in enumerate(B):
        for j, Ej in enumerate(B):
            Q[i, j] = fp_form(Ei, Ej, k)
    return Q, B


def vec_sym(h, B):
    """Coordinates of symmetric h in the sym_basis (dual via matching)."""
    out = np.zeros(10, dtype=h.dtype)
    idx = 0
    for mu in range(4):
        for nu in range(mu, 4):
            out[idx] = h[mu, nu]
            idx += 1
    return out


def E_of_h(h, k):
    """The tensor E(h)^{mu nu} defined by fp_form(g, h) = g_{mu nu} E^{mu nu}.

    Computed by feeding unit symmetric g's (off-diagonals counted once
    via the symmetric unit matrices)."""
    E = np.zeros((4, 4), dtype=complex)
    for mu in range(4):
        for nu in range(mu, 4):
            g = np.zeros((4, 4))
            g[mu, nu] = 1.0
            g[nu, mu] = 1.0
            val = fp_form(g, h, k)
            if mu == nu:
                E[mu, nu] = val
            else:
                E[mu, nu] = 0.5 * val
                E[nu, mu] = 0.5 * val
    return E


def lin_einstein(h, k):
    """Linearised Einstein tensor with the replacement d_a d_b -> k_a k_b
    (lower indices)."""
    kup = ETA @ k
    kk = k @ ETA @ k
    kh = kup @ h  # k_alpha h^alpha_nu  (lower nu)
    R = 0.5 * (np.outer(k, kh) + np.outer(kh, k) - kk * h
               - tr_eta(h) * np.outer(k, k))
    Rs = tr_eta(R)
    return R - 0.5 * ETA * Rs


def t1_fp_uniqueness():
    print("T1: Fierz-Pauli uniqueness scan")
    rows = []
    for _ in range(80):
        k = rng.normal(size=4)
        xi = rng.normal(size=4)
        A = rng.normal(size=(4, 4))
        h = A + A.T
        G = gauge_dir(xi, k)
        rows.append(bilinears(h, G, k))
    rows = np.array(rows)
    u, s, vt = np.linalg.svd(rows)
    nullity = int(np.sum(s < 1e-10 * s[0]))
    check("T1a 6-param scan has exactly 1 gauge-invariant direction",
          nullity == 1, f"singular values tail: {s[-2]:.2e}, {s[-1]:.2e}")
    v = vt[-1]
    v = v / v[1]  # normalise a2 = 1
    target = FP / FP[1]
    check("T1b null direction = FP ratios (-1/2, 1, -1, 1/2, 0, 0)",
          np.allclose(v, target, atol=1e-9),
          f"found {np.round(v, 6)}")
    check("T1c mass terms killed (graviton massless)",
          abs(v[4]) < 1e-9 and abs(v[5]) < 1e-9)


def t2_polarisations():
    print("T2: physical polarisation count at null momentum")
    omega = 1.3
    k = np.array([omega, 0.0, 0.0, omega])  # k.eta.k = 0
    Q, B = fp_operator_matrix(k)
    u, s, vt = np.linalg.svd(Q)
    kerdim = int(np.sum(s < 1e-10 * s[0]))
    check("T2a dim ker FP-operator at null k = 6", kerdim == 6,
          f"kernel dim {kerdim}")
    # gauge orbit
    Gs = []
    for a in range(4):
        xi = np.zeros(4)
        xi[a] = 1.0
        Gs.append(vec_sym(gauge_dir(xi, k), B))
    Gs = np.array(Gs)
    gdim = np.linalg.matrix_rank(Gs, tol=1e-10)
    check("T2b gauge orbit is 4-dimensional", gdim == 4)
    inker = max(np.linalg.norm(Q @ g) for g in Gs)
    check("T2c gauge orbit lies inside the kernel", inker < 1e-10,
          f"max |Q g| = {inker:.2e}")
    check("T2d physical polarisations = 6 - 4 = 2", kerdim - gdim == 2)


def t3a_variation_is_einstein():
    print("T3a: FP variation = linearised Einstein tensor")
    lam = None
    ok = True
    worst = 0.0
    for _ in range(20):
        k = rng.normal(size=4)
        A = rng.normal(size=(4, 4))
        h = (A + A.T).astype(complex)
        E = E_of_h(h, k)                       # upper indices
        G = raise2(lin_einstein(h, k))         # raise to upper indices
        if lam is None:
            lam = np.sum(np.conj(G) * E) / np.sum(np.conj(G) * G)
        r = np.linalg.norm(E - lam * G) / np.linalg.norm(E)
        worst = max(worst, r)
        ok = ok and r < 1e-10
    check("T3a delta S_FP / delta h ∝ G^lin (one constant, random inputs)",
          ok, f"lambda = {complex(lam):.3f}, worst residual {worst:.2e}")


def solve_weak_field(n=48, sigma=0.03, L=1.0):
    """FFT solve of nabla^2 Phi = 4 pi rho for a Gaussian blob, then the
    trace-reversal conversion h = hbar - 1/2 eta tr(hbar) with
    hbar_00 = -4 Phi."""
    x = (np.arange(n) / n - 0.5) * L
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    r2 = X**2 + Y**2 + Z**2
    rho = np.exp(-r2 / (2 * sigma**2))
    M = rho.sum() * (L / n) ** 3
    kf = 2 * np.pi * np.fft.fftfreq(n, d=L / n)
    KX, KY, KZ = np.meshgrid(kf, kf, kf, indexing="ij")
    k2 = KX**2 + KY**2 + KZ**2
    k2[0, 0, 0] = 1.0
    rho_h = np.fft.fftn(rho)
    phi_h = -4 * np.pi * rho_h / k2
    phi_h[0, 0, 0] = 0.0
    Phi = np.real(np.fft.ifftn(phi_h))
    hbar = np.zeros((4, 4) + Phi.shape)
    hbar[0, 0] = -4.0 * Phi
    trbar = -hbar[0, 0]  # eta^{mu nu} hbar_{mu nu} = -hbar_00
    h = hbar.copy()
    for mu in range(4):
        h[mu, mu] = hbar[mu, mu] - 0.5 * ETA[mu, mu] * trbar
    return X, Y, Z, rho, M, Phi, h, (KX, KY, KZ)


def t3_grid_solve():
    print("T3: weak-field grid solve (factor 2 + isotropy + full EOM)")
    X, Y, Z, rho, M, Phi, h, Ks = solve_weak_field()
    n = rho.shape[0]
    # algebraic structure
    iso = max(np.max(np.abs(h[1, 1] - h[0, 0])),
              np.max(np.abs(h[2, 2] - h[0, 0])),
              np.max(np.abs(h[3, 3] - h[0, 0])))
    off = max(np.max(np.abs(h[0, i])) for i in (1, 2, 3))
    check("T3b isotropy: h_00 = h_11 = h_22 = h_33 exactly",
          iso < 1e-14, f"max dev {iso:.2e}")
    check("T3c h_0i = 0", off < 1e-14)
    factor = np.max(np.abs(h[0, 0] + 2 * Phi))
    check("T3d factor 2: h_00 = -2 Phi from trace reversal",
          factor < 1e-12, f"max dev {factor:.2e}")
    # physical profile vs 2GM/r outside the blob
    r = np.sqrt(X**2 + Y**2 + Z**2)
    mask = (r > 0.10) & (r < 0.22)
    pred = 2 * M / r[mask]
    got = h[0, 0][mask]
    A = np.vstack([1.0 / r[mask], np.ones(mask.sum())]).T
    coef, *_ = np.linalg.lstsq(A, got, rcond=None)
    check("T3e radial profile h_00 = 2GM/r + offset (periodic artifact)",
          abs(coef[0] / (2 * M) - 1) < 0.03,
          f"fit A = {coef[0]:.4f}, 2GM = {2*M:.4f}, offset {coef[1]:+.4f}")
    _ = pred
    # full gauge-unfixed equation, mode by mode:
    #   E(h(k); k) must be ∝ Theta^{mu nu}(k) with ONE constant
    KX, KY, KZ = Ks
    rho_h = np.fft.fftn(rho)
    h_h = np.fft.fftn(h, axes=(2, 3, 4))
    idxs = [(1, 0, 0), (0, 2, 0), (0, 0, 3), (2, 3, 1), (4, 1, 2)]
    lam = None
    ok = True
    worst = 0.0
    for (i, j, l) in idxs:
        k4 = np.array([0.0, KX[i, j, l], KY[i, j, l], KZ[i, j, l]])
        hk = h_h[:, :, i, j, l]
        Theta = np.zeros((4, 4), dtype=complex)
        Theta[0, 0] = rho_h[i, j, l]  # dust: Theta_00 = rho c^2
        E = E_of_h(hk, k4)
        T_up = raise2(Theta)
        if lam is None:
            lam = np.sum(np.conj(T_up) * E) / np.sum(np.conj(T_up) * T_up)
        res = np.linalg.norm(E - lam * T_up) / np.linalg.norm(E)
        worst = max(worst, res)
        ok = ok and res < 1e-10
    check("T3f harmonic solution satisfies full linearised Einstein eq "
          "(E(h) ∝ dust Theta, one constant across modes)",
          ok, f"coupling lambda = {complex(lam):.4f}, worst residual {worst:.2e}")


def t4_light_bending():
    print("T4: light bending through the solved metric")
    X, Y, Z, rho, M, Phi, h, _ = solve_weak_field(n=64, sigma=0.02)
    r = np.sqrt(X**2 + Y**2 + Z**2)
    # radially averaged profile of h_00 (= h_ii)
    nb = 60
    rmax = 0.30
    bins = np.linspace(0.005, rmax, nb + 1)
    rc = 0.5 * (bins[:-1] + bins[1:])
    prof = np.zeros(nb)
    for ib in range(nb):
        m = (r >= bins[ib]) & (r < bins[ib + 1])
        prof[ib] = h[0, 0][m].mean()
    # subtract the periodic zero-point: fit A/r + B on a clean shell
    fitm = (rc > 0.10) & (rc < 0.22)
    Amat = np.vstack([1.0 / rc[fitm], np.ones(fitm.sum())]).T
    (Afit, Bfit), *_ = np.linalg.lstsq(Amat, prof[fitm], rcond=None)
    M_A = Afit / 2.0
    f00 = prof - Bfit              # h_00(r), zeroed at infinity
    Rd = 0.24                      # trust data inside this radius

    def h00_of_r(rr):
        rr = np.atleast_1d(rr)
        out = np.where(rr < Rd,
                       np.interp(rr, rc, f00),
                       Afit / rr)
        return out

    def deflection(weight_spatial):
        """alpha(b) = -d/db ∫ (n-1) dz, with n-1 = (h_00 + w*h_xx)/2
        and h_xx = h_00 (isotropy, T3b)."""
        b = 0.12
        zs = np.linspace(-60.0, 60.0, 200001)

        def col(bb):
            rr = np.sqrt(bb**2 + zs**2)
            n_minus_1 = 0.5 * (1.0 + weight_spatial) * h00_of_r(rr)
            return np.trapz(n_minus_1, zs)

        db = 1e-4
        return -(col(b + db) - col(b - db)) / (2 * db), b

    a_tensor, b = deflection(1.0)   # full derived metric
    a_scalar, _ = deflection(0.0)   # h_00-only control
    pred = 4 * M_A / b
    check("T4a tensor deflection = 4GM/(b c^2)",
          abs(a_tensor / pred - 1) < 0.05,
          f"alpha = {a_tensor:.5f}, 4GM/b = {pred:.5f}")
    check("T4b scalar-only control gives exactly half",
          abs(a_tensor / a_scalar - 2.0) < 0.02,
          f"ratio = {a_tensor / a_scalar:.4f}")


def load_600cell():
    d = np.load(DATA_PATH)
    return d["vertices"], d["adjacency"].astype(float), d["laplacian"].astype(float)


def t5_t6_substrate_conservation():
    print("T5/T6: exact conservation laws on the 600-cell substrate")
    verts, A, Lg = load_600cell()
    n = len(verts)
    tau = 0.05
    F0 = rng.normal(size=(n, 4))
    F1 = F0 + tau * rng.normal(size=(n, 4)) * 0.2
    Fm, Fc = F0, F1
    E0 = None
    drift = 0.0
    for t in range(2000):
        Fp = 2 * Fc - Fm - tau**2 * (Lg @ Fc)
        E = (0.5 * np.sum(((Fp - Fc) / tau) ** 2)
             + 0.5 * np.sum(Fc * (Lg @ Fp)))
        if E0 is None:
            E0 = E
        drift = max(drift, abs(E - E0) / abs(E0))
        Fm, Fc = Fc, Fp
    check("T5 leapfrog tick-energy conserved exactly (2000 ticks)",
          drift < 1e-10, f"max relative drift {drift:.2e}")

    # T6: local continuity identity, semi-discrete, machine precision
    F = rng.normal(size=(n, 4))
    Fd = rng.normal(size=(n, 4))          # dF/dt, arbitrary state
    Fdd = -(Lg @ F)                        # equations of motion (c=a=1)
    # e_v = 1/2 |Fd_v|^2 + 1/4 sum_w |F_v - F_w|^2
    # de_v/dt = Fd_v . Fdd_v + 1/2 sum_w (F_v - F_w).(Fd_v - Fd_w)
    nbrs = [np.nonzero(A[v])[0] for v in range(n)]
    worst = 0.0
    for v in range(n):
        dv = F[v] - F[nbrs[v]]            # (12, 4)
        de = F[v] @ np.zeros(4) + Fd[v] @ Fdd[v] + 0.5 * np.sum(
            dv * (Fd[v] - Fd[nbrs[v]]))
        J = 0.5 * np.sum(dv * (Fd[v] + Fd[nbrs[v]]))
        worst = max(worst, abs(de + J))
    scale = np.abs(Fd).max() ** 2 * 12
    check("T6 local continuity de_v/dt + sum_w J_vw = 0 at every vertex",
          worst / scale < 1e-12, f"worst residual {worst:.2e}")


def t7_stress_tensor():
    print("T7: canonical stress tensor of the substrate field")
    mu = 6.0
    ks = np.array([1.0, 2.0, 3.0])
    amps = np.array([0.7, 0.4, 0.3])
    phs = rng.uniform(0, 2 * np.pi, size=3)
    oms = np.sqrt(mu**2 + ks**2)

    def field(x, t):
        return sum(a * np.cos(k * x) * np.cos(o * t + p)
                   for a, k, o, p in zip(amps, ks, oms, phs))

    def dfield(x, t, dx=0, dt=0):
        out = 0.0
        for a, k, o, p in zip(amps, ks, oms, phs):
            fx = np.cos(k * x + dx * np.pi / 2) * k**dx
            ft = np.cos(o * t + p + dt * np.pi / 2) * o**dt
            out += a * fx * ft
        return out

    def theta(x, t):
        ft_ = dfield(x, t, dt=1)
        fx_ = dfield(x, t, dx=1)
        f = field(x, t)
        lag = 0.5 * (-(-ft_**2 + fx_**2) - mu**2 * f**2)  # -1/2(dphi.dphi + mu^2 phi^2), eta=(-,+)
        T00 = ft_ * ft_ - (-1.0) * (-lag)
        T01 = ft_ * fx_
        T11 = fx_ * fx_ - (+1.0) * (-lag)
        return T00, T01, T11

    xs = np.linspace(0, 2 * np.pi, 41)[:-1]
    t0 = 0.37
    T00, T01, T11 = theta(xs, t0)
    check("T7a Theta_00 >= 0 pointwise", np.all(T00 >= -1e-12),
          f"min {T00.min():.3e}")

    # on-shell conservation: d^mu Theta_mu0 = -d_t T00 + d_x T01 -> 0
    def divergence(delta):
        T00p, _, _ = theta(xs, t0 + delta)
        T00m, _, _ = theta(xs, t0 - delta)
        dT00 = (T00p - T00m) / (2 * delta)
        _, T01p, _ = theta(xs + delta, t0)
        _, T01m, _ = theta(xs - delta, t0)
        dT01 = (T01p - T01m) / (2 * delta)
        return np.max(np.abs(-(-dT00) - dT01))  # eta^{00} d_0 = -d_t

    r1 = divergence(1e-2)
    r2 = divergence(5e-3)
    check("T7b on-shell conservation, O(delta^2) convergence",
          r1 / r2 > 3.5 and r1 / r2 < 4.5,
          f"residual ratio {r1 / r2:.2f} (expect 4)")

    # dust limit: single mode k << mu; time-averaged pressure/energy = k^2/omega^2
    def dust_ratio(kk):
        om = np.sqrt(mu**2 + kk**2)
        ts = np.linspace(0, 2 * np.pi / om, 401)[:-1]
        accP = accE = 0.0
        for t in ts:
            ft_ = -om * np.cos(kk * xs) * np.sin(om * t)
            fx_ = -kk * np.sin(kk * xs) * np.cos(om * t)
            f = np.cos(kk * xs) * np.cos(om * t)
            T00 = 0.5 * (ft_**2 + fx_**2 + mu**2 * f**2)
            T11 = 0.5 * (ft_**2 + fx_**2 - mu**2 * f**2)
            accP += T11.mean()
            accE += T00.mean()
        return accP / accE, kk**2 / om**2

    g1, p1 = dust_ratio(1.0)
    g2, p2 = dust_ratio(0.5)
    ok = abs(g1 / p1 - 1) < 1e-6 and abs(g2 / p2 - 1) < 1e-6
    check("T7c dust limit: <T_11>/<T_00> = k^2/omega^2 = O(eps^2)",
          ok, f"k=1: {g1:.5f} vs {p1:.5f}; k=0.5: {g2:.5f} vs {p2:.5f}")


def t8_chart_freedom():
    print("T8: chart redescription = linearised gauge transformation")
    # static metric built from explicit Fourier modes (exact anywhere)
    modes = []
    for _ in range(3):
        kv = rng.integers(-2, 3, size=3).astype(float) * 2 * np.pi
        amp = rng.normal(size=(4, 4)) * 1e-3
        amp = amp + amp.T
        ph = rng.uniform(0, 2 * np.pi)
        modes.append((kv, amp, ph))

    def h_at(pts):  # pts (..., 3) -> (..., 4, 4)
        out = np.zeros(pts.shape[:-1] + (4, 4))
        for kv, amp, ph in modes:
            c = np.cos(pts @ kv + ph)
            out += c[..., None, None] * amp
        return out

    def dh_at(pts):  # spatial gradient (..., 3, 4, 4)
        out = np.zeros(pts.shape[:-1] + (3, 4, 4))
        for kv, amp, ph in modes:
            s = -np.sin(pts @ kv + ph)
            out += s[..., None, None, None] * kv[:, None, None] * amp
        return out

    xi_modes = []
    for _ in range(2):
        kv = rng.integers(-2, 3, size=3).astype(float) * 2 * np.pi
        a4 = rng.normal(size=4)
        ph = rng.uniform(0, 2 * np.pi)
        xi_modes.append((kv, a4, ph))

    def xi_at(pts, s):  # xi^mu (upper), time-independent
        out = np.zeros(pts.shape[:-1] + (4,))
        for kv, a4, ph in xi_modes:
            c = np.cos(pts @ kv + ph)
            out += c[..., None] * a4
        return s * out

    def dxi_at(pts, s):  # d_i xi^mu  (..., 3, 4); time derivs vanish
        out = np.zeros(pts.shape[:-1] + (3, 4))
        for kv, a4, ph in xi_modes:
            sn = -np.sin(pts @ kv + ph)
            out += sn[..., None, None] * np.outer(kv, a4)
        return s * out

    pts = rng.uniform(0, 1, size=(200, 3))

    def residual(s):
        xiu = xi_at(pts, s)            # xi^mu at x'
        dxiu = dxi_at(pts, s)          # d_i xi^mu at x'
        xsrc = pts - xiu[:, 1:]        # x = x' - xi_spatial(x')
        g_src = h_at(xsrc)
        for m in range(4):
            g_src[:, m, m] += ETA[m, m]
        # Jacobian J[p, a, m] = d x^a / d x'^m = delta - d_m xi^a
        J = np.tile(np.eye(4), (len(pts), 1, 1))
        J[:, :, 1:] -= np.transpose(dxiu, (0, 2, 1))  # columns m=1..3: -d_m xi^a
        gp = np.einsum("pam,pbn,pab->pmn", J, J, g_src)
        h_new = gp.copy()
        for m in range(4):
            h_new[:, m, m] -= ETA[m, m]
        # prediction: dh = -xi^l d_l h - (d_mu eps_nu + d_nu eps_mu)
        #             - h_{a nu} d_mu xi^a - h_{mu b} d_nu xi^b
        h_here = h_at(pts)
        dh_here = dh_at(pts)
        adv = -np.einsum("pl,plmn->pmn", xiu[:, 1:], dh_here)
        deps = np.zeros((len(pts), 4, 4))
        # eps_mu = eta_{mu a} xi^a ; d_i eps_mu = eta_{mu a} d_i xi^a
        depslow = np.einsum("ma,pia->pim", ETA, dxiu)  # (p, i, mu)
        deps[:, 1:, :] += depslow
        deps = deps + np.transpose(deps, (0, 2, 1))
        hdx = np.einsum("pan,pma->pmn", h_here,
                        np.concatenate([np.zeros((len(pts), 1, 4)),
                                        dxiu], axis=1))
        pred = adv - deps - hdx - np.transpose(hdx, (0, 2, 1))
        got = h_new - h_here
        return np.max(np.abs(got - pred)), np.max(np.abs(got))

    (r1, _), (r2, _) = residual(1e-3), residual(5e-4)
    check("T8a chart shift matches gauge direction, O(xi^2) convergence",
          3.0 < r1 / r2 < 5.0, f"residual ratio {r1 / r2:.2f} (expect 4)")
    r3, g3 = residual(1e-4)
    check("T8b residual is a vanishing fraction of the shift",
          r3 / g3 < 0.02, f"relative residual {r3 / g3:.4f} at |xi| ~ 1e-4")


def t9_tt_waves():
    print("T9: TT waves ride the substrate light cone")
    kz = 0.9
    hp = np.zeros((4, 4))
    hp[1, 1], hp[2, 2] = 1.0, -1.0
    hx = np.zeros((4, 4))
    hx[1, 2] = hx[2, 1] = 1.0
    on, off = [], []
    for hTT in (hp, hx):
        k_on = np.array([kz, 0, 0, kz])
        k_off = np.array([1.25 * kz, 0, 0, kz])
        on.append(np.linalg.norm(E_of_h(hTT.astype(complex), k_on)))
        off.append(np.linalg.norm(E_of_h(hTT.astype(complex), k_off)))
    check("T9a h_+, h_x solve the FP equation at omega = c|k|",
          max(on) < 1e-12, f"|E| on-shell = {max(on):.2e}")
    check("T9b ...and fail it off-shell (omega != c|k|)",
          min(off) > 1e-3, f"|E| off-shell = {min(off):.2e}")


def t10_second_difference():
    print("T10: (H-wave) continuum step")
    f = lambda t: np.sin(1.3 * t + 0.4)
    fdd = lambda t: -1.3**2 * np.sin(1.3 * t + 0.4)
    t0 = 0.7

    def err(tau):
        return abs((f(t0 + tau) - 2 * f(t0) + f(t0 - tau)) / tau**2 - fdd(t0))

    r = err(1e-2) / err(5e-3)
    check("T10a second difference -> d_t^2 f at O(tau^2)",
          3.9 < r < 4.1, f"convergence ratio {r:.3f} (expect 4)")

    verts, A, Lg = load_600cell()
    lam, vecs = np.linalg.eigh(Lg)
    i = np.argmin(np.abs(lam - lam[lam > 1e-8][0]))  # first nonzero eigenvalue
    w = vecs[:, i]
    om_cont = np.sqrt(lam[i])

    def measured_omega(tau):
        Fm = w.copy()
        Fc = w * np.cos(om_cont * tau)  # seed near the mode oscillation
        ps = [w @ Fm, w @ Fc]
        for _ in range(40):
            Fp = 2 * Fc - Fm - tau**2 * (Lg @ Fc)
            Fm, Fc = Fc, Fp
            ps.append(w @ Fc)
        ps = np.array(ps)
        cosw = (ps[2:] + ps[:-2]) / (2 * ps[1:-1])
        return np.arccos(np.clip(cosw.mean(), -1, 1)) / tau

    e1 = abs(measured_omega(0.04) - om_cont)
    e2 = abs(measured_omega(0.02) - om_cont)
    check("T10b 600-cell eigenmode leapfrog frequency -> continuum, O(tau^2)",
          3.5 < e1 / e2 < 4.5, f"ratio {e1 / e2:.2f} (expect 4)")


def kg_packet(mu, k1, sig, n=2048, L=200.0):
    """Positive-frequency KG packet: exact spectral evolution."""
    x = np.arange(n) / n * L - L / 2
    k = 2 * np.pi * np.fft.fftfreq(n, d=L / n)
    psi0 = np.exp(-x**2 / (4 * sig**2)) * np.exp(1j * k1 * x)
    a = np.fft.fft(psi0)
    om = np.sqrt(mu**2 + k**2)
    return x, k, a, om


def t11_envelope_schrodinger():
    print("T11: Klein-Gordon envelope -> Schrodinger (massive end of C_phi)")

    def env_error(mu):
        sig = 5.0
        x, k, a, om = kg_packet(mu, 0.0, sig)
        # fixed physical Schrodinger time: t such that k_typ^2 t/(2 mu) = const
        t = 8.0 * mu
        exact = np.fft.ifft(a * np.exp(-1j * (om - mu) * t))
        schro = np.fft.ifft(a * np.exp(-1j * (k**2 / (2 * mu)) * t))
        return np.max(np.abs(exact - schro)) / np.max(np.abs(exact))

    e1, e2 = env_error(2.0), env_error(4.0)
    check("T11a envelope error is O(eps^2): doubling mu quarters it",
          3.5 < e1 / e2 < 4.5, f"errors {e1:.2e} -> {e2:.2e}, ratio {e1/e2:.2f}")
    check("T11b error is small in the regime of validity",
          e2 < 5e-3, f"{e2:.2e}")


def t12_equivalence_principle():
    print("T12: inertial mass = gravitating mass on one packet")
    mu, k1, sig = 8.0, 0.8, 6.0
    x, k, a, om = kg_packet(mu, k1, sig)
    n, L = len(x), x[-1] - x[0] + (x[1] - x[0])
    dx = L / n

    def field_at(t):
        Phi = np.fft.ifft(a * np.exp(-1j * om * t))
        Phid = np.fft.ifft(-1j * om * a * np.exp(-1j * om * t))
        Phix = np.fft.ifft(1j * k * a * np.exp(-1j * om * t))
        return Phi, Phid, Phix

    # group velocity from centroid drift
    t1, t2 = 0.0, 6.0
    cents = []
    for t in (t1, t2):
        Phi, _, _ = field_at(t)
        w = np.abs(Phi) ** 2
        cents.append(np.sum(x * w) / np.sum(w))
    vg = (cents[1] - cents[0]) / (t2 - t1)

    Phi, Phid, Phix = field_at(0.0)
    T00 = (np.abs(Phid) ** 2 + np.abs(Phix) ** 2
           + mu**2 * np.abs(Phi) ** 2)
    E = np.sum(T00) * dx
    P = -np.sum(np.conj(Phid) * Phix + np.conj(Phix) * Phid).real * dx
    Q = (1j * np.sum(np.conj(Phi) * Phid - Phi * np.conj(Phid))).real * dx

    m_grav = E / Q                # energy per quantum = relativistic mass
    p_per_q = P / Q
    m_inert = p_per_q / vg        # inertia: p = m v
    rel = abs(m_inert / m_grav - 1)
    check("T12a gravitating mass (T_00/quantum) = inertial mass (p/v)",
          rel < 5e-3, f"m_grav = {m_grav:.4f}, m_inert = {m_inert:.4f}, "
          f"rel dev {rel:.1e}")
    check("T12b both equal the carrier mass mu at O(eps^2)",
          abs(m_grav / mu - 1) < 0.02,
          f"m/mu = {m_grav / mu:.5f} (eps^2 = {(k1/mu)**2 + (1/(2*sig*mu))**2:.4f})")


def t13_maxwell():
    print("T13: same mechanism one rank down -> Maxwell")
    rows = []
    for _ in range(40):
        k = rng.normal(size=4)
        kup = ETA @ k
        A1 = rng.normal(size=4)
        chi = rng.normal()
        G = k * chi  # gauge direction
        kk = k @ ETA @ k
        C1 = kk * (A1 @ ETA @ G)
        C2 = (kup @ A1) * (kup @ G)
        Cm = A1 @ ETA @ G
        rows.append([C1, C2, Cm])
    rows = np.array(rows)
    u, s, vt = np.linalg.svd(rows)
    nullity = int(np.sum(s < 1e-10 * s[0]))
    v = vt[-1] / vt[-1][0]
    check("T13a rank-1 scan: 1-dim null space", nullity == 1)
    check("T13b ratios (1, -1, 0) = Maxwell, photon massless",
          np.allclose(v, [1.0, -1.0, 0.0], atol=1e-9),
          f"found {np.round(v, 6)}")
    # polarisations at null k: ker(Maxwell op) = {A : k.A = 0} (3) / gauge (1) = 2
    kz = 1.1
    k = np.array([kz, 0, 0, kz])
    kup = ETA @ k
    kk = 0.0
    Kmat = kk * ETA - np.outer(kup, kup)  # E(A)_nu ~ kk A_nu - k_nu (k.A)
    s2 = np.linalg.svd(Kmat, compute_uv=False)
    kerdim = int(np.sum(s2 < 1e-12 * max(s2[0], 1)))
    check("T13c photon polarisations = 3 - 1 = 2", kerdim - 1 == 2,
          f"kernel dim {kerdim}, gauge dim 1")


def t14_substrate_tensoriality():
    print("T14: rank-2 tensoriality of the coarse bilinear on V_600")
    verts, A, Lg = load_600cell()
    n = len(verts)
    keys = {tuple(np.round(v, 8)): i for i, v in enumerate(verts)}

    def qmul(q1, q2):
        a_, b, c, d = q1
        e, f, g, h_ = q2
        return np.array([a_*e - b*f - c*g - d*h_,
                         a_*f + b*e + c*h_ - d*g,
                         a_*g - b*h_ + c*e + d*f,
                         a_*h_ + b*g - c*f + d*e])

    def qconj(q):
        return np.array([q[0], -q[1], -q[2], -q[3]])

    QB = [np.array([0, 1, 0, 0.]), np.array([0, 0, 1, 0.]),
          np.array([0, 0, 0, 1.])]

    nbrs = [np.nonzero(A[v])[0] for v in range(n)]

    def h_of(F):
        H = np.zeros((n, 3, 3))
        for v in range(n):
            e = np.stack([qmul(verts[v], q) for q in QB])  # (3, 4) frame
            tw = verts[nbrs[v]] - verts[v]                 # (12, 4)
            comp = tw @ e.T                                # (12, 3)
            dF = F[nbrs[v]] - F[v]                         # (12, 4)
            grad = comp.T @ dF                             # (3, 4)
            H[v] = grad @ grad.T
        return H

    F = rng.normal(size=(n, 4))
    H = h_of(F)

    g = verts[rng.integers(n)]
    while abs(abs(g[0]) - 1) < 1e-9:  # avoid +-1 (trivial rotation)
        g = verts[rng.integers(n)]

    # left action: (g.F)(v) = F(g v); frame components transport trivially
    permL = np.array([keys[tuple(np.round(qmul(g, v), 8))] for v in verts])
    HL = h_of(F[permL])
    errL = np.max(np.abs(HL - H[permL]))
    check("T14a left 2I action: h transports as a scalar field of frames",
          errL < 1e-10, f"max dev {errL:.2e}")

    # right action: (g.F)(v) = F(v g); frame rotates by Ad(g)
    permR = np.array([keys[tuple(np.round(qmul(v, g), 8))] for v in verts])
    HR = h_of(F[permR])
    R = np.array([[qmul(qmul(g, qb), qconj(g))[1 + a] for a in range(3)]
                  for qb in QB])  # R[b, a] = <q_a, g q_b g^-1>
    cand1 = np.einsum("ab,vbc,dc->vad", R.T, H[permR], R.T)
    cand2 = np.einsum("ab,vbc,dc->vad", R, H[permR], R)
    err1 = np.max(np.abs(HR - cand1))
    err2 = np.max(np.abs(HR - cand2))
    check("T14b right 2I action: h rotates as a rank-2 tensor (Ad(g))",
          min(err1, err2) < 1e-10,
          f"residuals {err1:.2e} / {err2:.2e} (one must vanish)")
    PR = np.zeros((n, n))
    PR[np.arange(n), permR] = 1.0
    comm = np.max(np.abs(PR @ Lg - Lg @ PR))
    check("T14c coarse kernel commutes with the action (pi_r equivariant)",
          comm < 1e-12, f"|[P, L]| = {comm:.2e}")


def t15_collective_quadratic():
    print("T15: collective-field effective action is quadratic (Wishart)")
    d = 3
    S0 = np.array([[2.0, 0.3, 0.1], [0.3, 1.5, 0.2], [0.1, 0.2, 1.0]])
    S0inv = np.linalg.inv(S0)
    D = rng.normal(size=(d, d))
    D = D + D.T

    def gamma(s, N):
        X = S0inv @ (s * D)
        sign, logdet = np.linalg.slogdet(np.eye(d) + X)
        return (N / 2.0) * (np.trace(X) - logdet)

    N = 4000
    s = 1e-3
    quad_num = gamma(s, N) + gamma(-s, N)        # 2 * quadratic + O(s^4)
    quad_pred = 2 * (N / 4.0) * s**2 * np.trace((S0inv @ D) @ (S0inv @ D))
    check("T15a quadratic coefficient = (N/4) tr((S0^-1 dh)^2)",
          abs(quad_num / quad_pred - 1) < 1e-4,
          f"ratio {quad_num / quad_pred:.6f}")

    def cubic_over_quad(N):
        sstar = 1.0 / np.sqrt(N)
        cub = (gamma(sstar, N) - gamma(-sstar, N)) / 2.0  # odd part ~ cubic
        quad = (gamma(sstar, N) + gamma(-sstar, N)) / 2.0
        return abs(cub / quad)

    r1, r4 = cubic_over_quad(1000), cubic_over_quad(16000)
    check("T15b cubic/quadratic at fluctuation scale falls as N^{-1/2}",
          3.0 < r1 / r4 < 5.3, f"ratio {r1 / r4:.2f} (expect 4)")

    # empirical premise: sample second-moment fluctuations scale as N^{-1/2}
    def fluct(N, reps=200):
        devs = []
        for _ in range(reps):
            Xs = rng.multivariate_normal(np.zeros(d), S0, size=N)
            Sh = Xs.T @ Xs / N
            devs.append(np.linalg.norm(Sh - S0))
        return np.mean(devs)

    f1, f4 = fluct(500), fluct(8000)
    check("T15c empirical d h ~ N^{-1/2}",
          3.0 < f1 / f4 < 5.3, f"ratio {f1 / f4:.2f} (expect 4)")


def main():
    print("=" * 70)
    print("GR closure verification — docs/gr-closure-derivation.md")
    print("=" * 70)
    t1_fp_uniqueness()
    t2_polarisations()
    t3a_variation_is_einstein()
    t3_grid_solve()
    t4_light_bending()
    t5_t6_substrate_conservation()
    t7_stress_tensor()
    t8_chart_freedom()
    t9_tt_waves()
    t10_second_difference()
    t11_envelope_schrodinger()
    t12_equivalence_principle()
    t13_maxwell()
    t14_substrate_tensoriality()
    t15_collective_quadratic()
    print("=" * 70)
    print(f"SUMMARY: {len(PASS)} PASS, {len(FAIL)} FAIL")
    for name in FAIL:
        print(f"  FAILED: {name}")
    return 0 if not FAIL else 1


if __name__ == "__main__":
    raise SystemExit(main())
