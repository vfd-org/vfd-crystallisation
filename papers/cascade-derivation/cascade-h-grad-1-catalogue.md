# H-grad-1 — Math Catalogue

**Companion to:** `cascade-h-grad-1-closure.md`,
`WO-H-GRAD-1.md`.
**Status:** LEDGER. Lists every build target, numerical result,
and open item in H-grad-1. Cross-references the derivation note
and the verification sim.
**Date:** 2026-04-24.

---

## Builds (B1–B6)

Each build is defined by object/domain/codomain in §7 of the
derivation note. Status reflects sim-verification where applicable.

| ID | Object / Map | Bridge | Route | Status |
|----|---------------|--------|-------|--------|
| B1 | `B_I = {ω_1, …, ω_8} ⊂ I`, Z-basis of icosian ring | A1 | Conway–Sloane Ch. 8, Table 8.1 / Moody–Patera Thm 4.1 | **BUILD COMPLETE (sim-verified 2026-04-24)** |
| B2 | `q_I : I/2I_lat → F_2`, `q_I([x]) = Tr_{Q(φ)/Q}(N(x)) mod 2` | A2 | Classical, composed with B1 | **BUILD COMPLETE (sim-verified 2026-04-24)** |
| B3 | `μ_I : I/2I_lat ↠ (F_2)³` with 5-dim kernel `K` | A3 | K (Kirmse–Coxeter) | **BUILD COMPLETE (sim-verified 2026-04-24)** via `scripts/verify_h_grad_1_b3.py` |
| B4 | `red : Z[φ]⁶ → I/2I_lat`, factoring through `L_O/2L_O` | O2 | Route P (Phase-M3 projection) | **BUILD COMPLETE (sim-verified 2026-04-24)** via `scripts/verify_h_grad_1_b4.py` |
| B5 | Eight characters `χ_0, …, χ_7` of `Z[φ]⁶`, `≡ {1, e_1, …, e_7}` | A4 / O3 | Pontryagin pullback through μ∘red | **BUILD COMPLETE (sim-verified 2026-04-24)** via `scripts/verify_h_grad_1_b5.py` |
| B6 | `G_p`-canonicality proof sketch; G₂ pullback outlined | O1 | Witt extension (classical) + cascade pullback κ (outlined, not executed) | **PROOF-SKETCH COMPLETE at `G_p` level (2026-04-24)** — transitivity on 40 320 reduced frames via Witt's theorem in `O⁺(8, 2)`. Classical G₂/octonion pullback `κ : {KC octonion frames} → Adm_red` outlined in §5c B6.4, not fully constructed. Sanity-sim in `scripts/verify_h_grad_1_b6.py` confirms counts + type-equivalence. |

## Numerical results (N1–N3)

| ID | Claim | Sim | Status |
|----|-------|-----|--------|
| N1 | Explicit 8-element Z-basis `B_I ⊂ I`: all 120 unit icosians decompose as integer combinations of `B_I`; 120×8 coefficient matrix has rank 8 over Q; basis quaternion traces lie in Z[φ] | `scripts/verify_h_grad_1.py` §B1 | **VERIFIED** (120/120 PASS) |
| N2 | Mod-2 totals on I/2I_lat = 1 zero + **135** nonzero isotropic + **120** anisotropic = 256 = `|E_8/2E_8|`; polar form of `q_I` has F_2-rank 8 (non-degenerate, Arf invariant 0) | `scripts/verify_h_grad_1.py` §B2 | **VERIFIED** (matches canonical E_8/2E_8) |
| N3 | 120 unit icosians collapse to 60 distinct nonzero isotropic classes in I/2I_lat (since `u ≡ −u mod 2I_lat`) | `scripts/verify_h_grad_1.py` §Sanity | **VERIFIED** (60/60 PASS) |
| N4 | **270** maximal totally singular 4-dim subspaces of F_2⁸ under `q_I` (classical formula `N = ∏_{i=0}^{n-1}(2^i + 1) = 2·3·5·9 = 270` for `n = 4`); 30 contain the identity class `[1]`; canonical `L_0` lex-first NOT containing `[1]` (so `K = L_0 ⊕ ⟨[1]⟩` has dim 5); μ_I 3×8 matrix has rank 3, kernel size 32, image = all 8 of (F_2)³; all 8 octonion labels match v_i; 7 Fano lines sum to 0; **exhaustive F_2-linearity over all 65536 pairs** | `scripts/verify_h_grad_1_b3.py` | **VERIFIED** (all checks PASS) |
| N5 | Primal `red : Z[φ]⁶ → I/2I_lat` via Route P (Phase-M3 projection `π_int(L_12) = σ(I) ⊕ M`). Z[φ]-basis `{ω₁, ω₂, ω₄, ω₅}` verified via det ±1; `red` as 8×12 F_2 matrix has rank 8, image 256, kernel 16 (dim 4); `μ_I ∘ red` has rank 3 and hits all 8 Fano values; 4 M-summand generators all map to 0. | `scripts/verify_h_grad_1_b4.py` | **VERIFIED** (all checks PASS) |
| N6 | 8 Pontryagin characters `α_v ∈ C_O ⊂ F_2¹²` indexed by `v ∈ (F_2)³`, defined as `α_v = v^T · MR` where `MR = M_μ · R` is the composed B3/B4 matrix. C_O is a 3-dim F_2-subspace (order-8 subgroup) of the mod-2 character quotient. Pontryagin pairing `⟨α_v, x⟩ = v · (μ∘red)(x)` verified exhaustively over all 32 768 `(v, x)` pairs. Trace-dual lifts `α_v = (1/2)·Σ c_j · τ_{j mod 2}` with `τ_0 = (3-φ)/5`, `τ_1 = (-1+2φ)/5` give 8 distinct elements of Q(φ)⁶/(Z[φ]⁶)^∨. | `scripts/verify_h_grad_1_b5.py` | **VERIFIED** (all checks PASS) |
| N7 | Reduced-frame set `Adm_red(V, q, p, A)` has size **40 320 = 240 · 168**: 240 max totally singular 4-subspaces `L` with `p = [1] ∉ L`, times 168 = \|GL(3,2)\| labellings of `V/K ≅ (F_2)³`. `p = [1]` is **isotropic** (`q(p) = Tr(N(1)) mod 2 = 2 mod 2 = 0`), consistent with the 30 max isotropics through `p` and 240 not through `p`. `G_p = Stab_{O⁺(8,2)}(p)` acts transitively on `Adm_red` by Witt's extension theorem (proof-sketch in §5c; sanity-sim verifies counts and type-equivalence on 2 random pairs). | `scripts/verify_h_grad_1_b6.py` | **VERIFIED** (counts + type-equivalence PASS; full orbit enumeration deferred) |

**Bug caught 2026-04-23→24:** the original task draft stated the
isotropic/anisotropic counts as `120 / 135`. The correct classical
E_8/2E_8 totals are `135 isotropic + 120 anisotropic` (Conway–Sloane
Ch. 8). `cascade-h-grad-1-closure.md` §3.3 and
`cascade-fano-grading-lift.md:163-169` were corrected in the same
round. The sim flagged the mismatch by reporting FAIL rather than
hand-tuning — correct behaviour per task guardrail §4.

## Acceptance criteria status (per WO-H-GRAD-1.md §0)

| Item | Status | Build | Note |
|------|--------|-------|------|
| A1 | **BUILD COMPLETE (sim-verified)** | B1 | Z-basis exhibited; 120/120 decomposition |
| A2 | **BUILD COMPLETE (sim-verified)** | B2 | Counts + polar rank = Arf-0 E_8/2E_8 |
| A3 | **BUILD COMPLETE (sim-verified)** | B3 | Route K (Kirmse-Coxeter) closed; 270 maximal isotropics enumerated, μ_I construction passes all 6 AC checks |
| A4 | **BUILD COMPLETE (sim-verified)** | B4 + B5 | Both primal `red` and dual C_O characters sim-closed |
| O1 | **PROOF-SKETCH COMPLETE (2026-04-24)** | B6 | `G_p`-level transitivity via Witt's theorem; G₂ pullback outlined |
| O2 | **BUILD COMPLETE (sim-verified)** | B4 | Primal map `Z[φ]⁶ → I/2I_lat` closed; Route P via Phase-M3 projection |
| O3 | **BUILD COMPLETE (sim-verified)** | B5 | Eight Pontryagin representatives via trace-dual basis |
| O4 | **BUILD COMPLETE (sim-verified)** | B1 | Subsumed by A1 |
| O5 | **BUILD COMPLETE (sim-verified)** | B4 + B5 | V1–V3 verification steps executed |

## Route commentary

- **Route K vs Route Q for B3.** Route K (Kirmse–Coxeter) is
  classical and safer. Route Q (QMS-3 seven-Fano-triad) is a
  conjectural cascade-internal route via the god-prime
  decomposition `084473 = 137(7·87+8) − 56` (`insight.md:670-679`).
  Route Q requires a canonical attachment map
  `Θ_QMS : I/2I_lat → (F_2)³` that reproduces the QMS-3 factor-7
  count. The seven Fano triads themselves are *not* explicitly
  listed in `insight.md`; Route Q begins as a conjecture.

- **Pentagonal holonomy orthogonality.** The Z[φ]^×-valued edge
  1-cocycle `ω` and cascade clock `T` from `insight.md:878-892` are
  orthogonal to H-grad-1 (additive vs multiplicative). They
  belong to the observer-zeta O2 track (intrinsic ζ_F from
  F-iteration), not to the Fano grading.

## Upstream / external dependencies

| Source | Use | Status |
|--------|-----|--------|
| `cascade-algebraic-substrate.tex:480–514` | Canonical icosian definition | Settled 2026-04-23 via Task #10 |
| Conway–Sloane, *Sphere Packings* Ch. 8 | Icosian basis + E_8 identification | Standard literature |
| Moody–Patera, J. Phys. A 26 (1993) Thm 4.1 | Equivalent 8-unit icosian basis | Standard literature |
| `cascade-fano-grading-lift.md:163-169` | E_8/2E_8 counts | Corrected 2026-04-24 to 135/120 |
| `cascade-q-o-measurement-bridge.md:112-138` | `Q_O ≅ Meas(S⁷, σ)` | Used for B5 derivation; Thm 3.1 does NOT give explicit Pontryagin generators |
| `insight.md:670-679` | QMS-3 / 7-Fano-triad motivation | Route Q conjectural only |
| `insight.md:878-892` | Pentagonal holonomy | Orthogonal; flagged for observer-zeta O2 track |

## Codex review history

| Round | Date | Verdict | Notes |
|-------|------|---------|-------|
| 1 | 2026-04-23 | Publication ready: no; 4 residuals + structural gaps | `WO-H-GRAD-1-20260423T104006Z.md` |
| 2 | 2026-04-23 | Publication ready: no; must-fix downgrade reversal | `WO-H-GRAD-1-20260423T225436Z.md` |
| 3 | 2026-04-23 | Publication ready: no; B1/B2 sim-closure credible, A2 stale counts | `WO-H-GRAD-1-20260423T231558Z.md` |

## Out of scope

- **Full cascade-specific `G_2` pullback `κ`** from real octonion
  frames to `Adm_red`. B6 outlines this (§5c, B6.4) but does not
  execute the construction; it requires writing Conway–Sloane's
  classical icosian↔E_8 identification explicitly at the cascade
  level. The claim that `G_p`-canonicality suffices for the
  H-grad-1 / P-A Access Principle application is a **declared
  judgement** here, not yet backed by a formal equivalence
  theorem against the statement in
  `cascade-access-principle-theorem.md`. Formalising this
  equivalence (or executing `κ` to recover full G₂-canonicality)
  would close the residual gap.
- Explicit orbit enumeration over all 40 320 reduced frames
  under a generating set of `G_p`. The sanity-sim only checks
  counts and type-equivalence on two random pairs; full orbit
  enumeration is a worthwhile follow-up but not blocking.
- Any "publication ready" declaration for H-grad-1 as a whole,
  pending either the cascade-side pullback, the formal
  `G_p`-sufficiency equivalence, or an explicit scope statement
  that closes the residual judgement.
