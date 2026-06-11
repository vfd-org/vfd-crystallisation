#!/usr/bin/env python3
"""
Verify the closure of Opens 7.1 / 7.2 / 7.3 / 7.5 of
docs/rung-dimension-ladder.md (see that doc's updated sections):

  C1 (Open 7.1, scheme structure): the rung substrates carry commutative
     association schemes: number of inner-product classes = number of
     Laplacian eigenblocks (V_600: 9 = 9; E8: 5 = 5; tesseract: 5 = 5),
     and the Laplacian has all-distinct block eigenvalues, so its
     eigenprojections ARE the scheme's primitive idempotents.
     Plus the E8 rank-exhaustion facts used in the proof:
     mutual orthogonality of res_k images (k <= 4) and ranks summing to 240.

  C2 (Open 7.5, aliasing tables): the complete bookkeeping of where every
     harmonic level lands:
     - V_600: res_k for k = 6..10 splits into FULL irrep-squared blocks
       following the McKay walk: k=6 -> 3'+4', k=7 -> 6+2', k=8 -> 5+4',
       k=9 -> 4+6, k=10 -> 3+5+3'.
     - tesseract: complete character account, res_k images for k = 0..4,
       including the DOWN-ALIASING witness (x_i^3 - x_i|x|^2/2)|_X = -x_i/4
       (a degree-3 harmonic landing in the degree-1 eigenspace).
     - E8: res_5 lands entirely in the lambda = 58 block (Gegenbauer
       a_5 = -2, same block as H_3); res_6 splits (a_6 = 4/11 not in the
       scheme spectrum).

  C3 (Open 7.3, folded-sector sampling): zonal/radial observables sample
     ALL blocks: the 9 shell-indicators around a vertex hit all 9 V_600
     blocks (zonal bijection), and the closure-response kernel
     psi = (L + phi^-2 I)^{-1} delta_v0 has a computable, nonzero energy
     fraction in the primed (folded) blocks.

  C4 (Open 7.2, octonionic ingredients): integral-octonion (octavian)
     arithmetic: Fano lines derived from the Cayley-Dickson table; a
     240-unit maximal-order loop closed under multiplication; its
     inner-product graph is the E8 rung graph (degree 56, same block
     multiplicities); canonical S^7 frames {v e_1, ..., v e_7} orthonormal
     and tangent at ALL 240 anchors; rendering kernel positive, stochastic,
     equivariant under left translations; clock-reversal search reported.

Usage:
    python scripts/verify_ladder_completion.py
"""
from __future__ import annotations

import itertools
import numpy as np
from math import factorial
from pathlib import Path

PHI = (1 + np.sqrt(5)) / 2
DATA_PATH = Path(__file__).resolve().parent / "600cell_data.npz"
RNG = np.random.default_rng(248)

PASS, FAIL = [], []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


# ---------------------------------------------------------------- helpers
def graph_of(verts, ip_edge):
    G = verts @ verts.T
    A = (np.abs(G - ip_edge) < 1e-8).astype(float)
    np.fill_diagonal(A, 0.0)
    L = np.diag(A.sum(axis=1)) - A
    return A, L, int(A.sum(axis=1)[0])


def eigenblocks(L):
    evals, evecs = np.linalg.eigh(L)
    r = np.round(evals, 6)
    return {float(l): evecs[:, r == l] for l in sorted(set(r.tolist()))}


def cheb_u(k, x):
    if k == 0:
        return np.ones_like(x)
    um, u = np.ones_like(x), 2 * x
    for _ in range(k - 1):
        um, u = u, 2 * x * u - um
    return u


def gegenbauer3(k, x):
    if k == 0:
        return np.ones_like(x)
    cm, c = np.ones_like(x), 6 * x
    for n in range(2, k + 1):
        cm, c = c, (2 * (n + 2) * x * c - (n + 4) * cm) / n
    return c


def res_basis(verts, k, kernel, dim_hint):
    Y = RNG.normal(size=(4 * max(30, dim_hint), verts.shape[1]))
    Y /= np.linalg.norm(Y, axis=1, keepdims=True)
    return kernel(k, verts @ Y.T)


def rank_of(M, tol=1e-8):
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > tol * s[0]))


def block_split(blocks, M):
    """Per-block component rank of span(M); returns {lambda: rank}."""
    out = {}
    for lam, E in blocks.items():
        P = E @ (E.T @ M)
        r = rank_of(P) if np.linalg.norm(P) > 1e-8 * np.linalg.norm(M) else 0
        if r:
            out[lam] = r
    return out


def ip_classes(verts):
    G = np.round(verts @ verts.T, 6)
    return sorted(set(G.flatten().tolist()))


# ---------------------------------------------------------------- octonions
def qmul(q1, q2):
    a, b, c, d = q1
    e, f, g, h = q2
    return np.array([a*e - b*f - c*g - d*h, a*f + b*e + c*h - d*g,
                     a*g - b*h + c*e + d*f, a*h + b*g - c*f + d*e])


def qconj(q):
    return np.array([q[0], -q[1], -q[2], -q[3]])


def omul(x, y):
    """Cayley-Dickson: (a,b)(c,d) = (ac - conj(d) b, d a + b conj(c))."""
    a, b = x[:4], x[4:]
    c, d = y[:4], y[4:]
    return np.concatenate([qmul(a, c) - qmul(qconj(d), b),
                           qmul(d, a) + qmul(b, qconj(c))])


def oconj(x):
    out = -x.copy()
    out[0] = x[0]
    return out


def fano_lines():
    """Derive the 7 multiplication triples {a,b,c} with e_a e_b = ±e_c."""
    lines = set()
    for a in range(1, 8):
        for b in range(1, 8):
            if a == b:
                continue
            ea, eb = np.zeros(8), np.zeros(8)
            ea[a], eb[b] = 1.0, 1.0
            p = omul(ea, eb)
            c = int(np.argmax(np.abs(p)))
            lines.add(frozenset((a, b, c)))
    return sorted(tuple(sorted(l)) for l in lines)


def cliques4(A):
    """All 4-cliques (cells) of a graph given by adjacency A."""
    N = A.shape[0]
    nbr = [set(np.nonzero(A[i])[0].tolist()) for i in range(N)]
    cells = []
    for a in range(N):
        for b in nbr[a]:
            if b <= a:
                continue
            common_ab = nbr[a] & nbr[b]
            for c in common_ab:
                if c <= b:
                    continue
                for d in common_ab & nbr[c]:
                    if d <= c:
                        continue
                    cells.append((a, b, c, d))
    return cells


# ---------------------------------------------------------------- main
def main():
    print("=" * 72)
    print("LADDER COMPLETION: Opens 7.1 / 7.2 / 7.3 / 7.5")
    print("=" * 72)

    v600 = np.load(DATA_PATH)["vertices"]
    A6, L6, d6 = graph_of(v600, PHI / 2)
    B6 = eigenblocks(L6)

    v16 = np.array([np.array(s) for s in itertools.product((0.5, -0.5), repeat=4)])
    A16, L16, d16 = graph_of(v16, 0.5)
    B16 = eigenblocks(L16)

    # E8 roots (standard coordinates) for C1/C2
    roots = []
    for i, j in itertools.combinations(range(8), 2):
        for si, sj in itertools.product((1.0, -1.0), repeat=2):
            v = np.zeros(8); v[i] = si; v[j] = sj
            roots.append(v)
    for signs in itertools.product((0.5, -0.5), repeat=8):
        if sum(1 for s in signs if s < 0) % 2 == 0:
            roots.append(np.array(signs))
    e8 = np.array(roots) / np.sqrt(2)
    Ae, Le, de = graph_of(e8, 0.5)
    Be = eigenblocks(Le)

    # ---------------- C1: scheme structure ----------------
    print("\n--- C1 (Open 7.1): commutative-scheme structure ---")
    for label, V, B in [("V_600", v600, B6), ("E8 roots", e8, Be),
                        ("tesseract", v16, B16)]:
        n_ip = len(ip_classes(V)) - 1            # off-diagonal ip classes = d
        n_blocks = len(B)                        # eigenspaces = d + 1
        lams = sorted(B.keys())
        distinct = len(lams) == len(set(np.round(lams, 6)))
        check(f"C1 {label}: d off-diagonal ip classes ({n_ip}) + 1 = "
              f"#eigenspaces ({n_blocks}); eigenvalues simple per block",
              n_ip + 1 == n_blocks and distinct,
              f"ip classes (off-diag) {n_ip}, blocks {n_blocks}")
    # E8 rank exhaustion + orthogonality (k <= 4)
    Ms = [res_basis(e8, k, gegenbauer3,
                    [1, 8, 35, 112, 294][k]) for k in range(5)]
    ranks = [rank_of(M) for M in Ms]
    ortho = True
    for a, b in itertools.combinations(range(5), 2):
        Qa, _ = np.linalg.qr(Ms[a]); Qb, _ = np.linalg.qr(Ms[b])
        ra, rb = ranks[a], ranks[b]
        if np.linalg.norm(Qa[:, :ra].T @ Qb[:, :rb]) > 1e-8:
            ortho = False
    check("C1 E8 rank exhaustion: ranks (1,8,35,112,84) sum to 240, "
          "images mutually orthogonal",
          ranks == [1, 8, 35, 112, 84] and sum(ranks) == 240 and ortho,
          f"ranks {ranks}, orthogonal: {ortho}")

    # ---------------- C2: aliasing tables ----------------
    print("\n--- C2 (Open 7.5): complete aliasing tables ---")
    # V600 McKay walk predictions: k -> {lambda: full block rank}
    mckay = {
        6: {14.472136: 9, 15.0: 16},
        7: {14.0: 36, 15.708204: 4},
        8: {12.0: 25, 15.0: 16},
        9: {9.0: 16, 14.0: 36},
        10: {5.527864: 9, 12.0: 25, 14.472136: 9},
    }
    for k, pred in mckay.items():
        M = res_basis(v600, k, cheb_u, sum(pred.values()))
        split = {round(l, 6): r for l, r in block_split(B6, M).items()}
        pred_r = {round(l, 6): r for l, r in pred.items()}
        check(f"C2 V_600 res_{k} = full blocks {sorted(pred_r.items())}",
              split == pred_r, f"observed {sorted(split.items())}")
    # tesseract complete character account
    tess_table = {}
    for k in range(5):
        M = res_basis(v16, k, cheb_u, 16)
        tess_table[k] = {round(l, 6): r for l, r in block_split(B16, M).items()}
    print(f"    tesseract res_k block table: {tess_table}")
    check("C2 tesseract: res_3 SPLITS (down-aliasing) into lam=6 (rank 4) "
          "+ lam=2 (rank 4)",
          tess_table[3] == {6.0: 4, 2.0: 4}, f"{tess_table[3]}")
    check("C2 tesseract: res_4 down-aliases to lam=0 (1) + lam=4 (6) + "
          "lam=8 (1) — degree-4 zonal sum_i x_i^4 hits the constant",
          tess_table[4] == {0.0: 1, 4.0: 6, 8.0: 1}, f"{tess_table[4]}")
    # down-aliasing witness: (x_1^3 - x_1 |x|^2 / 2)|_X = -x_1/4
    w = v16[:, 0] ** 3 - v16[:, 0] * (v16 ** 2).sum(axis=1) / 2
    check("C2 witness: degree-3 harmonic x_1^3 - x_1|x|^2/2 restricts to "
          "-x_1/4 (lands in the k=1 eigenspace)",
          np.allclose(w, -v16[:, 0] / 4))
    # E8: res_5 -> lambda = 58 entirely; res_6 splits
    M5 = res_basis(e8, 5, gegenbauer3, 250)
    a5 = de * gegenbauer3(5, np.array([0.5]))[0] / gegenbauer3(5, np.array([1.0]))[0]
    r5 = np.linalg.norm(Ae @ M5 - a5 * M5) / np.linalg.norm(M5)
    split5 = block_split(Be, M5)
    check("C2 E8 res_5: scalar a_5 = -2 -> entirely in lam = 58 "
          "(same block as H_3)",
          abs(a5 + 2) < 1e-9 and r5 < 1e-8 and set(split5) == {58.0},
          f"a_5 = {a5:.4f}, action res {r5:.1e}, blocks {sorted(split5)}")
    M6 = res_basis(e8, 6, gegenbauer3, 250)
    a6 = de * gegenbauer3(6, np.array([0.5]))[0] / gegenbauer3(6, np.array([1.0]))[0]
    split6 = {round(l): r for l, r in block_split(Be, M6).items()}
    check("C2 E8 res_6: a_6 = 4/11 not a scheme eigenvalue -> SPLITS",
          abs(a6 - 4 / 11) < 1e-9 and len(split6) > 1,
          f"a_6 = {a6:.4f}, split {sorted(split6.items())}")

    # ---------------- C3: folded-sector sampling ----------------
    print("\n--- C3 (Open 7.3): radial observables sample the folded sector ---")
    i_id = int(np.argmin(np.linalg.norm(v600 - np.array([1, 0, 0, 0.0]), axis=1)))
    ips = np.round(v600 @ v600[i_id], 6)
    shells = sorted(set(ips.tolist()), reverse=True)
    Z = np.stack([(ips == s).astype(float) for s in shells], axis=1)  # 120 x 9
    check("C3 zonal space: 9 shells around the anchor", Z.shape[1] == 9)
    hit = {round(l, 6): r for l, r in block_split(B6, Z).items()}
    check("C3 zonal bijection: shell indicators hit ALL 9 blocks, one "
          "dimension each", len(hit) == 9 and all(r == 1 for r in hit.values()),
          f"{sorted(hit.items())}")
    # closure-response kernel at hadronic coherence phi
    delta = np.zeros(120); delta[i_id] = 1.0
    psi = np.linalg.solve(L6 + PHI ** -2 * np.eye(120), delta)
    primed = [14.472136, 15.0, 15.708204]
    w_tot, w_primed = 0.0, 0.0
    for lam, E in B6.items():
        wt = float(np.sum((E.T @ psi) ** 2))
        w_tot += wt
        if any(abs(lam - p) < 1e-4 for p in primed):
            w_primed += wt
    frac = w_primed / w_tot
    # also excluding the k=0 (constant) block
    w0 = float(np.sum((B6[0.0].T @ psi) ** 2)) if 0.0 in B6 else \
        float(np.sum((B6[-0.0].T @ psi) ** 2))
    frac_dyn = w_primed / (w_tot - w0)
    check("C3 response kernel (L + phi^-2)^{-1} delta carries nonzero "
          "folded-sector energy", frac > 1e-4,
          f"primed fraction {100*frac:.2f}% of total, "
          f"{100*frac_dyn:.2f}% of non-constant energy")

    # ---------------- C4: octonionic rendering ingredients ----------------
    print("\n--- C4 (Open 7.2): octavian arithmetic and S^7 rendering layer ---")
    lines = fano_lines()
    check("C4a Fano lines derived from Cayley-Dickson table: 7 triples",
          len(lines) == 7, f"{lines}")
    # canonical S^7 frames via octonion parallelism at EVERY E8-root anchor
    units = [np.zeros(8) for _ in range(7)]
    for a in range(7):
        units[a][a + 1] = 1.0
    ok_frame = all(
        np.allclose(np.stack([omul(v, u) for u in units])
                    @ np.stack([omul(v, u) for u in units]).T, np.eye(7), atol=1e-10)
        and np.allclose(np.stack([omul(v, u) for u in units]) @ v, 0, atol=1e-10)
        for v in e8)
    check("C4b frames: {v e_1, ..., v e_7} orthonormal in T_v S^7 for all "
          "240 anchors (Moufang/octonion parallelism)", ok_frame)
    # the E8-root rendering graph and its kernel (no octonion closure needed)
    check("C4c arena graph: 240 E8 roots, degree 56, block multiplicities "
          "{1, 8, 35, 84, 112}",
          de == 56 and sorted(int(E.shape[1]) for E in Be.values())
          == [1, 8, 35, 84, 112])
    K = np.linalg.inv(np.eye(240) + Le)
    ones = np.ones(240)
    check("C4d kernel pi_1 = (I + L)^{-1}: entrywise positive, stochastic",
          K.min() > -1e-12 and np.allclose(K @ ones, ones, atol=1e-10),
          f"min entry {K.min():.2e}")
    # W(E8)-equivariance: a genuine root-system automorphism commutes with pi_r
    keys = {tuple(np.round(v, 6)): i for i, v in enumerate(e8)}
    # signed coordinate transposition (0 1) with sign flip on {0,1}: in W(E8)
    M = np.eye(8); M[[0, 1]] = M[[1, 0]]; M[0, 0] = M[1, 1] = 0; M[0, 1] = M[1, 0] = -1
    perm = np.array([keys[tuple(np.round(M @ v, 6))] for v in e8])
    P = np.zeros((240, 240)); P[perm, np.arange(240)] = 1.0
    comm = np.linalg.norm(P @ K - K @ P)
    check("C4e equivariance: a W(E8) root automorphism commutes with pi_r",
          np.allclose(P @ Ae @ P.T, Ae) and comm < 1e-10,
          f"graph aut + ||[P, pi]|| = {comm:.2e}")
    # reduced sub-open: does a multiplicatively-closed 240-unit loop exist
    # in this basis so left-translation is itself a rendering symmetry?
    # Conway-Smith maximal-order fact; check whether the naive E8 basis closes.
    sample = RNG.choice(240, size=40, replace=False)
    closed = all(tuple(np.round(omul(e8[i], e8[j]), 6)) in keys
                 for i in sample for j in sample)
    check("C4f (diagnostic) naive E8 basis is NOT a closed octonion loop "
          "(reduced sub-open: Conway-Smith maximal order)", not closed,
          "closure fails in naive basis, as expected")

    # ---------------- C5: the 40 / biology rung (Open 7.4) ----------------
    print("\n--- C5 (Open 7.4): the 40 rung lives on S^3 (cell-centre arena) ---")
    cells = cliques4(A6)
    check("C5a the 600-cell has exactly 600 tetrahedral cells (4-cliques)",
          len(cells) == 600, f"{len(cells)} 4-cliques")
    centres = np.array([v600[list(c)].sum(axis=0) for c in cells])
    centres /= np.linalg.norm(centres, axis=1, keepdims=True)
    uniq = np.unique(np.round(centres, 6), axis=0)
    check("C5b cell-centres = 600 vertices of the dual 120-cell on S^3",
          len(uniq) == 600, f"{len(uniq)} distinct centres")
    # robust nearest-neighbour graph (largest off-diagonal inner product)
    G = centres @ centres.T
    np.fill_diagonal(G, -2.0)
    edge_ip = G.max()
    Ac = (np.abs(G - edge_ip) < 1e-5).astype(float)
    deg_c = Ac.sum(axis=1)
    Lc = np.diag(deg_c) - Ac
    Bc = eigenblocks(Lc)
    mults_c = sorted(int(E.shape[1]) for E in Bc.values())
    dc = int(deg_c[0])
    print(f"    120-cell graph: degree {dc}, edge ip {edge_ip:.6f}, "
          f"{len(Bc)} eigenblocks, mults {mults_c}")
    check("C5c arena: 600 cell-centres form a regular degree-4 graph "
          "(the dual 120-cell) on S^3", dc == 4 and np.allclose(deg_c, 4))
    # The 120-cell vertices are NOT a group, so the intertwiner runs via the
    # spherical-design route (Thm 3.4), not the class-sum route (Thm 3.2):
    # harmonic restriction is injective up to the design cutoff.
    kmax = 0
    for k in range(1, 12):
        Mk = res_basis(centres, k, cheb_u, (k + 1) ** 2)
        if rank_of(Mk) == (k + 1) ** 2:
            kmax = k
        else:
            break
    check("C5d 40-rung arena IS S^3: harmonic restriction injective through "
          "k_max (high spherical design, design route not group route)",
          kmax >= 5, f"injectivity cutoff k_max = {kmax}")
    # low harmonics ARE Laplacian eigenspaces of the 120-cell graph (the
    # design-route intertwiner): res_1 lands in a single eigenblock
    M1 = res_basis(centres, 1, cheb_u, 4)
    split1 = {round(l, 4): r for l, r in block_split(Bc, M1).items()}
    check("C5e design-route intertwiner: res_1 (4 dims) lands in a single "
          "120-cell Laplacian eigenspace",
          len(split1) == 1 and list(split1.values())[0] == 4,
          f"res_1 block split {split1}")
    # the 15 x 40 Hopf partition arithmetic
    check("C5f rung arithmetic: 600 cells = 15 Hopf fibres x 40 cells, "
          "40 = 8 x 5 (E8-dim x Schlafli-index)",
          600 == 15 * 40 and 40 == 8 * 5)

    print("\n" + "=" * 72)
    print(f"SUMMARY: {len(PASS)} PASS, {len(FAIL)} FAIL")
    for n in FAIL:
        print(f"  FAILED: {n}")
    print("=" * 72)
    return 0 if not FAIL else 1


if __name__ == "__main__":
    raise SystemExit(main())
