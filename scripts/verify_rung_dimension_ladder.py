#!/usr/bin/env python3
"""
Verify the rung-dimension-ladder derivations of docs/rung-dimension-ladder.md
(hardened successor to scripts/explore_rung_dimension_ladder.py):

  L1 (nesting): V_16 (tesseract) subset of V_24 (24-cell) subset of V_120
     (600-cell) as point sets on S^3 — the rungs sample ONE arena.

  L2 (intertwiner, S^3 rungs): for each rung X and harmonic level k, the
     restriction res_k : H_k(S^3) -> R^X of continuum S^3 harmonics
     (a) has rank (k+1)^2 for k <= k_max(X) (injectivity), and
     (b) satisfies A_X res_k = a_k(X) res_k with the SU(2) character scalar
         a_k(X) = deg_X * sin((k+1)theta_X) / ((k+1) sin theta_X),
     so the rung's harmonic eigenspaces ARE the sampled continuum harmonics.

  L3 (intertwiner, S^7 rung): same for the 240 unit octavians (E8 roots)
     with the Gegenbauer scalar a_k = 56 * C_k^{(3)}(1/2) / C_k^{(3)}(1):
     predicted Laplacian eigenvalues 28, 48, 58 (k = 1..3, injective) and
     60 (k = 4, aliased: rank 84 < dim H_4 = 294).

  L4 (nested sampling): the fine rung's harmonic eigenspace, restricted to
     the coarse rung's vertices, spans exactly the coarse rung's harmonic
     eigenspace (V_120 -> V_24 for k <= 2; V_24 -> V_16 for k <= 1).

  L5 (aliasing mechanisms):
     - fold (irrep splitting): res_6 on V_120 has rank 25 and lands in the
       primed blocks lambda = 14.4721 (3') and 15.0000 (4');
     - kernel (sparse sampling): res_2 on the tesseract has rank 6
       (kernel 3 = span{x_i^2 - x_j^2}) and lands in the lambda = 4 block,
       at the eigenvalue still predicted by the dispersion formula.

Usage:
    python scripts/verify_rung_dimension_ladder.py
"""
from __future__ import annotations

import itertools
import numpy as np
from math import factorial
from pathlib import Path

PHI = (1 + np.sqrt(5)) / 2
DATA_PATH = Path(__file__).resolve().parent / "600cell_data.npz"
RNG = np.random.default_rng(600)

PASS, FAIL = [], []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


# ---------------------------------------------------------------- geometry
def build_24cell():
    verts = []
    for i in range(4):
        for s in (1.0, -1.0):
            v = np.zeros(4); v[i] = s
            verts.append(v)
    for signs in itertools.product((0.5, -0.5), repeat=4):
        verts.append(np.array(signs))
    return np.array(verts)


def build_tesseract():
    return np.array([np.array(s) for s in itertools.product((0.5, -0.5), repeat=4)])


def build_e8_units():
    roots = []
    for i, j in itertools.combinations(range(8), 2):
        for si, sj in itertools.product((1.0, -1.0), repeat=2):
            v = np.zeros(8); v[i] = si; v[j] = sj
            roots.append(v)
    for signs in itertools.product((0.5, -0.5), repeat=8):
        if sum(1 for s in signs if s < 0) % 2 == 0:
            roots.append(np.array(signs))
    return np.array(roots) / np.sqrt(2)


def graph_of(verts, ip_edge):
    G = verts @ verts.T
    A = (np.abs(G - ip_edge) < 1e-8).astype(float)
    np.fill_diagonal(A, 0.0)
    deg = A.sum(axis=1)
    assert np.allclose(deg, deg[0])
    L = np.diag(deg) - A
    return A, L, int(deg[0])


def eigenblocks(L):
    evals, evecs = np.linalg.eigh(L)
    r = np.round(evals, 6)
    blocks = {}
    for lam in sorted(set(r.tolist())):
        blocks[float(lam)] = evecs[:, r == lam]
    return blocks


def nearest_block(blocks, lam, tol=1e-4):
    for l, E in blocks.items():
        if abs(l - lam) < tol:
            return l, E
    return None, None


# ------------------------------------------------------- zonal harmonics
def cheb_u(k, x):
    """U_k(x): zonal S^3 harmonic kernel, U_k(cos g) = sin((k+1)g)/sin g."""
    if k == 0:
        return np.ones_like(x)
    um, u = np.ones_like(x), 2 * x
    for _ in range(k - 1):
        um, u = u, 2 * x * u - um
    return u


def gegenbauer3(k, x):
    """C_k^{(3)}(x): zonal S^7 harmonic kernel."""
    if k == 0:
        return np.ones_like(x)
    cm, c = np.ones_like(x), 6 * x
    for n in range(2, k + 1):
        cm, c = c, (2 * (n + 2) * x * c - (n + 4) * cm) / n
    return c


def res_basis(verts, k, kernel, n_dim_ambient):
    """Matrix whose columns span res_k(H_k(S^{n-1})) on the vertex set."""
    dim_y = 4 * max(20, n_dim_ambient)
    Y = RNG.normal(size=(dim_y, verts.shape[1]))
    Y /= np.linalg.norm(Y, axis=1, keepdims=True)
    return kernel(k, verts @ Y.T)


def rank_of(M, tol=1e-8):
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > tol * s[0]))


def scalar_action_residual(A, M, a):
    return np.linalg.norm(A @ M - a * M) / np.linalg.norm(M)


def containment_residual(E, M):
    """||(I - E E^T) M|| / ||M||: how much of span(M) lies outside span(E)."""
    return np.linalg.norm(M - E @ (E.T @ M)) / np.linalg.norm(M)


def dim_Hk_S7(k):
    return (2 * k + 6) * factorial(k + 5) // (factorial(k) * 720)


# ---------------------------------------------------------------- main
def main():
    print("=" * 72)
    print("RUNG DIMENSION LADDER: intertwiner verification")
    print("=" * 72)

    v600 = np.load(DATA_PATH)["vertices"]
    v24 = build_24cell()
    v16 = build_tesseract()
    e8 = build_e8_units()

    # ---------------- L1: nesting ----------------
    print("\n--- L1: nested sampling of one S^3 ---")
    key600 = {tuple(np.round(v, 8)) for v in v600}
    key24 = {tuple(np.round(v, 8)) for v in v24}
    in120 = all(tuple(np.round(v, 8)) in key600 for v in v24)
    in24 = all(tuple(np.round(v, 8)) in key24 for v in v16)
    check("L1a: V_24 (Hurwitz units) subset of V_120 (icosians)", in120)
    check("L1b: V_16 (tesseract) subset of V_24 (24-cell)", in24)

    idx24_in_600 = [int(np.argmin(np.linalg.norm(v600 - v, axis=1))) for v in v24]
    idx16_in_24 = [int(np.argmin(np.linalg.norm(v24 - v, axis=1))) for v in v16]

    # ---------------- rung graphs ----------------
    A600, L600, d600 = graph_of(v600, PHI / 2)
    A24, L24, d24 = graph_of(v24, 0.5)
    A16, L16, d16 = graph_of(v16, 0.5)
    Ae8, Le8, de8 = graph_of(e8, 0.5)
    B600, B24, B16, Be8 = (eigenblocks(L) for L in (L600, L24, L16, Le8))

    # ---------------- L2: S^3 intertwiner ----------------
    print("\n--- L2: intertwiner on the S^3 rungs ---")
    rungs = [
        ("H4/V_600", v600, A600, B600, d600, np.pi / 5, 5),
        ("D4/24-cell", v24, A24, B24, d24, np.pi / 3, 2),
        ("16/tesseract", v16, A16, B16, d16, np.pi / 3, 1),
    ]
    for label, V, A, B, deg, theta, kmax in rungs:
        for k in range(kmax + 1):
            M = res_basis(V, k, cheb_u, (k + 1) ** 2)
            a_k = deg * np.sin((k + 1) * theta) / ((k + 1) * np.sin(theta))
            rk = rank_of(M)
            res = scalar_action_residual(A, M, a_k)
            lam = deg - a_k
            _, E = nearest_block(B, lam)
            cont = containment_residual(E, M) if E is not None else np.inf
            ok = (rk == (k + 1) ** 2) and res < 1e-8 and cont < 1e-8
            check(f"L2 {label} k={k}: rank {(k+1)**2}, scalar a_k, in lam={lam:.4f}",
                  ok, f"rank {rk}, action res {res:.1e}, containment {cont:.1e}")

    # ---------------- L3: S^7 intertwiner (E8 rung) ----------------
    print("\n--- L3: intertwiner on the S^7 rung (240 unit octavians) ---")
    for k in range(1, 5):
        a_k = de8 * gegenbauer3(k, np.array([0.5]))[0] / gegenbauer3(k, np.array([1.0]))[0]
        lam = de8 - a_k
        M = res_basis(e8, k, gegenbauer3, dim_Hk_S7(k))
        rk = rank_of(M)
        res = scalar_action_residual(Ae8, M, a_k)
        _, E = nearest_block(Be8, lam)
        cont = containment_residual(E, M) if E is not None else np.inf
        if k <= 3:
            ok = (rk == dim_Hk_S7(k)) and res < 1e-8 and cont < 1e-8
            check(f"L3 E8 k={k}: rank {dim_Hk_S7(k)} (injective), Gegenbauer "
                  f"a_k -> lam={lam:.4f}", ok,
                  f"rank {rk}, action res {res:.1e}, containment {cont:.1e}")
        else:
            ok = (rk == 84) and res < 1e-8 and cont < 1e-8
            check(f"L3 E8 k=4: ALIASED rank 84 < dim H_4 = {dim_Hk_S7(4)}, "
                  f"lam={lam:.4f}", ok,
                  f"rank {rk}, action res {res:.1e}, containment {cont:.1e}")

    # ---------------- L4: nested sampling intertwines ----------------
    print("\n--- L4: coarse-rung fields = fine-rung fields, sampled ---")
    for k in range(0, 3):
        lam120 = d600 - d600 * np.sin((k + 1) * np.pi / 5) / ((k + 1) * np.sin(np.pi / 5))
        _, E120 = nearest_block(B600, lam120)
        S = E120[idx24_in_600, :]                      # sample on the 24 sub-vertices
        lam24 = d24 - d24 * np.sin((k + 1) * np.pi / 3) / ((k + 1) * np.sin(np.pi / 3))
        _, E24 = nearest_block(B24, lam24)
        rk, cont = rank_of(S), containment_residual(E24, S)
        ok = (rk == (k + 1) ** 2) and cont < 1e-8
        check(f"L4a V_120 -> V_24, k={k}: sampled eigenspace spans 24-cell "
              f"lam={lam24:.4f} block", ok, f"rank {rk}, containment {cont:.1e}")
    for k in range(0, 2):
        lam24 = d24 - d24 * np.sin((k + 1) * np.pi / 3) / ((k + 1) * np.sin(np.pi / 3))
        _, E24 = nearest_block(B24, lam24)
        S = E24[idx16_in_24, :]
        lam16 = d16 - d16 * np.sin((k + 1) * np.pi / 3) / ((k + 1) * np.sin(np.pi / 3))
        _, E16 = nearest_block(B16, lam16)
        rk, cont = rank_of(S), containment_residual(E16, S)
        ok = (rk == (k + 1) ** 2) and cont < 1e-8
        check(f"L4b V_24 -> V_16, k={k}: sampled eigenspace spans tesseract "
              f"lam={lam16:.4f} block", ok, f"rank {rk}, containment {cont:.1e}")

    # ---------------- L5: aliasing mechanisms ----------------
    print("\n--- L5: the two cutoff mechanisms ---")
    # fold: V_6|_2I = 3' + 4' -> res_6 splits into primed blocks
    M6 = res_basis(v600, 6, cheb_u, 49)
    rk6 = rank_of(M6)
    _, E3p = nearest_block(B600, 14.472136)
    _, E4p = nearest_block(B600, 15.0)
    Eprimed = np.hstack([E3p, E4p])
    cont6 = containment_residual(Eprimed, M6)
    check("L5a fold: res_6 on V_120 has rank 25 = 9 + 16 inside the primed "
          "blocks 14.4721 (3') + 15.0000 (4')", rk6 == 25 and cont6 < 1e-8,
          f"rank {rk6}, containment {cont6:.1e}")
    # kernel: res_2 on tesseract has rank 6, lands at the dispersion-predicted
    # eigenvalue lam = 4 (a_2 = 0); kernel 3 = span{x_i^2 - x_j^2}
    M2 = res_basis(v16, 2, cheb_u, 9)
    rk2 = rank_of(M2)
    _, E4 = nearest_block(B16, 4.0)
    cont2 = containment_residual(E4, M2)
    res2 = scalar_action_residual(A16, M2, 0.0)
    check("L5b kernel: res_2 on tesseract has rank 6 (kernel 3) inside "
          "lam = 4, at the dispersion-predicted a_2 = 0",
          rk2 == 6 and cont2 < 1e-8 and res2 < 1e-8,
          f"rank {rk2}, containment {cont2:.1e}, action res {res2:.1e}")
    # explicit kernel witness: x_1^2 - x_2^2 vanishes on all tesseract vertices
    w = v16[:, 0] ** 2 - v16[:, 1] ** 2
    check("L5c kernel witness: (x_1^2 - x_2^2)|_tesseract = 0",
          np.allclose(w, 0.0))

    print("\n" + "=" * 72)
    print(f"SUMMARY: {len(PASS)} PASS, {len(FAIL)} FAIL")
    for n in FAIL:
        print(f"  FAILED: {n}")
    print("=" * 72)
    return 0 if not FAIL else 1


if __name__ == "__main__":
    raise SystemExit(main())
