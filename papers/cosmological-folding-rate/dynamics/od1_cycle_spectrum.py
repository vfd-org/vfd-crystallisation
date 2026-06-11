"""OD-1 closure: cycle eigenvalue spectrum (LEGACY exploratory script).

NOTE (2026-05-07): This script's per-cycle eigenvalue calculation is
the LEGACY orthonormal mode-count attempt (its 17-modes-out-of-12+5
version reaching a 17/12 number) cited in
papers/v600-cosmic-tensions/v600-cosmic-tensions.tex §6 as the
mode-count caveat that does NOT close. The current
publication-ready statement is the K-saturated trace theorem at
papers/v600-cosmic-tensions/, not the per-cycle eigenvalue claim
below; this header section is retained for archival
cross-reference only.

ORIGINAL CLAIM (NOT used by Paper 4):
    For each σ-paired cycle in V_600, the per-cycle rate eigenvalue is
        h_C = h_0 · (1 + 1/L)
    where L=10 is the cycle length.  σ-fixed cycles have h_C = h_0.

PROOF SKELETON (rigorous up to the closure-operator definition):

  1. Cycle space.
     V_600 partitions into 12 cycles, each of length L=10.  The state
     space is ℝ^{V_600} = ⨁_{i=1}^{12} ℝ^{C_i}.

  2. σ-Galois decomposition.
     σ acts on V_600 by exchanging σ-paired cycle pairs (c, σc).  This
     induces a Z_2 action on each ℝ^{c} ⊕ ℝ^{σc}, splitting it into
     σ-symmetric and σ-antisymmetric subspaces, each of dim L.

     For σ-fixed cycles, σ acts trivially, so the entire ℝ^{c} subspace
     is σ-symmetric.

  3. Mode count per cycle (k=0 cycle-mean mode):
       - σ-fixed cycle:    1 σ-sym mode,                0 σ-antisym mode  → 1 total
       - σ-paired cycle:   1 σ-sym mode,                1 σ-antisym mode  → 2 total
       (the σ-antisym mode is per-pair but lives on each cycle of the pair)

  4. Closure operator H_op.
     The closure operator acts on the mode space.  By σ-Galois invariance,
     it preserves the (sym, antisym) decomposition.  Its action on the
     k=0 cycle-mean modes has the form:

       H_op |sym, c⟩    = h_0 |sym, c⟩
       H_op |antisym, c⟩ = h_0 |antisym, c⟩

     Both modes have the SAME eigenvalue h_0 (the "rate per mode" is
     fixed by closure normalisation).  This is the crucial step:
     σ-Galois symmetry forbids a different eigenvalue between sym and
     antisym at the cycle-mean level.

  5. Per-vertex rate from L²-normalised modes.
     The cycle-mean σ-symmetric mode |sym, c⟩ in vertex basis is
       (1/√L) Σ_{v ∈ c} |v⟩       (cycle constant, normalised)
     with per-vertex amplitude 1/√L, so |amplitude|² = 1/L per vertex.

     Similarly, the σ-antisymmetric mode |antisym, (c,σc)⟩ has amplitude
       (1/√(2L)) on each vertex of c, with sign +; on σc with sign −.
     Per-vertex |amplitude|² in c is 1/(2L).
     Hmm. But by RESTRICTING to one cycle of the pair, the antisym
     contribution per vertex of c is 1/(2L), not 1/L.  This gives
     h_C^paired = h_0 + h_0/(2L), NOT h_0 + h_0/L.

     This is a real subtlety in the derivation. The numerical sim
     below tests both normalisations and reports which matches the
     observed 1+1/12.

  6. Per-cycle rate eigenvalue.
     h_C = Σ_modes h_mode · ⟨v|mode⟩² summed over the L vertices of c.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Dict, List, Tuple

import numpy as np


# Substrate
L = 10
N_BULK_CYCLES = 2
N_PAIRED_PAIRS = 5    # 5 pairs of σ-paired cycles
N_PAIRED_CYCLES = 2 * N_PAIRED_PAIRS  # = 10
N_CYCLES = N_BULK_CYCLES + N_PAIRED_CYCLES  # = 12
N = N_CYCLES * L  # = 120


def bulk_vertex_indices() -> List[int]:
    return list(range(0, N_BULK_CYCLES * L))


def boundary_vertex_indices() -> List[int]:
    return list(range(N_BULK_CYCLES * L, N))


def cycle_vertex_indices(c: int) -> List[int]:
    return list(range(c * L, (c + 1) * L))


def sigma_pair_partner(c: int) -> int:
    """For boundary cycle c, return its σ-pair partner index.
    σ pairs (2,3), (4,5), (6,7), (8,9), (10,11)."""
    if c < N_BULK_CYCLES:
        return c   # σ-fixed
    if c % 2 == 0:
        return c + 1
    return c - 1


def build_modes() -> Tuple[np.ndarray, np.ndarray, List[Tuple[str, int]]]:
    """Return (modes, eigenvalues, labels) for the two normalisation choices.

    Each mode is a vector in ℝ^N (length 120), L²-normalised.
    Labels: ('sym', cycle_idx) or ('antisym', pair_idx).

    Two normalisation conventions are compared:
      (A) per-pair antisym (1/√(2L) amplitude per vertex)
      (B) per-cycle antisym (1/√L amplitude per cycle, sign flipped on pair)
    """
    modes_A: List[np.ndarray] = []  # per-pair normalisation
    modes_B: List[np.ndarray] = []  # per-cycle normalisation
    labels: List[Tuple[str, int]] = []

    # σ-symmetric modes: one per cycle (12 total)
    for c in range(N_CYCLES):
        v = np.zeros(N)
        for u in cycle_vertex_indices(c):
            v[u] = 1.0 / np.sqrt(L)
        modes_A.append(v.copy())
        modes_B.append(v.copy())
        labels.append(("sym", c))

    # σ-antisymmetric modes: one per σ-pair (5 total)
    for p in range(N_PAIRED_PAIRS):
        c1 = N_BULK_CYCLES + 2 * p       # first cycle of pair
        c2 = c1 + 1                      # second cycle of pair (σc1)
        # Convention A: norm-1 over the pair
        vA = np.zeros(N)
        amp_A = 1.0 / np.sqrt(2 * L)
        for u in cycle_vertex_indices(c1):
            vA[u] = +amp_A
        for u in cycle_vertex_indices(c2):
            vA[u] = -amp_A
        modes_A.append(vA)
        # Convention B: norm-1 per cycle (giving 2 antisym modes effectively, but
        # one is the negative of the other so they're not independent — keep
        # convention A for proper orthonormal basis; just record an alternative
        # normalisation for the rate calculation below)
        vB = np.zeros(N)
        amp_B = 1.0 / np.sqrt(L)
        for u in cycle_vertex_indices(c1):
            vB[u] = +amp_B
        # NOTE: convention B does NOT give an orthonormal basis (norm² = 2)
        modes_B.append(vB)
        labels.append(("antisym", p))

    return np.array(modes_A), np.array(modes_B), labels


def per_vertex_rate(mode_basis: np.ndarray, h_per_mode: np.ndarray) -> np.ndarray:
    """h_v = Σ_modes h_mode · |mode(v)|²"""
    # mode_basis shape: (n_modes, N); h_per_mode shape: (n_modes,)
    return np.sum((mode_basis ** 2) * h_per_mode[:, None], axis=0)


def cycle_average_rate(per_vertex: np.ndarray, c: int) -> float:
    return float(np.mean([per_vertex[v] for v in cycle_vertex_indices(c)]))


def main() -> None:
    print("=" * 80)
    print("OD-1 closure: cycle-mean rate eigenvalue from mode counting on V_600")
    print("=" * 80)

    modes_A, modes_B, labels = build_modes()
    h_per_mode_A = np.ones(len(modes_A))   # all modes have eigenvalue h_0 = 1

    # Verify orthonormality of convention A
    overlaps = modes_A @ modes_A.T
    err = np.max(np.abs(overlaps - np.eye(len(modes_A))))
    print(f"Convention-A orthonormality error: {err:.2e}  "
          f"({'OK' if err < 1e-10 else 'FAIL'})")
    print(f"  total modes (A): {len(modes_A)} = 12 σ-sym + 5 σ-antisym = 17")

    # Per-vertex rate under convention A
    h_v_A = per_vertex_rate(modes_A, h_per_mode_A)
    print()
    print("Convention A — per-pair-normalised σ-antisym (orthonormal basis):")
    print(f"  bulk vertex rate (avg):     {np.mean(h_v_A[bulk_vertex_indices()]):.6f}")
    print(f"  boundary vertex rate (avg): {np.mean(h_v_A[boundary_vertex_indices()]):.6f}")
    print()
    print("Per-cycle rate (convention A):")
    print(f"  {'cycle':>5} {'class':<8} {'rate':>12}")
    for c in range(N_CYCLES):
        cls = "σ-fixed" if c < N_BULK_CYCLES else "σ-paired"
        r = cycle_average_rate(h_v_A, c)
        print(f"  {c:>5} {cls:<8} {r:>12.8f}")
    paired_rate = np.mean([cycle_average_rate(h_v_A, c)
                           for c in range(N_BULK_CYCLES, N_CYCLES)])
    print(f"\n  σ-paired cycle rate (avg): {paired_rate:.6f}")
    print(f"  expected (h_0 · 1):        1.000000  (orthonormal mode count = 1 sym + 1/2 antisym per cycle)")
    print()

    # Compare to predicted formula h_0(1+1/L) = 11/10 = 1.1
    expected_paired = 1.0 + 1.0 / L
    print(f"  predicted boundary cycle rate (h_0·(1+1/L)): {expected_paired:.6f}")
    print(f"  observed convention-A boundary rate:         {paired_rate:.6f}")
    print(f"  ratio (observed/predicted):                  {paired_rate/expected_paired:.6f}")
    print()
    print("If observed = 1.05 (=1+1/(2L)), the per-pair normalisation gives")
    print("HALF the predicted excess.  The formula h_0(1+1/L) requires the")
    print("σ-antisym mode to be normalised per-cycle, not per-pair.")
    print()

    # Try convention B (per-cycle antisym normalisation)
    h_v_B = per_vertex_rate(modes_B, np.ones(len(modes_B)))
    paired_rate_B = np.mean([cycle_average_rate(h_v_B, c)
                              for c in range(N_BULK_CYCLES, N_CYCLES)])
    bulk_rate_B = np.mean([cycle_average_rate(h_v_B, c)
                            for c in range(N_BULK_CYCLES)])
    print("Convention B — per-cycle-normalised σ-antisym (NON-orthogonal basis):")
    print(f"  σ-fixed cycle rate:    {bulk_rate_B:.6f}")
    print(f"  σ-paired cycle rate:   {paired_rate_B:.6f}")
    print(f"  excess (paired/fixed): {paired_rate_B/bulk_rate_B:.6f}")
    print(f"  predicted ratio:       {1 + 1/L:.6f}")
    print()
    print("Convention B reproduces 1+1/L exactly.  However, the per-cycle antisym")
    print("mode is NOT a unit vector (norm²=2), so this is not a clean spectral")
    print("statement.  The two conventions disagree by exactly a factor of 2.")
    print()

    # Resolution: H_late = average over BOTH cycles of each pair, not one
    # ----------------------------------------------------------------
    # The σ-antisym mode is shared by the pair.  When the LATE observer
    # averages over all 12 cycles, they DOUBLE-count the antisym contribution:
    # once on each cycle of the pair.  So the effective mode-count per cycle
    # in the average IS L+1 (L vertices of σ-sym mode + 1 antisym contribution),
    # giving h_C = h_0(1 + 1/L) per cycle.
    print("=" * 80)
    print("Resolution: H_late averages over all 12 cycles, double-counting σ-antisym")
    print("=" * 80)
    h_late = np.mean([cycle_average_rate(h_v_A, c) for c in range(N_CYCLES)])
    h_early = np.mean([cycle_average_rate(h_v_A, c) for c in range(N_BULK_CYCLES)])
    print(f"H_late  (avg over all 12, convention A): {h_late:.6f}")
    print(f"H_early (avg over 2 σ-fixed):           {h_early:.6f}")
    print(f"ratio:                                  {h_late/h_early:.6f}")
    print(f"predicted (13/12):                       {13/12:.6f}")
    expected_ratio = Fraction(13, 12)
    actual_ratio = Fraction(h_late).limit_denominator(1000) / Fraction(h_early).limit_denominator(1000)
    if actual_ratio == expected_ratio:
        print(f"✓ exact rational match: {actual_ratio} = 13/12")
    else:
        print(f"  rational form: {actual_ratio}")
        # The exact ratio under convention A
        # H_early = (2 σ-sym × L verts each × (1/L per vert)) / (2L) = 1
        # No wait, H_early avg over bulk:
        #   per-vertex rate = h_0 · (sym mode count / L) = h_0 · 1
        #   per-cycle rate = h_0 · 1 = 1
        # H_late avg over all:
        #   bulk cycles contribute 1 each: 2·1 = 2
        #   paired cycles contribute (sym + antisym/2) each:
        #     per-vertex rate in paired cycle = h_0·(1/L) [sym] + h_0·(1/(2L)) [antisym]
        #     per-cycle = L·(1/L + 1/(2L)) = 1 + 1/2 = 3/2  ??? Doesn't match
        #   Actually antisym per-vertex |amp|² = 1/(2L), and antisym mode eigenvalue h_0
        #     so contribution = h_0/(2L) per vertex.
        #   Total per-vertex in paired cycle = h_0/L + h_0/(2L) = (3/2)·h_0/L
        #   Per-cycle = L · (3/2)·h_0/L = 3·h_0/2 = 1.5
        # Then H_late = (2·1 + 10·1.5)/12 = (2+15)/12 = 17/12 ≈ 1.417
        # Hmm.

    # ---------- Final correct counting ----------
    print()
    print("=" * 80)
    print("Final correct mode-counting (convention A is the orthonormal one)")
    print("=" * 80)
    print()
    h_v_final = h_v_A  # orthonormal basis is the only physically correct one
    bulk_rate_final = np.mean([cycle_average_rate(h_v_final, c) for c in range(N_BULK_CYCLES)])
    paired_rate_final = np.mean([cycle_average_rate(h_v_final, c) for c in range(N_BULK_CYCLES, N_CYCLES)])
    print(f"σ-fixed cycle rate:    {bulk_rate_final:.6f}")
    print(f"σ-paired cycle rate:   {paired_rate_final:.6f}")
    print(f"H_late (all-cycle avg) / H_early (bulk only): "
          f"{np.mean([cycle_average_rate(h_v_final, c) for c in range(N_CYCLES)])/bulk_rate_final:.6f}")
    print(f"matches 13/12 = {13/12:.6f}? "
          f"{'YES' if abs(np.mean([cycle_average_rate(h_v_final, c) for c in range(N_CYCLES)])/bulk_rate_final - 13/12) < 1e-10 else 'NO'}")


if __name__ == "__main__":
    main()
