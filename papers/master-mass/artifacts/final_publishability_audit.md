# Final Publishability Audit — Papers I and II

## Part 2: Claim-Inflation Audit

### Paper I Flagged Phrases

| Line/Location | Current Phrase | Risk | Action | Revised |
|---------------|---------------|------|--------|---------|
| Abstract | "zero fitted parameters" | Medium | NEEDS QUALIFIER | "zero fitted continuous parameters" |
| Abstract | "structural agreement...at the ~2×10^{-4} relative level" | SAFE | Keep | — |
| Abstract | "falsifiable structural hypothesis" | SAFE | Keep | — |
| Sec 5, Theorem | "fixed integer determined by R1-R5 with zero free parameters" | Low | NEEDS QUALIFIER | "zero free continuous parameters" |
| Sec 11 | "All three terms are derived from the closure-class structure" | Medium | NEEDS QUALIFIER | "All three terms are obtained from the closure-class structure within the present framework" |
| Sec 12 | "arises from a single structural principle" | SAFE | Keep (true by construction) | — |
| Sec 13, Status table | "Established" (multiple rows) | Low | NEEDS QUALIFIER | Add "within framework" for derived items |
| Sec 14 | "three-order zero-parameter mass law" | Medium | Already qualified elsewhere | Add "continuous" before "parameters" |
| Conclusion | "established within the present framework" | SAFE | Keep | — |
| Conclusion | "falsifiable" | SAFE | Keep | — |

### Paper II Flagged Phrases

| Location | Current Phrase | Risk | Action | Revised |
|----------|---------------|------|--------|---------|
| Abstract | "exponent 1/phi...consistent with hydrogen-like spectral scaling" | SAFE | Keep (already qualified) | — |
| Abstract | "unique phi-integer-power" | SAFE | Keep (factually true) | — |
| Abstract | "zero fitted continuous parameters" | SAFE | Keep | — |
| Abstract | "spectral-dimension assumption...remain open" | SAFE | Keep (honest) | — |
| No-go section | "prove a formal no-go" | SAFE | Keep (it IS proved) | — |
| Operator section | "conditionally derived" | SAFE | Keep | — |
| Coefficient section | "structurally motivated" | SAFE | Keep | — |
| Conclusion | "structural mass architecture covering...three lepton generations" | Medium | NEEDS QUALIFIER | "structural mass architecture providing leading-order coverage of..." |

## Part 3: Notation Consistency

### Audit Results

| Symbol | Paper I Usage | Paper II Usage | Conflict? | Fix |
|--------|--------------|---------------|-----------|-----|
| \|E\| | Edge count (Sec 10, explicit disclaimer) | Edge count | No conflict | — |
| E_sum | Class energy (Sec 8) | Not used | No conflict | — |
| V | Vertex count | Vertex count | No conflict | — |
| C(A) | Combinatorial complexity | Same | No conflict | — |
| L | Graph Laplacian | Same | No conflict | — |
| w | Winding number (mentioned in R4) | Winding number (central) | No conflict | — |
| phi | Golden ratio (varphi macro) | Same macro | No conflict | — |
| f(w) | Not used | Winding operator | No conflict | — |
| N | Shell count (implicit) | Shell count (explicit) | Low risk | Paper I should define N if it appears |
| a | Not used | Winding coefficient | No conflict | — |
| delta_sigma | Mentioned (neutron/proton) | Used | Should be consistent | Ensure same notation |

**Required fixes:** Minor. Paper I should ensure N is defined if referenced in the closing paragraph pointing to Paper II.

## Part 4: Cross-Paper Consistency

### Verification

1. **Paper I does not overpromise Paper II:** Paper I closing says "A companion paper [II] proves that shell-support extension cannot produce heavier lepton generations and identifies a winding-dependent boundary excitation operator." This is accurate — Paper II does prove the no-go and does identify the operator.

2. **Paper II does not contradict Paper I:** Paper II explicitly preserves the three-order law (f(1)=0). No contradiction.

3. **Shared assumptions stated consistently:** Both use R1-R5, same phi-manifold, same closure-class definitions. Paper II references Paper I for these.

4. **Shared equations consistent:** The three-order law appears identically in both (by reference in Paper II).

5. **Paper II opens from Paper I's limitation:** Yes — Paper II intro states Paper I "cannot accommodate heavier lepton masses" and proves this as a theorem.

6. **Continuation, not repair:** Yes — Paper II reads as "the next layer" not "fixing a problem."

**Cross-reference text:**
- Paper I conclusion: "A companion paper [II] proves..."
- Paper II abstract: "The three-order baryon-lepton mass law of [I]..."
- Paper II intro: "A companion paper [I] establishes..."

## Part 6: Hostile Review Pass

### Paper I — Top 10 Likely Attacks

| # | Attack | Status | Fix |
|---|--------|--------|-----|
| 1 | "The phi-manifold is ad hoc" | Partially handled (Sec 4 assumptions) | Ensure Sec 4 explicitly calls it a modelling assumption |
| 2 | "R1-R5 are cherry-picked to give the right answer" | Partially handled (enumeration table) | Add sentence: "The rules are stated prior to evaluation; Table 1 shows they also exclude nearby alternatives" |
| 3 | "Zero parameters is misleading — discrete structural choices count" | Handled (Sec 1, "absence of fitted continuous parameters does not imply...") | Keep |
| 4 | "Only one ratio tested" | Handled (Sec 16 validation section) | Keep — explicitly states muon/tau fail |
| 5 | "0.02% could be coincidence" | Handled (Sec 16 "broader validation required") | Keep |
| 6 | "Degree-variance normalization is numerically selected" | Handled (Appendix B) | Ensure "within tested family" always present |
| 7 | "Why phi? Why not another irrational?" | Not handled | Add one sentence in Sec 4: "The choice of phi is motivated by its unique self-similar nesting property; the framework does not claim phi is the only possible geometric substrate" |
| 8 | "The three sectors are not proven independent" | Partially handled | Add: "The independence is asserted at leading order; subleading sector couplings may exist" |
| 9 | "No connection to QFT / Standard Model" | Handled (Discussion: "does not replace the Standard Model") | Keep |
| 10 | "Neutron/proton just says 'compatible'" | Handled (honest) | Keep |

### Paper II — Top 10 Likely Attacks

| # | Attack | Status | Fix |
|---|--------|--------|-----|
| 1 | "d = phi is assumed, not derived" | Handled (hardened wording) | Ensure "under the assumption" always present |
| 2 | "a = phi^5 is just a nice number" | Partially handled | Ensure "uniquely privileged within phi^k" is prominent |
| 3 | "Tau prediction has 3.7% error — that's weak" | Not explicitly handled | Add: "The tau prediction is a genuine test, not a calibration; the 3.7% error is the framework's current structural precision for this ratio" |
| 4 | "Only three particles tested" | Handled (scope limitation section) | Keep |
| 5 | "Winding number w is ad hoc" | Partially handled | Add: "Winding is a standard topological label in the closure-class definition (R4)" |
| 6 | "Why hydrogen-like scaling?" | Partially handled | Add: "This is the standard spectral scaling for principal quantum numbers; we adopt it as the simplest structural analogy compatible with the phi-manifold" |
| 7 | "The operator is not really derived" | Handled (claim level 3) | Keep — Paper II is honest about this |
| 8 | "This is numerology" | Main risk | The no-go theorem is the defense — it proves NECESSITY, not just curve fitting |
| 9 | "No dynamics — just a static classification" | Handled (Paper I establishes dynamics via crystallisation) | Add cross-reference to Paper I dynamics |
| 10 | "One calibration parameter (muon)" | Handled (a = phi^5 is structural, not calibrated) | But note: if a IS phi^5, then zero calibration. If a is from muon, then one calibration. Must be clear about which claim level is used |

## Part 8: Result Status Matrix

### Paper I

| Result | Status |
|--------|--------|
| Closure-class definition | Structural (definitional) |
| R1-R5 | Structural (postulated) |
| Electron {1} unique | Derived within framework |
| Proton {2,3,4} unique | Derived within framework |
| Delta C = 15 | Mathematically exact |
| Additive energy insufficient | Derived within framework |
| Bounds phi^15 — phi^16 | Derived within framework |
| Graph Laplacian term | Derived within framework |
| Degree-variance source | Derived within framework |
| Normalization |V|^2/|E| | Structurally selected (unique in tested family) |
| Exponent 1265/81 | Derived within framework |
| Ratio ~1835.8 | Numerically supported (2×10^{-4} structural agreement) |
| Neutron/proton scale | Compatible only |
| Muon/tau | Not reproduced (no-go in Paper II) |

### Paper II

| Result | Status |
|--------|--------|
| Shell-extension no-go | Mathematically exact |
| Winding mechanism necessity | Derived (from no-go) |
| Exponent 1/phi | Conditionally derived (requires d=phi assumption) |
| Identity phi/(phi+1) = 1/phi | Mathematically exact |
| Coefficient a = phi^5 | Structurally motivated (unique in phi^k) |
| Muon prediction (0.5%) | Numerically supported (if a = phi^5) |
| Tau prediction (3.7%) | Numerically supported (genuine prediction, not calibration) |
| Unified law form | Compatible (factorisation extended) |

## Part 9: Release Readiness

1. **Is Paper I release-ready?** YES — after applying the 4 minor fixes from the claim audit.

2. **Is Paper II release-ready?** YES — after applying the 3 minor fixes from the hostile review.

3. **Blocking issues?** None. All issues are wording-level, not structural.

4. **Simultaneous release?** YES — they are designed as a pair and should appear together.

5. **Final edits:**
   - Paper I: add "why phi" defense sentence, add sector-independence qualifier, ensure "continuous parameters" everywhere
   - Paper II: add tau-prediction defense sentence, add winding-label justification, clarify a = phi^5 vs calibrated-from-muon distinction
   - Both: final bibliography formatting, equation numbering check, section cross-references

### Pre-Release Checklist

- [ ] Paper I "why phi" sentence in Sec 4
- [ ] Paper I sector-independence qualifier
- [ ] Paper I "continuous parameters" audit
- [ ] Paper II tau-prediction defense
- [ ] Paper II winding-label justification
- [ ] Paper II a-vs-calibration clarity
- [ ] Cross-reference text finalized
- [ ] Bibliography entries for both papers
- [ ] Equation numbering sequential
- [ ] All symbols defined before first use
- [ ] PDF compilation test
