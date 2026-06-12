#!/usr/bin/env python3
"""
Verify the "why this crystal" forcing chain (docs/why-this-crystal.md) and
the non-abelian half of the gauge mechanism — the two book mechanisms that
previously had no in-tree verification.

  CF (the crystal is forced, not chosen):
      CF1  the 120 vertices of the 600-cell form a GROUP under quaternion
           multiplication (closure, inverses): the crystal IS the binary
           icosahedral group 2I.
      CF2  2I is perfect (its commutators generate all of it): no smaller
           quotient exists — nothing about it can be "turned off".
      CF3  2I has exactly 9 conjugacy classes; the Burnside-Dixon class-sum
           algorithm recovers its irreducible representation dimensions
           {1, 2, 2, 3, 3, 4, 4, 5, 6} with sum of squares 120, computed
           from the multiplication table alone.
      CF4  McKay correspondence, by direct computation: tensoring with the
           geometric 2-dim representation (character 2*q0) gives a graph on
           the 9 irreps that is a TREE with one degree-3 node and arm
           lengths {1, 2, 5} — the affine E8 Dynkin diagram — and the irrep
           dimension vector is its Perron eigenvector with eigenvalue 2.
           The crystal carries E8 inside its representation theory.
      CF5  the binary tetrahedral group 2T (the 24-cell) sits inside 2I:
           the exceptional chain 2T < 2O, 2I terminates at 2I.
      CF6  extension witness: adjoining any unit quaternion outside 2I
           generates unboundedly many new elements (no larger finite
           crystal exists; witness, with the classification theorem cited
           for the proof).

  GE (the graph knows its own shape — Ch4's "no dimension smuggled in"):
      GE1  from the ADJACENCY MATRIX ALONE, the eigenvectors of the first
           nonzero Laplacian level reconstruct the vertex coordinates up to
           a global rotation: the pairwise inner products of the
           reconstructed embedding match the true 600-cell exactly.
      GE2  the reconstructed embedding is genuinely 4-dimensional with all
           120 points on one sphere (uniform row norms: a tight frame).

  YM (the gauge mechanism completes non-abelianly — Ch9):
      YM1  the Yang-Mills action for an su(2) triplet is gauge-invariant at
           second order in the gauge parameter (the O(s) variation cancels
           exactly), verified on a 4D grid with the full nonlinear field
           strength.
      YM2  the null: an antisymmetric coupling tensor that VIOLATES the
           Jacobi identity loses invariance at first order — consistency of
           the self-coupled vector multiplet FORCES the charge algebra to
           be a Lie algebra (Gell-Mann-Glashow / Deser, here by machine).

Usage:
    python scripts/verify_crystal_forcing.py
"""
from __future__ import annotations

import numpy as np
from pathlib import Path

rng = np.random.default_rng(20260613)

DATA_PATH = Path(__file__).resolve().parent / "600cell_data.npz"

PASS = []
FAIL = []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


def qmul(q1, q2):
    a, b, c, d = q1
    e, f, g, h = q2
    return np.array([a*e - b*f - c*g - d*h,
                     a*f + b*e + c*h - d*g,
                     a*g - b*h + c*e + d*f,
                     a*h + b*g - c*f + d*e])


def key(q):
    return tuple(np.round(q, 8))


# ======================================================================
# CF: the crystal is the terminal exceptional group
# ======================================================================

def cf_forcing():
    print("CF: the crystal is forced (2I, perfect, ADE-terminal, McKay = E8)")
    verts = np.load(DATA_PATH)["vertices"]
    n = len(verts)
    idx = {key(v): i for i, v in enumerate(verts)}

    # CF0: data-file provenance — the stored vertices ARE the
    # unit-circumradius 600-cell: 120 distinct unit quaternions whose
    # pairwise inner products take only the nine icosian values.
    phi = (1 + np.sqrt(5)) / 2
    norms_ok = np.max(np.abs(np.linalg.norm(verts, axis=1) - 1)) < 1e-12
    distinct = len(idx) == 120
    G = verts @ verts.T
    allowed = np.array([1.0, -1.0, 0.5, -0.5, 0.0,
                        phi / 2, -phi / 2, 1 / (2 * phi), -1 / (2 * phi)])
    vals_ok = np.max(np.min(np.abs(G[..., None] - allowed), axis=-1)) < 1e-9
    deg12 = np.all(np.sum(np.abs(G - phi / 2) < 1e-9, axis=1) == 12)
    check("CF0 data provenance: 120 distinct unit quaternions, icosian "
          "inner-product spectrum, 12 nearest neighbours at phi/2",
          norms_ok and distinct and vals_ok and deg12)

    # CF1: closure under multiplication and inverses
    mul = np.zeros((n, n), dtype=int)
    ok_closed = True
    for i in range(n):
        for j in range(n):
            k = key(qmul(verts[i], verts[j]))
            if k not in idx:
                ok_closed = False
                break
            mul[i, j] = idx[k]
    inv = np.zeros(n, dtype=int)
    e_id = idx[key(np.array([1.0, 0, 0, 0]))]
    for i in range(n):
        conj = verts[i] * np.array([1, -1, -1, -1])
        inv[i] = idx[key(conj)]
        ok_closed = ok_closed and mul[i, inv[i]] == e_id
    check("CF1 the 120 vertices form a group (the crystal IS 2I)", ok_closed)

    # CF2: perfect group — commutators generate everything
    comms = set()
    for _ in range(400):
        i, j = rng.integers(n, size=2)
        c = mul[mul[i, j], mul[inv[i], inv[j]]]
        comms.add(int(c))
    gen = set(comms) | {e_id}
    frontier = list(gen)
    while frontier:
        new = []
        for a in frontier:
            for b in list(comms)[:20]:
                c = int(mul[a, b])
                if c not in gen:
                    gen.add(c)
                    new.append(c)
        frontier = new
    check("CF2 2I is perfect: commutators generate the whole group",
          len(gen) == 120, f"generated {len(gen)}/120")

    # CF3: conjugacy classes + Burnside-Dixon character dimensions
    class_of = -np.ones(n, dtype=int)
    classes = []
    for i in range(n):
        if class_of[i] >= 0:
            continue
        orbit = {i}
        for g in range(n):
            orbit.add(int(mul[mul[g, i], inv[g]]))
        cid = len(classes)
        classes.append(sorted(orbit))
        for x in orbit:
            class_of[x] = cid
    ncl = len(classes)
    check("CF3a exactly 9 conjugacy classes", ncl == 9, f"found {ncl}")

    sizes = np.array([len(c) for c in classes], dtype=float)
    # class-sum multiplication coefficients a_{ijk}
    a = np.zeros((ncl, ncl, ncl))
    for ci in range(ncl):
        for cj in range(ncl):
            counts = np.zeros(ncl)
            for x in classes[ci]:
                for y in classes[cj]:
                    counts[class_of[mul[x, y]]] += 1
            a[ci, cj] = counts / sizes  # coefficient per element of target class
    Ms = [a[i] for i in range(ncl)]          # commuting matrices
    R = sum(rng.normal() * M for M in Ms)
    _, V = np.linalg.eig(R)
    dims = []
    chars = np.zeros((ncl, ncl))
    for c in range(ncl):
        v = np.real(V[:, c])
        om = np.array([np.real((M @ v)[np.argmax(np.abs(v))] / v[np.argmax(np.abs(v))])
                       for M in Ms])         # om_i = |C_i| chi(g_i)/chi(1)
        d = np.sqrt(n / np.sum(om**2 / sizes))
        dims.append(d)
        chars[c] = d * om / sizes
    dims_sorted = sorted(round(d) for d in dims)
    ok_dims = (dims_sorted == [1, 2, 2, 3, 3, 4, 4, 5, 6]
               and max(abs(d - round(d)) for d in dims) < 1e-6
               and sum(x * x for x in dims_sorted) == 120)
    check("CF3b irreducible representation dimensions = {1,2,2,3,3,4,4,5,6}, "
          "sum of squares 120", ok_dims, f"{dims_sorted}")

    # CF4: McKay graph from the geometric 2-dim character chi_2(g) = 2 q0
    chi2 = np.array([2 * verts[classes[c][0]][0] for c in range(ncl)])
    A = np.zeros((ncl, ncl))
    for p in range(ncl):
        for q in range(ncl):
            A[p, q] = np.sum(sizes * chi2 * chars[p] * chars[q]) / n
    ok_int = np.max(np.abs(A - np.round(A))) < 1e-9
    A = np.round(A)
    ok_mats = (ok_int and np.allclose(A, A.T)
               and np.all((A == 0) | (A == 1) | (np.eye(ncl) > 0))
               and np.all(np.diag(A) == 0)
               and np.all(A >= 0))
    check("CF4 pre-check: McKay matrix is symmetric, non-negative integer, "
          "0/1 off-diagonal, zero diagonal", ok_mats)
    Adj = (A > 0).astype(int)
    np.fill_diagonal(Adj, 0)
    nedge = Adj.sum() // 2
    is_tree = (nedge == ncl - 1)
    degs = Adj.sum(axis=1)
    branch = np.where(degs == 3)[0]
    ok_shape = is_tree and len(branch) == 1 and np.max(degs) == 3
    # arm lengths from the branch node
    arms = []
    if ok_shape:
        b = branch[0]
        for nb in np.where(Adj[b])[0]:
            length, prev, cur = 1, b, nb
            while True:
                nxt = [x for x in np.where(Adj[cur])[0] if x != prev]
                if not nxt:
                    break
                prev, cur = cur, nxt[0]
                length += 1
            arms.append(length)
    ok_arms = sorted(arms) == [1, 2, 5]
    check("CF4a McKay graph is a tree, one branch node, arms {1,2,5}: "
          "the affine E8 Dynkin diagram", ok_shape and ok_arms,
          f"tree={is_tree}, arms={sorted(arms)}")
    dvec = np.array([round(d) for d in dims], dtype=float)
    ok_perron = np.allclose(Adj @ dvec, 2 * dvec, atol=1e-9)
    check("CF4b irrep dimensions are the Perron vector: A d = 2 d "
          "(the E8 marks)", ok_perron)

    # CF5: the 24-cell (2T) sits inside as a subgroup
    sub = [i for i, v in enumerate(verts)
           if np.allclose(np.sort(np.abs(v)), [0, 0, 0, 1], atol=1e-9)
           or np.allclose(np.abs(v), [0.5, 0.5, 0.5, 0.5], atol=1e-9)]
    ok_sub = len(sub) == 24
    subset = set(sub)
    for i in sub:
        for j in sub:
            ok_sub = ok_sub and (int(mul[i, j]) in subset)
    check("CF5 the 24-cell vertices form the subgroup 2T inside 2I "
          "(the exceptional chain ends here)", ok_sub,
          f"|2T| = {len(sub)}")

    # CF6: extension witness — adjoining any outside unit quaternion
    # generates unboundedly many elements
    t = 0.7
    g_out = np.array([np.cos(t), np.sin(t), 0.0, 0.0])
    words = {key(v) for v in verts}
    frontier = [g_out]
    words.add(key(g_out))
    counts = [len(words)]
    for _ in range(4):
        new = []
        for w in frontier:
            # mix group elements AND the outside element, else the walk
            # stays inside one coset g*2I
            cands = [qmul(w, verts[i]) for i in range(0, n, 11)]
            cands.append(qmul(w, g_out))
            cands.append(qmul(g_out, w))
            for p in cands:
                kk = key(p)
                if kk not in words:
                    words.add(kk)
                    new.append(p)
        frontier = new
        counts.append(len(words))
    growing = all(b > a for a, b in zip(counts, counts[1:]))
    check("CF6 extension witness: one outside element generates unboundedly "
          "(no larger finite crystal; classification cited for proof)",
          growing and counts[-1] > 1200,
          f"growth {counts} — never closes")


# ======================================================================
# GE: the graph knows its own shape
# ======================================================================

def ge_graph_knows_shape():
    print("GE: dimension and shape from the bare adjacency matrix")
    d = np.load(DATA_PATH)
    verts = d["vertices"]
    A = d["adjacency"].astype(float)
    L = np.diag(A.sum(axis=1)) - A          # built from adjacency ONLY
    lams, vecs = np.linalg.eigh(L)
    lam1 = lams[1]
    band = vecs[:, np.abs(lams - lam1) < 1e-8]
    check("GE0 first excited level has multiplicity 4 (a 3-sphere's "
          "degree-1 harmonics)", band.shape[1] == 4)

    X = band * np.sqrt(len(verts) / band.shape[1])  # tight-frame scaling
    norms = np.linalg.norm(X, axis=1)
    ok_sphere = np.max(np.abs(norms - 1)) < 1e-9
    check("GE2 reconstructed points all lie on one sphere (uniform norms)",
          ok_sphere, f"norm spread {np.max(np.abs(norms-1)):.2e}")

    G_rec = X @ X.T
    G_true = verts @ verts.T
    # full Gram-matrix equality, same vertex labelling
    ok_gram = np.max(np.abs(G_rec - G_true)) < 1e-9
    check("GE1 full Gram matrix of the spectral embedding equals the "
          "600-cell's (same labelling, every angle)", ok_gram,
          f"max |G_rec - G_true| = {np.max(np.abs(G_rec - G_true)):.2e}")
    # and the explicit global alignment: Procrustes. Eigenvector signs are
    # free, so orient the eigenbasis first to make the alignment a proper
    # rotation (flip one column if the optimal orthogonal map is improper).
    U, _, Vt = np.linalg.svd(X.T @ verts)
    if np.linalg.det(U @ Vt) < 0:
        X[:, -1] *= -1.0
        U, _, Vt = np.linalg.svd(X.T @ verts)
    R = U @ Vt
    ok_proc = (np.max(np.abs(X @ R - verts)) < 1e-9
               and abs(np.linalg.det(R) - 1.0) < 1e-9)
    check("GE1b with oriented eigenbasis, an explicit proper rotation "
          "(det = +1) maps the reconstruction onto the true vertices "
          "pointwise", ok_proc,
          f"max coordinate dev = {np.max(np.abs(X @ R - verts)):.2e}, "
          f"det R = {np.linalg.det(R):+.1f}")
    # and the neighbour relation is recovered: largest off-diagonal inner
    # product = cos 36 deg = phi/2, exactly the edge relation
    phi = (1 + np.sqrt(5)) / 2
    od = G_rec - np.diag(np.diag(G_rec))
    ok_edge = abs(np.max(od) - phi / 2) < 1e-9
    nbr_match = np.allclose((np.abs(G_rec - phi / 2) < 1e-8).astype(int), A)
    check("GE3 edges = inner product phi/2: the graph reconstructs its own "
          "adjacency from spectrum alone", ok_edge and nbr_match)


# ======================================================================
# YM: non-abelian gauge consistency forces a Lie algebra
# ======================================================================

def ym_jacobi():
    print("YM: gauge consistency of the vector multiplet forces a Lie algebra")
    nn = 6
    x = np.arange(nn) * 2 * np.pi / nn
    grids = np.meshgrid(*([x] * 4), indexing="ij")

    def spectral_d(field, axis):
        k = 2j * np.pi * np.fft.fftfreq(nn, d=2 * np.pi / nn)
        shape = [1] * field.ndim
        shape[axis] = nn
        return np.real(np.fft.ifft(np.fft.fft(field, axis=axis)
                                   * k.reshape(shape), axis=axis))

    def rand_scalar(scale):
        out = np.zeros((nn,) * 4)
        for _ in range(2):
            kv = rng.integers(-1, 2, size=4)
            if not kv.any():
                kv[0] = 1
            ph = rng.uniform(0, 2 * np.pi)
            out += rng.normal() * np.cos(sum(k * g for k, g in zip(kv, grids)) + ph)
        return scale * out

    Nc = 3
    Afield = np.array([[rand_scalar(0.4) for _ in range(4)] for _ in range(Nc)])
    chi = np.array([rand_scalar(1.0) for _ in range(Nc)])

    def action(Af, f):
        S = 0.0
        for aa in range(Nc):
            for m in range(4):
                for v in range(m + 1, 4):
                    F = spectral_d(Af[aa, v], m) - spectral_d(Af[aa, m], v)
                    for bb in range(Nc):
                        for cc in range(Nc):
                            F = F + f[aa, bb, cc] * Af[bb, m] * Af[cc, v]
                    S += np.sum(F * F)
        return S * (2 * np.pi / nn) ** 4

    def transformed(f, s):
        Ap = Afield.copy()
        for aa in range(Nc):
            for m in range(4):
                dA = spectral_d(chi[aa], m)
                for bb in range(Nc):
                    for cc in range(Nc):
                        dA = dA + f[aa, bb, cc] * Afield[bb, m] * chi[cc]
                Ap[aa, m] = Afield[aa, m] + s * dA
        return Ap

    def odd_part(f, s):
        """Odd-in-s part of S(A + s dA): isolates the first-order gauge
        violation. True Lie algebra: O(s^3). Non-Jacobi: O(s)."""
        return abs(action(transformed(f, s), f)
                   - action(transformed(f, -s), f)) / 2

    # su(2): f = epsilon_{abc}, satisfies Jacobi
    eps = np.zeros((3, 3, 3))
    for (i, j, k_), s_ in (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                           ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)):
        eps[i, j, k_] = s_
    r1 = odd_part(eps, 1e-2)
    r2 = odd_part(eps, 5e-3)
    check("YM1 su(2) multiplet: first-order gauge variation cancels exactly "
          "(odd part O(s^3))", 6.5 < r1 / r2 < 9.5,
          f"odd-part ratio {r1 / r2:.2f} (expect 8)")

    # the null: antisymmetric in (a,b) but NOT a Lie algebra
    fbad = rng.normal(size=(3, 3, 3))
    fbad = fbad - np.transpose(fbad, (1, 0, 2))
    jac = np.einsum("abe,ecd->abcd", fbad, fbad) \
        + np.einsum("bce,ead->abcd", fbad, fbad) \
        + np.einsum("cae,ebd->abcd", fbad, fbad)
    assert np.max(np.abs(jac)) > 0.1  # genuinely non-Jacobi
    r1b = odd_part(fbad, 1e-2)
    r2b = odd_part(fbad, 5e-3)
    check("YM2 null: a non-Lie coupling loses invariance at first order "
          "(odd part O(s)) — the charge algebra MUST be a Lie algebra",
          1.7 < r1b / r2b < 2.3, f"odd-part ratio {r1b / r2b:.2f} (expect 2)")


def main():
    print("=" * 70)
    print("Crystal-forcing + gauge-completion verification")
    print("=" * 70)
    cf_forcing()
    ge_graph_knows_shape()
    ym_jacobi()
    print("=" * 70)
    print(f"SUMMARY: {len(PASS)} PASS, {len(FAIL)} FAIL")
    for name in FAIL:
        print(f"  FAILED: {name}")
    return 0 if not FAIL else 1


if __name__ == "__main__":
    raise SystemExit(main())
