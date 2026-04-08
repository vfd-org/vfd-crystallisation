#!/usr/bin/env python3
"""
Paper III — Spectral Dimension and Coefficient Derivation Analysis
===================================================================

Tests whether d_s = phi and a = phi^5 can be derived from
the present closure framework, or must remain postulated.

Zero fitting. Adversarial to own claims.
"""

import math
import numpy as np
import json
import os

PHI = (1 + math.sqrt(5)) / 2
BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "artifacts")
os.makedirs(BASE_DIR, exist_ok=True)

# ═══════════════════════════════════════════════════════════════
# PART 3 — SPECTRAL DIMENSION DERIVATION ATTEMPTS
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("SPECTRAL DIMENSION DERIVATION ATTEMPTS")
print("=" * 80)

sd_routes = []

def add_sd(rid, name, mechanism, result, yields_phi, status, reason):
    sd_routes.append({
        "id": rid, "name": name, "mechanism": mechanism,
        "result": result, "yields_phi": yields_phi,
        "status": status, "reason": reason,
    })

# SD1: Graph-Laplacian spectral dimension
print("\n  SD1: GRAPH-LAPLACIAN SPECTRAL DIMENSION")
print("    For a finite path graph P_k, the spectral dimension is")
print("    computed from the heat kernel K(t) = sum exp(-lambda_i * t).")
print("    The spectral dimension d_s is defined by:")
print("    K(t) ~ t^{-d_s/2} for small t.")
print()

# For P_k, eigenvalues are lambda_j = 2 - 2*cos(pi*j/k) for j=0,...,k-1
# For P_3: lambda = {0, 1, 3}
# Heat kernel: K(t) = 1 + exp(-t) + exp(-3t)
# For small t: K(t) ≈ 3 - 4t + ... so K(t)/K(0) = 1 - (4/3)t
# This gives d_s/2 from -d(ln K)/d(ln t) as t -> 0
# For finite graphs, d_s is not well-defined in the usual sense.

# For infinite path (Z lattice): d_s = 1 (well-known)
print("    For infinite path graph (Z lattice): d_s = 1.")
print("    For finite P_k: d_s not well-defined (no scaling regime).")
print("    The graph Laplacian of path graphs gives d_s = 1, not phi.")

add_sd("SD1", "Graph-Laplacian spectral dimension",
    "Heat kernel scaling on path graphs",
    "d_s = 1 for infinite path", False, "NOT DERIVABLE",
    "Standard graph spectral dimension of path/line is 1, not phi.")

# SD2: Shell-manifold Laplacian
print("\n  SD2: SHELL-MANIFOLD LAPLACIAN")
print("    Shells at r_n = r_0 * phi^{-n}.")
print("    The 1D radial operator on this grid:")
print("    -d^2f/dr^2 discretized on phi-spaced points.")
print()

# On a phi-spaced grid, the spacing decreases geometrically.
# The eigenvalue density of the discrete Laplacian on such a grid
# depends on the metric weight.
# For uniform weight: d_s = 1 (it's still a 1D chain).
# For phi-weighted measure: the spectral dimension could differ.

# The spectral dimension from the Laplacian with weight w(n) = phi^{2n}:
# The weighted Laplacian is L_{ij} = w_i * (standard L)_{ij}
# Its spectrum scales differently from the unweighted case.
# But the spectral dimension is still defined by heat kernel scaling.

# For a 1D chain with geometrically varying weights, the spectral
# dimension is known to be 1 unless the chain has fractal structure.
# A phi-spaced chain is NOT fractal — it's a monotone sequence.

print("    A phi-spaced 1D chain has spectral dimension 1.")
print("    Geometric spacing changes eigenvalue MAGNITUDES but not")
print("    the spectral DIMENSION (still a 1D chain).")

add_sd("SD2", "Shell-manifold Laplacian",
    "1D Laplacian on phi-spaced grid",
    "d_s = 1", False, "NOT DERIVABLE",
    "1D manifold has d_s = 1 regardless of spacing.")

# SD3: Self-similar/fractal dimension
print("\n  SD3: SELF-SIMILAR / FRACTAL DIMENSION")
print("    Hausdorff dimension of a phi-scaled nesting:")
print("    If scaling ratio = phi and branching = 1:")
print("    d_H = log(1)/log(phi) = 0. Not useful.")
print("    If scaling ratio = phi and branching = phi:")
print("    d_H = log(phi)/log(phi) = 1.")
print("    If scaling ratio = phi and branching = phi^2:")
print("    d_H = log(phi^2)/log(phi) = 2.")
print()
print("    To get d_H = phi, need branching b satisfying:")
print("    log(b)/log(phi) = phi")
print("    b = phi^phi ≈ 2.390")
print("    This is NOT a natural integer or phi-rational branching.")

add_sd("SD3", "Self-similar/fractal dimension",
    "Hausdorff dimension from scaling + branching",
    "d_H = phi only if branching = phi^phi ≈ 2.39", False, "NOT DERIVABLE",
    "No natural branching ratio gives d_H = phi.")

# SD4: Boundary excitation effective dimension
print("\n  SD4: BOUNDARY EXCITATION EFFECTIVE DIMENSION")
print("    The boundary shell (n=1) has excitation modes.")
print("    If the boundary is a phi-scaled 'disk' with area ~ phi^{-2},")
print("    the mode density scales differently from the bulk.")
print("    BUT: the boundary is a single shell, not a continuum.")
print("    A single-shell boundary has zero internal dimension.")
print("    Excitation 'dimension' only makes sense if the boundary")
print("    has internal structure (modes, angular decomposition, etc.)")
print()
print("    In the current framework, the boundary shell has NO")
print("    specified internal structure. It is a single discrete point.")

add_sd("SD4", "Boundary excitation effective dimension",
    "Internal mode structure of boundary shell",
    "Undefined (no internal structure specified)", False, "NOT DERIVABLE",
    "Boundary shell has no specified internal structure.")

# SD5: Closure recursion effective dimension
print("\n  SD5: CLOSURE RECURSION EFFECTIVE DIMENSION")
print("    Ask: does the closure recursion induce an effective")
print("    spectral exponent d/(d+1) = 1/phi without d = phi?")
print()
print("    The identity 1/phi = phi/(phi+1) is exact.")
print("    So d/(d+1) = 1/phi implies d = phi.")
print("    There is no way to get exponent 1/phi from d/(d+1)")
print("    WITHOUT d = phi. The identity is rigid.")
print()
print("    But: can the closure recursion DEFINE an effective d?")
print("    If the recursion has a self-similar structure with")
print("    effective branching phi at each level, the return")
print("    probability after w steps scales as w^{-d_s/2}.")
print("    For this to give d_s = phi, the return probability")
print("    must scale as w^{-phi/2}.")
print()
print("    On a 1D chain, return probability ~ w^{-1/2} (d_s=1).")
print("    On a phi-structured recursion... we need to define it.")

# Actually check: if the closure graph is NOT a simple path but
# a RECURSIVE phi-tree structure, the spectral dimension could be phi.
# The Sierpinski gasket has d_s = 2*log(3)/log(5) ≈ 1.365.
# A phi-branching recursive structure would have:
# d_s = 2*log(phi)/log(phi+2) ≈ 2*0.481/1.283 = 0.750 — not phi.
# Or: d_s = 2*log(phi)/log(phi^2+1) ≈ 0.643 — closer but not phi.

# Check: is there ANY standard fractal/recursive structure with d_s = phi?
# The answer from the literature: not commonly known.
# phi ≈ 1.618 would require a specific recursive structure.

print("    No standard recursive structure is known to have d_s = phi.")
print("    The phi-branching tree gives d_s ≈ 0.75, not 1.618.")

add_sd("SD5", "Closure recursion effective dimension",
    "Return probability on phi-recursive structure",
    "No standard structure gives d_s = phi", False, "NOT DERIVABLE",
    "No known recursive structure has spectral dimension phi.")


# ═══════════════════════════════════════════════════════════════
# SPECTRAL DIMENSION CONCLUSION
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("SPECTRAL DIMENSION: CONCLUSION")
print("=" * 80)
print(f"""
  ALL FIVE ROUTES FAIL TO DERIVE d_s = phi.

  SD1 (graph Laplacian): d_s = 1
  SD2 (shell Laplacian): d_s = 1
  SD3 (fractal dimension): d_H = phi only with non-natural branching
  SD4 (boundary modes): undefined without internal structure
  SD5 (closure recursion): no standard structure gives d_s = phi

  EXACT CONCLUSION: d_s = phi is NOT DERIVABLE from the present formalism.

  The identity phi/(phi+1) = 1/phi is mathematically exact, but the
  claim "d_s = phi" requires a specific manifold/operator structure
  that is not present in the current framework. The phi-shell manifold
  is 1-dimensional (a chain of shells), and its spectral dimension is 1.

  MISSING STRUCTURE:
  To derive d_s = phi, the framework would need either:
  1. A phi-branching recursive manifold structure (not currently defined)
  2. Internal boundary modes giving a phi-dimensional mode space
  3. A weighted spectral measure that effectively raises d_s from 1 to phi

  None of these exist in the present framework.

  STATUS: d_s = phi must remain a MODELLING ASSUMPTION.
  The exponent 1/phi is structurally motivated (by the exact identity
  and the phi-manifold context) but not derived.
""")


# ═══════════════════════════════════════════════════════════════
# PART 5 — COEFFICIENT a = phi^5 DERIVATION ATTEMPTS
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("COEFFICIENT a = phi^5 DERIVATION ATTEMPTS")
print("=" * 80)

coeff_routes = []

def add_coeff(rid, name, mechanism, result, yields_phi5, status, reason):
    coeff_routes.append({
        "id": rid, "name": name, "mechanism": mechanism,
        "result": result, "yields_phi5": yields_phi5,
        "status": status, "reason": reason,
    })

# C1: Shell depth
print("\n  C1: SHELL DEPTH DERIVATION")
print("    The manifold has N=5 shells.")
print("    a = phi^N = phi^5.")
print("    Is N=5 derived or postulated?")
print()
print("    N=5 is the number of shells in the current model.")
print("    It is a MODEL PARAMETER, not derived from any deeper principle.")
print("    Changing N would change phi^N.")
print("    The model does not derive why N=5 is the correct shell count.")

add_coeff("C1", "Shell depth",
    "a = phi^N with N = model shell count",
    "Gives phi^5 if N=5 is assumed", True, "STRUCTURALLY SELECTED",
    "N=5 is a model parameter, not derived.")

# C2: Boundary normalization
print("\n  C2: BOUNDARY NORMALIZATION")
print("    The boundary shell has spectral weight lambda(1) = phi^2.")
print("    The total manifold spectral weight is sum phi^{2n} for n=1..5.")
total_weight = sum(PHI**(2*n) for n in range(1, 6))
print(f"    Total: {total_weight:.4f}")
print(f"    phi^5 = {PHI**5:.4f}")
print(f"    Ratio: {total_weight/PHI**5:.4f}")
print("    No simple ratio of manifold weights gives phi^5.")

add_coeff("C2", "Boundary normalization",
    "Ratio of manifold spectral weights",
    f"Total weight = {total_weight:.2f}, not simply related to phi^5", False,
    "NOT DERIVABLE", "No natural spectral-weight ratio gives phi^5.")

# C3: Operator norm
print("\n  C3: OPERATOR NORM")
print("    If the winding operator has a natural norm...")
print("    The Laplacian of P_5 has eigenvalues that can be computed.")
L5 = np.zeros((5,5))
for i in range(5):
    L5[i,i] = (1 if i==0 else 2 if i<4 else 1)
    if i > 0: L5[i,i-1] = -1
    if i < 4: L5[i,i+1] = -1
eigs5 = np.sort(np.linalg.eigvalsh(L5))
print(f"    P_5 Laplacian eigenvalues: {np.round(eigs5, 4)}")
print(f"    Spectral radius: {max(abs(eigs5)):.4f}")
print(f"    Trace: {np.trace(L5):.1f}")
print(f"    phi^5 = {PHI**5:.4f}")
print(f"    No eigenvalue or simple spectral quantity equals phi^5.")

add_coeff("C3", "Operator norm",
    "Spectral properties of P_5 Laplacian",
    "No eigenvalue/trace equals phi^5", False, "NOT DERIVABLE",
    "P_5 Laplacian spectral properties don't produce phi^5.")

# C4: Recursion count
print("\n  C4: RECURSION COUNT")
print("    5 = number of shells.")
print("    Also: 5 = F(5) (5th Fibonacci number).")
print(f"    phi^(F(5)) = phi^5 = {PHI**5:.4f}")
print("    But F(5) = 5 is a coincidence of small Fibonacci numbers.")
print("    This is numerological, not structural.")

add_coeff("C4", "Recursion count",
    "N as Fibonacci number or recursion depth",
    "F(5) = 5 is a coincidence at small n", False, "NOT DERIVABLE",
    "Numerological coincidence, not structural.")

# C5: Uniqueness in phi^k
print("\n  C5: UNIQUENESS IN phi^k FAMILY")
needed_a = math.log(206.768) / math.log(PHI)
for k in range(3, 8):
    val = PHI**k
    err = abs(val - needed_a) / needed_a * 100
    unique = "*" if err < 1 else ""
    print(f"    phi^{k} = {val:.4f}, error from needed ({needed_a:.4f}): {err:.2f}% {unique}")

add_coeff("C5", "Uniqueness in phi^k",
    "phi^5 is uniquely closest to needed a",
    "phi^5 within 0.1%; phi^4 at 38%, phi^6 at 62%", True,
    "STRUCTURALLY SELECTED",
    "Unique within phi^k but uniqueness is numerical, not derived.")

# C6: Cross-link to Paper I
print("\n  C6: CROSS-LINK TO PAPER I")
print("    Does 5 appear elsewhere in the architecture?")
print("    - Shell count: N = 5 (model parameter)")
print("    - Max proton shell: n = 4 (not 5)")
print("    - Number of assignment rules: 5 (R1-R5)")
print("    - Delta C = 15 = 3 × 5")
print("    - Proton shell product: 24 (not related to 5)")
print()
print("    The number 5 appears as shell count and rule count.")
print("    But the rule count is a coincidence — rules could be")
print("    reformulated as 4 or 6 rules with different grouping.")
print("    Only the shell count N=5 is structurally meaningful.")

add_coeff("C6", "Cross-link to Paper I",
    "Occurrence of 5 in the framework",
    "5 = shell count (meaningful), 5 = rule count (coincidence)", True,
    "STRUCTURALLY SELECTED",
    "N=5 as shell count is the only meaningful link.")


# ═══════════════════════════════════════════════════════════════
# COEFFICIENT CONCLUSION
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("COEFFICIENT: CONCLUSION")
print("=" * 80)
print(f"""
  a = phi^5 is STRUCTURALLY SELECTED but NOT DERIVED.

  The selection is based on:
  - N = 5 is the model's shell count (a model parameter)
  - phi^5 is uniquely privileged within phi^k (0.1% match vs 38%+ for neighbors)
  - The interpretation "boundary excitation scale = manifold depth" is plausible

  But:
  - N = 5 is not derived from deeper principles
  - The same framework with N = 6 would give phi^6 (wrong)
  - No operator, norm, or spectral property produces phi^5 independently

  STATUS: a = phi^5 remains STRUCTURALLY SELECTED.

  MISSING STRUCTURE:
  A derivation would require either:
  1. Proving that the manifold must have exactly 5 shells
  2. Deriving a from the boundary Laplacian or closure operator
  3. Finding an operator-algebraic reason for a = phi^N specifically
""")


# ═══════════════════════════════════════════════════════════════
# FINAL CLAIM-STATUS MATRIX
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("FINAL CLAIM-STATUS MATRIX")
print("=" * 80)

status_matrix = {
    "Exponent identity phi/(phi+1) = 1/phi": "Mathematically exact",
    "Spectral dimension d_s = phi": "NOT DERIVABLE from present formalism (must be postulated)",
    "Exponent 1/phi in f(w)": "Conditionally derived (exact IF d_s = phi)",
    "Coefficient a = phi^5": "Structurally selected (unique in phi^k; N=5 is model parameter)",
    "Full winding operator f(w)": "Constrained (form motivated, not derived)",
    "Unified mass law": "Structurally compatible (factorisation extended)",
}

for item, status in status_matrix.items():
    print(f"  {item}")
    print(f"    → {status}")
    print()


# ═══════════════════════════════════════════════════════════════
# EVALUATION ANSWERS
# ═══════════════════════════════════════════════════════════════

print("=" * 80)
print("EVALUATION ANSWERS")
print("=" * 80)
print(f"""
  Q1: Can d_s = phi be derived?
      NO. All five derivation routes fail. The phi-shell manifold is
      1-dimensional (d_s = 1). To get d_s = phi would require a
      phi-branching recursive structure or internal boundary modes,
      neither of which exists in the present framework.

  Q2: Can a = phi^5 be derived?
      NO. It is structurally selected (unique in phi^k, matched to shell
      count N=5) but N=5 is a model parameter, not derived. No operator
      or spectral property produces phi^5 independently.

  Q3: What exact missing structure prevents derivation?
      For d_s: a recursive manifold structure with effective spectral
      dimension phi, or internal boundary mode space. Currently absent.
      For a: a principle fixing the manifold shell count N, or an
      operator whose norm equals phi^N. Currently absent.

  PUBLICATION RECOMMENDATION:
      Papers I + II should be released NOW.
      Paper III documents the derivation-status results honestly.
      It should be released alongside or shortly after, as a
      "derivation status and missing structure" paper.

      Paper II's claims are already correctly calibrated:
      - "conditionally derived" for the exponent
      - "structurally motivated" for the coefficient
      Paper III confirms these labels are accurate and specifies
      exactly what would be needed to upgrade them.
""")

# Save
json.dump({
    "spectral_dimension": {
        "target": "phi",
        "routes_tested": len(sd_routes),
        "routes_yielding_phi": sum(1 for r in sd_routes if r["yields_phi"]),
        "conclusion": "NOT DERIVABLE from present formalism",
        "missing_structure": "Recursive manifold with d_s = phi, or internal boundary modes",
    },
    "coefficient": {
        "target": "phi^5",
        "routes_tested": len(coeff_routes),
        "routes_yielding_phi5": sum(1 for r in coeff_routes if r["yields_phi5"]),
        "conclusion": "STRUCTURALLY SELECTED but not derived",
        "missing_structure": "Principle fixing N=5, or operator with norm phi^N",
    },
    "overall_outcome": "Honest negative: neither derivable from present formalism",
    "paper_II_labels_correct": True,
    "publication_recommendation": "Release I+II now; III as derivation-status companion",
}, open(os.path.join(BASE_DIR, "paper3_result.json"), "w"), indent=2)
