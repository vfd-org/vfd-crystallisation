"""Figure for the pair-correlation instrument: the ramp and the plateau.
Run from the repo root: python3 figures/make_pair_correlation.py"""
import json
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
GREEN, WARM = "#0b6e4f", "#b54708"

with open(os.path.join(ROOT, "out", "pair_correlation.json")) as fh:
    d = json.load(fh)
taus = np.array(d["taus"])
K = np.array(d["K_decimated"])

fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.2), width_ratios=[3, 2])
a1.plot(taus, K, color="#c8b8a8", lw=0.7, alpha=0.8,
        label="$K(\\tau)$, raw decimated (exponential-type scatter)")
gb = d["gated_bins"]
a1.plot(gb["ramp_centers"], gb["ramp_means"], "o-", color=WARM, lw=2,
        ms=4, label="gated bin means (ramp)")
a1.plot(gb["plateau_centers"], gb["plateau_means"], "s-", color=WARM,
        lw=2, ms=4, mfc="white", label="gated bin means (plateau)")
tt = np.linspace(0, 3, 200)
a1.plot(tt, np.minimum(tt, 1), "--", color=GREEN, lw=1.6,
        label="sine-kernel $\\min(\\tau,1)$")
a1.axvspan(0, 1, color=GREEN, alpha=0.06)
a1.text(0.45, 1.55, "ramp window\n(Montgomery-ramp\nrange)", fontsize=9,
        color=GREEN, ha="center")
a1.text(2.0, 1.55, "plateau: the conjectural half\n(= the wall's second floor)",
        fontsize=9, color="#5b6472", ha="center")
a1.set_xlabel("$\\tau$ (unfolded)")
a1.set_ylabel("$K(\\tau)$")
a1.set_ylim(0, 1.8)
a1.legend(frameon=False, fontsize=9, loc="lower right")
a1.set_title("Spectral form factor of %d zeta zeros" % d["n_zeros"])

al = np.array(d["montgomery_panel"]["alphas"])
F = np.array(d["montgomery_panel"]["F"])
dT = d["montgomery_panel"]["finite_T_diagonal_level"]
a2.plot(al, F, color=WARM, lw=1.5, label="$F(\\alpha, T)$ measured")
a2.axhline(dT, color=GREEN, ls="--", lw=1.2,
           label="finite-$T$ level $d_T$ = %.3f" % dT)
a2.set_xlabel("$\\alpha$")
a2.set_ylim(0, max(2.0, F.max() * 1.05))
a2.legend(frameon=False, fontsize=9)
a2.set_title("Montgomery's $F$ (finite-$T$ panel)")
for a in (a1, a2):
    a.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "fig_pair_correlation.png"), dpi=160)
print("fig_pair_correlation.png")
