# WO-VFD-H4-E8-TRACE-FORM-003 — H4→E8 Trace-Form Completion (report)

**Status:** run; **the open technical bridge is RESOLVED at its core, exactly:
the Q(√5) trace form fixes the naive ±½ failure (derived, not tuned), and the
5×24-cell partition of the 600-cell is verified.** Modules: `golden_field.py`,
`run_h4_e8_trace_form.py` (exact `Fraction` arithmetic). **No proof of RH/physics;
no claim E8 is the universe; these are KNOWN results verified exactly, not VFD
discoveries.**

## 1. Summary
The prior WO left one genuinely open thread: the naive `x→(x,σx)` H4→E8 map gave
norm² = 2 but inner products with **±½ ∉ E8**. This WO resolves it with exact
golden-field arithmetic:
1. **Trace form fixes integrality (derived).** With `B(x,y) = Tr_{K/Q}(c·⟨x,y⟩)`,
   `c = 1 + 1/√5` (Tr c = 2), the 120 600-cell vertices get **norm² = 2** and
   **inner products `{−2,−1,0,1}` — all integers in {−2..2}** (0 non-integer).
   `c` is **forced** by (norm 2 ⟹ Tr c = 2) + (integrality), **not tuned**.
2. **Controls confirm the mechanism.** Naive `c=1` reproduces the **±½ failure**;
   `c=φ` (Tr=1) gives norm 1, not 2. So the fix is the *form*, not a fudge.
3. **5×24-cell partition verified exactly.** The 600-cell's 120 vertices split
   into **5 disjoint 24-cells** (Frame₀ = the 24 φ-free vertices; its 5 cosets
   under an order-5 element), each a genuine 24-cell — the classical **compound
   of five 24-cells** (cosets of 2T in 2I).
4. **Honest scope on full E8.** The 120 unit icosians under `B` give **120**
   norm-2 E8-compatible roots (a half-shell). The exact **240-root** E8 needs the
   *second* icosian shell (icosians of squared-length φ, `p+q=1`) — **not** the
   φ-scaled copy (that has B-norm 4). That is a short-vector enumeration of the
   icosian ring, deferred to the follow-on.

**Both verified facts are KNOWN mathematics** (Wilson's icosian/Q(√5) E8
construction; the compound of five 24-cells) — **verified exactly here, not
discovered.**

## 2. Why this followed
LOCAL-LINK-002 confirmed H3 ⊂ H4 and flagged the H4→E8 integrality gap as the one
open technical thread. This WO closes the *integrality* half exactly and verifies
the 5×24 frame structure the programme's "5×24-cell" notes pointed to.

## 3. Golden-field arithmetic (Phase 1)
`golden_field.G` = `a + b√5` with `Fraction` coefficients; exact `+,−,×`,
conjugation σ (`√5→−√5`), trace `Tr = 2a`, norm `a²−5b²`, and quaternion product.
Verified: `φ² = φ+1`, `σ(φ) = −1/φ`, `Tr(φ)=1`, `Norm(φ)=−1` (all exact).

## 4. H4 over Q(√5) (Phase 2)
120 600-cell vertices built with exact coordinates: `(±1,0,0,0)` [8],
`(±½)⁴` [16], even signed permutations of `(φ/2, ½, 1/(2φ), 0)` [96] — with
`φ/2 = (¼,¼)`, `1/(2φ) = (−¼,¼)` in `(a,b√5)` form. Count = 120 ✓.

## 5. Trace-form derivation and test (Phase 3) — the core result
`B(x,y) = Tr(c·⟨x,y⟩)`. For unit vertices `⟨x,x⟩=1`, so `B(x,x)=Tr(c)`; **norm² = 2
⟹ Tr(c) = 2**. Writing `⟨x,y⟩ = p+q√5`, `c = 1 + t√5` gives `B = 2p + 10tq`.
Requiring the 600-cell inner products (`p+q√5 ∈ {1, φ/2, ½, 1/(2φ), 0}`) to be
**integers** forces `t = 1/5`, i.e. **`c = 1 + 1/√5`**, giving `B = 2(p+q)`:

| ⟨x,y⟩ | (p,q) | naive `2p` | **`B=2(p+q)`** |
|---|---|---|---|
| 1 | (1,0) | 2 | 2 |
| φ/2 | (¼,¼) | **½** ✗ | **1** ✓ |
| ½ | (½,0) | 1 | 1 |
| 1/(2φ) | (−¼,¼) | **−½** ✗ | **0** ✓ |
| 0 | (0,0) | 0 | 0 |

**Measured over all 120 vertices:** norms `{2}`; inner-product set `{−2,−1,0,1}`;
**0 non-integer**; **E8-compatible = True**. The fix is exact and derived.

## 6. Controls (Phase 8)
- **Naive `c=1`:** inner products `{−2,−1,−½,0,½,1}` — **reproduces the ±½
  failure** (matches the prior WO). ✓
- **Wrong `c=φ` (Tr=1):** `B(x,x) = {1}` — norm 1, not 2. ✗ as expected.
So the integrality is carried by the *specific* trace factor, not by tuning.

## 7. E8 completion (Phases 4, 6) — honest scope
The 120 unit icosians under `B` are **120 norm-2, E8-compatible roots** — a
half-shell. Full **E8 has 240** roots. Under `B`, a vector has norm 2 iff its
squared-length `|x|² = p+q√5` satisfies `p+q = 1`: units give `(1,0)`; the other
solution is `|x|² = φ = (½,½)` — a **second shell** of non-unit icosians. The
φ-*scaled* copy `φ·(units)` has `|x|²=φ²`, `p+q=2`, **B-norm 4** — so it is **not**
the second shell. Recovering the exact 240 = enumerating icosian-ring vectors of
squared-length φ (a short-vector search). **Deferred** — not faked.

## 8. 5×24-cell decomposition (Phase 5) — verified exactly
- **Frame₀** = the 24 φ-free vertices (`(±1,0,0,0)` + `(±½)⁴`) — a 24-cell (= the
  unit quaternions of the binary tetrahedral group 2T).
- Its **5 left cosets** under an order-5 element `g ∈ 2I` (a φ-type vertex):
  sizes `[24,24,24,24,24]`, **pairwise disjoint**, **cover all 120**, and **every
  frame is a 24-cell** (24 verts, unit norm, inner products `{0,±½,±1}`).

This is the classical **compound of five 24-cells** (cosets of 2T in 2I, index 5),
verified by exact quaternion arithmetic. So the 600-cell **does** admit a clean
`5 × 24` partition.

## 9. Ten-24 / E8 (Phase 6) — conditional
If/when the second icosian shell is enumerated (Phase 7 follow-on), the natural
expectation is that E8's 240 roots organise as **two golden-conjugate copies of
the 5×24 frame system (10 × 24)**. This is **not** verified here (depends on the
deferred 240-root construction) and is flagged as conditional, not claimed.

## 10. Local-link ladder integration (Phase 7)
Verified rungs: **H3 icosahedron** (600-cell vertex figure, LOCAL-LINK-002) →
**24-cell/D4 frame** (Frame₀, here) → **5×24 = H4/600-cell** (here) →
**trace-form integrality to E8** (here, half-shell). The only unverified rung is
the **full 240-root E8** (second shell). The ladder is *real* up to that point.

## 11. Obstructions & limits
- Full 240-root E8 needs the second icosian shell (short-vector enumeration);
  the φ-scaled copy is the wrong (norm-4) set.
- Everything verified is **known** (Wilson icosian E8; compound of five 24-cells);
  this WO **verifies exactly**, it does not discover.
- No VFD-specific law beyond the recovered classical structure.

## 12. What this does and does NOT claim
- **Does:** resolve the open integrality gap exactly (`c=1+1/√5` trace form,
  derived, fixes ±½ → integers); verify the 5×24-cell partition exactly; confirm
  controls; give the exact half-shell E8-compatible 120.
- **Does NOT:** produce the full 240-root E8 (deferred to short-vector
  enumeration); claim a new VFD law; claim E8 is the universe; claim discovery of
  known icosian/24-cell results.

## 13. Recommended next WO
The honest, genuinely-open next step is **WO-VFD-H4-E8-SECOND-SHELL-004**: enumerate
the icosian-ring vectors of squared-length φ (`p+q=1`) — reusing the route_b
short-vector enumerator — to complete the exact **240-root E8** and test the
**10×24** frame organisation. Alternatively **WO-VFD-H4-E8-FORMAL-PAPER-004** to
write up the verified bridge (trace form + 5×24) with exact arithmetic, *citing*
Wilson/Moody–Patera and the compound of five 24-cells as the classical sources.
