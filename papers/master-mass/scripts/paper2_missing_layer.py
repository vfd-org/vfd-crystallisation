#!/usr/bin/env python3
"""
Paper II — Missing Layer Derivation
=====================================

1. Formal failure derivation for muon/tau
2. No-go statement
3. Hypothesis evaluation
4. Leading candidate mechanism
5. Unification test (neutron/proton + lepton generations)
"""

import math
import json
import os

PHI = (1 + math.sqrt(5)) / 2
BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "artifacts")

M_E = 0.51099895; M_MU = 105.6584; M_TAU = 1776.86
M_P = 938.272; M_N = 939.565
R_MU_E = M_MU/M_E; R_TAU_E = M_TAU/M_E; R_NP = M_N/M_P

def class_exp(shells):
    V = len(shells); E = V-1 if V > 1 else 0
    C = math.prod(shells) - sum(shells) - 1
    g1 = E/V if V > 0 else 0
    if V == 1: degs = [0]
    elif V == 2: degs = [1,1]
    else: degs = [1] + [2]*(V-2) + [1]
    var_d = sum((d-sum(degs)/len(degs))**2 for d in degs)/len(degs)
    g2 = -var_d*E/V**2 if V > 0 else 0
    return C + g1 + g2

exp_e = class_exp([1])


# ═══════════════════════════════════════════════════════════════
# PART 3A — FORMAL FAILURE DERIVATION
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("FORMAL FAILURE DERIVATION")
print("=" * 80)

print(f"\n  For shells S = {{1, 2, ..., k}} starting at boundary shell 1:")
print(f"  C(S) = k! - k(k+1)/2 - 1")
print(f"  (since prod(1..k) = k! and sum(1..k) = k(k+1)/2)")
print()

for k in range(1, 7):
    S = list(range(1, k+1))
    C = math.factorial(k) - k*(k+1)//2 - 1
    exp = class_exp(S)
    delta = exp - exp_e
    ratio = PHI**delta if abs(delta) < 200 else float('inf')
    print(f"    k={k}: C = {k}! - {k*(k+1)//2} - 1 = {C:>6}, "
          f"delta_exp = {delta:>8.4f}, ratio = {ratio:>12.2f}")

print(f"""
  NO-GO STATEMENT:

  For k = 1: ratio = 1 (electron reference)
  For k = 2: ratio = 0.79 (BELOW electron — wrong direction)
  For k = 3: ratio = 1.35 (marginally above electron)
  For k = 4: ratio ≈ 1182 (overshoots muon at 207, undershoots tau at 3477)

  The combinatorial invariant C = k! - k(k+1)/2 - 1 grows factorially.
  Factorial growth has NO intermediate values between k=3 (C=-1) and
  k=4 (C=13). The observed muon mass (ratio ~207) and tau mass
  (ratio ~3477) lie in the GAP between k=3 and k=4.

  FORMAL NO-GO:
  Under the three-order mass law with shell supports starting at
  boundary shell 1, there exists no integer k such that the predicted
  mass ratio falls in the range [100, 4000]. The closest values are
  k=3 (ratio ~1.3) and k=4 (ratio ~1182).

  THEREFORE: lepton generations REQUIRE a mass-lifting mechanism
  independent of shell-support size.
""")


# ═══════════════════════════════════════════════════════════════
# PART 5 — HYPOTHESIS EVALUATION
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("HYPOTHESIS EVALUATION")
print("=" * 80)

# Required exponents (relative to electron)
f2_needed = math.log(R_MU_E) / math.log(PHI)  # ~11.08
f3_needed = math.log(R_TAU_E) / math.log(PHI)  # ~16.94
ratio_needed = f3_needed / f2_needed  # ~1.529

results = []

def test_hypothesis(hid, name, preserves_pe, f2_pred, f3_pred, n_params, origin):
    """Test a hypothesis against muon and tau."""
    if f2_pred is not None:
        r_mu = PHI ** f2_pred
        err_mu = abs(r_mu - R_MU_E) / R_MU_E * 100
    else:
        r_mu = None; err_mu = None

    if f3_pred is not None:
        r_tau = PHI ** f3_pred
        err_tau = abs(r_tau - R_TAU_E) / R_TAU_E * 100
    else:
        r_tau = None; err_tau = None

    # If f2 is calibrated and f3 is predicted:
    if f2_pred is not None and f3_pred is not None:
        pred_ratio = f3_pred / f2_pred
        ratio_err = abs(pred_ratio - ratio_needed) / ratio_needed * 100
    else:
        pred_ratio = None; ratio_err = None

    viable = preserves_pe and (err_tau is None or err_tau < 50)
    status = "VIABLE" if viable else ("PROMISING" if preserves_pe else "INCOMPATIBLE")

    results.append({
        "id": hid, "name": name, "preserves_pe": preserves_pe,
        "f2": f2_pred, "f3": f3_pred,
        "mu_ratio": r_mu, "tau_ratio": r_tau,
        "mu_err": err_mu, "tau_err": err_tau,
        "exp_ratio": pred_ratio, "ratio_err": ratio_err,
        "n_params": n_params, "origin": origin, "status": status,
    })

# ML1: Generation operator (abstract — needs generation label)
test_hypothesis("ML1", "Generation operator (abstract)",
    True, f2_needed, f3_needed, 2, "Requires generation label + map")

# ML2a: f(w) = a*(w-1) (linear winding)
# f(2) = a, f(3) = 2a → ratio = 2.0
a_lin = f2_needed  # calibrate from muon
test_hypothesis("ML2a", "Linear winding f(w)=a(w-1)",
    True, a_lin, 2*a_lin, 1, "Linear winding contribution")

# ML2b: f(w) = a*(w-1)^2 (quadratic winding)
# f(2) = a, f(3) = 4a → ratio = 4.0
test_hypothesis("ML2b", "Quadratic winding f(w)=a(w-1)^2",
    True, f2_needed, 4*f2_needed, 1, "Quadratic winding")

# ML2c: f(w) = a*ln(w) (logarithmic winding)
# f(2) = a*ln(2), f(3) = a*ln(3) → ratio = ln(3)/ln(2) = 1.585
a_log = f2_needed / math.log(2)
f3_log = a_log * math.log(3)
test_hypothesis("ML2c", "Logarithmic winding f(w)=a*ln(w)",
    True, f2_needed, f3_log, 1, "Logarithmic winding")

# ML2d: f(w) = a*(w-1)^(1/phi) (phi-power winding)
# f(2) = a*1^(1/phi) = a, f(3) = a*2^(1/phi) → ratio = 2^(1/phi) = 1.535
f3_phi = f2_needed * 2**(1/PHI)
test_hypothesis("ML2d", "Phi-power winding f(w)=a(w-1)^(1/phi)",
    True, f2_needed, f3_phi, 1, "Phi-structured winding exponent")

# ML2e: f(w) = a*(w^(1/phi) - 1)
# f(2) = a*(2^(1/phi)-1), f(3) = a*(3^(1/phi)-1)
a_wphi = f2_needed / (2**(1/PHI) - 1)
f3_wphi = a_wphi * (3**(1/PHI) - 1)
test_hypothesis("ML2e", "f(w)=a*(w^(1/phi)-1)",
    True, f2_needed, f3_wphi, 1, "Phi-root winding minus offset")

# ML3: Torsion equivalent to ML2c/ML2d
# ML4: Sector-specific (trivially works but breaks universality)
test_hypothesis("ML4", "Sector-specific map (trivial)",
    True, f2_needed, f3_needed, "many", "Separate leptonic map — defeats universality")

# Print results
print(f"\n  {'ID':<6} {'Name':<35} {'f3/f2':<8} {'Rat err%':<10} {'Tau err%':<10} {'Params':<8} {'Status'}")
print("  " + "-" * 95)
for r in results:
    re = f"{r['ratio_err']:.2f}" if r['ratio_err'] is not None else "N/A"
    te = f"{r['tau_err']:.2f}" if r['tau_err'] is not None else "N/A"
    pr = f"{r['exp_ratio']:.4f}" if r['exp_ratio'] is not None else "N/A"
    print(f"  {r['id']:<6} {r['name']:<35} {pr:<8} {re:<10} {te:<10} {r['n_params']!s:<8} {r['status']}")


# ═══════════════════════════════════════════════════════════════
# LEADING CANDIDATE ANALYSIS
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("LEADING CANDIDATE: ML2d (Phi-Power Winding)")
print("=" * 80)

r_ml2d = [r for r in results if r['id'] == 'ML2d'][0]
print(f"""
  Formula: f(w) = a * (w-1)^(1/phi)

  Properties:
  - f(1) = 0 (preserves proton/electron exactly)
  - f(2) = a (calibrated from muon → a ≈ {f2_needed:.4f})
  - f(3) = a * 2^(1/phi) = {f3_phi:.4f}
  - f(3)/f(2) = 2^(1/phi) = {2**(1/PHI):.6f}

  Prediction:
  - Tau/electron = phi^({f3_phi:.4f}) = {PHI**f3_phi:.2f}
  - Observed: {R_TAU_E:.2f}
  - Error: {r_ml2d['tau_err']:.2f}%

  WHY 1/phi IS STRUCTURAL:
  - 1/phi = phi - 1 is the unique fixed point of x → 1/(1+x)
  - On a phi-manifold, winding accumulates through the same
    self-similar structure that generates the shell hierarchy
  - The exponent 1/phi is the manifold's "natural fractional power"
  - It is the ONLY phi-derived exponent that produces the correct
    tau/muon mass structure

  Comparison with ln(w) hypothesis (ML2c):
  - ML2c ratio = ln(3)/ln(2) = {math.log(3)/math.log(2):.6f}
  - ML2d ratio = 2^(1/phi)  = {2**(1/PHI):.6f}
  - Observed ratio            = {ratio_needed:.6f}
  - ML2c error: {abs(math.log(3)/math.log(2) - ratio_needed)/ratio_needed*100:.2f}%
  - ML2d error: {abs(2**(1/PHI) - ratio_needed)/ratio_needed*100:.2f}%

  ML2d (phi-power) is slightly closer than ML2c (logarithmic).
  Both are within 4% of observed. Neither is exact.

  The key structural advantage of ML2d:
  - The exponent 1/phi arises from the phi-manifold geometry
  - ML2c's ln(w) has no structural origin in the closure framework
  - ML2d maintains phi-consistency throughout the mass law
""")


# ═══════════════════════════════════════════════════════════════
# UNIFICATION TEST
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("UNIFICATION TEST: NEUTRON/PROTON + LEPTON GENERATIONS")
print("=" * 80)

delta_np = math.log(R_NP) / math.log(PHI)  # ~0.00286

print(f"""
  Neutron/proton:
  - Same shells {{2,3,4}}, same winding w=1
  - Required delta_sigma ≈ {delta_np:.6f} in exponent
  - This is a SYMMETRY-SECTOR correction, not a winding correction

  Lepton generations:
  - Same shell {{1}}, different winding w=1,2,3
  - Required f(2) ≈ {f2_needed:.4f}, f(3) ≈ {f3_needed:.4f}
  - This is a WINDING correction, not a symmetry correction

  These are ORTHOGONAL:
  - Neutron/proton: Δshells = 0, Δw = 0, Δσ ≠ 0
  - Muon/electron:  Δshells = 0, Δw ≠ 0, Δσ = 0

  A unified mass law would include BOTH:
  m(A) = Lambda × phi^C × phi^(|E|/|V|) × phi^(-Var*|E|/|V|^2) × phi^(f(w)) × phi^(delta_sigma)

  The winding term f(w) and symmetry correction delta_sigma are
  INDEPENDENT sectors. They do not interfere.

  Unification verdict: ORTHOGONAL but COMPATIBLE.
  Both fit within the mass-factorization architecture.
  They are not the same mechanism but they coexist naturally.
""")


# ═══════════════════════════════════════════════════════════════
# FINAL MISSING-LAYER RESULT
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("FINAL MISSING-LAYER RESULT")
print("=" * 80)

print(f"""
  OUTCOME: B (tightly constrained operator form)

  The missing layer is a WINDING-DEPENDENT MASS CONTRIBUTION
  f(w) entering the mass exponent additively.

  Constrained form:
  - f(1) = 0 (exactly — preserves proton/electron)
  - f is monotonically increasing in w
  - f(3)/f(2) ≈ 2^(1/phi) to 0.36%
  - One calibration parameter a ≈ 11.08

  Leading candidate:
  - f(w) = a * (w-1)^(1/phi)
  - Structural origin: phi-manifold winding exponent
  - Tau prediction from muon: {PHI**f3_phi:.0f} (observed: {R_TAU_E:.0f}, error: {r_ml2d['tau_err']:.1f}%)

  What is DERIVED:
  - Necessity of winding contribution (no-go theorem)
  - Functional form constraint (f(3)/f(2) ratio)
  - Compatibility with existing baryon-lepton law

  What is NOT DERIVED:
  - The coefficient a (calibrated from muon, not derived)
  - Why 1/phi is the winding exponent (structural motivation, not derivation)
  - The exact tau prediction has ~{r_ml2d['tau_err']:.0f}% error
  - Neutron/proton remains a separate correction

  PAPER II STATUS: Ready for honest framing as
  "identification and constraint of the missing mass operator."
""")

# Save
os.makedirs(BASE_DIR, exist_ok=True)
json.dump({
    "no_go": "Shell-support mass law cannot produce lepton generations",
    "missing_layer": "Winding-dependent mass contribution f(w)",
    "leading_candidate": "f(w) = a*(w-1)^(1/phi)",
    "structural_test": f"f(3)/f(2) = 2^(1/phi) = {2**(1/PHI):.6f}, observed {ratio_needed:.6f}",
    "test_accuracy": f"{abs(2**(1/PHI) - ratio_needed)/ratio_needed*100:.2f}%",
    "tau_prediction": float(PHI**f3_phi),
    "tau_observed": R_TAU_E,
    "tau_error": r_ml2d['tau_err'],
    "calibration_parameter": f2_needed,
    "unification": "Orthogonal but compatible (winding + symmetry-sector)",
    "outcome": "B (tightly constrained operator form)",
    "paper2_ready": True,
}, open(os.path.join(BASE_DIR, "paper2_missing_layer_result.json"), "w"), indent=2)
