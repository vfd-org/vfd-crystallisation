# Preregistered Paper Predictions

**Frozen: 2026-04-18** — predictions below were locked before running
any validation. They are derived from discovery runs reported in
`CASCADE_FINDINGS.md` (pairwise ablations, multi-subject EEG,
conversation + chess closed-loop, HCP registration).

Each prediction has:
- a **specific numerical claim**
- a **pass threshold** (interval, inequality, or categorical match)
- a **validation test** (which run on which seeds will test it)
- a **rationale** (why the claim is non-trivial — what would break it)

**Hit rate** will be reported after validation in `VALIDATION_RESULTS.md`.

---

## Predictions 1-5: Cascade geometry

### P1. Cascade α is in the SOC range
- **Claim**: Mean α across 5 fresh-seed (30000-30004) baseline runs
  of 200 epochs each will satisfy **2.5 ≤ α ≤ 3.5**.
- **Rationale**: Beggs & Plenz 2003 put biological neuronal avalanches
  in [1.5, 3.0]. Our discovery runs gave α ≈ 2.91-3.02. A new-seed
  violation would mean the signature doesn't replicate.
- **Run**: `_run_single_seed` with all mechanisms active.

### P2. Pairwise ablation — context rotation is the dominant mechanism
- **Claim**: On 3 fresh seeds (30010-30012), main effect of
  `ablate_context_rotation` on α is **≥ +0.30**.
- **Rationale**: Discovery observation was +0.625. A small or negative
  main effect would falsify the dominant-mechanism claim.
- **Run**: Conditions `----` vs `-C--` on fresh seeds.

### P3. D×C interaction is near-zero (independence)
- **Claim**: |D×C interaction| < **0.20** on the fresh 2x2 sub-matrix
  (----/D---/-C--/DC--) at 3 seeds.
- **Rationale**: Discovery gave 0.039. A large interaction would mean
  D₄ and context rotation are not independent — reviewer-critical for
  #2+#3 separability.
- **Run**: Fresh seeds, 4 conditions, compute interaction term.

### P4. C×P synergy is positive and substantial
- **Claim**: C×P interaction **≥ +0.10** on the 2x2 (----/-C--/--P-/-CP-)
  at 3 seeds.
- **Rationale**: Discovery gave +0.229. The "partial emission is a
  redundant recovery mechanism" story depends on this being > 0.
- **Run**: Fresh seeds, 4 conditions.

### P5. Equator compensation is null (≤ small main effect)
- **Claim**: Main effect of `ablate_equator_compensation` on α has
  **|effect| < 0.15** on 3 fresh seeds.
- **Rationale**: Discovery gave −0.082. Tests the "formally removable"
  claim.
- **Run**: Fresh seeds, conditions ---- vs ---E.

---

## Predictions 6-8: EEG spindle & state analysis

### P6. Real EEG spindle α is in the SOC range
- **Claim**: On the existing 30 Sleep-EDFx subjects, pooled spindle α
  (bootstrap 1000 resamples, fresh seed 30100) falls in **[2.0, 3.0]**.
- **Rationale**: Discovery with 500-bootstrap (seed 42) gave
  2.513 [2.504, 2.526]. A different seed's bootstrap CI should
  overlap substantially.
- **Run**: `bootstrap_alpha_ci` with fresh seed on already-computed
  spindle sizes (not re-detecting spindles).

### P7. W→N3 coherence variance collapses
- **Claim**: Mean N3/W variance ratio across 24 subjects **< 0.70**.
- **Rationale**: Discovery gave 0.365. If the ratio is ≥ 0.70 it means
  coherence variance does not meaningfully collapse — corresponding
  to #4 being general reduced-state failing empirically.
- **Run**: Re-execute `run_sleep_stage_coherence.py` (deterministic).

### P8. W→N3 regime switching drops (opposite to anaesthesia)
- **Claim**: Mean N3/W switching ratio **< 0.50**.
- **Rationale**: Discovery gave 0.058. If the ratio > 0.50 (near-unity
  or rising), the dissociation story breaks — this is the empirical
  test of "#5 is anaesthesia-specific, not general reduced-state."
- **Run**: Re-execute deterministic analysis.

---

## Predictions 9-13: Closed-loop classification (chess)

### P9. Chess 5-fold CV ≥ chance + substantial margin
- **Claim**: 5-fold CV on v2 features at n=25 ticks, 5 fresh seeds
  (30200-30204), mean ≥ **70%**.
- **Rationale**: Discovery gave 81.9% ± 4.6%. Chance = 25%. A result
  < 70% would mean our 84.4% LOO number was misleadingly inflated.
- **Run**: `run_chess_pattern_readout.py` + 5-fold with fresh seeds.

### P10. Null feature→frame mapping ≥ 50% (domain-invariant floor)
- **Claim**: Mean accuracy over 20 random permutations (fresh RNG
  seed 30210) **≥ 50%**.
- **Rationale**: Discovery gave 64.2%. A floor below 50% would mean
  the architectural-invariant story is fragile.
- **Run**: `run_chess_robustness.py` (fresh seed).

### P11. Random-label baseline = chance
- **Claim**: Mean random-label accuracy **∈ [15%, 35%]** (chance ± 1σ).
- **Rationale**: Protocol-clean test. Discovery gave 26.1% ± 9.4%.
  If the baseline drifts from chance, CV is leaking.
- **Run**: `run_chess_robustness.py` (fresh seed 30211).

### P12. Diffusion-depth goldilocks peaks in [15, 60]
- **Claim**: Across depths {5, 15, 25, 40, 60, 100}, the peak accuracy
  is achieved in **{15, 25, 40, 60}** (not at 5 or 100).
- **Rationale**: Cortical integration-time analogue (Thorpe 1996).
  Peak outside the window would break the analogy.
- **Run**: `run_chess_pattern_readout.py --sweep 5,15,25,40,60,100`.

### P13. Substrate lift on chess v2 is positive
- **Claim**: At n=25, substrate ≥ raw **+ 15pp** on 5-fold CV (fresh
  seeds).
- **Rationale**: The central closed-loop claim.
- **Run**: Compare raw-features classification vs substrate-pattern
  classification.

---

## Predictions 14-16: Closed-loop (conversation) + cross-domain

### P14. Conversation raw features already discriminative
- **Claim**: Raw conversation 5-fold CV accuracy **≥ 75%** on fresh
  seeds (30220-30224).
- **Rationale**: Discovery gave 87.5% LOO. If much lower, the
  selective-amplifier story's premise fails.
- **Run**: `run_conversation_readout.py` (raw-features classification).

### P15. Substrate does NOT lift clean features much
- **Claim**: |substrate lift − raw| **< 10pp** on conversation (fresh
  seeds). Substrate adds at most 10pp or subtracts at most 10pp.
- **Rationale**: Selective-amplifier prediction. Large substrate lift
  on already-clean features would break the Thorpe/Kiani analogy.
- **Run**: 5-fold CV raw vs substrate on fresh seeds.

### P16. Architecture-invariant null mapping ≥ 50% on both domains
- **Claim**: Null feature→frame permutation mean ≥ **50%** on BOTH
  chess AND conversation, fresh RNG.
- **Rationale**: Discovery gave ~65% in both. Domain-invariant claim.
- **Run**: Null-permutation controls on both domains.

---

## Predictions 17-18: HCP structural registration

### P17. ARIA degree std = 0 exactly (theorem-level)
- **Claim**: ARIA vertex adjacency graph has mean-degree exactly 12.00,
  std exactly 0.00.
- **Rationale**: H₄ symmetry acts transitively. This is a theorem,
  not a measurement. A non-zero std would indicate a bug.
- **Run**: Deterministic recompute.

### P18. HCP ICA-50 has non-trivial degree std
- **Claim**: On 100 subjects (100 different ones if available; else
  same), group-averaged HCP graph has **degree std > 2.0** at
  density-matched threshold.
- **Rationale**: Discovery gave 3.39. Hub-spoke heterogeneity is the
  brain's signature. Below 2.0 would mean the brain is more regular
  than expected.
- **Run**: Deterministic recompute (HCP data is fixed).

---

## Meta-claims (reported but not tested)

- **M1**: We will report ALL outcomes, including broken predictions.
- **M2**: We will NOT revise predictions after seeing results.
- **M3**: If a prediction breaks, we will explicitly note it in
  the paper and retract or reframe the corresponding claim.

## Validation protocol

1. Predictions frozen at time of this file's creation (git-tracked).
2. Fresh seeds (30000+) not used in discovery runs.
3. No code changes to analysis scripts between freeze and validation.
4. Single validation run — no "best of N" cherry-picking.
5. Results recorded in `VALIDATION_RESULTS.md` with hit/miss per
   prediction + full numerics.

## Success thresholds

- **≥ 14/18 predictions pass**: paper claims are well-supported.
- **10-13/18**: paper is publishable but with honest caveats on
  broken predictions.
- **< 10/18**: substantial revision needed; multiple correspondences
  require retraction or reframing.

We do not expect 18/18 — some are noisy empirical tests and statistical
luck alone would produce an occasional miss at the α=0.05 level. A
bulletproof paper should land 14-17.
