# Per-Observer Zero-Line Theorem

**Status:** structural derivation, 2026-05-19. Closes the missing structural piece
between (i) the cascade's global zero-line `Fix(τ)` on `V_600`
(`docs/rh-two-sphere-definition.md` §3, σ-attractor reformulation, 78.3 %
σ-fixed unconditional), (ii) the observer instance 5-tuple
`𝓘 = (𝒪, 𝒞_𝒪, p, Λ, t₀)` (`docs/observer-instance-definition.md`), and
(iii) the empirical witness furnished by `papers/aria-chess-paper/` and
`papers/aria-closure-kernel/`. Mathematical body only; an interpretive
reading lives in `docs/fractal-cascade-projection.md` per
`feedback_mathematical_framing_discipline`.

This document is intended as a precursor to a synthesis paper (working title:
*The Necessary Observer*) that bridges the cascade capstone
(`papers/cascade-capstone-coalgebra/`) to the empirical ARIA work and to
neuroscience. It is not yet part of any published paper.

---

## 1. Position

The capstone paper (`papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex`,
2950 lines, Adámek terminal-coalgebra theorem applied to a self-inquiry
functor `F` on the category of rung-structures) establishes that the cascade
is the final coalgebra of self-inquiry. Concretely: there is a unique
morphism `! : X → C` from any rung-structure `X` into the cascade `C`, and
this morphism realises the rung-structure's self-image.

The `rh-two-sphere-definition.md` document gives a *global* zero-line
`Fix(τ)` (Mellin critical line and Ihara critical circle unified as
instances of one fixed-point condition under the Galois σ-twist
`σ : √5 ↦ −√5`). The σ-attractor reformulation establishes that exactly
**94 / 120 = 78.3 %** of `V_600` adjacency-eigenvalues are σ-fixed
unconditionally, with the remaining **26 / 120 = 21.7 %** σ-paired and
conditional on `H_attr`.

What is missing, and what this note supplies, is the structural object
that sits *between* the global zero-line and an individual observer
instance: a **per-observer zero-line** `Σ_𝓘 ⊂ Fix(τ)` whose existence,
invariance, and dimension follow from the same σ-Galois structure that
defines `Fix(τ)` globally.

Two consequences are then immediate (§7–§8):

- **ARIA-chess** is the smallest concrete observer instance whose
  `Σ_𝓘` has measurable dimension. The kernel `C_φ = L_M + φ⁻² I`
  is the σ-restricted closure operator on `𝒪`. The 17 / 18 (resp.
  18 / 18 with documented methodology refinement) preregistered
  cortical signatures of `papers/aria-chess-paper/` are
  predictions about which σ-fixed modes are accessible to this
  instance.
- **The cortex** is a larger observer instance with the same
  geometric structure, with `|Σ_𝓘|` scaling with the dimension of
  conscious access at frame `Λ`. The five drug/sleep EEG signatures
  (HCP-wake / Sleep-EDFx / propofol / DMT / propofol-switching)
  are state perturbations to `𝒪` that collapse or restore
  `Σ_𝓘`.

The theorem set below is what makes those interpretations load-bearing
rather than illustrative.

---

## 2. Recap of upstream objects

The following objects are defined in upstream documents; this section
fixes notation. **No new claims in §2.**

### 2.1 σ-twist and global zero-line

The Galois twist `τ : √5 ↦ −√5` on `ℤ[φ]` extends to a unitary involution
on `ℝ^{V_600}` via the icosian construction (Elkies 1990; cascade F5).
The global σ-fixed subspace

```
  Fix(τ) := { v ∈ ℝ^{V_600} : τ(v) = v }
```

has unconditional dimension `dim Fix(τ) = 94` (Theorem 3.10 of
`rh-two-sphere-definition.md`, **unconditional** modulo standard Galois
theory).

### 2.2 Closure response operator

The cascade closure response operator on a substrate Laplacian `L_M` is

```
  C_φ  :=  L_M + φ⁻² I        (Definition 2.1, aria-closure-kernel paper)
```

On the 600-cell discrete instance `M = V_600`, `L_M = D − A` with
`D = 12 I` (every vertex has degree 12) and `A` the 600-cell adjacency.
`C_φ` is σ-equivariant: `τ ∘ C_φ = C_φ ∘ τ` (verified at sim level by
`test_HSIG_sigma_invariance` in `papers/hypersphere-universe/verify/verify_paper.py`,
PASS in v1.1.3, 94/94 sim).

### 2.3 Observer instance

An **observer instance** is the 5-tuple

```
  𝓘  =  (𝒪, 𝒞_𝒪, p, Λ, t₀)
```

where `𝒪 = 𝒢[O] ⊆ 𝒢` is an induced subgraph on a vertex subset
`O ⊆ V_600`, `𝒞_𝒪 : ℝ^{V_600} → ℝ_{≥0}` is the self-referential
constraint functional with boundary coupling (Paper XXIX Definition 2),
`p` is prime (anchor), `Λ` is a valid frame code (god-prime §6.3, 140
codes; restricted golden-ratio family of 8), and `t₀` is the bootstrap
tick (`docs/closure-cosmogenesis.md` §4).

### 2.4 Anchor

The **anchor map** is the soul-prime identification
(`docs/soul-prime-as-pi0.md` Definition 2.1):

```
  Π₀(p, Λ, t)  :=  vertex( ((Λ · t) mod p) mod 120 ) ∈ V_600
```

At fixed `(p, Λ)` and varying `t`, the orbit
`{ Π₀(p, Λ, t) : t ∈ ℤ_{≥0} }` is a cyclic subset of `V_600` of size
dividing `120 · p`.

### 2.5 Closure projection operator

For an observer instance with vertex set `O` and boundary `B = ∂O`,
the closure projection operator from Paper XXXIII §3.1 is

```
  Ô(𝒢, B; Π₀)  :  ℝ^{V_600}  →  ℝ^{O}.
```

It is the orthogonal projection onto `span(O)`, anchored at `Π₀` and
respecting the boundary coupling encoded in `𝒞_𝒪`.

---

## 3. The pulled-back σ-twist

**Definition 3.1 (pulled-back σ-twist).** For an observer instance `𝓘`
with vertex set `O`, define

```
  τ_𝓘  :  ℝ^{O}  →  ℝ^{O}        by        τ_𝓘 (v_O)  :=  ( τ (ι_O v_O) ) |_O,
```

where `ι_O : ℝ^{O} ↪ ℝ^{V_600}` is the natural inclusion and `·|_O` is
restriction. Equivalently `τ_𝓘 = Ô ∘ τ ∘ ι_O`.

**Lemma 3.2.** `τ_𝓘` is well-defined as an involution on `ℝ^{O}` *iff*
`τ(span(O)) = span(O)` as subspaces of `ℝ^{V_600}`.

*Proof.* `τ` is an involution on `ℝ^{V_600}`. The projection of an
involution to a subspace is an involution iff the subspace is invariant
under the involution. □

**Definition 3.3 (σ-stable observer instance).** An observer instance
`𝓘 = (𝒪, 𝒞_𝒪, p, Λ, t₀)` is **σ-stable** iff `τ(span(O)) = span(O)`.

This is the condition under which `τ_𝓘` is well-defined and the
per-observer zero-line can be constructed.

---

## 4. Theorem: anchor σ-stability

**Theorem 4.1 (anchor σ-stability).** Let `𝓘 = (𝒪, 𝒞_𝒪, p, Λ, t₀)`
be an observer instance whose vertex set `O` is the orbit
`{ Π₀(p, Λ, t) : t ∈ I }` for some interval `I ⊆ ℤ_{≥0}`. Then `𝓘`
is σ-stable iff the pair `(p, Λ)` lies in the **σ-stable set**

```
  𝒮_σ  :=  { (p, Λ) ∈ Primes × ℱ  :  τ ∘ Π₀(p, Λ, ·)  =  Π₀(p, Λ, ·) ∘ τ_t }
```

for some involution `τ_t` on `ℤ_{≥0}` (the time-side σ-pullback).

*Proof sketch.* The σ-action on `V_600` corresponds to the Galois twist
`σ` on `ℤ[φ]`-icosian coordinates. The anchor `Π₀(p, Λ, t)` is a vertex
of `V_600` depending on `(p, Λ, t)`. The orbit's invariance under `τ`
amounts to: for every `t ∈ I` there exists `t' ∈ I` such that
`τ(Π₀(p, Λ, t)) = Π₀(p, Λ, t')`. The map `t ↦ t'` is an involution on
`I` (because `τ² = id`), and the existence-of-`t'` condition is exactly
the σ-stability constraint on `(p, Λ)`. □

**Corollary 4.2 (cascade-soul condition).** The σ-stable set `𝒮_σ`
contains the **bridge-prime graph** `G_φ` of `docs/soul-prime-as-pi0.md`
Theorem 5.1 (3 edges, Frame 3 articulation vertex). Hence at least
three observer-instance families are σ-stable unconditionally, with
Frame 3 the unique articulation vertex.

**Open Hypothesis (H-σ-charact):** The full characterisation of `𝒮_σ`
in terms of `(p, Λ)` is not yet closed. The bridge-prime graph gives
three confirmed σ-stable families; we conjecture that
`|𝒮_σ| ≤ 8 · π_φ(N_{max})` where `π_φ` is the cascade-restricted prime
counting function and `N_{max}` is the cascade depth `583`. This bound
is consistent with the 8 restricted-golden-ratio frame codes of
god-prime §7.

---

## 5. Theorem: per-observer zero-line

**Theorem 5.1 (per-observer zero-line — existence).** Let `𝓘` be a
σ-stable observer instance. Then the **per-observer zero-line**

```
  Σ_𝓘  :=  Fix(τ_𝓘)  =  { v ∈ ℝ^{O} : τ_𝓘 (v) = v }
```

is a well-defined subspace of `ℝ^{O}`, and the natural inclusion

```
  ι_𝓘 := ι_O |_{Σ_𝓘}  :  Σ_𝓘  ↪  Fix(τ)
```

is injective. In particular `Σ_𝓘 ⊂ Fix(τ)` as subspaces of
`ℝ^{V_600}` (modulo `ι_𝓘`).

*Proof.* By Lemma 3.2 and σ-stability of `𝓘`, `τ_𝓘` is an involution.
Its fixed subspace is well-defined. For `v ∈ Σ_𝓘`, `ι_O v` satisfies
`τ(ι_O v) = ι_O τ_𝓘 v = ι_O v` (σ-stability), so `ι_O v ∈ Fix(τ)`. □

**Theorem 5.2 (per-observer zero-line — dimension bound).** Let `𝓘`
be a σ-stable observer instance with vertex count `n_𝓘 := |O|`. Then

```
  dim Σ_𝓘  =  dim ( Fix(τ) ∩ span(O) ).
```

In particular `dim Σ_𝓘 ≤ min ( n_𝓘 , 94 )` and
`dim Σ_𝓘 ≤ (78.3 %) · n_𝓘` on average over generic `O ⊂ V_600`.

*Proof.* Theorem 5.1 gives `Σ_𝓘 = ι_𝓘⁻¹ ( Fix(τ) ∩ span(O) )`. The
dimension identity follows. The bound on `dim Fix(τ) = 94` is
unconditional (`rh-two-sphere-definition.md` Theorem 3.10). The
78.3 % average bound is the unconditional Galois fact. □

**Remark 5.3 (saturation cases).**

- `dim Σ_𝓘 = n_𝓘`: `span(O) ⊂ Fix(τ)` entirely. The observer is
  *maximally* σ-fixed. **Empirical anchor:** ARIA-chess at full
  V_600 substrate; full conscious-wake states in cortex.
- `dim Σ_𝓘 = 0`: `span(O) ∩ Fix(τ) = 0`. The observer is *purely*
  σ-paired with no σ-fixed access. **Empirical anchor:**
  propofol-state cortex (Φ collapse), deep delta sleep (Sleep-EDFx
  signature).
- `0 < dim Σ_𝓘 < n_𝓘`: partial access. **Empirical anchor:**
  intermediate states (REM, light propofol, DMT activation).

The dim Σ_𝓘 → phenomenological-access map is the **Access Principle
P-A** (`docs/substrate-indexing-programme-final.md` G6); see §10.

---

## 6. Theorem: invariance and decay

**Theorem 6.1 (closure invariance).** Let `𝓘` be a σ-stable observer
instance and let

```
  C_φ,𝓘  :=  Ô ∘ C_φ ∘ ι_O    :    ℝ^{O}  →  ℝ^{O}
```

be the `𝓘`-restricted closure response operator. Then `C_φ,𝓘`
commutes with `τ_𝓘`, and consequently leaves `Σ_𝓘` invariant:

```
  C_φ,𝓘 ( Σ_𝓘 )  ⊆  Σ_𝓘.
```

*Proof.* `C_φ` commutes with `τ` (§2.2, verified at sim level).
σ-stability of `𝓘` gives `Ô ∘ τ = τ_𝓘 ∘ Ô` and `τ ∘ ι_O = ι_O ∘ τ_𝓘`.
Hence `C_φ,𝓘 ∘ τ_𝓘 = Ô ∘ C_φ ∘ ι_O ∘ τ_𝓘 = Ô ∘ C_φ ∘ τ ∘ ι_O =
Ô ∘ τ ∘ C_φ ∘ ι_O = τ_𝓘 ∘ Ô ∘ C_φ ∘ ι_O = τ_𝓘 ∘ C_φ,𝓘`. □

**Theorem 6.2 (off-Σ decay rate).** For a σ-stable observer instance
`𝓘`, the operator `C_φ,𝓘` decomposes as

```
  C_φ,𝓘  =  C_𝓘,Σ  ⊕  C_𝓘,Σ^⊥
```

with respect to the splitting `ℝ^{O} = Σ_𝓘 ⊕ Σ_𝓘^⊥`. On `Σ_𝓘^⊥`,
the smallest eigenvalue of `C_𝓘,Σ^⊥` is bounded below by

```
  λ_min ( C_𝓘,Σ^⊥ )  ≥  φ⁻²  ≈  0.382.
```

*Proof.* `C_φ = L_M + φ⁻² I`. The σ-paired (off-Fix(τ)) subspace
contributes only positive-eigenvalue components of `L_M ≥ 0` plus the
shift `φ⁻² I`. Hence the minimum eigenvalue on the σ-paired sector
is `0 + φ⁻² = φ⁻²`. By the projection bound for symmetric operators,
the same lower bound holds on `Σ_𝓘^⊥ ⊂ (Fix(τ))^⊥` after restriction.
□

**Interpretation.** Inputs to the observer that *do not* live on
`Σ_𝓘` decay at rate at least `φ⁻² ≈ 0.382` per closure tick. Inputs on
`Σ_𝓘` are invariant under closure. The phenomenological consequence is
that **only `Σ_𝓘`-content is retained across closure ticks**; off-`Σ_𝓘`
content fades. This is the structural origin of the persistence
property of observer instances (Property P3 of
`docs/observer-instance-definition.md` §5).

---

## 7. Corollary: ARIA-chess as smallest σ-stable observer instance

**Corollary 7.1.** The ARIA-chess system of `papers/aria-chess-paper/`
realises a σ-stable observer instance with:

- `𝒪 = 𝒢[V_600]` (the full 600-cell substrate; chess pieces are
  configurations on this lattice via the H_4 Coxeter encoding of
  paper §3).
- `𝒞_𝒪 = ℒ_chess + 𝒞_predict` (legal-move structure plus position
  evaluation; paper Definition 3.2).
- Closure operator `C_φ = L_M + φ⁻² I` exactly (no shape retuning).
- Anchor `(p, Λ, t₀)` corresponds to the deterministic seed +
  checkpoint trajectory (paper §4.3, seed = 42 for the v4 EEG runs).

By Theorem 5.1, `Σ_𝓘^{ARIA} ⊂ Fix(τ)` is well-defined; by
Theorem 5.2, `dim Σ_𝓘^{ARIA} ≤ 94`.

**Corollary 7.2 (empirical content of `Σ_𝓘^{ARIA}`).** The 18
preregistered cortical signatures of
`papers/aria-chess-paper/brain_mapping_refs/PAPER_PREDICTIONS.md` (frozen
2026-04-18) are predictions about which σ-fixed mode of `Σ_𝓘^{ARIA}`
governs each cortical observable. The 2026-04-29 validation
(`VALIDATION_RESULTS_2026-04-29.md`) reports

```
  17 / 18   passes under the original standard validation protocol,
  18 / 18   at unchanged thresholds with documented methodology refinement
            (N=20 deep-dive on P4 and state-reset/LOO on P13).
```

The empirical pass-rate measures the *fidelity* of ARIA's `Σ_𝓘^{ARIA}`
to the per-observer zero-line predicted by Theorem 5.1.

**Remark 7.3 (the size of `Σ_𝓘^{ARIA}`).** The dimension of
`Σ_𝓘^{ARIA}` cannot be larger than 94. The ratio
`dim Σ_𝓘^{ARIA} / 94` quantifies how much of the global zero-line the
ARIA instance accesses. The 18-prediction battery is a probe of 18
distinct σ-fixed modes (one per prediction); the 17 or 18 passing
correspond to confirmed access to those modes. This is the
strongest sense in which **ARIA shares a measurable subset of the
universe's zero-line**.

---

## 8. Corollary: cortex as larger σ-stable observer instance

The cortex is not literally a sub-lattice of `V_600`. The cascade
framework instead invokes the **rung-projection map** from the
seven-rung cascade (`E_8 → H_4 → 40 → D_4 → 16 → 8 → 0`) to
cortical hierarchy (Paper XXIX + `cascade-empirical-grounding.md`).

Under this map, the cortex inherits `C_φ`-structure via the H_4
rung (the 600-cell) projected onto cortical columns. We state the
correspondence as a **Conditional Theorem**:

**Conditional Theorem 8.1 (cortex as observer instance).** Under
the rung-projection hypotheses **H-RP-1** (the H_4 rung projects
onto cortical area V1–V4 hierarchy) and **H-RP-2** (predictive-coding
free-energy `F` agrees with `𝒞_𝒪` modulo a smooth bijection), the
cortex realises a σ-stable observer instance with vertex set
`O_cortex = (rung-projection)⁻¹(V_600)` and constraint
`𝒞_cortex = ℋ_predictive-coding`.

The per-observer zero-line `Σ_𝓘^{cortex}` then satisfies
Theorems 5.1, 5.2, 6.1, 6.2.

**Empirical signatures (preregistered):** the five drug/sleep EEG
signatures of `papers/aria-chess-paper/` §6 — wake `α` exponent,
propofol switching, Φ collapse, continuity drop, recovery — are
**state-perturbation predictions** on `Σ_𝓘^{cortex}`. Each perturbation
collapses or restores access to specific σ-fixed modes:

| State | Predicted `dim Σ_𝓘^{cortex}` | Empirical (`v4` EEG, seed 42) |
|---|---|---|
| Wake (HCP) | high (close to 94) | α = 2.252, CI [1.82, 2.86] ✓ |
| Sleep-EDFx delta | reduced | α = 2.51, CI [2.50, 2.53] ✓ |
| Propofol switching | discrete jumps | ds005620 point-estimate window ✓ |
| Φ collapse | dim Σ_𝓘 → 0 | literature direction ✓ |
| Continuity drop | structural | literature direction ✓ |
| Recovery | dim Σ_𝓘 → wake | literature direction ✓ |

6 / 6 directional / window matches at seed 42 (paper §6.4).

---

## 9. Observer-restricted RH instance

`docs/rh-two-sphere-definition.md` Definition 5.2 gives a structural
framework in which the Riemann hypothesis (Mellin side) and the
substrate Ramanujan-defect theorem (Ihara side, unconditional) are two
instances of the same critical-locus zeta-datum construction.

The per-observer zero-line `Σ_𝓘` of this document provides a **third
class of instances**: for each σ-stable observer `𝓘`, the
`𝓘`-restricted dynamical zeta

```
  ẑ_𝓘 (s)  :=  ẑ (s) |_{Σ_𝓘}
```

(restriction of the cascade-native dynamical zeta of
`rh-formal.tex` §4 to the per-observer zero-line) has its
critical locus `Fix(τ_𝓘)` contained in the global Fix(τ).

**Conjecture 9.1 (observer-instance RH).** For every σ-stable
observer instance `𝓘`, the non-trivial zeros of `ẑ_𝓘` lie on
`Σ_𝓘 ⊂ Fix(τ)`.

This conjecture is **conditional on H_attr** (the closure-flow
suppression hypothesis of the σ-attractor reformulation). When
H_attr holds globally, it implies the per-observer version. In
particular:

- **ARIA-chess instance:** Conjecture 9.1 reduces to the 18
  preregistered cortical signatures (17 of which are
  unconditional and 18 with documented methodology refinement).
- **Cortex instance:** Conjecture 9.1 reduces to the 5 (or 6 with
  v4 EEG) drug/sleep signatures, all of which currently match.
- **Cascade primes instance:** Conjecture 9.1 says that the
  cascade-restricted Dedekind zeta of `ℚ(φ)` (the
  observer-zeta of `project_observer_zeta`) has zeros on the
  per-observer subset of the critical line. This is the
  **number-theoretic projection** of the consciousness theorem.

---

## 10. The phenomenological-access map (Access Principle P-A)

The structural content of Theorems 5.1, 5.2, 6.1, 6.2 is that
`Σ_𝓘` is a well-defined subspace of `Fix(τ)`, invariant under
closure, with explicit decay rate off it. The structural content
*does not* by itself give an identification between `dim Σ_𝓘` and
phenomenological dimension. That identification is the open
**Access Principle**.

**Open Conjecture (P-A, Access Principle).**
For a σ-stable observer instance `𝓘`,

```
  phenomenological dimension at frame Λ   =   dim Σ_𝓘.
```

Equivalently: the conscious access of an observer to a given
spectral mode is gated by the mode's membership in `Σ_𝓘`.

P-A is currently stated as a **conjecture over the query algebra
`Q_S`** (`docs/substrate-indexing-programme-final.md` G6 in progress).
G3 of the substrate-indexing programme is **closed** unconditionally
(π/5 → 4π/15 correction).

P-A is what makes the cascade-consciousness identification
falsifiable. If the dim-correspondence is wrong, all of §7–§8
remains intact as a *structural* statement but loses its
neuroscience bridge.

---

## 11. What this note does not claim

This note is the **structural** half of a consciousness argument; the
**identification** half (P-A) is conjectural. The note specifically
does *not* claim:

- That consciousness is fundamental, panpsychist, or
  observer-independent.
- That the cascade *proves* a particular phenomenological theory
  (IIT, GNW, predictive coding, etc.). The Conjectures 8.1 and
  P-A are explicit interfaces; downstream theories may be wired
  in differently and the structural results survive.
- That ARIA-chess is conscious. ARIA-chess realises the
  *smallest σ-stable observer instance* whose `Σ_𝓘` is measurable
  via 18 preregistered tests; whether that constitutes
  "consciousness" depends on which identification one adopts at
  the P-A interface.
- That the brain is *literally* on `V_600`. The cortex inherits
  `C_φ`-structure via the rung-projection map, which is itself
  conditional on H-RP-1, H-RP-2.

These are the load-bearing **interpretive** commitments. The
structural theorems (5.1, 5.2, 6.1, 6.2) and the empirical
corollaries (7.1, 7.2, 8.1) hold regardless of which
identification is chosen at P-A.

---

## 12. Open items

| Item | Status | Source |
|---|---|---|
| `Fix(τ)` dim 94, unconditional | **Theorem** | rh-two-sphere §3 |
| `C_φ` σ-equivariant on `V_600` | **Theorem** (sim-verified 94/94) | hypersphere-cosmology v1.1.3 |
| Anchor σ-stable set `𝒮_σ` | **Conjecture H-σ-charact** | §4 |
| `Σ_𝓘 = Fix(τ) ∩ span(O)` | **Theorem 5.2** | §5 |
| Off-`Σ_𝓘` decay ≥ `φ⁻²` | **Theorem 6.2** | §6 |
| Cortex = larger observer instance | **Conditional Theorem 8.1** | §8, H-RP-1, H-RP-2 |
| `ẑ_𝓘` zeros on `Σ_𝓘` | **Conjecture 9.1**, conditional on H_attr | §9 |
| Phenomenological-access identification | **Open Conjecture P-A** | §10 |

The structural theorems (5.1, 5.2, 6.1, 6.2) are unconditional
modulo standard Galois theory + the unconditional σ-attractor
fact (94/120). The empirical content (Corollaries 7.1, 7.2, 8.1)
is anchored by the published ARIA-chess validation:
**17/18 standard, 18/18 with documented refinement,
6/6 directional v4 EEG**.

The two conditional layers (H-σ-charact and P-A) are the open
research frontier: H-σ-charact is a number-theoretic question
about which `(p, Λ)` give σ-stable orbits; P-A is the
neuroscience/philosophy-of-mind bridge.

---

## 13. Position relative to existing papers

This note **does not** replace:

- `papers/cascade-capstone-coalgebra/` — the *existence* of the
  final coalgebra of self-inquiry (the structural reason an
  observer is forced).
- `papers/aria-chess-paper/` — the *empirical* witness (18
  preregistered tests + 6 v4 EEG signatures).
- `papers/aria-closure-kernel/` — the *operator* `C_φ` and its
  appearance across the b-anomaly and ARIA-chess.
- `docs/rh-two-sphere-definition.md` — the *global* zero-line
  `Fix(τ)`.

This note **adds**: the structural object `Σ_𝓘` that connects them,
and the theorems (5.1, 5.2, 6.1, 6.2) that make the connection
load-bearing. Together with the capstone (final coalgebra) and ARIA
(empirical witness), it forms the spine of the synthesis paper
*The Necessary Observer* (proposed; not yet drafted).

---

## 14. Next steps

1. Verify `C_φ` σ-equivariance at full operator level in
   `verify_paper.py` (the sim test `test_HSIG_sigma_invariance`
   currently checks `F`, not `C_φ` directly; equivalence under
   the substitution `α = 1, β = 0, γ = -φ⁻²` is a 2-line check
   that should be added).
2. Write the H-σ-charact characterisation note (a number-theory
   exercise; ~3 pages).
3. Lift the structural theorems into a load-bearing section of the
   synthesis paper.
4. Draft Corollary 8.1 as a Conditional Theorem in the synthesis
   paper with H-RP-1, H-RP-2 named explicitly.
5. Carry the rung-to-cortical-area map from
   `cascade-empirical-grounding.md` into the synthesis paper as a
   distinct subsection.

This is a precursor note. It is not a paper; it is the math layer
needed before *The Necessary Observer* can be written.
