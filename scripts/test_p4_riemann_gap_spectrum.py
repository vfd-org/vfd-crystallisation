#!/usr/bin/env python3
"""
P4 test: cascade cum-κ closure gaps vs rescaled Riemann zero gaps.

Reads the helix-sim infrastructure from notebooks/explorer/04_helix_closure.py
(reused functions: pentagonal-clock K-multiset, cycle-resolved κ trajectory,
δ(γ) closure detector cum_κ ≡ 0 mod 150) but runs at higher T for cleaner
gap-spectrum statistics.

Compares the cascade closure-gap distribution against the rescaled Riemann
zero gaps using:
  (1) Kolmogorov-Smirnov two-sample test
  (2) cumulative distribution overlay
  (3) spectral cross-correlation of unfolded gap series

Honest scope: this tests the GAP SPECTRUM.  Pass means the cascade closure
gaps come from the same statistical distribution as Riemann zero gaps after
rescaling to unit mean; that would tighten the cascade ↔ RH consilience to
distribution-level (GUE-like) agreement.  Fail means the distributions are
different and the cum-κ-closure interpretation is empirically distinct from
the Riemann-zero structure.

Either outcome is informative.  Results feed back into:
  - docs/cascade-helix-hypothesis.md (P4 verdict)
  - docs/fractal-cascade-projection.md (open list)
  - docs/rh-projection-class.md (consilience scope)
"""
from __future__ import annotations

import sys
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from collections import Counter

# --- Helix-sim wiring ----------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "papers" / "paper-xxii" / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "papers" / "cascade-derivation" / "scripts"))


def compute_pentagonal_clock_data():
    """Mirror of `04_helix_closure.compute_pentagonal_clock_data`."""
    from run_icosian_exact import (
        q_zero, q_one, qq_mul, qq_key, qq_distance_sq,
        build_vertices, vertex_index_map, vertex_index_exact,
    )
    from derive_pentagonal_clock_B8p_proper import qsq5_less

    verts = build_vertices()
    assert len(verts) == 120
    identity = (q_one(), q_zero(), q_zero(), q_zero())
    id_idx = vertex_index_exact(identity, verts)
    verts[0], verts[id_idx] = verts[id_idx], verts[0]
    idx_map = vertex_index_map(verts)
    identity_key = qq_key(identity)

    shells_by_dist = {}
    for i, v in enumerate(verts):
        d_sq = qq_distance_sq(identity, v)
        shells_by_dist.setdefault(d_sq, []).append(i)
    sorted_dists = list(shells_by_dist.keys())
    n_dist = len(sorted_dists)
    for i in range(n_dist):
        for j in range(i + 1, n_dist):
            if qsq5_less(sorted_dists[j], sorted_dists[i]):
                sorted_dists[i], sorted_dists[j] = sorted_dists[j], sorted_dists[i]
    shell_of_idx = {}
    for shell_num, d_sq in enumerate(sorted_dists):
        for v_idx in shells_by_dist[d_sq]:
            shell_of_idx[v_idx] = shell_num

    kappa_per_vertex = [(shell_of_idx[i] - 4) ** 2 for i in range(120)]

    def element_order(g):
        power = g
        for n in range(1, 121):
            if qq_key(power) == identity_key:
                return n
            power = qq_mul(power, g)
        raise RuntimeError("order not found")

    tau = None
    for i, v in enumerate(verts):
        if i == 0:
            continue
        if element_order(v) == 10:
            tau = v
            break
    assert tau is not None

    visited = [False] * 120
    cycle_index_lists = []
    for start in range(120):
        if visited[start]:
            continue
        orbit = []
        i = start
        while not visited[i]:
            visited[i] = True
            orbit.append(i)
            i = idx_map[qq_key(qq_mul(tau, verts[i]))]
        cycle_index_lists.append(orbit)
    assert len(cycle_index_lists) == 12

    K_per_cycle = [sum(kappa_per_vertex[v] for v in cyc) for cyc in cycle_index_lists]
    return K_per_cycle, cycle_index_lists, kappa_per_vertex


def detect_cum_kappa_closures(cycle_index_lists, kappa_per_vertex,
                               T: int, modulus: int = 150) -> np.ndarray:
    """δ(γ) detector: ticks where cum-κ ≡ 0 mod 150."""
    cum_kappa = np.zeros(T, dtype=np.int64)
    for cyc in cycle_index_lists:
        kappa_seq = [kappa_per_vertex[v] for v in cyc]
        n_repeats = T // len(kappa_seq) + 1
        full_seq = (kappa_seq * n_repeats)[:T]
        cum_kappa += np.cumsum(full_seq)
    return np.where((cum_kappa % modulus) == 0)[0]


# --- Riemann data --------------------------------------------------------

def load_riemann_zeros(path: Path, n: int = 1000) -> np.ndarray:
    """Load first n Riemann zero imaginary parts."""
    with open(path) as f:
        zeros = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            zeros.append(float(line))
            if len(zeros) >= n:
                break
    return np.array(zeros)


def unfold_riemann_zeros(gammas: np.ndarray) -> np.ndarray:
    """Unfold Riemann zeros to unit-mean spacing.

    Standard unfolding:  γ_n* = (γ_n / (2π)) · log(γ_n / (2π e)) + 1/8.
    The 1/8 constant follows from the Riemann-Siegel formula; for our
    distribution-comparison purposes it is a tick offset and irrelevant.
    The unfolded series has unit mean spacing asymptotically.
    """
    return (gammas / (2 * math.pi)) * np.log(gammas / (2 * math.pi * math.e))


# --- Cascade gap rescaling ----------------------------------------------

def rescale_to_unit_mean(gaps: np.ndarray) -> np.ndarray:
    """Rescale a gap series to unit mean."""
    if len(gaps) == 0:
        return gaps
    return gaps / gaps.mean()


# --- KS test ------------------------------------------------------------

def two_sample_ks(a: np.ndarray, b: np.ndarray) -> tuple:
    """Two-sample Kolmogorov-Smirnov statistic + asymptotic p-value.

    Returns (D, p) where D is the supremum |F_a - F_b| and p is the
    Kolmogorov-Smirnov asymptotic p-value.
    """
    a_sorted = np.sort(a)
    b_sorted = np.sort(b)
    all_pts = np.concatenate([a_sorted, b_sorted])
    cdf_a = np.searchsorted(a_sorted, all_pts, side="right") / len(a_sorted)
    cdf_b = np.searchsorted(b_sorted, all_pts, side="right") / len(b_sorted)
    D = float(np.max(np.abs(cdf_a - cdf_b)))
    n_a, n_b = len(a), len(b)
    en = math.sqrt(n_a * n_b / (n_a + n_b))
    # Asymptotic p-value (Kolmogorov distribution).
    lam = (en + 0.12 + 0.11 / en) * D
    j = np.arange(1, 101)
    terms = 2 * (-1) ** (j - 1) * np.exp(-2 * (lam * j) ** 2)
    p = float(min(1.0, max(0.0, terms.sum())))
    return D, p


# --- Main ---------------------------------------------------------------

def main():
    print("=" * 70)
    print("P4 TEST: cascade cum-κ closure gaps vs rescaled Riemann zero gaps")
    print("=" * 70)

    # 1. Cascade closures at higher T.
    T = 20_000
    print(f"\n[cascade] Building pentagonal clock from icosian arithmetic ...")
    K_per_cycle, cycle_index_lists, kappa_per_vertex = compute_pentagonal_clock_data()
    K_multiset = Counter(K_per_cycle)
    print(f"[cascade] K-multiset: {dict(sorted(K_multiset.items()))}")

    print(f"[cascade] Detecting cum-κ ≡ 0 mod 150 closures over T = {T} ticks ...")
    closures = detect_cum_kappa_closures(cycle_index_lists, kappa_per_vertex, T)
    cascade_gaps_raw = np.diff(closures).astype(float)
    print(f"[cascade] {len(closures)} closures → {len(cascade_gaps_raw)} gaps")
    print(f"[cascade] gap stats: mean = {cascade_gaps_raw.mean():.3f}, "
          f"std = {cascade_gaps_raw.std():.3f}, "
          f"min = {int(cascade_gaps_raw.min())}, "
          f"max = {int(cascade_gaps_raw.max())}")

    cascade_gaps = rescale_to_unit_mean(cascade_gaps_raw)
    print(f"[cascade] rescaled gap mean = {cascade_gaps.mean():.4f}, "
          f"std = {cascade_gaps.std():.4f}")

    # 2. Riemann gaps from Odlyzko data.
    odlyzko_path = REPO_ROOT / "data" / "odlyzko_zeros1.raw"
    n_zeros = min(len(cascade_gaps_raw) + 1, 1000)
    print(f"\n[riemann] Loading first {n_zeros} Odlyzko zeros from {odlyzko_path.name} ...")
    gammas = load_riemann_zeros(odlyzko_path, n=n_zeros)
    print(f"[riemann] zero range: γ_1 = {gammas[0]:.3f}, γ_{n_zeros} = {gammas[-1]:.3f}")

    unfolded = unfold_riemann_zeros(gammas)
    riemann_gaps = np.diff(unfolded)
    print(f"[riemann] {len(riemann_gaps)} unfolded gaps")
    print(f"[riemann] unfolded gap mean = {riemann_gaps.mean():.4f}, "
          f"std = {riemann_gaps.std():.4f}")
    # Sanity: unfolded gap mean should be ≈ 1.
    assert 0.9 < riemann_gaps.mean() < 1.1, \
        f"unfolded mean {riemann_gaps.mean():.4f} not ≈ 1 — unfold formula may be off"

    # 3. KS two-sample test.
    print(f"\n[KS]    Two-sample test: cascade gaps vs unfolded Riemann gaps")
    n_use = min(len(cascade_gaps), len(riemann_gaps))
    D, p = two_sample_ks(cascade_gaps[:n_use], riemann_gaps[:n_use])
    print(f"[KS]    D = {D:.4f}, p = {p:.4e} (n_samples = {n_use} per side)")

    # 4. Distribution-shape diagnostics.
    print(f"\n[shape]   GUE vs Poisson level-spacing diagnostics")
    # Wigner surmise (GUE): P(s) = (32/π²) s² exp(-4s²/π).  std/mean ≈ 0.4226.
    # Poisson:              P(s) = exp(-s).                   std/mean = 1.0.
    cs_ratio = float(cascade_gaps.std() / cascade_gaps.mean())
    rm_ratio = float(riemann_gaps.std() / riemann_gaps.mean())
    print(f"[shape]   std/mean — cascade:  {cs_ratio:.4f}")
    print(f"[shape]   std/mean — Riemann:  {rm_ratio:.4f}")
    print(f"[shape]   reference — GUE Wigner surmise: 0.4226 (level repulsion)")
    print(f"[shape]   reference — Poisson:            1.0000 (no repulsion)")

    # Level-repulsion check: fraction of gaps below 0.1 (small-s tail).
    cs_small = float((cascade_gaps < 0.1).mean())
    rm_small = float((riemann_gaps < 0.1).mean())
    print(f"[shape]   P(rescaled gap < 0.1) — cascade: {cs_small:.4f}")
    print(f"[shape]   P(rescaled gap < 0.1) — Riemann: {rm_small:.4f}")

    # 5. De-trended power-spectrum comparison.  Cumulative-sum Pearson is
    # trivially ≈ 1 for any unit-mean series; instead compare the power
    # spectra of the gap series themselves.
    print(f"\n[spectral] Power-spectrum overlap of detrended gap series")
    cs_d = cascade_gaps[:n_use] - cascade_gaps[:n_use].mean()
    rm_d = riemann_gaps[:n_use] - riemann_gaps[:n_use].mean()
    cs_psd = np.abs(np.fft.rfft(cs_d)) ** 2
    rm_psd = np.abs(np.fft.rfft(rm_d)) ** 2
    cs_psd /= cs_psd.sum()
    rm_psd /= rm_psd.sum()
    psd_overlap = float(np.minimum(cs_psd, rm_psd).sum())  # Bhattacharyya-ish overlap
    print(f"[spectral] PSD overlap (∫min(cs, rm) df): {psd_overlap:.4f}")
    print(f"[spectral]   reference: 1.0 = identical spectra, 0.0 = disjoint")

    # Pearson on detrended gap SERIES (not cumulatives).  Should be ≈ 0
    # if no point-by-point correlation exists.
    a_norm = np.linalg.norm(cs_d)
    b_norm = np.linalg.norm(rm_d)
    pearson = float(np.dot(cs_d, rm_d) / max(a_norm * b_norm, 1e-30))
    print(f"[spectral] Pearson on detrended gap series:    {pearson:.4f}")

    # 5. Verdict.
    print("\n" + "=" * 70)
    print("VERDICT")
    print("=" * 70)
    if p > 0.05:
        verdict = "PASS — cannot reject same-distribution hypothesis at α = 0.05"
    elif p > 0.01:
        verdict = "MARGINAL — distributions differ at α = 0.05 but not α = 0.01"
    else:
        verdict = "FAIL — distributions clearly differ"
    print(f"  KS verdict:  {verdict}")
    print(f"  cascade std/mean = {cs_ratio:.4f}  (GUE: 0.42, Poisson: 1.00)")
    print(f"  Riemann std/mean = {rm_ratio:.4f}  (GUE: 0.42, Poisson: 1.00)")
    if cs_ratio < 0.6:
        cs_class = "GUE-like (level repulsion)"
    elif cs_ratio < 0.85:
        cs_class = "intermediate (weak repulsion)"
    else:
        cs_class = "Poisson-like (no repulsion)"
    print(f"  cascade gap-statistic class: {cs_class}")
    print(f"  PSD overlap: {psd_overlap:.4f}  (Pearson on detrended series: {pearson:.4f})")

    # 6. Plot.
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

    ax = axes[0]
    ax.hist(cascade_gaps[:n_use], bins=50, density=True, alpha=0.6,
            label=f"cascade (n={n_use})", color="steelblue")
    ax.hist(riemann_gaps[:n_use], bins=50, density=True, alpha=0.4,
            label=f"unfolded Riemann (n={n_use})", color="crimson")
    ax.set_xlabel("rescaled gap (unit mean)")
    ax.set_ylabel("density")
    ax.set_title("Gap distributions (rescaled to unit mean)")
    ax.legend()

    ax = axes[1]
    cs_sorted = np.sort(cascade_gaps[:n_use])
    rm_sorted = np.sort(riemann_gaps[:n_use])
    cdf = np.linspace(0, 1, n_use)
    ax.plot(cs_sorted, cdf, label="cascade CDF", color="steelblue")
    ax.plot(rm_sorted, cdf, label="Riemann CDF", color="crimson")
    ax.set_xlabel("rescaled gap")
    ax.set_ylabel("CDF")
    ax.set_title(f"CDF overlay (KS D = {D:.3f}, p = {p:.2e})")
    ax.legend()

    ax = axes[2]
    s = np.linspace(0.01, 4, 200)
    wigner = (32 / math.pi ** 2) * s ** 2 * np.exp(-4 * s ** 2 / math.pi)
    poisson_pdf = np.exp(-s)
    ax.plot(s, wigner, "k--", lw=1, label="GUE Wigner surmise")
    ax.plot(s, poisson_pdf, "k:", lw=1, label="Poisson")
    ax.hist(cascade_gaps[:n_use], bins=40, density=True, alpha=0.6,
            label=f"cascade (σ/μ={cs_ratio:.2f})", color="steelblue")
    ax.hist(riemann_gaps[:n_use], bins=40, density=True, alpha=0.4,
            label=f"Riemann (σ/μ={rm_ratio:.2f})", color="crimson")
    ax.set_xlabel("rescaled gap s")
    ax.set_ylabel("P(s)")
    ax.set_title("Level-spacing distribution vs GUE / Poisson")
    ax.legend(fontsize=8)
    ax.set_xlim(0, 4)

    plt.tight_layout()
    out_path = REPO_ROOT / "scripts" / "p4_gap_spectrum.png"
    plt.savefig(out_path, dpi=120)
    print(f"\nplot saved to {out_path}")

    return {
        "D": D, "p": p,
        "psd_overlap": psd_overlap,
        "pearson_detrended": pearson,
        "cascade_std_over_mean": cs_ratio,
        "riemann_std_over_mean": rm_ratio,
        "n_samples": n_use,
        "cascade_gaps_raw": cascade_gaps_raw,
        "cascade_gaps_rescaled": cascade_gaps,
        "riemann_gaps_unfolded": riemann_gaps,
    }


if __name__ == "__main__":
    main()
