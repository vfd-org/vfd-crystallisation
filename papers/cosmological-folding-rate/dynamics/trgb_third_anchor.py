"""TRGB as a third independent H0 anchor — discriminates 1/12 vs other models.

If 1/12 is real, the question is whether TRGB (Freedman 69.8 ± 1.7) lands
in the right place. TRGB sits between Planck (67.36) and SH0ES (73.04).

Key physics question: what is the natural prediction for an INTERMEDIATE
distance ladder?

Three competing pictures, each predicting where TRGB should land:

  (A) Same correction as SH0ES:
      H_TRGB = H_Planck · (1 + 1/12) = 72.97
      → 1.86σ tension with observed 69.80

  (B) ΛCDM null (no correction):
      H_TRGB = H_Planck = 67.36
      → 1.43σ tension with observed 69.80

  (C) Resolution-dependent correction. TRGB anchors at lower precision /
      different stellar population than Cepheids; if the projection
      coupling depends on resolution C_i, TRGB sees a *fractional* correction.
      Suppose TRGB samples half the σ-paired sector that SH0ES samples,
      i.e. (1 + 1/24):
      H_TRGB = H_Planck · (1 + 1/24) = 70.16
      → 0.21σ tension with observed 69.80

Picture (C) is the most VFD-flavoured but is post-hoc. The honest test is:
which of (A), (B), (C) gives the smallest |z| WITHOUT TUNING?

We score all three plus a few more substrate-derived candidates.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Anchor:
    name: str
    H0: float
    sigma: float


PLANCK = Anchor("Planck18 (early)", 67.36, 0.54)
TRGB   = Anchor("Freedman21 TRGB",  69.80, 1.70)
SH0ES  = Anchor("Riess22 SH0ES",    73.04, 1.04)


@dataclass(frozen=True)
class Hyp:
    name: str
    eps: float
    rationale: str


def hyps() -> List[Hyp]:
    return [
        Hyp("ΛCDM null",          0.0,         "no correction"),
        Hyp("1/24 (half-fold)",   1.0/24,      "half of 1/12 — TRGB samples half boundary"),
        Hyp("1/18",               1.0/18,      "between 12 and 24"),
        Hyp("1/12 (full-fold)",   1.0/12,      "same as SH0ES — full boundary"),
        Hyp("1/8 (frame inv)",    1.0/8,       "frame-ladder inverse"),
        Hyp("1/(2·6)",            1.0/12,      "duplicate of 1/12 (different rationale)"),
        Hyp("ln(φ)/(2π)·(1/2)",   math.log((1+math.sqrt(5))/2)/(4*math.pi),
            "log-period damped"),
    ]


def score(eps: float, anchor: Anchor, target: Anchor) -> dict:
    pred = anchor.H0 * (1 + eps)
    sigma_pred = anchor.sigma * (1 + eps)
    sigma_total = math.hypot(sigma_pred, target.sigma)
    z = (pred - target.H0) / sigma_total
    return {"predicted": pred, "delta": pred - target.H0, "abs_z": abs(z)}


def main() -> None:
    print("=" * 70)
    print("TRGB as third independent anchor — comparing folding hypotheses")
    print("=" * 70)
    print(f"  Planck:  {PLANCK.H0} ± {PLANCK.sigma}")
    print(f"  TRGB:    {TRGB.H0} ± {TRGB.sigma}")
    print(f"  SH0ES:   {SH0ES.H0} ± {SH0ES.sigma}")
    print()

    print(f"{'hypothesis':<22} {'pred(TRGB)':>10} {'|z|':>5}    "
          f"{'pred(SH0ES)':>11} {'|z|':>5}     rationale")
    print("-" * 100)
    for h in hyps():
        rt = score(h.eps, PLANCK, TRGB)
        rs = score(h.eps, PLANCK, SH0ES)
        print(f"{h.name:<22} {rt['predicted']:>10.2f} {rt['abs_z']:>5.2f}    "
              f"{rs['predicted']:>11.2f} {rs['abs_z']:>5.2f}     {h.rationale}")

    print()
    print("Joint score sum_z = |z_TRGB| + |z_SH0ES|:")
    rows = []
    for h in hyps():
        rt = score(h.eps, PLANCK, TRGB)
        rs = score(h.eps, PLANCK, SH0ES)
        rows.append((h.name, rt['abs_z'] + rs['abs_z'], rt['abs_z'], rs['abs_z']))
    rows.sort(key=lambda r: r[1])
    for name, total, zt, zs in rows:
        print(f"  {name:<22} sum={total:>5.2f}  (TRGB={zt:.2f}, SH0ES={zs:.2f})")


if __name__ == "__main__":
    main()
