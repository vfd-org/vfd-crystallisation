# Trilogy Audit — What Survives the Geometry-First Honesty Bar

**Question.** Of the 2,205 lines across the three trilogy drafts (Paper I:
critical-line-foundation, Paper II: primes-as-closure-irreducibles, Paper III:
euler-bridge-closure-irreducibles), how much content stands without leaning on
an interpretive overlay that geometry-first never verified?

**Honesty bar.** Geometry-first FINDINGS.md established three verified
structural facts about V_600: (1) 9-class Euclidean Bose–Mesner scheme, (2)
A_1-spectrum in Z[φ] with σ-paired (dim-4, dim-9, dim-16) eigenspaces, (3) the
1-skeleton is NOT a strict DRG. No "closure", "observation manifold",
"closure-irreducible", or "cascade-σ" claim has been independently verified.

---

## 1. Per-paper content audit

### Paper I — *Critical Line as Observation Manifold* (639 lines)

| Section | Content type | Survives honesty bar? |
|---------|--------------|------------------------|
| §2 σ-paired class on V_600 | Cites existence-programme Paper I T1 (eigenspace σ-pairing) | YES — verified geometry-first |
| §3 Mellin frame, critical line = Fix(τ_crit) | Cites rh-formal Thm 2 (τ_crit involution) | NO — geometry-first never built τ_crit |
| §4 Five-level typology L_0…L_4 | New definitional construction (vertex / orbit / spectral / K-pole / classical prime) | PARTIAL — L_0 verified (V_600 vertices), L_4 classical (Dedekind), L_1–L_3 are unsupported labels |
| §5 Observation-manifold interpretation | Marked Conditional under H-Observe | NO — purely interpretive |
| §6 Implications for classical RH | Disclaims it does not prove RH | OK as disclaimer, no positive content |
| §7 Relation to existing approaches | Survey | OK |
| §8 Falsifiers | OK |

**Verdict:** The σ-paired class on V_600 (§2) is the only structurally
load-bearing section that survives geometry-first. Everything else either
depends on rh-formal's τ_crit (geometry-first did not establish), introduces
unsupported labels (L_1–L_3), or is explicitly conditional/interpretive.

### Paper II — *Classical Primes as Closure-Irreducibles* (706 lines)

| Section | Content type | Survives honesty bar? |
|---------|--------------|------------------------|
| §2 Q(√5) as cascade's natural field | Justification narrative | NO — assumes the cascade-Q(√5) link |
| §3 Dedekind splitting law in Z[φ] | Classical Theorem (Dedekind 1871) | YES — classical fact, not VFD content |
| §4 L_4 σ-classification of classical primes | Conditional under H-SigmaRestrict | NO — labels a classical fact as "L_4" without earning |
| §5 Universal σ-pattern theorem | Conditional under H-SigmaRestrict + H-UniqueSigma | NO — depends on L_0–L_3 typology that didn't survive |
| §6–§8 Hecke obstruction + falsifiers | OK as disclaimer | OK |

**Verdict:** Paper II's mathematical content reduces to **Dedekind 1871** —
classical, century-old, doesn't need a new paper. The cascade-σ wrapping is
unsupported.

### Paper III — *Toward the Euler Bridge* (860 lines)

| Section | Content type | Survives honesty bar? |
|---------|--------------|------------------------|
| §2 Cascade L_4 ζ definition (ζ_L4 = ζ_K) | Conditional under H-NaturalIrreducibles + H-EulerBridge | NO — assumes the L_4 identification |
| §3 Dedekind factorisation ζ_K = ζ · L(χ_5) | Classical (Dedekind/Hecke) | YES — classical fact, not VFD content |
| §4 Main Euler-bridge theorem | Conditional under H-NaturalIrreducibles + H-EulerBridge | NO — labels classical fact as "bridge" without earning |
| §5–§6 Hypotheses + numerical verification | Sim verifies ζ(2) · L(2, χ_5) = ζ_K(2) to 10+ digits | Classical, well-known |
| §7–§9 Relation + falsifiers | OK |

**Verdict:** Paper III's mathematical content reduces to **classical Dedekind
factorisation of ζ_{Q(√5)}** — also century-old, also classical. The "Euler
bridge" framing is unsupported reinterpretation.

---

## 2. The honest summary

Stripping the interpretive overlay, the trilogy's substantive content is:

1. **V_600 has σ-paired eigenspaces (dim 4-9-16 in Galois-conjugate pairs).**
   — geometry-first verified.
2. **Classical Dedekind splitting in Z[φ] (Dedekind 1871).**
   — classical, century-old.
3. **Classical Dedekind factorisation ζ_K = ζ · L(χ_5) for K = Q(√5)
   (Dedekind/Hecke).** — classical, century-old.

Items 2 and 3 don't need new papers. Item 1 *is* a paper, but it's a paper
about V_600's structural data, not about "the critical line as observation
manifold" or "closure-irreducibles" or an "Euler bridge".

**The 2,205 lines reduce to ~one paper of ~25–30 pages, which is exactly the
Paper A described in FINDINGS.md §4.**

---

## 3. What to do with the existing drafts

Three honest options:

### Option (a): retire the trilogy, keep only the verified structural Paper A.
- Pros: cleanest, fully defensible.
- Cons: discards a lot of writing; the L_0–L_4 typology and σ-pattern
  framing are lost.
- Recovery path for typology: it becomes informal companion notes, not
  numbered papers, until each named hypothesis (H-Observe, H-SigmaRestrict,
  H-UniqueSigma, H-NaturalIrreducibles, H-EulerBridge) can be closed
  structurally or empirically.

### Option (b): demote the trilogy to "open research notes" and add Paper A as the structural foundation.
- Pros: keeps existing writing; positions Paper A as "what the trilogy was
  trying to find structural support for".
- Cons: the trilogy still depends on unverified hypotheses; calling them
  research notes is honest but inflates the public corpus.

### Option (c): partial salvage — pull only the survives-honesty-bar paragraphs from each paper into Paper A.
- Pros: gives Paper A more material (§2 of Paper I as core, §3 of Paper II
  and §3 of Paper III as classical-reference appendices).
- Cons: requires manual extraction and rewriting.

---

## 4. Recommendation

**Option (a) + (c).** Write Paper A around FINDINGS.md as the structural
foundation. Lift these specific paragraphs from the trilogy into Paper A:

- **Paper I §2 (σ-paired class on V_600)** — promotes to a load-bearing
  section of Paper A.
- **Paper II §3 (Dedekind splitting in Z[φ])** — used as a 1-page
  classical-background appendix.
- **Paper III §3 (Dedekind factorisation ζ_K = ζ · L(χ_5))** — used as a
  1-page classical-background appendix.

Move the trilogy's `.tex` files to `papers/archived/` with a README explaining
the demotion. Their named hypotheses (H-Observe, H-SigmaRestrict, etc.) become
TODO items for future structural work, not paper material.

The result: **one paper, structurally honest, ~25 pages**, with all
classical references properly cited and no unverified interpretation
load-bearing.

---

## 5. Concrete next steps if recommendation accepted

1. Create `papers/archived/closure-irreducibles-trilogy-2026-05/` and move
   the three .tex + repro directories there with a clear README explaining
   why they were demoted.
2. Create `papers/v600-structural/v600-structural.tex` as the new Paper A,
   structured around FINDINGS.md.
3. Lift Paper I §2, Paper II §3, Paper III §3 into Paper A as identified
   sections.
4. Update `project_critical_line_primes_paired.md` memory to reflect the
   demotion, so future sessions don't try to compile/ship the trilogy.
