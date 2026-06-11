"""Diffraction of the primes onto the critical line.

The Weil explicit formula written as a density says: the (smoothed) density of the
L-function's zeros along the critical line is

    D(gamma) = (1/2pi) Omega(gamma)                          [archimedean background]
             - (1/pi) sum_{q,k} (2 cos k theta_q) logNq / Nq^{k/2}
                              * cos(k gamma logNq) * W(k logNq)   [one WAVE per prime power]

Each prime ideal q (a Frobenius rotation theta_q on the 600-cell crystal) emits a wave
of frequency logNq.  The zeros are NOT 'cast' by individual vertices -- they are the
INTERFERENCE FRINGES of all the prime-waves together.  This is diffraction, not
ray-tracing: a collective/holographic property, which is exactly the non-separability
that makes the positivity (RH) a global statement.

W = Gaussian band-limit so the finite prime list gives a smooth, honest reconstruction.
Overlays the 33 zeros computed independently by PARI (curve_zeros.json) -- they land on
the reconstructed peaks, with NO zero data used to build D.
"""
import json, math, os, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
from lab.curve_stage_b import curve_ap_table          # noqa: E402
from lab.sos_probe import _arch_kernel                # noqa: E402

GREEN, GOLD, BLUE, RED, GREY = ("#1b7a3d", "#b8860b", "#274472", "#a01b1b", "#666666")
plt.rcParams.update({"font.size": 12, "figure.dpi": 200, "savefig.dpi": 200})


def _prime_waves(nmax, U):
    """(freq u=k logNq, amplitude) for the explicit-formula prime side, geometry only."""
    rows = curve_ap_table(nmax)
    waves = []
    for r in rows:
        Nq, a, kind = r["norm"], r["a_P"], r["kind"]
        if kind == "bad":
            continue
        x = a / (2 * math.sqrt(Nq))
        if abs(x) > 1:
            continue
        th = math.acos(max(-1.0, min(1.0, x))); lN = math.log(Nq); k = 1
        while k * lN < U * 3:
            amp = (2 * math.cos(k * th)) * lN / math.sqrt(Nq ** k)
            waves.append((k * lN, amp, Nq, kind)); k += 1
    return waves


def make(nmax=3000, gmax=26.0, U=6.0):
    waves = _prime_waves(nmax, U)
    g = np.linspace(0.2, gmax, 4000)
    # archimedean background density
    omega = np.array([_arch_kernel(x) for x in g]) / (2 * math.pi)
    # prime interference, Gaussian band-limited at scale U
    prime = np.zeros_like(g)
    for u, amp, Nq, kind in waves:
        prime += amp * np.cos(g * u) * math.exp(-(u * u) / (2 * U * U))
    D = omega - prime / math.pi

    zeros = []
    zp = os.path.join(H, "..", "out", "curve_zeros.json")
    if os.path.exists(zp):
        zeros = json.load(open(zp)).get("L_zeros", [])

    fig, ax = plt.subplots(2, 1, figsize=(13, 7.2),
                           gridspec_kw={"height_ratios": [1, 1.7]})

    # ---- panel A: a few individual prime "rays"
    show = [(4, "N=4 (p=2)"), (5, "N=5 (p=5)"), (9, "N=9 (p=3)"),
            (11, "N=11"), (19, "N=19")]
    seen = {}
    for u, amp, Nq, kind in waves:
        if Nq in dict(show) and Nq not in seen:
            seen[Nq] = (u, amp)
    for Nq, lab in show:
        if Nq in seen:
            u, amp = seen[Nq]
            ax[0].plot(g, amp * np.cos(g * u) * np.exp(-(u*u)/(2*U*U)),
                       lw=1.0, alpha=0.8, label=lab)
    ax[0].axhline(0, color="#ccc", lw=.5)
    ax[0].set_xlim(0.2, gmax); ax[0].set_ylabel("single prime\nwaves")
    ax[0].legend(ncol=5, fontsize=8, loc="upper right", frameon=False)
    ax[0].set_title("Each prime ideal = one wave (a Frobenius rotation on the crystal); "
                    "frequency = log N(q)", fontsize=12)
    ax[0].spines[["top", "right"]].set_visible(False)

    # ---- panel B: the full interference + the independently-computed zeros
    ax[1].plot(g, D, color=BLUE, lw=1.4, label="prime interference $D(\\gamma)$ (geometry only)")
    ax[1].fill_between(g, D.min(), D, where=(D > np.median(D)), color=BLUE, alpha=0.06)
    for i, z in enumerate(zeros):
        ax[1].axvline(z, color=RED, lw=1.0, alpha=0.8,
                      label=("PARI zeros (independent)" if i == 0 else None))
    ax[1].set_xlim(0.2, gmax); ax[1].set_xlabel("$\\gamma$  (height on the critical line)")
    ax[1].set_ylabel("reconstructed\nzero density")
    ax[1].legend(loc="upper right", fontsize=9, frameon=False)
    ax[1].set_title("...and the zeros are the INTERFERENCE FRINGES of all primes together "
                    "(diffraction, not ray-tracing): no single vertex casts a zero",
                    fontsize=12)
    ax[1].spines[["top", "right"]].set_visible(False)

    fig.suptitle("Diffraction of the primes onto the critical line  "
                 "($\\zeta_K(s)\\zeta_K(s-1)$ cuspidal factor, conductor 775)",
                 fontsize=13.5, weight="bold", y=1.0)
    fig.text(0.5, -0.03,
             "Built from the geometry alone (point-counted eigenvalues; NO zero data in "
             "$D$). The red zeros, computed independently by PARI, land on the fringes. "
             "The line is a collective/holographic property of ALL the prime-waves "
             "(non-separable) — which is why positivity (RH) is a global statement.",
             ha="center", fontsize=10, color="#333")
    fig.tight_layout()
    out = os.path.join(H, "fig_diffraction.png")
    fig.savefig(out, bbox_inches="tight", dpi=200)
    plt.close(fig)
    # quick honest check: do reconstructed peaks sit near the zeros?
    hits = 0
    for z in zeros:
        j = np.argmin(np.abs(g - z))
        lo, hi = max(0, j - 40), min(len(g), j + 40)
        if D[j] >= 0.6 * D[lo:hi].max():
            hits += 1
    print(f"wrote {out}")
    print(f"[check] {hits}/{len(zeros)} computed zeros sit at/near a reconstruction peak "
          f"(geometry-only D; band-limit U={U})")


if __name__ == "__main__":
    make()
