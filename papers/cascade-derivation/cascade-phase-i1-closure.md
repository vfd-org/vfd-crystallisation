# Phase I-1 — Explicit 2-Cocycle on the Info Rung (Tesseract ↔ Cl(1,3))

**Status: CLOSED.** Closes sub-phase 2a-4 of `cascade-info.md` §6 (the single remaining info-rung gap flagged for closure). Derives the explicit 2-cocycle ε(S, T) on tesseract vertices and verifies it against (i) the examples in `cascade-info.md` §3, (ii) the general cocycle condition over all 4096 triples, and (iii) direct Dirac-gamma-matrix multiplication over all 256 vertex pairs.

**Date:** 2026-04-22
**Parallel to:** `cascade-phase-o2-closure.md` (same template — a rigorous closure of a classical-algebra sub-phase).
**Scope:** Explicit 2-cocycle formula + verification. Does **not** close sub-phases 2a-5 (signature from observer), 2a-6 (fermion generations), or 2a-7 (decoherence); those are separate items.

---

## 0. What closes

> **Theorem I-1.** For S, T ⊆ {0, 1, 2, 3}, the 2-cocycle of the Clifford algebra Cl(1,3), identified via the tesseract-vertex ↔ Cl(1,3)-basis bijection of `cascade-info.md` §1, is
>
>     ε(S, T) = (−1)^{A(S, T)} · ∏_{i ∈ S ∩ T} η_i
>
> where
>
>     A(S, T) := #{(s, t) : s ∈ S, t ∈ T, s > t}    (pair-inversion count)
>     η_0 = +1    (timelike; γ_0² = +1)
>     η_1 = η_2 = η_3 = −1    (spacelike; γ_i² = −1)
>
> This formula (a) reproduces all examples in `cascade-info.md` §3, (b) satisfies the 2-cocycle condition over all 4096 triples (S, T, U), and (c) agrees with direct Dirac-gamma matrix multiplication over all 256 pairs (S, T).

---

## 1. Setup

### 1.1 Tesseract–Clifford bijection (recall, `cascade-info.md` §1)

For any subset S = {s_1 < s_2 < … < s_k} ⊆ {0, 1, 2, 3}, define

    γ_S := γ_{s_1} · γ_{s_2} · … · γ_{s_k}    (ordered product)

with γ_∅ := 1. The 16 tesseract vertices are in bijection with the 16 Cl(1,3) basis elements {γ_S : S ⊆ {0,1,2,3}} via the sign-pattern-to-subset map.

### 1.2 What's given (Z₂⁴ structure mod signs, `cascade-info.md` §2)

    γ_S · γ_T = ε(S, T) · γ_{S △ T}    for some ε(S, T) ∈ {+1, −1}.

The "Z₂⁴ grading" is the vertex-XOR operation on subsets. The 2-cocycle ε(S, T) encodes the full multiplicative structure beyond this grading.

### 1.3 What was open (sub-phase 2a-4)

`cascade-info.md` §3 identified ε(S, T) as a 2-cocycle, stated that it satisfies the cocycle condition, and listed example values — but did not give an explicit closed-form formula. The "edge-labelling on the tesseract graph" was flagged as "pending" in §6.

Phase I-1 closes this sub-phase by supplying the explicit formula (Theorem I-1) and verifying it rigorously.

---

## 2. Derivation of the formula

### 2.1 Anticommutation and signature generators

In Cl(1,3):
- **Anticommutation** between distinct generators: γ_i γ_j = −γ_j γ_i for i ≠ j.
- **Squaring** each generator: γ_i² = η_i ∈ {+1, −1}.
- For signature (1,3): η_0 = +1, η_1 = η_2 = η_3 = −1.

These two rules completely determine the algebra's multiplication.

### 2.2 Reducing γ_S · γ_T to γ_{S △ T}

Write γ_S = γ_{s_1} γ_{s_2} … γ_{s_k} and γ_T = γ_{t_1} γ_{t_2} … γ_{t_l}. The product is:

    γ_{s_1} γ_{s_2} … γ_{s_k} γ_{t_1} γ_{t_2} … γ_{t_l}.

To reduce this to γ_{S △ T} times a sign, we perform two operations in order:

**Step A — Sort.** Bubble-sort the concatenated list (s_1, …, s_k, t_1, …, t_l) into increasing order, swapping adjacent γ_i γ_j (for distinct i, j) using the anticommutation rule (each swap contributes a factor −1).

**Step B — Pair-annihilate.** Each element i that appears in both S and T will end up with two adjacent γ_i's after sorting; apply γ_i² = η_i to remove the pair, contributing η_i to the overall sign.

After Step A + Step B, what remains is γ_{S △ T} in sorted-subset form (elements of S △ T are exactly those appearing an odd number of times in the concatenation).

### 2.3 Counting the sort sign

The bubble-sort sign count is well-defined: count the number of inversions in the concatenated sequence. For sequences (s_1 < … < s_k) and (t_1 < … < t_l) placed back-to-back, an inversion occurs whenever a t_j later in the sequence is smaller than an s_i earlier in the sequence.

    A(S, T) := #{(s, t) : s ∈ S, t ∈ T, s > t}

This counts all such pairs, regardless of whether s and t are equal or distinct. When s = t (i.e. i ∈ S ∩ T), the inversion count contribution is zero (s > t is false when s = t), so the formula is consistent.

### 2.4 Combining

Steps A + B give:

    γ_S · γ_T = (−1)^{A(S, T)} · ∏_{i ∈ S ∩ T} η_i · γ_{S △ T}.

Identifying the coefficient with ε(S, T):

    **ε(S, T) = (−1)^{A(S, T)} · ∏_{i ∈ S ∩ T} η_i.**    (Theorem I-1)

This is the closed-form expression for the 2-cocycle. ∎

---

## 3. Verification

### 3.1 Examples from `cascade-info.md` §3

All six examples pass (numerical script `/tmp/cl13_cocycle_verify.py`, §1 of verification output):

| γ_S | γ_T | ε(S, T) — Theorem I-1 | ε(S, T) — cascade-info.md | Match |
|-----|-----|------------------------|----------------------------|:---:|
| γ_0 | γ_1 | +1 | +1 | ✓ |
| γ_1 | γ_0 | −1 | −1 | ✓ |
| γ_0 | γ_0 | +1 | +1 (γ_0² = +1) | ✓ |
| γ_1 | γ_1 | −1 | −1 (γ_1² = −1) | ✓ |
| γ_{01} | γ_{23} | +1 | +1 | ✓ |
| γ_5 = γ_{0123} | γ_{0123} | −1 | −1 (γ_5² = −1 in sig (1,3)) | ✓ |

### 3.2 2-cocycle condition

The cocycle condition for ε:

    ε(S, T) · ε(S △ T, U) = ε(S, T △ U) · ε(T, U)    for all S, T, U.

Verified numerically over all 16³ = **4096 triples**: 0 failures.

### 3.3 Comparison with direct matrix multiplication

Using standard Dirac gamma matrices in signature (+, −, −, −), compute γ_S · γ_T for all 16 × 16 = **256 pairs** and extract the sign by comparing the result matrix to γ_{S △ T}: 0 disagreements.

### 3.4 Edge-label form

For edges in the tesseract graph — pairs (S, S △ {μ}) differing by a single generator μ — the edge label (sign of multiplication by γ_μ on the *right*) is:

    ε(S, {μ}) = (−1)^{σ_S(μ)} · (η_μ if μ ∈ S else +1)
    where σ_S(μ) := #{s ∈ S : s > μ}.

Sample edge labels (numerical output):

| S | μ | ε(S, {μ}) | Interpretation |
|---|---|:--:|----------------|
| ∅ | 0 | +1 | Identity × γ_0 = γ_0 (no inversions, not in S) |
| {1} | 0 | −1 | γ_1 · γ_0 = −γ_{01} (inversion: 1 > 0) |
| {2} | 0 | −1 | γ_2 · γ_0 = −γ_{02} (inversion: 2 > 0) |
| {3} | 0 | −1 | γ_3 · γ_0 = −γ_{03} |
| {0} | 0 | +1 | γ_0 · γ_0 = γ_0² = +1 (timelike, η_0 = +1) |
| {1} | 1 | −1 | γ_1² = −1 (spacelike, η_1 = −1) |
| {3} | 2 | −1 | γ_3 · γ_2 = −γ_{23} |
| {3} | 3 | −1 | γ_3² = −1 (spacelike) |

The full 16 × 4 = 64 directed edge labels are computable from Theorem I-1 and recorded in the verification script output.

---

## 4. Structural properties

### 4.1 Signature-dependence

The cocycle depends on signature (1, 3) only through the η_i factors. Changing to signature (2, 2) or (0, 4) re-assigns η's but the inversion-count factor is signature-independent. Thus:

- The **Z₂⁴-graded part** of the cocycle — captured by (−1)^{A(S, T)} — is signature-independent; it comes purely from anticommutation.
- The **signature-dependent part** — captured by ∏_{i ∈ S ∩ T} η_i — is what distinguishes Cl(1,3) from Cl(4, 0), Cl(0, 4), Cl(2, 2), etc.

This separation matches `cascade-info.md` §4's "working hypothesis (cross-rung): the signature choice is supplied by the coupling between the 16 rung and the 8 rung (observer)." Phase I-1 explicates why: the signature enters only through η_i, which is exactly the observer-supplied data. Sub-phase 2a-5 (signature from observer) becomes the task of pinning down η_i from observer-rung structure.

### 4.2 Z₂⁴-cohomological content

The cocycle ε(S, T) as a function on Z₂⁴ × Z₂⁴ defines an element of the group cohomology H²(Z₂⁴, Z₂), classifying central extensions of Z₂⁴ by Z₂. For Cl(p, q), this cohomology class is **non-trivial whenever p + q > 0** — hence Cl(1,3) is not a commutative group algebra.

- The **non-triviality** of the class is the formal statement that Cl(1,3) is non-abelian.
- The **specific class** (out of the H²(Z₂⁴, Z₂) ≅ (Z₂)^{(4 choose 2) + 4} = (Z₂)^{10} classifying data) encodes the (1, 3) signature.

### 4.3 Path-independence (cocycle condition as associativity)

The 2-cocycle condition ε(S, T)·ε(S △ T, U) = ε(S, T △ U)·ε(T, U) is exactly the associativity of Cl(1,3) multiplication (γ_S γ_T) γ_U = γ_S (γ_T γ_U). The numerical verification of this condition over all 4096 triples (§3.2) is therefore a direct check that the Cl(1,3) multiplication table is consistent.

### 4.4 Reduction: edge labelling captures the full cocycle

For any pair (S, T), ε(S, T) can be computed by decomposing γ_T into a product of single generators γ_{t_1} · γ_{t_2} · … · γ_{t_l} and multiplying into γ_S step by step:

    ε(S, T) = ∏_{j=1}^{l} ε(S ⊕ T_{<j}, {t_j})

where T_{<j} := {t_1, …, t_{j-1}}. Each factor is a single "edge label" ε(·, {t_j}).

Path-independence (from the cocycle condition) ensures this product is the same regardless of the order in which T's elements are multiplied in. So the edge labels on the 16-vertex, 4-edge-type tesseract graph determine the full 2-cocycle.

This is the "edge-labelling on the tesseract graph" representation that sub-phase 2a-4 asked for.

---

## 5. What Phase I-1 closes and doesn't close

### 5.1 Closed
- **Sub-phase 2a-4:** explicit 2-cocycle formula + edge-labelling on the tesseract graph. See Theorem I-1 (§0, §2).
- **Consistency with the multiplication table** of Cl(1,3): verified numerically over all 256 pairs (§3.3) and 4096 triples (§3.2).

### 5.2 Not closed (per Phase I-1 scope)
- **Sub-phase 2a-5** (signature from observer): which η_i are +1 vs −1 is set by the observer rung per `cascade-info.md` §4. Phase O-2 closed the observer-rung algebra; the explicit signature-supplying mechanism (how the observer's octonion unit direction q ∈ S⁷ determines η_0 = +1) is a separate theorem that would close 2a-5 rigorously. Target for a future Phase I-2 or Phase O-3.
- **Sub-phase 2a-6** (fermion generations): requires cross-rung coupling to QM (H₄) for mass assignment. Separate.
- **Sub-phase 2a-7** (decoherence as 120 → 16 projection): requires QM-rung dynamics. Separate.

### 5.3 Minor recommendations
- `cascade-info.md` §6 can be updated: 2a-4 moves from **pending** to **✓ closed**.
- `cascade-info.md` §3 can cite Theorem I-1 as the explicit formula.
- `scripts/verify_cl13_tesseract.py` can be supplemented by the verification script `/tmp/cl13_cocycle_verify.py` (used in §3); that script specifically verifies Theorem I-1's closed-form matches the matrix multiplication.

---

## 6. Verification checks

### Check 1 — compatibility with existing cascade-info.md examples
All six examples in §3 table pass Theorem I-1 exactly. ✓ (§3.1)

### Check 2 — cocycle condition holds
4096 triples tested; 0 failures. This directly verifies associativity of Cl(1,3) multiplication under the Theorem I-1 formula. ✓ (§3.2)

### Check 3 — matches standard Dirac matrix multiplication
256 pairs tested against explicit 4×4 complex matrix multiplication with signature (+, −, −, −). 0 disagreements. ✓ (§3.3)

### Check 4 — Z₂⁴ graded structure preserved
XOR on subsets gives the correct underlying Z₂⁴ structure (`cascade-info.md` §2); the cocycle is the sign layer on top of this. Theorem I-1's formula cleanly separates the two. ✓

### Check 5 — compatibility with signature discussion
The formula's η_i factors are exactly the signature-dependent part, cleanly separated from the signature-independent inversion count. This matches `cascade-info.md` §4's intuition that signature = observer-supplied data. ✓

### Check 6 — edge-labelling is well-defined
The "path from identity" interpretation of ε(S, T) as a product of nearest-neighbor edge labels (§4.4) is path-independent by the cocycle condition. ✓

### Check 7 — no circular dependencies
Phase I-1 uses `cascade-info.md` §1, §2 (bijection + Z₂⁴ structure, both classical/verified). It does NOT depend on any later sub-phase (2a-5, 2a-6, 2a-7 all untouched). ✓

---

## 7. Honest assessment

### 7.1 Risk level
Very low. The 2-cocycle formula is **classical Clifford-algebra theory** — it appears in standard references (Lounesto, *Clifford Algebras and Spinors*, 2nd ed., Thm. 1.9.1; Chevalley, *Algebraic Theory of Spinors*). Phase I-1 explicitly derives it from the two algebra rules (anticommutation + squaring) and verifies numerically.

### 7.2 Significance for the cascade programme
- Info rung goes from "Bijection + Z₂⁴ level RIGOROUS; cocycle identified but not constructed" (previous status) to **"Full 2-cocycle constructed explicitly and verified"**. The algebra side of rung 16 is now complete.
- The cross-rung coupling (info × observer → signature) has a cleaner structure: the η_i signature data is the *only* input the observer rung needs to supply. Phase I-1 makes this separation manifest (§4.1).
- The Dirac equation's form at rung 16 is now fully derivable from Theorem I-1 + observer-rung signature supply.

### 7.3 Parallel to Phase O-2
- Phase O-2 (observer rung): classical algebra fact (quaternion subalgebras, Hurwitz + Artin) gives a forcing theorem. Design-level work remains for specific calibrations.
- Phase I-1 (info rung): classical algebra fact (Cl(1,3) 2-cocycle) gives an explicit formula. Design-level work remains for observer-supplied signature (sub-phase 2a-5).

Same pattern; different rung.

### 7.4 What external review might flag
- The verification used a specific Dirac-gamma matrix representation (§3.3). Other representations (e.g., Weyl or Majorana) give the same sign structure up to overall phase; this could be spelled out if reviewers ask. Not a concern for the theorem content.

---

## 8. Updates to cross-referenced documents

### 8.1 `cascade-info.md` §6 sub-phase map
Update 2a-4 entry:

> **2a-4** | Explicit cocycle edge-labelling on tesseract graph | **✓ closed (Phase I-1, 2026-04-22)** — formula ε(S, T) = (−1)^{A(S,T)} · ∏_{i ∈ S∩T} η_i; see `cascade-phase-i1-closure.md`.

### 8.2 `cascade-info.md` §3
Add reference: "Explicit formula in Theorem I-1 of `cascade-phase-i1-closure.md`; verified against this table over all 256 pairs."

### 8.3 `cascade-completeness-audit.md` §3.5
Update info-rung status:

> **Explicit 2-cocycle edge-labelling** | RIGOROUS (Phase I-1) | Theorem I-1 closes sub-phase 2a-4.

---

## 9. Programme position

### 9.1 Info-rung status after Phase I-1

| Component | Status |
|-----------|--------|
| Tesseract ↔ Cl(1,3) bijection (§1) | RIGOROUS |
| Z₂⁴ grading (§2) | RIGOROUS |
| 2-cocycle identified (§3) | RIGOROUS |
| **Explicit 2-cocycle formula** | **RIGOROUS (Phase I-1)** |
| Signature supplied by observer (2a-5) | OPEN (handshake with Phase O-2) |
| Fermion generations (2a-6) | OPEN |
| Decoherence 120 → 16 (2a-7) | OPEN |

Info rung's **algebraic spine is complete**. Remaining sub-phases (2a-5, 2a-6, 2a-7) are cross-rung couplings, not intra-rung closures.

### 9.2 Next natural targets

- **Phase I-2** (signature supply from observer): close sub-phase 2a-5. Derive η_i values from observer-rung octonion structure (Phase O-2 supplies 4-axis quaternion subalgebra; which axis is "timelike" is the remaining choice, set by the observer's σ-direction per cascade-observer.md §3). Estimated: 3–5 days. This is a natural Phase-O-2 extension.
- **Life-rung audit**: rung 40 currently SEMI-DEFINED in the completeness audit. Would need analogous Phase L-1 to close its algebraic spine.
- **Pause and review**: several Phase-closure docs in rapid succession again; a codex-review pass would be warranted.

### 9.3 Cascade-completeness state

After Phases M-1/2/3 (meta-layer over L₁₂), O-1 (S7-E retirement), O-2 (observer handshake), and I-1 (info 2-cocycle), the cascade's rigorous coverage is:

| Rung | Status |
|------|--------|
| E₈ | RIGOROUS |
| H₄ | RIGOROUS |
| 40 (Life) | SEMI-DEFINED |
| D₄ | RIGOROUS |
| **16 (Info)** | **ALGEBRAIC SPINE COMPLETE (Phase I-1)** |
| 8 (Observer) | RIGOROUS + handshake (Phase O-2) |
| 0 (Unity) | PLACEHOLDER |
| L₁₂ meta-layer | RIGOROUS (Phases M-1/2/3) |

Life rung is now the single remaining rung with SEMI-DEFINED intra-rung status.

---

## 10. Summary

Phase I-1 closes sub-phase 2a-4 of the info rung with an **explicit closed-form 2-cocycle**:

    ε(S, T) = (−1)^{A(S, T)} · ∏_{i ∈ S ∩ T} η_i

where A counts inversion pairs and η captures Cl(1,3) signature. Verified against `cascade-info.md` §3 examples, the 2-cocycle condition (4096 triples), and direct Dirac matrix multiplication (256 pairs) — **all with zero failures**.

The formula cleanly separates the signature-independent inversion-count factor from the signature-dependent η factor, giving a formal basis for the `cascade-info.md` §4 observation that the observer rung supplies the signature through exactly the η_i data.

The info rung's algebraic spine is now complete; remaining sub-phases (2a-5/6/7) are cross-rung couplings.

---

**End of Phase I-1 document.**
Recommended next: Phase I-2 (signature from observer) as a natural Phase O-2 extension; or pause for codex-review pass on the M-/O-/I- chain.
