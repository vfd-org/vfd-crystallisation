"""OD-1 Operator-level trace identities (LEGACY exploratory script).

NOTE (2026-05-06): This file is the original 2025 exploratory note.
The publication-ready statement lives at
`papers/v600-cosmic-tensions/`, which separates Layer 1 (theorem-grade
trace identities + K-saturated admissibility theorem) from Layer 3
(coupling-rule hypothesis, NOT a theorem). Forceful "FORCED / no
choices" language has been removed from this script.

Setup:
  - V_600 = 2I, 12 T_τ-cycles, K-multiset = {72:1, 0:1, 52:5, 20:5}.
  - Cycle space C_Q ≅ Q^12 with basis indexed by the 12 cycles.
  - K-class diagonal projectors P_K on C_Q.
    rank(P_72) = 1, rank(P_0) = 1, rank(P_52) = 5, rank(P_20) = 5.

Key identities (all on C_Q, all exact rationals):
  Σ_K P_K = I_12                 (K-classes partition cycles)
  rank(P_K) = m_K                (K-multiplicity)
  tr(I_12) = 12                  (baseline cycle count)
  tr(P_K) = m_K                  (per K-class)

Operators (Layer 1):
  Ĥ_VFD := I_12 + P_72           tr = 13, ratio 13/12
  Ĉ_VFD := I_12 - P_0            tr = 11, ratio 11/12

Layer 3 (hypothesis, NOT proved here): the coupling rule
H_0 ↔ +P_72 and S_8 ↔ -P_0. The numerical match to SH0ES H_0 and
KiDS S_8 is observational; this script does not derive cosmology.

The K-saturated admissibility theorem (only ±P_72 and ±P_0 are
rank-one corrections to I_12 in the K-saturated diagonal projector
algebra A_K) is proved in the publication paper, not here.
"""
from __future__ import annotations

import sys
from pathlib import Path
from fractions import Fraction
from collections import Counter

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, qq_mul, qq_eq, qq_key,
    build_vertices, vertex_index_map, qq_distance_sq,
)


def build_K_classes():
    """Return list of K-values per cycle index (length 12)."""
    verts = build_vertices()
    idx_of = vertex_index_map(verts)
    n = len(verts)
    one = (q_one(), q_zero(), q_zero(), q_zero())

    def order_of(g):
        r = one
        for k in range(1, 31):
            r = qq_mul(r, g)
            if qq_eq(r, one): return k
        return -1

    tau = next(v for v in verts if order_of(v) == 10)
    T = [idx_of[qq_key(qq_mul(tau, verts[i]))] for i in range(n)]
    visited = [False] * n
    cycles = []
    for s in range(n):
        if visited[s]: continue
        c = []; cur = s
        while not visited[cur]:
            visited[cur] = True; c.append(cur); cur = T[cur]
        cycles.append(c)

    distance_sq = [qq_distance_sq(one, verts[j]) for j in range(n)]
    keys_d = [(float(d2[0]) + float(d2[1]) * (5 ** 0.5)) for d2 in distance_sq]
    unique_d = sorted(set(keys_d))
    d2_to_shell = {k: i for i, k in enumerate(unique_d)}
    shell = [d2_to_shell[k] for k in keys_d]
    K_of_cycle = [sum((shell[v] - 4) ** 2 for v in c) for c in cycles]
    return K_of_cycle


def main():
    print("=" * 60)
    print("OD-1 operator-trace derivation of (1 ± 1/12)")
    print("=" * 60)

    K_of_cycle = build_K_classes()
    n_cycles = len(K_of_cycle)
    K_multiset = Counter(K_of_cycle)

    print(f"\nCycle count: n_cycles = {n_cycles}")
    print(f"K-multiset: {dict(K_multiset)}")
    assert dict(K_multiset) == {72: 1, 0: 1, 52: 5, 20: 5}
    assert n_cycles == 12

    # ============================================================
    # K-class projectors P_K on cycle space ℂ^12
    # ============================================================
    print()
    print("=" * 60)
    print("K-class projectors P_K (diagonal on cycle basis)")
    print("=" * 60)

    print(f"\n{'K':<6}{'rank(P_K)':<12}{'tr(P_K)':<10}")
    for K in (72, 0, 52, 20):
        rank_K = K_multiset[K]
        print(f"{K:<6}{rank_K:<12}{rank_K:<10}")

    rank_total = sum(K_multiset.values())
    print(f"\nΣ rank(P_K) = {rank_total} = dim(C) = 12 ✓")

    # ============================================================
    # Operator construction (within K-saturated diagonal projector
    # algebra A_K)
    # ============================================================
    print()
    print("=" * 60)
    print("Building Ĥ and Ĉ from the K-multiset")
    print("=" * 60)

    # The K-multiset {72:1, 0:1, 52:5, 20:5} has exactly TWO rank-1
    # K-classes: K=72 (rank 1) and K=0 (rank 1). The other two classes
    # (K=52, K=20) have rank 5 each.
    #
    # Within the K-saturated diagonal projector algebra A_K, the only
    # rank-1 projector corrections to I_12 are:
    #   + P_72   (max-K-class enhancement)
    #   - P_0    (trivial-K-class suppression)
    #
    # See papers/v600-cosmic-tensions/v600-cosmic-tensions.tex
    # (Theorem 4.2) for the formal statement and the explicit
    # K-saturation hypothesis. Outside A_K (e.g. arbitrary rank-one
    # projectors on C, or τ_σ-invariant rank-one projectors built from
    # mixed K=52 / K=20 directions), there are many other rank-1
    # corrections; this script is restricted to A_K.

    # H(z) operator: expansion observable couples to scale-setting mode
    # (K=72 is the max-distortion bulk anchor). ΛCDM = I_12, VFD = I_12 + P_72.
    tr_H_LCDM = 12
    tr_H_VFD = 12 + K_multiset[72]
    factor_H = Fraction(tr_H_VFD, tr_H_LCDM)
    print(f"\nĤ_ΛCDM = I_12,        tr = {tr_H_LCDM}")
    print(f"Ĥ_VFD  = I_12 + P_72,  tr = 12 + 1 = {tr_H_VFD}")
    print(f"H(z) modification factor: tr(Ĥ_VFD) / tr(Ĥ_ΛCDM) = {factor_H} = 1 + 1/12")

    # σ_8 operator: clustering observable couples to non-trivial cycles.
    # K=0 is the equatorial zero-mode (κ² ≡ 0); it doesn't contribute to
    # clustering. ΛCDM = I_12, VFD = I_12 - P_0.
    tr_C_LCDM = 12
    tr_C_VFD = 12 - K_multiset[0]
    factor_C = Fraction(tr_C_VFD, tr_C_LCDM)
    print(f"\nĈ_ΛCDM = I_12,       tr = {tr_C_LCDM}")
    print(f"Ĉ_VFD  = I_12 - P_0,  tr = 12 - 1 = {tr_C_VFD}")
    print(f"σ_8 modification factor: tr(Ĉ_VFD) / tr(Ĉ_ΛCDM) = {factor_C} = 1 - 1/12")

    # ============================================================
    # Why these are the ONLY rank-1 corrections
    # ============================================================
    print()
    print("=" * 60)
    print("Classification of rank-1 projector corrections in A_K")
    print("=" * 60)
    print(f"""
The K-multiset {dict(K_multiset)} has exactly two rank-1 K-classes:
  - K = 72 (rank 1) ⇒ P_72 is a rank-1 K-class projector.
  - K = 0  (rank 1) ⇒ P_0  is a rank-1 K-class projector.

K=52 and K=20 are each rank 5, so neither P_52 nor P_20 is rank-1.

WARNING (corrected 2026-05-07): the legacy claim "τ_σ-symmetry alone
excludes rank-1 sub-projectors of P_52 / P_20" is FALSE. The rank-1
projector onto span_Q(e_52 + e_20) for a τ_σ-paired K=52, K=20 pair
of basis vectors IS τ_σ-invariant; what excludes it is the
K-saturation hypothesis (i.e. restriction to the diagonal projector
algebra A_K), NOT τ_σ-symmetry. See the K-saturated admissibility
theorem and Remark 3.2 in
papers/v600-cosmic-tensions/v600-cosmic-tensions.tex.

Within A_K, the only rank-1 projector corrections to I_12 are
±P_72 and ±P_0. The sign assignment H_0 ↔ +P_72, S_8 ↔ −P_0 is a
Layer-3 hypothesis (NOT a theorem); see H1 in the publication paper.

Given the K-saturated admissibility criterion, the trace factors
13/12 and 11/12 follow exactly; the observable coupling rule
(H_0 ↔ +P_72, σ_8 ↔ −P_0) remains a separately stated hypothesis.
""")

    # ============================================================
    # Empirical comparison
    # ============================================================
    print("=" * 60)
    print("Empirical match")
    print("=" * 60)

    H0_planck = 67.36
    H0_sh0es = 73.04
    s8_planck = 0.811
    s8_kids = 0.760

    H0_predicted = H0_planck * float(factor_H)
    s8_predicted = s8_planck * float(factor_C)

    print(f"\nH₀:")
    print(f"  Planck:                   {H0_planck} km/s/Mpc")
    print(f"  Predicted (×13/12):       {H0_predicted:.2f} km/s/Mpc")
    print(f"  Observed SH0ES:           {H0_sh0es} km/s/Mpc")
    print(f"  Tension after correction: |{H0_predicted - H0_sh0es:+.2f}| / σ_combined")

    print(f"\nσ_8:")
    print(f"  Planck:                   {s8_planck}")
    print(f"  Predicted (×11/12):       {s8_predicted:.4f}")
    print(f"  Observed KiDS:            {s8_kids}")
    print(f"  Tension after correction: |{s8_predicted - s8_kids:+.4f}| / σ_combined")

    print()
    print("=" * 60)
    print("OD-1 trace identities (Layer 1) + coupling hypothesis (Layer 3)")
    print("=" * 60)
    print(f"""
Layer 1 (theorem-grade): the K-saturated trace identities
  tr(I_12 + P_72) = 13      → ratio 13/12
  tr(I_12 - P_0)  = 11      → ratio 11/12
on the 12-dim rational T_τ-cycle space of V_600 are exact rationals.

Within the K-saturated diagonal projector algebra A_K, the only
rank-one corrections to I_12 are ±P_72 and ±P_0 (proof: orthogonal
idempotent decomposition, Q² = Q forces 0/1 coefficients, K-multiset
{dict(K_multiset)} selects the rank-1 combinations).

Layer 3 (hypothesis, NOT a theorem): the assignment H_0 ↔ +P_72,
S_8 ↔ -P_0 is a separately stated coupling rule. The numerical
match to 73.04 km/s/Mpc and 0.766 is an observational coincidence
that would become a parameter-free consequence of that hypothesis if
assumed; this script does not prove the coupling rule.

See papers/v600-cosmic-tensions/ for the publication-ready statement.
""")


if __name__ == "__main__":
    main()
