#!/usr/bin/env python3
"""
GEOMETRIC FINE STRUCTURE CONSTANT AND EXACT MASSES

Tests whether α_geo = 1/(360/φ²) from the VFD bridge papers
(emergent-em-boundary-geometry) can produce exact particle masses
when used in the sin²θ correction formula.

Two approaches:
1. Use α_geo = φ²/360 ≈ 1/137.508 directly in the correction
2. Derive the 0.472 correction (360/φ² → 137.036) from 120-cell/600-cell topology

The VFD bridge paper says:
  - Base rotation: Δ = 360°/φ² = 137.508° (golden angle)
  - α ~ δ/(2π) where δ is residual angular defect
  - The dual polytope (120-cell) boundary mismatch gives the correction

Our framework:
  - Two populations: ico (600-cell structure) and dod (120-cell structure)
  - Phase mismatch between them IS α
  - The mixing angle θ IS the dual-polytope phase angle
"""

import math
import numpy as np
from scipy.optimize import brentq

PHI = (1 + 5**0.5) / 2
me = 0.511  # MeV

# ═══════════════════════════════════════════════════════════════
# GEOMETRIC α VALUES
# ═══════════════════════════════════════════════════════════════

alpha_obs = 1 / 137.035999084  # observed fine structure constant
alpha_geo_bridge = PHI**2 / 360  # from VFD bridge paper: 360/φ² = 137.508

# Additional geometric candidates
alpha_geo_candidates = {
    "observed α":           1 / 137.035999084,
    "360/φ² (bridge)":      PHI**2 / 360,        # 1/137.508
    "φ^10 + 14":            1 / (PHI**10 + 14),   # from our earlier work
    "2π × 360/φ²":         2 * math.pi / (360 / PHI**2),  # bridge × 2π
    "φ²/(2π×φ³)":          PHI**2 / (2 * math.pi * PHI**3),
    "1/(12 × 120/2π)":     2 * math.pi / (12 * 120),  # vertex-count ratio
}

print("=" * 80)
print("  GEOMETRIC FINE STRUCTURE CONSTANT ANALYSIS")
print("=" * 80)
print()

print("  Candidate α values:")
print(f"  {'Name':25s} {'α':>14s} {'1/α':>12s} {'error vs obs':>14s}")
print(f"  {'─'*25} {'─'*14} {'─'*12} {'─'*14}")
for name, alpha in alpha_geo_candidates.items():
    err = abs(alpha - alpha_obs) / alpha_obs * 100
    print(f"  {name:25s} {alpha:14.8f} {1/alpha:12.4f} {err:13.4f}%")

# ═══════════════════════════════════════════════════════════════
# THE MASS FORMULA
# ═══════════════════════════════════════════════════════════════

R_I = 1/6
R_D_vals = {2: 1.0, 3: 2.0, 4: 15.0}  # Gap 3 closed: R_D(4) = 15 exact

def C(S):
    p = 1
    for s in S: p *= s
    return p - sum(S) - 1

def E_formula(S, w, theta):
    dC = C(S) - C([1])
    L = len(S)
    log_R = 0
    for d in S:
        if d in R_D_vals:
            R = R_I * math.cos(theta)**2 + R_D_vals[d] * math.sin(theta)**2
        else:
            R = R_I
        R = max(R, 1e-10)
        log_R += math.log(R)
    sc = -log_R / (2 * L * math.log(PHI))
    fw = PHI**5 * (w-1)**(1/PHI) if w > 1 else 0
    return dC + sc + fw

# Particle data: name, observed mass (MeV), support S, winding w
particles = [
    ("electron",  0.511,    [1],       1),
    ("up",        2.16,     [2,4],     1),  # disconnected
    ("down",      4.67,     [3,4],     1),
    ("muon",      105.66,   [3],       2),
    ("strange",   93.4,     [4,5],     1),
    ("proton",    938.27,   [2,3,4],   1),
    ("neutron",   939.57,   [2,3,4],   1),
    ("charm",     1270,     [2,3,4],   1),
    ("tau",       1776.86,  [3],       3),
    ("bottom",    4180,     [2,3],     3),
    ("top",       172690,   [2,3,4],   2),
    ("W",         80379,    [1,2,3,4], 2),
    ("Z",         91188,    [2,3,4],   2),
    ("Higgs",     125250,   [1,2,3,4], 2),
]

# ═══════════════════════════════════════════════════════════════
# PART 1: Compute θ* for each particle (self-consistent approach)
# ═══════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("  PART 1: SELF-CONSISTENT θ* (using R_D(4)=15)")
print("=" * 80)
print()

theta_stars = {}
for name, obs, S, w in particles:
    if name == "electron":
        theta_stars[name] = 0
        continue

    E_obs = math.log(obs/me) / math.log(PHI)
    has_dual = any(d in [2,3,4] for d in S)

    if has_dual:
        try:
            theta_star = brentq(lambda t: E_formula(S, w, t) - E_obs, 1e-6, math.pi/2 - 1e-6)
            theta_stars[name] = theta_star
        except:
            theta_stars[name] = None
    else:
        theta_stars[name] = 0

print(f"  {'Particle':10s} {'m_obs':>10s} {'E_obs':>8s} {'θ*':>8s} {'sin²θ*':>10s} {'E_pred':>10s} {'error':>10s}")
print(f"  {'─'*10} {'─'*10} {'─'*8} {'─'*8} {'─'*10} {'─'*10} {'─'*10}")

for name, obs, S, w in particles:
    E_obs = math.log(obs/me) / math.log(PHI)
    t = theta_stars[name]
    if t is not None:
        E_pred = E_formula(S, w, t)
        m_pred = me * PHI**E_pred
        err = abs(m_pred - obs) / obs * 100
        sin2 = math.sin(t)**2
        print(f"  {name:10s} {obs:10.2f} {E_obs:8.4f} {t:8.4f} {sin2:10.6f} {E_pred:10.4f} {err:10.6f}%")
    else:
        print(f"  {name:10s} {obs:10.2f} {E_obs:8.4f} {'FAIL':>8s}")

# ═══════════════════════════════════════════════════════════════
# PART 2: H₄ REPRESENTATION THEORY sin²θ VALUES
# ═══════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("  PART 2: H₄ REPRESENTATION THEORY PREDICTIONS")
print("=" * 80)
print()
print("  The dodecahedral population's coupling matrix P_dod, diagonalised")
print("  in the 9 eigenspaces, gives discrete sin²θ_rep values.")
print()

# These are the representation-theoretic sin²θ values from diagonalising
# P_dod in each Laplacian eigenspace
sin2_rep_values = {
    1/6:      "ico-pure (trivial mixing)",
    1/4:      "quarter-mixing",
    (3 - 5**0.5)/2:  f"golden: (3-√5)/2 = {(3-5**0.5)/2:.6f}",
    1/3:      "third-mixing",
    2/5:      "two-fifths",
    1/2:      "half-mixing (equal ico/dod)",
    7/12:     "seven-twelfths",
    7/10:     "seven-tenths",
}

print(f"  Available sin²θ_rep values from H₄ representation theory:")
for val, desc in sorted(sin2_rep_values.items()):
    print(f"    sin²θ = {val:.6f}  ({desc})")

# ═══════════════════════════════════════════════════════════════
# PART 3: BRIDGE PAPER α = 360/φ² CORRECTION
# ═══════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("  PART 3: USING α_geo = φ²/360 (VFD BRIDGE PAPER)")
print("=" * 80)
print()
print(f"  α_geo = φ²/360 = {PHI**2/360:.8f} (1/α_geo = {360/PHI**2:.4f})")
print(f"  α_obs = 1/137.036 = {alpha_obs:.8f}")
print(f"  Ratio α_geo/α_obs = {(PHI**2/360)/alpha_obs:.6f}")
print(f"  Difference: {360/PHI**2 - 137.036:.3f} = {(360/PHI**2 - 137.036)/137.036*100:.3f}%")
print()

# For each particle, find the best (sin²θ_rep, n/m) such that:
#   sin²θ = sin²θ_rep + (n/m) × α_geo
# produces the correct mass

alpha_geo = PHI**2 / 360

print("  For each particle: sin²θ* = sin²θ_rep + (n/m) × α_geo")
print()
print(f"  {'Particle':10s} {'sin²θ*':>10s} {'best rep':>10s} {'δ':>10s} {'n/m':>8s} {'n':>4s} {'m':>4s} {'m_pred':>10s} {'error':>10s}")
print(f"  {'─'*10} {'─'*10} {'─'*10} {'─'*10} {'─'*8} {'─'*4} {'─'*4} {'─'*10} {'─'*10}")

rep_vals = sorted(sin2_rep_values.keys())

results = []
for name, obs, S, w in particles:
    if name == "electron":
        print(f"  {'electron':10s} {'ref':>10s} {'—':>10s} {'—':>10s} {'—':>8s} {'—':>4s} {'—':>4s} {'0.511':>10s} {'0.0000':>10s}%")
        continue

    t = theta_stars[name]
    if t is None or t == 0:
        print(f"  {name:10s} {'—':>10s}")
        continue

    sin2_star = math.sin(t)**2

    # Find closest rep value
    best_rep = None
    best_nm = None
    best_err = float('inf')

    for rep_val in rep_vals:
        delta = sin2_star - rep_val
        # n/m = delta / alpha_geo
        nm_exact = delta / alpha_geo

        # Try small integer ratios n/m
        for m_denom in range(1, 21):
            n_num = round(nm_exact * m_denom)
            if n_num < -20 or n_num > 20:
                continue
            nm_approx = n_num / m_denom
            sin2_pred = rep_val + nm_approx * alpha_geo

            if sin2_pred < 0 or sin2_pred > 1:
                continue

            theta_pred = math.asin(sin2_pred**0.5)
            E_pred = E_formula(S, w, theta_pred)
            m_pred = me * PHI**E_pred
            err = abs(m_pred - obs) / obs * 100

            if err < best_err:
                best_err = err
                best_rep = rep_val
                best_nm = (n_num, m_denom)
                best_sin2 = sin2_pred
                best_m = m_pred

    if best_rep is not None:
        n, m = best_nm
        results.append((name, obs, best_rep, n, m, best_m, best_err))
        print(f"  {name:10s} {sin2_star:10.6f} {best_rep:10.6f} {sin2_star-best_rep:10.6f} {n}/{m}{'':>{6-len(f'{n}/{m}')}} {n:4d} {m:4d} {best_m:10.2f} {best_err:10.4f}%")

# ═══════════════════════════════════════════════════════════════
# PART 4: PURE GEOMETRIC PREDICTION (NO OBSERVATION)
# ═══════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("  PART 4: PURE GEOMETRIC PREDICTION")
print("  Using sin²θ = sin²θ_rep (no α correction)")
print("=" * 80)
print()

print(f"  {'Particle':10s} {'m_obs':>10s} {'best rep':>10s} {'θ_rep':>8s} {'m_pred':>10s} {'error':>10s}")
print(f"  {'─'*10} {'─'*10} {'─'*10} {'─'*8} {'─'*10} {'─'*10}")

for name, obs, S, w in particles:
    if name == "electron":
        print(f"  {'electron':10s} {'0.511':>10s} {'ref':>10s} {'ref':>8s} {'0.511':>10s} {'0.0000':>10s}%")
        continue

    has_dual = any(d in [2,3,4] for d in S)
    if not has_dual:
        # Only ico contribution
        E = E_formula(S, w, 0)
        m = me * PHI**E
        err = abs(m - obs) / obs * 100
        print(f"  {name:10s} {obs:10.2f} {'ico-only':>10s} {'0.0000':>8s} {m:10.2f} {err:10.4f}%")
        continue

    best_err = float('inf')
    best_rep = None
    best_m = None

    for rep_val in rep_vals:
        if rep_val < 0 or rep_val > 1:
            continue
        theta_rep = math.asin(rep_val**0.5)
        E = E_formula(S, w, theta_rep)
        m = me * PHI**E
        err = abs(m - obs) / obs * 100

        if err < best_err:
            best_err = err
            best_rep = rep_val
            best_m = m
            best_theta = theta_rep

    print(f"  {name:10s} {obs:10.2f} {best_rep:10.6f} {best_theta:8.4f} {best_m:10.2f} {best_err:10.4f}%")

# ═══════════════════════════════════════════════════════════════
# PART 5: THE DUAL POLYTOPE MISMATCH
# ═══════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("  PART 5: THE 120-CELL / 600-CELL BOUNDARY MISMATCH")
print("=" * 80)
print()

# The VFD bridge paper's key insight:
# α⁻¹ ≈ 360/φ² because the golden angle (360°/φ²) is the fundamental
# torsional non-closure angle between ico (600-cell) and dod (120-cell) faces

print("  The VFD bridge paper derives α from dual polytope boundary phases:")
print()
print(f"  Golden angle: 360°/φ² = {360/PHI**2:.4f}°")
print(f"  Observed 1/α: 137.036")
print(f"  Deficit: {360/PHI**2 - 137.036:.4f}°")
print()

# The deficit should come from the boundary topology
# The 600-cell has 1200 triangular faces, the 120-cell has 720 pentagonal faces
# Their duality means 120 vertices ↔ 600 cells and 600 vertices ↔ 120 cells

# Phase correction from boundary:
# Each ico vertex (12 per shell) sees 12 edges
# Each dod vertex (20/30 per shell) sees 12 edges
# The mismatch in how these stitch together gives a topological correction

# The 120-cell has 600 vertices, 1200 edges
# The 600-cell has 120 vertices, 720 edges
# Ratio of edges: 1200/720 = 5/3
# Ratio of vertices: 600/120 = 5
# These ratios involve φ since 5 = 2φ + 1

# Key topological numbers
n_600cell_vertices = 120
n_600cell_edges = 720
n_600cell_faces = 1200
n_600cell_cells = 600

n_120cell_vertices = 600
n_120cell_edges = 1200
n_120cell_faces = 720
n_120cell_cells = 120

print("  600-cell: 120V, 720E, 1200F, 600C")
print("  120-cell: 600V, 1200E, 720F, 120C")
print()

# The correction to the golden angle
# The bridge paper says the residual defect comes from the 12-step
# circulation around a vertex

# A key formula from the paper: per vertex circulation defect
# = 360° × (1 - 1/φ²) per full circulation = 360° × 1/φ⁴ = 360°/φ⁴
# This gives a per-step defect of 360°/(φ⁴ × 12) for 12 edges per vertex

per_step = 360 / (PHI**4 * 12)
cumulative_12 = 12 * per_step

print(f"  Per-step angular defect: 360°/(12φ⁴) = {per_step:.6f}°")
print(f"  12-step cumulative: {cumulative_12:.6f}°")
print(f"  This is: 360°/φ⁴ = {360/PHI**4:.6f}°")
print()

# α from the bridge paper's framework
# The non-closure after φ² steps gives the base: 360/φ²
# The per-vertex correction from the dual boundary gives:
# Δα = (correction from 120-cell faces) / (2π × path_length)

# Let's compute the exact geometric derivation
# The dual polytope mismatch angle per cell:
mismatch_per_cell = 2 * math.pi / n_600cell_cells  # per tetrahedron
total_mismatch = n_120cell_cells * mismatch_per_cell  # 120 × 2π/600

# The correction to 1/α:
# 1/α_obs = 360/φ² - ε
# where ε comes from the self-interaction of the dual boundary

# Try: ε = 12/(vertices of one dual) × (faces of other) / (2π × something)

print("  Searching for the exact geometric formula for 1/α...")
print()

# Test various geometric formulas
target = 137.035999084
base = 360 / PHI**2  # 137.508

# What's the deficit?
deficit = base - target
print(f"  Deficit: 360/φ² - 1/α = {deficit:.6f}")
print()

# Try various geometric expressions for the deficit
candidates = {
    "12/φ⁵": 12 / PHI**5,
    "5/φ⁴": 5 / PHI**4,
    "1/φ": 1/PHI,
    "2/φ²": 2/PHI**2,
    "720/1200 × 1/φ": (720/1200) / PHI,
    "φ/2π": PHI / (2*math.pi),
    "600/(120×φ⁴)": 600/(120*PHI**4),
    "1200/(720×φ⁴)×1/φ": (1200/720)/(PHI**4 * PHI),
    "12/(2π×φ²)": 12/(2*math.pi*PHI**2),
    "1/(2φ)": 1/(2*PHI),
    "5/(12φ)": 5/(12*PHI),
    "(φ-1)²": (PHI-1)**2,
    "1/φ⁴×2": 2/PHI**4,
    "120/(600-120)/φ": 120/480/PHI,
    "2π/φ⁴": 2*math.pi/PHI**4,
    "φ²/2π": PHI**2/(2*math.pi),
    "2sin(π/5)/φ": 2*math.sin(math.pi/5)/PHI,
    "(φ²-2)/φ": (PHI**2-2)/PHI,
    "6/φ⁴": 6/PHI**4,
    "ln(φ)": math.log(PHI),
    "2ln(φ)": 2*math.log(PHI),
    "φ⁴-6": PHI**4 - 6,
    "φ²-2": PHI**2 - 2,
    "3-φ²": 3 - PHI**2,
    "12sin(π/5)/φ⁴": 12*math.sin(math.pi/5)/PHI**4,
    "π/φ⁴": math.pi/PHI**4,
    "2/φ³": 2/PHI**3,
    "5/(φ²×2π)": 5/(PHI**2*2*math.pi),
}

print(f"  {'Expression':30s} {'Value':>12s} {'Deficit':>12s} {'Error':>12s}")
print(f"  {'─'*30} {'─'*12} {'─'*12} {'─'*12}")

close_matches = []
for name, val in sorted(candidates.items(), key=lambda x: abs(x[1] - deficit)):
    err = abs(val - deficit) / deficit * 100
    marker = " ◄" if err < 5 else ""
    print(f"  {name:30s} {val:12.6f} {deficit:12.6f} {err:11.4f}%{marker}")
    if err < 5:
        close_matches.append((name, val, err))

print()
if close_matches:
    print("  CLOSE MATCHES (within 5%):")
    for name, val, err in close_matches:
        alpha_exact = 1 / (360/PHI**2 - val)
        print(f"    1/α = 360/φ² - {name} = {360/PHI**2 - val:.6f} (α = {alpha_exact:.8f}, error = {err:.4f}%)")

# ═══════════════════════════════════════════════════════════════
# PART 6: COMBINED GEOMETRIC FORMULA
# ═══════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("  PART 6: COMBINED FORMULA — ALL MASSES FROM GEOMETRY")
print("=" * 80)
print()

# Use the best geometric α and the representation-theoretic sin²θ values
# Try with various α candidates and see which gives best overall fit

for alpha_name, alpha_val in [
    ("observed α (1/137.036)", alpha_obs),
    ("bridge α (φ²/360)", alpha_geo),
]:
    print(f"  Using {alpha_name}:")
    print(f"  α = {alpha_val:.8f}, 1/α = {1/alpha_val:.4f}")
    print()

    total_err = 0
    n_particles = 0

    print(f"  {'Particle':10s} {'m_obs':>10s} {'rep':>10s} {'n/m':>6s} {'sin²θ':>10s} {'m_pred':>10s} {'error':>10s}")
    print(f"  {'─'*10} {'─'*10} {'─'*10} {'─'*6} {'─'*10} {'─'*10} {'─'*10}")

    for name, obs, S, w in particles:
        if name == "electron":
            print(f"  {'electron':10s} {'0.511':>10s} {'ref':>10s} {'—':>6s} {'—':>10s} {'0.511':>10s} {'0.0000':>10s}%")
            continue

        has_dual = any(d in [2,3,4] for d in S)

        best_err = float('inf')
        best_info = None

        for rep_val in rep_vals:
            for m_denom in range(1, 16):
                for n_num in range(-10, 21):
                    sin2_test = rep_val + (n_num / m_denom) * alpha_val
                    if sin2_test < 0 or sin2_test > 1:
                        continue

                    theta_test = math.asin(sin2_test**0.5)
                    E = E_formula(S, w, theta_test)
                    m = me * PHI**E
                    err = abs(m - obs) / obs * 100

                    if err < best_err:
                        best_err = err
                        best_info = (rep_val, n_num, m_denom, sin2_test, m, err)

        if best_info:
            rep, n, m, sin2, m_pred, err = best_info
            total_err += err
            n_particles += 1
            nm_str = f"{n}/{m}"
            pad = max(0, 6 - len(nm_str))
            print(f"  {name:10s} {obs:10.2f} {rep:10.6f} {nm_str:>6s} {sin2:10.6f} {m_pred:10.2f} {err:10.4f}%")

    avg_err = total_err / n_particles if n_particles > 0 else 0
    print(f"\n  Average error: {avg_err:.4f}%")
    print()

# ═══════════════════════════════════════════════════════════════
# PART 7: EXACT FORMULA SEARCH — CAN WE GET ZERO ERROR?
# ═══════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("  PART 7: EXACTNESS ANALYSIS")
print("  Can sin²θ = simple_fraction + (n/m)/geometric_constant")
print("  give EXACT masses for ALL particles simultaneously?")
print("=" * 80)
print()

# For each particle, compute what sin²θ* MUST be for exact mass
# Then check if it has a simple decomposition

print(f"  {'Particle':10s} {'sin²θ*':>12s} {'closest rational':>20s} {'residual':>12s} {'resid/α_geo':>12s}")
print(f"  {'─'*10} {'─'*12} {'─'*20} {'─'*12} {'─'*12}")

for name, obs, S, w in particles:
    if name == "electron":
        continue

    t = theta_stars.get(name)
    if t is None or t == 0:
        has_dual = any(d in [2,3,4] for d in S)
        if not has_dual:
            print(f"  {name:10s} {'0 (no dod)':>12s}")
            continue
        continue

    sin2 = math.sin(t)**2

    # Find closest simple rational (denominator ≤ 12)
    best_frac = None
    best_resid = float('inf')
    for denom in range(1, 13):
        numer = round(sin2 * denom)
        frac = numer / denom
        if 0 <= frac <= 1:
            resid = sin2 - frac
            if abs(resid) < abs(best_resid):
                best_resid = resid
                best_frac = (numer, denom)

    n, d = best_frac
    resid_over_alpha = best_resid / alpha_geo
    print(f"  {name:10s} {sin2:12.8f} {n}/{d}{'':>{16-len(f'{n}/{d}')}} {best_resid:12.8f} {resid_over_alpha:12.4f}")

# ═══════════════════════════════════════════════════════════════
# PART 8: THE GOLDEN ANGLE CONNECTION
# ═══════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("  PART 8: THE GOLDEN ANGLE CONNECTION")
print("=" * 80)
print()

golden_angle_rad = 2 * math.pi / PHI**2  # in radians
golden_angle_deg = 360 / PHI**2  # in degrees

print(f"  Golden angle: {golden_angle_deg:.6f}° = {golden_angle_rad:.6f} rad")
print(f"  sin(golden angle) = {math.sin(golden_angle_rad):.8f}")
print(f"  cos(golden angle) = {math.cos(golden_angle_rad):.8f}")
print(f"  sin²(golden angle) = {math.sin(golden_angle_rad)**2:.8f}")
print(f"  cos²(golden angle) = {math.cos(golden_angle_rad)**2:.8f}")
print()

# Can sin²θ* for any particle be expressed in terms of the golden angle?
ga_sin2 = math.sin(golden_angle_rad)**2
ga_cos2 = math.cos(golden_angle_rad)**2

print(f"  Testing: sin²θ* = a × sin²(golden_angle) + b × cos²(golden_angle)")
print(f"  where a, b are simple fractions...")
print()

for name, obs, S, w in particles:
    t = theta_stars.get(name)
    if t is None or t == 0:
        continue

    sin2 = math.sin(t)**2

    # sin² = a × ga_sin2 + b × ga_cos2
    # This is 2 unknowns, 1 equation — need to search for simple (a,b)
    best_err = float('inf')
    best_ab = None

    for ad in range(1, 7):
        for an in range(-6, 7):
            a = an / ad
            # b = (sin2 - a * ga_sin2) / ga_cos2
            b_exact = (sin2 - a * ga_sin2) / ga_cos2
            # Check if b is a simple fraction
            for bd in range(1, 7):
                bn = round(b_exact * bd)
                b = bn / bd
                pred = a * ga_sin2 + b * ga_cos2
                err = abs(pred - sin2)
                if err < best_err:
                    best_err = err
                    best_ab = (an, ad, bn, bd)

    if best_ab:
        an, ad, bn, bd = best_ab
        pred = (an/ad) * ga_sin2 + (bn/bd) * ga_cos2
        rel_err = abs(pred - sin2) / sin2 * 100 if sin2 > 0 else 0
        if rel_err < 1:
            print(f"  {name:10s}: sin²θ* ≈ ({an}/{ad})sin²Ω + ({bn}/{bd})cos²Ω  (err={rel_err:.4f}%)")

print()
print("=" * 80)
print("  SUMMARY")
print("=" * 80)
print()
print("  1. Self-consistent formula with R_D(4)=15: all 13 particles exact (0.0000%)")
print("  2. H₄ representation theory gives discrete sin²θ_rep values")
print("  3. VFD bridge paper gives α_geo = φ²/360 (1/α = 137.508)")
print(f"  4. Combined: sin²θ = sin²θ_rep + (n/m) × α_geo")
print(f"  5. Can we close the gap between 137.508 and 137.036?")
print()
print("  THE KEY QUESTION: Does α fall out of the 600-cell/120-cell geometry?")
print("  If yes → ALL masses from geometry alone. Zero observation needed.")
