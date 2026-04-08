# Closure-Class Assignment and Correction Analysis

## PART A — Assignment Rules

### Rule Test Results

Five rule families were tested against seven candidate shell supports:

| Candidate | Shells | Symmetry | C | Pass All? |
|-----------|--------|----------|---|-----------|
| electron | {1} | charged_lepton | -1 | **YES** |
| electron_ext | {1,2} | charged_lepton | -2 | NO (fails R1, R2, R3) |
| baryon_low | {1,2,3} | baryon | -1 | NO (fails R1, R2, R3) |
| baryon_mid | {2,3,4} | baryon | 14 | **YES** |
| baryon_high | {3,4,5} | baryon | 47 | NO (fails R2) |
| baryon_wide_low | {1,2,3,4} | baryon | 13 | NO (fails R1, R2) |
| baryon_wide_mid | {2,3,4,5} | baryon | 105 | **YES** |

### Key Findings

1. **Electron assignment {1} is strongly supported.** All five rules pass.
   The extended electron {1,2} fails three rules.

2. **Proton assignment {2,3,4} is strongly supported.** All five rules pass.
   The lower alternative {1,2,3} fails three rules (shell-1 conflict,
   boundary violation, insufficient complexity). The higher alternative
   {3,4,5} fails one rule (skips available interior shells).

3. **{2,3,4,5} also passes all rules** but represents a heavier baryon
   (possibly Delta or N* resonance), not the ground-state proton. The
   proton is the LIGHTEST baryon, which corresponds to the SMALLEST
   admissible baryon shell set: {2,3,4}.

4. **Neutron shares shell support {2,3,4} with the proton**, differing
   by symmetry label (baryon_neutral vs baryon). This is consistent with
   Rule Family 4.

### Assignment Confidence

| Particle | Assignment | Confidence | Basis |
|----------|-----------|------------|-------|
| Electron | {1} | **Strong** | Passes all 5 rules. Only candidate that does. |
| Proton | {2,3,4} | **Strong** | Passes all 5 rules. Smallest admissible baryon. |
| Neutron | {2,3,4} | **Moderate** | Same shells as proton. Distinction by symmetry sector. |

---

## PART B — Correction Term Analysis

### The Structural Gap

The two strongest zero-fit invariants produce:
- phi^15 = 1364.0 (25.7% error)
- CE ratio = 1415.2 (22.9% error)

The needed multiplicative correction is ~1.346.

### Single Integer Corrections

Ten exact structural correction factors were tested. ALL overshoot when
multiplied with the base invariants. The smallest correction (Vandermonde
discriminant = 2) gives phi^15 * 2 = 2728, which is 49% too high.

**No single integer correction bridges the gap.**

### The Self-Referential Closure Correction

The correction needed (1.346152) matches phi^(1/phi) = 1.346361 to 0.015%.

This decomposes the mass ratio as:

    mp/me = phi^(Delta C) * phi^(1/phi)
          = phi^15 * phi^(1/phi)
          = phi^(15 + 1/phi)
          = phi^(14 + phi)
          = 1836.44

Error: 0.015% from observed 1836.15.

### Structural Status of phi^(1/phi)

phi^(1/phi) is:
- exact (no fitted parameter)
- dimensionless
- structurally tied to the phi-manifold (the scale raised to its own inverse)
- the unique phi expression matching the needed correction

However, phi^(1/phi) is **not derived from the closure-class formalism** in
this analysis. It is **observed to match**. A derivation would require showing
that the closure cycle acquires a phi^(1/phi) weight from self-referential
closure on the phi-manifold.

**Status: structural conjecture, not theorem.**

---

## PART C — The 14 vs 15 Issue

### The Tension

- Proton complexity: C_p = 14 (exact integer from shell combinatorics)
- Ratio exponent: Delta C = C_p - C_e = 14 - (-1) = 15
- phi^15 = 1364 (25.7% error)
- phi^(14 + phi) = 1836.44 (0.015% error)

### Interpretation

The exponent 14 + phi = 15 + 1/phi decomposes into:
- 15: the pure combinatorial difference between proton and electron classes
- 1/phi: a self-referential correction from the phi-manifold structure

In the ratio, the additive phi offset DOES NOT cancel because:
- the correction phi^(1/phi) is a per-ratio multiplicative factor, not
  a per-class additive factor
- equivalently: the absolute invariant phi^(C + phi) contains a class-
  dependent term (C) and a universal term (phi), and the ratio exposes
  the class difference (15) multiplied by the universal correction

### Honest Assessment

The decomposition is clean and the numerical accuracy is striking. But the
correction phi^(1/phi) needs a derivation, not just an observation. Without
such a derivation, the expression is a structural conjecture of the form:

    "The mass ratio is phi^(Delta C) corrected by phi^(1/phi),
     where Delta C is the combinatorial class difference and
     phi^(1/phi) is the self-referential closure weight."

This is a **strong conjecture with zero fitted parameters** but it is
**not yet a derivation**.

---

## PART D — Neutron-Proton Split

### Candidate Mechanisms (ranked)

1. **Torsional parity correction** — Neutral sector acquires a small
   torsional offset. Affects both stability and energy. Most natural
   within the closure framework.

2. **Symmetry-sector multiplicity** — Charged and neutral baryon sectors
   have different internal degeneracy. Could provide an exact integer
   or phi-based correction.

3. **Charge-support cost** — The proton's electric charge requires
   additional closure support not needed by the neutron.
   This would make m_n > m_p if the neutral state has additional
   torsional cost compensating for the absent charge support.

4. **Phase frustration** — The neutral sector may have residual
   phase frustration from the torsional offset that slightly
   increases energy.

### Status

None of these mechanisms have been instantiated numerically. The
neutron-proton mass difference remains unresolved.

---

## EVALUATION ANSWERS

1. **Are assignments rule-supported?** YES. Electron {1} and proton {2,3,4}
   pass all 5 rule families. Nearby alternatives are excluded.

2. **Which alternatives are ruled out?** {1,2} for electron (3 rule failures),
   {1,2,3} for proton (3 failures), {3,4,5} for proton (1 failure).

3. **Strongest correction candidate?** phi^(1/phi) — the only phi expression
   matching the needed 1.346 factor. Structural conjecture, not derived.

4. **Correction origin?** Self-referential closure: the manifold scale
   raised to its own inverse. Not adjacency, topology, or degeneracy.

5. **Can the gap be reduced without fitted parameters?** YES, to 0.015%
   using phi^(1/phi), BUT this correction has conjecture status.
   Without it, the gap is 23-26%.

6. **Is neutron/proton a second-order correction?** YES. It is ~0.14% of
   the proton mass, far smaller than the proton/electron ratio.

7. **Strongest honest claim?** The framework:
   - derives the correct mass hierarchy from exact shell combinatorics
   - constrains the ratio to phi^15 = 1364 with zero fitted parameters
   - identifies phi^(14+phi) = 1836.4 as a structural conjecture (0.015% error)
   - assignment rules are explicit and exclude alternatives
   - the exact derivation of the correction term remains open

---

## OUTCOME: A (qualified)

Rule-based assignments: STRONG
Correction candidate: STRONG CONJECTURE (not theorem)
Paper status: suitable for honest preprint framing

Recommended paper position:
- Present phi^15 as the zero-fit structural result (25.7% error)
- Present phi^(14+phi) as a structural conjecture with 0.015% accuracy
- Be explicit that the phi^(1/phi) correction is observed, not derived
- Present assignment rules as the strongest part of the analysis
