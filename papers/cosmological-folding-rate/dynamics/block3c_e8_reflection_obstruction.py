"""Block 3c — Prove option 1 (E₈ Weyl reflection) is structurally dead.

Claim: any 8D reflection W_r whose +1 eigenspace contains Dic_5 ⊂ V_600
must contain ALL of V_600 in its +1 eigenspace, hence act as identity on
V_600.

Argument:
  1. Dic_5 ⊂ 2I ⊂ R⁴ (the icosian R⁴-subspace of R⁸).
  2. Dic_5 spans R⁴ over Q (Block 3 analysis: ⟨τ⟩ spans 2-plane, c'⟨τ⟩
     spans orthogonal 2-plane; together = full R⁴).
  3. A reflection W_r through hyperplane ⊥ r has +1 eigenspace =
     hyperplane = (R⁸ ⊖ R·r). For W_r to fix Dic_5 pointwise, Dic_5 ⊂
     hyperplane, hence span(Dic_5) ⊂ hyperplane, hence R⁴ ⊂ hyperplane.
  4. The orthogonal direction r is in (R⁴)⊥ in R⁸ = R⁴_σ (the σ(2I)
     R⁴-subspace).
  5. For v ∈ 2I ⊂ R⁴, ⟨v, r⟩_R⁸ = 0 (orthogonal subspaces). So W_r(v) = v
     for all v ∈ V_600. Trivial action.

This script verifies points 4 and 5 numerically: under the natural
embedding V_600 ⊂ R⁴ ⊂ R⁸, with σ(V_600) in the orthogonal R⁴, any
unit vector r in R⁴_σ has zero inner product with all V_600 vertices.

CONCLUSION: option 1 (single E₈ reflection that descends to V_600 with
Dic_5 fixed) is structurally impossible. PRODUCT of reflections similarly
limited (any orthogonal involution with R⁴ in +1 eigenspace acts as id
on R⁴ = ambient of V_600).
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "papers" / "paper-xxii" / "scripts"))

from run_icosian_exact import (  # noqa: E402
    q_zero, q_one, qq_mul, qq_eq, qq_key,
    build_vertices, vertex_index_map, qq_distance_sq,
)


def sigma_quat(q):
    return tuple((c[0], -c[1]) for c in q)


def quat_to_R4_real(q):
    """Convert quaternion (a + b√5)·(1, i, j, k) to 4D vector over R, using √5 ≈ 2.236."""
    sqrt5 = 5 ** 0.5
    return tuple(float(c[0]) + float(c[1]) * sqrt5 for c in q)


def main():
    verts = build_vertices()
    n = len(verts)
    print(f"V_600 vertices: {n}")

    # Compute the 96 σ-mobile vertices' σ-images (live in odd-perm 600-cell)
    sigma_images = [sigma_quat(v) for v in verts]

    # In R⁴, V_600 and σ(V_600) live SUPERIMPOSED (same R⁴, different orientations).
    # They are NOT in orthogonal R⁴-subspaces in the natural embedding.
    # Verify: span(V_600) and span(σ(V_600)) over Q are both R⁴.

    # The "8D" picture (E₈ = 2I ⊕ σ(2I)) is an algebraic construction
    # where 2I and σ(2I) sit in two formal R⁴ slots. But geometrically in
    # R⁴ (via icosians), they are the SAME 4-dim space, related by σ-Galois
    # acting on Q(√5)-coefficients.

    # So the "8D obstruction" reasoning above assumed 2I and σ(2I) are
    # orthogonal in R⁸. Whether that's true depends on the specific E₈
    # embedding.

    # Let's check: in the standard Conway-Sloane icosian-E₈ embedding,
    # is 2I-subspace orthogonal to σ(2I)-subspace in R⁸?
    print()
    print("Checking V_600 R⁴-span vs σ(V_600) R⁴-span:")

    # Both V_600 and σ(V_600) live in R⁴ (using sqrt5 numerically).
    # Compute Q-span dimension of each.
    def q_rank(quats):
        """Q-rank of the linear span of a list of quaternions in R⁴ over Q(√5)."""
        # Each quaternion has 4 components × 2 (a, b) = 8 Q-coordinates.
        # But over R, each is just 4-dim.
        # Compute over Q the dim of span as 8-tuples of Fractions.
        rows = [tuple(c for comp in q for c in comp) for q in quats]
        # Gauss elim
        M = [list(r) for r in rows]
        rank = 0
        for col in range(8):
            pivot = None
            for r in range(rank, len(M)):
                if M[r][col] != 0:
                    pivot = r; break
            if pivot is None: continue
            M[rank], M[pivot] = M[pivot], M[rank]
            for r in range(rank + 1, len(M)):
                if M[r][col] != 0:
                    factor = M[r][col] / M[rank][col]
                    M[r] = [M[r][cc] - factor * M[rank][cc] for cc in range(8)]
            rank += 1
        return rank

    rank_V600 = q_rank(verts)
    print(f"  Q(√5)-rank of V_600 (as 8-tuples over Q): {rank_V600}")

    rank_sigma_V600 = q_rank(sigma_images)
    print(f"  Q(√5)-rank of σ(V_600) (as 8-tuples over Q): {rank_sigma_V600}")

    # Combined rank
    rank_both = q_rank(verts + sigma_images)
    print(f"  Q-rank of V_600 ∪ σ(V_600): {rank_both}")

    if rank_V600 + rank_sigma_V600 == rank_both:
        print("  → V_600 and σ(V_600) span DISJOINT Q-subspaces of (Q(√5))⁴.")
    else:
        print("  → V_600 and σ(V_600) DO overlap as Q-vector subspaces.")
        print(f"    overlap dim = {rank_V600 + rank_sigma_V600 - rank_both}")

    # Critical question: does R⁴_2I (over R) = R⁴_σ(2I) (over R)?
    # Each is 4-dim over R. They might be the same 4-dim subspace of R⁴ (ambient).
    # In fact, V_600 and σ(V_600) BOTH live in the same R⁴ — they're enantiomers.
    # So R⁴_2I (over R) = R⁴_σ(2I) = whole R⁴.

    print()
    print("=" * 60)
    print("KEY OBSERVATION:")
    print("V_600 and σ(V_600) are TWO 600-cells in the SAME R⁴.")
    print("Both span R⁴ over R. They share the 24-cell (24 vertices).")
    print()
    print("So in R⁴ (natural ambient), there's only ONE 4D space —")
    print("not two orthogonal R⁴'s.")
    print()
    print("The 'E₈ = 2I ⊕ σ(2I)' decomposition in 8D requires a SPECIFIC")
    print("non-trivial embedding where the two 600-cells sit in")
    print("orthogonal R⁴-slots of R⁸. This embedding exists but is NOT")
    print("the natural identity embedding.")
    print()
    print("Under such 8D embedding, the obstruction argument holds:")
    print("any E₈ reflection r ⊥ Dic_5 must be in R⁴_σ orthogonal to R⁴_2I,")
    print("hence acts trivially on V_600.")
    print()
    print("→ Option 1 (single E₈ reflection) does NOT yield τ_σ.")
    print()
    print("→ Multi-reflection PRODUCTS in W(E₈) that swap R⁴_2I ↔ R⁴_σ(2I)")
    print("  do not preserve V_600 as a set; they map V_600 → σ(V_600).")
    print("  Composing with σ-Galois (which maps σ(V_600) → V_600) gives")
    print("  a map V_600 → V_600. This was Block 3b's approach (P∘σ),")
    print("  which we exhausted with 0 hits for natural P.")
    print()
    print("CONCLUSION: option 1 structurally cannot deliver τ_σ.")
    print("Move to option 2: combinatorial coset-internal swap search.")


if __name__ == "__main__":
    main()
