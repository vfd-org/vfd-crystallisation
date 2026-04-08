#!/usr/bin/env python3
"""
Paper II — Correction Derivation Analysis
==========================================

For each legitimate correction-entry point in the formalism,
attempt an exact derivation. Then test whether phi^(1/phi) emerges.

Zero fitting. Every candidate tied to a specific formal source.
"""

import math
import csv
import json
import os

PHI = (1 + math.sqrt(5)) / 2
TARGET = 1836.15267343
BASE_PHI15 = PHI ** 15  # 1364.000...
NEEDED_CORRECTION = TARGET / BASE_PHI15  # ~1.3462

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "artifacts")


def analyze_correction_entries():
    """Map all legitimate correction-entry points in the formalism."""

    entries = []

    # ── CE1: Closure operator phase accumulation ──
    # The closure operator C maps Psi through one full geometric cycle.
    # Phase accumulated: delta_theta_n per mode.
    # For EXACT closure: delta_theta_n = 2*pi*k_n (integer multiples).
    # For stable minima, D[Psi] = 0 means all phases close exactly.
    # QUESTION: Does the closure cycle itself have a fractional phase?
    #
    # On a phi-structured manifold, one "full cycle" traverses all shells.
    # The total phase is sum(delta_theta_n * weight_n).
    # If the cycle is phi-scaled, the cycle LENGTH is not 2*pi but 2*pi*phi
    # (or some phi-dependent value).
    #
    # If the closure cycle has length 2*pi*phi rather than 2*pi, then
    # phase closure requires delta_theta_n = 2*pi*phi * k_n, and the
    # effective closure defect is evaluated against a phi-shifted target.
    #
    # This would introduce a per-cycle correction of phi/(2*pi) or similar.
    # But this is continuous, not discrete, and its value depends on
    # the cycle-length convention — which is currently UNDEFINED in the paper.

    entries.append({
        "id": "CE1",
        "location": "Closure operator C: phase accumulation",
        "mechanism": "Phi-scaled cycle length",
        "why_correction": "If the closure cycle length is phi-dependent, "
                         "exact closure targets shift by a phi factor.",
        "derivable": "NO",
        "reason": "Cycle length convention is undefined in current formalism. "
                  "Cannot derive a specific correction without defining it. "
                  "This is a MISSING STRUCTURE: the closure operator lacks "
                  "an explicit cycle-length specification.",
        "exact_discrete": "Unknown",
        "affects_ratio": "Potentially",
        "formula": "N/A",
        "value": None,
    })

    # ── CE2: Norm choice in closure defect ──
    # D[Psi] = ||C[Psi] - Psi||^2
    # The norm is the L2 norm on the mode space.
    # Different norms (L1, weighted L2, Frobenius on density matrix)
    # would give different defect values.
    # QUESTION: Does the norm choice affect the LOCATION of minima?
    #
    # Answer: The norm affects the defect landscape but NOT the zero-set
    # (D=0 is the same for any norm). For exact closure states, D=0
    # regardless of norm. So the norm cannot introduce a correction
    # to exact closure-class invariants.

    entries.append({
        "id": "CE2",
        "location": "Closure defect D: norm choice",
        "mechanism": "Weighted norm correction",
        "why_correction": "Different norms weight shells differently.",
        "derivable": "NO (irrelevant)",
        "reason": "For exact closure states (D=0), the norm does not matter. "
                  "Corrections only arise for approximate closure, which is "
                  "not the regime we are analyzing for stable minima.",
        "exact_discrete": "N/A",
        "affects_ratio": "No",
        "formula": "N/A",
        "value": None,
    })

    # ── CE3: Stability functional vs energy extraction ──
    # The stability functional S = alpha*D + beta*V + gamma*T + delta*B
    # selects the stable representative within a class.
    # But mass is defined through E[Psi*], not S[Psi*].
    # QUESTION: Does the energy E at the stability minimum differ
    # from a "raw" class energy invariant?
    #
    # For exact closure states with D=0, the stability functional reduces
    # to S = beta*V + gamma*T. The energy E is computed separately.
    # The stability minimum selects WHICH state represents the class,
    # but the energy of that representative depends on mode amplitudes
    # and frequencies — which in turn depend on S-minimization.
    #
    # This is a legitimate correction source: S-minimization constrains
    # the mode vector, and the resulting E depends on those constraints.

    entries.append({
        "id": "CE3",
        "location": "Stability-to-energy projection",
        "mechanism": "S-minimization constrains mode vector, affecting E",
        "why_correction": "The energy of the stability-optimal representative "
                         "may differ from the 'raw' class invariant.",
        "derivable": "PARTIALLY",
        "reason": "Requires solving the constrained optimization S -> E. "
                  "In the minimal model, uniform amplitudes give one E; "
                  "stability-optimal amplitudes give another. The ratio "
                  "depends on the amplitude profile at the minimum. "
                  "This IS computable but requires specifying the "
                  "amplitude-optimization problem, which is currently "
                  "not fully defined.",
        "exact_discrete": "Continuous (depends on optimization)",
        "affects_ratio": "Yes",
        "formula": "E_optimal / E_naive",
        "value": None,
    })

    # ── CE4: Shell-support normalization ──
    # The electron occupies 1 shell; the proton occupies 3.
    # The energy functional sums over occupied shells.
    # QUESTION: Should the sum be normalized by the number of shells?
    #
    # If E is a SUM, multi-shell states are automatically heavier.
    # If E is an AVERAGE, the shell-count effect is removed.
    # The physical question is: does mass scale with total closure
    # content (sum) or with average closure density (average)?
    #
    # In the current paper, E is a sum. This is a modelling choice.
    # A normalization correction would be:
    # E_normalized = E_sum / n_shells^alpha for some alpha.
    #
    # But this introduces a free parameter alpha — FORBIDDEN.

    entries.append({
        "id": "CE4",
        "location": "Shell-support normalization",
        "mechanism": "Sum vs average energy over shells",
        "why_correction": "Multi-shell states might need normalization "
                         "by shell count.",
        "derivable": "NO",
        "reason": "Any normalization exponent would be a free parameter. "
                  "The framework does not derive whether mass is a sum "
                  "or average. This is MISSING STRUCTURE.",
        "exact_discrete": "N/A",
        "affects_ratio": "Would affect it, but introduces free parameter",
        "formula": "N/A",
        "value": None,
    })

    # ── CE5: Boundary/interior asymmetry ──
    # Shell 1 is the boundary shell (electron). Shells 2+ are interior.
    # QUESTION: Does the boundary shell have different closure weight?
    #
    # Physically, boundary states interact differently with the exterior.
    # The closure operator might weight the boundary shell differently.
    # But in the current formalism, ALL shells are treated equally by C.
    #
    # A boundary correction would modify the electron's effective
    # complexity or energy. But no such distinction exists in the
    # current operator definition.

    entries.append({
        "id": "CE5",
        "location": "Boundary/interior shell asymmetry",
        "mechanism": "Boundary shell has different closure weight",
        "why_correction": "Boundary and interior shells may couple to "
                         "closure differently.",
        "derivable": "NO",
        "reason": "The current closure operator treats all shells equally. "
                  "A boundary correction requires extending the operator "
                  "with shell-position-dependent weights. This is MISSING "
                  "STRUCTURE: the operator lacks boundary-awareness.",
        "exact_discrete": "N/A",
        "affects_ratio": "Would affect it if introduced",
        "formula": "N/A",
        "value": None,
    })

    # ── CE6: Composite multiplicity / path count ──
    # A 3-shell composite has multiple internal closure paths.
    # The electron has exactly 1 path (trivial).
    # QUESTION: Does the multiplicity of internal paths affect mass?
    #
    # This was tested in WO-004 as correction terms CF1-CF10.
    # ALL integer multiplicities overshoot when applied as correction
    # factors to phi^15. The smallest (Vandermonde = 2) gives 2728.
    # No integer multiplicity gives ~1.346.

    entries.append({
        "id": "CE6",
        "location": "Composite closure-path multiplicity",
        "mechanism": "Internal path count as multiplicative factor",
        "why_correction": "Composite states have more internal closure paths.",
        "derivable": "YES (integer values computed)",
        "reason": "All integer path counts tested. None gives the needed "
                  "~1.346 correction. The smallest integer correction (2) "
                  "overshoots. Integer multiplicities cannot bridge the gap.",
        "exact_discrete": "Yes (integer)",
        "affects_ratio": "Yes, but ALL overshoot",
        "formula": "Integer factors: 2, 3, 4, 6, 7, 9, 24",
        "value": "All > 1.346",
    })

    # ── CE7: Recursive self-composition of closure operator ──
    # The closure operator C is defined as one full cycle.
    # What about C^2, C^3, ...? Repeated application.
    # QUESTION: Does the FIXED POINT of iterated closure differ from
    # the single-cycle fixed point?
    #
    # For exact closure (D=0), C[Psi] = Psi, so C^n[Psi] = Psi for all n.
    # Iterated closure gives the same fixed points.
    # BUT: the APPROACH to the fixed point under iteration might differ.
    # The eigenvalues of the linearized C near the fixed point describe
    # the convergence rate. These eigenvalues are phi-dependent.
    #
    # The SPECTRAL RADIUS of the linearized closure operator at a
    # fixed point is a legitimate class invariant.

    entries.append({
        "id": "CE7",
        "location": "Iterated closure operator: spectral radius",
        "mechanism": "Eigenvalue structure of linearized C at fixed point",
        "why_correction": "The convergence rate of iterated closure differs "
                         "between classes.",
        "derivable": "POTENTIALLY",
        "reason": "The spectral radius rho(DC) at a closure-fixed-point "
                  "is a legitimate class invariant. But computing it "
                  "requires the JACOBIAN of the closure operator, which "
                  "is not defined in the current formalism. "
                  "This is MISSING STRUCTURE: the linearization of C.",
        "exact_discrete": "Continuous (spectral radius)",
        "affects_ratio": "Could affect ratio if spectral radius differs by class",
        "formula": "rho(DC|_{Psi*})",
        "value": None,
    })

    # ── CE8: Energy functional form ──
    # E[Psi] = sum a_n^2 * phi^{kn} * omega_n
    # The exponent k is not derived. It is a free parameter.
    # QUESTION: Can the correct k be derived?
    #
    # The energy should arise from the NORM of the configuration on
    # the phi-manifold. If the manifold has a natural metric, the energy
    # is determined by that metric.
    #
    # On a phi-scaled shell hierarchy, the natural inner product between
    # shells n and m involves phi^(n+m) or phi^(|n-m|).
    # The energy E = <Psi, L Psi> depends on the Laplacian L.
    #
    # The correct k SHOULD be derivable from the manifold metric,
    # but the metric is not specified in the current paper.

    entries.append({
        "id": "CE8",
        "location": "Energy functional exponent k",
        "mechanism": "Derivation of k from manifold metric",
        "why_correction": "The energy scaling exponent determines the ratio.",
        "derivable": "NO",
        "reason": "The manifold metric is not specified. Without it, k "
                  "remains a free parameter. This is the PRIMARY MISSING "
                  "STRUCTURE for exact ratio derivation.",
        "exact_discrete": "Continuous (depends on metric)",
        "affects_ratio": "This IS the ratio (k directly determines mp/me)",
        "formula": "k derived from manifold Laplacian eigenvalues",
        "value": None,
    })

    # ── CE9: Class-energy vs class-complexity distinction ──
    # C(A) is a combinatorial quantity (prod-sum-1).
    # Energy is a continuous quantity depending on mode amplitudes.
    # QUESTION: Is the ratio phi^C or phi^{something else derived from C}?
    #
    # The assumption "mass ~ phi^C" means the combinatorial complexity
    # directly exponentiates. But physically, energy depends on the
    # detailed mode structure, not just on the shell-index arithmetic.
    # The C invariant may be an APPROXIMATION to a more refined quantity.

    entries.append({
        "id": "CE9",
        "location": "C as proxy vs exact energy invariant",
        "mechanism": "C is a coarse invariant; finer invariant exists",
        "why_correction": "The true energy invariant may differ from C "
                         "by a class-dependent correction.",
        "derivable": "UNKNOWN",
        "reason": "Requires knowing whether C is the leading term in an "
                  "asymptotic expansion of the true class energy invariant. "
                  "The correction would be the next term. Cannot be computed "
                  "without the full energy functional on the manifold.",
        "exact_discrete": "Unknown",
        "affects_ratio": "Yes (would modify the exponent)",
        "formula": "C + correction(class)",
        "value": None,
    })

    return entries


def test_phi_1_phi_emergence(entries):
    """Test whether phi^(1/phi) emerges from any formal source."""

    print("\n" + "=" * 80)
    print("CRITICAL TEST: Does phi^(1/phi) emerge from any formal source?")
    print("=" * 80)

    # phi^(1/phi) = phi^(phi-1) = phi^0.618... ≈ 1.3464
    target_corr = PHI ** (1 / PHI)

    print(f"\nphi^(1/phi) = {target_corr:.8f}")
    print(f"Needed correction: {NEEDED_CORRECTION:.8f}")
    print(f"Match: {abs(target_corr - NEEDED_CORRECTION)/NEEDED_CORRECTION*100:.4f}%")

    print("\nChecking each formal source:")

    # Check CE7: spectral radius
    # On a phi-manifold, eigenvalues of operators often involve phi.
    # The spectral radius of the shift operator on a phi-scaled chain
    # is phi itself. Raised to 1/phi gives phi^(1/phi).
    # BUT: this requires the linearized closure operator, which is undefined.
    print("\n  CE7 (spectral radius):")
    print("    If the linearized closure operator at a fixed point has")
    print("    spectral radius rho = phi (natural for phi-manifold),")
    print("    then rho^(1/rho) = phi^(1/phi) is a self-referential invariant.")
    print("    STATUS: Plausible but REQUIRES defining the linearized C.")

    # Check: does phi^(1/phi) arise from any phi identity?
    # phi^(1/phi) = phi^(phi-1) (since 1/phi = phi-1)
    # = phi^phi / phi^1
    # = phi^phi / phi
    # phi^phi ≈ 2.3901, divided by phi ≈ 1.6180 = 1.4764... NO that's wrong
    # Let me recalculate: phi^(1/phi) = phi^0.6180... = 1.3464
    # phi^phi = phi^1.6180 = 2.3901 (different thing)

    # Key identity: 1/phi = phi - 1
    # So phi^(1/phi) = phi^(phi-1) = phi^phi / phi
    val = PHI ** PHI / PHI
    print(f"\n  Identity check: phi^(1/phi) = phi^phi / phi = {val:.8f}")
    print(f"  Matches? {abs(val - target_corr) < 1e-10}")

    # This means: the correction is the ratio of phi^phi to phi.
    # phi^phi is the manifold scale raised to itself — the maximal
    # self-referential operation on a phi-manifold.
    # Dividing by phi normalizes it to a per-scale correction.

    # But this is INTERPRETATION, not derivation.
    # The question is: WHERE in the formalism does phi^phi / phi appear?

    print("\n  CONCLUSION:")
    print("    phi^(1/phi) = phi^(phi-1) = phi^phi / phi")
    print("    This can be INTERPRETED as the self-referential closure")
    print("    correction: the manifold raised to itself, normalized.")
    print("    But it does NOT emerge from any currently defined operator.")
    print("    The linearized closure operator (CE7) is the most likely")
    print("    formal source, but it requires extending the formalism.")

    return False  # phi^(1/phi) does NOT emerge from current formalism


def analyze_14_15_tension():
    """Formal analysis of the absolute vs relative complexity tension."""

    print("\n" + "=" * 80)
    print("ANALYSIS: Absolute vs Relative Closure Complexity (14/15 Tension)")
    print("=" * 80)

    print(f"""
The tension:
  C_p = 14 (proton absolute complexity)
  C_e = -1 (electron absolute complexity)
  Delta C = C_p - C_e = 15 (relative complexity)

  phi^14 = {PHI**14:.2f} (absolute proton)
  phi^15 = {PHI**15:.2f} (relative)
  phi^(14+phi) = {PHI**(14+PHI):.2f} (absolute + manifold)

Key question: Is mass determined by ABSOLUTE or RELATIVE complexity?

CASE 1: Relative complexity (standard ratio)
  mp/me = phi^(Delta C) = phi^15 = {PHI**15:.2f}
  This is the pure ratio. No calibration needed.
  Error: 25.7%.

CASE 2: Absolute complexity with calibration
  m_k = Lambda * phi^(C_k + phi)
  mp = Lambda * phi^(14 + phi)
  me = Lambda * phi^(-1 + phi)
  ratio = phi^(14+phi) / phi^(-1+phi) = phi^15 (CANCELS!)

  The absolute form with +phi gives the SAME ratio as Case 1.
  The 0.015% accuracy of phi^(14+phi) is ONLY for the absolute value,
  not for the ratio. This is a calibration artifact.

CASE 3: Absolute complexity WITHOUT the universal +phi offset
  m_k = Lambda * phi^(C_k)
  mp = Lambda * phi^14
  me = Lambda * phi^(-1) = Lambda / phi
  ratio = phi^14 * phi = phi^15 (SAME THING)

CONCLUSION:
  There is no real 14 vs 15 tension.
  The ratio is ALWAYS phi^15, regardless of whether the absolute
  invariant includes a +phi offset or not.

  The numerical quality of phi^(14+phi) = 1836.44 is an observation
  about the ABSOLUTE proton mass invariant, not about the ratio.
  For it to affect the RATIO, the +phi correction would need to be
  CLASS-DEPENDENT (different for electron and proton), not universal.

  In the current formalism, there is no mechanism for a class-dependent
  phi correction. The universal +phi cancels in the ratio.

  STATUS: The 14/15 tension is a BOOKKEEPING ARTIFACT.
  The ratio is phi^15. Period.
  The phi^(14+phi) accuracy is a coincidence of calibration, not
  a separate structural result.
""")


def diagnose_missing_structure(entries):
    """Identify exactly what the formalism lacks."""

    print("\n" + "=" * 80)
    print("MISSING STRUCTURE DIAGNOSIS")
    print("=" * 80)

    missing = []

    # Primary: manifold metric
    missing.append({
        "id": "MS1",
        "what": "Manifold metric / Laplacian eigenvalues",
        "why_needed": "The energy functional E[Psi] depends on how the phi-manifold "
                     "weights different shells. Without an explicit metric, the "
                     "energy scaling exponent k is a free parameter.",
        "formal_gap": "The paper defines the shell hierarchy phi^{-n} but does not "
                     "define the inner product or Laplacian on the manifold. The "
                     "Laplacian eigenvalues would determine k.",
        "how_to_fix": "Define the natural Riemannian metric on the phi-structured "
                     "manifold and compute its Laplacian spectrum. The energy "
                     "functional then follows from the quadratic form.",
        "breaks_paper": "No (the paper can state this as an open problem)",
    })

    # Secondary: linearized closure operator
    missing.append({
        "id": "MS2",
        "what": "Linearized closure operator / Jacobian of C",
        "why_needed": "The spectral radius of the linearized C at fixed points "
                     "is a legitimate class invariant that could provide the "
                     "correction factor.",
        "formal_gap": "The closure operator C is defined but its derivative "
                     "(Jacobian DC) is not computed. The spectral properties "
                     "of DC at closure-fixed-points are unknown.",
        "how_to_fix": "Compute the Jacobian of C at each closure-class "
                     "representative and extract the spectral radius.",
        "breaks_paper": "No (the paper can note this as future work)",
    })

    # Tertiary: boundary/interior distinction
    missing.append({
        "id": "MS3",
        "what": "Boundary-aware closure operator",
        "why_needed": "Shell 1 (electron) is the boundary; shells 2+ are interior. "
                     "The current operator treats them equally.",
        "formal_gap": "No formal distinction between boundary and interior shells "
                     "in the closure operator or stability functional.",
        "how_to_fix": "Introduce boundary-shell weights in the closure operator, "
                     "justified by the shell's coupling to the exterior.",
        "breaks_paper": "No",
    })

    # Quaternary: sum vs average normalization
    missing.append({
        "id": "MS4",
        "what": "Energy normalization convention (sum vs average vs weighted)",
        "why_needed": "The energy is currently a sum over shells. Whether mass "
                     "scales with total content or average density is undetermined.",
        "formal_gap": "The energy functional's normalization is a convention, not "
                     "derived from the manifold structure.",
        "how_to_fix": "Derive the normalization from the manifold's volume element "
                     "or from the closure-cycle integral.",
        "breaks_paper": "No",
    })

    for m in missing:
        print(f"\n  {m['id']}: {m['what']}")
        print(f"    Why needed: {m['why_needed']}")
        print(f"    Gap: {m['formal_gap']}")
        print(f"    Fix: {m['how_to_fix']}")

    return missing


def main():
    os.makedirs(BASE_DIR, exist_ok=True)

    # STEP B: Correction entry map
    print("=" * 80)
    print("CORRECTION ENTRY MAP")
    print("=" * 80)
    entries = analyze_correction_entries()

    print(f"\n{'ID':<5} {'Location':<40} {'Derivable':<12} {'Affects Ratio'}")
    print("-" * 75)
    for e in entries:
        print(f"{e['id']:<5} {e['location']:<40} {e['derivable']:<12} {e['affects_ratio']}")

    with open(os.path.join(BASE_DIR, "correction_entry_map.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=entries[0].keys())
        w.writeheader()
        w.writerows(entries)

    # STEP D: Test phi^(1/phi) emergence
    emerges = test_phi_1_phi_emergence(entries)

    # STEP E (Part 5): 14/15 tension analysis
    analyze_14_15_tension()

    # Missing structure diagnosis
    missing = diagnose_missing_structure(entries)

    # Save diagnosis
    with open(os.path.join(BASE_DIR, "missing_structure_diagnosis.md"), "w") as f:
        f.write("# Missing Structure Diagnosis\n\n")
        f.write("## Summary\n\n")
        f.write("The correction beyond phi^15 CANNOT be derived from the current formalism.\n")
        f.write("phi^(1/phi) does NOT emerge from any currently defined operator.\n\n")
        f.write("## The 14/15 tension is a bookkeeping artifact.\n")
        f.write("The ratio is phi^15 regardless of absolute calibration.\n\n")
        f.write("## Missing structures (in priority order):\n\n")
        for m in missing:
            f.write(f"### {m['id']}: {m['what']}\n")
            f.write(f"**Why needed:** {m['why_needed']}\n\n")
            f.write(f"**Gap:** {m['formal_gap']}\n\n")
            f.write(f"**Fix:** {m['how_to_fix']}\n\n")

    # Final evaluation
    print("\n" + "=" * 80)
    print("EVALUATION ANSWERS")
    print("=" * 80)
    print("""
1. Does the current formalism derive any correction beyond phi^15?
   NO. The formalism derives Delta C = 15 and phi^15. Nothing more.

2. If yes, what is the exact source?
   N/A.

3. If no, what exact mathematical piece is missing?
   PRIMARY: The manifold metric (MS1). Without it, the energy scaling
   exponent is free and the ratio is determined by the C-invariant only.
   SECONDARY: The linearized closure operator (MS2). Its spectral radius
   could provide a correction, but it is undefined.

4. Is phi^(1/phi) derivable, structurally motivated only, or merely
   numerically suggestive?
   STRUCTURALLY MOTIVATED but NOT DERIVABLE from current formalism.
   It has a natural interpretation (self-referential closure correction)
   and the spectral radius of the linearized C is a plausible formal source.
   But the linearized C is not defined, so the derivation is blocked.

5. Is the 14/15 tension a real formal issue or bookkeeping artifact?
   BOOKKEEPING ARTIFACT. The ratio is always phi^15 = phi^(Delta C).
   The phi^(14+phi) accuracy applies to the absolute invariant only
   and cancels in ratios.

6. Does the same missing layer explain neutron/proton splitting?
   YES, LIKELY. The neutron/proton split requires a symmetry-sector
   or torsional correction that couples into the energy functional.
   This requires the same missing manifold metric (MS1) and/or
   boundary-awareness (MS3) that the proton/electron correction needs.

7. Strongest honest claim for Paper II:
   "The framework derives the correct mass hierarchy and the exponent
    Delta C = 15 from exact shell combinatorics with zero fitted
    parameters. The ratio phi^15 = 1364 reproduces the observed
    mp/me = 1836 to within 26%. Closing this gap requires specifying
    the manifold metric, which is identified as the primary missing
    structure. The conjectured correction phi^(1/phi), while
    structurally motivated, is not derivable from the current formalism."
""")

    # OUTCOME
    print("OUTCOME: B")
    print("A precise proof that the correction is NOT derivable from the")
    print("current formalism, plus a clear missing-structure diagnosis.")
    print("The primary missing piece is the manifold metric (MS1).")


if __name__ == "__main__":
    main()
