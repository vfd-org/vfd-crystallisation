**1. Claim audit**

- “`νF is the formal cogito ... F-irreducible sub-coalgebras correspond to the prime ideals ... its σ-fixed sub-coalgebra projects to the critical line`” (`papers/cascade-derivation/cascade-observer-zeta.md:24`): not established. This bundles three open steps: undefined `F-Irr` (O1), undefined `ζ_F` (O2), and an unbuilt Lawvere lift (O3). The capstone only gives a conditional final coalgebra and in fact identifies it with the terminal object `1_C` (`papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1251`), which makes the arithmetic jump worse, not better.

- “`The right cascade-native zeta is Dedekind ζ_K`” (`...observer-zeta.md:44`): over-claim. Experiment C verifies a classical ideal-counting identity for `O_K`; it does not derive any cascade-native zeta from `F`-iteration. The note itself concedes “`ζ_F is not defined`” (`...observer-zeta.md:318`, `475`).

- “`If the Lawvere-diagonal step closes categorically, RH follows`” (`...observer-zeta.md:47`): over-claim. Even a successful P4 would still leave O1 and O2 unresolved. RH does not follow from O3 alone.

- “`Adámek's theorem gives a final coalgebra ... c: Ω̂→F(Ω̂) an isomorphism`” (`...observer-zeta.md:66`): established only conditionally, and the note omits the crucial degeneracy that the capstone proves `Ω̂ = 1_C` and `c = id` (`...capstone-coalgebra.tex:1251-1267`).

- “`Ω̂ is ... the universal object of self-observation`” (`...observer-zeta.md:69`): rhetorically stronger than the source. The source gives terminal/final universal property; it does not give any independent arithmetic or “self-observer” structure beyond that (`...capstone-coalgebra.tex:1301-1313,1681-1702`).

- “`Conjectured cascade Lawvere-lift ... final coalgebra inherits induced σ_Ω ... in the Cartesian-closed category of σ-equivariant F-coalgebras`” (`...observer-zeta.md:87`, `249`): not established, and not even well-posed from current artefacts. I found no local source proving `C` or the σ-equivariant coalgebra category is cartesian closed or has exponentials/diagonals. This is a deeper gap than “missing proof”.

- “`ζ_K = ζ·L(χ_5)`” (`...observer-zeta.md:106`): established classically; Experiment C correctly verifies the coefficient identity for `n≤100` (`papers/cascade-derivation/scripts/observer_zeta_dedekind.py:104-110,133-155`).

- “`Riemann ζ is the σ-fixed factor; L(s,χ_5) is the σ-anti-invariant factor`” (`...observer-zeta.md:109-111`): not established by any local σ-action on the analytic factors. The factorisation is classical; the “fixed/anti-invariant” interpretation is imported by slogan.

- “`Both factors satisfy GRH`” (`...observer-zeta.md:111`): false as stated. GRH is conjectural.

- Numerical baseline in §2.1 (`...observer-zeta.md:122-125`): established by the script output (`papers/cascade-derivation/scripts/observer_prime_inert_split.py:73-109`).

- Negative claims in §2.2 and §2.3 (`...observer-zeta.md:129-144`): established for the toy models actually implemented in `observer_zeta_candidate.py` (`...scripts/observer_zeta_candidate.py:81-130,137-188`). They do not say anything direct about the full capstone functor with closure data.

- “`Positive result: ζ_K = ζ·L(χ_5) ... This empirically grounds ... the cascade's natural zeta is Dedekind ζ_K`” (`...observer-zeta.md:154-156`): first sentence yes, second no. The script checks classical arithmetic, not a cascade construction.

- Prime Detector claim (`...observer-zeta.md:158-170`): not locally verifiable. `vfd_prime_detector.js` is not in this repo.

- aria-chess claim (`...observer-zeta.md:172-183`): not locally verifiable. The cited `aria-chess` document is external to this repo.

- Definition of `F-irreducible` (`...observer-zeta.md:191-195`): defective. In a category whose morphisms are inclusions (`...capstone-coalgebra.tex:416-430`), “`factors uniquely through S itself`” is close to vacuous, and the coproduct formulation is unsupported because no coproduct theory for `F`-coalgebras is developed. This definition does not currently pick out a meaningful arithmetic atom.

- P1 (`...observer-zeta.md:202-207`): unsupported. No canonical map from sub-coalgebras of `Ω̂=1_C` to `Spec(O_K)` is given.

- P2 (`...observer-zeta.md:218-221`): unsupported/vacuous. `ζ_F` is not constructed.

- P3 (`...observer-zeta.md:232-241`): unsupported, and one substantive part is wrong. The classical inert/split classification is fine, but “`inert + ramified contribute exactly the ζ(s) factor; σ-orbit-2 contribute the L-factor`” is false. Euler factors do not split that way: inert primes contribute local factor `(1-p^{-2s})^{-1}`, not the `ζ` local factor. The script repeats this bad interpretation (`...scripts/observer_zeta_dedekind.py:199-204`).

- P4 (`...observer-zeta.md:249-253`): unsupported. No diagonal, no terminal σ-equivariant coalgebra, no dynamical zeta, no zero-projection map.

- P5 (`...observer-zeta.md:269-279`): unsupported. Canonicality of `L` is not shown, and the cited icosian bridge is itself inconsistent upstream.

- P5-apex (`...observer-zeta.md:284-292`): only the mod-5 sanity check is supported. `2^{136279840}+1 ≡ 2 mod 5` is true, hence inert. The Fano-triad map is wholly blocked by open H-grad-1 (`papers/cascade-derivation/WO-H-GRAD-1.md:1-21`).

- Closed-claims table §4.1 has defects. C5 is overstated because the cited bridge is only “working note, lemma-grade” and leaves sub-gap G6.4-a open (`papers/cascade-derivation/cascade-q-o-measurement-bridge.md:3,193-196`). C6 is wrong: the cited Access Principle is explicitly conditional on `H-grad, H-meas` (`papers/cascade-derivation/cascade-access-principle-theorem.md:3,21,29-33,188`). C7 is not backed by a closed source: `cascade-12d-closure.md` is architectural/conjectural (`papers/cascade-derivation/cascade-12d-closure.md:3,142-170`) and `dual_600cell_factor2.py` says its E8 decomposition is “simplified” (`papers/cascade-derivation/scripts/dual_600cell_factor2.py:142-145`).

- “`The third (Lawvere-σ lift for P4) is ... categorically well-posed`” (`...observer-zeta.md:443-445`): not true. The cartesian-closed/equivariant setup is missing.

**2. WO acceptance audit**

- Acceptance criteria: none are stated in this WO. That is a bookkeeping defect. This file has open items and self-critique, but no numbered acceptance criteria to audit.

- O1 (`...observer-zeta.md:313-316`): not resolved. Still the central failure.

- O2 (`...observer-zeta.md:318-321`): not resolved. `ζ_F` remains undefined.

- O3 (`...observer-zeta.md:323-327`): not resolved. No diagonal mechanism is exhibited.

- O4 (`...observer-zeta.md:329-330`): not resolved. Only the trivial inertness sanity check is touched.

- O5 (`...observer-zeta.md:332-335`): not resolved.

- O6 (`...observer-zeta.md:337-340`): not resolved. The inconsistency is correctly flagged, not fixed.

- O7 (`...observer-zeta.md:342-347`): partially sharpened by §4.3, but not resolved. This is the real central issue.

- Self-critique §8 (`...observer-zeta.md:471-490`): accurate. All five weaknesses remain weaknesses.

**3. Catalogue audit**

- No math-catalogue is supplied for this strand. That is itself a defect.

- Therefore every object introduced here is uncatalogued: the working Definition of `F-irreducible` (`...observer-zeta.md:191`), Conjectures P1-P5 and P5-apex (`202, 218, 232, 249, 269, 284`), and the numerical results in §§2.1-2.4 (`122, 129, 138, 148`).

- The status table C1-C8 is not a substitute for a catalogue. It also contains wrong statuses (C5, C6, C7).

**4. Attribution / external consistency**

- `cascade-capstone-coalgebra.tex` does support conditional Adámek/Lambek existence (`...capstone-coalgebra.tex:1251-1267,1697-1702`). It also states the final coalgebra is the terminal rung-structure, which the note underuses.

- `cascade-access-principle-theorem.md` does not support “unconditional” C6. It supports only a conditional theorem and explicitly says full `Ẑ[φ]^6`-level P-A still awaits H-grad-1 (`...access-principle-theorem.md:29-33,232-233,301,315-319`).

- `cascade-q-o-measurement-bridge.md` does state `Q_O ≅ Meas(S^7,σ)` (`...q-o-measurement-bridge.md:19-27,112-138`), but the same file labels itself lemma-grade and leaves a technical verification gap open (`...:3,193-196`).

- `cascade-fano-grading-lift.md` explicitly says only `P-A-Fano` is unconditional; full P-A remains conditional on H-grad-1 (`...cascade-fano-grading-lift.md:209-215,231-239`). The note’s C6 ignores that.

- `WO-H-GRAD-1.md` is still open (`...WO-H-GRAD-1.md:1-21`), so P5-apex is correctly blocked.

- O6 is a real inconsistency: `cascade-12d-closure.md` uses the naive `Z[φ]`-with-quaternion-units description of the icosian ring (`...cascade-12d-closure.md:39`), while `cascade-algebraic-substrate.tex` explicitly says that naive form is wrong (`papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:506-513`).

- The note’s claim that `cascade-sigma-rationality.tex` shows the RH-note identification is “classical Mellin intertwining” is not locally verifiable from that file. `cascade-sigma-rationality.tex` is a narrow scalar-extension paper; it does not discuss Mellin transforms or `s↔1-s`.

- `cascade-rh-proof.md` does indeed identify cascade σ with the functional-equation reflection (`papers/cascade-derivation/cascade-rh-proof.md:115-121`). That part of the attribution is accurate.

- Prime Detector and aria-chess citations are not locally verifiable because the cited artefacts are not in this repo.

**5. Sim correctness**

- `observer_prime_inert_split.py` is fine for what it actually does: classify rational primes by splitting type in `Z[φ]`.

- `observer_zeta_candidate.py` honestly implements toy counterexamples. Its negative conclusions are limited to those toys; the derivation mostly respects that.

- `observer_zeta_dedekind.py` correctly computes the classical coefficient identity `a_n=(1*χ_5)(n)` for ideals of `O_K`. It does not implement any claim about `F`-iteration or a cascade zeta.

- The same script then over-interprets its own output. The block at `...observer_zeta_dedekind.py:199-204` asserts a false factor assignment (“sigma-fixed primes contribute to the zeta factor”). They do not.

- Minor but real bug: `...observer_zeta_dedekind.py:176` labels a truncated ratio as “`L(2, chi_5) exact`”. It is not exact.

**6. Tightness**

- `papers/cascade-derivation/cascade-observer-zeta.md:47`: replace “`If the Lawvere-diagonal step closes categorically, RH follows`” with “`Even with a Lawvere lift, RH would still require intrinsic constructions of F-irreducibles and ζ_F.`”

- `...observer-zeta.md:154-156`: replace “`This empirically grounds the reframe: the cascade's natural zeta is Dedekind ζ_K`” with “`This verifies the classical Dedekind factorisation and motivates ζ_K as a candidate target.`”

- `...observer-zeta.md:249-253`: replace “`is distinguished by universal property`” with “`would need to be characterised by a universal property, if an appropriate σ-equivariant CCC can be built.`”

- `...observer-zeta.md:442-445`: replace “`categorically well-posed`” with “`interesting but not yet categorically formulated in a usable way.`”

**7. Top three fixes**

1. Fix §3.1 before anything else. Give a non-circular definition of the atomic objects you want to count inside the actual capstone category, and explain how that survives the fact that `Ω̂ = 1_C` (`papers/cascade-derivation/cascade-observer-zeta.md:191-207`; `papers/cascade-capstone-coalgebra/cascade-capstone-coalgebra.tex:1251-1267`).

2. Remove or rewrite P2/P3 until `ζ_F` exists. Right now P2 is undefined and P3 contains a false Euler-factor interpretation (`papers/cascade-derivation/cascade-observer-zeta.md:218-245`; `papers/cascade-derivation/scripts/observer_zeta_dedekind.py:199-204`).

3. Stop treating P4 as the single remaining load-bearing step. Build the σ-equivariant categorical setting and the actual diagonal, or downgrade all RH-corollary language accordingly (`papers/cascade-derivation/cascade-observer-zeta.md:47-48, 249-265, 442-460`).

**8. Verdict**

Publication ready: no.
