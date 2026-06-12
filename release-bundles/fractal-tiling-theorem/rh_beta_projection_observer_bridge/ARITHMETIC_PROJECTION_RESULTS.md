# Deliverable D — arithmetic operator projection results

Source: `arithmetic_projection_tests.py`,
`results/vfd_brandt_beta_audit/`, `results/projection_candidates/`.

## The actual icosian/Brandt objects audited

| object | size | spectral structure | β-class (spacing) | β-class (symmetry) |
|---|---|---|---|---|
| 600-cell adjacency | 120×120 | **9 distinct eigenvalues**, 93% degenerate spacings | none (structured, not random) | β=4 (quaternionic) |
| icosian unit group `2I` | 120 | ⊂ **SU(2)** (120/120), Kramers `J²=−1` | n/a | β=4 (symplectic) |
| Brandt/Hecke `B(P)` | 2×2 | self-adjoint, real spectrum `= a_P` | too small for spacing | coefficient-side |

## Per-projection survival (Tests 1–6 of the WO)

For the **complexification** `Π = (ℍ⊗ℂ ≅ M₂(ℂ))`, the canonical candidate:

| question | answer |
|---|---|
| 1 self-adjointness survives? | yes (Hermitian on `M₂(ℂ)`) |
| 2 positivity survives? | yes (the trace form stays positive) |
| 3 trace arithmetically meaningful? | yes (reduced trace/norm preserved) |
| 4 β-class changes? | **yes** — quaternionic (β=4) → complex (β=2) at the symmetry-class level |
| 5 zero-sensitive info appears? | **no** — still coefficient-side, zero-blind |
| 6 connects to Weil/explicit formula? | only via the prime side already built; the map itself does not |

For the **spacing-level** projections (B3, B4): β-class does **not** change
(stays β=4); for the circular B1-restriction it changes but **destroys** the
arithmetic object (builds a generic GUE matrix). So:

- **Pass** (WO Deliverable D): complexification moves the symmetry class β=4→β=2
  while preserving self-adjointness, positivity and trace — a genuine non-circular
  projection of the arithmetic structure.
- **Fail** of the stronger hope: it does **not** make the object zero-sensitive.
  No projection moves the coefficient-side object to a zero-side spectral object
  without either staying β=4 or destroying arithmetic meaning.

## Reading

The β=4 of the icosian substrate is quaternionic *symmetry*, and it canonically
complexifies to β=2 *symmetry* — but this is the Jacquet–Langlands / `ℍ⊗ℂ=M₂(ℂ)`
move (known, verified to `2e-16` in `JACQUET_LANGLANDS.md`), and it is zero-blind.
The zeta zeros' β=2 is a **spacing** fact about analytic zeros, reached only
through the explicit formula / Weil positivity — not through this projection.
