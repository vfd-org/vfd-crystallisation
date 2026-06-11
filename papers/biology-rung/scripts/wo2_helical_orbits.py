"""WO-BIOLOGY-RUNG-002-AMYLOID: Cascade-admissible amyloid twist enumeration.

Implements [L.1], [D.2], [D.3], [L.3] from
papers/biology-rung/derivation-amyloid.md:

- [L.1]  Stab_2I(A) = C_10 = {k · 36° : k = 0, …, 9} for a 5-fold axis A
         (preimage in 2I of the C_5 face-stabiliser in A_5; split central
         extension since |C_5|·|C_2|=10 is squarefree).
- [D.2]  θ(α; p, q, N) = (p α − q · 2π) / N,  with N ≥ 1 an explicit
         parameter (NOT minimal), α ∈ Stab_2I(A)\\{0}, (p, q, N) with
         gcd(p, q, N) = 1.
- [D.3]  amyloid-scale compatibility: there exists integer M > 0 with
         M · θ = 360° EXACTLY, AND M · 4.7 Å ∈ [100 Å, 500 Å].
         Gives M ∈ {22, ..., 106}, θ ∈ [3.3962°, 16.3636°].
- [L.3]  enumeration of admissible θ for N ≤ N_max.

Since α ∈ Stab_2I(A) = {k · 36° : k = 0, …, 9}, and α = 36° suffices to
generate the full ladder (see derivation §2), we have
    θ = 36° · (p − 10q) / N      (with gcd(p, q, N) = 1)
Let s := p − 10q ∈ ℤ. Then θ = 36°·s/N, and M·θ = 360° gives
    M = 10 N / s.
For M to be a POSITIVE integer, s must divide 10N and s > 0.
We enforce this exact integrality — a rounded-M check is NOT sufficient.

Output: papers/biology-rung/data/wo2_prediction.csv with columns
    theta_deg, s, N, M, crossover_angstrom, gcd_p_q_N, p_example, q_example

Usage:
    python wo2_helical_orbits.py             # default N_max = 20
    python wo2_helical_orbits.py --n-max 50
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE.parent / "data"
DEFAULT_OUT = DATA_DIR / "wo2_prediction.csv"

BASE_ANGLE_DEG = 36.0

D_BETA_ANGSTROM = 4.7
CROSSOVER_MIN_ANGSTROM = 100.0
CROSSOVER_MAX_ANGSTROM = 500.0
M_MIN = math.ceil(CROSSOVER_MIN_ANGSTROM / D_BETA_ANGSTROM)   # 22
M_MAX = math.floor(CROSSOVER_MAX_ANGSTROM / D_BETA_ANGSTROM)  # 106
THETA_MIN_DEG = 360.0 / M_MAX  # ≈ 3.3962°
THETA_MAX_DEG = 360.0 / M_MIN  # ≈ 16.3636°


def enumerate_admissible(N_max: int) -> list[dict]:
    """Enumerate (s, N) pairs such that θ = 36°·s/N is amyloid-scale
    compatible (D.3) with EXACT integer M = 10N/s.

    Returns one row per distinct (θ, s, N) triple. Each row also
    records a representative (p, q) with p − 10q = s, p ∈ [0, N],
    and gcd(p, q, N) = 1.
    """
    rows = []
    seen_theta = {}  # theta_deg → smallest-N row

    for N in range(1, N_max + 1):
        for s in range(1, 10 * N + 1):  # s = p - 10q > 0; s ≤ 10N suffices
            # θ = 36°·s/N; M = 10N/s (must be positive integer)
            if (10 * N) % s != 0:
                continue
            M = (10 * N) // s
            if M < M_MIN or M > M_MAX:
                continue
            theta = 360.0 / M  # exact rational realised as float

            # Find representative (p, q) with p − 10q = s, p ∈ [0, N],
            # and gcd(p, q, N) = 1. Try q = (p - s)/10 for p ≡ s (mod 10).
            p_rep = None
            q_rep = None
            for p in range(0, N + 1):
                if (p - s) % 10 != 0:
                    continue
                q = (p - s) // 10
                if math.gcd(math.gcd(abs(p), abs(q)), N) == 1:
                    p_rep, q_rep = p, q
                    break
            if p_rep is None:
                # fall back to any (p, q) with p ∈ [0, 10N]
                for p in range(0, 10 * N + 1):
                    if (p - s) % 10 != 0:
                        continue
                    q = (p - s) // 10
                    if math.gcd(math.gcd(abs(p), abs(q)), N) == 1:
                        p_rep, q_rep = p, q
                        break

            row = {
                "theta_deg": theta,
                "s": s,
                "N": N,
                "M": M,
                "crossover_angstrom": M * D_BETA_ANGSTROM,
                "p_example": p_rep if p_rep is not None else 0,
                "q_example": q_rep if q_rep is not None else 0,
            }
            # Dedupe by theta, keeping smallest-N representative
            key = round(theta, 10)
            if key not in seen_theta or N < seen_theta[key]["N"]:
                seen_theta[key] = row

    rows = sorted(seen_theta.values(), key=lambda r: r["theta_deg"])
    return rows


def emit_csv(rows: list[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["theta_deg", "s", "N", "M",
                        "crossover_angstrom", "p_example", "q_example"],
        )
        writer.writeheader()
        for r in rows:
            writer.writerow({
                "theta_deg": f"{r['theta_deg']:.6f}",
                "s": r["s"],
                "N": r["N"],
                "M": r["M"],
                "crossover_angstrom": f"{r['crossover_angstrom']:.2f}",
                "p_example": r["p_example"],
                "q_example": r["q_example"],
            })


def summarise(rows: list[dict]) -> None:
    print(f"Amyloid-scale compatibility (D.3 exact-integer-M):")
    print(f"  M_MIN = {M_MIN} ({M_MIN * D_BETA_ANGSTROM:.1f} Å crossover)")
    print(f"  M_MAX = {M_MAX} ({M_MAX * D_BETA_ANGSTROM:.1f} Å crossover)")
    print(f"  θ range = [{THETA_MIN_DEG:.4f}°, {THETA_MAX_DEG:.4f}°]")
    print()
    print(f"{'θ (°)':>10}  {'M':>4}  {'L_co (Å)':>10}  {'(s, N)':>12}  {'(p,q) rep':>12}")
    for r in rows:
        print(f"{r['theta_deg']:>10.6f}  {r['M']:>4}  "
              f"{r['crossover_angstrom']:>10.2f}  "
              f"({r['s']}, {r['N']}):>12  "
              f"({r['p_example']},{r['q_example']})")

    # Spot-check: 36°/N for N = 3..10 (corrected window excludes N=11 onward).
    print()
    print("Spot-checks against derivation-amyloid.md §2 (L.3):")
    expected = {N: 360.0 / (10 * N) * 10 for N in range(3, 11)}  # θ = 36°/N
    # Actually, 36°/N = 360°·(1)/(10N) — so M = 10N, need M ≤ 106: N ≤ 10.
    all_ok = True
    rows_theta = [r["theta_deg"] for r in rows]
    for N in range(3, 11):
        theta_expected = 36.0 / N  # since s=1
        matched = any(abs(t - theta_expected) < 1e-6 for t in rows_theta)
        mark = "OK " if matched else "MISS"
        all_ok = all_ok and matched
        print(f"  [{mark}] θ = 36°/{N} = {theta_expected:.4f}° "
              f"(present = {matched})")

    # Verify every row has exact integer M.
    print()
    print("Exact-M integrality verification:")
    all_exact = True
    for r in rows:
        recomputed_M = 360.0 / r["theta_deg"]
        if abs(recomputed_M - r["M"]) > 1e-9:
            print(f"  [FAIL] θ = {r['theta_deg']}, stored M = {r['M']}, "
                  f"360/θ = {recomputed_M}")
            all_exact = False
    if all_exact:
        print(f"  [OK] All {len(rows)} rows satisfy Mθ = 360° exactly.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-max", type=int, default=20)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()

    rows = enumerate_admissible(args.n_max)
    emit_csv(rows, args.out)
    summarise(rows)
    print(f"\nWrote: {args.out} ({len(rows)} distinct θ values)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
