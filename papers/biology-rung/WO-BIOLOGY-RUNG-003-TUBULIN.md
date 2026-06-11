# WO-BIOLOGY-RUNG-003-TUBULIN: Microtubule C₁₃ Symmetry and Taxane Binding

**Status:** Stub — opens after WO-2, explicitly stretch
**Date opened:** 2026-04-23
**Classification:** Biology-rung + cancer chemotherapy prediction
**Priority:** Stretch — highest disease-leverage but most speculative

---

## 1. Executive Summary

Microtubules are 13-protofilament tubes. Taxanes (paclitaxel,
docetaxel — front-line cancer chemotherapy) stabilise microtubules
by binding at a specific site on β-tubulin, disrupting mitotic
spindle dynamics. The 13-fold symmetry ties into the cascade through
`papers/cascade-derivation/cascade-photon-microtubule-alpha-programme.md`
which notes a C₁₃ irrep match.

**Prediction this WO aims at:** the binding-pocket geometry that
makes a taxane therapeutically effective can be read from the C₁₃
irrep structure of the protofilament lattice + the icosahedral
closure constraints on axial transport. Could suggest why certain
binding pockets are privileged (therapeutic) vs. others
(non-therapeutic or resistant).

This is the most speculative of the three WOs. It depends on both
WO-1 (closure machinery) and WO-2 (helical orbits). It is explicitly
a stretch goal — a hit would be a significant result for cancer
pharmacology; a miss costs us only the research effort spent
trying.

---

## 2. Goals

### 2.1 Geometric predictions (must)

1. **Derive** the C₁₃ irrep structure of the protofilament lattice
   from cascade closure, importing the C₁₃ claim in
   `cascade-photon-microtubule-alpha-programme.md` and re-proving it
   with the WO-1 catalogue conventions.
2. **Predict** the symmetry of taxane binding-pocket geometry on
   β-tubulin: which symmetry orbits admit a stable binding pocket
   versus which are forbidden.
3. **Predict** protofilament pitch / dimer spacing from the cascade
   φ-helical orbit machinery (shared with WO-2).

### 2.2 Molecular-biology empirical comparison (must, per programme scope)

4. **Fetch** relevant tubulin / microtubule PDB structures (the PDB
   REST API is public; candidate tubulin entries including
   tubulin-taxane complexes are well-catalogued under e.g. tubulin /
   paclitaxel / docetaxel keywords). Emit observed pocket geometry
   and dimer-spacing measurements to
   `data/wo3_tubulin_observed.csv`.
5. **Compare** predicted symmetry / pitch against observed. Emit
   `data/wo3_comparison.md` with hit / partial / miss per prediction
   and any clean falsifications.
6. **Cryo-EM cross-check** for dimer spacing / pitch where available
   (EMDB entries for microtubule maps).

### 2.3 Cancer-pharmacology handle (stretch)

7. **Identify** which of several taxane-binding-site variants
   (paclitaxel vs. docetaxel vs. cabazitaxel vs. known resistant
   tubulin mutants) the cascade predicts are therapeutically
   privileged. A hit is a significant pharmacology result; a miss
   costs only the research time spent.
8. **Report** whether the cascade predicts specific β-tubulin
   mutations (e.g. clinically-observed βIII isotype upregulation in
   taxane-resistant tumours) as being geometrically incompatible with
   the cascade's C₁₃ pocket geometry.

### 2.4 Non-goals

- Full kinetic model of microtubule polymerisation/depolymerisation.
- Novel drug design (we predict binding-pocket symmetry, not new
  molecules).
- Non-microtubule tubulin forms (e.g. tubulin in centrioles with
  different geometry) — out of scope.

---

## 3. Dependencies

- WO-1 complete (closure-operator machinery, catalogue convention,
  `μ` / chirality infrastructure)
- WO-2 complete (φ-helical orbit enumeration infrastructure shared
  with protofilament-pitch prediction)
- `cascade-photon-microtubule-alpha-programme.md` reviewed for its
  existing C₁₃ claims
- Access to PDB and EMDB public APIs (or curated literature CSVs
  populated from primary structural-biology publications, matching
  the WO-1 VIPERdb-fetch pattern)

---

## 4. Status Log

- 2026-04-23: WO opened as stub. Not yet active.
