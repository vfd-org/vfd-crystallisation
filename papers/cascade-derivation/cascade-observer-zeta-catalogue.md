# Observer-Zeta Programme — Math Catalogue

**Companion to:** `cascade-observer-zeta.md`.
**Status:** LEDGER. Lists every definition, conjecture, open item,
numerical result, and external motivation introduced in the note.
**Date:** 2026-04-23.

This ledger is not a derivation; it is a cross-reference. Each entry
points to the note location and gives the current status after four
codex review rounds.

---

## Definitions

| ID | Name | Note § | Status |
|----|------|--------|--------|
| D1 | 𝒞oalg(F) (category of F-coalgebras) | §3.1 | IMPORTED (standard categorical construction); reframe target per codex Round 1 |
| D2 | F-irreducible F-coalgebra (candidate) | §3.1 | WORKING-DRAFT DEFINITION, NOT PROVED WELL-POSED (see O1) |
| D3 | σ : 𝒞 → 𝒞 auto-functor (Galois twist lift) | §1.2 | WORKING DESCRIPTION, NOT CONSTRUCTED |
| D4 | ζ_F candidate dynamical zeta | §3.3 (referenced) | **NOT DEFINED**; all downstream uses are vacuous until construction |

## Research questions (P1–P5, reframed)

Note per §3: these are stated as open questions, not conjectures with
truth values. Each has a specific named obstruction before it can be
evaluated.

| ID | Question | Note § | Blocked by |
|----|----------|--------|------------|
| P1 | Canonical bijection F-Irr(𝒞oalg(F)) ≅ Spec(O_K) \ {0} ? | §3.2 | O1 (F-Irr not defined); O7 |
| P2 | Does F-iteration intrinsically produce a Dirichlet series, and does it equal ζ_K ? | §3.3 | O2 (ζ_F not constructed); O7 |
| P3 | Does σ-action on (hypothetical) ζ_F admit eigenspace decomposition matching ζ · L(χ_5) ? | §3.4 | P2; the classical Artin side is standard |
| P4 | Lawvere-style universal property distinguishing σ-fixed sub-object of ν F ? | §3.5 | O3-a/b/c (CCC not shown to exist); NOT YET WELL-POSED |
| P5 | Canonical L : F-Irr(𝒞oalg(F)) → V(600-cell)/H_4 ? | §3.6 | O1, O5; O6 resolved 2026-04-23 |
| P5-apex | L(god-prime) = specific Fano triad via H-grad-1 μ ? | §3.7 | H-grad-1 (WO-H-GRAD-1 codex R1 open); O6 resolved 2026-04-23 |

## Numerical results

| ID | Claim | Script | Status |
|----|-------|--------|--------|
| N1 | π(10⁴) = 1229 rational primes: 619 inert, 609 split, 1 ramified in ℤ[φ] | `scripts/observer_prime_inert_split.py` | **VERIFIED** (classical) |
| N2 | Bare-rung F has 32 F-fixed rung-subsets; 12 distinct Z-dim norms; finite Dirichlet support | `scripts/observer_zeta_candidate.py` Exp A | **VERIFIED** (toy) |
| N3 | F1 scalar shadow ζ_F1(1) ≈ 3.3599 (reciprocal-Fibonacci constant) | `scripts/observer_zeta_candidate.py` Exp B | **VERIFIED** (toy) |
| N4 | ζ_K = ζ · L(χ_5) at Dirichlet coefficients n ≤ 100: 100/100 matches | `scripts/observer_zeta_dedekind.py` Exp C | **VERIFIED** (classical) |
| N5 | God-prime P_G = 2^136279840 + 1 is inert in ℤ[φ] (P_G ≡ 2 mod 5) | §3.7 inline | **VERIFIED** (arithmetic fact) |
| N6 | 084473 mod 7 = 4 (candidate Fano-triad index) | §3.7 inline | **VERIFIED** (arithmetic fact); content depends on H-grad-1 |

## Open items and resolved audit items

| ID | Description | Load-bearing | Blocking |
|----|-------------|-------------|----------|
| O1 | Non-vacuous F-irreducibility definition on 𝒞oalg(F) | Yes | P1, P5 |
| O2 | Intrinsic construction of ζ_F from F-iteration | Yes | P2, P3, P4 |
| O3-a | CCC structure on 𝒞 (or enlargement) | Yes (framework) | P4 |
| O3-b | σ : 𝒞 → 𝒞 explicit; verify σF ≅ Fσ | Yes (framework) | P4 |
| O3-c | 𝒞oalg(F) inherits CCC + σ-action compatibly | Yes (framework) | P4 |
| O4 | H-grad-1 closure (WO-H-GRAD-1) | No for P1–P4; yes for P5-apex | P5-apex only |
| O5 | Canonical L : F-Irr(𝒞oalg(F)) → V(600-cell)/H_4 | Yes | P5 |
| O6 | **RESOLVED 2026-04-23.** Upstream icosian-coordinatisation inconsistency; `cascade-12d-closure.md` Level 2 now follows the canonical `papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:480-514` definition and explicitly rejects {1, i, j, k} as a Z[φ]-basis | No (audit trail only) | None; prior conflict was formerly at `cascade-12d-closure.md:39` vs `papers/cascade-algebraic-substrate/cascade-algebraic-substrate.tex:506-513` |
| O7 | Does F intrinsically produce Spec(O_K), or externally? | **DECISIVE** | P1, P2, P3, P4 all depend on positive resolution |

## Closed / conditional / classical items (C1–C8)

See `cascade-observer-zeta.md` §4.1 status ledger. Not duplicated here.

**Source-status mismatches** (flagged in §4.1):
- **C6b:** note downgrades to "CONDITIONAL on candidate μ"; cited source claims "UNCONDITIONAL."
- **C7:** O6 is resolved; note still downgrades to "working-note / simplified" because `dual_600cell_factor2.py:142-145` remains a simplified decomposition caveat.

## External motivation (NOT AUDITED in this repo)

| ID | Item | Location | Audit status |
|----|------|----------|--------------|
| E1 | Prime Detector shell-signature classifier | `/Prime Detector/vfd_prime_detector.js` (sibling project) | NOT AUDITABLE in this repo |
| E2 | aria-chess crystallisation architecture | `/aria-chess/docs/UNIVERSAL_CRYSTALLISATION_ARCHITECTURE.md` (sibling project) | NOT AUDITABLE in this repo |

E1 and E2 are motivational background only. No claim in the note's
mathematical content rests on them. Any downstream use would require a
self-contained sim in `papers/cascade-derivation/scripts/`.

## Codex review history

| Round | Review file | Verdict |
|-------|-------------|---------|
| 1 | `docs/reviews/cascade-observer-zeta-20260423T123044Z.md` | Publication ready: no. 4 structural defects. |
| 2 | `docs/reviews/cascade-observer-zeta-20260423T130513Z.md` | Publication ready: no. 4 fixes landed, 3 residuals. |
| 3 | `docs/reviews/cascade-observer-zeta-20260423T131344Z.md` | Publication ready: no. 5 fixes landed, 3 residuals. |
| 4 | `docs/reviews/cascade-observer-zeta-20260423T131950Z.md` | Publication ready: no. 4 fixes landed, 3 residuals (ledger + §2.5 + C6b/C7 wording). |
| 5 | TBD | TBD — target: yes at problem-statement scope. |

## Out-of-scope (explicit)

- **Not in scope:** proving RH. Proving GRH over K. Constructing ν F
  unconditionally. Showing 𝒞 is Cartesian-closed.
- **Not in scope:** philosophical claims about consciousness, cogito,
  or spiritual-mystical content.
- **Not in scope:** replacement for `cascade-rh-proof.md` Hilbert-Pólya
  programme (those are independent routes).
- **Not in scope:** closing H-grad-1 (own WO).
