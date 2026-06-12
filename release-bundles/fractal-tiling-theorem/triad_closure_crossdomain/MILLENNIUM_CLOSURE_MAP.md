# Triad-Closure Framework vs the Millennium Problems — honest fit map

**WO-VFD-TRIAD-CLOSURE-CROSSDOMAIN-001 (Millennium extension).**
This maps the closure-test object `(X, T, τ, θ, B, ∂X, Q)` onto each Clay
Millennium problem and grades the fit **at true strength**. It proves nothing.
The single question the framework asks everywhere is:

> Does repeated application of `T` produce closure (a positive invariant form / a
> capacity `Q ≥ 0`), a critical boundary (`Q = 0`), or forbidden escape (`Q < 0`)?

Two distinct **closure modes** (this is the corrected lesson from the simplex leg —
"self-adjoint" alone is *not* the universal test):

| mode | invariant | spectrum | closure meaning | example |
|------|-----------|----------|-----------------|---------|
| **isometry** | `TᵀBT = B` | unit circle | the phase *returns* | triad 3-cycle, rotation, unitary flow |
| **symmetric** | `BT = TᵀB` | real line | monotone / contractive | Collatz odd-map, Weil quadratic form |

The shared invariant is **"T preserves a positive form B"** (B-normality);
self-adjointness is the real-spectrum special case.

---

## The grades

| Problem | Closure mode | `Q` (capacity) | Fit | What the framework does / does NOT do |
|---|---|---|---|---|
| **Navier–Stokes** | symmetric (dissipative) | dissipation − nonlinear transfer | **STRONG analogy** | The cleanest fit. Blow-up ⟺ escape (`Q<0`); regularity ⟺ closure (`Q>0`). Our dyadic-shell probe reproduces the ν-trichotomy with the *same* `Q` as Collatz. **Does NOT prove NS**: real 3-D obstruction = controlled energy is *supercritical*, so `Q`'s sign is undetermined = the framework's CRITICAL-BOUNDARY verdict. |
| **Yang–Mills mass gap** | symmetric + gap | spectral gap Δ above vacuum | **MEDIUM–STRONG (as language)** | Osterwalder–Schrader **reflection positivity** *is literally* "a positive invariant form" — the framework's central object. Mass gap = strict `Q>0` (gap, not just `≥0`). **Does NOT construct** the measure or the gap; that is the open problem. |
| **Riemann Hypothesis** | symmetric (positivity) | Weil quadratic form | **MEDIUM (re-expression)** | RH ⟺ Weil positivity `Q ≥ 0`. Our FE-residual leg captures the `s↔1−s` reflection symmetry (closure of the completed trace); the genuine wall is infinite-dimensional positivity (Connes arithmetic site) — the same wall documented in the Triskelion note. **No new RH content.** |
| **Birch–Swinnerton-Dyer** | symmetric (FE) + rank | order of vanishing of `L` at `s=1` | **WEAK–MEDIUM** | Shares the functional-equation closure leg with RH (same `s↔` reflection). But rank-vs-analytic-rank is *not* a capacity drift; the framework adds only the FE-symmetry observation. Do not overclaim. |
| **Poincaré (SOLVED)** | symmetric (monotone) | Perelman W-entropy / reduced volume | **STRONG retrospective** | **Validation that the shape is decisive when it applies.** Ricci flow with surgery *is* a closure-drift proof: a **monotone capacity functional** (W-entropy) + no-local-collapsing forces the manifold to close to round spheres. The framework's exact shape, realised in the one solved case. |
| **P vs NP** | — | — | **POOR — do not force** | No natural `T`/positive-form/capacity. Framing computation as "does the search braid close" adds no leverage. Honest negative. |
| **Hodge Conjecture** | — | — | **POOR — do not force** | Algebraic-cycle span of Hodge classes is not a dynamical or positivity drift. No fit. Honest negative. |

---

## The honest synthesis

1. **The framework is a genuine organizing language, not a method.** It cleanly
   *unifies the dynamical/dissipative and positivity problems* (NS, Yang–Mills,
   RH, and — retrospectively — Poincaré) under one shape: *stability = a positive
   invariant form / a non-negative capacity*. It correctly *refuses* the
   combinatorial/algebraic problems (P vs NP, Hodge). That selectivity is itself a
   good sign it is tracking something real rather than being a universal solvent.

2. **Fitting the shape is not solving the problem.** In *every* open case the
   precise obstruction survives intact and is exactly the framework's
   CRITICAL-BOUNDARY verdict:
   - NS: the a-priori-controlled norm is supercritical → sign of `Q` undetermined.
   - Yang–Mills: reflection positivity must be *constructed* in the continuum limit.
   - RH: positivity must hold on an infinite-dimensional adelic space (Connes site).
   These are not relabellings the engine can break — they are the theorems.

3. **The one solved case (Poincaré) shows the shape can be decisive** — but only
   when someone supplies the *specific monotone functional* (Perelman's W-entropy)
   and proves its monotonicity. The framework points at "find the monotone
   capacity"; it does not hand you one.

4. **The corrected hypothesis.** "Self-adjointness is the universal closure test"
   is *too narrow*: rotations/triad-cycles close by **isometry** (unit-circle
   spectrum), not self-adjointness. The right universal statement is *"closure =
   existence of a positive invariant form."* This is the single most useful
   technical output of this WO.

**This document is a map, not a result. It does not prove, partially prove, or
reduce any Millennium problem. It identifies which problems share a structural
shape with VFD closure and — crucially — where each one's real wall stands.**
