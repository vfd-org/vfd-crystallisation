# The Critical Line, Pulled Back to V₆₀₀

**Computational checks on the substrate image of ζ(s)'s non-trivial
zeros — a pipeline sanity check, two verified finite computations, one
exact negative result (the principal finding), and four exploratory
follow-ons stamped as such**

> **v1.1 revision note (2026-06-12).** Adversarial review found v1's
> framing too strong in specific places, now fixed in the paper:
> Finding 1 is a *sanity check* (the vanishing is forced by the
> explicit ζ factor — the evaluation imports both the published
> factorisation and the tabulated zero ordinates); Finding 5 is a
> *bookkeeping-level* Galois split of the spectrum, not a constructed
> involution, and the v1 wording locating the zeros on the 94-dim block is withdrawn
> (only scalar factor attribution is computed); Finding 7 is a
> *conditional suppression lemma*, not a universality theorem;
> Finding 8 is a *heuristic sweep*, not certified root-finding, and
> "every zero attributed exactly" is withdrawn. Sims v9/v10 are
> least-squares-fitted and serve only as negative controls.

This bundle is the geometry-first probe answering the question:

> "When the analytic critical line of ζ(s) is pulled back into V₆₀₀
> coordinates via the Hilbert modular L-function identity, where does
> it sit on the substrate? Is it a helix, as the original geometric
> intuition suggested?"

## The findings (status-stamped)

1. **Sanity check: substrate L vanishes at the tabulated Riemann
   zeros.** Evaluating L_sub(s) = ζ_K(s)·ζ_K(s−1)·C_2(s) at the
   first 10 tabulated zeros gives |L_sub| < 2.2·10⁻¹¹ — *as forced by
   the explicit ζ(s) factor of the published factorisation*. This
   verifies the pipeline and displays the substrate image of the
   critical line; it is not evidence of a substrate zero law.

2. **Eichler–Brandt holds exactly at K=4.** For every odd inert
   prime p ≤ 23, the icosian representation count r(p) matches
   8(1+p²) exactly. p=2 reproduces the Jacobi anomaly r(2)=24.

3. **The helix is visible.** A V₆₀₀ vertex of order 10 produces a
   closed 10-vertex helical orbit on S³, stereographically
   projected to R³.

4. **Principal finding (exact, negative): coordinate-Galois σ does
   NOT preserve V₆₀₀.** 96 of 120 vertices map under φ → 1−φ to
   positions outside V₆₀₀. The "94 + 13 + 13" σ-decomposition from
   the icosian-triad paper must come from a different involution τ.
   Finding 5 (exploratory) gives a bookkeeping-level candidate by
   grouping the C_φ eigenvalues by Galois conjugacy; constructing τ
   on the vertex space or operator algebra remains open.

## What is in this bundle

```
paper/
  critical-line-pullback.tex
  critical-line-pullback.pdf
  references.bib

sims/
  sim_critical_line_pullback.py   (v1: initial probe)
  sim_v2.py                        (v2: analytic L, clean helix, K=4 Eichler-Brandt)
  sim_v3_sigma_exact.py            (v3: exact sigma diagnostic)

outputs/
  01_v600_stereographic.png        (v1)
  02_icosian_rotation_helix.png    (v1)
  03_prime_norm_shells.png         (v1)
  04_l_function_path.png           (v1)
  05_zero_proximity_log.png        (v1)
  v2/
    01_clean_helix.png             (the 10-vertex closed orbit)
    02_l_spiral_riemann_marked.png (THE LOAD-BEARING PLOT)
  v3/
    01_c_phi_sigma_split_exact.png (diagnostic only — σ fails to
                                     preserve V_600)

data/
  v600_vertices.csv
  icosian_helix_orbit.csv
  icosian_norm_distribution.csv
  l_function_path.csv
  v2/
    helix_orbit.csv
    l_substrate_at_riemann_zeros.csv  (key empirical table)
    eichler_brandt_table.csv
    c_phi_spectrum.csv
  v3/
    sigma_decomposition.csv

README.md
CHANGELOG.md
LICENSE
.gitignore
```

## How to reproduce

```bash
# Requires: numpy, scipy, matplotlib, mpmath
python3 sims/sim_v2.py             # main probe
python3 sims/sim_v3_sigma_exact.py # sigma diagnostic
```

The `sim_v2.py` run takes ~30 seconds; v3 takes ~10 seconds. Outputs
go to `outputs/v2/` and `data/v2/`.

## What this is and is not

### Is

A self-contained geometry-first numerical probe showing where the
Riemann critical line lives on the V₆₀₀ substrate under the
Hilbert modular L-function identity. The empirical core is
Finding 1: the substrate L-function vanishes at every Riemann
zero, plotted explicitly.

### Is not

A proof of the Riemann Hypothesis. The factorisation identity
L_sub = ζ_K·ζ_K(s−1)·C_2 is one-way: ζ-zeros imply L_sub zeros,
but the converse direction (any off-critical L_sub zeros
corresponding to off-critical ζ zeros) is not provided here.

## Status

Pre-peer-review open research preprint, v1.1.0-rc1, 2026-06-12
(revised after adversarial review; see CHANGELOG). Not independently
validated.

## Open follow-on (pinned down)

**Identify the involution τ on the icosian unit shell that
carries the "94 + 13 + 13" decomposition of C_φ.** Coordinate-
Galois σ on its own is not τ — Finding 4 shows σ doesn't preserve
V₆₀₀ as a set. The natural candidates are: (i) σ ∘ (parity flip
even-perm ↔ odd-perm); (ii) icosian conjugation q → q̄; (iii) a
Hecke operator T_p. Resolving this is the next probe.

## Companion bundles

- `vfd-org/icosian-triad-v600` — the math anchor (substrate, C_φ,
  Eichler–Brandt theorem).
- `vfd-org/closure-picture` — the programme-wide interpretive
  synthesis (places this probe in the larger Closure-and-Number
  chapter).
- `release-bundles/translation-layer` — the polytope-overlap-as-
  grammar paper (this probe is one Layer-3 translation row).
- `release-bundles/evidence-ledger` — the audit framework
  (Finding 1 is a pipeline sanity check of a published identity;
  Finding 2 is Class A empirical verification; Finding 4 is the
  principal exact negative result, with its follow-on a Class B open).

## Licence

CC BY 4.0. See `LICENSE`.
