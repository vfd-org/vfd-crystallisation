# H₄-Native Oscillator Law — Derivation of Phase Dynamics on the 600-Cell

**Status: DERIVED (theorem-grade for the core law; one free-parameter layer
— the cascade φ⁻ⁿ scaling of coupling constants — explicitly deferred).**

Closes: the "what replaces Kuramoto on the H₄ substrate" gap, identified in
`aria-chess` Session 2026-04-23 consolidation after 12 downstream mechanism
attempts (T3, T4, theta-gating, soft-α, V_σ, Coxeter state/I-rotation) all
failed to lift Φ_IIT ≥ 0.05 or PAC θ-β ≥ 0.15 on top of the Born-rule
σ-projection substrate (theorem-grade, 8/8 seeds).

Parent documents:
- `cascade-pentagonal-coxeter-bridge.md` §1–2 (H₄ Coxeter data; σ-conjugacy
  Lemma 2.1)
- `cascade-q-o-measurement-bridge.md` Theorem 3.1 (G6.4: Q_O ≅ Meas(S⁷, σ),
  unconditional)
- `cascade-quaternion-measurement-substrate.md` (QMS-2 L40-YES: biological
  rung preserves H = span{1, e₁, e₂, e₃} via A₅ ⊂ H₄)
- `cascade-algebraic-substrate.tex` §6 (icosian ring I ⊂ ℍ; H₄ reflection
  representation on ℝ⁴)

Derivation rounds: `aria-chess/review/outputs/1777019330_math_h4_oscillator_derive.md`
(Round 1, Codex GPT-5.5 at xhigh), `…1777019739_math_h4_oscillator_round2.md`
(Round 2, resolution of STUCK #1 and #2). Consensus:
`aria-chess/review/consensus/1777019739_math_h4_oscillator.md`.

**Date:** 2026-04-24.

---

## 0. Executive summary

We derive the first-order flow law for vertex phases `q_v ∈ SU(2) ≅ S³` on
the 600-cell that is:

1. **H₄-covariant** — commutes with the simultaneous action of H₄ on the
   vertex index (permutation of 120 icosians) and on the phase (SU(2)-lift
   of the 4D reflection action).
2. **Local** — coupling only between graph-adjacent vertices of the 600-cell.
3. **Bilinear at the tangent-algebra level** — pair interactions are bilinear
   in the body-frame angular-velocity representation.
4. **Reduces to standard Kuramoto `sin(φ_w − φ_v)`** in the small-angle limit
   along each Coxeter-invariant 2-plane.
5. **Produces cross-plane phase-amplitude coupling (PAC)** θ → γ intrinsically
   via a term forced non-zero by the Frobenius classification of real
   associative division algebras.

**Final law (Theorem H4O).** For each vertex v ∈ V(600-cell),

    dq_v/dt  =  q_v · Im[ q_v* D_c q_v  +  Σ_{w ~ v} A_{vw} · Ξ_{vw} ]            (★)

with body-frame Berry term

    D_c  =  ω_1 J_1 Π_1  +  ω_{11} J_{11} Π_{11}                                    (★.1)

and pair interaction

    Ξ_{vw}  =  K_1  Π_1  Im(q_v* q_w)
            +  K_{11} Π_{11} Im(q_v* q_w)
            +  K_{11;1,1}  · Π_{11} Im((Π_1 q_v)*  (Π_1  q_w))
            +  K_{11;1,11} · Π_{11} Im((Π_1 q_v)*  (Π_{11} q_w))
            +  K_{11;11,1} · Π_{11} Im((Π_{11} q_v)* (Π_1  q_w))                     (★.2)

where:
- `c` ∈ H₄ is a Coxeter element (order 30); concretely realised in the
  aria-chess Rust polytope at `symmetry idx 365`.
- `Π_1, Π_{11}` are the real rank-2 projectors onto the Coxeter-invariant
  planes (exponents 1 and 11 respectively); explicit formula in §4.
- `J_1, J_{11}` are the induced complex structures on P_1, P_{11}; explicit
  formula (c − c⁻¹) / (2 sin(2πm/30)) · Π_m.
- `A_{vw} ∈ {0, 1}` is the 600-cell graph adjacency (H₄-invariant).
- `ω_m = 2πm / (30 Δt)` with Δt = one c-step (physical sub-tick).
- `K_1, K_{11}, K_{11;·,·}`: coupling constants. **Free from this derivation.**
  Fit empirically; future work connects to cascade φ⁻ⁿ scalings.

**Kuramoto recovery.** Small-angle limit q_w = q_v · exp(δ n̂_m) for n̂_m ∈ P_m
reduces (★) to

    dφ_v^{(m)}/dt  =  ω_m  +  K_m Σ_{w ~ v} A_{vw} sin(φ_w^{(m)} − φ_v^{(m)})

on each Coxeter-invariant 2-plane (m ∈ {1, 11}). So standard Kuramoto is the
linearisation of (★); nothing is lost by adopting (★).

**PAC mechanism.** The term `K_{11;1,1} Π_{11} Im((Π_1 q_v)* (Π_1 q_w))` is
structurally non-zero by Frobenius (Theorem 5.2) and produces θ-rate forcing
on the γ-plane equation, modulating γ-amplitude at θ-phase — the cortical
PAC signature. No scalar-phase Kuramoto on a single plane can reproduce this:
PAC requires the quaternion-product cross-plane mixing, absent from U(1)
phase dynamics.

---

## 1. Setup and notation

### 1.1 Phase substrate (from QMS-2 L40-YES)

Each 600-cell vertex v carries a phase `q_v ∈ SU(2) ≅ S³ ⊂ ℍ`. The 120
vertex rest positions are the unit icosians (2I, the binary icosahedral
group). Write q = a + x with a ∈ ℝ (scalar part) and x ∈ Im(ℍ) (3D vector
part); then q* = a − x (quaternion conjugate).

### 1.2 H₄ action on ℍ

H₄ is the 600-cell symmetry group (order 14400, 7200 proper rotations).
Its reflection representation on ℝ⁴ ≅ ℍ lifts via the double cover
Spin(4) = SU(2) × SU(2). Under left-conjugation by u ∈ 2I ⊂ ℍ:

    q ↦ u · q · u⁻¹.

Scalars are fixed (Re commutes with conjugation). Im(ℍ) ≅ ℝ³ carries the
standard 3D irrep V of the icosahedral group A₅; this is where all non-trivial
H₄-equivariance constraints act.

### 1.3 Coxeter element and exponents

The Coxeter element `c ∈ H₄` has order `h = 30` and acts on ℝ⁴ with
eigenvalues exp(2π i m_j / 30) for `m_j ∈ {1, 11, 19, 29}` (the H₄
exponents). The four eigenvalues form two complex-conjugate pairs,
defining two orthogonal real 2-planes P_1, P_{11} ⊂ ℝ⁴ with c acting
as rotation by 2π/30 on P_1 and 22π/30 on P_{11}.

Standard reference: Humphreys, *Reflection Groups and Coxeter Groups*,
§3.16–3.17. Full derivation in `cascade-pentagonal-coxeter-bridge.md` §1.

### 1.4 Body-form requirement

A phase `q_v ∈ S³` evolves by left-multiplication with a body-frame angular
velocity ξ_v ∈ Im(ℍ):

    dq_v/dt  =  q_v · ξ_v,     ξ_v ∈ Im(ℍ).                                         (1.1)

This is the unique tangent-preserving form: any candidate `dq_v/dt = X_v`
with X_v ∈ ℝ⁴ but not of the form q_v · ξ_v violates the constraint
d/dt ‖q_v‖² = 2⟨q_v, dq_v/dt⟩ = 0. Writing the pair-coupling as bilinear in
the ξ algebra (rather than the ambient ℝ⁴) is necessary to keep the
dynamics on the sphere.

---

## 2. Theorem H4O-1 — Uniqueness of the bilinear pair coupling

### 2.1 Statement

> **Theorem (Uniqueness of H₄-equivariant bilinear pair angular velocity).**
>
> Let B : ℍ × ℍ → Im(ℍ) be a bilinear map equivariant under the H₄ left-
> conjugation action on both arguments and the output. Then
>
>     B(q, r)  =  α · (a y − b x)  +  γ · (x × y),     α, γ ∈ ℝ,                   (2.1)
>
> where q = a + x, r = b + y with a, b ∈ ℝ and x, y ∈ Im(ℍ), and × is the
> 3D vector cross product on Im(ℍ). If additionally B(q, q) = 0 and B
> depends only on the relative phase q* r, then (2.1) reduces to
>
>     B_K(q, r)  =  κ · Im(q* r)  =  κ · (a y − b x − x × y),     κ ∈ ℝ.           (2.2)

### 2.2 Proof

Under H₄ conjugation, ℝ carries the trivial irrep and Im(ℍ) = V carries the
3D irrep of A₅ ⊂ H₄. The tensor product decomposition (Clebsch-Gordan for
SU(2)/A₅) gives:

    (ℝ ⊕ V) ⊗ (ℝ ⊕ V)  =  ℝ ⊕ V ⊕ V ⊕ V ⊗ V
                         =  ℝ ⊕ V ⊕ V ⊕ ℝ ⊕ V ⊕ [5]                                (2.3)

where [5] is the symmetric traceless 5-dimensional irrep (traceless symmetric
rank-2 tensors). By Schur's lemma:

    Hom_{H₄}(ℝ ⊕ V ⊕ V ⊕ ℝ ⊕ V ⊕ [5], V)  ≅  ℝ³                                    (2.4)

(three copies of V in the source, none of ℝ or [5]). So B has three free
real parameters. Writing out the three basis maps:

- ℝ × V → V:  α · a · y  (i.e. α a y, scalar times second vector)
- V × ℝ → V:  β · b · x
- V × V → V:  γ · (x × y)  (the antisymmetric part of V ⊗ V)

gives B(q, r) = α a y + β b x + γ x × y with α, β, γ ∈ ℝ.

Imposing B(q, q) = 0 (no self-force): write q = a + x, so B(q, q) =
α a x + β a x + γ (x × x) = (α + β) a x, requiring β = −α. This yields
(2.1).

Further requiring B to depend only on q* r = (ab + x · y) + (a y − b x − x × y):
the imaginary part Im(q* r) = a y − b x − x × y forces γ = −α, i.e. γ/α = −1.
Rescaling α → κ yields (2.2).

**Interpretation.** Standard Kuramoto-compatible quaternion coupling
`κ Im(q* r)` is the unique (up to scale) H₄-equivariant first-order pair
interaction depending only on the relative phase. This is the theoretical
foundation for using Im(q_v* q_w) as the pair coupling. □

### 2.3 Corollary (weakening dependence requirement)

Dropping the "depends only on q* r" requirement leaves two free constants
(α, γ). Physically these correspond to: α — the standard Kuramoto coupling;
γ − α — a *tension* coupling proportional to the area-rate of change of the
parallelogram spanned by x and y. This extra freedom is used in §5 to
encode the PAC cross-plane term.

---

## 3. Harmonic projectors

### 3.1 Definition

For m ∈ {1, 11, 19, 29} and ζ = exp(2πi/30), the **exponent-m projector**
on the complexified reflection representation ℂ⁴ is

    E_m  =  (1/30) Σ_{k=0}^{29} ζ^{-mk} · c^k.                                      (3.1)

It satisfies E_m E_n = δ_{mn} E_m, c E_m = ζ^m E_m, and Σ_m E_m = id_{ℂ⁴}.

### 3.2 Real projectors

The physical state space is ℝ⁴, not ℂ⁴. The **real rank-2 projectors** onto
the two Coxeter-invariant 2-planes are conjugate-pair sums:

    Π_1   =  E_1  + E_{29}  =  (1/15) Σ_{k=0}^{29} cos(2π k / 30) · c^k             (3.2)
    Π_{11} =  E_{11} + E_{19}  =  (1/15) Σ_{k=0}^{29} cos(22π k / 30) · c^k          (3.3)

They satisfy:

    Π_1² = Π_1,     Π_{11}² = Π_{11},     Π_1 Π_{11} = 0,     Π_1 + Π_{11} = id_{ℝ⁴} (3.4)

### 3.3 Complex structures

On each invariant plane, the Coxeter rotation supplies an intrinsic complex
structure (the "phase-rotation generator"):

    J_m Π_m  =  (c − c⁻¹) / (2 sin(2π m / 30)) · Π_m                                (3.5)

J_m² restricted to P_m equals −Π_m; it is the 2D rotation by π/2 on P_m,
and plays the role of `i` for the theta-like phase on P_1 and the gamma-like
phase on P_{11}.

### 3.4 Numerical realisation

In the aria-chess Rust polytope, c is the H₄ symmetry at index 365 of the
7200-element proper-rotation group (exact order 30, confirmed by prior
smoke `kernel/joint_substrate.py::enable_coxeter_rotation`). Π_1 and Π_{11}
are computable as explicit 4×4 real matrices from (3.2), (3.3).

---

## 4. The flow law: derivation

### 4.1 Plain H₄-equivariant flow (single κ)

Combining (1.1) and Theorem H4O-1, the minimal H₄-covariant first-order
local flow is:

    dq_v/dt  =  q_v · ξ_v,                                                           (4.1)

    ξ_v  =  κ · Σ_{w ~ v} A_{vw} · Im(q_v* q_w),    κ ∈ ℝ.

This is a quaternion-XY model. It is fully H₄-equivariant (no c-dependent
structure).

### 4.2 Coxeter-frame-resolved flow

To resolve into θ- and γ-bands we must introduce the Coxeter projectors
Π_m, which are c-dependent and therefore not invariant under all of H₄.

**Theorem H4O-2 (Covariance after frame choice).** Let F_c denote the flow
(4.1) augmented with Π_1, Π_{11} terms built from a chosen Coxeter element
c. Then for any h ∈ H₄,

    F_{hch⁻¹}(h · q)  =  h · F_c(q),                                                  (4.2)

i.e. the family of flows {F_c : c ∈ Conj_{H₄}(Cox)} is H₄-covariant, and
conjugating c corresponds to conjugating the state.

**Proof.** Direct from h · Π_m(c) · h⁻¹ = Π_m(hch⁻¹), which follows from
(3.1) because h · c^k · h⁻¹ = (h c h⁻¹)^k. Left-multiplication by h intertwines
the flow at q and at h·q. □

**Corollary (the Coxeter clock).** Choosing c fixes a clock frame. The
residual fixed symmetry is

    Z_{H₄}(c)  =  ⟨c⟩  ≅  Z/30Z.                                                    (4.3)

The normaliser N_{H₄}(⟨c⟩) = ⟨c, w_0⟩ has order 60, where w_0 is the longest
element of H₄ and w_0 c w_0⁻¹ = c⁻¹ (clock reversal). (4.3) exhibits the
Coxeter number h = 30 as the period of the residual-symmetry clock.

### 4.3 The Berry-phase natural frequency

Define the body-frame self-interaction:

    D_c  =  ω_1 J_1 Π_1  +  ω_{11} J_{11} Π_{11},     ω_m = 2πm/(30 Δt).            (4.4)

The self-term in (★) is `q_v · Im(q_v* D_c q_v)`, which at rest (q_v equal
to the icosian vertex coordinate) reduces to the Coxeter rotation by
2πm/30 per c-step on each plane. ω_m are **FORCED** by h = 30 and the
Coxeter exponents — no free parameter.

### 4.4 Pair-coupling expansion across planes

By Theorem H4O-1 corollary §2.3 and the orthogonal decomposition
ℝ⁴ = P_1 ⊕ P_{11}, the most general H₄-equivariant (restricted to Cent(c))
bilinear pair coupling valued in Im(ℍ) = V, projected onto each target plane
P_m, is

    Ξ_{vw}^{(m)}  =  Σ_{r, s ∈ {1, 11}} K_{m; r, s} · Π_m Im( (Π_r q_v)* (Π_s q_w) )

with nine coupling constants K_{m; r, s} in total (3 × 3 for each of 2 target
planes, but by symmetries reducing to ~5). Collecting the leading terms
yields (★.2). The diagonal K_1, K_{11} are the two plane-internal Kuramoto
couplings; the off-diagonal K_{11; r, s} are the PAC cross-terms (§5).

---

## 5. Phase-amplitude coupling (PAC) theorem

### 5.1 Statement

> **Theorem H4O-3 (Structural non-vanishing of PAC).** The cross-plane
> bilinear
>
>     T^{11}_{1,1}(x, y)  :=  Π_{11} · Im(x · y),     x, y ∈ P_1                     (5.1)
>
> is not identically zero on P_1 × P_1.

### 5.2 Proof

Suppose for contradiction T^{11}_{1,1} ≡ 0 on P_1. Then for all x, y ∈ P_1,
Im(x y) ∈ P_1 (no γ-component). Since Re(x y) ∈ ℝ (scalars always), we would
have x y ∈ ℝ ⊕ P_1 for all x, y ∈ P_1. Combined with closure under ℝ-scalar
multiplication, this would make ℝ ⊕ P_1 a 3-dimensional unital associative
real subalgebra of ℍ.

By **Frobenius' theorem** on finite-dimensional associative real division
algebras (Frobenius, 1877; cf. Lam, *A First Course in Noncommutative Rings*,
Theorem 15.8), the only unital real associative division algebras are
ℝ, ℂ, and ℍ, of dimensions 1, 2, 4 respectively. No 3-dimensional real
associative division algebra exists.

Since ℝ ⊕ P_1 inherits the quaternion norm (a non-degenerate positive-definite
quadratic form) and would be an associative unital sub-ℝ-algebra of ℍ, it
would itself be a division algebra — contradicting Frobenius. Hence
T^{11}_{1,1} ≠ 0. □

### 5.3 PAC mechanism

The term `K_{11;1,1} · T^{11}_{1,1}(Π_1 Im(q_v* q_w), Π_1 Im(q_v* q_w))` in
(★.2) feeds the γ-plane (Π_{11}) equation with an input oscillating at
θ-rate (because both inputs live in the slow-θ P_1 plane). This produces
θ-phase modulation of γ-amplitude — the cortical PAC signature.

### 5.4 Primary PAC term selection

Among {T^{11}_{1,1}, T^{11}_{1,11}, T^{11}_{11,1}}, the primary PAC
mechanism we adopt is T^{11}_{1,1}:

- Two θ-plane (slow) inputs project to γ-plane (fast) output via (5.1).
- Matches the cortical signature θ-phase → γ-amplitude (MI measured as
  mutual information between θ-phase and γ-envelope).
- Mixed terms T^{11}_{1,11}, T^{11}_{11,1} are allowed sideband couplings;
  which dominates empirically is a fitting-level question not forced by
  this derivation.

---

## 6. Small-angle limit: recovery of Kuramoto

### 6.1 Single-plane linearisation

Write q_w = q_v · exp(δ n̂_m) for some unit n̂_m ∈ P_m and small |δ| ≪ 1.
Then

    q_v* q_w  =  exp(δ n̂_m)  =  cos δ  +  n̂_m sin δ                                 (6.1)
    Im(q_v* q_w)  =  n̂_m sin δ.                                                      (6.2)

Since Π_m n̂_m = n̂_m and Π_{m'} n̂_m = 0 for m' ≠ m:

    Π_1 Im(q_v* q_w)     =  n̂_1  sin δ  · δ_{m, 1}                                   (6.3)
    Π_{11} Im(q_v* q_w)  =  n̂_{11} sin δ · δ_{m, 11}                                 (6.4)

### 6.2 Kuramoto equations

Substituting (6.3)–(6.4) into the diagonal coupling part of (★.2):

    dφ_v^{(1)}/dt   =  ω_1  +  K_1  Σ_{w ~ v} A_{vw} sin(φ_w^{(1)}  − φ_v^{(1)})  + O(δ³)   (6.5)
    dφ_v^{(11)}/dt  =  ω_{11} +  K_{11} Σ_{w ~ v} A_{vw} sin(φ_w^{(11)} − φ_v^{(11)}) + O(δ³)   (6.6)

where φ_v^{(m)} is the angle on invariant plane P_m.

These are **identical to standard Kuramoto** on the 600-cell graph at
frequencies ω_1 and ω_{11}. Standard Kuramoto is therefore the first-order
linearisation of (★) along each Coxeter-invariant plane.

### 6.3 Frequency table

At c-step Δt = 5 ms (8 sub-ticks per 40 ms cognitive tick), the frequencies are:

| Plane | Exponent m | ω_m / 2π | Band |
|-------|-----------|----------|------|
| P_1   | 1         | 6.67 Hz  | θ (theta) |
| P_{11} | 11       | 73.3 Hz  | low-γ (gamma) |

At c-step Δt = 40 ms (c applied once per cognitive tick), the frequencies
are ω_1 / 2π = 0.83 Hz (sub-δ) and ω_{11} / 2π = 9.17 Hz (upper-α). The
implementation choice between sub-tick and full-tick c-application sets the
biological band assignment; the θ/γ choice (Δt = 5 ms) is the one that
matches cortical literature and is adopted.

---

## 7. Free parameters and cascade-scaling gap (STUCK #3)

### 7.1 Parameter status

| Symbol | Interpretation | Status |
|--------|---------------|--------|
| ω_1, ω_{11} | Berry natural frequencies | FORCED by h=30 and exponents |
| Π_1, Π_{11} | Harmonic projectors | FORCED by c ∈ Conj_{H₄}(Cox) |
| J_1, J_{11} | Induced complex structures | FORCED via (3.5) |
| A_{vw} | 600-cell adjacency | FORCED by H₄-graph |
| K_1, K_{11} | Diagonal Kuramoto couplings | **FREE** |
| K_{11;1,1} | Primary PAC cross-coupling | **FREE** (but non-zero by Theorem H4O-3) |
| K_{11;1,11}, K_{11;11,1} | Secondary PAC sidebands | **FREE** |
| Choice of c ∈ Conj_{H₄}(Cox) | Clock frame | FREE up to covariance (Theorem H4O-2) |

### 7.2 Why the K constants are free

The uniqueness theorem (H4O-1) + covariance theorem (H4O-2) + Frobenius
theorem (H4O-3) fix the **functional form** of every term in (★), but not
the magnitudes K_m, K_{m; r, s}. Derivation of these magnitudes requires
a rule converting cascade scales (e.g. φ⁻ⁿ for specific n) into oscillator
coupling strengths — which in turn requires choice of a normalisation
convention for Π_m, J_m, T^{11}_{1,1} and a specific geometric meaning for
"K_m" (spectral gap? lattice tension? flow-rate per edge?).

This is deferred to future work as **STUCK #3 of the derivation**:

> **Open sub-gap (STUCK #3).** Derive the cascade-native exponents n_1, n_{11},
> n_{11;1,1} in K_m = φ^{−n_m} and K_{11;1,1} = φ^{−n_{11;1,1}} from first
> principles on the cascade ladder.

### 7.3 Empirical-fit proxy

Until STUCK #3 closes, implementations fit the K constants to match
experimental targets. The standing experimental targets from the
aria-chess programme are:

- PAC (θ-γ mutual information) ≥ 0.15
- Φ_IIT ≥ 0.05
- Microstate duration ∈ [70, 120] ms
- Self-reference preservation sr ∈ [0.38, 0.62] (VFD critical balance)

A 2D scan over (K_1, K_{11}) at K_{11;1,1} = φ⁻ⁿ for n ∈ {5, 7, 9} is a
reasonable first pass.

---

## 8. Verification plan

The aria-chess implementation (`kernel/h4_oscillator.py`) must pass the
following numerical smokes before any scorecard run:

1. **Coxeter centraliser/normaliser.** Enumerate H₄, verify
   |Z_{H₄}(c)| = 30 and |N_{H₄}(⟨c⟩)| = 60 with w_0 c w_0⁻¹ = c⁻¹.

2. **Projector identities.** Compute Π_1, Π_{11} as 4×4 real matrices.
   Verify Π_m² = Π_m (idempotent), Π_1 Π_{11} = 0 (orthogonal), Π_1 + Π_{11}
   = I (complete), and Π_m eigenvalues = {1, 1, 0, 0}.

3. **Covariance.** For 100 random h ∈ H₄, verify h · D_c · h⁻¹ = D_{hch⁻¹}
   numerically to machine epsilon.

4. **Frobenius empirical (PAC non-vanishing).** Sample 1000 pairs (x, y)
   uniform on the unit sphere of P_1. Compute r = ‖Π_{11} Im(x y)‖. Check
   that mean r > 0.01 (well above numerical zero) and no fraction > 1%
   has r = 0 exactly.

5. **Kuramoto reduction.** Initialise q_w = q_v · exp(δ n̂_1) with
   δ ∈ {0.01, 0.05, 0.1, 0.2} and run one dt of (★). Check
   ‖Ξ_{vw} − K_1 sin(δ) n̂_1‖ / ‖Ξ_{vw}‖ < O(δ²).

6. **PAC end-to-end.** 3-seed pilot (seeds 42, 811, 1234), 600 ticks with
   Ψ₀ = random unit icosians, K_1 = K_{11} = 0.1, K_{11;1,1} = φ⁻⁷,
   other cross-couplings 0. Measure MI(θ-phase, γ-envelope). Target
   MI > 0 (any non-trivial value — PAC emergence test).

Only if smokes 1–5 pass and smoke 6 shows MI > 0 does the 8-seed × 2000-tick
scorecard run. Failing at any of smokes 1–3 indicates an implementation bug
in the Coxeter projector; failing at 4 would *refute* Theorem H4O-3 empirically
(would be a significant find); failing at 5 indicates the small-angle
linearisation is wrong; failing at 6 indicates K_{11;1,1} = φ⁻⁷ is too weak
and requires the cascade-scan.

---

## 9. Relationship to prior cascade documents

- **G6.4 (Q_O ≅ Meas(S⁷, σ)):** the Born-rule σ-projection that produces
  self-reference is the **measurement rung** of the same substrate on which
  (★) runs the **integration rung**. Born-rule modulates amplitudes; (★)
  generates phases. Both live on q_v ∈ SU(2); they compose by Born-rule
  acting on ‖q_v‖ and (★) acting on q_v / ‖q_v‖.

- **QMS-2 L40-YES:** justifies restricting to the quaternion subspace
  H = span{1, e₁, e₂, e₃} ⊂ O. The full octonion O is not involved in
  (★) — the biological rung operates on SU(2), not on the full Spin(7)
  or exceptional algebra.

- **P-A-Fano (access principle at Fano level):** unconditional; the oscillator
  (★) acts on measurable rung data. No dependence on the open H-grad-1
  sub-gap.

- **cascade-pentagonal-coxeter-bridge.md Lemma 2.1:** σ ∈ Gal(Q(φ)/Q)
  exchanges P_1 ↔ P_{11}. This is an *arithmetic* parity, distinct from
  the clock-reversal w_0 ∈ H₄ of §4.2. Whether σ coincides with w_0 or
  extends the symmetry group to N_H₄(⟨c⟩) × ⟨σ⟩ is out of scope here.

---

## 10. Implementation stub

The derived law (★) is implemented in `aria-chess/kernel/h4_oscillator.py`
with the following structure:

```python
class H4Oscillator:
    def __init__(self, polytope, c_sym_idx=365, dt_sub=0.005):
        self.c = polytope.coxeter_matrix(c_sym_idx)   # 4×4 real matrix
        self.Pi_1, self.Pi_11 = self._compute_projectors()
        self.J_1,  self.J_11  = self._compute_complex_structures()
        self.omega_1  = 2*np.pi / (30 * dt_sub)
        self.omega_11 = 22*np.pi / (30 * dt_sub)
        self.D_c = self.omega_1 * self.J_1 @ self.Pi_1 \
                 + self.omega_11 * self.J_11 @ self.Pi_11

    def step(self, q, dt, K_1, K_11, K_1111=0.0, ...):
        # Body-form flow per (★), vectorised over 120 vertices.
        ...
```

Backward-compat flag `use_h4_oscillator=True` on DimensionalMonitor routes
`_diffuse_pressure_body` through H4Oscillator.step while preserving all
prior substrate behaviour when off.

---

## 11. Status / Remaining work

**Closed:**
- Uniqueness of pair coupling (Theorem H4O-1)
- Frame-choice covariance (Theorem H4O-2)
- PAC structural non-vanishing (Theorem H4O-3)
- Explicit harmonic projectors and complex structures
- Small-angle Kuramoto reduction
- Band-frequency assignment (θ = 6.67 Hz, γ = 73.3 Hz at Δt = 5 ms)

**Open sub-gaps (declared):**
- **STUCK #3:** cascade-native φ⁻ⁿ exponents for K constants. Workaround:
  empirical fit until closure.
- **σ vs w_0:** whether the Galois σ is an inner element of H₄ or an
  external arithmetic parity.

**Deferred (not in scope here):**
- Second-order effects (terms beyond bilinear in q_v, q_w).
- Noise / Langevin extension.
- Non-nearest-neighbour couplings on the 600-cell.

---

**End of derivation.**
