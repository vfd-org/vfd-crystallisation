1. **Claim audit**
- `"None of those four steps is yet established"` and the surrounding Route (D) framing are honest; the note now states a research programme, not a theorem package. `cascade-observer-zeta.md:35`
- `"𝒞oalg(F) := category of pairs (Y,y) with y:Y→F(Y)"` is a standard imported definition and is used correctly. `cascade-observer-zeta.md:267`
- `"F-irreducible"` is explicitly marked as a candidate definition `"not proved well-posed"`; that is the right status. `cascade-observer-zeta.md:273`
- `P1` through `P5` and `P5-apex` are now stated as open questions or conditional targets, not as established results. No over-claim there. `cascade-observer-zeta.md:291`, `309`, `325`, `351`, `383`, `403`
- `"619 inert / 609 split / 1 ramified"` is established by the script output; the note’s summary is accurate. `cascade-observer-zeta.md:181`, script check: `observer_prime_inert_split.py`
- `"32 F-fixed rung-subsets"` and `"12 distinct dim values"` are established by the script output; the negative conclusion is warranted. `cascade-observer-zeta.md:188`
- `"ζ_{F1}(1) ≈ 3.3599"` and Fibonacci support are established by the script as a truncation/structural observation; the negative conclusion `"not Riemann zeta"` is warranted. `cascade-observer-zeta.md:197`
- `"100/100 coefficient matches"` and the `71/14/15` distribution are established by the script output; the positive conclusion is limited to coefficient-level verification for `n ≤ 100`, which is exactly what the script does. `cascade-observer-zeta.md:209`
- `C1` and `C1'` are supported by the capstone theorem exactly as stated: final coalgebra existence is conditional on `G-FIC-a`, `G-FIC-b`, `H-lift-fin`, and the carrier is `1_C`. `cascade-observer-zeta.md:421`, source: `cascade-capstone-coalgebra.tex:1251`
- `C2` is supported by the capstone corollary. `cascade-observer-zeta.md:423`, source: `cascade-capstone-coalgebra.tex:1697`
- `C3` and `C4` are classical and the local-factor reading is now correct; Round-4’s old prime-partition mistake is gone. `cascade-observer-zeta.md:424`
- `C5` is mostly honest now: the note does not silently inherit theorem-grade confidence, and it names the remaining sign-check hole. `cascade-observer-zeta.md:426`
- `C6a` is accurately stated as conditional on `H-grad + H-meas`. `cascade-observer-zeta.md:427`
- `C6b` is now correctly framed as a reviewer-side downgrade versus the cited source. That matches the cited source, which really does call P-A-Fano unconditional while still basing `μ` on a “most-natural candidate.” `cascade-observer-zeta.md:428`
- `C7` is the one claim still not cleanly sourced. The note now flags it as a downgrade, which is good, but the exact cited markdown source does not itself state `"σ swaps H₄ ⊕ H₄′ freely on nonzero 600-cell shells"` in that form. The script gives only a simplified version. `cascade-observer-zeta.md:429`
- `"O7 is currently open and is the programme's single most important next research step"` is a programme-priority judgement, not a theorem; acceptable as editorial framing. `cascade-observer-zeta.md:508`

2. **WO acceptance audit**
- There are no numbered acceptance criteria in the WO text. As a WO spec, that is still a defect: I can audit open items, but not declared acceptance criteria, because none are declared.
- Using the Round-5 residuals you gave as de facto acceptance targets:
- `(1) §2.5 and §2.6 merged into one external/unaudited block`: resolved. The banner is explicit and hard to misread. `cascade-observer-zeta.md:222`
- `(2) C6b and C7 framed as note-side downgrades vs cited source`: resolved. `cascade-observer-zeta.md:428`
- `(3) catalogue created covering D/P/N/O/E/review history`: partially resolved. The ledger exists and covers those families, but it still omits explicit `C1–C8` entries and loses the parent `O3` ID by splitting it into `O3-a/b/c`. `cascade-observer-zeta-catalogue.md:14`
- `O1`: partially resolved. Reframed onto `𝒞oalg(F)` with a candidate definition, but not closed. `cascade-observer-zeta.md:262`
- `O2`: partially resolved at most. The artefacts give negative toy evidence and a classical comparison target, but do not construct `ζ_F`. `cascade-observer-zeta.md:454`
- `O3`: partially resolved. It is decomposed honestly into framework substeps, but not closed. `cascade-observer-zeta.md:459`
- `O4`: not touched except status-reporting. `cascade-observer-zeta.md:468`
- `O5`: not resolved; only scoped. `cascade-observer-zeta.md:471`
- `O6`: not resolved; only flagged. `cascade-observer-zeta.md:476`
- `O7`: not resolved; sharpened and elevated correctly. `cascade-observer-zeta.md:483`

3. **Catalogue audit**
- Good: `D1–D4`, `P1–P5/P5-apex`, `N1–N6`, `E1–E2`, and review history are present and mostly faithful. `cascade-observer-zeta-catalogue.md:18`
- Defect: the derivation contains explicit `C1, C1', C2, ..., C8` ledger objects, but the catalogue does not list them; it only says “not duplicated here.” That fails the brief of a ledger. Derivation: `cascade-observer-zeta.md:421`. Catalogue omission: `cascade-observer-zeta-catalogue.md:63`
- Defect: the derivation’s open item is `O3`; the catalogue replaces it by `O3-a/b/c` without also preserving a parent `O3` row. That breaks ID consistency. Derivation: `cascade-observer-zeta.md:459`. Catalogue: `cascade-observer-zeta-catalogue.md:55`
- No obvious spurious catalogue entries beyond that.

4. **Attribution / external consistency**
- Capstone existence/degeneracy attribution is accurate. `cascade-capstone-coalgebra.tex:1251`
- Capstone fixed-point/Lambek follow-up attribution is accurate. `cascade-capstone-coalgebra.tex:1697`
- `Q_O ≅ Meas(S⁷,σ)` is accurately attributed as a theorem claim in a working note, and the observer-zeta note correctly keeps the remaining `G6.4-a` caveat visible. `cascade-q-o-measurement-bridge.md:19`, `193`
- Full `P-A` conditional status is accurately attributed. `cascade-access-principle-theorem.md:21`
- `P-A-Fano unconditional` is accurately reported as the source’s own claim, and the note’s downgrade is a fair reviewer judgement. `cascade-fano-grading-lift.md:209`
- `C7` is not cleanly attributable to `cascade-12d-closure.md:47`. That line says `E₈` decomposes into physical/phason icosian pieces under `σ`; it does not state the stronger shellwise free-swap claim. The simplified script comes closer, but only with an explicit caveat. `cascade-12d-closure.md:47`, `dual_600cell_factor2.py:138`
- The `icosian ring naive coordinatisation is wrong` attribution is accurate. `cascade-algebraic-substrate.tex:503`
- The statement that `cascade-rh-proof.md` identifies `σ` with `s↔1-s` is accurate. `cascade-rh-proof.md:115`
- The statement that `cascade-sigma-rationality.tex` is narrow and does not itself provide a non-classical geometric/dynamical lift is accurate. `cascade-sigma-rationality.tex:59`

5. **Sim correctness**
- A sim is supplied, in script form. The three scripts do what the note says they do.
- `observer_prime_inert_split.py` implements the mod-5 splitting law correctly and reproduces the stated counts.
- `observer_zeta_candidate.py` correctly implements the toy `F` enumeration and Fibonacci-series check. No statistical sleight of hand.
- `observer_zeta_dedekind.py` correctly compares direct ideal-counting against `(1*χ₅)(n)` and reproduces `100/100` matches for `n≤100`.
- No obvious bugs surfaced in the claimed outputs. The `s=2` ratio check is only a truncation sanity check, and the note does not overstate it.

6. **Tightness**
- `C1'` / `C2`: replace `"UNCONDITIONAL (given C1)"` with `"DERIVED once C1's hypotheses hold"`. `cascade-observer-zeta.md:422`
- Catalogue header: do not imply “ledger” completeness while omitting the `C`-series. Either add `C1–C8` rows or say explicitly that `C` claims are out of ledger scope. `cascade-observer-zeta-catalogue.md:4`
- `C7` source cell should stop pretending `cascade-12d-closure.md:47` is the exact source of the free-swap claim. `cascade-observer-zeta.md:429`

7. **Top three fixes**
1. Add explicit `C1–C8` rows to the catalogue and preserve a parent `O3` row. `cascade-observer-zeta-catalogue.md:63`
2. Tighten `C7` attribution: either cite only the simplified script caveat, or say no exact in-repo source for the stronger shellwise swap claim was found. `cascade-observer-zeta.md:429`
3. If this is truly a WO spec, add numbered acceptance criteria. Right now the document has goals and open items, but no auditable AC block. `cascade-observer-zeta.md:26`

8. **Verdict**
Publication ready: yes.

Reason: at problem-statement scope, the substantive math is now honestly scoped, the external anecdotal material is explicitly quarantined, the downgraded C6b/C7 framing is explicit, and the scripts support the numerical claims they are used for. The remaining defects are real, but they are catalogue/spec hygiene plus one still-loose attribution on `C7`, not a load-bearing mathematical over-claim.
