"""WO-BIOLOGY-RUNG-001-CAPSID: T-number prediction sim.

Implements [L.1] and [D.3] from
papers/biology-rung/derivation-capsid.md:

- [L.1]  spec(𝒯_casc) = Loeschian numbers; enumerate (h, k) ∈ ℤ²
        and compute T = h² + hk + k².
- [D.3]  μ(T) = number of C_6-orbits on {(h, k) ∈ ℤ² \\ {0} : T(h,k) = T}.
        C_6 acts on ℤ[ω] by multiplication by the six Eisenstein units
        (ω = e^{iπ/3}); in (h, k) coordinates, ω sends (h, k) ↦ (-k, h+k).

Output: papers/biology-rung/data/wo1_prediction.csv with columns
    T, mu, representative, chirality
one row per C_6 orbit (so Loeschian `T` values with μ(T) > 1 occupy
multiple rows). `representative` is the canonical (h, k) with
h ≥ 0, k ≥ 0, maximal h (see `canonical_rep`). `chirality` is
"achiral" when the representative lies on a hexagonal-lattice
reflection axis (k = 0 or h = k) and "chiral" otherwise.

Also emits a human-readable summary to stdout with μ spot-checks
against the values stated in derivation-capsid.md §5.

Usage:
    python wo1_capsid_predict.py             # default T_max = 100
    python wo1_capsid_predict.py --t-max 400
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def T_of(h: int, k: int) -> int:
    """Caspar-Klug / Eisenstein norm T = h² + hk + k²."""
    return h * h + h * k + k * k


def omega_action(hk: tuple[int, int]) -> tuple[int, int]:
    """Action of ω (primitive sixth root) on (h, k): (h,k) ↦ (-k, h+k).

    Derivation: ω satisfies ω² = ω − 1 (minimal poly x² − x + 1 over ℚ).
    For z = h + kω, ωz = hω + kω² = hω + k(ω − 1) = -k + (h + k)ω.
    So (h, k) ↦ (-k, h + k).
    """
    h, k = hk
    return (-k, h + k)


def c6_orbit(hk: tuple[int, int]) -> frozenset[tuple[int, int]]:
    """The C_6 orbit of (h, k) under repeated ω-action.

    The unit group of ℤ[ω] is {1, ω, ω², −1, −ω, −ω²} ≅ C_6, so the
    orbit has at most six elements. Fixed points of ω: only (0, 0).
    """
    orbit: set[tuple[int, int]] = set()
    current = hk
    for _ in range(6):
        orbit.add(current)
        current = omega_action(current)
    return frozenset(orbit)


def canonical_rep(orbit: frozenset[tuple[int, int]]) -> tuple[int, int]:
    """Pick a canonical representative of an orbit: (h, k) with h ≥ 0,
    k ≥ 0, maximal h among such."""
    cands = [p for p in orbit if p[0] >= 0 and p[1] >= 0]
    if not cands:
        # Should not happen except for (0,0); fall back to max by tuple.
        cands = list(orbit)
    # Prefer larger h (puts the rep on the h-axis side for chirality labeling).
    cands.sort(key=lambda p: (-p[0], -p[1]))
    return cands[0]


def enumerate_orbits(T_max: int) -> dict[int, list[frozenset[tuple[int, int]]]]:
    """Return {T: [orbit₁, orbit₂, ...]} for all Loeschian T ≤ T_max.

    Enumeration bound: if T(h, k) ≤ T_max with h, k ≥ 0, then h ≤ sqrt(T_max)
    and k ≤ sqrt(T_max). We scan (h, k) in [0, sqrt(T_max)]² and take C_6
    orbits over ℤ[ω]; any orbit representative with T ≤ T_max is hit by
    some non-negative (h, k) because (-k, h+k) has h' = -k ≤ 0 when k > 0.
    Specifically, each C_6 orbit contains a representative in the closed
    wedge {h ≥ 0, k ≥ 0} (the fundamental domain for C_6 on the Eisenstein
    plane), so enumeration over that wedge is complete.
    """
    import math

    bound = int(math.isqrt(T_max)) + 1
    seen_orbits: set[frozenset[tuple[int, int]]] = set()
    per_T: dict[int, list[frozenset[tuple[int, int]]]] = defaultdict(list)

    for h in range(0, bound + 1):
        for k in range(0, bound + 1):
            if h == 0 and k == 0:
                continue
            t = T_of(h, k)
            if t > T_max:
                continue
            orbit = c6_orbit((h, k))
            if orbit in seen_orbits:
                continue
            seen_orbits.add(orbit)
            per_T[t].append(orbit)

    return dict(per_T)


def mu(orbit_table: dict[int, list], T: int) -> int:
    return len(orbit_table.get(T, []))


def _orbit_chirality(rep: tuple[int, int]) -> str:
    """Classify a single C_6-orbit by its canonical representative.

    An orbit is *achiral* if the representative lies on a reflection
    axis of the hexagonal lattice: either k == 0 (the real/h-axis)
    or h == k (the k = h diagonal). Equivalently, the orbit is fixed
    under the h ↔ k reflection, so it coincides with its mirror under
    D_6 = C_6 ⋊ reflection, making laevo and dextro indistinguishable.

    Otherwise the orbit is *chiral* — swapping h ↔ k gives a distinct
    C_6-orbit (the mirror) and the orbit is one member of a
    laevo/dextro pair.

    Canonical representatives with h ≥ 0, k ≥ 0 (from canonical_rep)
    make this a simple predicate on (h, k).
    """
    h, k = rep
    if k == 0 or h == k:
        return "achiral"
    return "chiral"


def write_prediction_csv(
    orbit_table: dict[int, list[frozenset[tuple[int, int]]]],
    out_path: Path,
) -> None:
    """Emit per-orbit rows, one per C_6 orbit.

    This is deliberately PER-ORBIT rather than per-T, because at T
    with multiple orbits (e.g. T=49 with μ=3: one achiral + one
    chiral pair) the T-level chirality label is ambiguous.
    """
    rows = []
    for T in sorted(orbit_table.keys()):
        orbits = orbit_table[T]
        mu_T = len(orbits)
        for orbit in orbits:
            rep = canonical_rep(orbit)
            rows.append((T, mu_T, f"({rep[0]},{rep[1]})", _orbit_chirality(rep)))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["T", "mu", "representative", "chirality"])
        writer.writerows(rows)


def summarise(orbit_table: dict, T_max: int) -> None:
    loeschians = sorted(orbit_table.keys())
    total_orbits = sum(len(v) for v in orbit_table.values())
    print(f"T_max = {T_max}")
    print(f"Loeschian numbers ≤ {T_max}: {len(loeschians)}")
    print(f"Total C_6 orbits ≤ {T_max}: {total_orbits}")
    print()
    print(f"{'T':>4}  {'mu':>3}  reps")
    for T in loeschians[:40]:
        reps = [canonical_rep(o) for o in orbit_table[T]]
        reps_str = ", ".join(f"({h},{k})" for h, k in reps)
        print(f"{T:>4}  {len(reps):>3}  {reps_str}")
    if len(loeschians) > 40:
        print(f"  ... ({len(loeschians) - 40} more)")

    # Spot-check expected values from derivation-capsid.md §5 (D.3 table).
    # Includes the novel μ(91) = 4 emergent result (91 = 7 × 13, both
    # chiral Loeschian primes).
    expected = {
        1: 1, 3: 1, 4: 1, 7: 2, 9: 1, 12: 1, 13: 2, 16: 1,
        19: 2, 21: 2, 25: 1, 27: 1, 28: 2, 31: 2, 37: 2, 39: 2,
        49: 3,
        91: 4,   # novel emergent result, see derivation-capsid.md §5
    }
    print()
    print("Spot-checks against derivation-capsid.md §5:")
    all_ok = True
    for T, mu_expected in sorted(expected.items()):
        mu_actual = mu(orbit_table, T)
        ok = mu_actual == mu_expected
        all_ok = all_ok and ok
        mark = "OK " if ok else "FAIL"
        print(f"  [{mark}] mu({T}) expected={mu_expected} actual={mu_actual}")
    if not all_ok:
        raise SystemExit("Spot-check failure — derivation and sim disagree.")
    # Also confirm forbidden values absent
    forbidden = [2, 5, 6, 8, 10, 11, 14, 15, 17, 18, 20]
    print()
    print("Forbidden-T spot-checks (must have mu=0):")
    for T in forbidden:
        assert T not in orbit_table, f"T={T} unexpectedly present"
        print(f"  [OK ] T={T} absent (non-Loeschian)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--t-max", type=int, default=100,
                    help="Maximum T to enumerate (default 100)")
    ap.add_argument("--out", type=Path,
                    default=Path(__file__).resolve().parent.parent / "data" / "wo1_prediction.csv",
                    help="Output CSV path")
    args = ap.parse_args()

    orbit_table = enumerate_orbits(args.t_max)
    summarise(orbit_table, args.t_max)
    write_prediction_csv(orbit_table, args.out)
    print(f"\nWrote: {args.out}")


if __name__ == "__main__":
    main()
