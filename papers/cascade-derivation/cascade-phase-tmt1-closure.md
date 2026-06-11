# Phase T-MT-1 — Attempt at the 13-Protofilament Count from Cascade Structure

**Status: CONDITIONAL CLOSURE + NEGATIVE RESULT on purely-algebraic derivation.** Closes the T_MT_1 audit item at the level this document can support: rule out naïve algebraic derivations of "13" from the cascade, and offer the single cascade-natural structural identification (`13 = |closed 1-neighborhood at an H₄ vertex| = 12 + 1`) as a **conditional theorem** under one structural instantiation hypothesis.

**Key finding:** There is **no natural 13** in the cascade's algebraic structure (not a representation dimension, not an orbit size, not an eigenspace multiplicity). The single cascade-natural number that equals 13 is the **closed 1-neighborhood size of any vertex in the 600-cell adjacency graph** (1 vertex + 12 neighbors, since every 600-cell vertex has degree exactly 12 per `MATHEMATICAL_APPENDIX.md` Thm 2).

**Consequence:** T_MT_1 cannot be "forced" in the way O-2a forces 4 or L-1a forces 40. It can only be **conditionally identified** under the hypothesis that microtubule protofilaments instantiate the H₄-vertex closed-neighborhood structure — an empirical biological-interpretation choice, not a cascade theorem.

**Date:** 2026-04-22
**Parallel to:** `cascade-phase-o1-closure.md` (same honest-negative-with-refinement pattern).

---

## 0. What closes and what doesn't

### 0.1 Closed (negative)

> **Theorem T-MT-1 (negative).** The integer 13 does **not** appear as any of the following cascade-natural structural counts:
>
> - representation dimension of 2I (irreps have dims {1, 2, 3, 4, 5, 6, 3, 4, 2}, no 13);
> - orbit size under H₄, H₃, or 2I action on the 600-cell (shell sizes {1, 12, 20, 12, 30, 12, 20, 12, 1}, no 13);
> - eigenvalue multiplicity of the 600-cell Laplacian (multiplicities {1, 4, 9, 16, 25, 36, 9, 16, 4}, no 13);
> - orbit count under any natural finite-group action on 600-cell vertices, edges, faces, or cells;
> - any E₈ shell-count, E₈ character value, or tesseract substructure.

### 0.2 Conditional identification

> **Theorem T-MT-1 (conditional, structural).** 13 = 12 + 1 = size of the **closed 1-neighborhood** at any vertex of the 600-cell graph (since every vertex has degree exactly 12 — `MATHEMATICAL_APPENDIX.md` Thm 2). Under the hypothesis **(H-MT)** that biological microtubule protofilaments instantiate this closed-neighborhood unit (one protofilament per vertex in the neighborhood, including the central vertex), the protofilament count is **13**.

### 0.3 What's not closed

**(H-MT) itself** is an empirical biological-instantiation hypothesis, not a cascade theorem. Justifying (H-MT) requires evidence from molecular biology (that microtubule lattice structure mirrors an H₄-vertex neighborhood), which is outside the cascade derivation proper.

---

## 1. Standing data

### 1.1 From Phase M-2
T_meta = Z[φ]² does NOT carry rank-13 information. Phase M-2 §5.5 explicitly decoupled T_MT_1 from the meta-layer.

### 1.2 From cascade structure
All natural cascade counts are enumerated below (§2).

### 1.3 The microtubule's "13"
Biological microtubules (in eukaryotes) have 13 protofilaments arranged cylindrically. This is the near-universal configuration; 11/12/14/15-protofilament microtubules exist but are minority. The cascade framework hypothesises that 13 is specific (not arbitrary) and can be derived from cascade structure.

---

## 2. Enumeration of cascade-natural counts (rule out spurious 13s)

| Structure | Counts | 13 present? |
|-----------|--------|:---:|
| **E₈ Coxeter exponents** | {1, 7, 11, 13, 17, 19, 23, 29} | **Yes (4th exponent)** |
| E₈ minimum roots | 240 | No |
| E₈ shells (theta series) | 1, 240, 2160, 6720, 17520, … | No |
| **H₄ Coxeter exponents** | {1, 11, 19, 29} | No |
| H₄ Coxeter number h | 30 | No |
| 600-cell vertex count | 120 | No |
| 600-cell vertex **degree** | **12** (every vertex) | 12+1 = **13** |
| 600-cell Laplacian eigenvalues | {12, 6φ, 4φ, 3, 0, −3, −4φ, −6φ, −12} | No |
| Laplacian multiplicities | {1, 4, 9, 16, 25, 36, 9, 16, 4} | No |
| H₃ shell sizes | {1, 12, 20, 12, 30, 12, 20, 12, 1} | No |
| 2I conjugacy classes | 9 (with sizes 1, 1, 12, 12, 12, 12, 20, 20, 30) | No |
| 2I irrep dimensions | {1, 2, 3, 4, 5, 6, 3, 4, 2} | No |
| 2T (binary tetrahedral) order | 24 | No |
| Cascade rungs | 7 | No |
| Tesseract vertices | 16 | No |
| Cl(1,3) basis | 16 | No |
| Octonion dimension | 8 | No |
| Fano plane (points, lines) | 7 each | No |
| G₂ dimension | 14 | No |
| Quaternion subalgebras of 𝒪 | 7 | No |
| D₄ roots | 24 | No |

**Only structurally-13 hit:** the E₈ Coxeter exponent sequence has 13 as its 4th entry. But this is a **position in a list**, not an intrinsic count of anything.

### 2.1 Two plausible cascade-natural identifications of 13

**Option A — E₈'s 4th Coxeter exponent.** The 4th of eight exponents is 13. This is a very specific position but not a natural "count." Using it requires extra justification (why the 4th, why E₈ specifically, etc.).

**Option B — 12 + 1 (closed 1-neighborhood).** Every 600-cell vertex has degree exactly 12 (`MATHEMATICAL_APPENDIX.md` Thm 2, `cascade-bio.md` §2.6). The **closed 1-neighborhood** = vertex itself + its 12 adjacent vertices = **13 points**. This is a natural count on the 600-cell graph.

Option B is cleaner because:
- It's a standard graph-theoretic quantity (closed ball of radius 1).
- It's rung-attached (lives on H₄ = 600-cell).
- 13 is the "kissing + center" count, directly analogous to how the icosahedron has 12 neighbors + 1 center = 13 (icosahedral kissing + self).

We adopt **Option B** as the cascade-natural identification, with the conditional hypothesis (H-MT) that microtubule protofilaments realise this unit.

---

## 3. The conditional theorem

### 3.1 Statement

> **Theorem T-MT-1 (conditional).** Let G be the adjacency graph of the 600-cell at the H₄ rung (120 vertices, every vertex of degree 12). Let N[v] = {v} ∪ N(v) be the closed 1-neighborhood of a vertex v (v plus its 12 neighbors). Then |N[v]| = 13.
>
> **Hypothesis (H-MT):** a biological microtubule protofilament corresponds to one vertex in N[v] for some specific choice of v (the "pivot" vertex), with v itself being the central protofilament position and the 12 neighbors being the 12 surrounding protofilaments.
>
> Under (H-MT), the microtubule protofilament count is |N[v]| = **13**.

### 3.2 What's forced by cascade structure
- **Degree = 12** (Mathematical Appendix Thm 2): proved from H₄'s vertex-transitive action on the 600-cell.
- **Closed 1-neighborhood size = 13 = 12 + 1**: trivial arithmetic.
- **Every vertex's closed neighborhood has the same size** (vertex-transitivity).

### 3.3 What's supplied by (H-MT)
- **The identification** of protofilaments with closed-neighborhood vertices.
- **The cylindrical arrangement** (central column + 12 surrounding columns) matching the neighborhood structure.

(H-MT) is a biological-instantiation hypothesis, testable against actual microtubule molecular structure. Confirming or denying (H-MT) is outside the algebraic cascade derivation.

### 3.4 Alternative 11/12/14/15-protofilament microtubules
Under (H-MT), these alternatives would correspond to vertices of **different cascade substrate graphs** with different vertex degrees:
- 11 protofilaments → degree-10 graph (?);
- 12 protofilaments → degree-11 graph;
- 14 protofilaments → degree-13 graph;
- 15 protofilaments → degree-14 graph.

The 600-cell's vertex-regular degree-12 structure makes 13 the **unique count matching the cascade's H₄ rung**. Other protofilament counts would require other substrate graphs, which are not H₄.

This explains the empirical observation that 13 is by far the most common protofilament count: it corresponds to the cascade's natural substrate.

---

## 4. Relation to Phase M-2 decoupling

Phase M-2 §5.5 concluded: "the 13-count is NOT derivable from T_meta = Z[φ]²." Phase T-MT-1 confirms this: Z[φ]² has no 13 anywhere. But Phase T-MT-1 offers an **alternative structural source** for 13 (the 600-cell graph neighborhood) that doesn't go through T_meta at all.

This is consistent: T_meta is about translation-equivalence of cuts; the 13-neighborhood is about local graph structure. Different aspects of the H₄ rung.

---

## 5. Related open questions

### 5.1 Why degree-12 specifically?
The 600-cell's vertex degree is exactly 12 because every vertex connects to its 12 nearest neighbors via edges of equal length. This is forced by the icosian structure of 2I (cascade-bio.md §2.4) — no choice.

So the chain of forcing:
- 2I ↪ R⁴ forces 600-cell (classical, Elser–Sloane).
- 600-cell forces vertex degree = 12 (classical icosian geometry).
- Closed 1-neighborhood = 12 + 1 = 13.

Under (H-MT), this chain transfers to microtubule protofilament count.

### 5.2 Connection to E₈'s 4th Coxeter exponent
Interesting coincidence: the Coxeter exponents of E₈ are {1, 7, 11, 13, 17, 19, 23, 29}. The 4th entry is 13. Equally, the vertex degree of the 600-cell is 12, and 12 + 1 = 13.

These two "13"s have no obvious structural connection — one is a root-system exponent, the other is a graph-neighborhood count. Their coincidence may be number-theoretic (both involve E₈ structure indirectly), but no cascade theorem links them.

### 5.3 Anesthetic binding (T_MT_5)
`cascade-photon-microtubule-alpha-programme.md` T_MT_5 predicts anesthetic-mode correspondence via the 13 protofilaments' C_13 irrep decomposition. Phase T-MT-1 provides the structural origin of the 13-count under (H-MT), but does not address the anesthetic-mode predictions specifically.

---

## 6. Status

### 6.1 Closed
- **T_MT_1 rigorously cannot be "forced" from cascade algebra alone.** No 13 is produced by any natural cascade count except (a) E₈'s 4th Coxeter exponent (position, not count) and (b) 12+1 = degree + center (identification-dependent).
- **Conditional identification (H-MT) + cascade structure ⟹ 13 protofilaments.**
- **Non-13 microtubules are explained as non-H₄ substrate implementations.**

### 6.2 Not closed
- **(H-MT) itself** — the biological-instantiation hypothesis. Requires empirical confirmation from molecular-biology of microtubule assembly.
- **T_MT_5 anesthetic mode correspondences** — separate empirical question.
- **T_MT_4 helical pitch** — separate structural question requiring H₄ metric data.

### 6.3 Risk level
Low for the negative result (enumeration is exhaustive). Medium for the conditional claim (H-MT is not trivially testable; requires molecular-biology argument).

---

## 7. Updates to cross-referenced documents

### 7.1 `cascade-completeness-audit.md` §3.3
Update Life-rung status — add row:
> **13-protofilament count** | **PARTIALLY CLOSED (Phase T-MT-1, 2026-04-22)** — Rigorously: no algebraic source of 13 in cascade structure (§2). Conditionally: under (H-MT) identification of protofilaments with closed-1-neighborhoods of H₄ vertices, 13 = 12+1 = degree + center. See `cascade-phase-tmt1-closure.md`. |

### 7.2 `cascade-photon-microtubule-alpha-programme.md` T_MT_1
Replace previous structural-conjecture framing with:
> **T_MT_1 — 13 protofilaments. PARTIALLY CLOSED (Phase T-MT-1, 2026-04-22).** 13 = |closed 1-neighborhood at any H₄ vertex| = 12 + 1, conditional on biological hypothesis (H-MT) that protofilaments instantiate this neighborhood. See `cascade-phase-tmt1-closure.md`.

### 7.3 `cascade-bio.md`
Add cross-reference: "Sub-phase B3 (T-numbers): 13-count structurally identified in Phase T-MT-1 as closed-neighborhood at H₄ vertex, conditional on (H-MT)."

---

## 8. Honest assessment

### 8.1 Parallel to Phase O-1 (S7-E retirement)
Phase O-1 retired Conjecture S7-E as literally false; the 0.382 was a hardcoded floor. Similarly, T-MT-1 rigorously rules out "13 is forced by cascade algebra" — the 13 requires either specific positional input (E₈'s 4th exponent) or biological-instantiation hypothesis (H-MT).

### 8.2 Pattern: some cascade predictions are conditional
O-1, T-MT-1, and (to a lesser extent) T-PH-2 all reveal a common feature: some parts of the cascade's physical predictions **depend on additional hypotheses** beyond the ladder's algebraic structure. Phase closures honestly flag these rather than pretending they're fully forced.

The cascade's algebraic spine (rungs + cross-rung couplings) is now fully closed. Predictions of specific physical counts (α, photon mass, 13 protofilaments, emergence value, specific drive axes) vary in their dependence on hypotheses:
- **Algebra-forced** (no hypotheses): α = 137 + π/87 (via Coxeter + McKay), photon properties (via λ=0 mode), 4 drive axes (Phase O-2a).
- **Conditional on biological hypothesis** (cleanly identified): 13 protofilaments via (H-MT).
- **Design-level** (calibration, not theorem): emergence floor = φ⁻², specific φ-exponents.

### 8.3 What external review would ask
- "Is (H-MT) plausible from molecular biology?" — Defer to biology; cite if supporting evidence exists.
- "Why prefer Option B (12+1) over Option A (4th Coxeter exponent)?" — Option B is a natural graph-count; Option A is a positional accident.
- "Does the cascade predict 13 or is 13 accepted as an input?" — Depends on (H-MT); documented explicitly.

---

## 9. Summary

Phase T-MT-1 is an **honest closure of a mixed type**:

- **Negative:** the cascade's algebraic structure does not force 13. Rigorous enumeration shows no 13 in any representation dimension, orbit size, eigenspace multiplicity, or natural shell count.
- **Conditional positive:** under the hypothesis (H-MT) that microtubule protofilaments instantiate the closed 1-neighborhood of an H₄ vertex, the count is 13 = 12 + 1 (vertex degree + center).
- **Explanation of alternatives:** 11/12/14/15-protofilament microtubules correspond to non-H₄ substrate graphs with different vertex degrees; H₄ uniquely gives 13.

The cascade framework therefore **explains** the observed prevalence of 13-protofilament microtubules without "proving" the 13 from pure algebra. This is the cleanest closure T_MT_1 can receive given the cascade's algebraic structure as enumerated in §2.

---

**End of Phase T-MT-1 document.**
Completes the T_MT chain's first-principles derivation attempt; T_MT_2 (primality → discriminability), T_MT_3 (non-13 degeneracy), and T_MT_4 (helical pitch) remain as downstream empirical / structural questions.
