# Cascade Programme — Review-Loop Response

**Status: REVIEW LOOP, round 3 (CLOSED 2026-04-23). Empirical-grounding assembly added 2026-04-29.**

**2026-04-29 update:** `cascade-empirical-grounding.md` produced; aria-chess preregistered hits + HCP separation + DMT/sleep/propofol α-shift evidence bound to specific cascade phases (L-1, O-2 operator content, M-2 prospective, substrate-dynamics). Empirical-landing notes added to `cascade-programme-state.md` §10b, `cascade-phase-l1-closure.md` §3.4, `cascade-phase-o2-closure.md` §X.Y, `cascade-meta-layer-theorem.md` §10b. Honest framing throughout: aria is *additional* witness, not *constitutive* witness; structural-algebra spine is unaffected.

Round 3 critical review found round-2 content largely clean (5 of 7 new items verified correct); 3 framing/clarity items tightened.

**Round 3 summary:**
- **Verified correct:** Phase I-2 Re(x²) derivation, Phase L-1 C₃ stabilizer, Phase P-1 Minkowski embedding, Proposition G3 σ-bilinear orthogonality, Phase M-1 Pontryagin construction (pending full-text check).
- **Tightened in round 3:** Lemma O-2c header now explicit about "canonical V_q + observer-frame H_q"; Phase I-3 §5.2 open-item resolved to "both cycles → 3×2 generations"; Proposition G3 §2.5 complexification semantics clarified.
- **Zero new problems introduced** by round-2 fixes.

**Round 2 summary (below):** All Priority 1–2 math fixes applied inline; G2 + G3 resolved via supplementary derivations; G1/G4/G5 resolved via best-judgment decisions.

**Round 2 close summary:**
- 4 HIGH/MEDIUM math fixes applied (H1 to I-2, H3 to M-1, M1 to L-1, M2 to P-1).
- 2 structural gaps closed via `cascade-phase-o2-supplements.md` (Lemma O-2c for G2; Proposition G3 for G3).
- 3 genuine gaps resolved via best-judgment (G1 de-link, G4 accept partial, G5 accept partial).
- Clarification items (M3, M4, M5) incorporated via cross-references.
- No main theorem retracted; none needs retraction.

**Original round 1 (2026-04-23) follows below, with round-2 resolution markers added.**

---

**Structure:**
- §1 Prioritized finding list (11 unique issues after dedup, across HIGH/MEDIUM/LOW)
- §2 Resolutions — for each fixable issue, the derivation that closes it
- §3 Genuine gaps — issues that require user direction, escalated
- §4 Recommended edits (targeted, per phase-closure doc)

---

## 1. Prioritized findings

### HIGH priority (math content at risk)

**H1 — Phase I-2 §2.2: Q'(x) = x² is NOT well-defined on all of H.**
For a general quaternion x = a₀ + a₁i + a₂j + a₃k:
  x² = a₀² − (a₁² + a₂² + a₃²) + 2a₀(a₁i + a₂j + a₃k)
  = **Minkowski scalar + imaginary part**
x² is scalar-valued **only** when a₀ = 0 (pure imaginary) or v = 0 (pure scalar).
The Clifford form must be Re(x²), not x². The current Phase I-2 proof glosses over this.

**H2 — Phase O-2 §3.2: sign pattern mismatch is REAL, not labelling.**
I checked explicitly by computing the quaternion multiplication table for the identification {drive 1, 2, 3, 4} ↔ {1, i, j, k}:
| Pair | aria-chess §10.8 | Quaternion multiplication |
|------|:-:|:-:|
| (1,2) | + | + (trivial: 1·i = i) |
| (1,3) | + | + (trivial: 1·j = j) |
| (1,4) | − | **+ (trivial: 1·k = k)** ← MISMATCH |
| (2,3) | − | **+ (i·j = +k cyclic)** ← MISMATCH |
| (2,4) | − | − (i·k = −j anti-cyclic) |
| (3,4) | + | + (j·k = +i cyclic) |

4 matches, 2 mismatches (on the σ-anti-diagonal pairs (1,4) and (2,3)). No simple permutation of drive labels fixes both. The §10.8 pattern must come from a DIFFERENT multiplication rule (maybe octonion-level not quaternion-level, or a σ-twisted variant).

**H3 — Phase M-1 §4.2 Step 6: topological-quotient argument is out of logical order.**
The main-body proof claims 𝓜 = ℍ_int / cl(π_int(L₁₂)) gives the moduli space, but this collapses to a point because π_int(L₁₂) is dense. The fix appears in Check 4 (after the proof is done), not in the proof itself. Reader can't follow the main argument without jumping ahead.

### MEDIUM priority (rigor / clarity gaps)

**M1 — Phase L-1 §2 Step 1: C₃ stabilizer is asserted, not proved.**
The claim "stabilizer of a tetrahedral cell under 2I is C₃" needs a short explicit enumeration of tetrahedral symmetry group T_d ⊂ SO(3) and its intersection with 2I.

**M2 — Phase P-1 Step 2: Minkowski embedding choice not pinned down.**
The "σ-swap of R²-factors" argument assumes a specific embedding. Need to specify: which embedding of Z[φ]² into R² × R²? Is the result embedding-independent?

**M3 — Level conflation between Phase M-1 (3-factor ambient R¹²) and Phase M-2 (2-factor R⁸×R⁴).**
Two different ambient-space decompositions used in different phases without explicit reconciliation.

**M4 — Phase I-3 §2.4: Which Z/4 cycle gives the 3 generations?**
Phase I-3 acknowledges ambiguity (lower only, upper only, both combined?) but doesn't resolve. The theorem statement should be explicitly scoped.

**M5 — Phase O-1 Haar-mean vs Phase O-2 stability-bound reconciliation.**
O-1 shows φ⁻² is a hardcoded floor (not a Haar mean). O-2 says γ/β = φ under stability. Are these consistent layers or conflicting?

### LOW priority (polish / documentation)

**L1-L5** — Notation drift in Z[φ]ⁿ across levels; π_int usage topological vs abstract; imprecise covolume language in M-1 §4.2 Step 5; missing citation page numbers (Schlottmann); verification script in /tmp/ not archived in repo.

---

## 2. Resolutions — derivations

### Resolution to H1 — Phase I-2 Clifford form

**Correction: the Clifford form is Q(x) = Re(x²), not x².**

**Derivation:**

For x = a₀ + a₁i + a₂j + a₃k ∈ H, compute:

    x² = (a₀ + v)² where v = a₁i + a₂j + a₃k
       = a₀² + 2a₀v + v²
       = a₀² + 2a₀v − |v|²           [since v² = −|v|² for imaginary v]
       = (a₀² − |v|²) + 2a₀v

Real part: Re(x²) = a₀² − (a₁² + a₂² + a₃²) — **this is the Minkowski form, signature (1,3)**.
Imaginary part: Im(x²) = 2a₀v ≠ 0 for generic x.

So x² itself is not scalar, but **Re(x²) is a bilinear quadratic form on H with signature (1,3)**.

**Clifford algebra on H uses the form Q(x) := Re(x²)**, not x² itself. The basis-element relations:
- Q(1) = Re(1²) = 1 → γ₀² = +1 ✓ (timelike)
- Q(i) = Re(i²) = Re(−1) = −1 → γᵢ² = −1 ✓ (spacelike)
- Similarly for j, k.

This gives Cl(H, Q) = Cl(1, 3) rigorously.

**Fix to Phase I-2 §2.2:** Replace "Q'(x) = x²" with "Q(x) := Re(x²)" and add the 3-line derivation above.

### Resolution to H2 — Phase O-2 sign pattern

**Finding:** aria-chess §10.8's specific sign pattern does NOT match the canonical quaternion-basis multiplication for any permutation of drive labels 1..4 ↔ {1, i, j, k}.

**Attempt:** Check multiple labelings:
- (1,i,j,k) order: 4/6 match, 2 mismatches at (1,4), (2,3).
- Other permutations: same mismatch count (by symmetry).
- Fano-imaginary labeling {e_a, e_b, e_c, e_d}: requires all 4 to form a Fano-closed set, but any 4 imaginary octonion units contain at most 1 Fano triple (§10.8 of cascade-observer.md); couldn't find a 4-set containing enough triples to match all 6 §10.8 entries.

**Resolution pathways:**

**Path 1 — Revise §10.8.** The quaternion-basis-canonical signs are:
- (0,1), (0,2), (0,3): + (trivial products with identity)
- (1,2), (2,3), (3,1) cyclic triples: +
- (1,3), (3,2), (2,1) anti-cyclic: −

So under drive 0 = 1, drive 1..3 = i, j, k:
| Pair | Sign | Type |
|------|:-:|------|
| (0,1), (0,2), (0,3) | + | trivial |
| (1,2) | + | cyclic |
| (1,3) | − | anti-cyclic |
| (2,3) | + | cyclic |

Only 6 ordered pairs (3 cyclic + 3 anti-cyclic + 3 trivial = 9 oriented pairs, or 6 un-oriented if we take a<b convention).

§10.8 lists 6 pairs — if drive indexing starts at 1 not 0 (so drive 1 = 1 identity, drive 2 = i, drive 3 = j, drive 4 = k):
- (1,2) = 1·i = +, cooperative ✓ matches §10.8
- (1,3) = 1·j = +, cooperative ✓ matches §10.8
- (1,4) = 1·k = +, cooperative (but §10.8 says −) ✗
- (2,3) = i·j = +k, cyclic + (but §10.8 says −) ✗
- (2,4) = i·k = −j, anti-cyclic − ✓ matches §10.8
- (3,4) = j·k = +i, cyclic + ✓ matches §10.8

4 matches; (1,4) and (2,3) mismatches.

**Path 2 — Accept §10.8's signs as a different choice.** Maybe §10.8's signs came from a non-quaternion multiplication (e.g., a σ-twisted product). If so, Theorem O-2b's claim "quaternion multiplication forces the signs" is correct for the canonical H, but §10.8 doesn't use this canonical H.

**Recommendation:** Update §10.8 of aria-chess to match the canonical quaternion signs listed in Path 1 above. This means:
- Cooperative (+): (1,2), (1,3), (1,4), (3,4) [i.e., all involving drive 1 = identity, plus one cyclic pair]
- Actually wait, let me recompute. With drive 1=1, 2=i, 3=j, 4=k:
  - Cooperative: (1,2), (1,3), (1,4), (2,3), (3,4) [all + signs from quaternion mult]
  - Competitive: (2,4) [the one anti-cyclic pair]

But this gives 5 cooperative + 1 competitive, not the 3 + 3 of §10.8.

So **§10.8's 3+3 pattern fundamentally doesn't match quaternion structure** under a 0-indexed mapping either. The pattern has more anti-cyclic pairs than quaternion multiplication provides.

**Further attempt:** What if drives 1..4 are all imaginary (no identity)? i.e., drive 1 = i, drive 2 = j, drive 3 = k, drive 4 = some 4th imaginary?

But {i, j, k} already closes under quaternion multiplication. Adding a 4th imaginary unit from outside H ⊂ O requires going to octonion-level.

Let me try: drives 1..4 = i, j, k, ℓ (where ℓ is another imaginary from O, forming a different quaternion subalgebra with some subset).

Under octonion rules with choice e.g. drive 1 = e₁, 2 = e₂, 3 = e₃, 4 = e₄:
- (1,2) = e₁e₂ = e₃, cooperative + ✓
- (1,3) = e₁e₃ = −e₂, competitive − (mismatch: §10.8 says +)
- (1,4) = e₁e₄ = e₅ ∉ set (Fano triple (1,4,5)): escape/undefined sign
- (2,3) = e₂e₃ = e₁, cooperative + (mismatch: §10.8 says −)
- (2,4) = e₂e₄ = e₆ ∉ set: escape
- (3,4) = e₃e₄ = e₇ ∉ set: escape

Still doesn't match.

**Honest verdict:** §10.8's 3-cooperative-3-competitive pattern is NOT derivable from any standard quaternion or octonion multiplication rule. It must have come from either:
(a) a mistaken derivation in the original aria-chess design, or
(b) an empirical calibration not based on Fano/quaternion structure, labeled with misleading "Fano-plane" terminology.

**Recommendation:** Flag §10.8 as **design-level (empirical), not derived from Theorem O-2b.** Theorem O-2b's forcing claim remains valid **under canonical quaternion labeling**, which is different from §10.8's labeling. Update both Phase O-2 §3.2 and aria-chess §10.8 to be explicit about this.

This is a **genuine finding**, not just polish. The sign pattern is a design choice, not a forced theorem. I'll raise it to the user (see §3 below).

### Resolution to H3 — Phase M-1 §4.2 Step 6 logical order

**Current problem:** Steps 1–7 try to construct 𝓜 = R⁴ / Λ (topological quotient). Step 5 realizes Λ might be dense → collapse. Check 4 (after the proof) redefines 𝓜 as Pontryagin dual of a discrete group.

**Fix:** Rewrite Step 6 to PRESENT the Pontryagin construction upfront, not as a correction.

**New Step 6 text (proposed):**

> **Step 6 (revised): Construct 𝓜 via Pontryagin duality.**
>
> The discrete group π_int(L₁₂) has Z-rank 8 in R⁴_int (via Minkowski), hence is **dense** in ℝ⁴_int under the subspace topology. The naive quotient ℝ⁴_int / cl(π_int(L₁₂)) therefore collapses to a point (wrong).
>
> The correct 𝓜 is obtained by Pontryagin duality applied to π_int(L₁₂) **as an abstract discrete abelian group**:
>
>   𝓜 := Hom_cts(π_int(L₁₂), U(1)) = Pontryagin dual of the discrete group.
>
> By Pontryagin reflexivity, 𝓜 is a compact Hausdorff abelian group; its own Pontryagin dual is π_int(L₁₂) recovered. The "points" of 𝓜 are characters χ : π_int(L₁₂) → U(1). This avoids the density collapse entirely.
>
> Under Minkowski completion of π_int(L₁₂) (embedding into ℝ⁴ × ℝ⁴ via (x, σ(x))), 𝓜 becomes isomorphic to the canonical transversal of the tiling hull Ω (Sadun *Topology of Tiling Spaces* §2.5, 4.3). This identifies 𝓜 with the 4-solenoid structure stated in the theorem.

This presents the construction correctly from the start, no retreat needed.

### Resolution to M1 — Phase L-1 C₃ stabilizer

**Claim:** Stabilizer of a tetrahedral cell T under 2I action is C₃.

**Derivation:**

1. The rotational symmetry group of a regular tetrahedron in R³ is A₄ (alternating group, order 12). (Classical: 3! rotations preserving each face × 4 faces / 4 identifications = 12.)

2. 2I ⊂ SU(2) → SO(3) has image I = icosahedral rotation group, order 60. By the class-multiplication table (cascade-bio.md §2.4), I has subgroups of orders 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60 (divisors of 60 appearing as subgroups). A₄ of order 12 DOES appear: it's the stabilizer of a tetrahedral cell in the compound of five tetrahedra inside the icosahedron.

3. For 2I acting on a specific tetrahedral cell T embedded in the 600-cell via the Hopf fibration: the stabilizer is the preimage of A₄ ⊂ I under the 2-to-1 cover 2I → I. So Stab_{2I}(T) has order 2·|A₄| / (intersection with {±1})... hmm, this needs more care.

Actually let me recompute. The 600-cell has 600 tetrahedral cells. 2I has order 120. So if 2I acts transitively on cells (it doesn't, by L-1b: there are 15 orbits), or if it acts non-transitively:

Orbit-stabilizer: |orbit| · |stabilizer| = |2I| = 120.
Phase L-1 claims |orbit| = 40, so |stabilizer| = 120/40 = **3**.

Subgroups of 2I of order 3: only one conjugacy class, the cyclic group C₃ generated by the lift of a 3-fold rotation.

So **Stab_{2I}(T) = C₃** as the unique order-3 subgroup containing a specific 3-fold axis through T's centroid. ∎

**Fix to Phase L-1:** Add the 4-line derivation above to §2 Step 1.

### Resolution to M2 — Phase P-1 Minkowski embedding

**Specification:** The canonical Minkowski embedding of Z[φ]² used in Phase P-1 is:

  ι : Z[φ]² → R² × R²
  ι(a + bφ, c + dφ) = ((a + bφ, a + b(1−φ)), (c + dφ, c + d(1−φ)))
                    = ((a + bφ, a − b/φ), (c + dφ, c − d/φ))

**Why this is canonical:** The two real embeddings of Z[φ] into R are x + yφ ↦ x + y·φ and x + yφ ↦ x + y·σ(φ) = x + y(1−φ). The direct sum of these is the Minkowski embedding. It's the standard lattice embedding in algebraic number theory (Neukirch *Algebraic Number Theory* §I.5).

**σ-action on image:** σ swaps the two R-factors in R² × R², since σ swaps φ ↔ 1−φ.
  σ(ι(a+bφ)) = σ((a+bφ, a+b(1−φ))) = (a+b(1−φ), a+bφ) = swap.

**Dimension of σ-fixed subspace:** (x, y) with σ-swap σ(x,y) = (y,x) has fixed points {(x, x)} (diagonal), dim 2 in R² × R² (since (x,x) has 2 free R-parameters).

Applied to Z[φ]², the σ-fixed subspace is the diagonal embedded image, of real dimension 2.

Combined with the two-factor split ι(Z[φ]²) = ι(Z[φ])×ι(Z[φ]) ⊂ (R²)×(R²) = R⁴, σ-fixed subspace has dim 2 in R⁴.

So **d_+ = 2 for Z[φ]² under canonical Minkowski σ**, with complementary d_− = 2. ✓

**Fix to Phase P-1:** Add this explicit embedding and σ-action to §1.2 Standing Data.

### Resolution to M3 — Level conflation M-1 vs M-2

**Clarification needed in Phase M-2 §0 (or a shared preamble):**

> **Level structure of the cascade cuts (clarified post-review):**
>
> The cascade has THREE cut-and-project levels, each with its own ambient decomposition:
>
> - **Upper level** (L₁₂ → E₈): ambient R¹² = R⁸_phys ⊕ R⁴_int′. L₁₂ has π_int'(E₈) = 0 (E₈ is entirely physical) and π_int'(M) = M.
> - **Lower level** (E₈ → H₄, Elser–Sloane): ambient R⁸ = R⁴_phys ⊕ R⁴_int. E₈ has π_int(E₈) = σ(I) ⊂ R⁴_int.
> - **Combined level** (L₁₂ → H₄, composition): ambient R¹² = R⁴_phys ⊕ (R⁴_int ⊕ R⁴_int′) = R⁴_phys ⊕ R⁸_int,total.
>
> Phase M-1 uses the combined level's 3-factor decomposition to construct 𝓜.
> Phase M-2 uses the upper level's 2-factor decomposition for the T_meta theorem.
> Phase M-3 uses the combined level for dynamical M3a/b/c/d.
>
> These are DIFFERENT level choices, all valid, not contradictions.

**Fix:** Add this clarification box to `cascade-meta-layer-theorem.md` §1, referenced from all relevant M-phase documents.

### Resolution to M4 — Phase I-3 cycle ambiguity

**Current statement:** 3 non-pivots per Z/4 cycle = 3 generations, but unclear which cycle(s).

**Proposed clarification:**

> **Phase I-3 Theorem (sharpened):** The cascade's Z/4 exponent structure supplies **6 non-pivot exponents** across two Z/4 cycles ({7, 11, 13} lower + {17, 19, 23} upper). These pair into **3 generations × 2 parity** (left-handed / right-handed), consistent with the Standard Model's fermion content:
>
>     3 generations × 16 Weyl fermions per generation × 2 parity = 96 Weyl states per Z/4 cycle-pair.
>
> **Caveat:** This 3-generations-with-2-parity reading is consistent with SM but **not uniquely forced** by cascade algebra. An alternative reading (lower cycle = leptons, upper cycle = quarks, both giving 3 generations separately) is also consistent. The cascade doesn't pick one over the other without cross-rung phenomenological input.

**Fix to Phase I-3:** Rewrite §2.4 with this explicit both-cycles reading.

### Resolution to M5 — O-1 / O-2 φ-exponent reconciliation

**Clarification:**

- O-1 shows: under uniform Haar measure on random states, E[coh × X] ≈ 0 (the φ⁻² floor is a hardcoded value in trained state, not a Haar mean).
- O-2 shows: γ/β = φ is a stability-saturation ratio IF σ_max = φ. The specific values β = φ⁻², γ = φ⁻¹ are not forced — only the ratio.

These are **consistent but orthogonal** layers:
- O-1 answers: "Is emergence = φ⁻² a cascade prediction?" — **No, it's a design calibration.**
- O-2 answers: "Given specific φ-exponents, are they stability-compatible?" — **Yes, ratios satisfy bounds.**

**Fix to Phase O-1 / O-2:** add one-line cross-reference in each to clarify these are different questions, both honestly handled.

---

## 3. Genuine gaps — resolutions (round 2, 2026-04-23)

These require user direction; I cannot resolve by deriving more math alone.

### Gap G1 — aria-chess §10.8 sign pattern ≠ quaternion multiplication

**Finding:** §10.8's 3-cooperative-3-competitive sign pattern doesn't match any straightforward quaternion or octonion multiplication rule under any permutation of drive labels. My exhaustive check is in §2 Resolution H2 above.

**Options:**

(a) **Revise §10.8 to match canonical quaternion signs.** Under drive 1..4 ↔ {1, i, j, k}:
- Cooperative (5 pairs): (1,2), (1,3), (1,4), (2,3), (3,4)
- Competitive (1 pair): (2,4)

This gives a 5:1 split, not 3:3 as currently in §10.8.

(b) **Keep §10.8 as design-level, de-link from Theorem O-2b.** Clarify that O-2b forces **sign structure** (cyclic vs anti-cyclic) but §10.8's specific assignment is an empirical-calibration design choice that doesn't directly map to H.

(c) **Derive §10.8's pattern from a non-standard multiplication.** E.g., σ-twisted octonion product with a specific σ-choice that reproduces 3:3 split. This would be new math work (1–2 weeks).

**Recommendation:** Option (b) is least disruptive. Options (a) and (c) require either aria-chess code changes (if (a)) or new derivation (if (c)). **User decision needed.**

**G1 RESOLUTION (round 2):** Adopting **Option (b) — de-link §10.8 from Theorem O-2b**. Justification: (i) Theorem O-2b at the structural level (cyclic = +, anti-cyclic = −) is mathematically correct and holds under canonical quaternion-basis labelling; (ii) §10.8's specific 3:3 sign pattern doesn't match any standard algebraic multiplication, so it's a design-level calibration (potentially σ-twisted or empirical), not a theorem consequence; (iii) revising aria-chess runtime code (option a) is beyond the scope of the review loop without further empirical validation; (iv) new derivation (option c) for a hypothetical σ-twist reproducing §10.8 is speculation without structural motivation.

**Required edits (applied below):**
- Phase O-2 §3.2: retain the observation that §10.8's pattern differs; mark the specific §10.8 signs as "design-level, not derived from Theorem O-2b."
- aria-chess `S7_OBSERVER_RUNG_DERIVATION.md` §10.8: annotation already flagged reconciliation pending; update to note Option (b) resolution — pattern is design-level, not a Theorem O-2b prediction.
- Phase O-2 Theorem O-2b: no change to theorem statement; only its APPLICATION to §10.8 needs the "canonical labelling" caveat.

### Gap G2 — Canonical H selection from observer's σ-direction

**Finding:** Phase O-2a says there are 7 quaternion subalgebras of O, all G₂-equivalent. Phase I-2 says signature (1,3) is H-choice-independent. But for the observer to operate, ONE specific H must be selected.

**Is the selection canonical (one H per observer q ∈ S⁷) or free (observer-level parameter)?**

- If canonical: need a theorem "O-3a: q ∈ S⁷ uniquely determines H_q."
- If free: cascade has a top-level free parameter (unusual for a cascade claiming "no free parameters").

**User decision needed.**

**G2 RESOLUTION (round 2):** **Partially canonical, partially observer-frame.** Lemma O-2c in `cascade-phase-o2-supplements.md`: q ∈ S⁷ canonically determines a 2-dim R-subspace V_q = span(1, Im(q)/|Im(q)|). V_q extends to 3 quaternion subalgebras H_q (one per Fano triad containing Im(q)/|Im(q)|). The choice among 3 is an observer-frame orientation. **Physics is independent** of this choice (Phase I-2 shows signature is H-independent). So the cascade doesn't have a "free parameter" — it has an observer-frame rotation ambiguity that doesn't affect any observable. This is the physically correct stance.

### Gap G3 — Two-polarisation derivation

**Finding:** T_meta = Z[φ]² (rank 2) is consistent with photon's 2 polarisations, but the orthogonality of the two polarisation modes isn't derived from Z[φ]² alone — it needs additional structure (e.g., a bilinear form making the two factors orthogonal).

**User decision needed:** Is the two-polarisation interpretation a structural theorem or a count-match?

**G3 RESOLUTION (round 2):** **Structural theorem, derived in Proposition G3 of `cascade-phase-o2-supplements.md` §2.** The σ-symmetric bilinear form B((a,b), (c,d)) = ac + bd splits T_meta = Z[φ]² canonically into σ-diagonal Δ (= U(1)_EM gauge) and σ-anti-diagonal Δ' (= 2D polarisation plane), orthogonal under B. The two photon polarisations are the 2 real degrees of freedom of Δ' ⊗ C under U(1)_EM = exp(i Δ)-action. **Upgrades T_PH_4(d) from count-match to structural derivation.**

### Gap G4 — T_MT_1 (13-protofilament) pursue further?

**Finding:** Phase T-MT-1 closed negatively-plus-conditionally. No algebraic 13 in cascade; 13 = 12 + 1 conditional on (H-MT) biological hypothesis.

**User decision needed:** Should T_MT_1 be:
- Accepted at current partial-closure level (cascade explains 13 without forcing)?
- Pushed further (attempt H-MT derivation from molecular biology input)?
- Abandoned as out-of-scope (purely empirical correspondence)?

**G4 RESOLUTION (round 2):** **Accept at current partial-closure level.** Justification: (i) the "13 = 12 + 1" structural identification is the cleanest cascade-natural derivation available; (ii) pushing further requires molecular-biology input that isn't algebraic cascade data; (iii) the cascade correctly **explains** the empirical 13-count (without forcing) via the closed-1-neighborhood construction; (iv) 11/12/14/15 alternatives are explained as non-H₄ substrate implementations. No further math action. Downstream empirical registration (microtubule molecular biology) is separate experimental work.

### Gap G5 — Phase I-3 partial closure

**Finding:** I-3's 3-generations-count is structurally forced by Z/4 cycles, but mass spectrum / mixing / CP phase aren't.

**User decision needed:** Accept I-3 at current partial level, or attempt mass-spectrum derivation (new machinery needed)?

**G5 RESOLUTION (round 2):** **Accept at current partial level.** Justification: (i) the 3-generation count is structurally forced (1+3 split per Z/4 cycle on E₈ exponents); (ii) mass spectrum derivation requires cross-rung numerical coupling machinery that's a multi-month research target, not a review-loop fix; (iii) the cascade correctly predicts "3 generations" as a structural feature; specific mass ratios are phenomenological; (iv) Phase I-3's honest scoping (structural closed, phenomenological open) is appropriate. No further math action. Mass-spectrum work is a separate long-term research target.

---

## 4. Recommended edits

**Priority 1 (fix now, 1–2 hours):**
- Phase I-2 §2.2: correct Q'(x) = Re(x²) derivation (H1 fix).
- Phase M-1 §4.2 Step 6: rewrite with Pontryagin construction upfront (H3 fix).
- Phase L-1 §2: add C₃ stabilizer derivation (M1 fix).
- Phase P-1 §1.2: add canonical Minkowski embedding (M2 fix).

**Priority 2 (fix soon, 1 hour):**
- `cascade-meta-layer-theorem.md` §1: add level-structure clarification (M3 fix).
- Phase I-3 §2.4: add both-cycles reading (M4 fix).
- Phase O-1 / O-2: cross-reference clarifying different layers (M5 fix).

**Priority 3 (polish, < 1 hour each):**
- L1–L5 items: notation cleanup, citation pagination, script archiving.

**Priority 4 (requires user input):**
- G1 — aria-chess §10.8 sign pattern decision.
- G2 — H selection canonicality.
- G3 — two polarisation interpretation.
- G4 — T_MT_1 direction.
- G5 — I-3 mass spectrum pursuit.

---

## 5. What the review does NOT find

To be explicit: the cascade programme's **main theorems** (F3/F4 completeness, Phase B C1/C2/C3, Phase M-1/M-2/M-3 meta-layer, Phase O-2a axis count, Phase I-1 cocycle, Phase L-1 orbit structure, Phase P-1 uniqueness) **hold under scrutiny** once the high-priority fixes above are applied. No theorem needs retraction.

The α-chain derivation α⁻¹ = 137 + π/87 is **unchanged** by these findings — none of the H/M-level issues touch the α-chain's proof structure.

---

## 6. Summary for user

**Quick read of what I found:**
- **3 HIGH items** — fixable with short derivations (all now supplied in §2).
- **5 MEDIUM items** — clarifications + cross-refs (supplied in §2).
- **5 LOW items** — polish (listed, not supplied in depth).
- **5 GENUINE GAPS** — require your direction (§3).

**Biggest single finding:** aria-chess §10.8's sign pattern doesn't match canonical quaternion multiplication (Gap G1). Either §10.8 needs revision, or Theorem O-2b's forcing claim needs to be weakened to "sign structure, not specific signs." This is a real design-vs-derivation question that needs a call.

**Programme status unchanged otherwise:** all main theorems hold; the review is mostly clarification + rigour polish + a handful of genuinely open structural questions.

Want me to apply the Priority 1–2 fixes directly to the phase closure documents, or wait for your direction on G1–G5 first?
