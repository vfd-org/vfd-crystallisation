# WO-VFD-INVARIANT-CLOSURE-CROSSDOMAIN-002 — Report

**Grade: MEDIUM PASS.**

## What was built
A closure-mode classifier that *searches for a positive form B* under which T closes and labels the mode (ISOMETRIC / SELF_ADJOINT / DISSIPATIVE / CRITICAL / MIXED / NONE), via rigorous spectrum + discrete-Lyapunov analysis; a control harness; and seven domain suites.

## Headline results (true strength)
1. **Calibration (all correct).** The classifier rediscovers the known closure mode on 8 known systems — finite cycles→ISOMETRIC, contractions→DISSIPATIVE, rotation→ISOMETRIC, Jordan block→CRITICAL, ρ>1→NONE. This is the calibration the WO demanded.
2. **Collatz cycle elimination (known, via new route).** The exact closure Diophantine equation eliminates the 1-cycle class for 3n+1 (only n=1 survives) and finds no small nontrivial cycles — recovering Steiner 1977 through the capacity/closure language. Genuine narrowing of the search space, but not new mathematics.
3. **Prime separation (real, known bias).** Real primes separate from density-matched fakes: trivially by residue (layer 1) and substantively by the Lemke-Oliver–Soundararajan consecutive-digit correlation (layer 2, ratio 1205× over shuffled/independent controls). The engine *does* tell real arithmetic structure from fake — necessary RH hygiene.
4. **Hypothesis correction confirmed.** Triad/cyclic closure is ISOMETRIC, not self-adjoint; the universal notion is *a positive invariant form*.

## The walls (unmoved)
- **Collatz:** no infinite non-closing braid = the conjecture.
- **RH:** infinite-limit Weil positivity = Connes arithmetic site. The positivity form is even *insensitive to prime shuffling* (caught only by the explicit-formula balance), underlining that the missing object is the positivity certificate, not a correlation.
- **Navier–Stokes:** supercriticality → Q sign undetermined; our shell sign-crossing is not robust.

## Honest bottom line
The upgrade does exactly what was asked of a *diagnostic*: it calibrates on known systems, separates true systems from controls in two domains, classifies the closure modes, and extracts each proof wall. It **reproduces known results via a new route** (Collatz cycles, LO-S) and **corrects a false hypothesis** (self-adjoint→positive-invariant-form) — items 1 and 4 of the WO's value test. It does **not** achieve item 3 (a *new* missing invariant) in any open problem: every wall is the original theorem. No claim of proof, partial proof, or reduction. Local; not pushed.
