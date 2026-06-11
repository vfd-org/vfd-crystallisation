Read-only status: I did not edit files or run tests.

**SECTION A. Insight / External Content Relevance**

Already in cascade papers/programme:

- Paper 2 scope is narrow: it inherits `V_600 + Dic_5 + V_24` from Paper 1 and adds only the sigma-pair excitation [SCOPE.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/v600-hawking-quantum/SCOPE.md:9). Its target theorem and first-law identity are stated at [SCOPE.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/v600-hawking-quantum/SCOPE.md:15) and [SCOPE.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/v600-hawking-quantum/SCOPE.md:17).
- Paper 1 already supplies the setup: `V_600=2I`, `Dic_5`, `V_24=Fix(sigma)`, and per-coset `4 fixed / 16 mobile` [bekenstein-incidence.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/bekenstein-incidence/bekenstein-incidence.tex:37), [bekenstein-incidence.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/bekenstein-incidence/bekenstein-incidence.tex:310), [bekenstein-incidence.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/bekenstein-incidence/bekenstein-incidence.tex:409).
- Shared code already implements sigma and the canonical energy convention: `sigma_pair_energy(v)` returns Euclidean `|v-sigma(v)|^2`, with no half factor [sigma.py](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/v600-programme/lib/vfd_v600/sigma.py:37). The docstring explicitly records the prior extra-half correction [sigma.py](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/v600-programme/lib/vfd_v600/sigma.py:45).
- Existing tests cover zero energy on fixed vertices, uniform `5/2` on mobile vertices, and the first-law identity over non-bulk left cosets [test_operator_traces.py](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/v600-programme/tests/test_operator_traces.py:39), [test_operator_traces.py](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/v600-programme/tests/test_operator_traces.py:46), [test_operator_traces.py](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/v600-programme/tests/test_operator_traces.py:54).
- Classical/literature anchors are already local: Bekenstein/Hawking entries [references-shared.bib](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/v600-programme/references-shared.bib:74), Coxeter/Conway-Sloane/Humphreys [references-shared.bib](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/v600-programme/references-shared.bib:125), and explicit `H_4`/600-cell coordinates [cascade-algebraic-substrate.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:778).

Only in `insight.md` or prior-session/external material:

- E8/two-600-cell/fine-structure material appears at [insight.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/insight.md:47) and [insight.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/insight.md:178). It is not needed for Paper 2.
- God-prime/QMS-3/RH content appears at [insight.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/insight.md:670) and [insight.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/insight.md:724). Keep out of Paper 2.
- Pentagonal holonomy is relevant only as future dynamics, not this paper’s observable [insight.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/insight.md:830), [insight.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/insight.md:878).

**SECTION B. Priority Gaps To Close The Task**

B1. Energy convention lock.  
Object: `E: V_600 -> Q_{\ge 0}`, `E(v)=||v-sigma(v)||^2_Euclidean`. Bridges SCOPE, shared code, old Hawking script. Route: correction plus finite derivation. First step: state lemma `E(v)=0` on `V_24`, `E(v)=5/2` on the 96 golden vertices.

B2. Coordinate proof of the quantum.  
Object: golden-coordinate orbit `G_mob = V_600 \ V_24 -> Q`. Bridges computation to manuscript theorem. Route: new exact derivation. First step: for `v=1/2(0, ±phi^{-1}, ±1, ±phi)` up to even permutation, show `v-sigma(v)` has exactly two nonzero coordinates `±sqrt(5)/2`, hence Euclidean norm squared `5/4+5/4=5/2`.

B3. Rigorous orbit certificate.  
Object: subgroup `Gamma <= W(H_4)` acting on `V_600`, preferably signed even coordinate permutations `C_2^4 ⋊ A_4`; codomain: permutation group on 120 vertices. Bridges “why monochromatic” to a theorem-grade symmetry statement. Route: classical `H_4` plus exact finite computation. First step: verify `Gamma` preserves `V_600`, preserves `V_24`, commutes with `sigma`, and has one orbit of size 96 on `V_600\V_24`.

B4. Full `W(H_4)` wording precision.  
Object: `W(H_4)` action and `Stab_{W(H_4)}(V_24)` action. Bridges the current phrase “W(H4) transitivity on mobile” to a correct certificate. Route: alternative full-Coxeter route. First step: either generate all 14400 `W(H_4)` permutations and certify the `V_24` stabilizer has mobile orbit size 96, or explicitly name `Gamma <= W(H_4)` as the transitive symmetry used.

B5. Paper 1 import theorem.  
Object: coset data `C in G/H` or `H\G`, with `S(C)=|C∩V_24|`, `A(C)=|C\V_24|`. Bridges Paper 1 incidence to Paper 2 first law. Route: cite Paper 1, do not reprove. First step: theorem/corollary: every left and right `Dic_5` coset has `S=4`, `A=16`, using Paper 1 [bekenstein-incidence.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/bekenstein-incidence/bekenstein-incidence.tex:310).

B6. First-law finite identity.  
Object: maps `E_C=sum_{v in C\V24} E(v)`, `T_C=E_C/A(C)`, `S(C)=A(C)/4`. Bridges spectrum to thermodynamic analogy. Route: new algebraic corollary. First step: prove `E_C=16*(5/2)=40`, `T_C=5/2`, `E_C=T_C A`, `T_C S=E_C/4`.

B7. Verification script certificate.  
Object: `papers/v600-hawking-quantum/verify.py -> exit 0`. Bridges claims to reproducibility. Route: shared `vfd_v600` package plus new orbit checks. First step: assert spectrum `{0:24, 5/2:96}`, `Gamma` orbit structure, both left/right coset first laws.

**SECTION C. Reversals / Corrections**

- At `papers/v600-hawking-quantum/SCOPE.md:5` replace `E(v) := |v − σ(v)|²/2 takes a single value E_q = 5/2` with `E(v) := |v − σ(v)|²_Euclidean takes a single value E_q = 5/2`.
- At `papers/v600-hawking-quantum/SCOPE.md:14` replace `E(v) := |v − σ(v)|²_trace / 2 (icosian trace metric).` with `E(v) := |v − σ(v)|²_Euclidean, computed exactly in Q(sqrt(5)).`
- At `papers/v600-hawking-quantum/SCOPE.md:16` replace `W(H₄) acts transitively on σ-mobile orbit` with `the V_24-preserving W(H_4) subgroup acts transitively on the σ-mobile sector; verify.py certifies the orbit structure explicitly`.
- At `papers/v600-programme/lib/vfd_v600/sigma.py:11` replace `|v - σ(v)|² / 2 in trace-units` with `|v - σ(v)|²_Euclidean`.
- When copying `hawking_radiation_derivation.py`, replace its trace-half convention at lines 12-14 and 114-118 with the canonical Euclidean convention from `sigma_pair_energy`.

**SECTION D. Work Order For `paper.tex` + `verify.py`**

1. Create `papers/v600-hawking-quantum/paper.tex`.  
Acceptance: title/abstract state one theorem: `24` zero modes, `96` mobile modes at `E_q=5/2`; no PBH numerics, no Planck-continuum derivation, no `tau_sigma`.

2. Section 1, Introduction.  
Acceptance: cites Bekenstein 1973 and Hawking 1975 for context; cites Paper 1 for `V_600 + Dic_5 + V_24`; states this paper adds one observable.

3. Section 2, Setup From Paper 1.  
Acceptance: defines `K=Q(sqrt(5))`, `sigma`, `V_600=2I`, `V_24=Fix(sigma)`, `H=Dic_5`, and cosets; does not re-litigate Paper 1.

4. Section 3, Sigma-Pair Excitation.  
Acceptance: definition uses Euclidean norm with no half factor; includes coordinate lemma B2.

5. Section 4, Main Theorem.  
Acceptance: theorem states spectrum as `24 δ_0 + 96 δ_{5/2}`; proof has both coordinate derivation and symmetry/orbit explanation.

6. Section 5, First-Law Structure.  
Acceptance: per coset `A=16`, `S=4`, `E=40`, `T_H=E_q=5/2`, `E=T_H A`, `S=A/4`, `T_H S=E/4`.

7. Section 6, Interpretation And Scope.  
Acceptance: sigma-pair/Hawking reading is marked interpretive; semiclassical Planck recovery and PBH cutoff remain qualitative Tier-2; cascade-unit calibration is out.

8. Appendix, Verification Certificate.  
Acceptance: documents `verify.py` assertions and exact arithmetic.

9. Create `papers/v600-hawking-quantum/verify.py`.  
Must assert: `|V_600|=120`; `|V_24|=24`; `|mobile|=96`; fixed energy all zero; mobile energy set exactly `{Fraction(5,2)}`; orbit certificate from B3/B4; all left and right cosets have `S=4`, `A=16`, `E=40`, `T=5/2`, `T*S=E/4`.

**SECTION E. Route Audit**

Route Q, recommended for theorem proof: direct coordinate calculation on the 96 golden vertices. Short, exact, hard to attack.

Route K/Gamma, recommended for symmetry explanation: signed even coordinate permutations as a concrete `W(H_4)` subgroup. This gives the requested orbit certificate without building all 14400 Coxeter elements.

Route Full W: generate simple `H_4` reflections and certify `Stab(V_24)` orbit size 96. Strongest, but more implementation surface.

Route old trace metric: only acceptable if explicitly defined as `trace norm = 2 * Euclidean norm`; otherwise it reintroduces the factor mismatch.

**SECTION F. Top 3 Next Builds**

1. Convention correction at [SCOPE.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/v600-hawking-quantum/SCOPE.md:5), [SCOPE.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/v600-hawking-quantum/SCOPE.md:14), and [sigma.py](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/v600-programme/lib/vfd_v600/sigma.py:11): lock `E=Euclidean norm squared`.

2. `verify.py` orbit certificate anchored to [SCOPE.md](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/v600-hawking-quantum/SCOPE.md:16): certify the mobile orbit rigorously, not just the energy values.

3. `paper.tex` math spine anchored to Paper 1 incidence [bekenstein-incidence.tex](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/bekenstein-incidence/bekenstein-incidence.tex:409) and existing energy tests [test_operator_traces.py](/mnt/c/Users/nexus/OneDrive/Documents/My%20Projects/vfd-crystalisation-paper/papers/v600-programme/tests/test_operator_traces.py:46): write Sections 2-5 as definitions, lemmas, theorem, corollaries.
