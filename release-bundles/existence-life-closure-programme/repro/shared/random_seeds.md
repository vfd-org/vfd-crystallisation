# Random seeds

All deterministic synthetic / structural demos in this repository use
**seed 42** unless explicitly stated otherwise. The discipline is:

- `numpy.random.default_rng(42)` for NumPy random sequences.
- `random.seed(42)` for stdlib random calls.
- For substrates with multiple stochastic stages, only the top-level RNG
  is seeded at 42; downstream RNGs are derived from it deterministically.
- For matplotlib figure generation, seeds do not matter beyond the data
  preparation step.

## Where seed 42 is used

- `papers/I-existence-as-closure/repro/closure_demo.py` (D1–D8).
- `papers/I-existence-as-closure/repro/rung_tower_demo.py` (C1).
- `papers/II-life-as-closure/repro/life_demo.py` (L1–L13).
- `papers/III-processing-to-point-of-view/repro/bridges_demo.py` (B1–B3).
- `notes/Note-A-bioelectric-closure/repro/synthetic_demo.py` (synthetic regeneration).
- `notes/Note-C-closure-as-distance/repro/strict_vs_passleaning_audit.py` (deterministic classification).
- All Solution Lab synthetic generators.

## Where seed 42 is not used

- Real-data analyses (OpenNeuro EEG cohorts): the data is the data; no
  random seed applies. The deterministic-pipeline guarantee is at the
  feature-computation stage.
- BETSE simulations: BETSE has its own deterministic configuration; we
  follow upstream conventions.
- LOSO/leave-one-out folds: the fold-iterator is deterministic by construction.

## Verification

Run `python repro/shared/run_all_smoke_tests.py`. If any demo's output
fails to match the deterministic expectation, the smoke test fails with
exit code 1 and prints diagnostics.

The expected SHA-256 hashes for committed deterministic outputs are in
`repro/shared/expected_hashes.json`.
