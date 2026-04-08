#!/usr/bin/env python3
"""
Paper II — Minimal Deterministic Mass-Ratio Model
===================================================
Stage 1: Generate candidate bounded closure states.

Enumerates all admissible (shell_support, winding, symmetry) tuples,
assigns mode amplitudes and phases under each tested law family,
and outputs candidate_states.csv.

All computation is deterministic. No random initialisation.
"""

import csv
import json
import math
import os
from dataclasses import dataclass, asdict
from typing import List, Tuple

# ═══════════════════════════════════════════════════════════════
# Constants
# ═══════════════════════════════════════════════════════════════

PHI = (1 + math.sqrt(5)) / 2  # golden ratio ≈ 1.6180339887
MAX_SHELL = 5
WINDINGS = [1, 2, 3]
SYMMETRY_LABELS = ["charged_lepton", "baryon", "baryon_neutral"]

# Admissibility: max shells per symmetry class
MAX_SHELLS_BY_SYMMETRY = {
    "charged_lepton": 2,   # leptons are minimal
    "baryon": 5,           # baryons can be composite (full shell access)
    "baryon_neutral": 5,   # neutral baryons same composite capacity
}

# Winding compatibility: which windings allowed per symmetry
ALLOWED_WINDINGS = {
    "charged_lepton": [1],
    "baryon": [1, 2, 3],
    "baryon_neutral": [1, 2, 3],
}

# ═══════════════════════════════════════════════════════════════
# Frequency law families
# ═══════════════════════════════════════════════════════════════

def freq_linear(n: int, w: int) -> float:
    """omega_n = n (linear shell law)."""
    return float(n)

def freq_phi_scaled(n: int, w: int) -> float:
    """omega_n = phi^n (phi-scaled law)."""
    return PHI ** n

def freq_closure_corrected(n: int, w: int) -> float:
    """omega_n = phi^n * (1 + w/10) (closure-corrected law)."""
    return PHI ** n * (1 + w / 10.0)

FREQUENCY_LAWS = {
    "linear": freq_linear,
    "phi_scaled": freq_phi_scaled,
    "closure_corrected": freq_closure_corrected,
}

# ═══════════════════════════════════════════════════════════════
# Amplitude families
# ═══════════════════════════════════════════════════════════════

def amp_uniform(shells: List[int]) -> List[float]:
    """Uniform amplitudes on occupied shells."""
    return [1.0 / len(shells)] * len(shells)

def amp_phi_decaying(shells: List[int]) -> List[float]:
    """Phi-decaying amplitudes: a_n = phi^{-n}, normalised."""
    raw = [PHI ** (-n) for n in shells]
    total = sum(r ** 2 for r in raw) ** 0.5
    return [r / total for r in raw] if total > 0 else raw

def amp_closure_weight(shells: List[int]) -> List[float]:
    """Amplitudes weighted by 1/(n*phi^n), normalised."""
    raw = [1.0 / (n * PHI ** n) for n in shells]
    total = sum(r ** 2 for r in raw) ** 0.5
    return [r / total for r in raw] if total > 0 else raw

AMPLITUDE_LAWS = {
    "uniform": amp_uniform,
    "phi_decaying": amp_phi_decaying,
    "closure_weight": amp_closure_weight,
}

# ═══════════════════════════════════════════════════════════════
# Phase families
# ═══════════════════════════════════════════════════════════════

def phase_exact_closure(shells: List[int], symmetry: str) -> List[float]:
    """Exact closure-aligned: theta_n = 0 for all n."""
    return [0.0] * len(shells)

def phase_torsional_offset(shells: List[int], symmetry: str) -> List[float]:
    """Small torsional offset for neutral partners."""
    if symmetry == "baryon_neutral":
        return [0.01 * n for n in shells]
    return [0.0] * len(shells)

def phase_winding_parity(shells: List[int], symmetry: str) -> List[float]:
    """Phase by shell parity: 0 for even, pi/6 for odd."""
    return [0.0 if n % 2 == 0 else math.pi / 6 for n in shells]

PHASE_LAWS = {
    "exact_closure": phase_exact_closure,
    "torsional_offset": phase_torsional_offset,
    "winding_parity": phase_winding_parity,
}

# ═══════════════════════════════════════════════════════════════
# Candidate state
# ═══════════════════════════════════════════════════════════════

@dataclass
class CandidateState:
    state_id: str
    shells: str          # comma-separated shell indices
    winding: int
    symmetry: str
    freq_law: str
    amp_law: str
    phase_law: str
    amplitudes: str      # comma-separated
    phases: str          # comma-separated
    frequencies: str     # comma-separated
    n_shells: int

# ═══════════════════════════════════════════════════════════════
# Admissibility check
# ═══════════════════════════════════════════════════════════════

def is_admissible(shells: List[int], winding: int, symmetry: str) -> bool:
    """Check all admissibility predicates."""
    # 1. bounded support
    if not shells:
        return False
    # 2. allowed shell occupancy size
    if len(shells) > MAX_SHELLS_BY_SYMMETRY.get(symmetry, 0):
        return False
    # 3. winding-shell compatibility
    if winding not in ALLOWED_WINDINGS.get(symmetry, []):
        return False
    # 4. shell range
    if any(n < 1 or n > MAX_SHELL for n in shells):
        return False
    # 5. charged leptons must be minimal (1-2 shells, starting from 1)
    if symmetry == "charged_lepton" and shells[0] != 1:
        return False
    # 6. baryons must occupy at least 3 shells (composite bound states)
    if symmetry in ("baryon", "baryon_neutral") and len(shells) < 3:
        return False
    # 7. baryons must start at shell >= 2 (not minimal like leptons)
    if symmetry in ("baryon", "baryon_neutral") and shells[0] < 2:
        return False
    return True

# ═══════════════════════════════════════════════════════════════
# Generate all shell support configurations
# ═══════════════════════════════════════════════════════════════

def generate_shell_supports(max_shell: int, max_size: int) -> List[List[int]]:
    """Generate all contiguous shell supports from 1..max_shell with size 1..max_size."""
    supports = []
    for start in range(1, max_shell + 1):
        for size in range(1, max_size + 1):
            end = start + size - 1
            if end <= max_shell:
                supports.append(list(range(start, end + 1)))
    return supports

# ═══════════════════════════════════════════════════════════════
# Main generation
# ═══════════════════════════════════════════════════════════════

def generate_candidates() -> List[CandidateState]:
    candidates = []
    idx = 0

    for symmetry in SYMMETRY_LABELS:
        max_sz = MAX_SHELLS_BY_SYMMETRY[symmetry]
        all_supports = generate_shell_supports(MAX_SHELL, max_sz)

        for shells in all_supports:
            for winding in WINDINGS:
                if not is_admissible(shells, winding, symmetry):
                    continue

                for freq_name, freq_fn in FREQUENCY_LAWS.items():
                    for amp_name, amp_fn in AMPLITUDE_LAWS.items():
                        for phase_name, phase_fn in PHASE_LAWS.items():
                            amps = amp_fn(shells)
                            phases = phase_fn(shells, symmetry)
                            freqs = [freq_fn(n, winding) for n in shells]

                            state_id = f"S{idx:05d}"
                            candidates.append(CandidateState(
                                state_id=state_id,
                                shells=",".join(str(s) for s in shells),
                                winding=winding,
                                symmetry=symmetry,
                                freq_law=freq_name,
                                amp_law=amp_name,
                                phase_law=phase_name,
                                amplitudes=",".join(f"{a:.8f}" for a in amps),
                                phases=",".join(f"{p:.8f}" for p in phases),
                                frequencies=",".join(f"{f:.8f}" for f in freqs),
                                n_shells=len(shells),
                            ))
                            idx += 1

    return candidates


def main():
    candidates = generate_candidates()
    out_dir = os.path.join(os.path.dirname(__file__), "..", "artifacts")
    os.makedirs(out_dir, exist_ok=True)

    # Write CSV
    csv_path = os.path.join(out_dir, "candidate_states.csv")
    fields = [f.name for f in CandidateState.__dataclass_fields__.values()]
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for c in candidates:
            writer.writerow(asdict(c))

    # Summary
    sym_counts = {}
    for c in candidates:
        sym_counts[c.symmetry] = sym_counts.get(c.symmetry, 0) + 1

    summary = {
        "total_candidates": len(candidates),
        "by_symmetry": sym_counts,
        "frequency_laws": list(FREQUENCY_LAWS.keys()),
        "amplitude_laws": list(AMPLITUDE_LAWS.keys()),
        "phase_laws": list(PHASE_LAWS.keys()),
        "max_shell": MAX_SHELL,
        "windings": WINDINGS,
        "phi": PHI,
    }
    print(f"Generated {len(candidates)} candidate states")
    for k, v in sym_counts.items():
        print(f"  {k}: {v}")

    json_path = os.path.join(out_dir, "generation_summary.json")
    with open(json_path, "w") as f:
        json.dump(summary, f, indent=2)

    return candidates


if __name__ == "__main__":
    main()
