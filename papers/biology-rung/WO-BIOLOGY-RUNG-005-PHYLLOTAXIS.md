# WO-BIOLOGY-RUNG-005-PHYLLOTAXIS: Fibonacci Phyllotaxis Angles from φ-Helical Closure Orbits

**Status:** Stub — natural addition after WO-2 (shares φ-helical orbit machinery)
**Date opened:** 2026-04-23
**Classification:** Biology-rung + botanical morphogenesis + α-structure bridge
**Priority:** Natural, not stretch — math bridge is short via WO-2's B2 orbits

---

## 1. Executive Summary

Phyllotaxis — the arrangement of leaves, florets, scales, etc.
around a plant stem or axis — shows angular spacing dominated by the
**Fibonacci / golden-section ratio**, producing the canonical
divergence angle

```
θ_phyllo ≈ 137.5077…°  =  360° · (1 − 1/φ)  =  360° · (2 − φ)
```

where φ = (1 + √5)/2. The phenomenon appears in sunflower heads,
pinecones, pineapples, Romanesco broccoli, cactus spines, vascular
branching, and many other biological contexts. In pure mathematics
it falls out of the continued-fraction expansion of φ being the
"most irrational" number, maximising the efficiency of a
self-similar lattice.

**Upstream hook.** `cascade-bio.md §B6` lists phyllotaxis as a
pending sub-phase:

> **B6.** Phyllotaxis Fibonacci angles (≈137.5°) — connect to
> α⁻¹ = 137 + π/87.

The `α⁻¹ = 137 + π/87` connection is striking: the Fibonacci
divergence angle is `360° · (2 − φ) ≈ 137.5077…°`, while the fine
structure constant inverse is `α⁻¹ ≈ 137.036…`. The two numbers
are not literally equal but are numerically close and have
structurally similar origins in φ-related continued fractions.
Settling the relationship (genuine cascade identity, a coincidence,
or a suggestive near-equality) is the analytic meat of this WO.

### Why this is a natural, not stretch, addition

- The math bridge is already in scope for WO-2 (φ-helical closure
  orbits on the 600-cell; `cascade-bio.md §B2`).
- Experimental data is abundant and free — counts of florets in
  sunflowers, spirals in pinecones, branching angles in plants —
  with no API / access issues.
- A cascade-derived divergence angle at `137.5077°` that matches
  observed phyllotaxis to within measurement precision, and a
  clean statement about whether that equals or merely approaches
  α⁻¹-structure, is itself publishable at the level of the other
  WOs.

---

## 2. Goals

### 2.1 Primary (must)

1. **Derive** the Fibonacci divergence angle `360° · (2 − φ)` from
   the WO-2 φ-helical closure-orbit machinery restricted to a
   cylindrical / axial geometry. The 600-cell hosts natural helical
   cell sequences; pick out the one whose rotation per step is the
   golden angle.
2. **State precisely** the relation between the phyllotaxis angle
   `137.5077°` and the fine-structure constant inverse
   `α⁻¹ = 137 + π/87 ≈ 137.036°` (per the alpha-chain programme):
   either
   - (a) they are equal up to a principled cascade reason, or
   - (b) they are distinct but both derive from the same upstream
     φ-continued-fraction, or
   - (c) the match is numerical only and no cascade identity holds.
   The answer must be stated with evidence, not hand-waved.
3. **Empirical test**: compare predicted phyllotaxis angles against
   published measurements from plant-biology primary sources
   (sunflower heads, pinecones, Romanesco, axillary branching).
   Because the prediction is numerically sharp
   (≈ `137.5077°` ± small cascade correction), a two-sigma
   empirical deviation would falsify.

### 2.2 Secondary (should)

4. Predict the **branching ratio** (Fibonacci number spacing along
   the spiral: 1, 1, 2, 3, 5, 8, 13, 21, 34, … parastichies) from
   the cascade orbit structure. This is a richer target than just
   the angle because different plants show different "levels" of
   Fibonacci spiraling.
5. State whether the cascade makes any distinguishing prediction
   between **di-cot vs. mono-cot** phyllotactic pattern (angle is
   the same, but arrangement primitives differ).
6. Connect to the **cascade-genetic-code** thread (the 20 amino
   acids live on icosahedral faces, 𝑐𝑓 `cascade-genetic-code.md`);
   phyllotaxis is arguably the macroscopic expression of the same
   icosahedral φ-structure.

### 2.3 Non-goals

- Full plant-morphogenesis model (hormone gradients, cellular
  dynamics, tissue mechanics). We predict the *angle*, not the
  *mechanism*.
- Animal phyllotactic analogues (e.g. horn spirals, shell spirals).
  Different math regime; out of scope.

---

## 3. Dependencies

- WO-2 φ-helical closure-orbit machinery (shared).
- `cascade-bio.md §B2` (φ-helical orbits sub-phase) and §B6
  (phyllotaxis pointer) as upstream scope.
- `cascade-derivation/cascade-alpha-chain-complete-theorem.md`
  for the `α⁻¹ = 137 + π/87` claim (already codex-verified per
  memory). The phyllotaxis angle vs. α⁻¹ question routes through
  this thread.
- `cascade-derivation/cascade-genetic-code.md` as a sister thread
  (icosahedral faces ↔ 20 amino acids, potential macro-expression
  connection).
- Public plant-biology measurement data: no API required; primary
  literature (Mathai & Davis 1974, Jean 1994, and downstream reviews).

---

## 4. Math to Derive (catalogue-style preview)

To be worked out when WO-5 opens. Anticipated new entries:

- **D** cylindrical / axial 600-cell helical closure orbit, restriction
  of the B2 machinery to a fixed-axis rotation action.
- **T / L** golden-angle theorem: the most efficient (most-irrational)
  helical packing rotation is `2π(1 − 1/φ)`, matching the observed
  Fibonacci divergence angle.
- **C** cascade statement on whether `360°·(2 − φ) = α⁻¹·(360°/137)`
  (a specific scaling identity) or whether the two numbers are
  merely numerically similar.

---

## 5. Status Log

- 2026-04-23: WO opened as stub per user request to keep phyllotaxis
  in scope alongside amyloid / tubulin / Levin.
- 2026-04-23: WO promoted to complete. Paper written at
  `papers/biology-rung-phyllotaxis/biology-rung-phyllotaxis.tex`
  leveraging upstream B6 work (`cascade-bio.md §B6.1–B6.2` +
  `scripts/phyllotaxis_alpha_check.py`). Key result: Theorem T.1
  (cascade golden-angle theorem) and Remark R.1 (integer-137
  shared between α⁻¹ and θ_phyllo via different operators, no
  clean fractional identity). Math catalogue WO-5 section
  populated. Codex review loop pending.
