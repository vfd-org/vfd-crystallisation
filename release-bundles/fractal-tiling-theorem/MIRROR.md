# What the mirror looks like — two mirrors, and the frequency layers
### 2026-05-30 · `route_b/mirror_layers.py`

Modelling the prime↔zero "mirror" and asking: is it layered as frequency
components? Answer: **yes, exactly** — and it is *frequency-graded*, not a
flat reflection.

## Two distinct mirrors (don't conflate them)
1. **Functional-equation mirror** — Λ(s)=Λ(1−s): a *literal* reflection
   about the critical line, relating a zero to its mirror zero. Direct and
   exact. Gives the symmetry *axis*; RH is whether the zeros sit *on* it.
2. **Prime↔zero mirror** — the explicit formula: a Fourier-type *duality*
   (mutually determining), but a *scrambling transform* (multiplicative
   primes ↔ additive zeros), **not** a flat reflection.

## The mirror is layered as frequency components (shown)
The explicit formula reconstructs the prime staircase ψ(x) as a sum of
waves, **one per zero**, of frequency γ:
$$ \psi(x)=x-\!\sum_{\gamma>0}\!\frac{2\sqrt{x}\,[\tfrac12\cos(\gamma\ln x)+\gamma\sin(\gamma\ln x)]}{\tfrac14+\gamma^2}-\log 2\pi-\tfrac12\log(1-x^{-2}). $$
Reconstructing from the first N Riemann zeros, RMS error vs the true ψ(x):

| layers (zeros) | 1 | 5 | 10 | 20 | 40 |
|---|---|---|---|---|---|
| RMS error | 0.756 | 0.564 | 0.519 | 0.423 | 0.324 |

More zero-frequencies → sharper prime steps. **The zeros are the harmonics;
the primes are the tune** ("music of the primes"). Plot:
`outputs/40_mirror_layers.png`.

## Tuning a zero off the line — what the mirror does when distorted
A zero at Re = 1/2 + β contributes amplitude ~ x^{1/2+β} instead of √x.
Moving the first zero off the line:

| β (off-line) | 0.0 | 0.2 | 0.4 |
|---|---|---|---|
| reconstruction RMS error | 0.324 | 0.450 | 0.943 |

So the mirror is **frequency-graded by Re(ρ)**: on the line, every layer has
the same depth √x — the mirror is *balanced*, all harmonics at one scale.
Off-line zeros are "louder" layers (x^{1/2+β}) that unbalance it. **RH is
exactly the balance condition**: all layers at the same √x amplitude. Plot:
`outputs/41_mirror_offline.png`.

## Honest status
This is the explicit formula (a theorem) made visual. It shows the mirror's
layered, frequency-graded structure and shows *why* RH is the balance
condition (minimal prime fluctuation). It does **not** prove RH: the
reconstruction (A) uses the actual zeros wherever they are; the off-line
demo (B) shows the *consequence* of an off-line zero, not that none exist.
Kind-1 texture — structure revealed, not proved.

**"Layers of reality" note:** the layers here are precise mathematical
frequency components (one per zero). Reading them as strata of reality is
interpretation, outside this mathematics; the math asserts only the
frequency decomposition. Per programme discipline, that reading is not
load-bearing and is not implied.
