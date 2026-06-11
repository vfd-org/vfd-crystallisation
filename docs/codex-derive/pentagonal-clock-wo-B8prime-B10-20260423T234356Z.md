**SECTION A. Insight / External Content Relevance**

Already in cascade papers/docs:
- F1 gives `φ` and `σ(φ)=1-φ=-1/φ`: `docs/pentagonal-torsion-derivation.md:21-33`, `papers/cascade-12d-closure/cascade-12d-closure.tex:249-269`.
- `Z[φ]=O_K`, PID/free-module substrate: `papers/cascade-12d-closure/cascade-12d-closure.tex:284-320`.
- `2I` as 600-cell vertex set, exact shell = conjugacy class: `papers/paper-xxii/paper-xxii.tex:200-219`; verifier states exact `Q(√5)` shell/class claims at `papers/paper-xxii/scripts/run_icosian_exact.py:13-21`.
- E8/icosian conjugate-pair substrate for B10: `papers/cascade-12d-closure/cascade-12d-closure.tex:380-391`, and two-to-one `E8 -> H4` pairing at `papers/paper-xxii/paper-xxii.tex:234-238`.
- Existing clock facts: order-10 `τ`, `T(v)=τv`, 12 cycles of length 10, unweighted zeta `(1-z^10)^(-12)` are at `docs/pentagonal-torsion-derivation.md:230-245` and implemented in `derive_pentagonal_clock_B5_B6.py:223-258`.

Only in `insight.md` / prior-session:
- The local-frame holonomy idea is directly relevant: dynamics should live in transition data, not the static bundle, `insight.md:846-851`.
- Weighted closed holonomy loops and `Z[φ]^×`-valued Artin-Mazur zeta are proposed at `insight.md:855-861`.
- The explicit missing object is a pentagonal holonomy connection on the 600-cell edge graph with `σ` as parallel transport: `insight.md:878-890`.
- God-prime / P5 material is later observer-zeta context, not needed for B8′-B10: `insight.md:652-659`, `670-689`, `713-715`.

**SECTION B. Priority Gaps To Close The Task**

B1. **B8′ minimal clock cocycle**
- Object: transformation-groupoid cocycle  
  `ω_+ : E_T^+={(v,Tv): v∈2I} -> Z[φ]^×`.
- Chosen construction: Route Q-min, a vertex-shell potential. Let `s(v)∈{0,...,8}` be the exact Euclidean shell index from identity, `r(v)=s(v)-4`, `κ(v)=r(v)^2`, and define  
  `ω_+(v,Tv)=φ^{κ(v)}`.
- Bridges: avoids constant transport `g(v,Tv)=τ`; uses only F1 `φ`, exact icosian shells, identity, and antipodal midpoint.
- First step: prove affine shell grades give constant/trivial cycle totals, while `κ=r^2` is the lowest-degree antipodal-even radial grade distinguishing cycle profiles.

B2. **B8′ cycle-profile invariant**
- Object: `P(C)=(# {v∈C : s(v)=j})_{j=0}^8 ∈ N^9`.
- Bridges: replaces noncanonical “representative class” with full 10-cycle data.
- First step: exact sim should report the four profile types, multiplicities `1,1,5,5`:
  - `{0:1,1:2,3:2,5:2,7:2,8:1}` gives `K_C=72`, `W_C=φ^72`.
  - `{4:10}` gives `K_C=0`, `W_C=1`.
  - `{1:2,2:2,4:2,6:2,7:2}` gives `K_C=52`, `W_C=φ^52`.
  - `{2:2,3:2,4:2,5:2,6:2}` gives `K_C=20`, `W_C=φ^20`.

B3. **B9 weighted Artin-Mazur zeta**
- Object:  
  `ζ_{T,ω}(z)=∏_C (1-W_C z^{|C|})^{-1} ∈ Z[φ][[z]]`.
- For chosen B8′:
  `ζ_+(z)=(1-φ^72 z^10)^-1(1-z^10)^-1(1-φ^52 z^10)^-5(1-φ^20 z^10)^-5`.
- Degree-30 inspection with `t=z^10`:
  `a1 = 1 + 5φ^20 + 5φ^52 + φ^72`.
  `a2 = 1 + 5φ^20 + 15φ^40 + 5φ^52 + 26φ^72 + 5φ^92 + 15φ^104 + 5φ^124 + φ^144`.
  `a3` should be computed by exact exponent-polynomial multiplication.
- First step: implement `φ^n` multiplication by integer recurrence / `Fraction` pairs, no floats.

B4. **B10 σ-equivariance theorem**
- Correct substrate: `V~ = 2I_+ ⊔ 2I_-`, where `2I_- := σ(2I_+)`, not one `2I`.
- Maps: `Σ(v)=σ(v)` swaps copies; `T_+(v)=τv`; `T_-(σ(v))=σ(τ)σ(v)`.
- Theorem: `Σ ∘ T_+ = T_- ∘ Σ`, hence globally `ΣT=TΣ` on `V~`.
- Cocycle covariance: define `ω_-(Σe)=σ(ω_+(e))`; then `W_{ΣC}=σ(W_C)`.
- Zeta consequence: `ζ_sym = ζ_+ · σ(ζ_+)`. For the chosen even exponents, paired factors are σ-fixed and canonically integer-coefficient after pairing.

**SECTION C. Reversals / Corrections**

- at `papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:353` replace “Alternative construction (BUILD REVISION): weight each” with “B8′ construction: weight each cycle by its full shell-profile invariant;”
- at `papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:354` replace “cycle by the H₄-orbit class of its representative vertex.” with “do not use a smallest-index representative as a mathematical invariant.”
- at `papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:372` replace “B7: 12-regular adjacency graph built; σ permutes 2I; σ-” with “B7: 12-regular adjacency graph built; σ does not preserve one 2I;”
- at `papers/cascade-derivation/scripts/derive_pentagonal_clock_B7_B8.py:373` replace “covariance on adjacency verified.” with “covariance must be stated on 2I ⊔ σ(2I).”
- at `docs/pentagonal-torsion-derivation.md:272` replace “ω is to be H₄-equivariant and σ-covariant: ω(σv,σw)=σ(ω(v,w)).” with “ω is σ-covariant only on the conjugate-pair substrate 2I ⊔ σ(2I), with Σ(v)=σ(v) swapping copies and ω(Σe)=σ(ω(e)).”

**SECTION D. Route Alternatives**

- Route Q-min, chosen: shell-profile transformation cocycle on `T`-edges. Lowest implementation load; exact `W_C` table available.
- Route K: full local-frame holonomy from `insight.md:878-889`. Best conceptual match, but requires proving canonical frame gauge.
- Route C: two-copy bipartite edge cocycle on `2I ⊔ σ(2I)`. Natural for B10, but unnecessary for minimal B8′ unless Route Q-min fails certification.

**SECTION E. Exact Verification Targets**

- B8′: compute shell profiles for all 12 cycles; assert `W_C` multiset `{φ^72:1, 1:1, φ^52:5, φ^20:5}`.
- B9: compute zeta coefficients through `z^30` exactly in `Z[φ]`.
- B10: verify `σ(τv)=σ(τ)σ(v)` for all 120 vertices and that `σ(2I)` is the second copy.
- Harness correction: remove float sorting/comparison from B7/B8 certification path; `derive_pentagonal_clock_B7_B8.py:94-99` currently uses floats for ordering.

**SECTION F. Top 3 Next Builds**

1. `derive_pentagonal_clock_B7_B8.py:353-367`: replace representative-class counting with full cycle shell-profile computation and `κ=(s-4)^2`.
2. `docs/pentagonal-torsion-derivation.md:293-312`: insert B9 product formula, exact `W_C` table, and degree-30 coefficient target.
3. `docs/pentagonal-torsion-derivation.md:272-280` plus `cascade-12d-closure.tex:380-391`: state B10 on `2I ⊔ σ(2I)` with `ΣT=TΣ` and `ω(Σe)=σ(ω(e))`.

No files edited.
