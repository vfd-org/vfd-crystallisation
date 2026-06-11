"""Sato-Tate fit + discrepancy curve from the 664 geometric eigenvalues (frontier-run).
Left: histogram of cos(theta_q)=a_q/(2 sqrt Nq) vs the SU(2) semicircle (2/pi)sqrt(1-x^2).
Right: sqrt(n)*D_n (Kolmogorov-Smirnov discrepancy vs the ST CDF) -- the forcing instrument;
bounded/flat == square-root-cancellation (GRH) regime. NO RH claim; evidence not proof.
"""
import json, math, os, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
from lab.geometric_forcing import _st_cdf            # noqa: E402

GREEN, BLUE, RED = "#1b7a3d", "#274472", "#a01b1b"
plt.rcParams.update({"font.size": 12, "figure.dpi": 200, "savefig.dpi": 200})


def _xs():
    geo = json.load(open(os.path.join(H, "..", "..", "frontier-run", "out",
                                       "a_q_extended.json")))["rows"]
    xs = []
    for g in sorted(geo, key=lambda r: r["norm"]):
        Nq, a = g["norm"], g["a_q_geometric"]
        if Nq == 31 and not g.get("self_adjoint", True):
            continue
        x = a / (2 * math.sqrt(Nq))
        if abs(x) <= 1:
            xs.append(x)
    return xs


def _disc(v):
    v = sorted(v); n = len(v); D = 0.0
    for i, x in enumerate(v):
        F = _st_cdf(x)
        D = max(D, abs((i + 1) / n - F), abs(i / n - F))
    return D


def make():
    xs = _xs(); n = len(xs)
    fig, ax = plt.subplots(1, 2, figsize=(13, 4.6))
    # left: histogram vs semicircle, WITH the statistical-noise band around the curve
    bins = 24; w = 2.0 / bins
    ax[0].hist(xs, bins=bins, range=(-1, 1), density=True, color=BLUE, alpha=0.5,
               edgecolor="white", label=f"{n} geometric eigenvalues")
    t = np.linspace(-0.999, 0.999, 400)
    pst = (2 / math.pi) * np.sqrt(1 - t * t)
    # +/-2 sigma band the bars are EXPECTED to land in (binomial noise on a density hist)
    se = np.sqrt(np.maximum(pst * (1 - pst * w), 0) / (n * w))
    ax[0].fill_between(t, np.maximum(pst - 2 * se, 0), pst + 2 * se, color=RED, alpha=0.18,
                       label=r"expected $\pm2\sigma$ scatter band")
    ax[0].plot(t, pst, color=RED, lw=2,
               label=r"Sato--Tate $\frac{2}{\pi}\sqrt{1-x^2}$")
    ax[0].set_xlabel(r"$\cos\theta_\mathfrak{q}=a_\mathfrak{q}/2\sqrt{N\mathfrak{q}}$")
    ax[0].set_ylabel("density")
    m2 = sum(x*x for x in xs)/n; m4 = sum(x**4 for x in xs)/n
    ax[0].set_title(f"Sato--Tate fit (norm $\\leq$ 4999):  "
                    f"$E[x^2]$={m2:.4f} (ST .25),  $E[x^4]$={m4:.4f} (ST .125)",
                    fontsize=11)
    ax[0].legend(fontsize=9, frameon=False); ax[0].spines[["top","right"]].set_visible(False)
    # right: sqrt(n) D_n
    ns = [16, 32, 64, 128, 256, 400, n]
    y = [_disc(xs[:k]) * math.sqrt(k) for k in ns]
    ax[1].plot(ns, y, "o-", color=GREEN, lw=1.6, ms=6)
    ax[1].axhline(np.mean(y), color="#999", ls="--", lw=1,
                  label=f"mean $\\approx${np.mean(y):.2f} (bounded)")
    ax[1].set_xscale("log"); ax[1].set_xlabel("$n$ (eigenvalues, log)")
    ax[1].set_ylabel(r"$\sqrt{n}\,D_n$"); ax[1].set_ylim(0, 1.4)
    ax[1].set_title("forcing instrument: $\\sqrt{n}\\,D_n$ bounded\n"
                    "$\\Rightarrow$ consistent with square-root-cancellation (GRH) regime",
                    fontsize=11)
    ax[1].legend(fontsize=9, frameon=False); ax[1].spines[["top","right"]].set_visible(False)
    fig.suptitle("Equidistribution of the icosian Brandt spectrum (664 eigenvalues, "
                 "geometry-only; evidence, not proof)", fontsize=12.5, weight="bold", y=1.01)
    fig.tight_layout()
    out = os.path.join(H, "fig_satotate.png")
    fig.savefig(out, bbox_inches="tight", dpi=200); plt.close(fig)
    print("wrote", out, f"(n={n}, sqrt(n)Dn mean={np.mean(y):.3f})")


if __name__ == "__main__":
    make()
