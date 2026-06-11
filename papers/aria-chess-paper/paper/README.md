# aria-chess paper

A geometry-fixed substrate witness for cortical signatures: eighteen
preregistered correspondences and six drug/sleep EEG signatures from
the 600-cell regular 4-polytope under H₄ Coxeter symmetry.

## Build

```
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Or whatever your LaTeX toolchain prefers. The bibliography uses
`natbib` with `plainnat` style. All paths are relative to this
directory; figures (if added) live under `figures/`.

## Sections

```
sections/01_introduction.tex
sections/02_method.tex
sections/03_substrate.tex
sections/04_consciousness_chain.tex
sections/05_results.tex
sections/06_stress_tests.tex
sections/07_cross_domain.tex
sections/08_discussion.tex
sections/09_limitations.tex
sections/10_conclusion.tex
```

## Reproduction

The empirical numbers in §5–§7 are reproduced from the project
repository's deterministic scripts. From the repo root:

```bash
# six drug/sleep signatures (~30 s)
python3 demo_drug_sleep_v4.py

# C×P synergy N=20 deep-dive (~28 min)
python3 demo_p4_cxp_deep_dive.py

# eighteen preregistered correspondences (~18 min)
python3 run_preregistered_validation.py

# whole-paper repro
bash reproduce_paper_claims.sh
```

All scripts are deterministic given seeds. The substrate's spectral
decomposition is cached at module level. Reruns at seed 42 reproduce
per-condition means in §5.1 to 4 decimal places.

## Source documents

The paper text is lifted from:

- `docs/brain_mapping/MANUSCRIPT_V2.md` (paper-shaped manuscript draft)
- `docs/brain_mapping/CONSCIOUSNESS_CHAIN_V4_SIGNATURES.md` (six signatures)
- `docs/brain_mapping/P4_SYNERGY_FINDING.md` (N=20 deep-dive)
- `docs/brain_mapping/CROSS_DOMAIN_RESULTS.md` (chess / conversation / HCP)
- `docs/brain_mapping/VALIDATION_RESULTS_2026-04-29.md` (18/18 tally)
- `docs/brain_mapping/PAPER_PREDICTIONS.md` (preregistered 2026-04-18)
- `docs/brain_mapping/NON_EQUILIBRIUM_FINDING.md` (state-reset protocol)

## Scope

This is a **substrate witness**: a geometry-fixed substrate is
consistent with eighteen preregistered neuroscience correspondences
and six drug/sleep EEG signatures, with no fitted shape parameters
on any neural dataset. It is **not** a derivation of consciousness,
not a selection theorem on the companion adaptive-closure-transport
4-tuple, and not a uniqueness claim for the 600-cell among regular
4-polytopes. See §1 and §9 for the explicit claim-boundary discipline.

## Status

Preprint, not peer-reviewed. April 2026.
