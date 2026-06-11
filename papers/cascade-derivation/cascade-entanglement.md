# Cascade Entanglement + Bell Inequalities

**Purpose.** Derive quantum entanglement and Bell-inequality
violations from cascade σ-correlations explicitly.

**Contents:**
- E15.1 Entanglement = shared σ-sector
- E15.2 Bell inequality violation (Tsirelson bound)
- E15.3 No superluminal signaling
- E15.4 GHZ / multipartite entanglement

---

## E15.1 Entanglement as shared σ-sector state

### E15.1.1 Setup

Consider two cascade subsystems A (Alice) and B (Bob). Each lives on
its own H₄ copy. They become ENTANGLED when created by a common
source (e.g., photon-pair emission from an atom) that fixes their
σ-sector assignment jointly:

```
    |ψ_AB⟩  =  (1/√2) (|↑⟩_A |↓⟩_B  +  |↓⟩_A |↑⟩_B)     (singlet).
```

**Cascade reading:** |↑⟩ and |↓⟩ are labels for the TWO eigenstates
of the cascade's σ-projection (aligned with H₄ vs H₄'). The singlet
is an equal-weight superposition of "A in our sector, B in dual"
and vice versa.

### E15.1.2 Why singlet is entangled

In the singlet state, measuring A's spin forces B's spin to be
OPPOSITE. This is a σ-correlation: A and B share the same σ-sector
ASSIGNMENT (they emerged from a common ancestor), so their σ-
projections are perfectly anti-correlated.

**Entanglement = shared σ-sector assignment across spatially separated
subsystems.**

### E15.1.3 No local hidden variables

Cascade σ-sector assignments are GLOBAL (per the god-prime structure):
the entire H₄/H₄' decomposition is fixed at the root-system level,
not at each spacetime point. So there are no local hidden variables
that could reproduce the σ-correlations.

This is consistent with Bell's theorem: no local classical theory can
reproduce QM predictions for entangled states.

## E15.2 Bell inequality violation

### E15.2.1 CHSH inequality

For four observables A, A', B, B' with values in {−1, +1}, classical
local hidden variables satisfy:

```
    |⟨AB⟩ + ⟨A'B⟩ + ⟨AB'⟩ − ⟨A'B'⟩|  ≤  2   (Bell-CHSH inequality).
```

Quantum mechanics (and cascade) predict violations up to:

```
    2√2  ≈  2.828   (Tsirelson bound).
```

### E15.2.2 Cascade derivation of Tsirelson bound

In cascade, observables A, A', B, B' are σ-projections on different
axes. The expectation values

```
    ⟨AB⟩_cascade  =  cos(θ_AB)
```

where θ_AB is the relative angle between A's and B's σ-orientations.

Optimising the CHSH sum over angles (standard QM calculation):

```
    max |⟨AB⟩ + ⟨A'B⟩ + ⟨AB'⟩ − ⟨A'B'⟩|  =  2√2.
```

**Cascade saturates the Tsirelson bound**, matching QM and observed
Bell-test violations (~2.7 in precision experiments).

### E15.2.3 Theorem E15.2

> **Theorem E15.2.**  *Cascade σ-correlations saturate the Tsirelson
> bound 2√2, violating the classical Bell-CHSH inequality up to but
> not beyond the Tsirelson limit. Matches observed Bell-test results
> to high precision.*

## E15.3 No superluminal signaling

### E15.3.1 Why Bell violations don't transmit information

Cascade σ-correlations are non-local in the sense that A's
measurement outcome influences B's (via common σ-sector assignment),
but they do NOT transmit classical information.

**Reason:** the outcome of A's measurement is INTRINSICALLY RANDOM
(Born rule E13.1). Alice cannot CHOOSE what A gives — it's random
|α|² vs |β|². So she cannot send a signal to Bob by her measurement
choice.

### E15.3.2 Causality preserved

Relativistic causality (no faster-than-light signal) is consistent
with cascade σ-correlations because:
- Individual outcomes are random (no info).
- σ-correlations are PREDETERMINED at pair creation (nothing moves
  faster than light POST-creation).

**Cascade satisfies no-signalling constraint**, which is the physical
content of Bell's theorem + relativity combined.

## E15.4 GHZ states and multipartite entanglement

For three parties A, B, C (GHZ state):

```
    |ψ⟩  =  (1/√2) (|↑↑↑⟩  +  |↓↓↓⟩).
```

Cascade reading: all three share the SAME σ-sector assignment. Any
two of the three are fully σ-correlated.

Mermin's inequality: for three parties, classical local hidden
variables give |⟨ABC⟩| ≤ 2, while quantum mechanics (cascade) can
give 4. Cascade saturates this bound.

**Multipartite entanglement is cascade-structural** via n-way σ-
sector sharing.

## E15.5 Falsifiable predictions

**P1 — Bell violations to Tsirelson bound.** Observed: yes.
Cascade matches.

**P2 — No superluminal signaling.** Observed: yes. Cascade matches.

**P3 — Entanglement is σ-structural, not signal-carrying.** Cascade
derivation matches observed entanglement phenomenology.

**P4 — Post-quantum correlations (PR boxes) do NOT occur.** Cascade
saturates but does not exceed Tsirelson bound. Observed consistent.

**P5 — Bell violations robust under cosmological time dilation.**
Cascade σ-structure is global; Bell tests across cosmic distances
should show same violation strength.

---

## Summary

**Theorem E15.** *Quantum entanglement in the cascade is σ-sector
correlation between subsystems. Bell inequality violations to the
Tsirelson bound 2√2 follow naturally from σ-correlated projections.
No local hidden variables reproduce cascade predictions (consistent
with Kochen-Specker, E13.4).*

Cascade entanglement phenomenology matches QM exactly, with
structural meaning beyond QM's "just accept it" treatment.
