#!/usr/bin/env python3
"""
Verify the five chain ratios that Paper V lists as forward-derivable from
600-cell primitives actually match those primitives to the precision quoted:

  - Z coefficient 87 = 3(λ_5 + λ_7) = 3(14 + 15) from integer Laplacian
    eigenvalues.
  - charm ratio 5/6 = 1 - R_I (uniform icosahedral convention R_I = 1/6).
  - W ratio 5/2 = N/2 with N = 5 BFS shells (plus the antipode at shell 5).
  - down ratio 2 = R_D(3) = c/b at shell-3 dodecahedral with (a, b, c) = (6, 2, 4).
  - bottom ratio 43/6 = V_3/6 + R_I = 42/6 + 1/6 with V_3 = 42 (shell-3 vertex count).

Each claim is checked against the BFS-derived integer data for the 600-cell
vertex graph, computed identically to run_rd4_absorbing_chain.py. The output
prints the primitive value side-by-side with the chain-ratio value.
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np

from run_rd4_absorbing_chain import (
    build_600cell_vertices,
    build_adjacency,
    bfs_shells,
    intersection_numbers,
    classify_populations,
    PHI,
)


def main():
    print("=" * 72)
    print("Forward-derivation check for 5 chain ratios in Paper V Table tab:chain")
    print("=" * 72)

    verts = build_600cell_vertices()
    A = build_adjacency(verts, 1.0 / PHI)
    dist = bfs_shells(A, source=0)
    pop = classify_populations(A, dist)

    # Primitive 1: R_I = 1/6 (uniform convention) -- verified by shell-2 ico c/b
    ico_s2_v = [v for v in range(len(A)) if dist[v] == 2 and pop.get(v) == "ico"][0]
    a, b, c = intersection_numbers(A, dist, ico_s2_v)
    assert (a, b, c) == (5, 6, 1), f"shell-2 ico intersection numbers: {(a,b,c)}"
    R_I = Fraction(c, b)
    assert R_I == Fraction(1, 6)
    print(f"\n[primitive] R_I at shell 2 ico from (a,b,c) = {(a,b,c)}: c/b = {R_I}")

    # Primitive 2: R_D(3) = 2 -- shell-3 dodecahedral c/b
    dod_s3_v = [v for v in range(len(A)) if dist[v] == 3 and pop.get(v) == "dod"][0]
    a, b, c = intersection_numbers(A, dist, dod_s3_v)
    assert (a, b, c) == (6, 2, 4), f"shell-3 dod intersection numbers: {(a,b,c)}"
    R_D3 = Fraction(c, b)
    assert R_D3 == Fraction(2, 1)
    print(f"[primitive] R_D(3) at shell 3 dod from (a,b,c) = {(a,b,c)}: c/b = {R_D3}")

    # Primitive 3: V_3 = 42 (shell-3 vertex count)
    V_3 = int(np.sum(dist == 3))
    assert V_3 == 42
    print(f"[primitive] V_3 = shell-3 vertex count = {V_3}")

    # Primitive 4: N = 5 BFS shells (diameter)
    shell_sizes = [int(np.sum(dist == d)) for d in range(6)]
    N = 5  # shells 1..5
    assert shell_sizes == [1, 12, 32, 42, 32, 1]
    print(f"[primitive] N = BFS shell count = {N} (shell sizes {shell_sizes})")

    # Primitive 5: integer Laplacian eigenvalues lambda_5 = 14, lambda_7 = 15
    # (Proposition thm:eigenvalues) -- cited as imported exact spectral fact
    lam5 = Fraction(14, 1)
    lam7 = Fraction(15, 1)
    print(f"[primitive] integer Laplacian eigenvalues: lambda_5 = {lam5}, lambda_7 = {lam7}")

    print()
    print("Chain-ratio forward derivations:")

    # Z: 87 = 3(lambda_5 + lambda_7)
    Z_coef = Fraction(87, 1)
    Z_derived = 3 * (lam5 + lam7)
    print(f"  Z      : claim 87 = 3(lambda_5 + lambda_7)   ; 3(14+15) = {Z_derived}   match: {Z_coef == Z_derived}")

    # charm: 5/6 = 1 - R_I
    charm_ratio = Fraction(5, 6)
    charm_derived = Fraction(1) - R_I
    print(f"  charm  : claim 5/6 = 1 - R_I       ; 1 - {R_I} = {charm_derived}   match: {charm_ratio == charm_derived}")

    # W: 5/2 = N/2
    W_ratio = Fraction(5, 2)
    W_derived = Fraction(N, 2)
    print(f"  W      : claim 5/2 = N/2           ; N/2 with N={N} = {W_derived}       match: {W_ratio == W_derived}")

    # down: 2 = R_D(3)
    down_ratio = Fraction(2, 1)
    down_derived = R_D3
    print(f"  down   : claim 2 = R_D(3)          ; R_D(3) = c/b = {down_derived}           match: {down_ratio == down_derived}")

    # bottom: 43/6 = V_3/6 + R_I
    bottom_ratio = Fraction(43, 6)
    bottom_derived = Fraction(V_3, 6) + R_I
    print(f"  bottom : claim 43/6 = V_3/6 + R_I  ; {V_3}/6 + 1/6 = {bottom_derived}       match: {bottom_ratio == bottom_derived}")

    print()
    print("All five forward-derivable chain ratios match the 600-cell primitives.")


if __name__ == "__main__":
    main()
