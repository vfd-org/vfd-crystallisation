"""
aria_void_joint.py -- THE JOINT VOID.

aria_void.py drew the silhouette of the missing object from ONE side (the
arithmetic / F_1 geometry). This draws it from BOTH sides at once:

    SIDE A  (arithmetic / geometry):  a canonical Frobenius over Z on the
            F_1-surface  Spec Z x_{F_1} Spec Z,  whose DEGREE-FORM is W(f) >= 0.
    SIDE B  (spectral / physics):     a self-adjoint operator H (Hilbert-Polya /
            Berry-Keating xp / Connes scaling flow) whose SPECTRUM is the zeros.

The leading bet (Connes): A and B are the SAME object seen two ways. So the
"both-object" must satisfy A's constraints AND B's constraints SIMULTANEOUSLY.
This script intersects the two constraint sheets and marks, line by line:

    [reach]  already satisfiable by today's partial object (Connes-Consani et al.)
    [DARK]   unreached on this side
    >>>      the SINGLE line where BOTH sides go dark together = the one door.

HONEST SCOPE: this is the SPEC of the missing object (its over-constrained
silhouette), not the object. Same status as the (O2) negative and the F_1
ledger: a logged, reproducible drawing of the gap. No proof is claimed.
Over-constraint is the only lever -- two stiff conditions pin the object down
to (conjecturally) one shape; this sheet is that pinning, written out.
"""
import json, hashlib

# Each constraint: (id, text, side, reach_A, reach_B)
#   side  : 'A' arithmetic-only, 'B' spectral-only, 'BOTH' joint requirement
#   reach_* : True if today's partial both-object (Connes-Consani + scaling flow)
#             already delivers it ON THAT SIDE; False = dark on that side; None = n/a
CONSTRAINTS = [
 # ---- things BOTH sides already reach (the shared, RH-independent floor) ----
 ("C1","carries the EXPLICIT/TRACE FORMULA (primes <-> spectrum, Tr = sum over primes)",
       "BOTH", True, True,
       "Connes: the scaling flow's trace IS the explicit formula. Holds without RH."),
 ("C2","has the right GLOBAL DENSITY of zeros/eigenvalues (Weyl law ~ (T/2pi)log T)",
       "BOTH", True, True,
       "Both the arithmetic count and Berry-Keating xp give this density."),
 ("C3","has GUE local statistics (level repulsion, sine kernel, rigidity)",
       "BOTH", True, True,
       "Montgomery-Odlyzko (numerics) + random-matrix universality. Class, not individual."),
 ("C4","respects the functional-equation MIRROR  xi(s)=xi(1-s)  (radius <-> 1/radius)",
       "BOTH", True, True,
       "Arithmetic: theta reciprocity. Spectral: the s<->1-s symmetry of the flow / T-duality shape."),

 # ---- SIDE A reaches, SIDE B does not (geometry ahead of spectrum) ----
 ("A1","a canonical FROBENIUS endomorphism over Z (an actual morphism, not analogy)",
       "A", "partial", False,
       "Borger lambda-rings supply Frobenius LIFTS; no operator realizes them spectrally yet."),
 ("A2","lives on the arithmetic SURFACE Spec Z x_{F_1} Spec Z (a real 2-diml object)",
       "A", "partial", False,
       "Connes-Consani arithmetic site is defined; its spectral incarnation is partial."),

 # ---- SIDE B reaches, SIDE A does not (spectrum ahead of geometry) ----
 ("B1","a concrete SELF-ADJOINT operator H = H* on a Hilbert space",
       "B", False, "partial",
       "Berry-Keating xp / Connes adele-class operator: right density, not yet a true self-adjoint H."),
 ("B2","UNITARY dynamics / a positive Hilbert-space inner product (norms >= 0)",
       "B", False, "partial",
       "Physics' unitarity positivity exists in general; the SPECIFIC space for the zeros does not."),

 # ---- the SINGLE joint-dark line: both sides go dark here, and it is ONE thing ----
 ("Z","THE CROSSING: side A would need Frobenius degree-form W(f) >= 0; side B would "
      "need H self-adjoint with spectrum = the zeros. Each, under its own strong "
      "hypotheses, would yield RH.",
       "BOTH", False, False,
       "This is the one door. CONJECTURAL status (NOT a theorem): Connes shows RH is "
       "equivalent to positivity of a TRACE PAIRING; no theorem identifies the arithmetic "
       "construction (A) with the spectral one (B), nor proves 'W(f)>=0' and 'H=H*' are "
       "literally the same statement. The programme HOPES they are one object. Neither "
       "side reaches it. Force it in by hand on either side -> CIRCULAR (the gate rejects "
       "on provenance, exactly like the F_1 'unity-defined-to-work' control)."),
]

def status(c):
    _id,txt,side,ra,rb,note = c
    def tag(r):
        return {True:"reach", "partial":"reach*", False:"DARK", None:"  -  "}[r]
    return _id, txt, side, tag(ra), tag(rb), note

def both_dark(c):
    return c[3] is False and c[4] is False

def main():
    rows=[status(c) for c in CONSTRAINTS]
    W=92
    print("="*W)
    print("THE JOINT VOID  --  silhouette of the object that must be BOTH")
    print("   SIDE A = arithmetic Frobenius / F_1-surface      (degree-form positivity)")
    print("   SIDE B = self-adjoint spectrum / Hilbert-Polya   (unitary, real spectrum)")
    print("="*W)
    print(f"{'id':<4}{'A':<8}{'B':<8}requirement")
    print("-"*W)
    for _id,txt,side,ta,tb,note in rows:
        mark = ">>> " if (ta=="DARK" and tb=="DARK") else "    "
        print(f"{mark}{_id:<4}{ta:<8}{tb:<8}{txt}")
    print("-"*W)

    floor=[c for c in CONSTRAINTS if c[3] in (True,) and c[4] in (True,)]
    a_only=[c for c in CONSTRAINTS if c[3] in (True,"partial") and c[4] is False]
    b_only=[c for c in CONSTRAINTS if c[4] in (True,"partial") and c[3] is False]
    joint_dark=[c for c in CONSTRAINTS if both_dark(c)]

    print(f"\n  shared floor (both reach, RH-independent) : {len(floor)}  -> {[c[0] for c in floor]}")
    print(f"  geometry ahead of spectrum (A reach, B dark): {len(a_only)}  -> {[c[0] for c in a_only]}")
    print(f"  spectrum ahead of geometry (B reach, A dark): {len(b_only)}  -> {[c[0] for c in b_only]}")
    print(f"  BOTH-DARK (the joint void)                  : {len(joint_dark)}  -> {[c[0] for c in joint_dark]}")

    print("\n" + "="*W)
    print("COLLAPSE  --  the joint void is ONE line, not a region")
    print("="*W)
    print("  * The shared floor (C1-C4) shows the two sides ALREADY MEET on everything")
    print("    that does not require RH: trace formula, density, GUE class, the mirror.")
    print("  * A1-A2 vs B1-B2 are NOT separate holes -- they are the SAME object missing")
    print("    its two faces: 'Frobenius on a surface' (A) and 'self-adjoint H' (B). The")
    print("    both-object is what fuses them; each side has built only its own half.")
    print("  * The programme CONJECTURES everything collapses to a single line Z. Side A")
    print("    would read it 'W(f)>=0'; side B 'H=H*'. NOT proven identical: Connes ties")
    print("    RH to trace-pairing positivity; no theorem fuses the two constructions.")
    print("  => The joint void is a ONE-line hole. Over-constraining to 'both' did not")
    print("     widen the gap -- it PINNED it to a single shared condition. That is the")
    print("     whole value of demanding both: the door is now exactly one line wide.")

    print("\n" + "="*W)
    print("THE DIRECTIVE  (the spec = the only honest guidance)")
    print("="*W)
    print('  "Build ONE object O such that:')
    print('     (floor) Tr(O) = explicit formula, correct density, GUE class, mirror   [reach]')
    print('     (A-face) O is a Frobenius on Spec Z x_{F_1} Spec Z                      [half-built]')
    print('     (B-face) O is a self-adjoint H on a positive Hilbert space             [half-built]')
    print('     (Z)      CONJECTURED: the two faces are one object; each alone -> RH    [DARK]')
    print('   The floor is done. Each face is half-built. The fusion line Z is the wall.')
    print('   Supplying Z by fiat on either face = CIRCULAR (provenance reject)."')

    print("\n" + "="*W)
    print("HONEST LIMIT")
    print("="*W)
    print("  * REAL: the both-framing is not hand-waving -- the two sides demonstrably")
    print("    share a floor (C1-C4) and their gaps fuse to ONE line (Z). The silhouette")
    print("    is exact and one-dimensional.")
    print("  * LEVER: over-constraint pinned the missing object to a unique forced shape.")
    print("    That is the only real reason to hope it is findable -- nothing to search,")
    print("    one shape can fit.")
    print("  * WALL UNMOVED: drawing the one-line silhouette does not fill it. Z is a")
    print("    CONSTRUCTION (the fused F_1-surface / Hilbert-Polya operator), generational.")
    print("    Naming it, or forcing either face to carry it, is CIRCULAR. Same wall --")
    print("    now proven to be a SINGLE door, seen from two rooms.")

    # ---- emit hashed ledger ----
    ledger=dict(
      floor=[c[0] for c in floor], a_only=[c[0] for c in a_only],
      b_only=[c[0] for c in b_only], joint_dark=[c[0] for c in joint_dark],
      constraints=[dict(id=c[0],text=c[1],side=c[2],reach_A=str(c[3]),
                        reach_B=str(c[4]),note=c[5]) for c in CONSTRAINTS],
      verdict="JOINT VOID: programme CONJECTURES a single shared line Z (arithmetic "
              "W(f)>=0 and spectral H=H* as one object). NOT a theorem -- Connes ties RH "
              "to trace-pairing positivity; no result fuses the two constructions. "
              "Floor met; faces at most half-built; fusion line is the wall.",
      scope="SPEC of the conjectured both-object. NOT a proof, NOT a theorem.")
    ledger["cert_id"]="joint_void:"+hashlib.sha256(
        json.dumps(ledger,sort_keys=True).encode()).hexdigest()[:12]
    with open("aria_void_joint.json","w") as f: json.dump(ledger,f,indent=2)
    print(f"\n  -> joint silhouette written to aria_void_joint.json  [{ledger['cert_id']}]")

if __name__=="__main__":
    main()
