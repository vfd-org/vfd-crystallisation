# cascade-refinement-papers

> *A five-paper bundle that builds the finite-level cascade refinement
> infrastructure (vertex/edge Hilbert chains, downward bonding maps,
> finite-level dynamics), discharges the refinement-compatibility
> obligation of the cascade-closure consumer API in an abstract
> scalar pure-midpoint model, and supplies a witnessed (O1) tuple
> for the cascade-mechanism API on the H_4 branch at every finite
> top-rung level.*

This repository ships **five preprints** as a single coherent release.
They share an underlying refinement geometry on the 600-cell and the
24-cell, and chain together as **P3 → P4 → cascade-refinement-compat →
cascade-mechanism → cascade-selection-h4**: P3 builds the finite-level
Hilbert spaces, P4 puts dynamics on them, cascade-refinement-compat
discharges the residual-monotonicity obligation in an abstract scalar
model, cascade-mechanism defines the consumer API that successor papers
in the cascade programme will cite, and cascade-selection-h4 is the
first such successor — a witnessed (O1) discharge on the H_4 branch
at every finite top-rung level N ≥ 0, parametrised by a free choice
in a punctured 28-dimensional W(H_4)-fixed subspace of F^0.

| | paper | scope | status |
|---|---|---|---|
| **P3** | [cascade-refinement-spaces][p3] — *finite-level Hilbert infrastructure* | Refinement datum (V, E, F, ∂); finite-level spaces $X_n^{0,\bullet}, X_n^{1,\bullet}$; downward bonding maps $p_{n+1,n}^0$ (restriction) and $p_{n+1,n}^1$ (averaging); adjoints $j_{n,n+1}^0, j_{n,n+1}^1$; vertex inverse-limit $X_\inv^{0,\bullet} \cong \ell^2(V_\infty^\bullet; F^0)$; finite-level Coxeter intertwinings; mixed-form vertex $\sigma$-intertwinings on $X_n^{0,\bullet}\vert_{\Q(\varphi)/\Q}$. | publication-ready (9 hostile-review rounds) |
| **P4** | [cascade-closure-dynamics][p4] — *finite-level closure dynamics* | Closure functional $F_n = \alpha R_n + \beta E_n - \gamma Q_n$ with bounded self-adjoint gradient $L_n$; continuous-time gradient flow $e^{-tL_n}$; energy dissipation; Euler one-step descent; coboundary refinement compatibility (factor $\tfrac{1}{2}$); mass-only refinement and flow intertwining ($\alpha=\beta=0$); explicit generator-family list with operator-norm bounds. | publication-ready (6 hostile-review rounds) |
| **cascade-refinement-compat** | [cascade-refinement-compat][rc] — *(O3) discharge in abstract scalar model* | Schur-complement halving identity for the scaled curvature operator $\widetilde A_n = 2^n A_n^{\mathrm{vertex}}$; full discharge of cascade-closure consumer-obligation (O3) in an abstract scalar pure-midpoint refinement model; explicit obstruction proof that strict operator-level (O2) fails for nontrivial refinements (with defect $D_n$ characterised via the unsigned vertex–edge incidence operator $\mathcal{B}_n$). Lift to full P3/P4 tower conditional on open hypotheses (L1) and (L3). | publication-ready (7 hostile-review rounds) |
| **cascade-mechanism** | [cascade-mechanism][cm] — *consumer API for cascade closure* | Definition 3.1 (cascade-closure event) + Proposition 3.6 (residual-zero / fixed-point propagation under flow-intertwining + monotonicity hypotheses) + Corollary 3.7 (convergence propagation) + Consumer API §3.4 (four obligations O0-O3) + Worked-invocation §3.5 (P3/P4 finite-level tower with explicit per-obligation open-status verdict) + Appendix C (programme-placement table). | publication-ready, codex programme-contribution verdict **(a) Moves the needle, now full** (20 hostile-review rounds + 3-round companion alignment) |
| **cascade-selection-h4** | [cascade-selection-h4][csh] — *witnessed (O1) discharge on the H_4 branch* | Auxiliary block graph Laplacian $L_N^{\mathrm{block}} = L^{\mathrm{cl}}_N \otimes \mathrm{id}_{F^0}$ on $X_N^{0,H_4}$ (distinct from P4's $A_n^{\mathrm{vertex}}$ and from compat's $\widetilde A_n$); single named Theorem `thm:main` with five proved ingredients — bounded self-adjoint PSD operator with Chung-style norm bound; connected refined graph $G_N^{H_4}$ + $\ker L_N^{\mathrm{block}} \cong F^0$ via constant embedding $\iota_N$; convergence of $e^{-tL_N^{\mathrm{block}}}$ to kernel projection at exponential rate $\lambda_+(L_N^{\mathrm{block}}) > 0$; $\dim_{\mathbb{R}}(F^0)^{W(H_4)} = 28$ from $H_4$-irreducibility; witnessed $(O1)$ five-tuple in the witnessed-fixed-point sense for any $\xi^* \in (F^0)^{W(H_4)} \setminus \{0\}$; (O0) verified at top-rung level only; explicit $N=0$ numerics ($\lambda_+ = 9 - 3\sqrt{5}$ from P2 spectrum). | publication-ready (5 hostile-review rounds, three consecutive yes verdicts) |

[p3]: papers/cascade-refinement-spaces/
[p4]: papers/cascade-closure-dynamics/
[rc]: papers/cascade-refinement-compat/
[cm]: papers/cascade-mechanism/
[csh]: papers/cascade-selection-h4/

## Reading order

1. **P3** (`cascade-refinement-spaces`) — read first; it fixes the
   notation, the refinement datum, the finite-level chain spaces,
   and the bonding-map / adjoint structure that everything else
   imports.
2. **P4** (`cascade-closure-dynamics`) — read second; it puts a
   bounded self-adjoint closure functional on each $X_n$, defines
   gradient flow, and proves a coboundary factor-$\tfrac{1}{2}$
   refinement identity plus mass-only flow intertwining.
3. **cascade-refinement-compat** — read third; it works in a
   deliberately reduced abstract scalar pure-midpoint model and
   proves the Schur-complement halving identity that discharges
   cascade-closure (O3) in that scope.
4. **cascade-mechanism** — read fourth; it defines the consumer
   API for cascade closure (O0)–(O3) and walks through the P3 / P4
   / compat machinery as a worked invocation, recording the
   precise open status of each obligation.
5. **cascade-selection-h4** — read fifth; it is the first
   successor that uses the cascade-mechanism API, supplying a
   witnessed (O1) tuple on the H_4 branch via a new auxiliary
   block graph Laplacian, parametrised by a free choice in the
   28-dimensional W(H_4)-fixed subspace of the fibre $F^0$.

## What this bundle claims

- A rigorous finite-level cascade refinement infrastructure: chain
  spaces, bonding maps, adjoints, inverse-limit Hilbert space (vertex
  sector), and finite-level Coxeter / mixed-form $\sigma$
  intertwinings — all proved at the standard of finite-dimensional
  functional analysis on top of P1 (`cascade-sigma-rationality`)
  and P2 (`cascade-algebraic-substrate`).
- A bounded self-adjoint quadratic closure functional with a
  well-defined gradient flow, energy dissipation identity, and
  explicit bounds — and a careful disambiguation of when refinement
  compatibility holds (mass-only flow, coboundary factor) and when
  it does not (full $L_n$ in $\alpha,\beta>0$ regime: open).
- A complete discharge of the residual-monotonicity obligation (O3)
  of the cascade-closure consumer API in an abstract scalar
  pure-midpoint refinement model, plus an explicit proof that strict
  (O2) fails for nontrivial refinements with the Schur-complement
  identity as the natural substitute.
- A consumer-grade interface for cascade closure: successor papers
  citing cascade closure as load-bearing know exactly which four
  obligations they must discharge, and exactly what the present
  bundle has and has not closed.
- A worked first invocation of that consumer API on the H_4
  branch: a single named theorem (`thm:main` in
  cascade-selection-h4) producing an explicit witnessed (O1)
  five-tuple at every finite top-rung level $N \geq 0$,
  parametrised by a free choice $\xi^*$ in a punctured
  28-dimensional $W(H_4)$-fixed subspace.

## What this bundle does not claim

- **No physical selection theorem.** cascade-mechanism is a
  *compatibility-template prerequisite*: it propagates residual-zero
  / fixed-point status downward under flow-intertwining + monotonicity
  hypotheses. cascade-selection-h4 then supplies a *witnessed* (O1)
  tuple on the $H_4$ branch in the fixed-point sense, but the
  $\xi^*$-parameter is a free choice in the punctured 28-dimensional
  $W(H_4)$-fixed subspace; **single-ray (single-state) physical
  selection** is the named open hypothesis **(H-uniqueness)** of
  cascade-selection-h4 §`sec:open-hyp` and lies *outside* the
  cascade-closure consumer API. No basin-of-attraction selection
  from arbitrary initial data is claimed.
- **No full P3/P4-tower (O3) discharge.** The Schur-complement
  identity and the (O3) discharge in cascade-refinement-compat hold
  in a deliberately reduced abstract scalar pure-midpoint model.
  Lift to the full P3/P4 tower is conditional on open hypotheses
  (L1) (refinement-compatibility of the *unscaled* curvature
  operator $A_n$) and (L3) (spectral-gap propagation across
  refinement levels). (L2), the half-section identity
  $p^1 j^1 = \tfrac{1}{2}\,\mathrm{id}$, is already a theorem of P3
  via Proposition `prop:adjoints`.
- **No edge inverse-limit Hilbert space.** P3 constructs the
  vertex inverse-limit $X_\inv^{0,\bullet}$ but explicitly does not
  build an edge inverse-limit Hilbert space with averaging-bonding
  maps. Edge intertwinings are stated only at the finite level.
- **No real-Hilbert $\sigma$-action.** The Galois involution
  $\sigma \colon \Q(\varphi) \to \Q(\varphi)$ is defined only on
  the mixed $\Q(\varphi)/\Q$ vertex form; it does not extend
  $\R$-linearly to the real Hilbert space $X_n^{0,\bullet}$.
- **No continuum limit / target-side correspondence.** No PDE
  identification of $\dot\Phi_n = -L_n\Phi_n$ with any classical
  evolution; no metric / spectral / Hecke / cohomology
  correspondence theorem.

## Repository layout

```
papers/cascade-refinement-spaces/   # P3 — finite-level Hilbert infrastructure
├── cascade-refinement-spaces.tex   # tex source, label-form citations to P1/P2
└── cascade-refinement-spaces.pdf   # built PDF, ~220 KiB

papers/cascade-closure-dynamics/    # P4 — finite-level closure dynamics
├── cascade-closure-dynamics.tex    # tex source, label-form citations to P3/P2
└── cascade-closure-dynamics.pdf    # built PDF, ~210 KiB

papers/cascade-refinement-compat/   # (O3) discharge in abstract scalar model
├── cascade-refinement-compat.tex
├── cascade-refinement-compat.pdf   # ~165 KiB
└── references.bib

papers/cascade-mechanism/           # cascade-closure consumer API
├── cascade-mechanism.tex
├── cascade-mechanism.pdf           # ~190 KiB
└── references.bib

papers/cascade-selection-h4/        # witnessed (O1) on H_4 branch
├── cascade-selection-h4.tex        # tex source, label-form citations
└── cascade-selection-h4.pdf        # built PDF, ~170 KiB
```

## Upstream dependencies (cited but not in this bundle)

This bundle uses two upstream cascade-correspondence papers as
theorem-grade input. They are part of the broader cascade programme
and are not duplicated here:

- **P1** (`cascade-sigma-rationality`): the Galois involution
  $\sigma \colon \Q(\varphi) \to \Q(\varphi)$, coefficientwise
  $\sigma_V$ on scalar extensions, and functoriality of the scalar
  extension $T_K$ for $\Q$-linear maps.
- **P2** (`cascade-algebraic-substrate`): the icosian ring, $V_{600}$
  and $V_{24}$ vertex sets, the Clifford monomial basis on
  $\Cl(1,3)$, the standard octonion basis, sector $\Q$-forms, and
  the $G_2$ stabilizer of a unit imaginary octonion.

## Provenance

Each paper went through a hostile-review loop with codex (`gpt-5.4`)
until a publication-ready convergence verdict was returned.
Round-by-round review notes are at
`docs/reviews/<paper-stem>-<UTC-timestamp>.md` in the upstream
working repository (vfd-crystallisation).

## License

MIT License — see [LICENSE](LICENSE).
