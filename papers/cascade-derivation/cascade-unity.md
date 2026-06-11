# The Unity Rung (0)

**Phase 2c deliverable.** Status: operational definition complete;
quantitative Λ derivation open.

Companion to `WO-CASCADE.md` and the other per-rung documents.

---

## 1. Purpose and Scope

The 0 rung is the **endpoint** of the cascade, not a non-trivial
geometric structure. It is what the other six rungs collapse to
under full closure. This document establishes its operational
definition, notes the structural consistency of its role in the
cascade, and honestly marks the one quantitative target that remains
open (the cosmological constant derivation).

---

## 2. Operational Definition

The 0 rung is the set of closure configurations at which the closure
functional F attains its global minimum:

```
Rung 0  :=  { Φ ∈ closure space  :  F[Φ] = min F = 0 }
```

The minimum is normalised to 0 by convention (zero-point subtraction),
so `F[Φ_0] = 0` at the ground state.

### 2.1 What this means physically

At the 0 rung:

- **All sub-rung closures are simultaneously satisfied.** No residual
  structure remains at any of the non-trivial rungs.
- **The state projects to the trivial irreducible representation on
  every rung.**
- **All observables are zero** (energy, momentum, charge, spin, etc.)
  relative to the ground state.

The 0 rung is therefore the **cascade vacuum**: the unique (up to
symmetry) configuration where all seven rungs close simultaneously.

### 2.2 Cascade dynamics

Physical dynamics is movement towards the 0 rung:

- The closure functional F acts as an energy functional; its
  gradient flow drives configurations toward the ground state.
- Each rung has its own closure criterion; the full ground state
  requires simultaneous satisfaction.
- Any **observable structure** is residual closure failure at some
  sub-rung — the deviation of the current configuration from the
  ideal 0-rung state.

This is consistent with the VFD programme's general framing: physics
is constraint-driven closure, with observable quantities as
symmetry-breaking residues of the ground state.

---

## 3. Structural Consistency: Sum over Rungs

`scripts/unity_rung.py` confirms that each of the seven cascade
rungs contributes **exactly one** ground-state dimension (the trivial
irreducible representation in each case):

| Rung | Ground-state object | Mult |
|---|---|---|
| E₈ (248) | trivial rep | 1 |
| H₄ (120) | trivial rep | 1 |
| 40 (icosahedral) | trivial rep | 1 |
| D₄ (24) | trivial rep | 1 |
| 16 (4-cube) | scalar γ_∅ | 1 |
| 8 (octonionic) | identity 1 ∈ O | 1 |
| 0 (unity) | vanishing F | 1 |
| **Total** | | **7** |

**The cascade has exactly 7 rungs, and each contributes exactly 1
dimension of ground-state structure. Total: 7.**

This matches the dimension of the **observer configuration space**
S⁷ identified at the 8 rung (Phase 2b). The two 7's are not
independent:

```
cascade rungs = 7 = dim(S⁷) = dim of observer configuration space.
```

This is a **structural consistency check**, not a derivation — but
it is not a trivial one. The number of cascade rungs, derived
independently from the god-prime modular cascade, matches the
dimension of S⁷ derived independently from the octonion algebra.
Both come from the same E₈/O/Spin(8) source.

---

## 4. The Cosmological Constant Problem

### 4.1 Statement of the problem

| Quantity | Value |
|---|---|
| Observed Λ | ≈ 1.1 × 10⁻⁵² m⁻² |
| Λ_Planck | ≈ 3.83 × 10⁶⁹ m⁻² (Planck-scale energy density) |
| Ratio | Λ_obs / Λ_Planck ≈ 10⁻¹²² |

The naive QFT vacuum-energy prediction matches Λ_Planck. The
discrepancy of 10¹²² is the cosmological-constant problem —
arguably the deepest unsolved problem in theoretical physics.

### 4.2 Cascade qualitative interpretation

The cascade interpretation, structurally consistent with the
operational definition (§2):

> At the ideal full-closure ground state, F = 0 exactly, and
> therefore Λ = 0. The observed nonzero Λ measures **residual
> cascade closure failure** — the system is not yet at its full
> ground state.

This explains *qualitatively* why Λ is small-but-nonzero: if it were
zero we would already be at the ground state; if it were Planck-
scale the cascade structure would not yet have acted at all. The
observed value is an intermediate closure residue.

### 4.3 Quantitative derivation: OPEN

No clean cascade-structural expression for the factor 10⁻¹²² has
been found. Candidates tested in `scripts/unity_rung.py`:

| Candidate expression | Value | Target |
|---|---|---|
| log₁₀(|2I|) × 7 rungs | 14.55 | 122 |
| log₁₀(|W(E₈)|) | 8.84 | 122 |
| 2 × log₁₀(|W(F₄)|) × 7 rungs | 42.86 | 122 |
| 7 × log₁₀(|2I|) × 2 | 29.11 | 122 |
| α⁻¹ × log₁₀(|2I|) | 284.85 | 122 |
| 120 × log₁₀(|2I|) / 4 | 62.38 | 122 |

None match 122 within reasonable tolerance. Deeper candidates
involving cross-rung couplings or non-trivial projection operators
have not been exhausted.

**The quantitative Λ derivation is therefore an open problem for the
cascade framework.** The qualitative interpretation (Λ as residual
cascade closure failure) is structurally consistent and meaningful,
but does not predict the specific exponent 122.

This is the most important open cascade prediction: a full
derivation of Λ = 10⁻¹²² × Λ_Planck from cascade structure would be
a major test (and, if quantitative, a Nobel-level result). We mark
it as the primary open Phase 2c sub-task.

---

## 5. Connection to Other Rungs

### 5.1 Relationship to the GR rung (C6: κ = 8πG)

The Einstein equations are G_μν = 8πG T_μν + Λ g_μν. The
cosmological constant Λ appears on the GR side. The Newton
constant κ = 8πG appears as the coupling to T_μν.

**The two open GR-rung quantitative targets** (C6 — κ identification;
§4.3 here — Λ derivation) are therefore closely related:
- κ measures how closure residual **couples to** matter.
- Λ measures the **ambient** closure residual.

Both should fall out of the same cascade-level coupling-constant
analysis. This is currently open; we flag it as the primary Phase 2c
× Phase 1c cross-phase task.

### 5.2 Relationship to Paper XXXIII (measurement)

Paper XXXIII identifies a measurement outcome as the closure
projection minimising F. At the 0 rung, F = 0 and measurement is
trivial (nothing to measure). Physical measurement therefore occurs
at **non-zero rungs** — the observation is the residual closure at
whichever rung the observer engages.

This is consistent with the cross-rung composition rule:
measurement = observer × QM (not observer × 0).

---

## 6. Status

| Item | Status |
|---|---|
| Operational definition of 0 rung | ✓ |
| Ground-state sum across rungs = 7 | ✓ structural consistency with S⁷ |
| Cosmological constant as residual closure | ✓ qualitative |
| Quantitative Λ ≈ 10⁻¹²² × Λ_Planck | ✗ open — primary open cascade target |
| Connection to κ = 8πG (GR C6) | ✓ identified as joint problem |

**Phase 2c substantively complete** at the operational / structural
level. Quantitative Λ derivation is the primary remaining cascade
target.

---

## 7. Working Log

### 2026-04-17 — Phase 2c (Unity rung) completed

- Stated operational definition: 0 rung = ground state of F.
- Verified 600-cell Laplacian has eigenvalue 0 with multiplicity 1
  (trivial rep of 2I), confirming the discrete ground state exists
  and is unique up to the trivial rep.
- Sum of ground-state dimensions across 7 rungs = 7 = dim(S⁷)
  observer space — structural consistency check.
- Cosmological-constant problem: cascade interpretation as residual
  closure failure is structurally consistent; quantitative derivation
  of 10⁻¹²² suppression remains open.
- Identified Λ and κ (= 8πG) as joint cascade targets — both involve
  the rung 0 closure structure and the GR rung 24 coupling.

**All seven cascade rungs now addressed.** Six verified concretely,
one operationally defined as cascade endpoint. The cascade is
structurally closed; quantitative deepening (Λ, κ, full C2 continuum
theorem, B2–B5 biology) continues.
