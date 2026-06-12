# Katz–Sarnak symmetry type — and the full ℝℂℍ trichotomy (Tier-1 step 2)
### 2026-05-30 · `route_b/katz_sarnak.py`

## Two statistics (don't conflate)
- **Bulk** (high zeros of the single L-function): **Unitary / GUE** — universal
  (Montgomery, Rudnick–Sarnak). Verified: `quantum_chaos_test` (⟨r⟩≈0.62).
- **Family** (low-lying zeros across the natural family): the Katz–Sarnak
  symmetry type — **Orthogonal (O+ / SO-even)** here.

## Classification
- **Self-duality** (verified from data): all a_𝔮 are real integers ⇒ L is
  self-dual ⇒ type is **O or Sp, not Unitary.**
- **O vs Sp** (theorem, ILS/Katz–Sarnak): weight-2 GL₂ / elliptic-curve
  families have root numbers varying ±1 ⇒ **Orthogonal** (Sp would need all
  signs +1, as for quadratic-character / symmetric-square families).
- **O+ vs O−** (root number): curve 31.1-a has analytic rank 0 ⇒ sign +1 ⇒
  **O+ (SO-even).**

## The full ℝℂℍ trichotomy — three roles in one object
| role | algebra | class |
|---|---|---|
| substrate (icosian ring) | **ℍ** | Dyson β=4 (quaternionic, GSE-flavoured, degenerate) |
| bulk zero statistics | **ℂ** | Unitary / GUE, β=2 (verified) |
| family symmetry type | **ℝ** | Orthogonal / O, β=1 (self-dual, here) |

The same ℝℂℍ ladder runs Dyson (GOE/GUE/GSE), Katz–Sarnak (O/U/Sp), the
division algebras, and the VFD cascade — and all three appear here, in three
distinct roles. The object is ℍ-built, has ℂ-unitary bulk zeros, sits in an
ℝ-orthogonal family.

## Consequence for the operator
- The missing self-adjoint operator lives on the **ℂ / unitary (GL₂)** side
  — the bulk-zero side (`JACQUET_LANGLANDS.md`).
- The **ℝ / orthogonal** type is the *family* symmetry (low zeros) — a
  different statistic, NOT where the generator lives.
- The **ℍ** substrate is the wrong Dyson class (β=4) to be the operator.
Keep the three roles distinct: the operator targets the ℂ/unitary bulk.

## Honest status
- Self-duality (→ O/Sp, not U): **verified** from data (a_𝔮 real).
- Orthogonal (not Sp) + O+ (rank 0): **theorem-grade** (ILS) + known rank.
  Full numerical confirmation needs the one-level density over a family of
  quadratic twists (many L-functions' zeros) — scoped, not run.
- Bulk GUE: verified earlier.
