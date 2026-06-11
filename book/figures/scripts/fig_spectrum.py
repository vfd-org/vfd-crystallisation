#!/usr/bin/env python3
"""
Track-A figure (precise, from real data): the 600-cell Laplacian spectrum,
showing the perfect-square eigenspace multiplicities that ARE the S^3
harmonic series 1,4,9,16,25,36. This is the book's hero figure for Ch4
("What the Spectrum Knows"): dimension 3 read straight off the substrate.

Generates book/figures/ch04-spectrum.{png,pdf} from scripts/600cell_data.npz.
Nothing is faked; the eigenvalues and multiplicities are computed live.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "scripts" / "600cell_data.npz"
OUT = Path(__file__).resolve().parents[1]

d = np.load(DATA)
A = d["adjacency"].astype(float)
L = np.diag(A.sum(1)) - A
ev = np.round(np.linalg.eigvalsh(L), 6)
vals = sorted(set(ev.tolist()))
mult = [int(np.sum(ev == v)) for v in vals]

# the unprimed S^3 harmonic chain (k+1)^2 for k=0..5 in increasing-lambda order
harm = {1: 0, 4: 1, 9: 2, 16: 3, 25: 4, 36: 5}
seen_k, chain = set(), []
for v, m in zip(vals, mult):
    if m in harm and harm[m] not in seen_k:
        chain.append((v, m, harm[m])); seen_k.add(harm[m])

INK = "#1a1a1a"
ACCENT = "#b3541e"   # warm ochre, restrained
FOLD = "#9aa0a6"     # grey for the folded/primed blocks

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.edgecolor": INK,
    "axes.linewidth": 0.8,
    "text.color": INK,
    "axes.labelcolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
})

fig, ax = plt.subplots(figsize=(7.2, 4.4))
chain_lams = {v for v, _, _ in chain}
for v, m in zip(vals, mult):
    on_chain = v in chain_lams
    c = ACCENT if on_chain else FOLD
    ax.vlines(v, 0, m, color=c, lw=1.4 if on_chain else 1.0,
              alpha=1.0 if on_chain else 0.7, zorder=2)
    ax.plot(v, m, "o", color=c, ms=5 if on_chain else 3.5,
            zorder=3, mec="white", mew=0.6)

# annotate the harmonic chain with k and the square
for v, m, k in chain:
    ax.annotate(f"${int(round(m**0.5))}^2={m}$", (v, m),
                xytext=(0, 9), textcoords="offset points",
                ha="center", fontsize=9.5, color=ACCENT)

ax.set_xlabel("Laplacian eigenvalue  $\\lambda$")
ax.set_ylabel("multiplicity  (size of eigenspace)")
ax.set_ylim(0, 40)
ax.set_xlim(-0.6, 16.4)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_yticks([0, 1, 4, 9, 16, 25, 36])

# a quiet note distinguishing the two families
ax.plot([], [], "o", color=ACCENT, ms=5, label="$S^3$ harmonics  $(k{+}1)^2$,  $k=0\\ldots5$")
ax.plot([], [], "o", color=FOLD, ms=3.5, label="folded (primed-irrep) blocks")
ax.legend(frameon=False, fontsize=9, loc="upper left", handletextpad=0.4)

fig.tight_layout()
for ext in ("png", "pdf"):
    fig.savefig(OUT / f"ch04-spectrum.{ext}", dpi=220, bbox_inches="tight")

print("multiplicities:", mult)
print("harmonic chain (lambda, mult, k):", chain)
print("saved:", OUT / "ch04-spectrum.png", "and .pdf")
