# OD-1 Status — Cycle eigenvalue spectrum

**Date:** 2026-05-05
**Verdict:** **NOT CLOSED.** The 1/12 fit to H₀ data is phenomenologically robust,
but a clean mode-counting derivation on V_600 gives 5/12, not 1/12.

## What was tried

`od1_cycle_spectrum.py` builds an explicit V_600 stand-in (12 cycles × 10
vertices) with σ-Galois decomposition into bulk (2 σ-fixed cycles) and
boundary (10 σ-paired cycles in 5 pairs). Modes:

- 12 σ-symmetric cycle-mean modes (one per cycle, L²-norm 1).
- 5 σ-antisymmetric cycle-pair modes (one per σ-pair, L²-norm 1 over 2L vertices).

Total 17 orthonormal cycle-mean modes.

## What the orthonormal sim says

Setting all mode eigenvalues equal (h_per_mode = h_0):

| cycle class | per-vertex diagonal | per-cycle eigenvalue |
|---|---:|---:|
| σ-fixed   | h₀/L                  | h₀/L              |
| σ-paired  | h₀/L + h₀/(2L) = 3h₀/(2L) | 3h₀/(2L)         |
| ratio (paired/fixed) | — | **3/2** |

So **mode-counting predicts σ-paired cycles have rate 3/2 of σ-fixed**,
not 11/10 as required by the 1/12 derivation.

H_late / H_early under orthonormal mode-counting:
```
H_late = (1/12) [2·(h₀/L) + 10·(3h₀/(2L))] = 17h₀/(12L)
H_early = h₀/L  (bulk only)
ratio = 17/12 ≈ 1.417  →  predicted H_local = 67.36 · 1.417 = 95.43 km/s/Mpc
```
That is **22 km/s/Mpc above SH0ES**. Wrong.

## What the data wants

Empirical 13/12 fit requires σ-paired cycles to have eigenvalue h₀(1+1/L) =
11h₀/10, **not** 3h₀/(2L) ≈ 0.15·h₀. The data-required boundary diagonal
is h₀ + h₀/L per vertex (not 3h₀/(2L)).

## Three honest possibilities

**Possibility A — The data fit is a coincidence.**
1/12 is what you'd expect by chance among ~178 natural rationals with
~0.6% probability (`look_elsewhere.py`). Plausible but unlikely given
the σ₈ cross-check also lands at 1/12.

**Possibility B — The closure operator is not the simple mode-eigenvalue
form.**
The closure operator may have non-trivial eigenvalues per mode, structured
to give h₀(1+1/L) per σ-paired cycle. This would require:
- σ-symmetric modes with eigenvalue h₀ × L (so per-vertex contribution L·(1/L) = 1)
- σ-antisymmetric modes with eigenvalue h₀ × 2L/L = 2h₀ (so per-vertex 1/(2L)·2h₀ = h₀/L)

Then σ-fixed cycle: h₀ per vertex → cycle eigenvalue h₀.
σ-paired cycle: h₀ + h₀/L per vertex → cycle eigenvalue h₀(1+1/L).

This reproduces 13/12 — but the eigenvalue assignment (h₀·L for sym,
h₀·2L for antisym) is not motivated; it's reverse-engineered to match.

**Possibility C — The relevant mode count is different.**
Maybe the closure operator has different effective mode count than the
cycle-mean Fourier basis. For instance, only the k=0 cycle-mean σ-sym
modes might be "live," with σ-antisym contributing only 1 unit total
(not 5). Then total live modes = 12 sym + 1 antisym = 13, distributed
across 120 vertices, giving 13/120 per vertex average and ratio 13/12
when normalised by bulk-only baseline.

Why only 1 σ-antisym mode total? No structural reason within V_600 alone.

## What this means for the framework

The **empirical 1/12 prediction** is robust:
- 0.06σ vs SH0ES H₀
- 0.14σ vs KiDS S₈
- Wrong-sign sanity at 5σ
- Look-elsewhere 0.56% (pool 178)

The **derivation** is incomplete:
- 12, 10, 10 are correct V_600 structural numbers.
- Mode-counting alone does not select 13/12.
- An unidentified additional structure (eigenvalue assignment or
  coarse-graining rule) is needed.

## What to do

1. **Do not claim a derivation in any write-up.** The 1/12 effect is a
   phenomenological observation that *aligns* with V_600 numbers, not a
   theorem.

2. **Pre-registered tests still valid.** k-ladder predictions for
   SPHEREx/LSST/SKA stand. If they survive, the framework grows; if
   they fail, the V_600 connection was coincidence.

3. **Open derivation as named gap.** Add OD-1' to the open-items list
   with explicit statement: "find the closure-operator definition that
   produces cycle eigenvalues (h₀, h₀(1+1/L)) from V_600 structure."

4. **Possibility C is the most interesting.** If only the σ-symmetric
   sector is "live" plus exactly one σ-antisymmetric "global" mode, this
   would reduce to a 13-mode system (12 cycles + 1 global). This connects
   to the soul-prime singleton structure (`docs/soul-prime-as-pi0.md`):
   maybe the soul prime IS the single global σ-antisymmetric mode.

## Files

- `od1_cycle_spectrum.py` — numerical sim (gives 17/12)
- `derivation.md` — original derivation (claimed 13/12 but argument is loose)
- this file — honest status report
