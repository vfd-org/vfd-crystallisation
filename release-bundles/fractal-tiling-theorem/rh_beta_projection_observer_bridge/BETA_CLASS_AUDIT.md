# Deliverable A — β-class audit

## What β=1, 2, 4 mean

Dyson's threefold way classifies Hamiltonians by their antiunitary (time-reversal)
symmetry, equivalently by the division algebra of the matrix entries:

| β | ensemble | entries | antiunitary `T` | level repulsion `p(s)~s^β` | spectral feature |
|---|---|---|---|---|---|
| 1 | GOE | real (ℝ) | `T²=+1` | `s¹` | — |
| 2 | GUE | complex (ℂ) | none | `s²` | — |
| 4 | GSE | quaternion (ℍ) | `T²=−1` | `s⁴` | Kramers doubling (every level 2×) |

Verified by our harness (`matrix_model_experiments.py`, `results/beta_baseline/`):
GOE→β=1 (repulsion s^0.90), GUE→β=2, GSE→β=4 (s^3.89). The harness separates the
three classes cleanly.

## Why zeta zeros are β=2

Montgomery's pair-correlation and Odlyzko's computations show the high zeros of
`ζ` have GUE/β=2 spacing. Our independent check (`mpmath.zetazero`, 300 zeros,
unfolded by the Riemann–von Mangoldt density) classifies them as **β=2** (best
fit, repulsion ≈ s^2.75). This is a statement about the **analytic zeros**.

## Why the VFD/icosian construction "appears β=4" — and the precise sense

The β=4 attribution is **real but symmetry-class only**, and must not be confused
with spacing. Two distinct facts:

1. **Symmetry class (β=4, true).** The icosian algebra is `B=(−1,−1/K)`, a
   quaternion (ℍ) algebra. The 120 unit icosians are **120/120 in SU(2)=Sp(1)**
   (verified, `arithmetic_projection_tests.py`); the quaternionic Hilbert space
   carries an antiunitary `J` with `J²=−1` (Kramers). This is genuinely the
   symplectic/GSE symmetry class — caused by quaternionic multiplication and the
   self-dual pairing, exactly the structures the WO asks to point to.

2. **Spacing (NOT β=4).** The actual icosian matrices are **highly structured,
   not random**: the 600-cell adjacency (120×120) has only **9 distinct
   eigenvalues** (93% of consecutive spacings are zero — huge multiplicities from
   the 2I=binary-icosahedral symmetry). It has **no GSE spacing** — it is an
   integrable/distance-regular object, not a GSE-random one. The Brandt/Hecke
   operators at our level are 2×2 (`h=2`) — far too small for any spacing
   statistic.

## Is β=4 truly present or merely inferred?

**Present, in the symmetry-class sense** (explicit: 120/120 ⊂ SU(2), `J²=−1`,
quaternion algebra). **Absent, in the spacing sense** (the matrices are
degenerate/structured, not GSE-random). Treating the symmetry-class β=4 as if it
were a spacing β=4 that must "become" the zeros' spacing β=2 is precisely the
**β-numerology** the WO forbids — and this audit flags it.

## Consequence for the bridge question

The honest comparison is therefore **not** "GSE spacing → GUE spacing" (the
substrate has no GSE spacing). It is "quaternionic symmetry class (ℍ) →
complex symmetry class (ℂ)", which is the classical **complexification**
`ℍ⊗_ℝℂ ≅ M₂(ℂ)` — analysed in `PROJECTION_CANDIDATES.md`.
