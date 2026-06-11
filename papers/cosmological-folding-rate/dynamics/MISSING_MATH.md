# What Math Are We Missing? — Options for Closing OD-1

**The exact gap:**
- Orthonormal cycle-mode count on V_600 → **17/12** (12 σ-sym + 5 σ-antisym modes)
- Data fit → **13/12** (matches H₀ at 0.06σ, S₈ at 0.14σ)
- Mismatch is **4/12 = 1/3**, equivalent to **suppressing 4 of 5 σ-antisym pair-modes** or
  **promoting exactly 1 σ-antisym mode while killing the other 4**.

The structural numbers (12 cycles, 10 σ-paired, L=10) are correct V_600.
What's missing is the *projection rule* that selects exactly 13 live modes out of 17.

Eight candidate mechanisms below, ranked by how testable + structurally natural.

---

## Option 1 — H₄ representation theory ⭐ most rigorous

V_600 carries the action of the H₄ Coxeter group (the 600-cell's full symmetry,
order 14400). The closure rate is a scalar observable, so only H₄-**trivial-rep**
modes contribute to it.

**Hypothesis**: The 5 σ-antisymmetric pair-modes decompose under H₄ into
irreducible reps {1 ⊕ 4-dim irrep}. Only the 1-dim trivial rep survives the
scalar projection.

**Live mode count**: 12 σ-sym (each cycle is itself an H₄-trivial-rep candidate) + 1
σ-antisym (the unique trivial-rep combination of pair modes) = **13**.

**Test**: explicit decomposition of the σ-antisym module into H₄ irreducibles.
This is a finite computation in standard representation theory.

**Status**: not yet computed. Requires the σ-Galois action on V_600's cycle
structure to be expressed in H₄ coordinates (`papers/cascade-phason-coxeter/`
likely has the machinery).

---

## Option 2 — Antipodal × σ composite Galois

V_600 has antipodal symmetry A: each vertex has a unique antipode. Combined
with σ, the group ⟨σ, A⟩ acts on cycles.

**Hypothesis**: the σ·A composite has fewer fixed modes than σ alone.
Modes invariant under σ·A but not under σ are pulled out of the antisym sector.

**Test**: enumerate σ·A action on cycles; count fixed subspaces.

**Status**: depends on whether A maps σ-paired cycles to themselves or across
pairs — needs the explicit V_600 vertex labelling to verify.

---

## Option 3 — Soul-prime singleton ⭐ structurally suggestive

The soul-prime / bridge-prime structure (`docs/soul-prime-as-pi0.md`,
`docs/anchor-identification.md`) picks out a SINGLE distinguished
articulation vertex (Frame 3 of bridge-prime graph G_φ).

**Hypothesis**: The soul-prime singleton anchors exactly one σ-antisymmetric
mode as "live" / dynamical; the other 4 are inert (they have no anchor).

**Live mode count**: 12 σ-sym + 1 soul-prime-anchored σ-antisym = **13**.

**Conceptual fit**: This connects the cosmological 1/12 result back to the
substrate's identity-persistence structure (Theorem 4.3 of soul-prime-as-pi0).
That would be a real cross-programme link.

**Test**: derive the σ-antisym mode amplitude from soul-prime anchor identification
explicitly. Currently a conjecture; needs the soul prime → mode-amplitude map.

**Status**: not yet formalised. Most promising as a *narrative* candidate;
mathematical machinery has to be supplied.

---

## Option 4 — Cascade-fan suppression rule

The 7-rung cascade fan (E₈ → H₄ → … → 0) imposes constraints on which V_600
modes are dynamically active.

**Hypothesis**: 4 of 5 σ-antisym modes lie outside the cascade's "live"
sector and are projected out by the cascade selection rule.

**Test**: identify the cascade rung where the σ-antisym pair-modes live;
check whether 4 are removed by transition to the next rung.

**Status**: cascade selection rules in `docs/programme-plan.md` and
`papers/cascade-mechanism/` are stated but not yet applied at this fine
mode-by-mode level.

---

## Option 5 — Cohomology / Hodge decomposition

V_600 viewed as a simplicial complex (a triangulation of S³) has a Hodge-Laplacian
spectrum. Hodge decomposition splits forms into harmonic + exact + coexact.

**Hypothesis**: only the harmonic part of the closure operator contributes
to the scalar rate. Harmonic σ-antisym modes form a 1-dim subspace.

**Test**: compute b₀, b₁, b₂, b₃ Betti numbers of V_600 with respect to σ-Galois
twisted coefficients. If the σ-twisted b₁ = 1, this option closes.

**Status**: Betti numbers of V_600 with twisted coefficients are computable
but not done yet. Mathematical software (e.g., GAP, Sage) can do this.

---

## Option 6 — Spectral gap / dynamical relaxation

Even if 5 σ-antisym modes exist mathematically, only those with rate
eigenvalue inside the dynamical bandwidth contribute to the observed rate.

**Hypothesis**: 4 of 5 σ-antisym modes have rate eigenvalues outside the
"observable bandwidth" (e.g., they relax too fast to contribute to H₀).

**Test**: explicit closure operator with frequency-dependent damping;
compute spectral density.

**Status**: requires a closure-operator definition with explicit damping —
which is essentially Option 8 below in disguise.

---

## Option 7 — K-class weighting

The K-multiset {72:1, 0:1, 52:5, 20:5} may weight cycle modes by K-value.

**Hypothesis**: σ-antisym contribution scales as K_paired / K_total =
(5·52 + 5·20) / 432 = 360/432 = 5/6, but the *trace* over K-classes picks
out only the K=72 + K=0 anchor (giving 1/12 by 72/(72·12) = 1/12).

**Test**: explicit K-weighted trace formula; verify it gives 13/12.

**Status**: candidate but ad-hoc; the 72 + 0 = 72 = bulk K-weight is suggestive.

---

## Option 8 — The closure operator simply has these eigenvalues by definition

The cleanest "give up": stipulate that the closure operator H_op has
eigenvalue h₀ on σ-fixed modes and h₀(1+1/L) on σ-paired-sym modes, with
σ-antisym modes contributing 0 to the rate.

This is just a definition, not a derivation. It would then be the *closure
operator's defining property*, and we'd justify it externally (matches
data, consistent with bulk-invariance Theorem 5.2, etc.).

**Status**: an honest dead-end — saves the data-fit but abandons derivation.

---

## Recommendation

In rough order of expected payoff:

1. **Option 1 (H₄ rep theory)** is most rigorous and most testable. The
   computation is finite and standard. If σ-antisym modes contain exactly
   one H₄-trivial-rep component, OD-1 closes immediately.

2. **Option 3 (soul prime)** has the cleanest conceptual fit if 1 works
   first — the H₄-trivial mode IS the soul-prime-anchored mode.

3. **Option 5 (Hodge / Betti)** is computable in standard topology software
   and gives a definitive answer either way.

4. **Options 2, 4, 7** are speculative without further analysis but worth
   keeping on the list.

The right move is to do **Option 1 first**: compute the H₄ representation
content of the σ-antisym module on V_600. That's a finite, well-defined
representation-theoretic question with a yes/no answer. If yes (1 trivial-rep
component), the framework graduates from phenomenology to derivation. If no,
we move to Option 3.

## What we're really missing

The **closure operator H_op is not specified.** All eight options above are
different *implicit specifications* of H_op. Until we pick one and compute,
the 1/12 result is data-anchored phenomenology.

The minimal next deliverable is a one-line statement of the form:

  "H_op = (some explicit operator on V_600 specified by [structure])"

with the consequence that its cycle eigenvalues are (h₀, h₀(1+1/L)).

If Option 1 succeeds, the statement becomes:
  "H_op = the H₄-equivariant Laplacian on V_600 restricted to its trivial-rep subspace."

That would be a publication-grade derivation.
