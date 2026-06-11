**1. Claim Audit**
- "`a route to GRH over K would become thinkable`" is now properly softened and does not overclaim. The added caveat that a separate zero-locus theorem would still be needed is the right repair. `papers/cascade-derivation/cascade-observer-zeta.md:31-38`
- "`suggests ... φ-structured supports`" in §2.3 is now appropriately weak. The earlier field-level identification claim is gone. `papers/cascade-derivation/cascade-observer-zeta.md:198-201`
- "`P3 (open, under-specified)`" is now correctly rewritten as inheriting the openness of P2; the bad prime-partition reading is explicitly retracted. This residual is fixed. `papers/cascade-derivation/cascade-observer-zeta.md:320-339`
- "`would supply the missing framework for attempting a categorical route`" is the right softening in §7. This residual is fixed. `papers/cascade-derivation/cascade-observer-zeta.md:623-627`
- "`C6b ... CONDITIONAL on the candidate μ`" is the right status in the WO note. But the cited source does not itself say that; it still says "`P-A-Fano` is unconditional" while also leaning on a merely “most-natural candidate” μ. So the WO wording is repaired, but the attribution remains dirty. `papers/cascade-derivation/cascade-observer-zeta.md:421-424`, `papers/cascade-derivation/cascade-fano-grading-lift.md:209-215`, `...:231-233`
- The numerical claims in §§2.1-2.4 are established by the supplied scripts. I ran them; the reported counts and `100/100` coefficient matches are correct. `papers/cascade-derivation/cascade-observer-zeta.md:175-212`
- The candidate-definition paragraph in §3.1 still contains one unsupported equivalence: “no proper sub-coalgebra” is not shown equivalent to “no non-trivial coproduct decomposition,” because the note itself admits coproduct theory in `𝒞oalg(F)` is undeveloped. `papers/cascade-derivation/cascade-observer-zeta.md:268-282`
- §2.5 Prime Detector and §2.6 aria-chess remain unsupported in this repo. The cited artefacts are absent, so those claims are not locally auditable. `papers/cascade-derivation/cascade-observer-zeta.md:218-243`

**2. WO Acceptance Audit**
- There is still no numbered acceptance-criteria section. That is a WO-spec defect.
- Using the five Round-3 residuals you named as the de facto acceptance list:
- `1.` C6b downgraded to conditional: partially resolved. The WO text is fixed; the cited source still is not aligned.
- `2.` P3 rewritten with partition language retracted: resolved.
- `3.` §0 RH/GRH implication softened: resolved.
- `4.` §7 final paragraph softened: resolved.
- `5.` §2.3 “identifies” softened to “suggests”: resolved.
- Numbered open items inside the WO:
- `O1`: still open.
- `O2`: still open.
- `O3`: still open / not yet well-posed.
- `O4`: untouched.
- `O5`: untouched beyond restatement.
- `O6`: citation fixed; underlying inconsistency still open.
- `O7`: still open.

**3. Catalogue Audit**
- No observer-zeta math catalogue / ledger is supplied.
- `cascade-atlas.md` is not a substitute; it contains no observer-zeta entries.
- Therefore the note’s new objects are uncatalogued: the working definition in §3.1, P1-P5, P5-apex, and the numerical results in §§2.1-2.4.

**4. Attribution / External Consistency**
- The capstone citation is now used correctly for conditional final-coalgebra existence and degeneracy. `papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:155-170`
- The `cascade-rh-proof.md` attribution is accurate: that file really does identify cascade `σ` with `s ↔ 1-s`. `papers/cascade-derivation/cascade-rh-proof.md:115-121`
- The `cascade-sigma-rationality.tex` caution is accurate: that paper is narrow scalar-extension algebra, not a Mellin or RH paper. `papers/cascade-sigma-rationality/cascade-sigma-rationality.tex:59-66`
- `C6b` remains source-misaligned, as above.
- `C7` is still only working-note / simplified support. The cited `cascade-12d-closure.md` does not prove the shellwise swap claim, and the script explicitly says its decomposition is simplified. `papers/cascade-derivation/cascade-observer-zeta.md:424`, `papers/cascade-derivation/cascade-12d-closure.md:47`, `papers/cascade-derivation/scripts/dual_600cell_factor2.py:142-144`
- The O6 inconsistency is real: `cascade-12d-closure.md` uses the naive icosian description, while `cascade-algebraic-substrate.tex` explicitly rejects it. `papers/cascade-derivation/cascade-12d-closure.md:39`, `papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:503-513`
- Prime Detector and aria-chess remain unverified because the files are absent.

**5. Sim Correctness**
- `observer_prime_inert_split.py`: correct for the splitting-count claim.
- `observer_zeta_candidate.py`: correctly implements the two toy negative results.
- `observer_zeta_dedekind.py`: correctly implements the classical Dedekind coefficient identity and the corrected Euler-factor reading.
- No χ² / KL / null-hypothesis machinery is present, so there is nothing to audit there.
- No Prime Detector sim is supplied.

**6. Tightness**
- `papers/cascade-derivation/cascade-observer-zeta.md:218-243`: either remove §§2.5-2.6 or mark them explicitly “external anecdotal motivation; not audited in this repo.”
- `papers/cascade-derivation/cascade-observer-zeta.md:421-424`: for `C6b`, say “WO reviewer downgrade; cited source itself still states unconditional P-A-Fano.”
- `papers/cascade-derivation/cascade-observer-zeta.md:268-273`: drop “equivalently” unless you actually prove coproducts exist in `𝒞oalg(F)`.

**7. Top Three Fixes**
1. Remove or quarantine the unsupported external-evidence sections. `papers/cascade-derivation/cascade-observer-zeta.md:218-243`
2. Repair the `C6b/C7` source-status mismatch instead of relying on reviewer-side reinterpretation. `papers/cascade-derivation/cascade-observer-zeta.md:421-424`
3. Supply an actual observer-zeta ledger, or stop claiming the note “catalogues” the programme objects. `papers/cascade-derivation/cascade-observer-zeta.md:27`, `...:684-704`

**8. Verdict**
- Publication ready: no.

The five Round-3 residuals you asked about are mostly fixed in the WO text itself. What still blocks publication, even at problem-statement scope, is attribution drift in `C6b/C7`, the unsupported §2.5/§2.6 evidence, and the absence of the promised catalogue.
