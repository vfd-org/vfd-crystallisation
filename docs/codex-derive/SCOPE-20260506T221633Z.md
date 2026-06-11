**SECTION A. Insight / External Content Relevance**

**Already in cascade papers / repo artifacts**

Paper 1 gives the theorem-grade substrate:
- `papers/bekenstein-incidence/bekenstein-incidence.tex:162-186` defines the 12 length-10 `T_tau` cycles and proves the K-multiset `{72:1, 0:1, 52:5, 20:5}`.
- `papers/bekenstein-incidence/bekenstein-incidence.tex:193-203` defines `H = Dic_5` as the union of the `K=72` and `K=0` cycles.
- `papers/bekenstein-incidence/bekenstein-incidence.tex:218-255` gives the right-coset carrier fact: each non-bulk right coset is one `K=52` cycle plus one `K=20` cycle.
- `papers/bekenstein-incidence/bekenstein-incidence.tex:430-448` is the right credibility model: exact arithmetic separated from interpretation.

Paper 3 supplies the tau-sigma bridge:
- `papers/tau-sigma-construction/tau-sigma-construction.tex:139-151` states the right-coset `K=52`/`K=20` pairing.
- `papers/tau-sigma-construction/tau-sigma-construction.tex:225-234` defines cycle phase swaps.
- `papers/tau-sigma-construction/tau-sigma-construction.tex:356-406` proves `tau_sigma` is an involution, fixes `Dic_5`, swaps `K=52 <-> K=20`, and commutes with `T_tau`.
- `papers/tau-sigma-construction/tau-sigma-construction.tex:410-434` matters: there are `2^5 = 32` valid phase lifts. Paper 4 must prove its cycle-space claims are phase-independent.

Paper 4 code currently proves Layer 1 traces once the operators are defined:
- `papers/v600-programme/lib/vfd_v600/operators.py:18-52` defines `I_12`, `P_K`, `H = I_12 + P_72`, `C = I_12 - P_0`, and `trace_ratio`.
- `papers/v600-programme/tests/test_operator_traces.py:12-36` tests `tr(I_12)=12`, projector ranks, `tr(H)=13`, `tr(C)=11`, and ratios `13/12`, `11/12`.
- `papers/v600-programme/lib/vfd_v600/group.py:66-84` is the safer exact K-class construction; it avoids the float shell sorting still present in the old inherited script at `papers/cosmological-folding-rate/dynamics/od1_operator_derivation.py:76-80`.

Prior OD1 notes are directly relevant as reversals to absorb:
- `papers/cosmological-folding-rate/dynamics/OD1_STATUS.md:3-6` says the older mode-count derivation was not closed.
- `OD1_STATUS.md:83-87` says mode-counting alone does not select `13/12`.
- `MISSING_MATH.md:3-10` identifies the exact missing projection rule: select 13 live modes out of 17.
- `MISSING_MATH.md:16-30` gives the most rigorous possible upgrade route: H4 representation decomposition of the sigma-antisymmetric module.

**Only in insight.md / prior-session material**

Mostly not theorem-grade for Paper 4:
- E8 double-cover / two-600-cell content at `insight.md:47-64`, `insight.md:249-328`, `insight.md:345-388` is interpretive or relevant only as a distant analogy for coupling/selection. Do not import into Paper 4 Layer 1.
- RH / god-prime / QMS material at `insight.md:641-715` is not directly relevant to Paper 4.
- Pentagonal holonomy at `insight.md:835-890` is relevant only as a future Route H for a real cycle-mode coupling law. It is exactly not yet in repo as a mathematical object (`insight.md:887-890`).

**External literature**

Use only as Layer 2 observation anchors:
- Planck 2018: `H0 ≈ 67.36/67.37`, `sigma8 ≈ 0.8111`, source: Planck Collaboration 2020, A&A 641 A6. Repo bib at `papers/v600-programme/references-shared.bib:149-156`; A&A page: https://www.aanda.org/articles/aa/abs/2020/09/aa33910-18/aa33910-18.html
- SH0ES 2022: `H0 = 73.04 ± 1.04`, source: Riess et al. 2022 ApJL 934 L7. Repo bib at `references-shared.bib:158-165`; abstract/value source: https://scixplorer.org/abs/2022ApJ...934L...7R/abstract
- KiDS: be precise. Public clean source gives `S8 = 0.759^{+0.024}_{-0.021}` for KiDS-1000 cosmic shear, not plain `sigma8`; A&A page: https://www.aanda.org/articles/aa/abs/2021/01/aa39070-20/aa39070-20.html

**SECTION B. Priority Gaps To Close The Task**

**B1. K-Saturated Admissibility Theorem**

Object: admissible rank-one K-projector classification.  
Domain/codomain: `A_K ⊂ End_Q(C_Q)`, where `C_Q = Q^12` with basis the 12 `T_tau` cycles; `A_K = span_Q{P_72, P_0, P_52, P_20}` or its projector semiring.  
Bridge: turns SCOPE’s “forcing theorem” into a true finite linear-algebra theorem.  
Route: new derivation from Paper 1 K-multiset plus Paper 3 tau-sigma pairing.  
First lemma: “The only rank-one K-saturated diagonal projectors in `End_Q(C_Q)` are `P_72` and `P_0`; `P_52` and `P_20` have rank 5. Therefore the only signed rank-one K-class corrections to `I_C` are `±P_72`, `±P_0`.”  
Hostile note: tau-sigma equivariance alone does not exclude arbitrary rank-one projectors in symmetric/antisymmetric paired subspaces. The theorem is true only after “K-saturated / K-class projector / diagonal in cycle basis” is explicit.

**B2. Trace Identity Theorem**

Object: `Hhat = I_C + P_72`, `Chat = I_C - P_0`.  
Domain/codomain: self-adjoint diagonal operators `C_Q -> C_Q`.  
Bridge: theorem-grade Layer 1.  
Route: already implemented in `operators.py` and `test_operator_traces.py`.  
First lemma: “For a diagonal projector `P_K`, `tr(P_K)=rank(P_K)=m_K`; hence `tr(I_C+P_72)=12+1=13` and `tr(I_C-P_0)=12-1=11`.”

**B3. Baseline Rule**

Object: baseline map `B_LCDM := I_C`.  
Domain/codomain: K-blind uniform cycle weighting to `End_Q(C_Q)`.  
Bridge: justifies why the denominator is 12.  
Route: new definitional/axiomatic bridge, not a tau-sigma theorem.  
First step: define “K-blind uniform cycle baseline” as the operator assigning coefficient 1 to every cycle basis vector. Then `I_C` is unique by definition in that class. Do not claim `I_12` is the unique tau-sigma-invariant rank-12 operator; that is false without extra restrictions.

**B4. Empirical Observation Table**

Object: observation map from published values to residuals.  
Domain/codomain: `(early benchmark, signed trace ratio, late benchmark) -> z residual`.  
Bridge: Layer 2 only.  
Route: external literature plus repo scripts.  
First step: table with exact arithmetic:
- `67.36 * 13/12 = 72.9733`; compare SH0ES `73.04 ± 1.04`.
- `0.8111 * 11/12 = 0.7435`; compare KiDS `sigma8 = 0.760 ± 0.021` if that exact sigma8 source is pinned.
- If using KiDS `S8`, write `0.832 * 11/12 = 0.7627` vs `0.759`, residual `~0.14σ`. Do not use the `≤0.1σ` line for plain `sigma8`.

**B5. Coupling Rule Hypothesis**

Object: signed coupling map  
`Gamma: {scale-rate, clustering-amplitude} -> {+P_72, -P_0}`.  
Domain/codomain: observable classes to signed admissible projectors.  
Bridge: Layer 3; connects math operators to H0 and sigma8.  
Route: hypothesis with physical motivation, not theorem.  
First statement: “Assuming scale-setting observables couple to max-K and clustering amplitudes exclude the trivial K=0 mode, the signed operators are `I+P_72` and `I-P_0`.”  
Keep this visibly below Layer 1.

**B6. Tau-Sigma Phase-Independence Lemma**

Object: induced cycle-space action of any admissible `tau_sigma` lift.  
Domain/codomain: `32` vertex maps from Paper 3 to a cycle-pairing map on `C_Q`.  
Bridge: prevents Paper 4 from depending on the arbitrary all-zero lift.  
Route: Paper 3 plus a short quotient proof.  
First lemma: “All `2^5` phase choices exchange the same `K=52` and `K=20` cycle carriers on the cycle quotient; hence `P_72`, `P_0`, and the K-saturated admissibility theorem are phase-independent.”

**B7. OD1 Mode-Count Reconciliation**

Object: relation between trace-projector theorem and older 17/12 orthonormal mode count.  
Bridge: prevents reviewers from finding the repo’s own contradiction first.  
Route: explicit scope paragraph.  
First step: “This paper proves a K-saturated operator-trace identity. It does not claim that unconstrained orthonormal sigma-mode counting gives the same result; upgrading the coupling rule to mode dynamics requires the H4 representation build of `MISSING_MATH.md:16-30`.”

**B8. Verification Script Hygiene**

Object: Paper 4 verification appendix.  
Bridge: makes theorem reproducible without legacy float code.  
Route: use `vfd_v600.group.build_state()` and `vfd_v600.operators`, not `od1_operator_derivation.py`.  
First step: appendix script imports `build_state`, asserts exact K-multiset, asserts projector ranks/traces, then optionally asserts tau-sigma properties.

**SECTION C. Reversals / Surgical Corrections**

1. At `papers/v600-cosmic-tensions/SCOPE.md:5` replace  
`The H_0 and σ_8 cosmological tensions close to ≤ 0.1σ via two unique rank-1 corrections`  
with  
`The H_0 tension closes at 0.06σ and the σ_8/S_8 tension lands within the weak-lensing uncertainty via two rank-one K-class projector corrections`.

2. At `papers/v600-cosmic-tensions/SCOPE.md:21` replace  
`the *only* rank-1 corrections to I_12 are ±P_72 and ±P_0`  
with  
`the only rank-one K-saturated diagonal projector corrections to I_12 are ±P_72 and ±P_0`.

3. At `papers/v600-cosmic-tensions/SCOPE.md:43` replace  
`only ±P_72 and ±P_0 are admissible. Proof.`  
with  
`only ±P_72 and ±P_0 are admissible among K-saturated diagonal projector corrections. Proof with admissibility hypotheses stated first.`

4. At `papers/v600-cosmic-tensions/SCOPE.md:53` replace  
`we prove that ±P_72 and ±P_0 are the only rank-1 corrections to I_12 admissible without violating either K-multiplicity or τ_σ-equivariance`  
with  
`we prove that ±P_72 and ±P_0 are the only rank-one K-class projector corrections to I_12; arbitrary rank-one subprojectors are outside the admissible K-saturated operator algebra`.

5. At `papers/v600-cosmic-tensions/SCOPE.md:62` replace  
`I_12 is the unique τ_σ-invariant rank-12 operator on C`  
with  
`I_12 is the unique K-blind uniform cycle baseline once the baseline is defined as unit weight on every T_tau cycle`.

6. At `papers/cosmological-folding-rate/dynamics/od1_operator_derivation.py:18` replace  
`Operators we DERIVE (not posit):`  
with  
`Operators for the K-saturated trace theorem:`.

7. At `papers/cosmological-folding-rate/dynamics/od1_operator_derivation.py:185-186` replace  
`This is now a derivation, not an assertion: given (V_600, K-multiset, τ_σ), the modification factors 13/12 and 11/12 are FORCED.`  
with  
`Given the K-saturated admissibility criterion, the trace factors 13/12 and 11/12 follow exactly; the observable coupling rule remains a separately stated hypothesis.`

**SECTION D. Alternative Routes**

**Route Q: Quotient / K-Saturated Trace Route**

Use this for Paper 4 Layer 1. Work entirely in `C_Q = Q^12` and the K-class projector algebra. This proves `13` and `11` cleanly. It does not prove the physical coupling.

**Route R: H4 Representation Route**

Use this only if upgrading Layer 3 toward theorem-grade. It is the `MISSING_MATH.md:16-30` route: decompose the five sigma-antisymmetric pair modes as `1 ⊕ 4`, then only the scalar/trivial piece couples. First hard step: define the actual group action on the cycle-pair module; full `H4` may not preserve a chosen `tau`, so the preserving subgroup may be the correct object.

**Route K: K-Weighted Trace Route**

Candidate route from `MISSING_MATH.md:125-135`. It tries to derive admissibility from K-weights. It is finite and computable but currently ad hoc. Use only as a backup if Route R fails.

**Route H: Pentagonal Holonomy Route**

Insight-only future dynamics: `insight.md:878-882` proposes a `Z[phi]^x`-valued 1-cocycle on the 600-cell edge graph and a clock map. This could become a genuine cycle-mode coupling law, but it is not needed for Paper 4 theorem-grade trace identities.

**SECTION E. Layer Discipline**

Layer 1 theorem-grade:
- `C_Q = Q^12`.
- `P_K` are K-class diagonal projectors.
- `tr(I + P_72)=13`; `tr(I - P_0)=11`.
- admissibility theorem only for K-saturated diagonal projector corrections.

Layer 2 observation:
- numerical match to H0 and sigma8/S8 benchmarks.
- no dynamical cosmology claimed.
- pin exact measurement choices and residual formula.

Layer 3 hypothesis:
- `H0 -> +P_72`, `sigma8 -> -P_0`.
- call it a coupling rule, not a forcing theorem.
- falsifiable by future measurements, but not mathematically forced by the trace identity.

**SECTION F. Top 3 Next Builds**

1. `papers/v600-cosmic-tensions/SCOPE.md:43`  
Build: replace “forcing theorem” with the formal K-saturated admissibility theorem. Mathematical content: define `C_Q`, `A_K`, admissible corrections, prove only `P_72` and `P_0` are rank-one K-class projectors.

2. `papers/v600-programme/lib/vfd_v600/operators.py:18-52` and `papers/v600-programme/tests/test_operator_traces.py:12-36`  
Build: Paper 4 appendix proof/verification. Mathematical content: exact projector ranks, traces, and rational ratios over `Q^12`; use shared exact state construction from `group.py:66-84`.

3. `papers/v600-cosmic-tensions/SCOPE.md:22-24`  
Build: split sign/coupling and empirical match into Layer 2/Layer 3 language. Mathematical content: `Gamma(scale-rate)=+P_72`, `Gamma(clustering)=-P_0` as hypothesis; table computes H0, sigma8, and S8 residuals with pinned external citations.
