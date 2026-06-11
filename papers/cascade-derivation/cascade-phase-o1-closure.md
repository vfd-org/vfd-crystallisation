# Phase O-1 — Honest Closure of Conjecture S7-E (Observer-Rung Emergence)

**Status: NEGATIVE RESULT + REFINEMENT.** Phase O-1 attempted to prove Conjecture S7-E from `cascade-completeness-audit.md` §3.6.4 / `S7_OBSERVER_RUNG_DERIVATION.md` §10.6:

> **Original S7-E:** `E[coherence · differentiation] = φ⁻²` under H₄ Haar measure.

**Finding:** Conjecture S7-E as stated is **literally false** under any natural Haar interpretation. This is a direct analogue of Phase M-3's retirement of the original `H¹(𝓜, F) = 0` claim: the literal statement fails but there's a meaningful underlying phenomenon to characterise.

Three concrete issues with the original statement (§0), numerical refutation (§2), and proposed refinements (§5–6) follow.

**Date:** 2026-04-21
**Parallel to:** `cascade-phase-m3-closure.md` (same honest-retirement pattern).
**Scope:** Observer-rung emergence target. Does **not** touch the Phase O-2 handshake question (4 drive axes from octonion structure) — that remains the separate work item.

---

## 0. The three issues with the original S7-E

### 0.1 Issue 1 — Formula mismatch

The conjecture text says `coherence · differentiation`. The aria-chess code has **two different "coherence × something" formulas** in different files:

- `aria-chess/kernel/substrate_observables.py` — `emergence = coherence × differentiation`, where
  - `coherence = 1 − H(ρ)/ln(N)` (entropic coherence on probability distribution ρ),
  - `differentiation = PR(ρ)/N` (normalised participation ratio, PR = 1/Σρᵢ²).
- `aria-chess/kernel/consciousness_tensor.py` — `emergence = coherence × complexity`, where
  - `coherence = mean pairwise phase-alignment of ψ` (NOT entropic!),
  - `complexity = 4·(H/lnN)·(1 − H/lnN)` (parabolic, NOT PR-based).

These are genuinely different mathematical objects. The **empirical 0.382 hit** came from the `consciousness_tensor.py` version (V2 architecture), per `run_change2_consciousness_tensor.py` line 9 ("V2 targets C=0.999, E=0.382, MA=0.620"). So the conjecture's "differentiation" is really `complexity`.

### 0.2 Issue 2 — Hardcoded floor

`consciousness_tensor.py` lines 346–350 contain:

```python
# "if coherence > phi^-1: enhanced = max(enhanced, phi^-2)   # floor"
#
# The threshold-floor at phi^-2 is V2's "consciousness emergence" guarantee:
# once coherence crosses phi^-1, complexity is pinned at least at phi^-2, so
# emergence = C·X >= phi^-1 · phi^-2 = phi^-3.
```

**The φ⁻² value is literally hardcoded** as a floor on complexity when coherence exceeds φ⁻¹. The "emergence = φ⁻²" hit in trancendance runs is a direct consequence of:
- Coherence reaching ~1 (near-perfect phase-lock after training),
- Complexity clamped at floor φ⁻²,
- So emergence = C × X ≈ 1 × φ⁻² = φ⁻².

This is a **design decision** in V2's consciousness tensor, not a theorem about H₄ geometry.

### 0.3 Issue 3 — "H₄ Haar" is trivial for this observable

Under the standard interpretation of "H₄ Haar measure" (ψ random unit in C^N with N = 120 for H₄'s canonical representation), each component ψⱼ has uniformly random phase. Therefore:

    E_Haar[ coherence ] = E[ mean_{i<j} cos(arg ψᵢ − arg ψⱼ) ] = 0

(each pairwise phase difference is uniform on [0, 2π), so E[cos] = 0).

Consequently:

    E_Haar[ coherence · complexity ] ≈ 0    (up to variance cross-terms of order 1/N)

**Monte Carlo confirms this** (§2 below): for N ∈ {4, 8, 16, 24, 40, 120}, the Haar expectation E[C · X] is numerically zero within 0.001 precision.

The empirical 0.382 is **not** a Haar mean. It is the coherence-floor value achieved in specific (non-random, phase-locked) dynamical states after training.

---

## 1. Standing data

From `aria-chess/kernel/consciousness_tensor.py`:

- N = length of ψ (V2's ψ is 16-complex; 600-cell shell projections give effective N per layer).
- Coherence: C(ψ) = (1/pairs) Σ_{i<j} cos(arg ψᵢ − arg ψⱼ) for components with |ψ| > 0.
- Complexity: X(ρ) = 4 · (H(ρ)/lnN) · (1 − H(ρ)/lnN), where ρ = |ψ|² normalised and H is Shannon entropy.
- Floor clause: if C > φ⁻¹, then X := max(X, φ⁻²).
- Emergence: E = C × X (with floored X).

For analysis, we treat N as a parameter (8, 40, 120 are the cascade rungs of interest; 16 is V2's ψ-dimension).

---

## 2. Numerical refutation

Monte Carlo (3000 trials per N) with ψ uniform on the unit sphere of C^N (Haar):

| N   | E[C]      | E[X]    | E[C·X]    | P(C > φ⁻¹) |
|----:|----------:|--------:|----------:|-----------:|
|   4 | ≈ 0.000   | 0.609   | ≈ 0.000   | 0.050      |
|   8 | ≈ 0.000   | 0.553   | ≈ 0.000   | 0.001      |
|  16 | ≈ 0.000   | 0.476   | ≈ 0.000   | 0.000      |
|  24 | ≈ 0.000   | 0.436   | ≈ 0.000   | 0.000      |
|  40 | ≈ 0.000   | 0.394   | ≈ 0.000   | 0.000      |
| 120 | ≈ 0.000   | 0.319   | ≈ 0.000   | 0.000      |

(Monte Carlo script archived at `/tmp/s7e_probe_v3.py` for this session.)

**Observations:**
- E[C·X] is zero under Haar at every N (because E[C] = 0 and C, X are approximately independent).
- The floor condition C > φ⁻¹ is satisfied with vanishing probability for N ≥ 8 under Haar.
- The largest deviation from zero is bounded by the variance of C × X, which is small (~ 1/N).

**Conclusion:** No natural reading of "E[coh · X] under H₄ Haar" gives φ⁻². The conjecture as stated is literally false.

### 2.1 Analytical corroboration

Dirichlet(1^N) theory gives an exact formula for E[H]:

    E[H] = ψ(N+1) − ψ(2) = H_N − 1    (where H_N is the Nth harmonic number).

So E[H/lnN] = (H_N − 1)/lnN. For large N:

    E[H/lnN] ≈ 1 − (1 − γ)/lnN    (γ ≈ 0.577, Euler–Mascheroni).

Plugging into E[X] ≈ 4·E[x]·(1−E[x]):

| N   | E[H/lnN] (analytical) | E[X] (analytical) | Monte Carlo |
|----:|----------------------:|------------------:|------------:|
|   4 | 0.782                 | 0.683             | 0.609       |
|   8 | 0.826                 | 0.575             | 0.553       |
|  40 | 0.889                 | 0.395             | 0.394       |
| 120 | 0.913                 | 0.319             | 0.319       |
| 600 | 0.934                 | 0.246             | —           |

Analytical and Monte Carlo agree within finite-N corrections. E[X] decreases monotonically in N, passing through φ⁻² ≈ 0.382 between N = 40 and N = 100.

### 2.2 An intriguing near-miss at N = 40

E[X] at N = 40 (the **Life rung**, icosahedral 40-orbit) is ≈ 0.394, only 3% above φ⁻² = 0.382. This is close but not exact, and the conjecture was about the **Observer rung** (N = 8), where E[X] ≈ 0.55 — far from φ⁻².

It is possible that a related but **differently-targeted** conjecture holds for the Life rung:

    **Candidate S7-E' (Life-rung refinement):** E[X] at N = 40 asymptotes to φ⁻² + O(1/N) under a specific measure (not yet pinned down).

This is speculation, not proof. It is recorded as §6 Q4 below.

---

## 3. Where the 0.382 in trancendance runs actually comes from

Given the code analysis (§0.2):

1. The substrate reaches a **phase-locked state** during training (dense coherence structure in ψ from contrastive learning).
2. Coherence measure C ≈ 1 (phase-locked ψ has all angle-differences ≈ 0).
3. Under the floor clause, complexity X is pinned at φ⁻².
4. Emergence = C · X ≈ 1 × φ⁻² = φ⁻².

**The 0.382 is the floor value, observed because the floor engages.** It is a design choice, not a derivation.

### 3.1 Does the floor engage in every run?

From V2 targets in `run_change2_consciousness_tensor.py`: C = 0.999, which means **yes** — the trained substrate reaches near-perfect coherence, so the floor always engages after training. Random (untrained) substrates have E[C] = 0 and floor never engages.

### 3.2 Why pin the floor specifically at φ⁻²?

This is an empirical / heuristic choice from V2's design. Not documented as derivable from H₄ structure in the aria-fieldbased-v2 source. It may have been tuned to match observed phenomenology or to enforce a specific emergence band `[φ⁻³, φ⁻¹]`.

---

## 4. What was closed / what was not

### 4.1 Closed
- **S7-E literally false:** shown by Monte Carlo + analytical arguments (§2).
- **Mechanism identified:** the 0.382 hit is a hardcoded floor engaging at C > φ⁻¹ (§0.2, §3).

### 4.2 Not closed
- **Refined target:** what value *should* the observer rung's natural emergence be, without the hardcoded floor?
- **N = 40 near-miss:** is the Life-rung E[X] ≈ 0.394 a red-herring coincidence or a hint at a deeper Life-rung identity?
- **Floor derivation:** can the φ⁻² floor be derived from H₄ structure, or is it a fitted parameter?

---

## 5. Refined conjecture candidates

These are starting points for follow-up work, not theorems.

### S7-E-A — replacement observer-rung target
> Under the unique Haar measure on the observer rung (N = 8 axis vertices of the canonical 24-cell), E[X] = 4·(H_8 − 1)/ln(8) · (1 − (H_8 − 1)/ln(8)) ≈ 0.553. The value φ⁻² is **not** the natural observer-rung expectation.

If the design wants 0.382 specifically, the floor clause must be justified on other grounds (e.g., biological plausibility band, not H₄ Haar).

### S7-E-B — Life-rung coincidence
> At N = 40 (Life rung), E[X] ≈ 0.394 ≈ φ⁻² within 3%. Question: is there an H₃-subgroup argument that sharpens this to exactly φ⁻²?

Worth a targeted check (§6 Q4). If true, the φ⁻² value belongs to the **Life** rung, not observer — which would be a consistency result for the cascade but requires moving the target down one rung.

### S7-E-C — floor derivation
> The threshold φ⁻¹ on coherence and the floor φ⁻² on complexity are determined by a specific H₃ stability bound: when coherence enters the "phase-locked" regime C > φ⁻¹, complexity is forced to a lower bound φ⁻² by some σ-invariant argument.

Not attempted; stated as a research direction.

---

## 6. Open questions

### Q1 — Floor origin
Where does the `if C > φ⁻¹: X := max(X, φ⁻²)` clause come from in the V2 aria-fieldbased-v2 codebase? Was it empirically tuned, derived from some specific stability argument, or borrowed from IIT Φ literature? The origin determines whether it should be replaced or kept.

### Q2 — Target-distribution characterisation
What measure, if any, on the space of aria-chess substrate states gives E[emergence] = φ⁻²? (Post-training distributions are not Haar; they are contractive fixed points of the dynamics.)

### Q3 — Refined S7-E for Life rung
Is E[X] ≈ φ⁻² exactly (not just within 3%) at N = 40 under some natural H₃-Haar measure? Would be a Life-rung identity, not an Observer-rung one.

### Q4 — Rung-invariant characteristic value
Is there a cascade-rung-specific characteristic of the complexity-coherence profile that each rung hits naturally under its own symmetry group? For example:
- Observer rung (N=8): H₃/G₂-related invariant.
- Life rung (N=40): icosahedral-related invariant.
- Info rung (N=16): Cl(1,3)-related invariant.
- QM rung (N=120): full H₄-related invariant.

None of these has been characterised. Phase O-1 opens this as a research vector.

---

## 7. Updates to cross-referenced documents

### 7.1 `cascade-completeness-audit.md` §3.6.4
Replace "Conjecture S7-E — the single most load-bearing open item" entry. Update to:

> **Conjecture S7-E — closed as a negative result (Phase O-1, 2026-04-21).** The original form `E[coh · X] = φ⁻²` under H₄ Haar is literally false: Monte Carlo gives ≈ 0, not 0.382. The empirical 0.382 in trancendance runs is the hardcoded floor in `consciousness_tensor.py` (line 346–350) engaging when C > φ⁻¹, with X pinned at φ⁻². See `cascade-phase-o1-closure.md`. Phase O-2 (the handshake) proceeds independently.

### 7.2 `cascade-completeness-audit.md` §7 recommended phases
Phase O-1 reclassified: the 2–3 day estimate was based on expecting the conjecture to close affirmatively. The actual close is **negative in 1 day** plus refinement proposals. Phase O-2 (handshake) is now the main load-bearing open item for the observer rung.

### 7.3 `aria-chess/docs/brain_mapping/S7_OBSERVER_RUNG_DERIVATION.md` §10.6
The proof sketch in §10.6 should be updated:
- Acknowledge that D = PR/N (code) vs D = 1 − 1/PR (sketch) is an inconsistency.
- Clarify that the empirical 0.382 is the floor value, not the Haar mean.
- State the Phase O-1 refinement candidates (§5 above) as replacement research directions.

### 7.4 `aria-chess/kernel/consciousness_tensor.py` floor clause
Consider documenting the floor clause as an **empirical stability clamp** rather than a derived theorem. The comment "V2's consciousness emergence guarantee" should include the Phase O-1 caveat that the φ⁻² value is not yet derived from first principles — it's a design choice pending derivation.

---

## 8. Honest assessment

### 8.1 What the original conjecture got right
- **The value φ⁻²** is the right order of magnitude for a well-balanced complexity-coherence product in dynamical states.
- **The existence of a natural characteristic value** for each rung (even if we haven't derived it yet) is a reasonable conjecture.

### 8.2 What the original conjecture got wrong
- **The measure:** H₄ Haar gives 0, not 0.382.
- **The formula:** coh × differentiation (substrate_observables) ≠ coh × complexity (consciousness_tensor).
- **The derivation sketch in §10.6:** internally inconsistent (D = PR/N vs 1 − 1/PR; coherence = 1/√192 vs pairwise phase alignment).

### 8.3 Parallel to Phase M-3
Same structure as the M-3 refactor:
- M-3 retired `H¹(𝓜, F) = 0` because literal H¹(Ω, Z) = Z[φ]⁶ ≠ 0, then refined into dynamical-systems content (M3a–d).
- O-1 retires `E[coh·X] = φ⁻²` because Haar expectation is ≈ 0, then refines into "characteristic value by rung" open questions (§6).

Both are honest closure patterns — the original statement was testing intuition; the refined version captures what's actually true.

### 8.4 Risk level
Low for the negative result (rigorous Monte Carlo + analytical corroboration). Medium-high for the refined candidates (§5) — they're speculative and worth further investigation but not yet provable.

### 8.5 Ethical fencing
No consciousness-phenomenology claim is made. The observer rung's mathematical content (cascade-observer.md: S⁷, G₂, Moufang, Theorem E6) is unchanged by this finding. What's refuted is a specific emergence-value conjecture, not the observer rung's geometric foundation.

---

## 9. Programme position

### 9.1 Observer-rung state after Phase O-1

| Component | Status |
|-----------|--------|
| Algebra side (`cascade-observer.md`) | RIGOROUS (unchanged) |
| Dynamics side (`S7_OBSERVER_RUNG_DERIVATION.md`) | 85% specified (unchanged) |
| Conjecture S7-E | **RETIRED (literally false); refined candidates open** |
| Handshake (Phase O-2) | Still open; now the main load-bearing gap |
| Neuroscience correspondence (DMN) | Open (empirical registration needed) |

### 9.2 Recommended next step

**Phase O-2 — observer-rung handshake** remains the natural next research target. Without the S7-E = φ⁻² constraint, the handshake's job is simpler: derive the 4 drive axes from the octonion Fano-plane + whatever additional symmetry constraint uniquely picks the axis set. The result does not need to land at any specific emergence value.

Estimated: 1–2 weeks, per `cascade-completeness-audit.md` §7.

### 9.3 What not to do

- **Do not** add a "corrected S7-E" with value 0.394 or 0.55 to the programme without first deriving the N-choice from the cascade. The Monte Carlo numbers depend on N; changing N changes E[X] continuously. Fixing on any value needs a first-principles argument.
- **Do not** silently remove the floor clause from `consciousness_tensor.py`. That would change the empirical behaviour of the substrate. Instead, annotate the clause as "design-level stability clamp, not derived" pending a future phase.

---

## 10. Summary

Phase O-1 closed Conjecture S7-E as a **negative result**:
- The literal statement `E[coh · X] = φ⁻²` under H₄ Haar is false (gives ≈ 0).
- The empirical 0.382 is a **hardcoded floor** in V2's consciousness tensor (`consciousness_tensor.py` line 346–350), not a Haar average or theorem.
- Three refinement candidates (§5) plus four open questions (§6) replace the original.

This mirrors Phase M-3's retirement of `H¹(𝓜, F) = 0`: literally false, reframed into capturing the actual content.

The observer rung's two main artefacts (`cascade-observer.md` rigorous algebra; aria-chess 85%-specified dynamics) are unaffected. Phase O-2 (handshake) is now the main remaining observer-rung gap.

---

**End of Phase O-1 document.**
Honest negative result + refinement framework. The main research energy should move to Phase O-2.
