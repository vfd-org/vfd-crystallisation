# Upstream Papers XVIII, XXI, XXIX — Codex Review Loop Session
## 2026-04-17

**Tool:** OpenAI Codex CLI v0.121.0, model `gpt-5.4`
**Script:** `scripts/review_paper.sh`
**Targets:** Paper XVIII (Nelson pairing), XXI (Closure-to-quantum synthesis), XXIX (Observer as constraint)

## Summary

After finishing Paper XXX's 10-round review loop, applied the same approach to the three upstream papers XVIII, XXI, XXIX whose additions in this session support Paper XXX. Each upstream paper got a lighter-touch review (2–3 rounds) since the additions are smaller in scope.

Result: **all three upstream papers' new content is now defensible against codex review** with substantive fixes applied. Remaining flagged issues are pre-existing content outside the scope of this session's additions.

## Per-paper summary

### Paper XVIII (Nelson pairing) — 2 rounds

**Review files:**
- `paper-xviii-20260417T121331Z.md` (round 1)
- `paper-xviii-20260417T121939Z.md` (round 2)

**Issues found in the added §7 (Geometric Structure of the Nelson Wavefunction):**
1. `\Ecal` macro used but not defined in XVIII preamble → replaced with `\psi` configuration-point notation
2. False claims about integrability: "Newlander–Nirenberg requires the dynamics preserving J is linear" — this is simply wrong. Nijenhuis-tensor vanishing is a property of J, not of the flow.
3. "Nijenhuis tensor vanishes since J is covariantly constant under a linear Hamiltonian flow" — conceptually muddled.
4. "Admissible-wavefunction manifold" used without definition.
5. Self-citation "Paper XVIII" from inside Paper XVIII.

**Fixes applied:**
- Rewrote §7 to be modest: J is the standard complex structure of the linear complex vector space $L^2$, read through the amplitude–phase chart. No new-theorem claim. The Proposition was changed to a Remark since $J^2 = -\mathrm{id}$ is tautological once $\Psi$ is complex-valued.
- Deleted the false integrability argument.
- Changed "Paper XVIII" self-reference to "this paper".
- Added positivity caveat ($\rho > 0$) for the amplitude decomposition domain.

**Final state:** round 2 codex accepts the section as honest bookkeeping observation. Remaining flagged issues in XVIII are pre-existing (prop:linearisation overclaiming, $\delta U$ definition mismatch, missing positivity hypotheses in earlier sections) — not from this session's additions.

### Paper XXI (Closure-to-quantum synthesis) — 3 rounds

**Review files:**
- `paper-xxi-20260417T122441Z.md` (round 1)
- `paper-xxi-20260417T123049Z.md` (round 2)
- `paper-xxi-20260417T123658Z.md` (round 3)

**Issues found in the added §4 (Geometric Structure at the Equilibrium Tangent):**
1. Hidden invariant-subspace assumption: $\HW$ preserving the finite-dimensional sector-superposition subspace was implicit but load-bearing.
2. LaTeX compile errors: `\begin{hypothesis}` used without declaring the environment; `\Mcl`, `\Ocal` macros used without definition.
3. Geometric setup treating ambient forms on $\mathcal{H}_O$ as if they were already the descended forms on $\mathbb{CP}^{N-1}$ — no explicit quotient.
4. `\mathbb{CP}^{N-1}$ definition malformed (equivalence classes of equivalence classes).
5. Wrong cross-reference at line 307 (cited `prop:unitary` where `cor:schroedinger_unitary` was meant).
6. Mixed `Kähler` / `K\"ahler` encodings.
7. Status table "Proved" overclaiming — the projective Kähler structure is standard geometric-QM, not proved here.
8. Group action wording (U(N) vs PU(N)) imprecise.
9. Line 177 inference "XXX's Mcl = CP implies hypothesis" — overclaim.

**Fixes applied:**
- Added `\newtheorem{hypothesis}` to preamble; added `\Mcl` and `\Ocal` macros.
- Promoted the invariant-subspace assumption to an explicit `Hypothesis` with its own label and status remark.
- Rewrote geometric setup with explicit unit sphere → horizontal quotient → descended forms. Ambient and descended forms kept distinct.
- Fixed `\mathbb{CP}^{N-1}$ as $S(\mathcal{H}_O)/U(1)$ quotient.
- Fixed cross-reference to `cor:schroedinger_unitary`.
- Normalised Kähler encoding to `K\"ahler` throughout.
- Softened status table entries to "Assembled from standard projective-Hilbert-space geometry, conditional on Hypothesis".
- Clarified that U(N) acts through its induced projective action (factoring through PU(N)).
- Separated state-completeness (observer-side) from sector-subspace invariance (H_W-side) — "compatible but logically distinct".
- Fixed misattribution ("amplitude-homogeneous" → Paper XX, not XIX).
- Updated abstract to flag the hypothesis.

**Final state:** round 3 codex accepts with remaining issues being pre-existing XXI overclaims (Fréchet linearisation language, programme-synthesis claims at §3) — not from this session's additions.

### Paper XXIX (Observer as constraint) — 3 rounds

**Review files:**
- `paper-xxix-20260417T124147Z.md` (round 1)
- `paper-xxix-20260417T124840Z.md` (round 2)
- `paper-xxix-20260417T125316Z.md` (round 3)

**Issues found in the added §5 (Localised Probe Observers):**
1. **Internal contradiction** in Definition `def:probe`: conditions (3) target coherence and (4) off-basin silence could not both hold non-vacuously. Condition (3) said $c_{\phi_j}$ vanishes iff target $\phi_j$ is matched at $O_{\phi_j}$; condition (4) said $c_{\phi_j}$ also vanishes on off-basins $B_{\phi_i}$ ($i \neq j$), which generically contradicts (3).
2. Stale reference to "Condition (4)" at line 323 after merging 3+4 into one condition.
3. "Reasonable $\epsilon < 4$" — journal-sloppy prose.
4. `B_i` vs `B_{\phi_i}` notation mixing in two-observer example.
5. `c_1, c_2, c_3` vs `c_{\phi_j}` functional naming inconsistency.
6. Undefined `O` (should be `O_{\phi_A}`) in toy model section.

**Fixes applied:**
- **Merged conditions (3) and (4) into a single basin-coherence condition**: $c_{\phi_j}$ vanishes whenever $\Phi$ lies in any admissible basin (including the target's own basin and other admitted basins). Positive only on incoherent configurations outside all admissible basins.
- Updated LMC theorem statement and proof to reflect the simpler definition: both observers give $\Ccal = 0$ on shared admissible basin.
- Added new Remark "LMC is definitional by design" acknowledging the simplification is the point: the localised-probe class is precisely defined so LMC holds, and the substantive content is that this class is non-empty and physically natural.
- Renamed "same probe hypothesis" subsection to reflect weaker requirement (just shared admissibility, not literal same functional).
- Fixed `B_i` → `B_{\phi_i}`, `c_1` → `c_{\phi_1}`, `\Phi|_O` → `\Phi|_{O_{\phi_A}}`.
- Fixed "reasonable $\epsilon < 4$" to "$0 < \epsilon < 4$".
- Fixed Condition (4) stale reference.

**Final state:** round 3 codex accepts the probe-observer section. Remaining flagged issues are pre-existing XXIX rhetoric ("Recovery of Quantum Measurement" / "Recovery of Relativistic Frames" titles too strong, consciousness-locus claims) — not from this session's additions.

## Overall trajectory

All three papers moved from "codex finds real bugs in the new content" (round 1 of each) to "codex's top-3 are now pre-existing content outside the session's scope" (round 2–3 of each). Pattern matches what we saw with Paper XXX: each paper's new content converges in ~3 rounds; further rounds would target pre-existing issues outside this session's scope.

## Practical note

Some of the fixes needed (e.g., the internal contradiction in XXIX's Definition `def:probe`) were genuine mathematical bugs that only surfaced under independent review. The loop successfully caught them. The LMC theorem in particular went from "proof uses a contradictory hypothesis" to "proof trivially follows from a coherent definition, with honest acknowledgement that the theorem is definitional by design."

## Suggested next steps

1. Optionally: one more pass on XXX to benefit from tightened upstream (the `fs_from_closure` real-slice pullback might now close cleanly given XVIII's softer language). Probably 1–2 rounds.
2. Pre-existing content across all four papers (XVIII linearisation overclaiming, XXI Fréchet language, XXIX "recovery" rhetoric, XXX remaining prose asymptote) is fair target for a future dedicated pass — but not in scope of this session.
3. Commit what's been done now.

## Addendum — extended refinement pass (rounds 3–5 for upstream, round 12 for XXX)

After the initial 2–3 rounds per upstream paper, the user requested continued refinement to "perfect" the papers as far as the review loop will take them. Further passes applied:

### Paper XVIII (rounds 3 & 4)
- Fixed `δU` definition/redefinition bug (distinct equilibrium-centred form vs raw modulus-curvature)
- Added positivity/nodal-set hypothesis to Prop `irrotational` (only on $\{\rho > 0\}$)
- Fixed `\HW` undefined macro → `H_{\mathrm{W}}`
- Softened overclaim language throughout: "linear quantum evolution emerges" → "formal linear Schrödinger dynamics at leading order at equilibrium tangent"; "vanishes entirely" → "drops out exactly at equilibrium, controlled perturbatively near it"
- Fixed Stage 1 of Prop `linearisation`: $U[\Psi_{\mathrm{st}}] = \sigma^2 V_W(\psi)$ is *state-independent*, not *constant* (a function of $\psi$)
- Fixed `H_W` non-negativity attribution: proved in XVII, not XVI

### Paper XXI (rounds 4 & 5)
- Resolved gauge-removability contradiction: XIX does prove non-removability under phase/linear-unitary transforms; the open question is broader classes of transformations
- Softened "Fréchet linearisation" language → "leading-order (formal) linearisation"
- Tightened abstract's "qualified positive answer" → "conditional, regime-restricted positive answer; full quantum mechanics not derived"
- Replaced "distinguished equilibrium tangent sector" → "leading-order equilibrium-tangent sector" throughout
- "demonstrates a mathematically consistent pathway" → "outlines a mathematically coherent but partly conditional pathway"

### Paper XXIX (rounds 4 & 5)
- Added missing `\Mcl` macro to preamble (compile error)
- Resolved the connected-subgraph vs disjoint-union conflict: Definition `def:probe` now explicitly states that probe observers have $\mathcal{O}$ a finite disjoint union of connected probe subregions, generalising the connected-region assumption of Definition 2
- Renamed §5 title: "Recovery of Quantum Measurement" → "Structural Placement of Quantum Measurement"
- Renamed §6 title: "Recovery of Relativistic Frames" → "Connection to Observer-Dependent Frames"
- Softened consciousness claims: "necessary structural conditions" → "candidate structural prerequisites"
- Tightened LMC downstream claim in Table 1 and in `rem:role_xxx`: LMC gives *numerator coincidence* only; non-contextuality of normalised probability requires an additional completeness hypothesis
- Softened "Physical measurement apparatuses are localised probe observers" → "Some measurement apparatuses can be modelled as localised probe observers"
- Softened XXIII global-clock claim: "structural explanation" → "structural compatibility"
- Softened "Both are instances of the same structural mechanism" → "The paper proposes to treat both as instances of the same structural mechanism"

### Paper XXX (round 12)
- Fixed Theorem `thm:noncontextuality` quantifier slide: state-specific hypothesis → state-specific conclusion, with explicit note that universal non-contextuality requires the strictly stronger universal-completeness hypothesis
- Added explicit state-completeness hypothesis (5) to Proposition `prop:born` — the proposition now derives the standard Born form `|c_i|^2` only under all five hypotheses; without state-completeness, the result is the conditional form `|c_i|^2 / ∑_{j∈adm}|c_j|^2`
- Updated abstract to stop over-stating Route E as "closure-derived forcing" — now "a conditional uniqueness argument given imported structures, not a derivation of the Born rule from closure alone"
- Added sector-supported caveat to the partial-observer formula in the abstract
- Updated synthesis paragraph to reflect the five-hypothesis structure of Proposition 1

## Final state after extended pass

All four papers now explicitly carry:
- Every hypothesis that was previously smuggled
- Every "imported from upstream" or "imported as cited result" acknowledgment
- The state-completeness vs universal-completeness distinction
- The sector-supported regime caveat for the partial-observer formula

The remaining flagged issues across all four papers are at the level of prose polish (specific wordings, formatting) rather than mathematical correctness or scope misstatement. Per reviewer critique, codex's "top 3" items after this pass are all refinements of already-flagged restrictions, not new defects.
