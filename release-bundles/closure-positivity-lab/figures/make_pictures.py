"""Generate the five figures for papers/how-the-primes-work.tex.

All figures are computed, not drawn: the wheels are exact residue counts, the
bars are sieve counts, the race is the exact lead sequence, the diffraction
panels are computed structure factors with independently computed zeta zeros
overlaid. Run from the bundle root:  python3 figures/make_pictures.py
"""
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from lab.prime_ledger import core  # noqa: E402

OUT = os.path.dirname(os.path.abspath(__file__))
GREEN, WARM, DEAD, ALIVE = "#0b6e4f", "#b54708", "#d9d9d9", "#9fd6b9"
PHI = (1 + 5 ** 0.5) / 2


def wheel(ax, p, offsets, title):
    """Draw the mod-p wheel: cell r is dead iff some offset hits 0 mod p."""
    dead = [r for r in range(p) if any((r + o) % p == 0 for o in offsets)]
    th = np.linspace(0, 2 * np.pi, p, endpoint=False) + np.pi / 2
    for r in range(p):
        c = DEAD if r in dead else ALIVE
        ax.bar(th[r], 1.0, width=2 * np.pi / p * 0.92, bottom=0.35,
               color=c, edgecolor="white", linewidth=2)
        ax.text(th[r], 0.92, str(r), ha="center", va="center", fontsize=13,
                color="#1a1f2b")
    alive = p - len(dead)
    ax.set_title("%s\n%d of %d cells survive" % (title, alive, p), fontsize=11)
    ax.set_axis_off()


def fig_wheels():
    fig, axes = plt.subplots(2, 2, figsize=(9, 9),
                             subplot_kw={"projection": "polar"})
    wheel(axes[0][0], 3, (0, 2), "twins (n, n+2) on the mod-3 wheel")
    wheel(axes[0][1], 3, (0, 6), "gap 6 (n, n+6) on the mod-3 wheel")
    wheel(axes[1][0], 5, (0, 2), "twins on the mod-5 wheel")
    wheel(axes[1][1], 3, (0, 2, 4), "(n, n+2, n+4): every cell dies")
    fig.suptitle("Patterns live or die cell-by-cell on each prime's wheel",
                 fontsize=14)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_wheels.png"), dpi=160)
    plt.close(fig)
    print("fig_wheels.png")


def fig_gaps(s):
    hs = list(range(2, 212, 2))
    n2 = core.count_pairs(s, 2)
    measured = [core.count_pairs(s, h) / n2 for h in hs]
    predicted = [core.gap_local_ratio(h) for h in hs]
    fig, ax = plt.subplots(figsize=(11, 4.2))
    ax.bar(hs, measured, width=1.6, color="#d8cfc4", label="measured (sieve to $5{\\times}10^7$)")
    ax.plot(hs, predicted, "o", ms=4, color=GREEN, label="predicted: $\\prod_{p|h,\\ p>2}(p-1)/(p-2)$")
    ax.set_xlabel("gap $h$"); ax.set_ylabel("abundance relative to twins")
    ax.legend(frameon=False); ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("Every even gap's abundance from its wheels alone")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_gap_bullseyes.png"), dpi=160)
    plt.close(fig)
    print("fig_gap_bullseyes.png")


def fig_race(s):
    P = core.primes_from(s)
    D = np.cumsum(np.where(P % 4 == 3, 1, np.where(P % 4 == 1, -1, 0)))
    idx = np.unique(np.logspace(np.log10(2), np.log10(P.size - 1), 3000).astype(int))
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4), width_ratios=[2, 1])
    a1.semilogx(P[idx], D[idx], color=WARM, lw=1.6)
    a1.axhline(0, color="#9aa3af", lw=0.8)
    a1.axvline(26861, color=GREEN, ls="--", lw=1)
    a1.text(26861, max(D[idx]) * 0.9, " 26,861", color=GREEN)
    a1.set_xlabel("$x$"); a1.set_ylabel("$\\pi(x;4,3)-\\pi(x;4,1)$")
    a1.set_title("The Chebyshev race to $5\\times10^7$")
    lo, hi = np.searchsorted(P, 26_000), np.searchsorted(P, 28_000)
    a2.plot(P[lo:hi], D[lo:hi], color=WARM, lw=1.2)
    a2.axhline(0, color="#9aa3af", lw=0.8)
    a2.plot([26861], [-1], "o", color=GREEN, ms=7)
    a2.set_title("first crossing: one point below zero")
    a2.set_xlabel("$x$")
    for a in (a1, a2):
        a.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_bias_race.png"), dpi=160)
    plt.close(fig)
    print("fig_bias_race.png")


def prime_spectrum(s, kmax=60.0, dk=0.01, xmax=1_000_000):
    P = core.primes_from(s[:xmax]).astype(np.float64)
    lg = np.log(P)
    # Riesz taper (1 - log p / log X): a sharp cutoff Gibbs-rings and smears
    # the peaks (5/15 aligned); the smooth taper resolves them (13/15, the
    # rest being close zero-pairs merged at this resolution).
    w = lg / np.sqrt(P) * (1.0 - lg / np.log(xmax))
    ks = np.arange(0.0, kmax + dk / 2, dk)
    F = np.empty(ks.size)
    chunk = 400
    for i in range(0, ks.size, chunk):
        kc = ks[i:i + chunk]
        F[i:i + chunk] = np.abs((w[None, :] *
                                 np.exp(1j * np.outer(kc, lg))).sum(axis=1))
    return ks, F


def fig_prime_diffraction(s):
    ks, F = prime_spectrum(s)
    zeros = np.loadtxt(os.path.join(ROOT, "out", "zeta_zeros.txt"))
    zeros = zeros[zeros <= 60]
    fig, ax = plt.subplots(figsize=(11, 4.2))
    m = ks >= 5.0  # clip the k->0 divergence (the pole term) so peaks fill the frame
    ax.plot(ks[m], F[m], color=WARM, lw=0.9,
            label="the primes' spectrum: $|\\sum_p w(p) \\log(p)\\, p^{-1/2+ik}|$, $p < 10^6$, smooth taper $w$")
    for j, z in enumerate(zeros):
        ax.axvline(z, color=GREEN, ls="--", lw=0.8, alpha=0.8,
                   label="zeta zeros (computed independently)" if j == 0 else None)
    ax.set_xlabel("$k$"); ax.set_ylabel("amplitude")
    ax.set_title("The diffraction pattern of the primes peaks at the zeta zeros")
    ax.legend(frameon=False, loc="upper right")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_prime_diffraction.png"), dpi=160)
    plt.close(fig)
    # internal validation: do spectrum maxima align with the zeros?
    hits = 0
    for z in zeros[:15]:
        i = np.argmin(np.abs(ks - z))
        lo, hi = max(0, i - 50), i + 50
        peak_k = ks[lo + np.argmax(F[lo:hi])]
        hits += abs(peak_k - z) < 0.15
    print("fig_prime_diffraction.png  (peak alignment: %d/15 zeros within 0.15)" % hits)
    return hits


def fig_fibonacci():
    # Fibonacci chain by substitution A->AB, B->A; tile lengths phi and 1
    word = "A"
    while len(word) < 3000:
        word = "".join("AB" if c == "A" else "A" for c in word)
    steps = np.array([PHI if c == "A" else 1.0 for c in word[:3000]])
    x_fib = np.cumsum(steps)
    rng = np.random.default_rng(31)  # fixed seed: reproducible figure
    x_rnd = np.sort(rng.uniform(0, x_fib[-1], x_fib.size))
    ks = np.arange(0.05, 30.0, 0.005)

    def spec(x):
        F = np.empty(ks.size)
        for i in range(0, ks.size, 400):
            kc = ks[i:i + 400]
            F[i:i + 400] = np.abs(np.exp(1j * np.outer(kc, x)).sum(axis=1)) ** 2
        return F / x.size

    fig, (a1, a2) = plt.subplots(2, 1, figsize=(11, 5.6), sharex=True)
    a1.plot(ks, spec(x_fib), color=GREEN, lw=0.8)
    a1.set_title("Fibonacci $\\varphi$-chain: sharp peaks with no period — a quasicrystal")
    a2.plot(ks, spec(x_rnd), color="#9aa3af", lw=0.8)
    a2.set_title("the same number of points at random: no structure")
    a2.set_xlabel("$k$")
    for a in (a1, a2):
        a.set_ylabel("intensity / N")
        a.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig_fibonacci.png"), dpi=160)
    plt.close(fig)
    print("fig_fibonacci.png")


def main():
    print("sieving ...")
    s = core.sieve()
    fig_wheels()
    fig_gaps(s)
    fig_race(s)
    fig_prime_diffraction(s)
    fig_fibonacci()


if __name__ == "__main__":
    main()
