# VFD Explorer

**One command reproduces every numerical claim in the Vibrational Field Dynamics
framework.**

```bash
pip install vfd-crystallisation
vfd verify
```

This site is the public, CI-generated credibility surface of the VFD
framework. Every page here is built from the same Python library that
any reader can install, run, audit, and fork. Nothing is curated by
hand: the table on the [credibility report](report.md) is re-derived
by GitHub Actions on every commit.

## What VFD claims

VFD proposes that the particle spectrum, gauge couplings, and charge
radii emerge from a single geometric object — the **600-cell** in 4D
and its embedding in **E₈** — through a deterministic closure rule.
No continuous free parameters are fitted.

If this is correct, then every measured quantity in hadron and atomic
physics should be a function of (a) the 600-cell Laplacian spectrum,
(b) a canonical shell assignment, and (c) a handful of integer
invariants. That is a falsifiable claim, and `vfd verify` is the
falsification harness.

## Headline results

The framework currently registers **20 numerical predictions** with
experimental or structural comparisons. All are re-derived on every
commit.

A summary:

- **Proton charge radius** $r_p = 4 \cdot \bar\lambda_p$ — matches
  PDG within 0.04 %, factor 4 triply determined.
- **Proton magnetic radius** $r_M = r_E$ — framework predicts
  equality; within 2 σ of PDG.
- **Fine-structure constant** $\alpha^{-1} = 137 + \pi / 87$ —
  matches CODATA to 0.81 ppm, where 87 is triply derived from
  H₄/E₈ Coxeter structure.
- **Hadron charge radii** (pion, kaon, neutron⟨r²⟩, deuteron) — all
  derived from shell support + path-graph Laplacian spectrum.
- **Mass ratios**: $m_p/m_e = \varphi^{1265/81}$ (0.02 %) from
  Paper IV shell-invariants; $m_\mu/m_e, m_\tau/m_e$ from the
  lepton-generations winding formula (weaker, 0.5 %–3.7 %).
- **Proton form factor $G_E(Q^2)$** 120-vertex resolvent sampled at
  Q² = 0, 0.05, 0.1 GeV², plus large-Q² asymptote, plus a
  self-consistency check that the slope at Q²=0 reproduces
  $4 \bar\lambda_p$.
- **Generation count = 3** from the Z₃ Hopf-fiber action.
- **Structural identities** (084473 activation code, integer-mode
  count 94, Σ upper Coxeter exponents = 88) verified byte-exactly.

See the [credibility report](report.md) for the full table with
σ-margins, and [coverage gaps](gaps.md) for the equally-honest list
of what's **not** yet derived (quark masses, W/Z/H, electric charge
integers, magnetic moments, neutrinos, CKM / PMNS, decay rates,
gravity numerics).

## Why a separate Explorer?

Before this library, every paper in the VFD corpus had its own
one-off verification script. A reader who wanted to check a claim
had to find the right script, install the right dependencies, and
run it. Reproducibility was possible but inconvenient.

The Explorer turns reproducibility into a single command and every
claim into a YAML registry entry mapped to a Python function. Change
a primitive — a shell assignment, an eigenvalue, a coupling — and
the consistency check surfaces every downstream prediction that
moves. Hand-wave arguments have no place in the registry.

## Open source, MIT licensed

The framework and the Explorer are [MIT-licensed](https://github.com/VFD-org/vfd-crystalisation-paper/blob/main/LICENSE).
Fork it. Challenge it. Replace a shell assignment and see what breaks.
Every commit on `main` rebuilds this site from the source of truth.

## Get started

- [Credibility report](report.md) — the table of every prediction vs
  experiment, regenerated on every commit.
- [Figures](figures.md) — spectrum, VFD-vs-experiment scatter,
  per-prediction error bars, proton form factor curves.
- [Coverage gaps](gaps.md) — honest list of what the framework has
  **not** yet derived as a runnable prediction.
- [How it works](architecture.md) — the architecture of the library.
- [Reproduce locally](reproduce.md) — installation and smoke-test
  instructions.
- [Papers](papers.md) — index of the underlying VFD papers.
