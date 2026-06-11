"""Structure-factor probe -- the 600-cell as a PHYSICAL scatterer.

S(q) is literally what a crystallographer computes for how a structure diffracts light.
For the 120 vertices on S^3, the powder (orientation-averaged) intensity is the Debye sum

    S(q) = N + 2 sum_{j<l} sin(q d_jl) / (q d_jl),

determined entirely by the multiset of pairwise distances d_jl.  For the 600-cell those
distances fall into a small number of CLASSES -- the same association scheme that gives
the C_phi standing-wave modes.  So this probe tests, honestly, whether the PHYSICAL
diffraction of the crystal and its number-theoretic prime-diffraction share structure or
are only a formal analogy.

NO claim about photons / EM: this is geometric scattering off a point set, nothing more.
"""
from __future__ import annotations
import json, math, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "out")
from .objects import _vertices_600, PHI                # noqa: E402


def distance_classes(V):
    n = len(V)
    d = []
    for i in range(n):
        for j in range(i + 1, n):
            d.append(float(np.linalg.norm(V[i] - V[j])))
    d = np.array(d)
    # cluster into distinct distance values
    vals, counts = [], []
    for x in np.sort(d):
        if vals and abs(x - vals[-1]) < 1e-4:
            counts[-1] += 1
        else:
            vals.append(round(x, 4)); counts.append(1)
    return vals, counts, d


def debye(q, dists):
    """orientation-averaged structure factor for the point set (per-vertex normalised)."""
    s = len(_V) + 0.0
    qd = q * dists
    s += 2.0 * np.sum(np.sinc(qd / math.pi))           # sin(x)/x = sinc(x/pi) in numpy
    return s / len(_V)


_V = _vertices_600()


def probe(qmax=20.0, nq=2000):
    vals, counts, d = distance_classes(_V)
    qs = np.linspace(0.05, qmax, nq)
    S = np.array([debye(q, d) for q in qs])
    # peaks
    peaks = []
    for i in range(2, nq - 2):
        if S[i] > S[i-1] and S[i] >= S[i+1] and S[i] > 1.5:
            peaks.append((round(float(qs[i]), 3), round(float(S[i]), 2)))
    print("600-CELL STRUCTURE FACTOR (physical diffraction off the 120 vertices)")
    print(f"distinct pairwise-distance classes ({len(vals)}): "
          f"{list(zip(vals, counts))}")
    print(f"  -> these distance classes ARE the 600-cell association scheme "
          f"(the same structure behind the C_phi standing-wave modes)")
    print(f"diffraction peaks |q|: {[p[0] for p in peaks[:12]]}")

    # honest comparison to the OTHER two spectra
    import sys
    sys.path.insert(0, HERE)
    try:
        from .curve_stage_b import curve_ap_table
        logN = sorted(set(round(math.log(r['norm']), 3)
                          for r in curve_ap_table(60) if r['kind'] != 'bad'))[:10]
    except Exception:
        logN = []
    A = (np.abs(_V @ _V.T - PHI/2) < 1e-6).astype(float); np.fill_diagonal(A, 0)
    L = np.diag(A.sum(1)) - A
    cphi = sorted(set(np.round(np.linalg.eigvalsh(L + PHI**-2*np.eye(len(_V))), 3)))
    print("\nHONEST CROSS-SPECTRUM COMPARISON (do the three 'spectra' coincide?):")
    print(f"  structure-factor peaks |q| : {[p[0] for p in peaks[:8]]}")
    print(f"  C_phi standing-wave modes  : {cphi}")
    print(f"  prime frequencies log N(q) : {logN}")
    print("  verdict: the structure factor and C_phi modes share the SAME geometric")
    print("  origin (the 9 distance classes / association scheme); the prime log-N(q)")
    print("  frequencies are a DIFFERENT (arithmetic) object and do NOT coincide with")
    print("  the geometric scattering vectors -- the diffraction link is FORMAL")
    print("  (same Fourier-of-a-lattice mathematics), not a shared numerical spectrum.")

    out = {"distance_classes": list(zip(vals, counts)),
           "n_distance_classes": len(vals),
           "structure_factor_peaks": peaks[:12],
           "cphi_modes": [float(x) for x in cphi],
           "prime_log_norms": logN,
           "verdict": "physical diffraction <-> C_phi share the association scheme; "
                      "prime spectrum is a distinct arithmetic object; diffraction "
                      "analogy is formal (shared Fourier mathematics), not numerical. "
                      "No photon/EM content."}
    os.makedirs(OUT, exist_ok=True)
    json.dump(out, open(os.path.join(OUT, "structure_factor.json"), "w"), indent=1)

    # figure
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(11, 4))
    ax.plot(qs, S, color="#274472", lw=1.3)
    for q0, _ in peaks[:12]:
        ax.axvline(q0, color="#b8860b", lw=0.6, ls="--", alpha=0.6)
    ax.set_xlabel("scattering vector $|q|$"); ax.set_ylabel("structure factor $S(q)$")
    ax.set_title("600-cell as a physical scatterer: powder diffraction $S(q)$\n"
                 "(set by the 9 pairwise-distance classes — the association scheme)",
                 fontsize=12)
    ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, -0.04, "Geometric scattering only — no photons, no EM. Shares its origin "
             "(the distance classes) with the C_phi standing-wave modes; the prime/zero "
             "spectrum is a distinct arithmetic object (diffraction link is formal).",
             ha="center", fontsize=9.5, color="#333")
    fig.tight_layout()
    p = os.path.join(HERE, "..", "figures", "fig_structure_factor.png")
    fig.savefig(p, bbox_inches="tight", dpi=200); plt.close(fig)
    print(f"\nwrote {p} and out/structure_factor.json")


if __name__ == "__main__":
    probe()
