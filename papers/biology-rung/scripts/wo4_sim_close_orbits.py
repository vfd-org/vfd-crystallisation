"""WO-4 build B_orbits: sim-close the 2I-on-cells orbit count.

The WO-4 bioelectric paper claims the 600 tetrahedral cells of
the 600-cell decompose into exactly 5 orbits under the action of
2I (the 120-element binary icosahedral group). This script
enumerates the action explicitly and reports the orbit count —
no hand-tuning, no appeal to counting arguments, just direct
enumeration.

Expected output: 5 orbits (the naive |cells|/|group| = 600/120 = 5,
if the action is free; fewer / smaller orbits otherwise).

Per the pair-programmer rule: STOP and report FAIL if the orbit
count is not 5; do NOT adjust expectations to match.

Uses exact arithmetic over ℚ(√5) where possible; falls back to
floating-point vertex matching with tolerance when necessary.
Cell identification: a cell is a 4-tuple of 600-cell vertices
forming a regular tetrahedron (minimum-distance 4-clique in the
vertex graph).
"""

from __future__ import annotations

import sys
from itertools import combinations
from pathlib import Path

import numpy as np

# Reuse the existing 600-cell builder
SCRIPTS_ROOT = Path(__file__).resolve().parents[3] / "scripts"
sys.path.insert(0, str(SCRIPTS_ROOT))

from build_600cell import build_vertices  # type: ignore  # noqa: E402


PHI = (1 + np.sqrt(5)) / 2
# Nearest-neighbour squared distance in the 600-cell (unit-sphere).
# Vertices at angular separation π/5 have squared distance
# 2·(1 − cos(π/5)) = 2 − (1 + √5)/2 · (something) — compute numerically
# via the actual vertex coordinates.


def quaternion_multiply(p, q):
    """Hamilton product p · q for 4-tuples (w, x, y, z)."""
    pw, px, py, pz = p
    qw, qx, qy, qz = q
    return np.array([
        pw * qw - px * qx - py * qy - pz * qz,
        pw * qx + px * qw + py * qz - pz * qy,
        pw * qy - px * qz + py * qw + pz * qx,
        pw * qz + px * qy - py * qx + pz * qw,
    ])


def match_vertex(v: np.ndarray, verts: np.ndarray, tol: float = 1e-9) -> int:
    """Return index of v in verts, or -1 if not found within tol."""
    diffs = np.linalg.norm(verts - v, axis=1)
    idx = int(np.argmin(diffs))
    if diffs[idx] < tol:
        return idx
    return -1


def find_cells(verts: np.ndarray, nn_d2_tol: float = 1e-8) -> list[tuple[int, ...]]:
    """Enumerate the 600 cells = regular tetrahedra of the 600-cell.

    A cell is a 4-clique in the NN-adjacency graph such that all
    six pairwise squared distances equal the NN squared distance.
    """
    N = verts.shape[0]
    # Compute NN squared distance
    d2 = np.sum((verts[:, None, :] - verts[None, :, :]) ** 2, axis=2)
    # Find minimum nonzero entry
    nonzero = d2[d2 > 1e-12]
    nn_d2 = float(np.min(nonzero))
    # Adjacency: pairs at NN distance
    adj = np.zeros((N, N), dtype=bool)
    for i in range(N):
        for j in range(i + 1, N):
            if abs(d2[i, j] - nn_d2) < nn_d2_tol:
                adj[i, j] = adj[j, i] = True
    # 4-cliques
    cells = []
    for i, j, k, l in combinations(range(N), 4):
        if adj[i, j] and adj[i, k] and adj[i, l] and adj[j, k] and adj[j, l] and adj[k, l]:
            cells.append(tuple(sorted((i, j, k, l))))
    return cells


def build_2I_action_on_cells(verts: np.ndarray, cells: list[tuple[int, ...]]
                             ) -> list[list[int]]:
    """For each vertex g ∈ 2I, compute the permutation on cells by left
    multiplication: cell {v_a, v_b, v_c, v_d} ↦ {g·v_a, g·v_b, g·v_c, g·v_d}.

    Returns a list `action[g] = [new_cell_idx_for_each_cell]`.
    """
    cell_set_to_idx = {frozenset(c): idx for idx, c in enumerate(cells)}
    N_cells = len(cells)
    action = []
    for g_idx in range(verts.shape[0]):
        g = verts[g_idx]
        perm = [0] * N_cells
        for c_idx, cell in enumerate(cells):
            new_vertex_indices = []
            for v_idx in cell:
                new_v = quaternion_multiply(g, verts[v_idx])
                # Normalise to unit length (should already be close)
                new_v = new_v / np.linalg.norm(new_v)
                matched = match_vertex(new_v, verts, tol=1e-7)
                if matched < 0:
                    raise RuntimeError(
                        f"Vertex {v_idx} × group-element {g_idx} did not "
                        f"match any 600-cell vertex within tolerance"
                    )
                new_vertex_indices.append(matched)
            new_cell = frozenset(new_vertex_indices)
            if new_cell not in cell_set_to_idx:
                raise RuntimeError(
                    f"Image of cell {c_idx} under group element {g_idx} "
                    f"is not a known cell: {sorted(new_vertex_indices)}"
                )
            perm[c_idx] = cell_set_to_idx[new_cell]
        action.append(perm)
    return action


def orbit_decomposition(action: list[list[int]], N_cells: int) -> list[list[int]]:
    """Compute 2I-orbits on the cell set by BFS through the group action."""
    visited = [False] * N_cells
    orbits = []
    for start in range(N_cells):
        if visited[start]:
            continue
        orbit = set()
        stack = [start]
        while stack:
            c = stack.pop()
            if c in orbit:
                continue
            orbit.add(c)
            for g_idx in range(len(action)):
                dest = action[g_idx][c]
                if dest not in orbit:
                    stack.append(dest)
        for c in orbit:
            visited[c] = True
        orbits.append(sorted(orbit))
    return orbits


def main() -> int:
    print("B_orbits: 2I action on 600-cell cells — orbit enumeration")
    print("=" * 65)
    print()
    print("Step 1: build 600-cell vertices")
    verts = build_vertices()
    N = verts.shape[0]
    print(f"  N vertices = {N} (expected 120)")
    assert N == 120, f"FAIL: expected 120 vertices, got {N}"

    print()
    print("Step 2: enumerate cells as regular tetrahedra (4-cliques at NN distance)")
    cells = find_cells(verts)
    N_cells = len(cells)
    print(f"  N cells = {N_cells} (expected 600)")
    if N_cells != 600:
        print(f"FAIL: expected 600 cells, got {N_cells}")
        return 2

    print()
    print("Step 3: enumerate 2I action on cells by left-multiplication")
    action = build_2I_action_on_cells(verts, cells)
    print(f"  Action built for {len(action)} group elements")

    print()
    print("Step 4: orbit decomposition")
    orbits = orbit_decomposition(action, N_cells)
    print(f"  N orbits = {len(orbits)}")
    print(f"  orbit sizes = {sorted([len(o) for o in orbits])}")

    print()
    print("Step 5: verdict")
    if len(orbits) == 5 and all(len(o) == 120 for o in orbits):
        print("  [SIM-CLOSED] 5 orbits of size 120 each — matches 600 = 5 × 120")
        print("  WO-4's 5-orbit claim is SIM-VERIFIED. Action is free on cells.")
        return 0
    else:
        print(f"  [REPORT] Orbit structure is NOT 5 × 120.")
        print(f"  Actual: {len(orbits)} orbits, sizes {sorted([len(o) for o in orbits])}")
        print(f"  WO-4's 5-orbit claim needs revision to match this actual structure.")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
