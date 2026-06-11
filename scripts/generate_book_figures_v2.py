#!/usr/bin/env python3
"""
Generate the Tier-1 book figures from computed data (no hand-drawn values).

  f1  ch04-multiplicities : the 600-cell Laplacian spectrum with its
                            perfect-square multiplicities 1,4,9,16,25,36
  f2  ch09-dispersion     : discrete eigenvalues vs the continuum S^3 law
  f3  ch06-kernel-decay   : rendering-kernel locality vs graph distance
  f4  ch09-light-bending  : ray deflection through the derived metric,
                            tensor (factor 4GM/b) vs scalar control (half)
  f5  ch08-mass-shells    : the cascade mass-shell ladder with offsets
                            (muon and Z highlighted)

Output: book/figures/<name>.pdf and .png

Usage:
    python scripts/generate_book_figures_v2.py
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "book" / "figures"
DATA = np.load(Path(__file__).resolve().parent / "600cell_data.npz")

plt.rcParams.update({
    "font.size": 11, "axes.spines.top": False, "axes.spines.right": False,
    "figure.dpi": 110,
})
INK = "#1a1a2e"
ACC = "#c0392b"
BLU = "#2c5f8a"


def save(fig, name):
    for ext in ("pdf", "png"):
        fig.savefig(OUT / f"{name}.{ext}", bbox_inches="tight",
                    dpi=220 if ext == "png" else None)
    plt.close(fig)
    print(f"  wrote book/figures/{name}.pdf/.png")


def f1_multiplicities():
    evals = np.round(np.linalg.eigvalsh(DATA["laplacian"].astype(float)), 6)
    counts = Counter(evals)
    lams = sorted(counts)
    mults = [counts[l] for l in lams]
    theta = np.pi / 5
    band = [12 * (1 - np.sin((k + 1) * theta) / ((k + 1) * np.sin(theta)))
            for k in range(6)]
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    for l, m in zip(lams, mults):
        in_band = any(abs(l - b) < 1e-6 for b in band)
        ax.bar(l, m, width=0.18, color=ACC if in_band else "#b8b8c8",
               zorder=3)
        if in_band:
            k = min(range(6), key=lambda kk: abs(band[kk] - l))
            ax.annotate(f"{m} = {k+1}²", (l, m), textcoords="offset points",
                        xytext=(0, 4), ha="center", fontsize=9, color=INK)
    ax.set_xlabel("vibration frequency (Laplacian eigenvalue)")
    ax.set_ylabel("number of independent patterns")
    ax.set_title("The crystal's spectrum: multiplicities are perfect squares\n"
                 "— the signature of a three-dimensional sphere", fontsize=11)
    save(fig, "ch04-multiplicities")


def f2_dispersion():
    theta = np.pi / 5
    ks = np.arange(0, 6)
    lam = [12 * (1 - np.sin((k + 1) * theta) / ((k + 1) * np.sin(theta)))
           for k in ks]
    kc = np.linspace(0, 5.4, 200)
    cont = 2 * theta**2 * kc * (kc + 2)
    fig, ax = plt.subplots(figsize=(6.0, 3.8))
    ax.plot(kc, cont, "-", color=BLU, lw=1.6,
            label="smooth sphere law  2θ²·k(k+2)")
    ax.plot(ks, lam, "o", color=ACC, ms=7, zorder=3,
            label="600-cell eigenvalues (exact)")
    for k, l in zip(ks, lam):
        ax.annotate(f"k={k}", (k, l), textcoords="offset points",
                    xytext=(6, -10), fontsize=9, color=INK)
    ax.set_xlabel("harmonic degree k")
    ax.set_ylabel("frequency")
    ax.set_title("The crystal's notes vs the smooth sphere's: they agree at\n"
                 "low pitch and bend away at the resolution limit, at a\n"
                 "rate given in closed form", fontsize=11)
    ax.legend(frameon=False, fontsize=9, loc="upper left")
    save(fig, "ch09-dispersion")


def f3_kernel_decay():
    L = DATA["laplacian"].astype(float)
    A = DATA["adjacency"]
    n = len(L)
    # graph distances from vertex 0 (BFS)
    from collections import deque
    dist = -np.ones(n, dtype=int)
    dist[0] = 0
    q = deque([0])
    while q:
        v = q.popleft()
        for w in np.nonzero(A[v])[0]:
            if dist[w] < 0:
                dist[w] = dist[v] + 1
                q.append(w)
    fig, ax = plt.subplots(figsize=(6.0, 3.8))
    for r, c in ((0.4, "#88a8c8"), (0.8, BLU), (1.6, INK)):
        Pi = np.linalg.inv(np.eye(n) + r**2 * L)
        row = np.abs(Pi[0])
        ds = sorted(set(dist))
        prof = [np.mean(row[dist == d]) for d in ds]
        ax.semilogy(ds, prof, "o-", color=c, ms=5, lw=1.4,
                    label=f"resolution r = {r}")
    ax.set_xlabel("graph distance from the anchor")
    ax.set_ylabel("kernel weight (log scale)")
    ax.set_title("Looking is local: the rendering kernel's weight falls\n"
                 "exponentially with distance, faster at finer resolution",
                 fontsize=11)
    ax.legend(frameon=False, fontsize=9)
    save(fig, "ch06-kernel-decay")


def f4_light_bending():
    # ray tracing through n(r) = 1 + (1+w)/2 * h00(r), h00 = 2GM/r
    GM = 0.018  # exaggerated for visibility
    b0 = 0.35

    def trace(w):
        n_of = lambda r: 1 + (1 + w) * GM / np.maximum(r, 0.05)
        # gradient of log n perpendicular to ray, simple RK integration
        pos = np.array([-3.0, b0])
        dirv = np.array([1.0, 0.0])
        path = [pos.copy()]
        ds = 0.004
        for _ in range(1500):
            r = np.linalg.norm(pos)
            grad = -(1 + w) * GM / max(r, 0.05) ** 2 * pos / max(r, 0.05)
            grad_perp = grad - (grad @ dirv) * dirv
            dirv = dirv + ds * grad_perp / n_of(r)
            dirv /= np.linalg.norm(dirv)
            pos = pos + ds * dirv
            path.append(pos.copy())
        return np.array(path)

    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    th = np.linspace(0, 2 * np.pi, 100)
    ax.fill(0.09 * np.cos(th), 0.09 * np.sin(th), color="#e8b84b", zorder=3)
    ax.plot([-3, 3], [b0, b0], ":", color="#b8b8c8", lw=1.2,
            label="no gravity (straight)")
    p_s = trace(0.0)
    ax.plot(p_s[:, 0], p_s[:, 1], "--", color=BLU, lw=1.6,
            label="time-warp only (Newton's value)")
    p_t = trace(1.0)
    ax.plot(p_t[:, 0], p_t[:, 1], "-", color=ACC, lw=1.8,
            label="derived metric: time + space warp (twice the bend)")
    ax.set_xlim(-3, 3)
    ax.set_ylim(-0.6, 0.5)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.annotate("mass", (0, -0.02), ha="center", va="top", fontsize=9,
                color="#8a6d1f")
    ax.set_title("The 1919 test, from the derived field: spatial warping\n"
                 "doubles the deflection — the factor the derivation forces",
                 fontsize=11)
    ax.legend(frameon=False, fontsize=8.5, loc="upper center",
              bbox_to_anchor=(0.5, -0.02), ncol=1)
    save(fig, "ch09-light-bending")


def f5_mass_shells():
    # cascade-masses.md §E3.1 (PDG 2024 central values, m_P = 1.22089e19 GeV)
    rows = [
        ("electron", 107.079), ("muon", 95.99980), ("tau", 90.135),
        ("up", 104.084), ("down", 102.481), ("strange", 96.256),
        ("charm", 90.828), ("bottom", 88.357), ("top", 80.623),
        ("proton", 91.462), ("W", 82.213), ("Z", 81.95097),
        ("Higgs", 81.291),
    ]
    fig, ax = plt.subplots(figsize=(6.2, 4.4))
    for i, (name, nsh) in enumerate(sorted(rows, key=lambda r: -r[1])):
        off = nsh - round(nsh)
        star = abs(off) < 0.05
        ax.plot([0, off], [i, i], "-", color="#d8d8e0", lw=3, zorder=2)
        ax.plot(off, i, "o", ms=8 if star else 6,
                color=ACC if star else BLU, zorder=3)
        ax.annotate(f"{name}  (shell {round(nsh)})", (-0.52, i),
                    fontsize=9, va="center", color=INK)
        if star:
            ax.annotate(f"{off:+.4f}" if abs(off) < 0.001 else f"{off:+.3f}",
                        (off, i), textcoords="offset points", xytext=(8, -3),
                        fontsize=8, color=ACC)
    ax.axvline(0, color=INK, lw=1)
    ax.set_xlim(-0.55, 0.55)
    ax.set_yticks([])
    ax.set_xlabel("offset from the nearest integer shell\n"
                  "(golden-ratio steps below the Planck mass)")
    ax.set_title("The mass ladder: every particle's shell, and how far it\n"
                 "sits from an integer — the muon and Z land almost exactly",
                 fontsize=11)
    save(fig, "ch08-mass-shells")


def main():
    OUT.mkdir(exist_ok=True)
    print("Generating book figures (v2):")
    f1_multiplicities()
    f2_dispersion()
    f3_kernel_decay()
    f4_light_bending()
    f5_mass_shells()
    print("done.")


if __name__ == "__main__":
    main()
