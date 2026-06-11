#!/usr/bin/env python3
"""
Exact B1/B2 verifier for H-grad-1.

This script implements the finite checks requested in
TASK-h-grad-1-b1b2-sim.md:

* build the 120 unit icosians in Q(phi)^4,
* use an explicit eight-unit Z-basis for their Z-span,
* decompose every unit icosian in that basis using exact rational
  Gaussian elimination,
* compute q([x]) = Tr_{Q(phi)/Q}(N(x)) mod 2 on I / 2I_lat.

No floating point arithmetic is used.

The task spec originally stated the classical E_8/2E_8 counts as
"120 isotropic / 135 anisotropic", which reversed the standard numbers.
The correct counts (Conway-Sloane Ch. 8) are 135 nonzero isotropic +
120 anisotropic + 1 zero = 256. The script expects and verifies the
correct totals. Similarly the 120 unit icosians collapse to exactly
60 distinct nonzero isotropic mod-2 classes because u == -u mod 2I_lat;
the script expects 60 (not 120).
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
import sys
from typing import List, Sequence, Tuple


@dataclass(frozen=True)
class ZPhi:
    """Element a + b*phi of Q(phi), with phi^2 = phi + 1."""

    a: Fraction
    b: Fraction

    def __add__(self, other: ZPhi) -> ZPhi:
        return ZPhi(self.a + other.a, self.b + other.b)

    def __sub__(self, other: ZPhi) -> ZPhi:
        return ZPhi(self.a - other.a, self.b - other.b)

    def __neg__(self) -> ZPhi:
        return ZPhi(-self.a, -self.b)

    def __mul__(self, other: ZPhi | int) -> ZPhi:
        if isinstance(other, int):
            return ZPhi(other * self.a, other * self.b)
        return ZPhi(
            self.a * other.a + self.b * other.b,
            self.a * other.b + self.b * other.a + self.b * other.b,
        )

    def __rmul__(self, other: int) -> ZPhi:
        return self * other

    def is_zphi_integer(self) -> bool:
        return self.a.denominator == 1 and self.b.denominator == 1


ZERO = ZPhi(Fraction(0), Fraction(0))
ONE = ZPhi(Fraction(1), Fraction(0))
PHI = ZPhi(Fraction(0), Fraction(1))
HALF = ZPhi(Fraction(1, 2), Fraction(0))

Quat = Tuple[ZPhi, ZPhi, ZPhi, ZPhi]
Matrix = List[List[Fraction]]


def z(a: int | Fraction, b: int | Fraction = 0) -> ZPhi:
    return ZPhi(Fraction(a), Fraction(b))


def fmt_frac(x: Fraction) -> str:
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def fmt_zphi(x: ZPhi) -> str:
    parts: list[str] = []
    if x.a:
        parts.append(fmt_frac(x.a))
    if x.b:
        coeff = fmt_frac(abs(x.b))
        sign = "-" if x.b < 0 else "+"
        term = "phi" if abs(x.b) == 1 else f"{coeff}*phi"
        if parts:
            parts.append(f"{sign} {term}")
        else:
            parts.append(f"-{term}" if x.b < 0 else term)
    return " ".join(parts) if parts else "0"


def fmt_quat(q: Quat) -> str:
    labels = ("", "i", "j", "k")
    return "(" + ", ".join(
        f"{label}:{fmt_zphi(comp)}" if label else fmt_zphi(comp)
        for label, comp in zip(labels, q)
    ) + ")"


def qadd(p: Quat, q: Quat) -> Quat:
    return tuple(p[i] + q[i] for i in range(4))  # type: ignore[return-value]


def qneg(q: Quat) -> Quat:
    return tuple(-c for c in q)  # type: ignore[return-value]


def qscale(n: int, q: Quat) -> Quat:
    return tuple(n * c for c in q)  # type: ignore[return-value]


def qnorm(q: Quat) -> ZPhi:
    out = ZERO
    for c in q:
        out = out + c * c
    return out


def quat_trace(q: Quat) -> ZPhi:
    return 2 * q[0]


def field_trace(x: ZPhi) -> Fraction:
    return 2 * x.a + x.b


def qkey(q: Quat) -> tuple[tuple[Fraction, Fraction], ...]:
    return tuple((c.a, c.b) for c in q)


def permutation_parity(p: Sequence[int]) -> int:
    inv = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                inv += 1
    return inv & 1


def build_unit_icosians() -> list[Quat]:
    """Conway-Sloane 8 + 16 + 96 unit icosian list."""

    units: list[Quat] = []

    for axis in range(4):
        for sign in (1, -1):
            q = [ZERO, ZERO, ZERO, ZERO]
            q[axis] = z(sign)
            units.append(tuple(q))  # type: ignore[arg-type]

    for signs in product((1, -1), repeat=4):
        units.append(tuple(z(Fraction(s, 2)) for s in signs))  # type: ignore[arg-type]

    entries = [ZERO, HALF, PHI * HALF, (PHI - ONE) * HALF]
    seen: set[tuple[tuple[Fraction, Fraction], ...]] = set()
    for perm in permutations(range(4)):
        if permutation_parity(perm) != 0:
            continue
        base = [entries[perm[i]] for i in range(4)]
        nonzero = [i for i, c in enumerate(base) if c != ZERO]
        for signs in product((1, -1), repeat=len(nonzero)):
            q = list(base)
            for idx, sign in zip(nonzero, signs):
                if sign < 0:
                    q[idx] = -q[idx]
            key = qkey(tuple(q))  # type: ignore[arg-type]
            if key not in seen:
                seen.add(key)
                units.append(tuple(q))  # type: ignore[arg-type]

    return units


def quat_from_scaled_row(row: Sequence[int]) -> Quat:
    if len(row) != 8:
        raise ValueError("scaled row must have eight entries")
    return tuple(
        ZPhi(Fraction(row[2 * i], 2), Fraction(row[2 * i + 1], 2))
        for i in range(4)
    )  # type: ignore[return-value]


# Rows are 2*(a,b,a_i,b_i,...) coordinates for eight unit icosians.
# This is an explicit eight-unit Z-basis of the Z-span of the 120 units.
BASIS_ROWS: tuple[tuple[int, ...], ...] = (
    (2, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 2, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 2, 0, 0, 0),
    (0, 0, -1, 0, 0, 1, -1, 1),
    (-1, 1, 0, 1, 1, 0, 0, 0),
    (0, 0, 1, -1, 1, 0, 0, -1),
    (0, -1, 0, 0, 1, 0, 1, -1),
    (-1, 1, 1, 0, 0, 0, 0, 1),
)
BASIS: tuple[Quat, ...] = tuple(quat_from_scaled_row(row) for row in BASIS_ROWS)


def embed_scaled(q: Quat) -> list[Fraction]:
    out: list[Fraction] = []
    for c in q:
        out.extend([2 * c.a, 2 * c.b])
    return out


def basis_column_matrix() -> Matrix:
    return [
        [Fraction(BASIS_ROWS[col][row]) for col in range(8)]
        for row in range(8)
    ]


def determinant(matrix: Matrix) -> Fraction:
    a = [row[:] for row in matrix]
    n = len(a)
    det = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        pivot_value = a[col][col]
        det *= pivot_value
        for r in range(col + 1, n):
            factor = a[r][col] / pivot_value
            if factor == 0:
                continue
            for c in range(col, n):
                a[r][c] -= factor * a[col][c]
    return det


def inverse(matrix: Matrix) -> Matrix:
    n = len(matrix)
    a = [
        matrix[r][:] + [Fraction(1 if r == c else 0) for c in range(n)]
        for r in range(n)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] != 0), None)
        if pivot is None:
            raise ValueError("singular matrix")
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
        pivot_value = a[col][col]
        for c in range(2 * n):
            a[col][c] /= pivot_value
        for r in range(n):
            if r == col:
                continue
            factor = a[r][col]
            if factor == 0:
                continue
            for c in range(2 * n):
                a[r][c] -= factor * a[col][c]
    return [row[n:] for row in a]


def mat_vec_mul(matrix: Matrix, vector: Sequence[Fraction]) -> list[Fraction]:
    return [sum(row[i] * vector[i] for i in range(len(vector))) for row in matrix]


def matrix_rank(rows: Matrix) -> int:
    a = [row[:] for row in rows]
    rank = 0
    nrows = len(a)
    ncols = len(a[0]) if a else 0
    for col in range(ncols):
        pivot = next((r for r in range(rank, nrows) if a[r][col] != 0), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        pivot_value = a[rank][col]
        for c in range(col, ncols):
            a[rank][c] /= pivot_value
        for r in range(nrows):
            if r == rank:
                continue
            factor = a[r][col]
            if factor == 0:
                continue
            for c in range(col, ncols):
                a[r][c] -= factor * a[rank][c]
        rank += 1
        if rank == nrows:
            break
    return rank


def coords_in_basis(q: Quat, basis_inverse: Matrix) -> list[Fraction]:
    return mat_vec_mul(basis_inverse, embed_scaled(q))


def lift_bits(bits: Sequence[int]) -> Quat:
    out: Quat = (ZERO, ZERO, ZERO, ZERO)
    for bit, basis_q in zip(bits, BASIS):
        if bit:
            out = qadd(out, basis_q)
    return out


def q_mod2(bits: Sequence[int]) -> int:
    trace = field_trace(qnorm(lift_bits(bits)))
    if trace.denominator != 1:
        raise ArithmeticError(f"nonintegral trace for {tuple(bits)}: {trace}")
    return int(trace) & 1


def mod2_class(coords: Sequence[Fraction]) -> tuple[int, ...]:
    if any(c.denominator != 1 for c in coords):
        raise ArithmeticError(f"nonintegral coordinates: {coords}")
    return tuple(int(c) & 1 for c in coords)


def verify_b1(units: list[Quat], basis_inverse: Matrix) -> tuple[bool, list[list[Fraction]]]:
    unit_keys = {qkey(u) for u in units}
    basis_membership = all(qkey(b) in unit_keys for b in BASIS)
    basis_unit_norms = all(qnorm(b) == ONE for b in BASIS)
    basis_integral_traces = all(quat_trace(b).is_zphi_integer() for b in BASIS)

    coord_rows: list[list[Fraction]] = []
    bad: list[tuple[int, Quat, list[Fraction]]] = []
    for idx, unit in enumerate(units):
        coords = coords_in_basis(unit, basis_inverse)
        coord_rows.append(coords)
        if any(c.denominator != 1 for c in coords):
            bad.append((idx, unit, coords))

    coeff_rank = matrix_rank(coord_rows)
    ok = (
        len(units) == 120
        and basis_membership
        and basis_unit_norms
        and basis_integral_traces
        and not bad
        and coeff_rank == 8
    )

    print("=== B1 - Z-basis of icosian ring I ===")
    print("Basis B_I = {omega_1, ..., omega_8}:")
    for idx, basis_q in enumerate(BASIS, start=1):
        print(f"  omega_{idx} = {fmt_quat(basis_q)}")
    print()
    print(f"Unit-icosian list size: {len(units)} / 120 - {'PASS' if len(units) == 120 else 'FAIL'}")
    print(f"Basis elements are unit icosians: {'PASS' if basis_membership and basis_unit_norms else 'FAIL'}")
    print(f"Basis quaternion traces lie in Z[phi]: {'PASS' if basis_integral_traces else 'FAIL'}")
    print(f"120x8 coefficient matrix rank over Q: {coeff_rank} / 8 - {'PASS' if coeff_rank == 8 else 'FAIL'}")
    print(
        "Unit-icosian decomposition check: "
        f"{120 - len(bad)} / 120 decompose as integer combinations - "
        f"{'PASS' if not bad else 'FAIL'}"
    )
    if bad:
        for idx, unit, coords in bad[:5]:
            print(f"  first bad unit #{idx}: {fmt_quat(unit)} coords={coords}")
    print()
    return ok, coord_rows


def polar_form_rank() -> int:
    """Rank over F_2 of the polar form b(x,y) = q(x+y) - q(x) - q(y).
    For E_8/2E_8, b is non-degenerate (rank 8, Arf invariant 0)."""
    # Compute the 8x8 Gram matrix of b on the standard basis e_1,...,e_8.
    e = [[1 if i == j else 0 for j in range(8)] for i in range(8)]
    gram = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            xi_plus_ej = tuple((e[i][k] ^ e[j][k]) for k in range(8))
            gram[i][j] = (q_mod2(xi_plus_ej) ^ q_mod2(tuple(e[i])) ^ q_mod2(tuple(e[j]))) & 1
    # Gaussian elimination over F_2.
    m = [row[:] for row in gram]
    rank = 0
    r = 0
    for c in range(8):
        pivot = None
        for i in range(r, 8):
            if m[i][c] == 1:
                pivot = i
                break
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        for i in range(8):
            if i != r and m[i][c] == 1:
                m[i] = [(m[i][k] ^ m[r][k]) & 1 for k in range(8)]
        rank += 1
        r += 1
    return rank


def verify_b2(coord_rows: list[list[Fraction]]) -> tuple[bool, bool]:
    counts = {0: 0, 1: 0}
    for bits in product((0, 1), repeat=8):
        counts[q_mod2(bits)] += 1

    zero_vector_count = 1
    nonzero_isotropic = counts[0] - 1
    anisotropic = counts[1]
    # E_8 / 2E_8 classical F_2-quadratic totals (Conway-Sloane Ch. 8):
    # 1 zero + 135 isotropic + 120 anisotropic = 256. The Z[phi]-trace form
    # on I / 2I_lat realises this via the icosian <-> E_8 identification.
    expected_counts = (1, 135, 120)
    actual_counts = (zero_vector_count, nonzero_isotropic, anisotropic)
    b2_ok = actual_counts == expected_counts
    # Non-degeneracy: polar form of q has F_2-rank 8 (Arf invariant 0).
    polar_rank = polar_form_rank()
    polar_ok = polar_rank == 8

    unit_classes = [mod2_class(coords) for coords in coord_rows]
    distinct_unit_classes = set(unit_classes)
    zero_class = (0,) * 8
    all_unit_classes_nonzero = zero_class not in distinct_unit_classes
    all_unit_classes_isotropic = all(q_mod2(bits) == 0 for bits in distinct_unit_classes)
    # u and -u reduce to the same class modulo 2I_lat, so 120 units
    # collapse to 60 distinct nonzero isotropic classes. This is a
    # correct classical fact, not a failure.
    expected_distinct_unit_classes = 60
    sanity_ok = (
        len(distinct_unit_classes) == expected_distinct_unit_classes
        and all_unit_classes_nonzero
        and all_unit_classes_isotropic
    )

    print("=== B2 - Mod-2 quadratic form on I/2I_lat ===")
    print("Quadratic form: q([x]) = Tr_{Q(phi)/Q}(N(x)) mod 2")
    print()
    print(
        f"Classical totals (expected 1 + 135 + 120 = 256 for E_8/2E_8):\n"
        f"  zero        = {zero_vector_count}  (expected 1)\n"
        f"  isotropic   = {nonzero_isotropic}  (expected 135)\n"
        f"  anisotropic = {anisotropic}  (expected 120)\n"
        f"  -> {'PASS' if b2_ok else 'FAIL'}"
    )
    if not b2_ok:
        print("  mismatch: recheck the trace form or the basis ordering.")
    print(
        f"Polar-form F_2-rank: {polar_rank} / 8 (expected 8, non-degenerate) - "
        f"{'PASS' if polar_ok else 'FAIL'}"
    )
    print()
    print("=== Sanity: unit-icosian mod-2 classes ===")
    print(
        f"120 unit icosians collapse to {len(distinct_unit_classes)} distinct "
        f"nonzero isotropic classes (expected 60, since u == -u mod 2I_lat) - "
        f"{'PASS' if sanity_ok else 'FAIL'}"
    )
    if not all_unit_classes_nonzero:
        print("  zero class occurs among unit reductions — unexpected")
    if not all_unit_classes_isotropic:
        print("  at least one unit class has q=1 — unexpected")
    print()
    return b2_ok and polar_ok, sanity_ok


def main() -> int:
    units = build_unit_icosians()
    basis_matrix = basis_column_matrix()
    det = determinant(basis_matrix)
    if det == 0:
        print("Basis matrix is singular - FAIL")
        return 1
    basis_inverse = inverse(basis_matrix)

    b1_ok, coord_rows = verify_b1(units, basis_inverse)
    b2_ok, sanity_ok = verify_b2(coord_rows)

    if b1_ok and b2_ok and sanity_ok:
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
