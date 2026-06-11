# Consistency and sensitivity

A framework of 20+ numerical predictions is only as strong as its
internal coherence. The VFD Explorer ships two tools that make that
coherence machine-checkable: a **dependency walker** and an
**integer-sensitivity sweep**.

## The dependency graph

Every prediction is annotated with the primitives it depends on —
shell assignments, eigenvalues, framework integers, path-graph
structure. The source of truth is `src/vfd_core/registry/dependencies.yaml`,
linted on every CI run: a registered prediction without declared
dependencies will fail `vfd consistency --lint` and block merge.

```bash
vfd consistency                   # summarise the graph
vfd consistency shell:proton      # which predictions depend on proton shells?
vfd consistency --lint            # enforce registry ↔ graph coverage
```

Representative fan-out (current main):

```
constant:LBAR_P                          ->   8 predictions
eigenvalue:600cell_spectrum              ->   6 predictions
shell:proton                             ->   4 predictions
constant:PHI                             ->   3 predictions
```

`constant:LBAR_P` (reduced Compton wavelength of the proton) is the
widest-fan-out primitive — eight predictions would move if you
perturbed the proton mass. That is the framework's structural spine
made visible.

## Integer sensitivity sweeps

Framework integers (87, 137, 8, 7) are claimed to be **overdetermined**
by multiple independent derivations. The sweep tool proves it: any
other value breaks at least one registered prediction.

```bash
vfd sweep consciousness_dof_87 85 86 87 88 89
```

Output:

```
Sweep consciousness_dof_87: 5 values tested
  value=85   [FAIL]  21 pass, 2 fail
      ✗ alpha_inverse                   rel_err=nan%
      ✗ god_prime_activation_084473     rel_err=nan%
  value=86   [FAIL]  21 pass, 2 fail
  value=87   [PASS]  23 pass, 0 fail
  value=88   [FAIL]  21 pass, 2 fail
  value=89   [FAIL]  21 pass, 2 fail
```

Only **87** passes. This is what "87 is triply overdetermined" means
turned into a runnable fact.

The same sweep on `alpha_inv_tree_137` is equally exclusive:

```
  α⁻¹_tree = 135   [FAIL]  21 pass, 2 fail
  α⁻¹_tree = 136   [FAIL]  21 pass, 2 fail
  α⁻¹_tree = 137   [PASS]  23 pass, 0 fail
  α⁻¹_tree = 138   [FAIL]  21 pass, 2 fail
```

## Shell-assignment sweeps

As of v1.3, `vfd sweep` also accepts `shell:<particle>` primitives
with tuple-shaped values:

```bash
vfd sweep shell:proton "2,3,4" "2,3,5" "3,4,5"
```

Output shows which alternative support breaks which prediction —
the canonical `(2,3,4)` is the only one that leaves the full set
passing.

## Adversarial uniqueness search

`vfd adversarial` enumerates plausible alternative shell
assignments and reports whether the canonical assignment is the
unique fit within the registry's tolerances:

```bash
vfd adversarial shell proton --size 3 --max-shell 6
vfd adversarial shell proton --size 3 --max-shell 6 --contiguous
```

Representative output:

```
Adversarial shell search: proton, size 3, max_shell 5
Tried 10 candidate(s).

Passing candidates (1):
  (2, 3, 4) [canonical]

Failing candidates (9) — sample:
  (1, 2, 3) → fails ['proton_charge_radius', 'deuteron_charge_radius', …]
  …

Uniqueness: 1 / 10 pass.  Canonical assignment is UNIQUE.
```

This is the framework's strongest credibility argument turned into
a runnable check: **of the plausible alternatives, only the
canonical one fits experiment**. The search is bounded (small
combinatorics), deterministic, and auditable.

## What's sweepable

- **Integers**: any primitive listed in
  `vfd_core.sweep.integer_sweep.SUPPORTED_PRIMITIVES`
  (`alpha_inv_tree_137`, `consciousness_dof_87`, `E8_small_8`,
  `S7_seven`, …).
- **Shell assignments**: any particle in
  `vfd_core.shells.assignment.SHELL_ASSIGNMENTS`
  (electron, proton, neutron, pion, kaon, deuteron).

Still not sweepable: 600-cell Laplacian eigenvalues (would require
regenerating the geometry). Flagged for a later release.

## Why this is the credibility story

Reproducibility only proves the framework is **implementable**.
Sensitivity proves it is **constrained** — i.e. that the values
the framework uses are the only values it could use without breaking.

A theory that could have used any integer for the couplings isn't
very predictive. A theory where each integer is forced by multiple
independent consistency checks is. `vfd sweep` is the evidence.
