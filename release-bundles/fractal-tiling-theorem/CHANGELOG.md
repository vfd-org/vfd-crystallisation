# Changelog

## [1.4.0-rc1] — 2026-05-31

Bundle repositioned around the verified result and the conceptual companion.

### Papers
- **`void-and-structure.tex`** added (8 pp): what the zeros are (a generative
  absence), how the primes are reconstructed from them (explicit formula), and
  a diagnosis of why the problem resists construction; codex-reviewed, every
  rung stated at its proven strength.
- **`rh-frontier-capstone.tex`** extended to 9 pp: folded in the
  multiplicativity tiling theorem and the three-tilings observation (why the
  Hecke structure is the one that reaches the L-function).
- The original conditional **`fractal-tiling-theorem.tex`** retired to
  `paper/_archive/`; its unconditional content now lives in the capstone.

### Sim
- **`route_b/deterministic_probability.py`**: deterministic Riemann zeros vs a
  random GUE matrix, both on the GUE law (⟨r⟩ = 0.617 vs 0.593) — deterministic
  pseudorandomness made explicit.

### Framing
- README rewritten findings-first: verified circle test as the credential, the
  void companion as the destination.

## [1.0.0-rc1] — 2026-05-30

Initial public release.

### Paper

**Title:** *The Fractal Tiling Theorem: Reducing RH to a Finite Hecke
Verification via Substrate Multiplicativity.*

**Main contribution:** isolates the three independent symmetry structures
on the V_600 substrate (W(H_4) geometric, cascade scale, Hecke
multiplicative) and proves only Hecke tiling has a finite generating set
and reaches the L-function's analytical content via the Weil explicit
formula.

**Main result (Theorem 5.1, Fractal Tiling Theorem):** **conditional**.
If V_min supports finite-prime Hecke operators on the 26-dim block
satisfying (A1)–(A7), then RH for L_sub follows by tiling.

**Unconditional supporting results:**
- Theorem 3.2 (Multiplicativity tiling)
- Lemma 4.1 (Explicit formula bridge)
- Corollary 4.2 (Zeros from finite tiling)

### Sim

- `sim_multiplicativity_tiling.py` — demonstrates the fractal tiling on
  15 prime generators tiled to 1000 coefficients; verifies Ramanujan
  bound, Sato-Tate distribution, and explicit-formula truncation
  convergence.

### Outputs

4 plots:
1. Dirichlet coefficient magnitudes (red = generators, blue = tiled)
2. Ramanujan bound check on prime generators
3. Explicit-formula truncation error vs. P_0 (the cutoff)
4. Sato-Tate semicircle distribution fit

### Scope discipline

- Pre-peer-review preprint footer enforced
- No unconditional RH proof claimed
- Theorem 5.1 is explicitly conditional
- (O1)–(O4) open items listed precisely
- Engine verdict at proxy level (5-of-7) stated as proxy, not genuine

## [1.1.0-rc1] — 2026-05-30

Circle test executed; honest audit + genuine-target computation + Route B
scaffold added.

### Corrections
- Paper level fixed: (2)·(φ−2) was wrong (φ−2 is a unit → collapses to (2),
  inert, no cusp form). Real level is the norm-31 prime 𝔭₃₁ (Dembélé's
  icosian HMF). Dembélé reference added.
- Added honesty caveat box to paper §6.4: proxy "passes" are tautological
  (hardcoded) / fitted, not genuine substrate Hecke data.

### Provenance audit (`CIRCLE_TEST.md`)
- (O2) does not currently hold: 26-dim A₁ block + C_φ are genuine geometry,
  but the prime→eigenvalue map is hardcoded (`hecke_lift` ignores the
  substrate) or LS-fitted to the Riemann zeros; spectral match is broken.

### Route A (`sims/sim_genuine_eigenvalues.py`, new)
- Genuine norm-31 newform eigenvalues over Q(√5) computed independently by
  point-counting curve 31.1-a1. 44 eigenvalues, N(P) ≤ 200.
- Verified two ways: Ramanujan PASS + torsion 8|#E(F_P) PASS.
- Dimension settled: 1 isogeny class at norm 31 → cuspidal space 1-dim.
- Target saved to `data/genuine_newform_eigenvalues.csv`.

### Route B scaffold (`route_b/`, new)
- `icosian.py`: exact icosian arithmetic; 120 units, all nrd=1, 14400/14400
  closure → 2I. VERIFIED.
- `brandt_level31.py`: Eichler-order + ideal-class + Brandt-matrix scaffold
  with circle-test harness done; acceptance gates G1–G4.
- `ROUTE_B_PLAN.md`: full algorithm and status.

## [1.2.0-rc1] — 2026-05-30

RH frontier completed and consolidated into a capstone paper.

### Verified — the circle closes
- `route_b/short_vectors.py`: rank-8 enumerator, gate r(2)=120; reduced-norm
  theta r_I(ν)=120·(N(ν)+1) (level-1 Eisenstein = ζ_K·ζ_K(·−1)).
- `route_b/step2_eichler.py`: 2I → A₅ ⊂ PGL₂(F₃₁), orbits [12,20], dim 2.
- `route_b/step3_4_hecke.py`: substrate Hecke eigenvalues == genuine newform
  on 11 prime ideals (norm ≤ 41), out-of-sample, no fitting. (O2) confirmed.

### Corrected
- `route_b/admissibility.py`: multiplicativity verified on the eigenform;
  established that admissibility + explicit formula do NOT give RH. Paper
  Theorem 5.1 conclusion (3) "satisfies RH" withdrawn (in fractal-tiling-theorem.tex).

### Frontier
- `route_b/satake_circle.py`: local critical line on the tiling (Satake circle).
- `route_b/positivity_analysis.py`: C_φ spectrum; positivity-category argument.
- `route_b/weil_positivity.py`: Connes/Weil functional, gated on ζ (0.01%),
  W(h) > 0 for our L-function — evidence consistent with RH.

### Capstone
- `paper/rh-frontier-capstone.tex` (6 pp, compiles, 0 undefined refs):
  status-tagged synthesis of the whole arc.
- `RH_FRONTIER.md`: navigation index (capstone + supporting docs + code).
- Supporting docs: `CIRCLE_TEST.md`, `SCOPE.md`, `GEOMETRIC_CRITICAL_LINE.md`,
  `THE_ADJOINT.md`, `POSITIVITY_AND_RH.md`, `CONNES_POSITIVITY.md`.

### Discipline
- No observer/consciousness/"self" in any definition; "selves-as-primes"
  reading explicitly marked outside the mathematics throughout.

## [1.3.0-rc1] — 2026-05-30

Frontier work consolidated; capstone paper extended (6 → 8 pp).

### New frontier results (all in `route_b/`, indexed in `RH_FRONTIER.md`)
- **Quantum chaos** (`quantum_chaos_test.py`, `QUANTUM_CHAOS.md`): zero
  spacings = GUE (level repulsion, 13× over Poisson) = the law measured in
  nuclei / microwave billiards. Geometry (A₁, 93% degenerate) vs arithmetic
  (GUE) — chaos lives in the arithmetic.
- **Quasicrystal** (`diffraction_quasicrystal.py`, `QUASICRYSTAL.md`): zeros
  diffract into primes, 11/11 Bragg peaks at log(pᵏ).
- **Mirror** (`mirror_layers.py`, `MIRROR.md`): prime↔zero mirror is
  frequency-layered; off-line tuning → x^(1/2+β), RH = balance condition.
- **Division algebra** (`DIVISION_ALGEBRA.md`): GUE const 0.6027 = ℂ (β=2,
  Dyson threefold way); substrate ℍ(β=4) vs zeros ℂ(β=2) class mismatch.
- **Jacquet–Langlands trace** (`jacquet_langlands_trace.py`,
  `JACQUET_LANGLANDS.md`): ℍ→ℂ = complexification (ℍ⊗ℂ=M₂(ℂ), nrd=det,
  2I⊂SU(2)), verified to 2e-16. Locates operator on GL₂/unitary side.
- **Katz–Sarnak** (`katz_sarnak.py`, `KATZ_SARNAK.md`): bulk Unitary/GUE +
  family Orthogonal O+; full ℝℂℍ trichotomy in 3 roles.
- **Adelic scaling** (`adelic_scaling.py`, `ADELIC_SCALING.md`): finite-place
  Hecke scaling algebra commutes, ℂ-class (verified); archimedean
  self-adjoint realisation = open (Tier-3).
- **Scale capstone** (`SCALE_AND_SYMMETRY.md`, `THE_ADJOINT.md` §7): RH as a
  question of scale; four operator-construction routes, one wall.

### Capstone paper
- `paper/rh-frontier-capstone.tex` extended to 8 pp: added §8 quantum chaos,
  §9 division-algebra structure, §10 locating the operator; updated abstract,
  status ledger, conclusion, and references (Montgomery, Rudnick–Sarnak,
  Atas et al., Dyson, Katz–Sarnak, Iwaniec–Luo–Sarnak). Compiles, 0 undefined.

### Net
The missing operator is now fully specified: class ℂ/unitary/β=2,
finite-place part = verified commutative Hecke scaling algebra, single open
step = archimedean self-adjoint realisation (= Weil positivity all-h = RH).

