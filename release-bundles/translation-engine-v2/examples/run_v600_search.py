"""Apply the extended translation engine to V_600's 26-dim Galois-paired
block.

The search asks: among compositions of (base block operators) + (Hecke
operators at various primes), is there a composition whose spectrum
best approximates the first 26 Riemann gamma_n?

This is an honest exploratory probe.  The expected outcome is that the
search finds a CANDIDATE-level fit but not an EXACT one -- because
constructing an EXACT match requires real Hilbert modular form
machinery (Hecke operators on actual modular forms over Q(sqrt 5))
that this prototype does not implement.
"""
from __future__ import annotations

import math
import sys
from itertools import permutations, product
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "code"))

import transformation_kinds as tk
import admissibility as adm
import search as srch

PHI = (1.0 + math.sqrt(5.0)) / 2.0
INVPHI = 1.0 / PHI


def _is_even_perm(p):
    sign = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                sign = -sign
    return sign == 1


def generate_v600():
    verts = []
    for i in range(4):
        for s in (1, -1):
            v = [0.0] * 4
            v[i] = float(s)
            verts.append(np.array(v))
    for signs in product((1, -1), repeat=4):
        verts.append(np.array(signs, dtype=float) / 2.0)
    base = (0.0, 1.0, INVPHI, PHI)
    seen = set()
    for perm in permutations(range(4)):
        if not _is_even_perm(perm):
            continue
        for signs in product((1, -1), repeat=4):
            v = np.zeros(4)
            for slot in range(4):
                v[slot] = signs[slot] * base[perm[slot]] / 2.0
            key = tuple(round(float(x), 9) for x in v)
            if key in seen:
                continue
            if abs(np.dot(v, v) - 1.0) > 1e-8:
                continue
            seen.add(key)
            verts.append(v.copy())
    return np.array(verts)


def build_a1(verts, tol=1e-6):
    n = len(verts)
    min_d2 = math.inf
    for i in range(n):
        for j in range(i + 1, n):
            d2 = float(np.dot(verts[i] - verts[j], verts[i] - verts[j]))
            if 1e-10 < d2 < min_d2:
                min_d2 = d2
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            d2 = float(np.dot(verts[i] - verts[j], verts[i] - verts[j]))
            if abs(d2 - min_d2) < tol:
                A[i, j] = 1.0
    return A


def main():
    print("=" * 70)
    print("TRANSLATION ENGINE v2: search for T on V_600's 26-dim block")
    print("=" * 70)

    print("\n[1] Build V_600 + extract 26-dim Galois-paired block...")
    verts = generate_v600()
    A1 = build_a1(verts)
    eigvals, eigvecs = np.linalg.eigh(A1)

    rational_a1 = [12.0, 3.0, 0.0, -2.0, -3.0]
    P_paired_cols = []
    for k in range(len(eigvals)):
        if not any(abs(eigvals[k] - r) < 1e-5 for r in rational_a1):
            P_paired_cols.append(eigvecs[:, k])
    V_paired = np.array(P_paired_cols).T  # 120 x 26
    A1_block = V_paired.T @ A1 @ V_paired
    A1_block = 0.5 * (A1_block + A1_block.T)
    print(f"  A1_block shape: {A1_block.shape}")

    print("\n[2] Apply MODULAR_EMBED transformation...")
    me_outcome = tk.modular_embed({"substrate": "V_600",
                                    "block_dim": 26,
                                    "level": 1})
    print(f"  -> {me_outcome.output_summary}")
    print(f"  -> admissibility = {me_outcome.admissibility.value}")

    print("\n[3] Apply HECKE_LIFT for primes p = 2, 3, 5, 7, 11, 13, "
          "17, 19, 23, 29, 31, 37...")
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    hecke_outcomes = []
    for p in primes:
        out = tk.hecke_lift(eigvals, p, representation_dim=26)
        hecke_outcomes.append((p, out))
        print(f"  T_{p}: kind={out.output_summary.split('=')[-1].strip()}")

    print("\n[4] Apply ANALYTIC_EXTEND to A1_block spectrum...")
    ae = tk.analytic_extend(np.linalg.eigvalsh(A1_block),
                             truncation_level=50)
    print(f"  -> {ae.output_summary}")
    print(f"  -> admissibility = {ae.admissibility.value}")

    print("\n[5] Apply SPECTRAL_LIFT_INFINITE to A1_block...")
    sli = tk.spectral_lift_infinite(A1_block, truncation_N=10)
    print(f"  -> {sli.output_summary}")

    print("\n[6] Run search over compositions...")
    print(f"  Target: first {len(adm.GAMMAS)} Riemann gamma_n values")
    print(f"  Composition pool: base operator A1_block, "
          f"plus T_p for p in {primes}")

    candidates = srch.search_compositions(
        A1_block,
        primes_to_try=primes,
        max_compositions=4,
        target_eigs=adm.GAMMAS,
        report_top_k=15,
    )

    print(f"\n[7] Top {len(candidates)} candidates by SPECTRAL_MATCH RMSE:")
    print(f"  {'rank':<5} {'RMSE':<12} {'verdict':<12} composition")
    print(f"  " + "-" * 64)
    for i, c in enumerate(candidates):
        comp = " | ".join(c.composition_steps)
        print(f"  {i+1:<5} {c.spectral_match_rmse:<12.4f} "
              f"{c.spectral_match_verdict:<12} {comp}")

    print()
    print("[8] Interpretation:")
    best = candidates[0]
    print(f"  Best fit: '{' | '.join(best.composition_steps)}'")
    print(f"  RMSE = {best.spectral_match_rmse:.4f}")
    print(f"  Verdict = {best.spectral_match_verdict}")
    print()
    print("  The search reports the best COMPOSITION found within the")
    print("  current transformation grammar.  An EXACT verdict would")
    print("  indicate a true Hilbert-Polya construction.  A CANDIDATE")
    print("  verdict indicates structural alignment but not exact match.")
    print("  A BROKEN verdict confirms the grammar in its current form")
    print("  cannot produce gamma_n.")
    print()
    print("  Next: extend the grammar with explicit Hecke matrix")
    print("  elements computed from Hilbert modular forms over Q(sqrt 5),")
    print("  Hecke commutation checks, and verifiable analytic")
    print("  continuation.  Each extension is a well-scoped piece of")
    print("  research work.")

    # Save outcomes
    outputs_dir = HERE.parent / "outputs"
    outputs_dir.mkdir(parents=True, exist_ok=True)
    with open(outputs_dir / "search_results.txt", "w") as f:
        f.write("Translation Engine v2 -- V_600 search results\n")
        f.write("=" * 60 + "\n")
        for i, c in enumerate(candidates):
            f.write(f"#{i+1}  RMSE = {c.spectral_match_rmse:.4f}  "
                    f"verdict = {c.spectral_match_verdict}\n")
            f.write(f"     composition: "
                    f"{' | '.join(c.composition_steps)}\n")
            for note in c.notes:
                f.write(f"     note: {note}\n")
            f.write("\n")


if __name__ == "__main__":
    main()
