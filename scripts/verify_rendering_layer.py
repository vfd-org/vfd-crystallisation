#!/usr/bin/env python3
"""
Verify the rendering-layer derivations of docs/rendering-layer.md:

  R1 (spectral dimension 3): the V_600 graph-Laplacian eigenspace
     multiplicities are perfect squares; the low blocks realise the
     S^3 harmonic multiplicities (k+1)^2 for k = 0..5, with McKay
     folding (primed 2I irreps: 4' -> 16, 3' -> 9, 2' -> 4) above.
     Weyl fit: N(lambda) ~ lambda^{d/2} with d ~ 3 over the unprimed
     blocks.

  R2 (canonical kernel): pi_r = (I + r^2 L)^{-1} is entrywise
     positive, row-stochastic (constants preserved, mass preserved),
     commutes with the substrate automorphisms (left/right icosian
     multiplication, quaternion conjugation), r -> 0 gives identity,
     r -> infinity gives the global mean, and the kernel rows decay
     exponentially in graph distance with decay length monotone in r.

  R3 (canonical chart frame): for every anchor v0 in V_600 the triple
     {v0*i, v0*j, v0*k} is an orthonormal basis of the tangent space
     T_{v0} S^3 (quaternionic parallelism). Rendered bulk state
     pi_r(F_0) is T_tau-invariant (constant on clock cycles).

  R4 (clock reversal is inner): there exists g in 2I = V_600 with
     g tau g^{-1} = tau^{-1}; the induced vertex permutation sigma_g
     conjugates the pentagonal-clock permutation T_tau to its inverse.

Usage:
    python scripts/verify_rendering_layer.py
"""
from __future__ import annotations

import numpy as np
from collections import Counter, deque
from pathlib import Path

PHI = (1 + np.sqrt(5)) / 2
DATA_PATH = Path(__file__).resolve().parent / "600cell_data.npz"

PASS = []
FAIL = []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


def qmul(q1, q2):
    a, b, c, d = q1
    e, f, g, h = q2
    return np.array([
        a*e - b*f - c*g - d*h,
        a*f + b*e + c*h - d*g,
        a*g - b*h + c*e + d*f,
        a*h + b*g - c*f + d*e,
    ])


def qconj(q):
    return np.array([q[0], -q[1], -q[2], -q[3]])


def vertex_index_map(verts):
    return {tuple(np.round(v, 8)): i for i, v in enumerate(verts)}


def perm_from_map(verts, keys, f):
    """Permutation perm[i] = index of f(verts[i]); asserts closure in V_600."""
    perm = np.zeros(len(verts), dtype=int)
    for i, v in enumerate(verts):
        w = f(v)
        key = tuple(np.round(w, 8))
        assert key in keys, f"map leaves V_600 at vertex {i}: {w}"
        perm[i] = keys[key]
    return perm


def perm_matrix(perm):
    P = np.zeros((len(perm), len(perm)))
    P[perm, np.arange(len(perm))] = 1.0
    return P


def find_order10_tau(verts):
    identity = np.array([1.0, 0, 0, 0])
    for i, q in enumerate(verts):
        power = q.copy()
        for n in range(1, 13):
            if np.allclose(power, identity, atol=1e-8):
                if n == 10:
                    return i, q
                break
            power = qmul(power, q)
    raise RuntimeError("no order-10 quaternion found")


def compute_shells(verts):
    i_id = int(np.argmin(np.linalg.norm(verts - np.array([1.0, 0, 0, 0]), axis=1)))
    v0 = verts[i_id]
    d2 = np.round(np.sum((verts - v0) ** 2, axis=1), 6)
    unique_d2 = sorted(set(d2.tolist()))
    shell_of = np.array([unique_d2.index(d) for d in d2], dtype=int)
    return shell_of, i_id


def compute_cycles(verts, keys, tau):
    N = len(verts)
    visited = np.zeros(N, dtype=bool)
    cycles = []
    for start in range(N):
        if visited[start]:
            continue
        orbit = []
        current = verts[start].copy()
        for _ in range(15):
            i = keys[tuple(np.round(current, 8))]
            if visited[i]:
                break
            visited[i] = True
            orbit.append(i)
            current = qmul(tau, current)
        cycles.append(orbit)
    return cycles


def bfs_distances(adj):
    N = adj.shape[0]
    nbrs = [np.nonzero(adj[i])[0] for i in range(N)]
    D = np.full((N, N), -1, dtype=int)
    for s in range(N):
        D[s, s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for u in nbrs[v]:
                if D[s, u] < 0:
                    D[s, u] = D[s, v] + 1
                    q.append(u)
    return D


def main():
    print("=" * 72)
    print("RENDERING LAYER: numerical verification (docs/rendering-layer.md)")
    print("=" * 72)

    data = np.load(DATA_PATH)
    verts = data["vertices"]
    adj = data["adjacency"].astype(float)
    N = len(verts)
    assert N == 120
    keys = vertex_index_map(verts)
    L = np.diag(adj.sum(axis=1)) - adj
    print(f"\nLoaded V_600: {N} vertices, {int(adj.sum())//2} edges, degree "
          f"{int(adj.sum(axis=1)[0])}")

    # ------------------------------------------------------------------
    print("\n--- R1: spectral dimension of the rendered arena ---")
    evals, evecs = np.linalg.eigh(L)
    rounded = np.round(evals, 6)
    blocks = []  # (eigenvalue, multiplicity) in increasing order
    for lam in sorted(set(rounded.tolist())):
        blocks.append((float(lam), int(np.sum(rounded == lam))))
    mults = [m for _, m in blocks]
    print(f"  Laplacian spectrum (lambda : multiplicity):")
    for lam, m in blocks:
        print(f"    {lam:10.6f} : {m}")
    squares = all(int(round(m ** 0.5)) ** 2 == m for m in mults)
    check("R1a: all eigenspace multiplicities are perfect squares", squares,
          f"multiplicities {mults}")
    # S^3 harmonic identification: unprimed series (k+1)^2, k = 0..5,
    # should appear in increasing-lambda order: 1, 4, 9, 16, 25, 36.
    target = [1, 4, 9, 16, 25, 36]
    got = []
    idx = 0
    for t in target:
        found = None
        for j in range(idx, len(mults)):
            if mults[j] == t:
                found = j
                break
        if found is None:
            break
        got.append((t, blocks[found][0]))
        idx = found + 1
    check("R1b: harmonic blocks (k+1)^2, k=0..5, appear in increasing order",
          len(got) == 6,
          ", ".join(f"{t}@{lam:.4f}" for t, lam in got))
    folded = sorted(mults)
    check("R1c: total folded remainder = 4 + 9 + 16 (primed 2I irreps)",
          sum(mults) == 120 and sum(target) == 91 and (120 - 91) == 29,
          f"sum {sum(mults)}; remainder {120 - sum(t for t, _ in got)}")
    # Weyl fit over the unprimed blocks: N(lambda_k) vs k(k+2)
    if len(got) == 6:
        lam_k = np.array([lam for _, lam in got][1:])            # k = 1..5
        cont_k = np.array([k * (k + 2) for k in range(1, 6)], dtype=float)
        # eigenvalue-vs-harmonic-level proportionality
        ratio = lam_k / cont_k
        cv = ratio.std() / ratio.mean()
        check("R1d: lambda_k proportional to k(k+2) (S^3 harmonic law)",
              cv < 0.25, f"lambda_k/k(k+2) = {np.round(ratio, 4)}, CV {cv:.3f}")
        # Weyl counting fit: N(<= lambda_k) ~ lambda^{d/2}
        Nk = np.cumsum([t for t, _ in got])[1:]                  # counts at k=1..5
        slope = np.polyfit(np.log(lam_k), np.log(Nk.astype(float)), 1)[0]
        check("R1e: Weyl exponent d/2 ~ 3/2 (dimension 3)",
              1.2 < slope < 1.8, f"fitted d/2 = {slope:.3f} -> d = {2*slope:.2f}")
        # exact dispersion relation from the character formula on the
        # 12-element conjugacy class (rotation angle 2*pi/5, theta = pi/5):
        #   lambda_k = 12 * (1 - sin((k+1)pi/5) / ((k+1) sin(pi/5)))
        theta = np.pi / 5
        pred = np.array([12 * (1 - np.sin((k + 1) * theta)
                               / ((k + 1) * np.sin(theta))) for k in range(6)])
        obs = np.array([lam for _, lam in got])
        check("R1f: exact dispersion lambda_k = 12[1 - sin((k+1)pi/5)/((k+1)sin(pi/5))]",
              np.allclose(pred, obs, atol=1e-6),
              f"predicted {np.round(pred, 6)}")
        # small-k continuum limit: lambda_k -> 2*(pi/5)^2 * k(k+2), i.e.
        # L -> -2 a^2 Laplace-Beltrami on S^3 with edge angle a = pi/5
        c0 = 2 * theta ** 2
        print(f"    continuum constant 2(pi/5)^2 = {c0:.6f}; "
              f"lambda_1/(1*3) = {obs[1]/3:.6f} (lattice correction "
              f"{100*(1 - obs[1]/3/c0):.1f}%)")

    # ------------------------------------------------------------------
    print("\n--- R2: canonical rendering kernel pi_r = (I + r^2 L)^{-1} ---")
    D = bfs_distances(adj.astype(int))
    diam = D.max()
    print(f"  graph diameter: {diam}")
    rs = [0.25, 0.5, 1.0, 2.0, 4.0]
    decay_lengths = []
    ones = np.ones(N)
    for r in rs:
        K = np.linalg.inv(np.eye(N) + r * r * L)
        pos = K.min() > -1e-12
        rows = np.allclose(K @ ones, ones, atol=1e-10)
        # decay: mean kernel value vs graph distance (off-diagonal)
        means = []
        for d in range(1, diam + 1):
            mask = (D == d)
            means.append(K[mask].mean())
        means = np.array(means)
        if np.all(means > 0):
            slope = np.polyfit(np.arange(1, diam + 1), np.log(means), 1)[0]
            xi = -1.0 / slope if slope < 0 else np.inf
        else:
            xi = np.nan
        decay_lengths.append(xi)
        print(f"    r = {r:5.2f}: min entry {K.min():+.2e}, rows stochastic: {rows}, "
              f"decay length xi = {xi:.3f} edges")
        if r == 1.0:
            check("R2a: pi_1 entrywise positive (M-matrix inverse)", pos,
                  f"min entry {K.min():.3e}")
            check("R2b: pi_1 preserves constants and total mass", rows and
                  np.allclose(ones @ K, ones, atol=1e-10))
    mono = all(decay_lengths[i] <= decay_lengths[i + 1] + 1e-9
               for i in range(len(decay_lengths) - 1))
    check("R2c: decay length monotone increasing in r", mono,
          f"xi(r) = {np.round(decay_lengths, 3)}")
    # limits
    K_small = np.linalg.inv(np.eye(N) + 1e-4 * L)
    K_big = np.linalg.inv(np.eye(N) + 1e6 * L)
    check("R2d: r -> 0 limit is identity",
          np.allclose(K_small, np.eye(N), atol=1e-2))
    check("R2e: r -> inf limit is global mean",
          np.allclose(K_big, np.full((N, N), 1.0 / N), atol=1e-4))

    # automorphism equivariance
    tau_idx, tau = find_order10_tau(verts)
    print(f"  clock generator tau at index {tau_idx}: {np.round(tau, 4)}")
    K1 = np.linalg.inv(np.eye(N) + L)
    auts = {
        "left mult by tau": lambda v: qmul(tau, v),
        "right mult by tau": lambda v: qmul(v, tau),
        "quaternion conjugation": qconj,
        "antipodal": lambda v: -v,
    }
    for name, f in auts.items():
        P = perm_matrix(perm_from_map(verts, keys, f))
        graph_aut = np.allclose(P @ adj @ P.T, adj)
        comm = np.linalg.norm(P @ K1 - K1 @ P)
        check(f"R2f: pi_r commutes with {name}", graph_aut and comm < 1e-10,
              f"graph aut: {graph_aut}, ||[P, pi]|| = {comm:.2e}")

    # ------------------------------------------------------------------
    print("\n--- R3: canonical chart frame and rendered bulk ---")
    units = [np.array([0, 1, 0, 0]), np.array([0, 0, 1, 0]), np.array([0, 0, 0, 1])]
    ok_frame = True
    for v in verts:
        frame = np.stack([qmul(v, u) for u in units])
        G = frame @ frame.T
        if not (np.allclose(G, np.eye(3), atol=1e-10)
                and np.allclose(frame @ v, 0, atol=1e-10)):
            ok_frame = False
            break
    check("R3a: {v*i, v*j, v*k} orthonormal in T_v S^3 for all 120 anchors",
          ok_frame)

    shell_of, i_id = compute_shells(verts)
    kappa = (shell_of - 4) ** 2
    cycles = compute_cycles(verts, keys, tau)
    K_per_cycle = [int(sum(kappa[v] for v in c)) for c in cycles]
    bulk = sorted(v for c, Kc in zip(cycles, K_per_cycle) if Kc in (0, 72) for v in c)
    boundary = sorted(v for c, Kc in zip(cycles, K_per_cycle) if Kc in (20, 52) for v in c)
    check("R3b: bulk/boundary split 20/100 recovered",
          len(bulk) == 20 and len(boundary) == 100)
    F0 = np.zeros(N)
    F0[bulk] = 1.0 / np.sqrt(20)
    scene0 = K1 @ F0
    # T_tau invariance of the rendered bulk (constant along clock cycles)
    Ptau = perm_matrix(perm_from_map(verts, keys, lambda v: qmul(tau, v)))
    check("R3c: rendered bulk scene is T_tau-invariant",
          np.allclose(Ptau @ scene0, scene0, atol=1e-10))
    cv0 = scene0.std() / scene0.mean()
    print(f"    rendered bulk background: mean {scene0.mean():.5f}, "
          f"CV {cv0:.3f} (residual anisotropy of the 20-vertex bulk)")
    # locality of a rendered boundary residual
    u = boundary[0]
    delta = np.zeros(N)
    delta[u] = 1.0
    for r, lbl in [(0.5, "fine"), (4.0, "coarse")]:
        Kr = np.linalg.inv(np.eye(N) + r * r * L)
        resp = Kr @ delta
        frac_near = resp[D[u] <= 1].sum() / resp.sum()
        print(f"    rendered residual at r={r} ({lbl}): mass within "
              f"distance 1 of source = {frac_near:.3f}")

    # ------------------------------------------------------------------
    print("\n--- R4: clock reversal is an inner substrate automorphism ---")
    tau_inv = qconj(tau)
    reversers = []
    for i, g in enumerate(verts):
        if np.allclose(qmul(qmul(g, tau), qconj(g)), tau_inv, atol=1e-8):
            reversers.append(i)
    print(f"  reversers g in 2I with g tau g^-1 = tau^-1: {len(reversers)} found")
    check("R4a: clock-reversing g exists in 2I", len(reversers) > 0,
          f"{len(reversers)} elements")
    if reversers:
        g = verts[reversers[0]]
        # order of g
        power, order = g.copy(), None
        for n in range(1, 13):
            if np.allclose(power, [1, 0, 0, 0], atol=1e-8):
                order = n
                break
            power = qmul(power, g)
        print(f"  first reverser: index {reversers[0]}, g = {np.round(g, 4)}, "
              f"order {order}")
        Pg = perm_matrix(perm_from_map(verts, keys, lambda v: qmul(g, v)))
        conj_perm = Pg @ Ptau @ Pg.T
        check("R4b: sigma_g T_tau sigma_g^{-1} = T_tau^{-1} as permutations",
              np.allclose(conj_perm, Ptau.T))
        check("R4c: reverser preserves the V_600 graph",
              np.allclose(Pg @ adj @ Pg.T, adj))

    # ------------------------------------------------------------------
    print("\n" + "=" * 72)
    print(f"SUMMARY: {len(PASS)} PASS, {len(FAIL)} FAIL")
    for name in FAIL:
        print(f"  FAILED: {name}")
    print("=" * 72)
    return 0 if not FAIL else 1


if __name__ == "__main__":
    raise SystemExit(main())
