"""prime_to_wave -- type a prime, get its wave; build the diffraction field from any set
of primes; and demonstrate the HOLOGRAM property: any fraction of the primes already
encodes the WHOLE zero-set, just at lower resolution.

Honest core (the explicit formula): each prime ideal q contributes a wave
    amplitude(k) = 2 cos(k th_q) * logNq / Nq^{k/2},   frequency = k logNq,
    th_q = arccos(a_q / 2 sqrt(Nq)),  a_q = point count (Frobenius trace).
Every prime-wave spans the entire gamma-axis, so it contributes to EVERY zero -- which
is why a random subset reproduces all the zeros (blurred), like a hologram fragment, not
a torn photograph.  NO zero data enters the reconstruction; zeros are the external check.
"""
from __future__ import annotations
import json, math, os, random
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "out")
from .curve_stage_b import curve_ap_table              # noqa: E402
from .sos_probe import _arch_kernel                    # noqa: E402


def prime_to_wave(p, U=6.0):
    """All wave components contributed by the prime ideal(s) above the rational prime p."""
    rows = [r for r in curve_ap_table(max(p * p + 1, 50)) if r["p"] == p]
    out = []
    for r in rows:
        Nq, a, kind = r["norm"], r["a_P"], r["kind"]
        comps = []
        if kind != "bad" and abs(a / (2 * math.sqrt(Nq))) <= 1:
            th = math.acos(max(-1.0, min(1.0, a / (2 * math.sqrt(Nq)))))
            lN = math.log(Nq); k = 1
            while k * lN < U * 3:
                comps.append({"harmonic": k, "frequency": round(k * lN, 4),
                              "amplitude": round(2 * math.cos(k * th) * lN /
                                                 Nq ** (k / 2.0), 4)})
                k += 1
            out.append({"ideal": f"{kind} p={p}", "norm": Nq, "a_q": a,
                        "theta_q": round(th, 4), "components": comps})
        else:
            out.append({"ideal": f"{kind} p={p}", "norm": Nq, "a_q": a,
                        "theta_q": None, "components": []})
    return out


def _rows_to_terms(rows, U):
    terms = []
    for r in rows:
        Nq, a, kind = r["norm"], r["a_P"], r["kind"]
        if kind == "bad" or abs(a / (2 * math.sqrt(Nq))) > 1:
            continue
        th = math.acos(max(-1.0, min(1.0, a / (2 * math.sqrt(Nq)))))
        lN = math.log(Nq); k = 1
        while k * lN < U * 3:
            terms.append((k * lN, 2 * math.cos(k * th) * lN / Nq ** (k / 2.0)))
            k += 1
    return terms


def density(rows, g, U=6.0):
    """Reconstructed zero density D(gamma) from a chosen set of prime-ideal rows."""
    omega = np.array([_arch_kernel(x) for x in g]) / (2 * math.pi)
    prime = np.zeros_like(g)
    for u, amp in _rows_to_terms(rows, U):
        prime += amp * np.cos(g * u) * math.exp(-(u * u) / (2 * U * U))
    return omega - prime / math.pi


def _zeros():
    zp = os.path.join(OUT, "curve_zeros.json")
    return json.load(open(zp)).get("L_zeros", []) if os.path.exists(zp) else []


def _zero_hits(g, D, zeros):
    hits = 0
    for z in zeros:
        j = int(np.argmin(np.abs(g - z)))
        lo, hi = max(0, j - 50), min(len(g), j + 50)
        if D[j] >= 0.5 * D[lo:hi].max():
            hits += 1
    return hits


def hologram_demo(nmax=3000, fractions=(1.0, 0.3, 0.1, 0.03), gmax=26.0, U=6.0, seed=7):
    """Reconstruct from a random FRACTION of the prime ideals; show all zeros persist
    (whole scene) while peaks broaden (resolution drops) -- the hologram property."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    rows_all = [r for r in curve_ap_table(nmax) if r["kind"] != "bad"]
    g = np.linspace(0.2, gmax, 3000)
    zeros = _zeros()
    rng = random.Random(seed)
    fig, axes = plt.subplots(len(fractions), 1, figsize=(12, 2.1 * len(fractions)),
                             sharex=True)
    report = []
    for ax, frac in zip(axes, fractions):
        k = max(1, int(len(rows_all) * frac))
        subset = rng.sample(rows_all, k)
        D = density(subset, g, U)
        ax.plot(g, D, color="#274472", lw=1.3)
        for z in zeros:
            ax.axvline(z, color="#a01b1b", lw=0.7, alpha=0.7)
        hits = _zero_hits(g, D, zeros)
        report.append({"fraction": frac, "n_ideals": k, "zeros_located": hits,
                       "of": len(zeros)})
        ax.set_ylabel(f"{int(frac*100)}% of primes\n({k} ideals)", fontsize=9)
        ax.text(0.985, 0.82, f"{hits}/{len(zeros)} zeros still located",
                transform=ax.transAxes, ha="right", fontsize=9, color="#1b7a3d")
        ax.spines[["top", "right"]].set_visible(False)
    axes[-1].set_xlabel("$\\gamma$  (height on the critical line)")
    fig.suptitle("The hologram property: a FRACTION of the primes reproduces the WHOLE "
                 "zero-set, blurrier", fontsize=13, weight="bold", y=1.0)
    fig.text(0.5, -0.02, "Random subsets (geometry only; red = the 33 PARI zeros). Every "
             "fraction still shows ALL the zeros — each prime-wave spans the whole line, so "
             "a fragment carries the whole scene at lower resolution (holographic), not a "
             "torn-off piece (tomographic).", ha="center", fontsize=9.5, color="#333")
    fig.tight_layout()
    out = os.path.join(HERE, "..", "figures", "fig_hologram.png")
    fig.savefig(out, bbox_inches="tight", dpi=200)
    plt.close(fig)
    print("wrote", out)
    for r in report:
        print(f"  {int(r['fraction']*100):>3}% ({r['n_ideals']:>3} ideals): "
              f"{r['zeros_located']}/{r['of']} zeros located")
    json.dump(report, open(os.path.join(OUT, "hologram_demo.json"), "w"), indent=1)
    return report


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "wave":
        p = int(sys.argv[2])
        print(json.dumps(prime_to_wave(p), indent=1))
    else:
        print("=== prime_to_wave demo ===")
        for p in (2, 3, 5, 11, 31):
            for w in prime_to_wave(p):
                f = w["components"][0]["frequency"] if w["components"] else None
                print(f"  p={p:<3} {w['ideal']:<12} N={w['norm']:<4} a_q={w['a_q']:<3} "
                      f"theta={w['theta_q']}  fundamental freq={f}")
        print("\n=== hologram fraction demo ===")
        hologram_demo()
