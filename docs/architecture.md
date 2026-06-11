# How the Explorer works

The Explorer is a small Python package (`src/vfd_core/`) with a
deliberately conservative architecture. Every design decision
optimises for one thing: **any reader can rederive any claim in
seconds, without trusting the authors.**

## Single source of truth

```
src/vfd_core/
    constants.py           # physical & framework constants (CODATA / PDG)
    geometry/
        sixhundred_cell.py # the 120-vertex 600-cell, built once
        path_graph.py      # P_n Laplacians used in hadron radii
    algebra/
        spectrum.py        # integer eigenvalues, the triple route to 87
        mass_exponent.py   # Paper IV shell-invariant mass exponent
    shells/
        assignment.py      # canonical particle → shell support map
    predictions/
        radii.py           # r_p (E + M), ⟨r_n²⟩, r_π, r_K, r_d
        couplings.py       # α⁻¹, sin²θ_W
        constants.py       # 084473, integer-mode count, Coxeter sum,
                           # 3/5 ratio, Hopf 12×10, generation count
        masses.py          # m_p/m_e, m_μ/m_e, m_τ/m_e
        form_factors.py    # G_E(Q²) 120-vertex resolvent + sampled points
        moments.py         # Dirac lattice g-factor (framework-internal)
    registry/
        predictions.yaml   # the contract: id → function → experiment
        dependencies.yaml  # DAG: which primitive each prediction touches
    validation/
        verify.py          # run the registry, score vs experiment
        report.py          # render Markdown credibility report
        consistency.py     # DAG walker, lint, perturbation report
        provenance.py      # `vfd why` — derivation chain for a prediction
    sweep/
        integer_sweep.py   # perturb integer primitives, re-run verify
        shell_sweep.py     # perturb shell assignments, re-run verify
        adversarial.py     # uniqueness search over shell alternatives
    cli.py                 # verify, predict, report, list, consistency,
                           # sweep (int + shell), why, adversarial
```

## The registry is the contract

`registry/predictions.yaml` lists every numerical claim with its
Python callable, its experimental target, its uncertainty source, and
its tolerance. A prediction cannot exist outside the registry; adding
one requires a YAML entry, a Python function, and a test. The
credibility report is the registry rendered against measurement.

## Every step is reversible

Each prediction function is a pure function of the canonical
primitives. If you disagree with a choice — a shell assignment, an
eigenvalue algebra, a coherence-length identity — change it and rerun
`vfd verify`. The consistency test will tell you immediately which
other predictions have moved.

## No hidden numerics

Framework integers (87, 94, 084473, factor 4) are never free
parameters. Each is derived from geometry or representation theory
and registered as a structural claim with zero tolerance — meaning
the identity must hold exactly, or the build fails.

## No curated success

The report shows every prediction in registry order, passes and
failures both. If a new paper registers a claim that does not match
experiment within its stated tolerance, the CI goes red and this
site shows the red in its table. The framework is not hidden; it is
exposed.
