#!/usr/bin/env python3
"""
Aria closure kernel — numerical verification.

Constructs V_600 from canonical generators, builds the short-edge
nearest-neighbour graph, computes the Laplacian spectrum, builds
C_phi = L + phi^-2 I, runs the discrete <-> continuum agreement
test as a per-vertex Pearson correlation between psi(v) and
(phi/2) exp(-|x|/phi) at each non-source vertex's chord radius
(plus a shell-mean cross-check), tests the unweighted vs
phi-cocycle-weighted Laplacian variants on the same geometry-only
correlation criterion, sweeps the per-vertex correlation across
all 120 source vertices to verify H_4 transitivity, checks
graph connectedness, and writes results.json.

All constants (phi, the 600-cell vertex generators, the short-edge
inner product phi/2) are mathematically determined by the choice of
substrate; no parameter is fitted to any dataset.

Determinism: no randomness anywhere. Source vertices are picked
by canonical projection (argmax of dot product with $+x_0$ axis);
the eigendecomposition is deterministic.

Run: python3 verify_kernel.py
"""

from __future__ import annotations

import json
import itertools
import math
from pathlib import Path

import numpy as np
from numpy.linalg import eigh, norm
from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


PHI = (1.0 + math.sqrt(5.0)) / 2.0          # golden ratio
INV_PHI = 1.0 / PHI                          # = phi - 1
INV_PHI2 = INV_PHI * INV_PHI                 # = 2 - phi ~ 0.381966


# ---------------------------------------------------------------------------
# 1. 600-cell vertex construction (120 vertices on S^3)
# ---------------------------------------------------------------------------

def even_perms(seq):
    """Return the 12 even permutations of a 4-tuple (alternating group A_4)."""
    n = len(seq)
    out = []
    for p in itertools.permutations(range(n)):
        # signature
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
        if inv % 2 == 0:
            out.append(tuple(seq[p[i]] for i in range(n)))
    return out


def build_v600():
    """
    Canonical 600-cell vertex set: 8 + 16 + 96 = 120 unit vectors on S^3.

    - 8 vertices: all permutations of (+/- 1, 0, 0, 0)
    - 16 vertices: all sign combinations of (+/- 1/2)^4
    - 96 vertices: all even permutations of (+/- phi/2, +/- 1/2, +/- 1/(2 phi), 0),
      with all sign assignments
    """
    verts = set()

    # 8 axis vertices
    for sign in (-1, 1):
        for i in range(4):
            v = [0.0] * 4
            v[i] = float(sign)
            verts.add(tuple(v))

    # 16 half-integer vertices
    for signs in itertools.product((-1, 1), repeat=4):
        v = tuple(0.5 * s for s in signs)
        verts.add(v)

    # 96 phi-mixed vertices: even perms of (+/- phi/2, +/- 1/2, +/- 1/(2 phi), 0)
    base = (PHI / 2.0, 0.5, 1.0 / (2.0 * PHI), 0.0)
    for signs in itertools.product((-1, 1), repeat=4):
        # apply signs componentwise to (PHI/2, 1/2, 1/(2 PHI), 0); the 0 sign is irrelevant
        signed = tuple(s * b for s, b in zip(signs, base))
        for p in even_perms(signed):
            verts.add(p)

    V = np.array(sorted(verts), dtype=np.float64)
    # Sanity check: all on the unit 3-sphere
    radii = np.linalg.norm(V, axis=1)
    assert np.allclose(radii, 1.0, atol=1e-10), \
        f"vertices not on unit S^3: max |r-1| = {np.max(np.abs(radii - 1.0)):.3e}"
    return V


# ---------------------------------------------------------------------------
# 2. Short-edge nearest-neighbour graph
# ---------------------------------------------------------------------------

def build_short_edge_graph(V, tol=1e-10):
    """
    Two vertices are connected iff <v, w> = phi/2 (the canonical short-edge
    criterion on the unit 3-sphere). For the 600-cell this gives a
    12-regular graph on 120 vertices with 720 edges.
    """
    G = V @ V.T  # Gram matrix of inner products
    short = PHI / 2.0
    A = (np.abs(G - short) < tol).astype(np.float64)
    np.fill_diagonal(A, 0.0)  # no self-loops
    return A


# ---------------------------------------------------------------------------
# 3. Laplacian spectrum
# ---------------------------------------------------------------------------

def laplacian_spectrum(A):
    """L = D - A; return sorted eigenvalues + eigenvectors."""
    D = np.diag(A.sum(axis=1))
    L = D - A
    w, U = eigh(L)  # ascending order
    return L, w, U


def round_spectrum(w, decimals=6):
    """Group eigenvalues into multiplicity classes (within numerical tol).

    Eigenvalues stored at full precision; ``decimals`` only sets the
    grouping tolerance.
    """
    classes = []
    seen = []
    for val in w:
        placed = False
        for idx, ref in enumerate(seen):
            if abs(val - ref) < 10 ** (-decimals):
                classes[idx] = (ref, classes[idx][1] + 1)
                placed = True
                break
        if not placed:
            seen.append(val)
            classes.append((float(val), 1))
    return classes


# ---------------------------------------------------------------------------
# 4. Closure operator and discrete Green's function
# ---------------------------------------------------------------------------

def build_C_phi(L):
    """C_phi = L + phi^-2 I."""
    return L + INV_PHI2 * np.eye(L.shape[0])


def green_response(C_phi, source_idx):
    """psi = C_phi^-1 e_source. Solves the linear system, no explicit inverse."""
    n = C_phi.shape[0]
    f = np.zeros(n)
    f[source_idx] = 1.0
    psi = np.linalg.solve(C_phi, f)
    return psi


# ---------------------------------------------------------------------------
# 5. Shell decomposition (9-shell H_3 partition)
# ---------------------------------------------------------------------------

def shell_indices(V, pole_idx):
    """
    Group vertices by their inner product with V[pole_idx]. The 600-cell's
    H_3 subgroup partitions the 120 vertices into 9 shells of sizes
    {1, 12, 20, 12, 30, 12, 20, 12, 1} indexed by inner-product class.
    """
    pole = V[pole_idx]
    inner = V @ pole
    # The 9 canonical inner-product values:
    canonical = np.array([
        1.0,                # shell 0: pole itself
        PHI / 2.0,          # shell 1
        0.5,                # shell 2
        1.0 / (2.0 * PHI),  # shell 3
        0.0,                # shell 4 (equator)
        -1.0 / (2.0 * PHI), # shell 5
        -0.5,               # shell 6
        -PHI / 2.0,         # shell 7
        -1.0,               # shell 8: antipode
    ])
    shells = {k: [] for k in range(9)}
    for i, val in enumerate(inner):
        # snap to nearest canonical
        k = int(np.argmin(np.abs(canonical - val)))
        shells[k].append(i)
    sizes = {k: len(shells[k]) for k in shells}
    return shells, sizes, canonical


# ---------------------------------------------------------------------------
# 6. Discrete <-> continuum agreement test
# ---------------------------------------------------------------------------

def discrete_continuum_test(V, C_phi, source_idx):
    """
    Compute psi(v) = C_phi^-1 e_{source}, then average over each shell. The
    shell radial coordinate x is the chord distance |v - v_source|. The
    continuum prediction is G(x) = (phi/2) exp(-|x|/phi) (up to a normalisation).

    Returns the per-shell discrete mean, the continuum prediction at each
    shell radius, and the Pearson correlation between them.
    """
    psi = green_response(C_phi, source_idx)
    shells, sizes, _ = shell_indices(V, source_idx)
    pole = V[source_idx]

    shell_means = []
    shell_radii = []
    shell_count = []
    for k in range(9):
        idxs = shells[k]
        if not idxs:
            continue
        mean_psi = float(np.mean(psi[idxs]))
        # mean chord radius from pole
        chord = float(np.mean(np.linalg.norm(V[idxs] - pole, axis=1)))
        shell_means.append(mean_psi)
        shell_radii.append(chord)
        shell_count.append(len(idxs))

    shell_means = np.array(shell_means)
    shell_radii = np.array(shell_radii)
    continuum = (PHI / 2.0) * np.exp(-shell_radii / PHI)

    # Pearson correlation of (discrete shell mean) with (continuum prediction)
    if len(shell_means) > 1 and np.std(shell_means) > 0 and np.std(continuum) > 0:
        corr = float(np.corrcoef(shell_means, continuum)[0, 1])
    else:
        corr = float("nan")

    return {
        "shell_radii": shell_radii.tolist(),
        "shell_count": shell_count,
        "shell_psi_mean": shell_means.tolist(),
        "continuum_prediction": continuum.tolist(),
        "pearson_correlation": corr,
    }


# ---------------------------------------------------------------------------
# 7. Variant comparison: unweighted vs phi-cocycle weighted Laplacian
# ---------------------------------------------------------------------------

def cocycle_weights(V, source_idx):
    """
    phi-cocycle vertex weights omega_+(v) = phi^kappa(v), where kappa(v) is
    the shell index of v with respect to a chosen pole. For the variant
    test we compare the unweighted graph Laplacian to two weighted variants
    discussed in the b-anomaly paper.
    """
    shells, _, _ = shell_indices(V, source_idx)
    kappa = np.zeros(V.shape[0])
    for k, idxs in shells.items():
        for i in idxs:
            kappa[i] = float(k)
    return PHI ** kappa


def weighted_laplacian(A, weights, mode="geometric"):
    """
    Weighted graph Laplacian. mode='geometric': w_{vw} = sqrt(omega(v) omega(w)).
    mode='arithmetic': w_{vw} = (omega(v) + omega(w))/2.
    """
    n = A.shape[0]
    if mode == "geometric":
        W = np.sqrt(np.outer(weights, weights))
    elif mode == "arithmetic":
        W = 0.5 * (weights[:, None] + weights[None, :])
    else:
        raise ValueError(mode)
    A_w = A * W
    D_w = np.diag(A_w.sum(axis=1))
    return D_w - A_w


def variant_correlation(V, A, source_idx, variant):
    if variant == "UNWEIGHTED":
        L_v = np.diag(A.sum(axis=1)) - A
    else:
        weights = cocycle_weights(V, source_idx)
        mode = "geometric" if variant == "PHI_GEOMETRIC" else "arithmetic"
        L_v = weighted_laplacian(A, weights, mode=mode)
    C_v = L_v + INV_PHI2 * np.eye(L_v.shape[0])
    test = discrete_continuum_test(V, C_v, source_idx)
    psi = green_response(C_v, source_idx)
    pole = V[source_idx]
    chord = np.linalg.norm(V - pole, axis=1)
    # Continuum kernel at each vertex's chord radius
    cont = (PHI / 2.0) * np.exp(-chord / PHI)
    # Per-vertex correlation (excluding the source itself, which is degenerate)
    mask = np.arange(V.shape[0]) != source_idx
    if np.std(psi[mask]) > 0 and np.std(cont[mask]) > 0:
        per_vertex_corr = float(np.corrcoef(psi[mask], cont[mask])[0, 1])
    else:
        per_vertex_corr = float("nan")
    return {
        "shell_mean_correlation": test["pearson_correlation"],
        "per_vertex_correlation": per_vertex_corr,
        "test": test,
    }


# ---------------------------------------------------------------------------
# 8. Operator-norm bound: ||C_phi^-1|| = 1 / lambda_min(C_phi) = phi^2
# ---------------------------------------------------------------------------

def connectivity_check(A):
    """
    Numerical connectedness verification: count connected components of the
    short-edge adjacency matrix. Connectedness is reported, not derived from
    a structural argument.
    """
    n_components, _ = connected_components(csr_matrix(A), directed=False)
    return {
        "n_connected_components": int(n_components),
        "connected": bool(n_components == 1),
    }


def multi_source_sweep(V, C_phi):
    """
    Per-vertex correlation between psi = C_phi^-1 e_v and the continuum kernel
    G(x) = (phi/2) exp(-x/phi) for every source vertex v in V. H_4 transitivity
    predicts the correlation is invariant under choice of source vertex; this
    function verifies the prediction numerically across all 120 sources and
    reports the min/mean/max envelope.
    """
    n = V.shape[0]
    corrs = np.zeros(n)
    for source_idx in range(n):
        psi = green_response(C_phi, source_idx)
        chord = np.linalg.norm(V - V[source_idx], axis=1)
        cont = (PHI / 2.0) * np.exp(-chord / PHI)
        mask = np.arange(n) != source_idx
        corrs[source_idx] = float(np.corrcoef(psi[mask], cont[mask])[0, 1])
    return {
        "n_sources": int(n),
        "min_correlation": float(corrs.min()),
        "mean_correlation": float(corrs.mean()),
        "max_correlation": float(corrs.max()),
        "max_minus_min": float(corrs.max() - corrs.min()),
    }


def operator_norm_check(L, w):
    lam_min_L = float(w[0])           # 0
    lam_min_C = lam_min_L + INV_PHI2  # phi^-2
    op_norm = 1.0 / lam_min_C         # phi^2
    return {
        "lambda_min_L": lam_min_L,
        "lambda_min_C_phi": lam_min_C,
        "operator_norm_C_phi_inv": op_norm,
        "predicted_phi_squared": PHI ** 2,
    }


# ---------------------------------------------------------------------------
# 9. Run everything and write results.json
# ---------------------------------------------------------------------------

def main():
    out_path = Path(__file__).parent / "results.json"

    V = build_v600()
    n = V.shape[0]
    A = build_short_edge_graph(V)
    deg = A.sum(axis=1)
    n_edges = int(A.sum() // 2)

    L, w, U = laplacian_spectrum(A)
    spectrum = round_spectrum(w, decimals=4)

    C_phi = build_C_phi(L)
    op_norm = operator_norm_check(L, w)
    connectivity = connectivity_check(A)
    multi_source = multi_source_sweep(V, C_phi)

    # Pick the +x_0 axis vertex as canonical pole/source.
    pole_idx = int(np.argmax(V @ np.array([1.0, 0.0, 0.0, 0.0])))
    pole = V[pole_idx]

    shells, shell_sizes, canonical_inner = shell_indices(V, pole_idx)

    test = discrete_continuum_test(V, C_phi, pole_idx)

    # Variant comparison on the same source
    variants = {}
    for variant in ("UNWEIGHTED", "PHI_GEOMETRIC", "PHI_ARITHMETIC"):
        out = variant_correlation(V, A, pole_idx, variant)
        variants[variant] = {
            "shell_mean_correlation": out["shell_mean_correlation"],
            "per_vertex_correlation": out["per_vertex_correlation"],
        }

    result = {
        "phi": PHI,
        "phi_inv_sq": INV_PHI2,
        "n_vertices": n,
        "n_edges": n_edges,
        "degree_sequence": {
            "min": int(deg.min()),
            "max": int(deg.max()),
            "mean": float(deg.mean()),
        },
        "connectivity": connectivity,
        "shell_sizes": shell_sizes,
        "shell_inner_products": canonical_inner.tolist(),
        "antipodal_check": {
            "pole_idx": pole_idx,
            "antipode_idx": int(np.argmin(V @ pole)),
            "expected_shell_8_size": 1,
            "observed_shell_8_size": shell_sizes.get(8, 0),
        },
        "laplacian_spectrum_grouped": [
            {"eigenvalue": ev, "multiplicity": m} for ev, m in spectrum
        ],
        "operator_norm": op_norm,
        "discrete_continuum_test": test,
        "variant_correlation": variants,
        "multi_source_sweep": multi_source,
    }

    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    # Headline summary
    print("=" * 60)
    print("ARIA Closure Kernel — verification")
    print("=" * 60)
    print(f"|V|           = {n}  (expected 120)")
    print(f"|E|           = {n_edges}  (expected 720)")
    print(f"degree min/max = {int(deg.min())}/{int(deg.max())}  (expected 12/12)")
    print(f"connected      = {connectivity['connected']}  "
          f"(components = {connectivity['n_connected_components']})")
    print(f"shell sizes   = {[shell_sizes[k] for k in range(9)]}")
    print(f"               (expected [1, 12, 20, 12, 30, 12, 20, 12, 1])")
    print()
    print("Laplacian spectrum (eigenvalue, multiplicity):")
    for ev, m in spectrum:
        print(f"  {ev:>8.4f}   x {m}")
    print()
    print(f"||C_phi^-1||  = {op_norm['operator_norm_C_phi_inv']:.6f}")
    print(f"   phi^2       = {op_norm['predicted_phi_squared']:.6f}  (predicted)")
    print()
    print("Discrete <-> continuum agreement (Pearson correlation):")
    print(f"  variant         | shell-mean  | per-vertex")
    for v in ("UNWEIGHTED", "PHI_GEOMETRIC", "PHI_ARITHMETIC"):
        sm = variants[v]["shell_mean_correlation"]
        pv = variants[v]["per_vertex_correlation"]
        print(f"  {v:<15} | {sm:>10.6f}  | {pv:>10.6f}")
    print()
    print(f"Multi-source sweep over all {multi_source['n_sources']} vertices:")
    print(f"  per-vertex correlation min  = {multi_source['min_correlation']:.6f}")
    print(f"  per-vertex correlation mean = {multi_source['mean_correlation']:.6f}")
    print(f"  per-vertex correlation max  = {multi_source['max_correlation']:.6f}")
    print(f"  max - min                   = {multi_source['max_minus_min']:.2e}")
    print()
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
