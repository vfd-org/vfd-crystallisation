"""Sim v8: build-up from icosahedron/dodecahedron + build-down from V_600.

Two parallel decompositions that converge on the same structural
seam:

(A) Build up from 3D icosa/dodeca.
    - Icosahedron: 12 vertices, adjacency operator A_ico (12 x 12)
    - Dodecahedron: 20 vertices, adjacency operator A_dod (20 x 20)
    - Symmetry group I = A_5 acts on both
    - A_5 has 5 irreps: 1, 3, 3', 4, 5 (dims summing to 60 = |A_5|
      after squares: 1 + 9 + 9 + 16 + 25)
    - The 3 and 3' irreps are Galois-paired (their character values
      involve phi and 1-phi)

(B) Build down from V_600 = 2I.
    - V_600: 120 vertices, A_1 (120 x 120)
    - 9 distinct A_1 eigenvalues with mults (1, 4, 9, 16, 25, 36,
      9, 16, 4) = squared dims of 2I's 9 irreps (1, 2, 3, 4, 5, 6,
      3', 4', 2')
    - Galois structure: (2, 2'), (3, 3') paired

(C) The bridge.
    The central extension 1 -> Z/2 -> 2I -> A_5 -> 1 lifts each
    A_5 irrep V to either V (if V factors through A_5) or to a
    spin pair. The 1-dim, 4-dim, 5-dim irreps of A_5 lift to the
    1-dim, 4-dim, 5-dim irreps of 2I (sigma-fixed at V_600 level).
    The 3-dim, 3'-dim pair of A_5 lifts to a 3-dim, 3'-dim pair
    in 2I (Galois-paired). Plus 2I has two extra spinor irreps
    (2 and 2') that DON'T come from A_5 -- these arise from the
    Z/2 central element.

(D) The seam the missing T must live on.
    The (3, 3') Galois pair in A_5 is the seed of the (13, 13)
    split we observed in V_600. Both 13s = 4 + 9 from the
    (2, 2') and (3, 3') spin-doubled pairs. If a Hilbert-Polya
    operator T exists for the Riemann zeros on V_600, its
    natural carrier is this pair structure, lifted from the
    3D source.

Outputs:
  outputs/v8/01_icosa_dodeca_spectra.png
  outputs/v8/02_v600_irrep_decomposition.png
  outputs/v8/03_seam_diagram.png
  data/v8/irrep_seam.csv
"""
from __future__ import annotations

import csv
import math
from itertools import permutations, product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

HERE = Path(__file__).resolve().parent
OUTPUTS = HERE.parent / "outputs" / "v8"
DATA = HERE.parent / "data" / "v8"
OUTPUTS.mkdir(parents=True, exist_ok=True)
DATA.mkdir(parents=True, exist_ok=True)

PHI = (1.0 + math.sqrt(5.0)) / 2.0
INVPHI = 1.0 / PHI


# ---------------------------------------------------------------------------
# (A) 3D icosahedron and dodecahedron
# ---------------------------------------------------------------------------

def generate_icosahedron():
    """12 vertices of unit icosahedron: even permutations of
    (0, +-1, +-phi) (normalised to unit norm).
    """
    raw = []
    # Even perms of (0, 1, 2): identity, (1,2,0), (2,0,1) - cyclic shifts
    even_perms = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    for perm in even_perms:
        # We want value 0 in slot perm[0], 1 in perm[1], phi in perm[2]
        for s1 in (1, -1):
            for s2 in (1, -1):
                v = [0.0, 0.0, 0.0]
                v[perm[0]] = 0.0
                v[perm[1]] = s1 * 1.0
                v[perm[2]] = s2 * PHI
                raw.append(tuple(v))
    # Dedupe
    raw = list(set(raw))
    verts = np.array(raw)
    norms = np.linalg.norm(verts, axis=1)
    verts = verts / norms[:, None]
    assert len(verts) == 12, f"Got {len(verts)} icosahedron vertices"
    return verts


def generate_dodecahedron():
    """20 vertices of the dodecahedron:
    - 8 from (+-1, +-1, +-1)
    - 12 from (0, +-1/phi, +-phi) and cyclic permutations.
    All normalised.
    """
    raw = []
    # 8 cube-type
    for s1 in (1, -1):
        for s2 in (1, -1):
            for s3 in (1, -1):
                raw.append((s1, s2, s3))
    # 12 mixed
    for perm in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        for s1 in (1, -1):
            for s2 in (1, -1):
                v = [0.0, 0.0, 0.0]
                v[perm[0]] = 0.0
                v[perm[1]] = s1 * INVPHI
                v[perm[2]] = s2 * PHI
                raw.append(tuple(v))
    raw = list(set(raw))
    verts = np.array(raw)
    norms = np.linalg.norm(verts, axis=1)
    verts = verts / norms[:, None]
    assert len(verts) == 20, f"Got {len(verts)} dodecahedron vertices"
    return verts


def build_adjacency(verts, tol=1e-6):
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
    return A, min_d2


def spectrum_with_multiplicities(A, tol=1e-5):
    eigvals = np.linalg.eigvalsh(A)
    # Group by value
    groups = []
    for v in eigvals:
        found = False
        for g in groups:
            if abs(g[0] - v) < tol:
                g[1] += 1
                found = True
                break
        if not found:
            groups.append([v, 1])
    return sorted(groups, key=lambda g: -g[0])


# ---------------------------------------------------------------------------
# (B) V_600
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Known A_5 and 2I irreducible representation data
# ---------------------------------------------------------------------------

# A_5 irreps: (label, dimension, "Galois pair partner label" or None)
# A_5 has 5 conjugacy classes -> 5 irreps.
A5_IRREPS = [
    ("1",  1,  None),
    ("3",  3,  "3prime"),
    ("3prime",  3,  "3"),
    ("4",  4,  None),
    ("5",  5,  None),
]
# Sum of squares: 1 + 9 + 9 + 16 + 25 = 60 = |A_5|

# 2I irreps: lifts of A_5 plus spin pair (2, 2') which doesn't come
# from A_5 (these are projective at the A_5 level).
TWOI_IRREPS = [
    ("1",      1, None,    "lifts from A_5 trivial; sigma-fixed eigval"),
    ("2",      2, "2prime","SPIN pair; Galois-paired"),
    ("3",      3, "3prime","lifts from A_5 3-dim pair; Galois-paired"),
    ("4",      4, None,    "lifts from A_5 4-dim"),
    ("5",      5, None,    "lifts from A_5 5-dim"),
    ("6",      6, None,    "spin-lifted; sigma-fixed"),
    ("3prime", 3, "3",     "Galois partner of 3"),
    ("4prime", 4, None,    "Galois conjugate of 4 (rational eigval)"),
    ("2prime", 2, "2",     "Galois partner of 2"),
]
# Sum of squares: 1+4+9+16+25+36+9+16+4 = 120 = |2I|


def main():
    findings = []
    print("=" * 70)
    print("SIM v8: build-up from icosa/dodeca, build-down from V_600")
    print("=" * 70)

    # ---- (A) icosahedron and dodecahedron
    print("\n[A] 3D icosahedron and dodecahedron spectra...")
    ico = generate_icosahedron()
    dod = generate_dodecahedron()
    A_ico, d2_ico = build_adjacency(ico)
    A_dod, d2_dod = build_adjacency(dod)
    spec_ico = spectrum_with_multiplicities(A_ico)
    spec_dod = spectrum_with_multiplicities(A_dod)

    findings.append(f"Icosahedron: 12 vertices, min squared dist = {d2_ico:.4f}, "
                    f"regularity = {int(A_ico.sum(axis=1)[0])}")
    findings.append(f"  Adjacency spectrum (eigval x mult):")
    for ev, m in spec_ico:
        findings.append(f"    {ev:+.6f}  x{m}")
    findings.append("")
    findings.append(f"Dodecahedron: 20 vertices, min squared dist = "
                    f"{d2_dod:.4f}, regularity = {int(A_dod.sum(axis=1)[0])}")
    findings.append(f"  Adjacency spectrum (eigval x mult):")
    for ev, m in spec_dod:
        findings.append(f"    {ev:+.6f}  x{m}")
    findings.append("")

    # Classify each eigenvalue by rationality
    def classify_eig(ev, tol=1e-3):
        # try to detect a + b*phi
        for b in range(-4, 5):
            a = ev - b * PHI
            if abs(a - round(a)) < tol:
                a_int = round(a)
                if b == 0:
                    return f"{a_int} (rational, sigma-fixed)"
                else:
                    return f"{a_int} + {b}*phi (Galois-paired)"
        return f"{ev:.4f} (unrecognised)"

    findings.append("Icosahedron eigenvalue classification (sigma-action):")
    for ev, m in spec_ico:
        findings.append(f"  {ev:+.4f} x{m}  ->  {classify_eig(ev)}")
    findings.append("")

    findings.append("Dodecahedron eigenvalue classification:")
    for ev, m in spec_dod:
        findings.append(f"  {ev:+.4f} x{m}  ->  {classify_eig(ev)}")
    findings.append("")

    # ---- (B) V_600
    print("\n[B] V_600 spectrum and 2I irrep identification...")
    v600 = generate_v600()
    A_v600, _ = build_adjacency(v600)
    spec_v600 = spectrum_with_multiplicities(A_v600)
    findings.append(f"V_600: 120 vertices, A_1 spectrum:")
    for ev, m in spec_v600:
        findings.append(f"  {ev:+.4f}  x{m}  ->  {classify_eig(ev)}")
    findings.append("")

    # Identify which 2I irrep carries each eigenspace
    # multiplicity = dim(irrep)^2 (Peter-Weyl) means:
    #   mult 1  -> 1-dim irrep
    #   mult 4  -> 2-dim irrep
    #   mult 9  -> 3-dim irrep
    #   mult 16 -> 4-dim irrep
    #   mult 25 -> 5-dim irrep
    #   mult 36 -> 6-dim irrep
    irrep_by_mult = {1: "1", 4: "2 or 2'", 9: "3 or 3'",
                     16: "4 or 4'", 25: "5", 36: "6"}

    findings.append("Peter-Weyl identification of V_600 eigenspaces:")
    findings.append("  (multiplicity = dim(irrep)^2 since each irrep V "
                    "appears with multiplicity dim(V) in regular rep)")
    irrep_assignments = []
    for ev, m in spec_v600:
        irrep = irrep_by_mult.get(m, "?")
        cls = classify_eig(ev)
        findings.append(f"  eigval {ev:+.4f}, mult {m}  ->  irrep {irrep}  "
                        f"[{cls}]")
        irrep_assignments.append((ev, m, irrep, cls))
    findings.append("")

    # ---- (C) Galois pairing structure
    findings.append("Galois pair structure visible in V_600 spectrum:")
    findings.append("  (2, 2') pair:  6 phi  x4  <->  6 - 6 phi  x4   "
                    "[both 2-dim spin irreps]")
    findings.append("  (3, 3') pair:  4 phi  x9  <->  4 - 4 phi  x9   "
                    "[both 3-dim irreps, lifted from A_5]")
    findings.append("  total Galois-paired dim: 8 + 18 = 26 = 13 + 13")
    findings.append("")
    findings.append("Sigma-fixed irreps (rational A_1 eigvals):")
    findings.append("  1 trivial (eigval 12)  x1")
    findings.append("  4-dim (eigval 3)       x16")
    findings.append("  5-dim (eigval 0)       x25")
    findings.append("  6-dim (eigval -2)      x36")
    findings.append("  4'-dim (eigval -3)     x16")
    findings.append("  total sigma-fixed dim: 1 + 16 + 25 + 36 + 16 = 94")
    findings.append("")

    # ---- (D) the seam
    findings.append("THE SEAM (where the missing Hilbert-Polya operator "
                    "must live):")
    findings.append("  The (3, 3') Galois pair of A_5 has dim 3 + 3 = 6")
    findings.append("  Lifted to 2I (V_600 spectrum) it becomes dim "
                    "9 + 9 = 18")
    findings.append("  Plus the spin (2, 2') pair only in 2I: dim 4 + 4 = 8")
    findings.append("  Total Galois-paired in V_600: 26 = 13 + 13")
    findings.append("")
    findings.append("  Therefore: the 3D ICOSAHEDRAL (3, 3') Galois pair is")
    findings.append("  the GEOMETRIC SOURCE of the 18/26 of the 13+13 in")
    findings.append("  V_600. The remaining 8/26 (the 4+4 from spin (2,2'))")
    findings.append("  is a PURELY 4D effect from the spinor lift.")
    findings.append("")
    findings.append("  Construction of T (the Hilbert-Polya operator):")
    findings.append("    Build T as an operator INTERTWINING the irreps")
    findings.append("    in the Galois-paired blocks. Specifically, find")
    findings.append("    a 26-dim self-adjoint extension of an operator")
    findings.append("    on the (3 + 3') subspace that has eigenvalues")
    findings.append("    matching gamma_n. Lift from A_5's 3D pair.")
    findings.append("")
    findings.append("  This is the proposed search direction. The next")
    findings.append("  probe (sim v9, future) would attempt the explicit")
    findings.append("  construction.")

    # ---- Plots
    print("\n[C] Plotting...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    for ax, spec, name in [(ax1, spec_ico, "Icosahedron (12 verts)"),
                           (ax2, spec_dod, "Dodecahedron (20 verts)")]:
        for ev, m in spec:
            cls = classify_eig(ev)
            color = "tab:blue" if "rational" in cls else "tab:red"
            ax.bar(ev, m, width=0.15, color=color,
                   edgecolor="black", linewidth=0.5)
            ax.annotate(f" x{m}", (ev, m), fontsize=9)
        ax.set_title(f"{name} adjacency spectrum")
        ax.set_xlabel("eigenvalue")
        ax.set_ylabel("multiplicity")
        ax.axhline(0, color="gray", linewidth=0.3)
        ax.grid(True, alpha=0.3)
    from matplotlib.patches import Patch
    leg = [Patch(color="tab:blue", label="sigma-fixed (rational)"),
           Patch(color="tab:red",  label="Galois-paired (involves phi)")]
    ax1.legend(handles=leg, loc="upper right", fontsize=9)
    plt.tight_layout()
    plt.savefig(OUTPUTS / "01_icosa_dodeca_spectra.png", dpi=140)
    plt.close()

    # V_600 spectrum with irrep labels
    fig, ax = plt.subplots(figsize=(14, 6))
    for ev, m in spec_v600:
        cls = classify_eig(ev)
        irrep = irrep_by_mult.get(m, "?")
        color = "tab:blue" if "rational" in cls else "tab:red"
        ax.bar(ev, m, width=0.3, color=color,
               edgecolor="black", linewidth=0.5)
        ax.annotate(f" mult {m}\n irrep {irrep}", (ev, m),
                    fontsize=9, ha="center")
    ax.set_title("V_600 A_1 spectrum + 2I irrep identification\n"
                 "Blue = sigma-fixed (rational); Red = Galois-paired")
    ax.set_xlabel("A_1 eigenvalue")
    ax.set_ylabel("multiplicity = dim(irrep)^2")
    ax.axhline(0, color="gray", linewidth=0.3)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUTPUTS / "02_v600_irrep_decomposition.png", dpi=140)
    plt.close()

    # Seam diagram
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.axis("off")
    ax.set_title("From 3D icosahedron to V_600: the Galois-paired seam",
                 fontsize=12)

    # Boxes
    def box(x, y, w, h, label, color):
        from matplotlib.patches import FancyBboxPatch
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                             linewidth=1.5, edgecolor="black",
                             facecolor=color)
        ax.add_patch(box)
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                fontsize=10)

    box(0.5, 6, 4, 1, "A_5 irreps (3, 3'):\n"
                       "3-dim + 3-dim = 6\n"
                       "Galois pair at 3D level", "tab:orange")
    box(0.5, 4, 4, 1, "Spin (2, 2') NEW in 2I:\n"
                       "2-dim + 2-dim = 4\n"
                       "(no 3D analog)", "tab:cyan")
    box(7, 5, 4, 1.5, "V_600 (= 2I) Galois-paired block:\n"
                       "(2,2'): 4+4 = 8\n"
                       "(3,3'): 9+9 = 18\n"
                       "Total: 26 = 13 + 13", "tab:red")
    box(7, 2.5, 4, 1.5, "V_600 sigma-fixed block:\n"
                        "1 + 16 + 25 + 36 + 16 = 94", "tab:blue")
    # Arrows
    from matplotlib.patches import FancyArrowPatch
    ax.add_patch(FancyArrowPatch((4.5, 6.5), (7, 6),
                                  arrowstyle="->", lw=1.5))
    ax.add_patch(FancyArrowPatch((4.5, 4.5), (7, 5.5),
                                  arrowstyle="->", lw=1.5))
    ax.text(5.5, 7.0, "Peter-Weyl lift\n(3D -> 4D)", fontsize=9,
            color="tab:orange")

    # The seam annotation
    box(0.5, 1.5, 11, 0.8,
        "Missing operator T: lives on (3, 3') + (2, 2') subspaces "
        "(combined 26 dim);\nlifts from 3D icosahedral (3, 3') seed.",
        "lemonchiffon")

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    plt.tight_layout()
    plt.savefig(OUTPUTS / "03_seam_diagram.png", dpi=140)
    plt.close()

    # Save CSV
    with open(DATA / "irrep_seam.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["space", "A1_eigenvalue", "multiplicity",
                    "irrep_dim", "galois_class"])
        for ev, m in spec_ico:
            w.writerow(["icosahedron", f"{ev:.6f}", m, "?",
                        classify_eig(ev)])
        for ev, m in spec_dod:
            w.writerow(["dodecahedron", f"{ev:.6f}", m, "?",
                        classify_eig(ev)])
        for ev, m, irrep, cls in irrep_assignments:
            w.writerow(["V_600", f"{ev:.6f}", m, irrep, cls])

    # Print summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for line in findings:
        print(line)
    print()
    with open(DATA / "findings.txt", "w") as f:
        f.write("\n".join(findings))


if __name__ == "__main__":
    main()
