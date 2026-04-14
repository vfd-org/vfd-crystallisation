#!/usr/bin/env python3
"""
Generation Structure from Z₃ ⊂ 2I
====================================
Paper XXII: Toward the Standard Model from Closure Geometry

Computes the concrete Z₃ decomposition of the mass-carrying irreps
of the binary icosahedral group 2I to determine whether 3 fermion
generations emerge naturally from the 600-cell structure.

Requirements: numpy, scipy
Usage: python run_generation_structure.py
"""

import numpy as np
from collections import Counter, defaultdict
from itertools import permutations, product as iproduct
from scipy.spatial.distance import cdist

PHI = (1 + np.sqrt(5)) / 2


def generate_600cell():
    vertices = set()
    for i in range(4):
        for s in [1.0, -1.0]:
            v = [0.0] * 4; v[i] = s
            vertices.add(tuple(round(x, 12) for x in v))
    for signs in iproduct([0.5, -0.5], repeat=4):
        vertices.add(tuple(round(x, 12) for x in signs))
    all_p = list(permutations([0, 1, 2, 3]))
    even_p = [p for p in all_p
              if sum(1 for i in range(4) for j in range(i+1, 4) if p[i] > p[j]) % 2 == 0]
    for perm in even_p:
        for s1 in [1, -1]:
            for s2 in [1, -1]:
                for s3 in [1, -1]:
                    base = [0.0, s1 * 0.5, s2 * PHI / 2, s3 / (2 * PHI)]
                    v = [base[perm.index(i)] for i in range(4)]
                    vertices.add(tuple(round(x, 12) for x in v))
    return np.array(sorted(vertices))


def quaternion_multiply(q1, q2):
    """Multiply two quaternions represented as 4-vectors (w, x, y, z)."""
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    return np.array([
        w1*w2 - x1*x2 - y1*y2 - z1*z2,
        w1*x2 + x1*w2 + y1*z2 - z1*y2,
        w1*y2 - x1*z2 + y1*w2 + z1*x2,
        w1*z2 + x1*y2 - y1*x2 + z1*w2
    ])


def find_order(q, vertices, max_order=60):
    """Find the order of quaternion q in the group."""
    identity = np.array([1.0, 0.0, 0.0, 0.0])
    power = q.copy()
    for k in range(1, max_order + 1):
        if np.allclose(power, identity, atol=1e-8):
            return k
        power = quaternion_multiply(power, q)
    return -1


def main():
    print("=" * 70)
    print("GENERATION STRUCTURE FROM Z₃ ⊂ 2I")
    print("Paper XXII: Toward the Standard Model from Closure Geometry")
    print("=" * 70)

    V = generate_600cell()

    # The 600-cell vertices ARE the elements of 2I as unit quaternions
    # Identity element: (1, 0, 0, 0)
    identity_idx = None
    for i, v in enumerate(V):
        if np.allclose(v, [1, 0, 0, 0], atol=1e-8):
            identity_idx = i
            break

    if identity_idx is None:
        # Find closest to identity
        dists_to_id = np.linalg.norm(V - np.array([1, 0, 0, 0]), axis=1)
        identity_idx = np.argmin(dists_to_id)

    print(f"\n[1] GROUP STRUCTURE OF 2I")
    print(f"    Identity element at index {identity_idx}: {V[identity_idx]}")

    # Find elements of each order
    orders = {}
    for i, v in enumerate(V):
        o = find_order(v, V)
        if o not in orders:
            orders[o] = []
        orders[o].append(i)

    print(f"\n    Element orders in 2I:")
    for o in sorted(orders.keys()):
        print(f"      Order {o:3d}: {len(orders[o]):4d} elements")

    # Z₃ elements: order 3 (or order 6 with order-3 cube)
    print(f"\n[2] Z₃ SUBGROUPS")

    # Elements of order 3 generate Z₃ subgroups
    order3_elements = orders.get(3, [])
    order6_elements = orders.get(6, [])

    # In 2I, elements of order 3 correspond to 2π/3 rotations
    # Elements of order 6 correspond to π/3 rotations (their cubes are order 2)
    print(f"    Elements of order 3: {len(order3_elements)}")
    print(f"    Elements of order 6: {len(order6_elements)}")

    # Each pair {g, g²} with g of order 3 generates a Z₃
    z3_subgroups = []
    used = set()
    for idx in order3_elements:
        if idx in used:
            continue
        g = V[idx]
        g2 = quaternion_multiply(g, g)
        # Find g² in the vertex list
        g2_idx = None
        for j, v in enumerate(V):
            if np.allclose(v, g2, atol=1e-8):
                g2_idx = j
                break
        if g2_idx is not None:
            z3_subgroups.append((identity_idx, idx, g2_idx))
            used.add(idx)
            used.add(g2_idx)

    print(f"    Distinct Z₃ subgroups: {len(z3_subgroups)}")

    if z3_subgroups:
        # Take the first Z₃ subgroup
        z3 = z3_subgroups[0]
        g_elem = V[z3[1]]
        print(f"\n    Using Z₃ = {{e, g, g²}} with g = {g_elem}")
        print(f"    g has order {find_order(g_elem, V)}")

        # Build the adjacency matrix and eigenspaces
        dists = cdist(V, V)
        np.fill_diagonal(dists, np.inf)
        nn_dist = np.min(dists)
        A = (np.abs(dists - nn_dist) < 1e-6).astype(float)
        adj_evals, adj_evecs = np.linalg.eigh(A)

        eig_sectors = defaultdict(list)
        for i, ev in enumerate(adj_evals):
            eig_sectors[round(ev, 2)].append(i)

        # Build the Z₃ action matrix
        # Left multiplication by g permutes the vertices
        g_perm = np.zeros(120, dtype=int)
        g2_perm = np.zeros(120, dtype=int)

        for i, v in enumerate(V):
            gv = quaternion_multiply(g_elem, v)
            g2v = quaternion_multiply(quaternion_multiply(g_elem, g_elem), v)
            # Find gv and g²v in vertex list
            for j, w in enumerate(V):
                if np.allclose(gv, w, atol=1e-8):
                    g_perm[i] = j
                if np.allclose(g2v, w, atol=1e-8):
                    g2_perm[i] = j

        # Build permutation matrix
        G_mat = np.zeros((120, 120))
        for i in range(120):
            G_mat[i, g_perm[i]] = 1

        print(f"\n[3] Z₃ ACTION ON EIGENSPACES")
        print(f"    For each eigenvalue sector, decompose under Z₃:")
        print(f"    Z₃ characters: 1, ω=e^(2πi/3), ω²=e^(-2πi/3)")

        omega = np.exp(2j * np.pi / 3)

        mass_alphas = {3.0: "λ=9 (dim4)", 0.0: "λ=12 (dim5)",
                       -2.0: "λ=14 (dim6)", -3.0: "λ=15 (dim4')"}

        for alpha in sorted(eig_sectors.keys(), reverse=True):
            indices = eig_sectors[alpha]
            mult = len(indices)
            lam = 12 - alpha
            is_int = abs(lam - round(lam)) < 0.01

            # Project G_mat onto this eigenspace
            V_sec = adj_evecs[:, indices]  # 120 × mult
            G_projected = V_sec.T @ G_mat @ V_sec  # mult × mult

            # Eigenvalues of the projected G should be cube roots of unity
            g_eigs = np.linalg.eigvals(G_projected)
            g_eigs_rounded = np.round(g_eigs, 4)

            # Count multiplicities of each Z₃ character
            n_trivial = sum(1 for e in g_eigs if abs(e - 1) < 0.1)
            n_omega = sum(1 for e in g_eigs if abs(e - omega) < 0.1)
            n_omega2 = sum(1 for e in g_eigs if abs(e - omega**2) < 0.1)

            name = mass_alphas.get(alpha, f"λ={lam:.2f}")
            marker = " ← MASS" if is_int and lam > 0.5 else ""

            print(f"    α={alpha:6.2f} ({name:>16}, mult {mult:3d}): "
                  f"1:{n_trivial}, ω:{n_omega}, ω²:{n_omega2}{marker}")

        # Detailed analysis of the spinor sectors
        print(f"\n[4] GENERATION DECOMPOSITION OF SPINOR SECTORS")

        for alpha, name in [(3.0, "λ=9 (spinor)"), (-3.0, "λ=15 (conj. spinor)")]:
            indices = eig_sectors[alpha]
            mult = len(indices)
            V_sec = adj_evecs[:, indices]
            G_projected = V_sec.T @ G_mat @ V_sec

            g_eigs = np.linalg.eigvals(G_projected)
            n1 = sum(1 for e in g_eigs if abs(e - 1) < 0.1)
            nw = sum(1 for e in g_eigs if abs(e - omega) < 0.1)
            nw2 = sum(1 for e in g_eigs if abs(e - omega**2) < 0.1)

            print(f"\n    {name} (multiplicity {mult} = {int(np.sqrt(mult))}²):")
            print(f"      Z₃ decomposition: {n1} × (trivial) + {nw} × (ω) + {nw2} × (ω²)")
            print(f"      Total: {n1} + {nw} + {nw2} = {n1 + nw + nw2}")

            if nw > 0 and nw == nw2:
                n_gen = nw
                print(f"      → {n_gen} generation-like pairs (ω, ω²)")
                print(f"      → {n1} trivial (singlet) components")
                if n_gen >= 3:
                    print(f"      → CONTAINS AT LEAST 3 GENERATION PAIRS ✓")

        # Summary
        print(f"\n{'='*70}")
        print("SUMMARY")
        print(f"{'='*70}")
        print(f"""
    The binary icosahedral group 2I contains elements of order 3,
    generating Z₃ subgroups. Under the Z₃ action:

    Each eigenvalue sector of the 600-cell decomposes into
    Z₃ representations: trivial (1), ω, and ω².

    The mass-carrying spinor sectors (dim 4, mult 16) decompose
    under Z₃, with the nontrivial representations providing
    a natural generation structure.

    Key question: does the Z₃ decomposition of the spinor sectors
    give exactly 3 generations? The computation above answers this
    for the specific Z₃ subgroup chosen.
        """)

    print("=" * 70)
    print("COMPUTATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
