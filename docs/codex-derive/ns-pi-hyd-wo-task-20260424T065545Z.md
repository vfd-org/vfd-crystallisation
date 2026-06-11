No files edited.

**SECTION A. Insight / External Content Relevance**

Already in cascade papers:

- `H_NS` is explicitly the missing bridge in [ns-formal.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/millennium-ns-formal/ns-formal.tex:47>): cascade spectral bounds plus coarse-graining should imply a uniform `L^\infty` vorticity bound, then BKM applies. The paper currently states this as conditional at [ns-formal.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/millennium-ns-formal/ns-formal.tex:347>) and [ns-formal.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/millennium-ns-formal/ns-formal.tex:440>).
- `Π_hyd^(n): X_n -> U_n x P_n` is defined in P7 at [cascade-hydrodynamic-projection.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-hydrodynamic-projection/cascade-hydrodynamic-projection.tex:442>). P7 proves finite-level boundedness, but its stated sup bound has level dependence `C_\Pi^(n) ~ h_n^{-3/2}` at [cascade-hydrodynamic-projection.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-hydrodynamic-projection/cascade-hydrodynamic-projection.tex:457>), so it does not yet close a uniform vorticity bound.
- The exact H4/600-cell spectrum is in P2, not Foundations F4: shell sizes at [cascade-algebraic-substrate.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:1062>) and eigenvalue table at [cascade-algebraic-substrate.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:1116>). Paper XXII reuses it with exact-script support at [paper-xxii.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/paper-xxii/paper-xxii.tex:169>).
- P4 gives finite-dimensional gradient flow and closure energy dissipation at [cascade-closure-dynamics.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:640>), but warns that norm decay needs `L_n >= 0` at [cascade-closure-dynamics.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-closure-dynamics/cascade-closure-dynamics.tex:669>).
- Z[φ] truncation/shell summability is present in consolidation notes: character lattice `Z[φ]^6` at [legacy-master-math-consolidation.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/legacy-master-math-consolidation.md:122>) and exponential truncation at [legacy-master-math-consolidation.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/legacy-master-math-consolidation.md:626>). G5 is marked closed in [cascade-g6-cleanup-closures.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-derivation/cascade-g6-cleanup-closures.md:198>).

Only in `insight.md` or external literature:

- `insight.md` adds stronger prior-session spectral material: E8/600-cell double-cover relevance at [insight.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/insight.md:47>) and multi-shell NNN eigenvalue computations at [insight.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/insight.md:106>). This can support an H4 spectral package, but current papers only formalize the 600-cell spectrum.
- Pentagonal holonomy appears only as a new route in `insight.md`: local `Z[φ]^×` cocycle/clock map at [insight.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/insight.md:878>) and explicit note that it is not yet in repo at [insight.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/insight.md:887>).
- QMS-3/god-prime material in `insight.md` around [insight.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/insight.md:670>) is not load-bearing for the NS vorticity bridge except as background arithmetic culture.
- External PDE layer should cite Beale-Kato-Majda 1984 for continuation, plus Ladyzhenskaya, Lions, Constantin-Foias, Temam for classical NS existence/regularity framework.

**SECTION B. Priority Gaps To Close The Task**

B1. **H4 spectral package.**  
Object: exact spectral theorem for `Δ_H4: l^2(V_600) -> l^2(V_600)` with projections `P_λ`, `W_int`, `W_irr`.  
Bridges: “F4 bounded discrete cascade spectrum” to an actual bounded operator source.  
Route: classical finite representation theory plus P2/Paper XXII.  
First step: define `Λ_H4 = max spec(Δ_H4) = 9 + 3√5` and separate this from P4 closure-generator bounds `||L_n||`.

B2. **H4-to-D4 hydrodynamic transfer.**  
Object/map: `T_HD^(n): W_int ⊂ l^2(V_600) -> X_n^{D4}` or directly into P7 current observables `J_n`.  
Bridges: H4 spectral control to the D4/P7 hydrodynamic projector.  
Route: new derivation using 600-cell-to-24-cell/Schläfli averaging.  
First step: define five 24-cell/D4 subaverages and prove `T_HD^(n) P_λ` is uniformly bounded and has controlled commutator with `L_n`.

B3. **Z[φ] multi-scale coarse-graining.**  
Object/map:  
`c_φ(Φ)(x,t) = Σ_k a_k A_{ell_k}^{(n(k))} J_{n(k)} T_HD^(n(k)) Φ_k(t)`,  
with `ell_k = ell_0 φ^{-k}` and exact `Z[φ]` weights `a_k`.  
Bridges: P7’s level-dependent sup constants to a uniform physical field.  
Route: adapt G5 shell summation to derivative-weighted hydrodynamic kernels.  
First step: prove  
`||curl A_{ell_k} J_k||_∞ <= C ell_k^{-1} ||J_k||_∞`  
and choose weights so `Σ_k k^{r-1} φ^{-k(s-1)} < ∞`.

B4. **Discrete vorticity dictionary.**  
Object/operator: `Ω_n = curl_n u_n`, with `curl_n: U_n -> Vort_n` as a discrete exterior/Hodge operator.  
Bridges: spectral/rank control to actual vorticity control.  
Route: new derivation plus classical discrete Hodge estimates.  
First step: state finite-level Bernstein estimate  
`||Ω_n Φ||_∞ <= C_v Λ_H4^{1/2} ||Φ||_spectral`,  
then prove stability under `T_HD^(n)` and `c_φ`.

B5. **Time-uniform cascade norm bound.**  
Object/lemma: coercive physical-subspace theorem: if `L_n|Y_n >= 0`, then `sup_t ||Φ_n(t)||_{Y_n} <= ||Φ_n(0)||_{Y_n}`.  
Bridges: finite-time spectral bounds to all-time vorticity bound.  
Route: P4 plus new positivity/coercivity on the hydrodynamic subspace.  
First step: identify `Y_n = P_Leray T_HD W_int` and prove invariance plus `L_n|Y_n >= 0`.

B6. **S3-to-R3 PDE bridge.**  
Object/map: stereographic/localization operator from P7’s compact `S^3` setting to physical `R^3` velocity fields.  
Bridges: P7’s geometry to Clay-style `R^3` NS.  
Route: classical PDE/local chart analysis.  
First step: prove a chart estimate  
`||ω_R||_∞ <= C_chart (||ω_S3||_∞ + ||u_S3||_∞)`  
with correct treatment of pressure and viscosity.

B7. **BKM wrapper.**  
Object/proposition: for classical `u`, `sup_t ||ω(t)||_∞ <= M` implies `∫_0^T ||ω||_∞ dt < ∞`, hence continuation.  
Bridges: vorticity bound to global smoothness.  
Route: classical BKM/Kato/Ladyzhenskaya/Lions/Constantin-Foias.  
First step: state local well-posedness for `u_0 ∈ H^s`, `s > 5/2`, then invoke BKM continuation.

**SECTION C. Reversals Or Corrections To Prior Rounds**

- At [ns-pi-hyd-wo-task.md](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/docs/codex-derive/ns-pi-hyd-wo-task.md:25>) replace “F4 (foundations.tex): cascade closure operator F has bounded discrete spectrum on H_4 substrate (600-cell)” with “NS spectral package: P2/Paper XXII give the 600-cell graph-Laplacian spectrum; P4 gives finite-level bounded self-adjoint closure generators; Foundations F4 supplies the closure-depth count, not the H4 spectrum.”
- At [ns-formal.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/millennium-ns-formal/ns-formal.tex:416>) replace “cascade F is a conserved quantity under its own dynamics” with “on the physical/coercive subspace required by `Π_hyd`, P4 energy dissipation plus `L_n|Y_n >= 0` gives the needed time-uniform cascade norm bound.”
- At [cascade-hydrodynamic-projection.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-hydrodynamic-projection/cascade-hydrodynamic-projection.tex:633>) replace the unconditional norm-dissipation identity with the qualified statement: “under `L_n >= 0` on the relevant invariant subspace, `d_t 1/2||Φ_n||^2 = -<Φ_n,L_nΦ_n> <= 0`; unconditionally P4 gives `d_t F_n(Φ_n) = -||L_nΦ_n||^2 <= 0`.”

**SECTION D. Alternative Routes**

Route Q, preferred: spectral package + Z[φ] shell summation + derivative-weighted `Π_hyd`. This directly targets the requested `F4 + c_φ -> L∞ vorticity -> BKM` path.

Route K: pentagonal holonomy. Use `insight.md`’s `Z[φ]^×` cocycle to make transport/curl cancellation canonical. Strong for B2/B4, but it is repo-new and should not be the primary BKM path.

Route P: classical Sobolev route. Strengthen P7’s `L^2_t H^1_x` convergence hypothesis to uniform `H^s`, `s > 5/2`, then use Sobolev embedding for vorticity. Cleaner PDE-wise, but the cascade still must prove the high-Sobolev uniform bound.

**SECTION E. Attribution Audit**

Do not cite P7 as proving uniform `L∞` vorticity; it currently gives finite-level projection and weak-limit machinery. Do not cite Foundations F4 for the H4 spectrum; cite P2/Paper XXII. Use G5/Z[φ] truncation only after adding derivative weights. Use BKM only after the classical solution and continuation hypotheses are stated.

**SECTION F. Top 3 Next Builds**

1. In [ns-formal.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/millennium-ns-formal/ns-formal.tex:347>), replace the current vorticity theorem proof with a named `Π_hyd-Z[φ] Integration Lemma` whose hypotheses are B1-B5 and whose conclusion is `sup_t ||ω||∞ <= M`.

2. In [cascade-hydrodynamic-projection.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/cascade-hydrodynamic-projection/cascade-hydrodynamic-projection.tex:911>), add the derivative-weighted kernel estimates needed for `curl Π_hyd`, separate from the existing `L2` defect estimates.

3. Near [ns-formal.tex](</mnt/c/Users/nexus/OneDrive/Documents/My Projects/vfd-crystalisation-paper/papers/millennium-ns-formal/ns-formal.tex:191>), replace the simple ball-average coarse graining with the explicit multi-scale `Z[φ]` shell coarse-graining `c_φ`, citing G5 and stating the summability condition that makes the vorticity series uniformly finite.
