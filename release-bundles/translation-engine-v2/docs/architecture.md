# Architecture: Translation Engine v2

## Design principles

1. **Typed transformations.** Each transformation kind has a typed
   input, typed output, and an explicit admissibility verdict. Adding
   a new kind is a new function with the right signature; it slots
   into the search engine without redesign.

2. **Decidable admissibility.** Every transformation outcome has a
   verdict from a finite enumeration ({EXACT, STRONG, CANDIDATE,
   WEAK, BROKEN, DEGENERATE} plus the analytic classes). No ambiguity.

3. **Compositional grammar.** Outcomes can be inputs to subsequent
   transformations. Compositions are sequences of typed steps.

4. **Search-driven discovery.** The composition-search engine
   enumerates compositions up to a depth limit and scores each
   candidate. Adding new kinds expands the search space automatically.

5. **Honest scope.** Prototype implementations are explicitly labelled.
   The architecture's promise is "you can wire in real mathematics
   here without changing the framework"; the framework itself is the
   contribution.

## Layer structure

```
┌────────────────────────────────────────────────────────────────┐
│ User code: examples/run_v600_search.py                         │
└───────────────────────────┬────────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────────────┐
│ search.py: composition enumeration + candidate ranking         │
└──────┬──────────────────────────────────────┬──────────────────┘
       │                                      │
       ▼                                      ▼
┌──────────────────────────────────┐ ┌────────────────────────────┐
│ transformation_kinds.py          │ │ admissibility.py           │
│   HECKE_LIFT                     │ │   SPECTRAL_MATCH           │
│   MODULAR_EMBED                  │ │   ZERO_LINE_FORCED         │
│   ANALYTIC_EXTEND                │ │   HECKE_COMPATIBLE         │
│   SPECTRAL_LIFT_INFINITE         │ │   MODULAR_INVARIANT        │
│   TRACE_FORMULA_CLOSE            │ │                            │
└──────────────────────────────────┘ └────────────────────────────┘
       │                                      │
       └──────────────┬───────────────────────┘
                      │
                      ▼
┌────────────────────────────────────────────────────────────────┐
│ Numerical / linear algebra (numpy, scipy)                      │
│ Future: SAGE / Pari for genuine Hecke and modular form data    │
└────────────────────────────────────────────────────────────────┘
```

## Extending the framework

To add a new transformation kind (e.g., a more refined Hecke
construction):

1. Add a new entry to `TransformationKind` enum.
2. Add a function `<new_kind_name>(input, ...)` returning a
   `TransformationOutcome` with `kind = TransformationKind.<NEW>`.
3. If the kind exposes new admissibility content, add a corresponding
   check in `admissibility.py`.
4. Optionally extend `search.py`'s composition generator to include
   the new kind in its enumeration.
5. Re-run examples; new candidates incorporating the new kind appear
   automatically.

No framework redesign is required. The architecture's whole point is
to make this kind of incremental extension safe and natural.

## What the framework is and is not

**Is:**
- A typed formal language for substrate transformations.
- A decidable admissibility predicate for every composition.
- A search engine producing ranked candidates with explicit verdicts.
- A scaffold for incremental addition of mathematical content.

**Is not:**
- A proof of any number-theoretic statement.
- A replacement for SAGE/Pari/Magma for the actual modular-form
  computations.
- A guarantee that a SPECTRAL_MATCH EXACT verdict implies anything
  more than numerical coincidence — the admissibility classes are
  *necessary* conditions for a Hilbert–Pólya construction, not
  sufficient ones.

## The full-translation-tool roadmap

To take this from prototype to "full translation tool" requires
filling in the genuine mathematical content of each transformation
kind. The sequence:

| Milestone | Content |
|---|---|
| 0.2 | Real Hecke action via SAGE / Pari interface on low-weight Hilbert modular forms over Q(√5) |
| 0.3 | Verifiable analytic continuation with functional-equation check |
| 0.4 | Genuine Selberg trace formula admissibility class |
| 0.5 | Integration with closure_ai for goal-directed search (not just enumeration) |
| 1.0 | All prototype kinds replaced; search demonstrably finds operators with EXACT SPECTRAL_MATCH if they exist in the grammar |

Each step is a finite, well-scoped research project. The architecture
is stable; the milestones are about wiring in real mathematics, not
about redesigning the framework.
