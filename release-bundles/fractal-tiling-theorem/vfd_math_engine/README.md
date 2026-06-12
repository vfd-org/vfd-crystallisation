# VFD Math Engine — a gate-first geometry→arithmetic certifier

A *math-as-language* engine. An **expression** is a proposed correspondence

```
(VFD geometric object)  <->  (arithmetic object / L-function)
```

The engine **computes** the correspondence and **certifies** it through a
verification gate. ARIA *proposes* candidate expressions; the gate *disposes*.

## Honest scope (welded into the code)

> This engine **CERTIFIES** the geometry↔arithmetic landscape. It issues
> **verification certificates** only — it **never** issues a proof certificate,
> and it does **not** prove the Riemann Hypothesis. The missing object that would
> prove RH (an arithmetic surface / a Frobenius whose degree-form is the Weil
> positivity) is a **construction**, not a search target. This is a **microscope
> that certifies structure**, not a forge that builds the missing object.

What it genuinely delivers: it separates the **cuspidal-reachable (proven) side**
(ζ_K *verifies*) from the **Eisenstein / ζ wall** (every "bridge to ζ" is
*rejected*), and it auto-kills **fitted maps** (the W5 hardcoding trap) by
provenance — making every VFD claim exact, reproducible, and undismissable.

## Architecture (5 layers)

| layer | file | role |
|---|---|---|
| representation / **dictionary** | `engine_v2.py` | `Expression(geometry, claim, predict, meta, provenance)` |
| **grammar** (composable ops) | `engine_v2.py` | `galois_twin`, `restrict_24cell`, … transform expressions |
| **compute** | builders inside each expression | produce the predicted on-line zeros / metadata |
| **verification gate** (load-bearing) | `engine_v2/v3.py` | 8 checks — see below |
| **certificates + atlas** | `engine_v2/v3.py` | hashed reproducible records → `atlas.json` |

## The gate — 8 checks

1. **no_hardcoding** — the builder must not take the target as input (anti-circular).
2. **provenance** — no `fitted`/`tuned` constants (kills the W5 trap).
3. **fingerprint** — spacing of on-line zeros (gaps<0.3): pure-ζ GUE ≈ 0.0 vs mixed ζ_K ≈ 0.08.
4. **pointwise** — first-8 predicted zeros match the claimed target.
5. **degree** — declared L-function degree matches.
6. **pole** — pole-at-s=1 status matches.
7. **density** — zeros-per-unit-height (Weyl law) matches.
8. **rigidity** — number variance Σ²(L) (GUE-rigid ≈ 0.3) matches.

An expression is **VERIFIED** only if it passes all applicable checks.

## ARIA proposer interface

`engine_v3.py`:
- `Proposer.propose(dictionary, goal) -> [Expression]` — `goal` is a desired
  arithmetic signature, e.g. `dict(degree=1, pole=True)`.
- `AriaProposer(llm_fn=...)` — **the real-ARIA slot.** `llm_fn(prompt:str)`
  returns a list of candidate specs `{name, object, claim, degree, pole, builder}`.
  Falls back to a structural heuristic if `llm_fn` is `None`.
- **ARIA proposes; the gate disposes.** ARIA never certifies — it only suggests.

## Run

```bash
python3 engine_v3.py        # demo: gate + ARIA + writes atlas.json
python3 run_programme.py    # programme-wide atlas (real VFD objects) + mock ARIA
```

## Extend

Add an `Expression` per VFD object you want to certify (its geometry, its claimed
L-function, a parameter-free builder for its on-line zeros, and honest provenance).
Run `run_atlas([...])`. The atlas accumulates PASS/FAIL certificates — and **most
honest outputs are negatives.** That is the point.
