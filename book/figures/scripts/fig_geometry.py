#!/usr/bin/env python3
"""Data-real geometry figures, all computed from scripts/600cell_data.npz
and from the E8 root system built here. Nothing decorative is invented.

  ch03-600cell.png    the 600-cell, 120 vertices / 720 edges, orthographic
  ch03-e8.png         the E8 root system, 240 roots, Coxeter-plane projection
  ch09-downsampling.png   one shape at three resolutions: 120 -> 24 -> 16
"""
import numpy as np
import matplotlib.pyplot as plt
import _style as S

S.apply()
d = np.load(S.DATA)
V = d["vertices"]          # (120,4) unit quaternions = 600-cell vertices
A = d["adjacency"]

PHI = (1 + 5 ** 0.5) / 2


def ortho_plane(a, b):
    """Gram-Schmidt a 4x2 orthonormal projector from two 4-vectors."""
    a = np.asarray(a, float); a /= np.linalg.norm(a)
    b = np.asarray(b, float); b -= (b @ a) * a; b /= np.linalg.norm(b)
    return np.column_stack([a, b])


def edges_of(adj):
    ii, jj = np.where(np.triu(adj) > 0)
    return list(zip(ii.tolist(), jj.tolist()))


def coxeter_plane(simple_roots):
    """The Coxeter-plane 4xN projector: build the Coxeter element from the
    simple reflections, take its complex eigenvector for the primitive
    rotation, and return [Re, Im] — the canonical symmetric projection."""
    n = len(simple_roots)
    w = np.eye(n)
    for a in simple_roots:
        a = np.asarray(a, float)
        Refl = np.eye(n) - 2 * np.outer(a, a) / (a @ a)
        w = Refl @ w
    evals, evecs = np.linalg.eig(w)
    # pick the eigenvalue closest to the primitive rotation e^{2 pi i / h}
    ang = np.angle(evals)
    k = np.argmin(np.abs(ang - np.min(np.abs(ang[ang > 1e-6]))))
    v = evecs[:, k]
    P = np.column_stack([v.real, v.imag])
    P[:, 0] /= np.linalg.norm(P[:, 0]); P[:, 1] /= np.linalg.norm(P[:, 1])
    return P


# H4 simple roots (the 600-cell's symmetry), golden-ratio entries.
H4 = np.array([
    [1, -1, 0, 0],
    [0, 1, -1, 0],
    [0, 0, 1, -1],
    [-0.5, -0.5 * (PHI - 1), -0.5 * PHI, 0],  # the golden node
], float)
P4 = coxeter_plane(H4)
# fall back to a plain symmetric plane if the Coxeter plane degenerates flat
if np.ptp(V @ P4) < 1e-6:
    P4 = ortho_plane([1, PHI, 0, 1 / PHI], [PHI, -1, 1 / PHI, 0])


def draw_polytope(ax, verts, adj, P, vsize=14, vcolor=S.INK,
                  ecolor=S.FOLD, elw=0.6, ealpha=0.9):
    XY = verts @ P
    for i, j in edges_of(adj):
        ax.plot([XY[i, 0], XY[j, 0]], [XY[i, 1], XY[j, 1]],
                color=ecolor, lw=elw, alpha=ealpha, zorder=1)
    ax.scatter(XY[:, 0], XY[:, 1], s=vsize, color=vcolor,
               zorder=3, edgecolors="white", linewidths=0.5)
    S.bare(ax)
    return XY


# ---------------------------------------------------------------- 600-cell
fig, ax = plt.subplots(figsize=(5.6, 5.6))
draw_polytope(ax, V, A, P4, vsize=15, ecolor=S.FOLD, elw=0.4, ealpha=0.55)
ax.set_title("The 600-cell: 120 corners, 720 edges",
             fontsize=11, color=S.INK, pad=8)
S.save(fig, "ch03-600cell")
plt.close(fig)


# ---------------------------------------------------------------- E8 roots
def e8_roots():
    roots = []
    # type 1: (+-1,+-1,0,...,0), all positions, 112 of them
    for i in range(8):
        for j in range(i + 1, 8):
            for si in (1, -1):
                for sj in (1, -1):
                    r = np.zeros(8); r[i] = si; r[j] = sj
                    roots.append(r)
    # type 2: (+-1/2)^8 with an even number of minus signs, 128 of them
    for m in range(256):
        signs = [(1 if (m >> k) & 1 == 0 else -1) for k in range(8)]
        if signs.count(-1) % 2 == 0:
            roots.append(np.array(signs) * 0.5)
    return np.array(roots)            # (240,8)


R = e8_roots()
# Coxeter-plane projection (Petrie view): the canonical 8 concentric 30-gons,
# built from the genuine Coxeter element of E8.
E8_simple = np.array([
    [1, -1, 0, 0, 0, 0, 0, 0],
    [0, 1, -1, 0, 0, 0, 0, 0],
    [0, 0, 1, -1, 0, 0, 0, 0],
    [0, 0, 0, 1, -1, 0, 0, 0],
    [0, 0, 0, 0, 1, -1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [-0.5] * 8,
    [0, 0, 0, 0, 0, 1, -1, 0],
], float)
E8_simple[6] = np.array([-0.5] * 8)
PE = coxeter_plane(E8_simple)
XY = R @ PE

fig, ax = plt.subplots(figsize=(5.6, 5.6))
# faint edges between roots at minimal mutual distance (the root polytope)
D = np.linalg.norm(R[:, None, :] - R[None, :, :], axis=2)
mind = np.min(D[D > 1e-6])
ii, jj = np.where(np.triu(np.abs(D - mind) < 1e-6))
for i, j in zip(ii, jj):
    ax.plot([XY[i, 0], XY[j, 0]], [XY[i, 1], XY[j, 1]],
            color=S.FAINT, lw=0.3, alpha=0.6, zorder=1)
ax.scatter(XY[:, 0], XY[:, 1], s=12, color=S.ACCENT, zorder=3,
           edgecolors="white", linewidths=0.4)
S.bare(ax)
ax.set_title("The E8 root system: 240 nearest neighbours in 8 dimensions",
             fontsize=11, color=S.INK, pad=8)
S.save(fig, "ch03-e8")
plt.close(fig)


# ------------------------------------------------------- downsampling cascade
# nested sub-polytopes, all genuine subsets of the 120 vertices:
axis_idx = [i for i, v in enumerate(V)
            if np.allclose(np.sort(np.abs(v)), [0, 0, 0, 1], atol=1e-6)]   # 8
half_idx = [i for i, v in enumerate(V)
            if np.allclose(np.abs(v), 0.5, atol=1e-6)]                     # 16
cell24 = sorted(axis_idx + half_idx)     # 24-cell  (Hurwitz units)
cell16 = sorted(half_idx)                # tesseract (16 corners)
assert len(cell24) == 24 and len(cell16) == 16


def own_edges(verts):
    """Connect each subset by its OWN nearest-neighbour distance."""
    D = np.linalg.norm(verts[:, None, :] - verts[None, :, :], axis=2)
    mind = np.min(D[D > 1e-6])
    adj = (np.abs(D - mind) < 1e-6).astype(int)
    return adj


# No single plane flatters all three nested polytopes, so each rung is shown in
# its OWN canonical projection: the 600-cell in its H4 Coxeter plane (P4), the
# 24-cell in its F4 Coxeter plane (twelvefold), the tesseract as cube-in-cube.
P24 = coxeter_plane(np.array(
    [[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, 0], [-0.5, -0.5, -0.5, -0.5]], float))
Ptess = np.array([[1, 0], [0, 1], [0.5, 0.42], [-0.126, 0.126]], float)
Ptess[:, 0] /= np.linalg.norm(Ptess[:, 0])
Ptess[:, 1] /= np.linalg.norm(Ptess[:, 1])

fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.1))
panels = [
    (V, A, P4, "120 corners", "the quantum grain", 14, S.FOLD, 0.4, 0.55),
    (V[cell24], own_edges(V[cell24]), P24, "24 corners", "the gravity grain",
     26, S.COOL, 0.7, 0.6),
    (V[cell16], own_edges(V[cell16]), Ptess, "16 corners", "coarser still",
     30, S.COOL, 1.0, 0.7),
]
for ax, (vv, aa, P, n, sub, vs, ec, lw, al) in zip(axes, panels):
    draw_polytope(ax, vv, aa, P, vsize=vs, ecolor=ec, elw=lw, ealpha=al)
    ax.set_title(n, fontsize=11.5, color=S.INK, pad=4)
    ax.text(0.5, -0.04, sub, transform=ax.transAxes, ha="center",
            va="top", fontsize=9.5, color=S.ACCENT)
S.save(fig, "ch09-downsampling")
plt.close(fig)
print("done geometry figures")
