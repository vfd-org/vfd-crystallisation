#!/usr/bin/env python3
"""Clean explanatory schematics — line-art in the book's textbook register,
deliberately plain (no glow, no cosmic styling).

  ch03-platonic.png        the five Platonic solids (real coordinates)
  ch02-closure-ladder.png  the gradient from distinction to self-modelling
  ch05-combing.png         why S2 can't be combed but S3 (and S7) can
  ch06-rendering-pipeline.png   bare numbers -> looking -> a scene
  ch09-cascade-ladder.png  the rungs as resolutions / domains of physics
  ch10-one-field-three-forces.png  one field, three settings, three laws
  ch11-division-ladder.png the number-system ladder and what each gives up
  ch12-symmetry-breaking.png   the marble on the dome: law vs history
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon
from itertools import combinations
import _style as S

S.apply()
PHI = (1 + 5 ** 0.5) / 2


def box(ax, xy, w, h, text, fc="white", ec=S.INK, tc=S.INK, fs=10, lw=1.1):
    x, y = xy
    p = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                       boxstyle="round,pad=0.02,rounding_size=0.06",
                       fc=fc, ec=ec, lw=lw, zorder=3)
    ax.add_patch(p)
    ax.text(x, y, text, ha="center", va="center", fontsize=fs,
            color=tc, zorder=4)


def arrow(ax, p0, p1, color=S.INK, lw=1.3, style="-|>", mut=12):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=mut,
                                 color=color, lw=lw, zorder=2,
                                 shrinkA=2, shrinkB=2))


# ============================================================ Platonic solids
def solid(verts):
    V = np.array(verts, float)
    D = np.linalg.norm(V[:, None] - V[None], axis=2)
    md = np.min(D[D > 1e-6])
    E = [(i, j) for i, j in combinations(range(len(V)), 2)
         if abs(D[i, j] - md) < 1e-6]
    return V, E


def reg_solids():
    t = (1 + 5 ** 0.5) / 2
    tet = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
    cube = [(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)]
    octa = [(s, 0, 0) for s in (-1, 1)] + [(0, s, 0) for s in (-1, 1)] + \
           [(0, 0, s) for s in (-1, 1)]
    ico = []
    for a in (-1, 1):
        for b in (-t, t):
            ico += [(0, a, b), (a, b, 0), (b, 0, a)]          # 12 verts
    dod = [(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)]  # 8
    for s1 in (-1, 1):
        for s2 in (-1, 1):
            dod += [(0, s1 / t, s2 * t), (s1 / t, s2 * t, 0),
                    (s2 * t, 0, s1 / t)]                       # +12 = 20
    return [("tetrahedron", tet), ("cube", cube), ("octahedron", octa),
            ("dodecahedron", dod), ("icosahedron", ico)]


def rot3(yaw, pitch):
    cy, sy = np.cos(yaw), np.sin(yaw)
    cp, sp = np.cos(pitch), np.sin(pitch)
    Ry = np.array([[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]])
    Rx = np.array([[1, 0, 0], [0, cp, -sp], [0, sp, cp]])
    return Rx @ Ry


# a viewing angle chosen per solid so the silhouette is recognisable
VIEWS = {
    "tetrahedron": rot3(0.65, 0.40),
    "cube": rot3(0.55, 0.42),
    "octahedron": rot3(0.785, 0.45),
    "dodecahedron": rot3(0.10, 0.62),   # near face-on: pentagon reads
    "icosahedron": rot3(0.32, 0.36),    # near a vertex: five-fold cap reads
}


def draw_solid(ax, V, E, R):
    V = V / np.max(np.linalg.norm(V, axis=1))    # unit circumradius
    P = V @ R.T
    xy, z = P[:, :2], P[:, 2]
    zr = (z.max() - z.min()) or 1.0
    # back-to-front so near edges overdraw far ones; depth sets alpha + weight
    for i, j in sorted(E, key=lambda e: z[e[0]] + z[e[1]]):
        f = ((z[i] + z[j]) / 2 - z.min()) / zr    # 0 = far, 1 = near
        ax.plot([xy[i, 0], xy[j, 0]], [xy[i, 1], xy[j, 1]], color=S.INK,
                lw=0.5 + 1.3 * f, alpha=0.22 + 0.72 * f,
                solid_capstyle="round", zorder=1 + f)
    zn = (z - z.min()) / zr
    ax.scatter(xy[:, 0], xy[:, 1], s=8 + 26 * zn, color=S.ACCENT, zorder=6,
               edgecolors="white", linewidths=0.5)
    S.bare(ax)
    ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.25, 1.25)


fig, axes = plt.subplots(1, 5, figsize=(12.6, 3.1))
for ax, (name, verts) in zip(axes, reg_solids()):
    V, E = solid(verts)
    draw_solid(ax, V, E, VIEWS[name])
    ax.set_title(name, fontsize=10.5, color=S.INK, pad=6)
fig.suptitle("The five Platonic solids — the complete list three dimensions allow",
             fontsize=11.5, y=1.04)
S.save(fig, "ch03-platonic")
plt.close(fig)


# ============================================================ closure ladder
fig, ax = plt.subplots(figsize=(9.5, 3.4))
stages = [
    ("a distinction", "one mark: this, not that"),
    ("a relation", "two, and a link"),
    ("a loop", "feeds back on itself"),
    ("a stable pattern", "holds its form"),
    ("self-modelling", "a model of itself, inside"),
]
n = len(stages)
for k, (title, sub) in enumerate(stages):
    x = k * 2.1
    y = k * 0.30
    # glyph
    if k == 0:
        ax.scatter([x], [y + 1.0], s=40, color=S.ACCENT, zorder=4)
    elif k == 1:
        ax.scatter([x - 0.18, x + 0.18], [y + 1.0, y + 1.0], s=34,
                   color=S.ACCENT, zorder=4)
        ax.plot([x - 0.18, x + 0.18], [y + 1.0, y + 1.0], color=S.INK, lw=1.2)
    else:
        circ = Circle((x, y + 1.0), 0.26, fill=False, ec=S.ACCENT, lw=1.6,
                      zorder=4)
        ax.add_patch(circ)
        ax.add_patch(FancyArrowPatch((x + 0.26, y + 1.07), (x + 0.20, y + 1.27),
                     arrowstyle="-|>", mutation_scale=9, color=S.ACCENT, lw=1.4))
        if k >= 3:
            ax.add_patch(Circle((x, y + 1.0), 0.12, fill=False, ec=S.COOL, lw=1.2))
        if k == 4:
            ax.add_patch(Circle((x, y + 1.0), 0.05, fill=False, ec=S.COOL, lw=1.0))
    ax.text(x, y + 0.45, title, ha="center", fontsize=10, color=S.INK)
    ax.text(x, y + 0.18, sub, ha="center", fontsize=8.2, color=S.FOLD, style="italic")
# baseline arrow
ax.annotate("", xy=(n * 2.1 - 1.4, -0.2), xytext=(-0.6, -0.2),
            arrowprops=dict(arrowstyle="-|>", color=S.INK, lw=1.3))
ax.text((n * 2.1) / 2 - 0.9, -0.45, "increasing closure  —  consistency holding itself together",
        ha="center", fontsize=9.5, color=S.INK)
ax.set_xlim(-1, n * 2.1); ax.set_ylim(-0.7, 2.9)
S.bare(ax)
S.save(fig, "ch02-closure-ladder")
plt.close(fig)


# ============================================================ combing spheres
fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.2))
# left: S2 with a cowlick (fails)
ax = axes[0]
ax.add_patch(Circle((0, 0), 1.0, fill=False, ec=S.INK, lw=1.3))
for t in np.linspace(0, 2 * np.pi, 16, endpoint=False):
    x, y = 0.80 * np.cos(t), 0.80 * np.sin(t)
    dx, dy = -np.sin(t) * 0.20, np.cos(t) * 0.20      # tangent swirl
    ax.add_patch(FancyArrowPatch((x, y), (x + dx, y + dy), arrowstyle="-|>",
                 mutation_scale=7, color=S.FOLD, lw=1.0))
ax.scatter([0], [1.0], s=80, color=S.ACCENT, zorder=5)
ax.annotate("a cowlick:\nthe directions\nmust fail here",
            xy=(0, 1.0), xytext=(1.15, 1.15), fontsize=8.4, color=S.ACCENT,
            ha="left", va="center",
            arrowprops=dict(arrowstyle="-", color=S.ACCENT, lw=0.8))
S.bare(ax)
ax.set_xlim(-1.5, 1.9); ax.set_ylim(-1.7, 1.6)
ax.set_title("the 2-sphere can't be combed", fontsize=11, pad=10)
ax.text(0.2, -1.5, "no smooth set of directions covers all of it —\none point always fails",
        ha="center", fontsize=8.8, color=S.INK)
# right: S3/S7 schematic — clean little frames at sample points
ax = axes[1]
ax.add_patch(Circle((0, 0), 1.0, fill=False, ec=S.INK, lw=1.3, ls=(0, (4, 3))))
for t in np.linspace(0, 2 * np.pi, 6, endpoint=False):
    x, y = 0.62 * np.cos(t), 0.62 * np.sin(t)
    for ddx, ddy, c in [(0.22, 0, S.ACCENT), (0, 0.22, S.COOL), (0.15, 0.15, S.FOLD)]:
        ax.add_patch(FancyArrowPatch((x, y), (x + ddx, y + ddy), arrowstyle="-|>",
                     mutation_scale=6, color=c, lw=1.2))
S.bare(ax)
ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.7, 1.6)
ax.set_title("the 3-sphere (and the 7-sphere) can", fontsize=11, pad=10)
ax.text(0, -1.5, "a full frame of directions sits smoothly at every point —\nthree on the 3-sphere, seven on the 7-sphere",
        ha="center", fontsize=8.8, color=S.INK)
S.save(fig, "ch05-combing")
plt.close(fig)


# ============================================================ rendering pipeline
fig, ax = plt.subplots(figsize=(11.0, 3.6))
box(ax, (1.1, 1.6), 1.5, 2.2,
    "120 bare\nnumbers\n\n(a column,\nnot a scene)", fc="#f6f4f0", fs=9)
box(ax, (4.4, 2.55), 2.0, 0.7, "an observer's corner", fc="white", fs=9.2)
box(ax, (4.4, 1.6), 2.0, 0.7, "three directions", fc="white", fs=9.2)
box(ax, (4.4, 0.65), 2.0, 0.7, "a resolution dial", fc="white", fs=9.2)
box(ax, (7.6, 1.6), 1.7, 1.1, "looking\n(the one\nforced kernel)", fc="#f6ece2",
    ec=S.ACCENT, tc=S.ACCENT, fs=9.4)
box(ax, (10.0, 2.25), 1.9, 0.95, "fixed background\n(the 20 core corners)",
    fc="white", fs=8.6)
box(ax, (10.0, 0.95), 1.9, 0.95, "moving foreground\n(the 100 surface corners)",
    fc="white", fs=8.6)
arrow(ax, (1.95, 1.6), (3.35, 1.6))
for yy in (2.55, 1.6, 0.65):
    arrow(ax, (5.45, yy), (6.7, 1.6), color=S.FOLD)
arrow(ax, (8.5, 1.6), (8.95, 2.1), color=S.ACCENT)
arrow(ax, (8.5, 1.6), (8.95, 1.05), color=S.ACCENT)
ax.set_xlim(0, 11.2); ax.set_ylim(-0.1, 3.2)
S.bare(ax)
ax.set_title("Looking: how a column of numbers becomes a scene", fontsize=11.5, pad=6)
S.save(fig, "ch06-rendering-pipeline")
plt.close(fig)


# ============================================================ cascade ladder
fig, ax = plt.subplots(figsize=(8.6, 4.6))
rungs = [
    ("E8", "the 8-dimensional pinnacle", S.FOLD, 3.6),
    ("600-cell · 120 corners", "the quantum grain — particles, masses", S.ACCENT, 2.7),
    ("24-cell · 24 corners", "the gravity grain — curved space", S.COOL, 1.8),
    ("tesseract · 16 corners", "coarser still — information", S.FOLD, 0.9),
]
for i, (name, sub, col, y) in enumerate(rungs):
    box(ax, (3.2, y), 4.4, 0.62, "", fc="white", ec=col, lw=1.6)
    ax.text(1.15, y, name, ha="left", va="center", fontsize=10.2, color=S.INK)
    ax.text(5.4, y, sub, ha="right", va="center", fontsize=8.6, color=S.FOLD,
            style="italic")
    if i < len(rungs) - 1:
        arrow(ax, (3.2, rungs[i][3] - 0.32), (3.2, rungs[i + 1][3] + 0.32),
              color=S.INK, lw=1.1)
ax.annotate("", xy=(6.2, 0.7), xytext=(6.2, 3.5),
            arrowprops=dict(arrowstyle="-|>", color=S.INK, lw=1.2))
ax.text(6.45, 2.1, "coarser sampling", rotation=90, va="center",
        fontsize=9.2, color=S.INK)
ax.set_xlim(0.8, 6.9); ax.set_ylim(0.3, 4.1)
S.bare(ax)
ax.set_title("The cascade: one sphere sampled at every grain", fontsize=11.5, pad=6)
S.save(fig, "ch09-cascade-ladder")
plt.close(fig)


# ============================================================ one field, three forces
fig, ax = plt.subplots(figsize=(9.6, 3.8))
box(ax, (1.7, 1.6), 2.0, 1.3, "one\nsubstrate field", fc="#f6ece2",
    ec=S.ACCENT, tc=S.ACCENT, fs=11)
outs = [
    (2.7, "fine grain", "Schrödinger's equation", "quantum mechanics"),
    (1.6, "one rung coarser", "Maxwell's equations", "electromagnetism"),
    (0.5, "coarse grain", "Einstein's equations", "gravity"),
]
for y, dial, law, dom in outs:
    arrow(ax, (2.8, 1.6), (4.5, y), color=S.FOLD)
    ax.text(3.6, (1.6 + y) / 2 + 0.06 * (y - 1.6), dial, ha="center",
            fontsize=8.2, color=S.FOLD, style="italic")
    box(ax, (6.4, y), 3.0, 0.8, f"{law}", fc="white", fs=9.6)
    ax.text(8.5, y, dom, ha="left", va="center", fontsize=8.4, color=S.COOL)
ax.set_xlim(0.4, 10.2); ax.set_ylim(-0.1, 3.3)
S.bare(ax)
ax.set_title("One field, three settings of a single dial", fontsize=11.5, pad=6)
S.save(fig, "ch10-one-field-three-forces")
plt.close(fig)


# ============================================================ division ladder
fig, ax = plt.subplots(figsize=(9.8, 4.0))
ladder = [
    ("the real line", "dimension 1", "ordinary numbers", ""),
    ("the complex plane", "dimension 2", "gives up: ordering", ""),
    ("the quaternions", "dimension 4", "gives up: commutativity", "our space, 3 directions"),
    ("the octonions", "dimension 8", "gives up: associativity", "the 7-direction arena"),
]
for i, (name, dim, gives, arena) in enumerate(ladder):
    x = i * 2.35
    y = i * 0.55
    box(ax, (x + 1.0, y + 0.5), 1.9, 0.95, f"{name}\n{dim}", fc="white",
        ec=S.INK, fs=9.4)
    ax.text(x + 1.0, y - 0.1, gives, ha="center", fontsize=8.3,
            color=S.ACCENT if "gives up" in gives else S.FOLD)
    if arena:
        ax.text(x + 1.0, y + 1.18, arena, ha="center", fontsize=8.0, color=S.COOL)
    if i < len(ladder) - 1:
        arrow(ax, (x + 1.7, y + 0.7), (x + 2.35 + 0.25, y + 0.55 + 0.7),
              color=S.INK)
# the wall
xw = 4 * 2.35
yw = 4 * 0.55
ax.plot([xw + 0.2, xw + 0.2], [yw - 0.2, yw + 1.3], color=S.ACCENT, lw=2.4)
ax.text(xw + 0.45, yw + 0.55, "stops here\n(zero divisors:\nnonzero × nonzero = 0)",
        ha="left", va="center", fontsize=8.4, color=S.ACCENT)
ax.set_xlim(-0.3, xw + 2.4); ax.set_ylim(-0.6, yw + 1.6)
S.bare(ax)
ax.set_title("The ladder of number systems — and where it has to stop",
             fontsize=11.5, pad=6)
S.save(fig, "ch11-division-ladder")
plt.close(fig)


# ============================================================ symmetry breaking
fig, ax = plt.subplots(figsize=(8.4, 4.0))
x = np.linspace(-2.2, 2.2, 400)
# sombrero cross-section: a bump in the middle, wells either side
y = (x ** 2 - 1.2) ** 2 * 0.5
ax.plot(x, y, color=S.INK, lw=1.6, zorder=2)
# marble at the unstable top
ax.scatter([0], [(0 - 1.2) ** 2 * 0.5 + 0.06], s=120, color=S.FOLD,
           zorder=4, edgecolors=S.INK, linewidths=1.0)
ax.text(0, 1.35, "the marble can't stay at the top", ha="center",
        fontsize=9.2, color=S.INK)
# rolled-down marble in one well (history's choice)
wx = np.sqrt(1.2)
ax.scatter([wx], [0.06], s=120, color=S.ACCENT, zorder=5,
           edgecolors=S.INK, linewidths=1.0)
ax.add_patch(FancyArrowPatch((0.25, 0.55), (wx - 0.2, 0.18), arrowstyle="-|>",
             mutation_scale=12, color=S.ACCENT, lw=1.5,
             connectionstyle="arc3,rad=-0.3"))
ax.text(wx, -0.18, "it ends up here — but it could have gone the other way",
        ha="center", fontsize=8.8, color=S.ACCENT)
ax.text(0, -0.55, "the law gives the symmetric dome;  the accident of history gives the direction",
        ha="center", fontsize=9.4, color=S.INK)
ax.set_xlim(-2.3, 2.3); ax.set_ylim(-0.7, 1.6)
S.bare(ax)
ax.set_title("Selection: how one world is chosen from many", fontsize=11.5, pad=6)
S.save(fig, "ch12-symmetry-breaking")
plt.close(fig)
print("done schematics")
