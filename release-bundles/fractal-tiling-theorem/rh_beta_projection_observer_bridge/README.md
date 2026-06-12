# RH β-Projection / Observer Bridge

**WO-RH-BETA-PROJECTION-OBSERVER-BRIDGE-001** — can the β=4 quaternionic/symplectic
icosian substrate canonically project to the β=2 GUE class of the zeta zeros,
without fitting zeros and without assuming RH?

## Result

```
GRADE 2 — candidate projection object (= classical complexification),
          reduces to Weil positivity for RH.   NO_RH_PROOF_CLAIMED.
```

Three honest findings (all backed by computation, not assertion):

1. **The β=4 of the substrate is a *symmetry class*, not a *spacing* class.** The
   600-cell adjacency (120×120) has only **9 distinct eigenvalues** — structured,
   not GSE-random. The β=4 is genuine quaternionic symmetry (120/120 units in
   SU(2), antiunitary `J²=−1`, Kramers). Conflating the two senses of β=4 is the
   "β-numerology" trap, and we flag it.
2. **The canonical β=4→β=2 projection is complexification** `ℍ⊗_ℝℂ ≅ M₂(ℂ)`,
   `2I ⊂ SU(2) ⊂ SL₂(ℂ)` — non-circular, preserves self-adjointness/positivity/
   trace — **but it is representation-level and zero-blind.** No projection turns
   GSE *spacing* into GUE *spacing* non-circularly (distinct universality classes).
3. **The RH-relevant content reduces to Weil positivity.** The zeros' β=2 is an
   analytic-zero fact reached only through the explicit formula / Weil pairing —
   the known wall.

So the β=4/β=2 "mismatch" is **not fatal** (it complexifies for free) and **not a
new bridge** (the spacing transition is a category error); it sharpens the
obstruction and localises the missing step in the archimedean/adelic completion.

## Layout

```
matrix_model_experiments.py     Phase 1: GOE/GUE/GSE harness + zeta zeros (validation)
arithmetic_projection_tests.py  Phases 2-4: icosian beta-audit + projection tests
BETA_CLASS_AUDIT.md             Deliverable A
PROJECTION_CANDIDATES.md        Deliverable B (6 candidates)
MATRIX_MODEL_RESULTS.md         Deliverable C
ARITHMETIC_PROJECTION_RESULTS.md Deliverable D
OBSERVER_COMPATIBILITY_FORMALISM.md Deliverable E
WEIL_POSITIVITY_RELATION.md     Deliverable F
CLAIM_BOUNDARY.md               Deliverable G
FINAL_CLASSIFICATION.md         Phase 5 grade
results/                        beta_baseline / vfd_brandt_beta_audit / projection_candidates / tables / plots
```

## Run

```bash
python3 matrix_model_experiments.py     # ~minutes (GSE eigensolves + 300 zeta zeros)
python3 arithmetic_projection_tests.py  # needs sibling icosian_brandt_cuspidal_geometry
```

Pure Python (`numpy`, `mpmath`). Zeta zeros are used **only** for validation,
never in any projection's definition.

## Boundary

Does not prove RH; does not simplify RH. Establishes that the β-mismatch is an
RH-free complexification plus the Weil wall, with the zero-reaching step being
exactly Weil positivity. See `FINAL_CLASSIFICATION.md`.
