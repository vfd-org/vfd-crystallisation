# WO-SHELL-OFFSET-001: The Shell-Integer Rule and the Offset Dynamics

**Date:** 2026-06-12 (Phase C added same day)
**Status:** First structured attack executed. **The rule was not derived — and the attack establishes, at proof grade, *why the easy routes cannot work*, what any future rule must look like, one excluded dressing form, and one recorded lead.** Every conclusion, including each null, is machine-checked: `scripts/explore_shell_rule.py` (8/8 PASS).
**Discipline:** golden-ratio expressions can "fit" any spectrum (the W5 trap). This work order therefore enumerates structure-derived hypothesis classes only, fixes criteria before judging, accounts for look-elsewhere, and publishes the negatives as constraints.

---

## 1. The target

Two derivations would convert the mass ladder from placement to prediction:
- **(i) the shell-integer rule**: a map (particle quantum numbers) → integer shell N, for the table N(L) = (107, 96, 90), N(U) = (104, 91, 81), N(D) = (102, 96, 88), N(W,Z,H) = (82, 82, 81);
- **(ii) the offset dynamics**: the sub-shell residuals (−0.38 … +0.48), the framework's analogue of radiative corrections.

## 2. What the attack PROVED (negatives with proof status)

**SR1 — Curvature obstruction (kills the largest class).** The generation curvatures (second differences) of the charged-fermion shells are **(5, 3, −2)** for (L, U, D) — three distinct values. In any rule of the form N = a_type + f(g) — with type-dependent offsets from *any* generation-independent features (charge, colour, isospin, hypercharge, anything static) and *any* universal generation function f — the curvature is f(3) − 2f(2) + f(1), independent of type. Distinct curvatures therefore refute **every** rule in the class "static quantum numbers + universal generation dependence". This is a proof, not a failed search.

**SR2 — Even per-type linear fails.** Within-type steps are unequal for all three types (L: −11, −6; U: −13, −10; D: −6, −8), so per-type affine rules (6 parameters) have no exact fit either. The cheapest exact polynomial class is quadratic-per-type: 9 parameters for 9 integers — zero compression, inadmissible by SR3's budget.

**SR3 — The bar for any future proposal.** The 9 charged-fermion integers carry ~43 bits; an admissible rule must spend ≤ ~25 bits of parameters (compression ≥ 1.7×). Any future claim that doesn't clear this bar is numerology by definition, whatever its R².

**SR4 — Cascade residues: null.** Residues mod 24 hit the rung numbers {0, 8, 16} 4/12 times: raw p = 0.053, ≈ 0.32 after the ~6-modulus look-elsewhere discount. The "96 = 24×4" reading does **not** extend to a general rung-residue rule on present evidence.

**SR8 — Simple log dressing excluded.** A one-loop-type dressing δ = c·Q²·ln(m_P/m) is monotone in the shell; the lepton offsets (+0.079, −0.0002, +0.135) are non-monotone. Excluded within the lepton sector.

## 3. What the attack FOUND (positives, graded)

**SR6 — The scheme-dependence gradient (observation, n = 13).** Mean |offset|: leptons 0.071 < EW bosons 0.184 < quarks 0.288 < composite 0.462 — monotone. The ladder is sharpest exactly where mass is a clean pole observable and worst where it is scheme-dependent (MS-bar light quarks) or confinement-dressed. **Implication for the target itself:** part of the "offset problem" is an artifact of comparing the ladder to scheme-dependent numbers; the proper targets are physical pole masses and hadron masses. Any future offset dynamics should be formulated against those.

**SR5 — One electroweak cluster.** W, Z, H sit at shells (82, 82, 81): one EW scale, not three independent placements — the rule's job for the boson sector is to place *one* cluster plus splittings, a smaller task than it first appears.

**SR7 — A lead, not a law (recorded with its failure).** The pre-registered expectation was a null; the data refused it in-sample: signed offsets regress on (Q², colour, N) with R² = 0.86, permutation p = 0.011, leave-one-out R² = 0.46. But the fermion-fitted law **fails catastrophically out-of-sample** on the bosons it never saw (Z predicted +1.34 vs observed −0.049 — beyond the admissible offset range entirely). Verdict: a sector-limited correlation worth re-testing if/when couplings are derived; not a law; not announced as one.

## 4. Why this is the honest state of the art (and what would change it)

The two routes that could still produce the rule:

1. **The dynamical route (the real one).** A particle = a localized closure mode; its shell = the depth at which that mode closes; the offset = its self-energy under the substrate's interaction. Computing either requires the derived couplings (the open coupling sector) and the mode spectroscopy of the interacting closure flow. This is blocked *behind* the couplings item, not behind cleverness with integers — which is consistent with everything SR1–SR2 proved: the integers do not factor through static quantum numbers, exactly as expected if they encode interacting dynamics.
2. **The pole-mass reformulation (cheap, should be done first).** Re-derive the shell table against pole/physical masses only (leptons, W/Z pole, top pole, hadrons instead of light quarks). If the SR6 gradient is right, the reformulated table should be materially sharper — a falsifiable expectation of this WO.

What is now impossible to do honestly: announce a shell rule from polynomial/static-feature classes (SR1–SR2 are proofs), or an offset law fitted to one sector (SR7's out-of-sample failure is the cautionary record).

## 4b. Phase C: the sieve hypothesis (intermediate geometry / prime resonances)

A genuinely different class, proposed from the 5×24 Schläfli structure: the geometry generates a **set of allowed levels** (a sieve), and particles occupy allowed levels. A sieve is not a function of quantum numbers, so the curvature obstruction of SR1 **does not apply to it** — the class is live. Tested (`scripts/explore_geometric_ladder.py`, 3/3 PASS, exact hypergeometric null model, Bonferroni over 8 sieves, density bound 18/27):

| Sieve (provenance) | hits | density | corrected p |
|---|---|---|---|
| multiples of 8 (Observer rung) | 3/9 | 3/27 | 0.23 |
| multiples of 6 (D₄ Coxeter) | 3/9 | 4/27 | 0.75 |
| 24a + 5b, small coeffs (the 5×24 coset idea) | 2/9 | 7/27 | 1.00 |
| H4 degrees 30a+20b+12c+2d | 6/9 | 13/27 | 1.00 |
| 96 ± E8 exponents | 2/9 | 8/27 | 1.00 |
| primes + prime powers | 2/9 | 7/27 | 1.00 |
| split-prime resonances (p, 2p; p ≡ ±1 mod 5) | 1/9 | 3/27 | 1.00 |
| pentagonal classes (0, ±1 mod 5) | 5/9 | 16/27 | 0.76 |

**Verdict: NULL across all eight admissible generators** — none beats chance after correction. **The open door, quantified (GL3):** a *derived* level set capturing all nine observed shells clears the pre-registered bar iff its span-density is ≤ 9/27 ≈ one-third. That is the precise target for any future intermediate-geometry construction (finer Schläfli strata, new prime-resonance levels from the pentagonal-clock instrument): derive the set first, from geometry, with no sight of the shell table — then score it once.

## 5. Verification

`scripts/explore_shell_rule.py` — 8/8 PASS; `scripts/explore_geometric_ladder.py` — 3/3 PASS (Phase C); each PASS reproduces a recorded conclusion including each null. Companion to `docs/sm-closeability-audit.md` §2 and `scripts/sm_ledger.py`.
