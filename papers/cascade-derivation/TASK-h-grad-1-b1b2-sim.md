# Task — Build B1 + B2 verification sim

**Task type:** Pair-programmer work (codex lead, Claude review).
**Scope:** Implement builds B1 (canonical icosian Z-basis) and B2
(mod-2 quadratic form count) from
`cascade-h-grad-1-closure.md:343-431` as an executable verification
script.
**Date opened:** 2026-04-23.

---

## §1 Goal

Produce `papers/cascade-derivation/scripts/verify_h_grad_1.py` which,
on a fresh run, prints:

1. **B1 output.** Eight explicit quaternions `ω_1, …, ω_8 ∈ H` given
   in exact Z[φ]-arithmetic (tuples of rationals or `Fraction`s over
   `Q(√5)`). Verify:
   - Each `ω_a` is a unit icosian (norm ∈ Z[φ], trace ∈ Z[φ]).
   - The 120 unit icosians (8 integer + 16 Hurwitz-half + 96 golden)
     each decompose uniquely as Z-linear combinations of
     `ω_1, …, ω_8`.
   - Equivalently, the 120×8 coefficient matrix has rank 8 over Q
     and every decomposition yields integer coefficients.

2. **B2 output.** Construct `I/2I_lat ≅ F_2^8` via mod-2 reduction
   of coefficients in the basis `ω_1, …, ω_8`. Define the F_2
   quadratic form `q([x]) = Tr_{Q(φ)/Q}(N(x)) mod 2` where
   `N(x) = x x̄` is the quaternion norm and `Tr_{Q(φ)/Q}` is the
   trace `a + bφ ↦ 2a + b`. Compute `q` on all 256 elements and
   verify the classical `E_8/2E_8` counts (**corrected
   2026-04-24**: the original draft reversed these):
   - 1 zero vector,
   - **135** nonzero isotropic vectors (`q = 0`),
   - **120** anisotropic vectors (`q = 1`).

3. **Sanity check.** Verify that the 120 unit icosians land on
   **60** distinct nonzero isotropic classes in `I/2I_lat` — the
   pair `u, −u` collapse since `2u ∈ 2I_lat`. All 60 classes have
   `q = 0`. This anchors the identification of `(I/2I_lat, q)`
   with the
   standard `E_8 / 2E_8` F_2-quadratic.

Pretty-printed output summarising each check with PASS / FAIL.

---

## §2 Why this is tractable in one round

- The icosian ring is well-documented (Conway–Sloane Ch. 8,
  Moody–Patera 1993, Wikipedia "icosian"). You have the canonical
  basis from pretraining.
- The arithmetic is exact. `Q(√5)` arithmetic is just 2-tuples of
  rationals; no floating-point.
- The verification is entirely finite (120 icosians, 256 mod-2
  classes).
- No new mathematical content is introduced; the sim just
  implements a textbook construction.

---

## §3 Acceptance criteria

- **AC1:** `scripts/verify_h_grad_1.py` exists and runs without
  errors on Python 3.10+.
- **AC2:** All 120 unit icosians decompose as **integer**
  combinations of the 8 basis elements. PASS printed.
- **AC3:** Classical counts verified: 1 + 120 + 135 = 256.
- **AC4:** No floating-point arithmetic used in the rank /
  decomposition checks. Use `Fraction` or integer arithmetic
  throughout.
- **AC5:** Update `cascade-h-grad-1-closure.md` §2 and §3 to
  reference the sim and flip B1/B2 status from "BUILD REQUIRED"
  to "BUILD COMPLETE (sim-verified 2026-04-23)".
- **AC6:** Update `cascade-h-grad-1-closure.md` §7 B1/B2 entries
  with the same status flip and add a "Verified by" line pointing
  at the sim.
- **AC7:** Update `WO-H-GRAD-1.md` Round-2 table A1/A2/O4 rows
  likewise.

---

## §4 Scope guardrails

- **Do not** attempt B3–B6 in this round.
- **Do not** touch `cascade-algebraic-substrate.tex` or any paper
  outside `papers/cascade-derivation/`.
- **Do not** declare H-grad-1 closed. Only B1 and B2 are closed by
  a successful sim.
- If the canonical basis you write down *does not* decompose all
  120 unit icosians, STOP and report. Do not fudge coefficients.
- If the F_2 counts don't come out 120 / 135 / 1, STOP and report.
  Do not adjust the quadratic form to force the count.

---

## §5 Reference material (codex already knows this from pretraining)

- Conway–Sloane, *Sphere Packings, Lattices, and Groups* 3rd ed.,
  Ch. 8.2 (icosian ring), Ch. 8.2.2 Table 8.1, Ch. 8.2.2 Eq. (17)
  (rank-8 Z-module structure).
- Moody & Patera, "Quasicrystals and Icosians," J. Phys. A 26
  (1993), Thm 4.1 (eight unit-icosian basis).
- Wilson, "The Finite Simple Groups," §5 (icosian structure on
  E_8).

If the canonical Moody–Patera basis uses a specific choice of 8
unit icosians, use theirs verbatim and cite the page. Alternative
choices are fine provided they pass the AC2 check.

---

## §6 Handoff format

Print to stdout:

```
=== B1 — Z-basis of icosian ring I ===
Basis B_I = {ω_1, ..., ω_8}:
  ω_1 = ...
  ω_2 = ...
  ...

Unit-icosian decomposition check: 120 / 120 decompose as integer
combinations — PASS.

=== B2 — Mod-2 quadratic form on I/2I_lat ===
Quadratic form: q([x]) = Tr_{Q(φ)/Q}(N(x)) mod 2

Classical counts: zero = 1, isotropic = 120, anisotropic = 135 — PASS.

=== Sanity ===
120 unit icosians land on 120 distinct nonzero isotropic classes — PASS.
```

No drama, no prose. If any check fails, print the failure with the
offending element(s) and STOP.

---

## §7 Reviewer expectations

Claude will:

1. Read the sim.
2. Run it and verify stdout matches the expected format with PASS.
3. Check that no hand-tuning was used to force a PASS (no
   suspicious comments, no silently-adjusted elements).
4. Verify §2 / §3 / §7 status flips in the derivation note.
5. Fire `scripts/review_wo.sh` with focus "audit sim correctness
   and status flips; verify 120/135/1 counts reflect the actual
   E_8/2E_8 mod-2 form and not something tuned to match."
