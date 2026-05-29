# Engine pointer

The grammar exhibited in this paper is reproducible from the
**closure transformation engine** in a separate repository:

    My Projects/tranformation-engine/

Within that repository:

```
tranformation-engine/
  closure_transform_engine/        <- the engine itself
    core/                          (closure_validator, invariants, spectrum, ...)
    transformations/               (12 transformation kinds + grammar)
    physics/                       (admissibility, transition_rules, bridges, ...)
    examples/
    tests/
    outputs/
    reports/
  closure_ai/                      <- relational AI on the engine
  min_aria/                        <- vector-state agent on the engine
  aria_experiments/                <- ARIA-on-engine variants
  scripts/                         <- run / reproduction scripts
  reports/
  runs/
```

## Modules referenced in the paper

For each module the paper cites we give the path within
`tranformation-engine/`.

### Schläfli decomposition (Theorem 1)
- `closure_transform_engine/decomposition.py` (in
  the older vendored package), and the equivalent functions
  exposed via `closure_transform_engine/core/` and
  `closure_transform_engine/physics/bridge_24_600.py`.

### λ=12 lift theorem (Theorem 2)
- `closure_transform_engine/keystone.py`
- `closure_transform_engine/physics/lambda12_a5_channel.py`

### λ=12 uniqueness scan (§5.3, negative grammar rule)
- `closure_transform_engine/physics/universality_lambda12.py`

### Transformation taxonomy (§5.4)
- `closure_transform_engine/transformations/transformation_grammar.py`
- `closure_transform_engine/transformations/transformation_report.py`
- `closure_transform_engine/transformations/transformation_search.py`

### Admissibility classes (§5.5)
- `closure_transform_engine/physics/admissibility.py`

### Transition rules (§5.6)
- `closure_transform_engine/physics/transition_rules.py`
- `closure_transform_engine/physics/closure_layers.py`

### Physical-interpretation labels (§6)
- `closure_transform_engine/physics/physical_interpretation.py`

### Compositional reasoning (§8)
- `closure_ai/` (relational architecture, with
  `model/reasoning_loop.py` + `model/admissibility_gate.py`)
- `min_aria/min_aria_v2.py` (vector-state agent)
- `min_aria/test_min_aria_v2.py` (numerical claims of
  identity-drift ≈ 0 under hostile prompt and closure-residual →
  0 after recover)

## How to reproduce the grammar

```bash
cd .../tranformation-engine
python -m closure_transform_engine.examples.run_wo007_schlafli_decomposition
python -m closure_transform_engine.examples.run_wo008_keystone
# universality scan:
python -m closure_transform_engine.physics.universality_lambda12

# downstream systems:
python min_aria/test_min_aria_v2.py
pytest closure_ai/tests
```

Every grammar claim made in the paper should be reproducible from
these calls. If a reviewer cannot find a cited function, please
open an issue against this bundle's repository so the pointer can
be updated.

## Why the engine is a separate repo

The engine is an independent computational artefact with its own
release cycle. This translation-layer paper is a published claim
that the engine's output, when read across the whole pipeline,
constitutes a formal language. Keeping them separate is the right
boundary: the engine can evolve independently; this paper is
versioned at a snapshot.
