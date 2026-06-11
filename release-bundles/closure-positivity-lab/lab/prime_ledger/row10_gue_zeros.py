"""Row 10 — Zero statistics (GUE): this row IS the wall.

Every conjectural row above has the same layer-2 factor: correlations of
zeros. This row measures those correlations directly on ~2,400 zeta zeros
(computed by PARI/GP, out/_zeta_zeros.gp -> out/zeta_zeros.txt) and checks
them against the random-matrix (GUE) prediction:

  - unfolded nearest-neighbour spacings: mean 1, variance 3*pi/8 - 1 = 0.1781
    (Wigner surmise for GUE), strong level repulsion (almost no spacings < 0.2);
  - Montgomery pair correlation R2(u) = 1 - (sin(pi u)/(pi u))^2.

Layer 1 (verified): the computed zeros match GUE statistics within
HEIGHT-CALIBRATED tolerances. At height T the pair correlation carries known
finite-height corrections of relative size ~ 1/log(T/2pi) (Berry's
semiclassical theory) — about 0.17 at T = 2500, which is why Odlyzko needed
zeros near height 10^12 for clean asymptotic agreement. The qualitative GUE
signature that IS decisive at this height: level repulsion. Poisson statistics
put 18% of spacings below 0.2; GUE puts ~0.3% there. Montgomery's THEOREM
covers restricted test functions only; the full GUE law is conjectural — so
unlike rows 4/6/7 this anchor calibrates a CONJECTURE's numerical face, and
is labelled so.

Our own 33 icosian-L zeros are far too few for spacing statistics; they are
reported descriptively, not gated — honesty over decoration.

Layer 2: there is no deeper layer. Proving these correlation laws (or even RH
itself, which they refine) is the single wall every other row points at.
"""
import os

import numpy as np

from . import core

ZEROS_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "out",
                          "zeta_zeros.txt")
GUE_VAR = 3 * np.pi / 8 - 1  # variance of the GUE Wigner-surmise spacing


def unfold(t):
    """Riemann-von Mangoldt smooth counting function N(t)."""
    return t / (2 * np.pi) * np.log(t / (2 * np.pi * np.e)) + 7.0 / 8.0


def run(s=None):  # sieve unused
    path = os.path.abspath(ZEROS_PATH)
    if not os.path.exists(path):
        return core.row_result(
            10, "zero statistics (GUE)", "data missing",
            "run: gp -q out/_zeta_zeros.gp", {"error": "no zeta_zeros.txt"},
            "n/a", "SKIP", "n/a")
    t = np.loadtxt(path)
    w = unfold(t)
    sp = np.diff(w)
    n = sp.size
    mean, var = float(np.mean(sp)), float(np.var(sp))
    repulsion = float(np.mean(sp < 0.2))

    # Montgomery pair correlation on unfolded zeros, u in (0, 3]
    bins = np.arange(0.0, 3.0 + 1e-9, 0.25)
    diffs = []
    for k in range(1, 40):  # successive differences cover u <= 3 easily
        d = w[k:] - w[:-k]
        diffs.append(d[d <= 3.0])
        if d.min() > 3.0:
            break
    d = np.concatenate(diffs)
    hist, _ = np.histogram(d, bins=bins)
    density = hist / (n * 0.25)  # normalized pair density per unit
    centers = 0.5 * (bins[1:] + bins[:-1])
    gue = 1.0 - (np.sin(np.pi * centers) / (np.pi * centers)) ** 2
    pc_dev = float(np.max(np.abs(density - gue)))

    # finite-height correction scale at this T (Berry): ~ 1/log(T/2pi)
    corr_scale = float(1.0 / np.log(t[-1] / (2 * np.pi)))
    gate = ("spacing mean within 1% of 1; repulsion P(s<0.2) < 0.03 (Poisson "
            "gives 0.18 - the decisive qualitative test); variance and pair "
            "correlation within the finite-height correction scale "
            "1/log(T/2pi) of GUE (~0.17 relative at T=2500)")
    ok = (abs(mean - 1) < 0.01 and repulsion < 0.03
          and abs(var - GUE_VAR) < corr_scale * GUE_VAR
          and pc_dev < corr_scale)
    return core.row_result(
        10, "zero statistics — the wall itself (GUE / pair correlation)",
        "Montgomery (1973) THEOREM for restricted test functions; full GUE "
        "law conjectural (Odlyzko numerics)",
        "none deeper: these correlations ARE the open global factor of every "
        "conjectural row above (1, 2, 3, 8) and of RH itself",
        {"n_zeros": int(t.size), "height": float(t[-1]),
         "spacing_mean": round(mean, 4), "spacing_var": round(var, 4),
         "gue_var": round(float(GUE_VAR), 4),
         "repulsion_P(s<0.2)": round(repulsion, 4),
         "poisson_would_give": round(1 - np.exp(-0.2), 4),
         "pair_corr_max_dev": round(pc_dev, 4),
         "finite_height_correction_scale": round(corr_scale, 4),
         "height_note": "asymptotic-GUE precision needs zeros at far greater "
                        "heights (Odlyzko); at T=2500 deviations of this "
                        "scale are the documented finite-height corrections",
         "icosian_L_note": "our 33 zeros are too few for spacing statistics; "
                           "not gated (n=33)"},
        gate, "PASS" if ok else "FAIL",
        "Compute more zeros (raise the height in out/_zeta_zeros.gp): "
        "spacing variance drifting from GUE, vanishing repulsion, or pair "
        "correlation departing from 1 - sinc^2 kills the row.")


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
