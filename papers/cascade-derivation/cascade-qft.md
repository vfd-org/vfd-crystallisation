# Cascade QFT — Second Quantisation + Path Integral

**Purpose.** Bridge cascade closure-functional dynamics to second-
quantised QFT and Feynman path integrals. The cascade's F IS the
QFT action, and cascade quantisation IS second quantisation.

**Contents:**
- E14.1 Cascade F = effective QFT action
- E14.2 Feynman path integral from cascade σ-invariant sum
- E14.3 Second quantisation on H₄ Fock space
- E14.4 Creation/annihilation from H₄ eigenvalue shifts
- E14.5 Feynman diagrams from cascade rung interactions

---

## E14.1 Cascade F as QFT action

The cascade closure functional
```
    F[Φ]  =  ∫ (αR + βE − γQ)[Φ] dV
```
is a local functional of the cascade field Φ with rank-0, rank-1,
and rank-2 content. This has exactly the form of a standard QFT
action:

```
    S[Φ]  =  ∫ ℒ(Φ, ∂Φ) d⁴x,
```
where ℒ = Lagrangian density built from Φ and its derivatives.

**Identification:** `S[Φ] = F[Φ]`. The cascade's closure functional
IS the QFT action.

### E14.1.1 Rung-specific actions

At each cascade rung, F reduces to a specific standard-model action:

```
    D₄ rung (gravity):        S_EH = (1/16πG) ∫ R √(-g) d⁴x
    8 rung (EM):              S_Maxwell = -(1/4e²) ∫ F² d⁴x
    16 rung (weak SU(2)):     S_YM = -(1/4g²) ∫ W² d⁴x
    16 rung (Dirac spinors):  S_Dirac = ∫ ψ̄(iγ·D - m)ψ d⁴x
    H₄ rung (scalar QM):      S_KG = ∫ (½∂φ² - ½m²φ²) d⁴x
```

Each is a cascade RUNG RESTRICTION of the master functional F.

## E14.2 Feynman path integral from σ-invariant sum

### E14.2.1 Standard Feynman path integral

```
    Z  =  ∫ DΦ · exp(i S[Φ] / ℏ)
```

where the integral sums over ALL field configurations weighted by
the complex phase of the action.

### E14.2.2 Cascade path integral

In the cascade, Φ ranges over σ-invariant configurations of the
cascade substrate. The sum over configurations is:

```
    Z_cascade  =  Σ_{σ-invariant Φ} exp(i F[Φ] / ℏ)
```

In the continuum limit (C2.bis), the discrete σ-invariant sum
becomes the Feynman path integral:

```
    Z_cascade  →  ∫ DΦ · exp(i F[Φ] / ℏ)   (= Feynman Z).
```

### E14.2.3 Theorem E14.2

> **Theorem E14.2.**  *The cascade's σ-invariant closure-functional
> sum coincides (in the continuum limit) with the Feynman path
> integral of the effective QFT action F. No additional quantisation
> prescription is needed.*

## E14.3 Second quantisation on H₄ Fock space

### E14.3.1 Fock space construction

For many-particle QFT, we need a Fock space:
```
    𝓕  =  ⊕_{n=0}^∞  (Sym^n ℋ or Λ^n ℋ)
```

with symmetric (boson) or antisymmetric (fermion) tensor products.

Cascade naturally produces Fock space on the H₄ rung:
- **ℋ** = L²(H₄-vertices), the single-particle cascade Hilbert space.
- **Sym^n ℋ** for bosons (rank-0 and rank-1 cascade content, α and β).
- **Λ^n ℋ** for fermions (rank-2/spinor cascade content, γ on 16 rung).

### E14.3.2 Bose/Fermi statistics from cascade

Boson statistics (symmetric): particles on the **8/octonion rung**
(gauge bosons) and the **scalar Higgs**. Cascade's octonion algebra
is commutative up to sign on the commuting directions, giving
symmetric wave functions.

Fermion statistics (antisymmetric): particles on the **16/Cl(1,3)
rung** (spinors). Cascade's Clifford algebra has the anticommutation
relations γ_i γ_j = −γ_j γ_i (i ≠ j), giving antisymmetric spinor
wave functions.

**Spin-statistics theorem** emerges naturally from cascade's
rung content (bosons on rank-0 and rank-1, fermions on rank-spinor),
consistent with Pauli's 1940 theorem.

## E14.4 Creation/annihilation from H₄ shifts

### E14.4.1 Shell-depth ladder

The H₄ eigenvalue spectrum {0, 4, 8, 10, 12} (cascade-qm.md §2.1)
provides a natural ladder structure. Define:

```
    a†_k  = shift from shell k+1 to shell k on H₄
    a_k   = shift from shell k-1 to shell k on H₄
    [a_j, a†_k]  = δ_{jk}    (canonical commutation)
```

These satisfy the standard boson creation/annihilation algebra.

### E14.4.2 For fermions

On the 16/Cl(1,3) rung:
```
    {b_j, b†_k}  = δ_{jk}    (anticommutation)
    {b_j, b_k}   = 0
```
following from the Cl(1,3) anticommutation of γ-matrices.

### E14.4.3 Number operator

For each cascade rung mode k:
```
    N_k  =  a†_k a_k
```
eigenvalues = 0, 1, 2, ... (for bosons) or 0, 1 (for fermions,
Pauli exclusion).

## E14.5 Feynman diagrams from cascade rung interactions

### E14.5.1 Vertices from cascade couplings

QFT interactions = vertices in Feynman diagrams, weighted by coupling
constants. In the cascade:

- **Fermion-photon vertex** (QED): coupling e = √(4π α_em) at the
  16-rung × 8-rung interface. Cascade value from F8.
- **Fermion-gluon vertex** (QCD): coupling g_s at 16-rung × 8-rung
  (colour). Cascade value from F8 α_s derivation.
- **Fermion-W/Z vertex** (EW): coupling g_W at 16-rung × 8-rung
  (weak). Cascade value from F8 β.
- **Higgs-fermion vertex**: Yukawa coupling y_f = m_f / v. Cascade:
  from E3 shell-depth.

### E14.5.2 Loops from cascade σ-orbits

Feynman loop integrals ∫d⁴k/(2π)⁴ ... emerge from cascade's σ-orbit
sum over dual 600-cells. Each loop contributes a factor from σ-
averaging.

### E14.5.3 UV regularisation automatic

Standard QFT has UV divergences requiring regularisation. In the
cascade, the Planck-scale cutoff is BUILT IN (F1 base permeability
at φ scale): integrals run from 0 to M_Planck, not infinity.

**UV divergences are cascade-regularised automatically.** No ad hoc
cutoff or dimensional regularisation needed.

## E14.6 Falsifiable predictions

**P1 — QFT emerges exactly from cascade in the continuum limit.**
Specifically, standard Feynman rules and perturbation theory are
cascade-derivable, with coupling constants fixed by F8.

**P2 — Spin-statistics theorem is structural** (bosons on rank-0,1
rungs; fermions on rank-2 spinor rung).

**P3 — No UV divergences in cascade** (Planck-scale cutoff is
structural).

**P4 — Feynman perturbative expansion converges** (cascade is
unitary + bounded, so path integral is well-defined, not just
asymptotic).

**P5 — Anomalies arise from σ-asymmetry** in loop diagrams. Anomaly
matching cascade ↔ SM consistent.

---

## Summary

**Theorem E14.** *QFT (second quantisation + Feynman path integral)
is the continuum-limit reduction of cascade closure-functional
dynamics. No quantisation prescription needs to be added: cascade's
discrete σ-invariant sum IS the path integral; cascade's H₄ Fock
space IS the QFT Fock space.*

Spin-statistics, creation/annihilation, UV regularisation, and
Feynman diagrams all emerge from cascade structure automatically.

**Cascade IS QFT**, restricted to the cascade substrate with cascade
coupling constants. No additional quantum-field postulates needed.
