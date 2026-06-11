# Task: WO for RH cascade-native reframing + Prime Detector equivalence sim

## Goal

Reframe `papers/millennium-rh-formal/rh-formal.tex` (and supporting
documents) under the new strategic template:

  (A) Cascade-native theorem (sim-verified, no ζ needed)
  (B) Equivalence proof to classical RH (Prime Detector L canonicity)
  (C) Architectural why (F1 + σ-equivariance + crystallisation rigidity)

The cascade-native RH theorem to be proved:

> Classical primes lie on the σ-fixed locus 2T ⊂ 2I (= 24 isolated
> points, sim-verified) under the Prime Detector L-map. The Mellin
> shadow of 2T is the critical line Re(s) = 1/2. Therefore the
> classical Riemann zeros (= Mellin transform of prime distribution)
> must lie on the critical line.

The bridging equivalence requires Prime Detector L-map canonicity:
the empirical 12-dim φ-shell signature of any prime p must align
with one of the 24 σ-fixed positions on 2I (or its multi-scale
extension to the cascade hierarchy).

## What we need codex to produce

### Section A — sim plan
Test for the equivalence claim on the first 100 primes:
1. Take primes p ∈ {2, 3, 5, 7, ..., 541} (first 100 primes).
2. For each prime, compute the cascade Prime Detector shell
   signature (the 12-dim φ-shell vector) using `vfd_prime_detector.js`
   or its cascade-paper counterpart.
3. Project each signature onto V(600-cell)/H₄ via the canonical
   icosian embedding.
4. Identify the closest 2I vertex to each prime's projection.
5. Check: how many of the 100 primes land on σ-fixed (2T) positions?
6. If statistical concentration on 2T is observed (binomial test
   against 24/120 = 20% baseline expected for random distribution),
   the equivalence claim is empirically supported.

### Section B — paper restructuring plan
Reframe rh-formal.tex (or split into a new
`papers/cascade-rh-native/cascade-rh-native.tex`) under:
- Theorem 1: σ-fixed locus on 2I = 2T (sim-verified, exists)
- Theorem 2: F is σ-equivariant (Theorem F5, exists)
- Theorem 3: Crystallisation operator selects σ-fixed critical
  points (cascade rigidity argument; needs articulation)
- Theorem 4: Prime Detector L canonically maps primes to 2T
  positions (the equivalence claim; sim-testable)
- Theorem 5: Mellin shadow of 2T = critical line Re(s) = 1/2
  (computational)
- Corollary: Classical RH follows from Theorems 1-5.

### Section C — architectural why
Articulate the cascade-native explanation that mainstream lacks:
- F1 → Z[φ] → σ → 2I is forced
- σ-equivariance + closure-functional rigidity → critical points
  are σ-fixed
- Crystallisation operator selects σ-fixed states
- Therefore primes (= F-irreducible closure points) lie on σ-fixed
  locus by architecture, not by accident

### Section D — bridge gap explicit
The single open piece: Theorem 4 (Prime Detector canonicity).
Describe what would have to be proven and how the sim test
either confirms or refutes empirically.

## Context files

- `docs/rh-cascade-closure-dynamics.md` — existing consolidation
- `papers/millennium-rh-formal/rh-formal.tex` — current paper to be restructured
- `papers/cascade-derivation/scripts/test_h4o_sigma_fixed_locus.py` — 2T sim
- `papers/paper-xxii/scripts/run_icosian_exact.py` — exact 2I machinery
- `insight.md` — Prime Detector + god-prime context (auto-included)
- aria-chess `vfd_prime_detector.js` — prime detector implementation reference

## Constraints

- **NO RETREAT.** This is the final reframing; either the equivalence
  lands (RH solved by proxy) or we honestly report cascade-RH as a
  separate theorem.
- **Sim-verifiable.** Every claim must be either sim-verified or
  classical-cited.
- **Architectural why required.** Not just "we have this", but "this
  is FORCED by F1 + cascade rigidity."
- **Use existing pair-programming infrastructure.** Codex generates
  the WO, Claude implements the sim, codex reviews.

## Required output (Sections A-F per codex_derive template)

A: Insight relevance (specific lines)
B: Named builds (B-RH-1 through B-RH-N) for the sim, paper restructuring, architectural argument
C: Revert strings if any rh-formal.tex passages need correction
D: Route alternatives (e.g., new file vs. restructure existing)
E: Exact verification targets
F: Top 3 builds to start with
