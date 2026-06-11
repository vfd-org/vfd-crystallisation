Publication ready: no.

**1. Claim Audit**
- Lemma `\mathcal O_K=\Ophi` (lines 271-285): established.
- Lemma `\disc(K)=5` (lines 287-297): established.
- Lemma “`\Ophi` is a PID” (lines 299-329): established.
- Lemma “torsion-free finitely generated `\Ophi`-modules are free” (lines 331-346): established.

- Theorem C2 (lines 563-600): not established as stated.
  The proof’s load-bearing step is lines 624-635: it treats `\HH_{\rm int}\cong\R^4` as “a free `\Ophi`-module of `\Ophi`-rank 2”. As written that is false or at least wholly unproved. `\R^4` is not a finitely generated `\Ophi`-module, so the bound `\rk_\Ophi \pi_{\rm int}^{\rm amb}(M_{\rm amb})\le 2` does not follow. Without that bound, the rank count collapses.
  Hidden assumptions are also doing most of the work: admissibility already fixes an `\Ophi`-module structure, a `\sigma`-twisted internal action, a fixed 4D internal target, and `\pi_{\rm phys}^{\rm amb}|_{M_{\rm amb}}=0` (lines 436-487). So even if repaired, C2 is only a theorem about this tightly engineered class of ambients, not “from F1 alone”.

- Proposition `\ref{prop:reduction}` (lines 770-814): acceptable only as a proof outline, not as a closed result.
  The case split is fine under the extra hypothesis (R1), but the parenthetical at lines 774-775, “so `\rk_\Z M_{\rm amb}=4` and no translation-trivial excess is present”, is false: rank 12 does not imply the absence of translation-trivial directions. The proof also mis-cites C2 at line 820.

- Theorem C1 (lines 856-871): the narrow algebraic conclusion `M\cong \Ophi^2` is established, but the advertised claim is overstated.
  From admissibility alone, `M` is already a finitely generated torsion-free `\Ophi`-module (lines 441-453, 874-875). Theorem C1 therefore does not materially use `\Hmin`; it repackages what admissibility already assumes. Calling this “phason complement uniqueness” is too strong: what is shown is only the `\Ophi`-module isomorphism type.

- Theorem C3 (lines 934-949): not established.
  Line 952, “(a): Immediate from Theorem C1”, is wrong. C1 gives an `\Ophi`-module structure and an isomorphism type; it does not show that `\Ophi` is the coefficient ring in any maximal/minimal/unique sense. Part (a) is exactly where `\Hmin` should be used, but no precise definition of “the coefficient ring” is given, and no proof is supplied.

**2. Internal Consistency**
- Lines 757-764 are internally contradictory. The text says C2 rules out all candidate rings of `\Z`-rank `\ge 3`, then immediately says a residual `\rk_\Z R=4` case remains. `4\ge 3`.
- Line 820 cites Theorem C2(ii) for `N=12`. C2(ii) is the `N>12` case and does not support the statement being used there.
- Lines 774-775 assert “no translation-trivial excess is present” in a rank-12 ambient. That does not follow from anything proved.
- Lines 909-926 are mathematically incoherent. `M\cong \Ophi^2` in this paper and `M\cong \Ophi^4` in the old notes do not describe “the same underlying algebraic object up to relabeling”. Those are different `\Ophi`-module ranks and different `\Z`-ranks.
- C1 proves `\Ophi`-torsion-freeness in lines 887-903 after already taking `M` to be torsion-free over `\Ophi` via admissibility in lines 874-875. The paper is not keeping straight what is assumed and what is proved.

**3. External Consistency**
- F1 attribution (lines 76-80, 112-118, 177-182, 242-245): not locally verifiable as cited.
  The cited file `papers/cascade-correspondence-foundations/foundations.tex` exists, but I could not locate a section “F1” or an axiom statement matching this citation contract in that file. The local source audit therefore fails on its own terms.

- Downstream use in `papers/paper-xxxiv/paper-xxxiv.tex`: citation contract not met.
  At lines 118-127, paper-xxxiv says “C2 and C3 are theorems” and “C1 is a theorem modulo a minimality principle”. That is incompatible with this manuscript, where C3 is not proved and C1/C3 are both conditional on `\Hmin`.
  At lines 107 and 127, paper-xxxiv still uses `\Zphi^4` for the phason complement, which is incompatible with this manuscript’s fixed rank convention.
  At lines 270-280, paper-xxxiv’s bibliography still points to the old markdown sources `cascade-12d-closure.md` and `cascade-phase-b-c1-c2-c3.md`, not this TeX preprint. So downstream attribution is not merely sloppy; it is pointed at different documents with different claims.

**4. Tightness**
- Lines 41-49: “we prove the three closure theorems” is too strong.
  Edit: “We prove C2 for admissible ambients; C1 and C3 remain conditional on `\Hmin`, with C3 requiring a precise coefficient-ring formulation.”

- Lines 57-63 and 124-131: “termination at rank 12” is too strong for the actual theorem.
  Edit: “For admissible ambients in the sense of Definition `\ref{def:admissible}`, no rank beyond 12 contributes new internal-image content.”

- Lines 923-926: “same underlying algebraic object up to relabeling” is indefensible.
  Edit: “The old `\Ophi^4` notation uses a different rank convention and is not interchangeable with the present `\Ophi^2` statement.”

**5. Surface Issues**
- No unresolved `\ref` labels showed up in a static check.
- The substantive surface failures are citation/notation failures, not typos:
  line 820 is a wrong internal citation;
  the F1 local citation is not verifiable;
  the `\Ophi^2`/`\Ophi^4` convention split is not cosmetic and cannot be waved away as notation.

**6. Top Three Fixes**
1. Repair C2 or downgrade it.
   The false/unproved step is lines 624-635. Either prove that `\pi_{\rm int}^{\rm amb}(M_{\rm amb})` lands in a finite-rank `\Ophi`-lattice such as a copy of `K^2`/the classical internal lattice, or stop claiming unconditional termination. As written, the flagship theorem fails.

2. Rewrite C3 around a precise definition of “coefficient ring”.
   Lines 737-750 and 934-960 need a real notion: minimal ring of definition, maximal scalar ring, endomorphism ring, or chosen base ring. Then prove part (a) from `\Hmin`. The current proof is a non sequitur.

3. Fix the downstream contract with paper-xxxiv.
   The present manuscript says `M\cong \Ophi^2` under a fixed `\Z`-rank convention; paper-xxxiv still uses `\Zphi^4` and treats C2/C3 as theorem-level inputs. That must be reconciled before publication, not deferred to a future paper.

Verdict: not publication-ready. The unconditional theorem C2 is not currently proved, C3 is not currently proved, and the downstream alpha-paper is citing an incompatible version of the result.
