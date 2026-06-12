"""Shared visual style for The Crystal and the Clock figures.

Textbook-clean register (Quanta / Carroll), deliberately NOT mystical:
flat white ground, ink line-art, one restrained warm accent, one cool accent,
greys for secondary structure. No glow, no gradients-as-decoration, serif type.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# palette (shared with fig_spectrum.py)
INK    = "#1a1a1a"   # primary line / text
ACCENT = "#b3541e"   # warm ochre — the "load-bearing" thing in each figure
COOL   = "#2f6f8f"   # muted teal — the second actor / comparison
FOLD   = "#9aa0a6"   # grey — secondary / context structure
FAINT  = "#d6d3cd"   # very light grey — gridlines, backdrops
PAPER  = "#ffffff"

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "scripts" / "600cell_data.npz"
OUT  = Path(__file__).resolve().parents[1]


def apply():
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "figure.facecolor": PAPER,
        "savefig.facecolor": PAPER,
        "axes.facecolor": PAPER,
        "axes.edgecolor": INK,
        "axes.linewidth": 0.8,
        "text.color": INK,
        "axes.labelcolor": INK,
        "xtick.color": INK,
        "ytick.color": INK,
    })


def save(fig, stem):
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(OUT / f"{stem}.{ext}", dpi=220, bbox_inches="tight")
    print("saved:", OUT / f"{stem}.png")


def bare(ax):
    """Strip an axes to nothing — for schematics and projections."""
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_aspect("equal")
