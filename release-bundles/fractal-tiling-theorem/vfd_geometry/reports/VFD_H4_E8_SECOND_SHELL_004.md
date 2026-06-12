# WO-VFD-H4-E8-SECOND-SHELL-004 — Second Icosian Shell / E8 Completion (report)

**Status:** run; **the H4→E8 trace-form bridge is COMPLETED EXACTLY — the full
240-root E8 is recovered and matches the canonical root system.** Modules:
`golden_field.py`, `e8_second_shell.py`, `run_h4_e8_second_shell.py` (exact
`Fraction` arithmetic). **No proof of RH/physics; no claim E8 is the universe;
this is the KNOWN Wilson icosian E8 construction VERIFIED exactly, not discovered.**

## 1. Summary
TRACE-FORM-003 turned one H4/600-cell shell (120) into E8-compatible roots under
`B(x,y)=Tr_{K/Q}(c⟨x,y⟩)`, `c=1+1/√5`, and verified the 5×24-cell partition, but
left the full 240 open. This WO closes it:
- **Second shell determined (not guessed):** `B = 2(p+q)` for `⟨x,x⟩=p+q√5`, so
  B-norm 2 ⟺ `p+q=1`. Units give `(1,0)`; **`(1/φ)·units` give `1/φ²=(3/2,−1/2)`,
  `p+q=1` → norm 2** (whereas `φ·units` give `φ²`, `p+q=2` → norm 4, the prior
  failure). Since `1/φ = φ−1 ∈ Z[φ]`, `x/φ` stays an icosian.
- **shell₂ = (1/φ)·shell₁:** 120 vectors, all B-norm² = 2, **disjoint** from shell₁.
- **Full 240 = shell₁ ∪ shell₂ = canonical E8:** all norm² = 2; inner products
  `{−2,−1,0,1}` (all integral); **E8 root-graph degree distribution exactly
  `(+1,−1,0,+2,−2) = (56,56,126,1,1)`**; rank 8; even integral. **Matches E8.**
- **10×24 organisation:** shell₂ is the exact golden-similarity image of shell₁'s
  five 24-cells → five more 24-cells; the ten partition the 240 (golden-similar
  pairs). *(By the similarity argument — see §7 caveat.)*

**This exactly reproduces the classical Wilson/Moody–Patera icosian construction
of E8. It is verified, not discovered.**

## 2. Why this followed
TRACE-FORM-003 explicitly scoped the 240 to "the second icosian shell"; this WO
supplies it with exact arithmetic and validates against canonical E8.

## 3. Exact trace form (recap)
`B(x,y) = Tr_{K/Q}(c·⟨x,y⟩)`, `c = 1 + 1/√5` (Tr c = 2). On `⟨x,y⟩ = p+q√5`,
`B = 2(p+q)`. Reproduced shell₁ (120 verts, norms `{2}`) before extending.

## 4. Reproduction of shell₁ + 5×24 (Phase 1)
shell₁ = 120 exact-coordinate 600-cell vertices, all B-norm² = 2 (reproduced from
TRACE-FORM-003), partitioned into five disjoint 24-cells.

## 5. Second-shell construction (Phases 2–5)
**Constructive** (not diagnostic): `shell₂ = (1/φ)·shell₁ = (φ−1)·shell₁`.
- 120 vectors; all **B-norm² = 2** (exact); `shell₁ ∩ shell₂ = ∅`.
- Derivation: B-norm 2 ⟺ Euclidean `⟨x,x⟩` has `p+q=1`; units (`p+q=1`) and the
  `1/φ`-scaled copy (`1/φ²=(3/2,−1/2)`, `p+q=1`) both satisfy it; the `φ`-scaled
  copy (`p+q=2`) does not. So shell₂ is the **1/φ shell**, not the φ shell.

## 6. Full 240-root E8 test (Phase 6) — PASSES

| test | result | E8 expected |
|---|---|---|
| root count | **240** (240 distinct) | 240 |
| all norm² | **{2}** | 2 |
| inner products (off-diag) | **{−2,−1,0,1}** | ⊆ {−2..2} |
| non-integer entries | **0** | 0 |
| per-root (+1,−1,0,+2,−2) | **(56, 56, 126, 1, 1)** | (56,56,126,1,1) |
| embedding rank | **8** | 8 |
| even integral | **yes** | yes |
| **matches canonical E8** | **YES** | — |

The `(56,56,126,1,1)` degree distribution is the decisive test: a 240-vector,
norm-2, rank-8 set with exactly this inner-product profile **is** the E8 root
system. (Embedding: `x ↦ (√c·x, √σc·σx)` realises `B` as the Euclidean dot in 8D.)

## 7. 10×24 frame organisation (Phase 7)
shell₂ = `(1/φ)·shell₁` is an exact **similarity** image of shell₁, which
partitions into five 24-cells (TRACE-FORM-003). Similarity preserves the 24-cell
combinatorics and the partition, and `shell₁ ∩ shell₂ = ∅`, so the **ten** 24-cell
frames partition the 240 — five golden-similar pairs.
**Honest caveat:** this is established by the *similarity argument*, not by
independently re-extracting shell₂'s frames under `B` (the `B`-restricted Gram on
shell₂ differs by the golden twist `1/φ²`, though it remains a 24-cell-isometric
set). The 240-root E8 result (§6) is fully independent and rigorous; the precise
"10 clean 24-cell frames under `B`" is asserted by similarity and flagged as such.

## 8. Relation to the 5×24-cell notes (Phase 8)
The programme's "5×24" picture is **confirmed and completed**: the 600-cell's five
24-cells (shell₁) are exactly **half** of a 10×24 system; the golden-conjugate /
`1/φ` second five complete it to E8. Recommended framing for any 5×24 write-up:
state it as the **shell₁ half** of the classical E8 = 10·D4 decomposition, citing
Wilson/Moody–Patera; do not present the 5×24 alone as the whole story.

## 9. Controls (Phase 9)
- **φ-scaled shell** `φ·x`: B-norm² = **{4}** — confirms it is **not** the second
  shell (the prior WO's dead end), and that `1/φ` (not `φ`) is correct.
- **Naive `c=1`:** inner products include **±½** — reproduces the original failure.
Both controls behave exactly as required; the completion is not tuning.

## 10. VFD interpretation (disciplined)
The H4→E8 bridge is **not** a naive Euclidean embedding; it is a **trace-form
completion over Q(√5)**: `E8 = shell₁ ⊕ (1/φ)·shell₁` under `B = Tr(c⟨·,·⟩)`,
`c = 1+1/√5`. The "self-adjoint/integral folding" reading is: the correct
invariant bilinear form (the golden trace form) is exactly what makes the H4-to-E8
fold land on an even integral lattice. Stated as a *verified exact bridge*, not a
new law.

## 11. Obstructions & honesty
- This is the **known** icosian E8 construction (Wilson 2009; Moody–Patera;
  Conway–Sloane) — **verified exactly here, not discovered.** No VFD-specific new
  mathematics.
- The 10×24 partition is asserted by the similarity argument (§7), not
  independently re-extracted under `B`.
- No physics/RH consequence is claimed.

## 12. What this does and does NOT claim
- **Does:** complete the exact 240-root E8 from H4 via the golden trace form
  (shell₂ = 1/φ·shell₁, derived); pass every canonical-E8 test (count, norm, ips,
  56/56/126/1/1, rank 8, even integral); confirm controls; confirm the 5×24→10×24
  ladder (with the §7 caveat).
- **Does NOT:** claim discovery (this is Wilson's construction); claim a new VFD
  law; claim E8 = universe; claim physics/RH; independently re-extract the 10
  frames under `B`.

## 13. Recommended next WO
The bridge is complete. The honest next step is **WO-VFD-H4-E8-FORMAL-PAPER-004**:
write up the verified bridge — golden trace form `c=1+1/√5`, `E8 = shell₁ ⊕
(1/φ)shell₁`, the 5×24→10×24 ladder, `H3 ⊂ 24-cell ⊂ H4 ⊂ E8` — with exact
arithmetic and **explicit citation** of Wilson/Moody–Patera (classical source).
Optionally **WO-VFD-E8-24CELL-FRAME-ATLAS-005** to independently re-extract and
catalogue the ten 24-cell frames under `B` (closing the §7 caveat).
