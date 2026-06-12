"""
f1_candidates.py -- run candidate definitions of F_1 ("the field with one element")
through an HONEST classification gate, and log which pile each lands in.

WHY THIS IS NOT A FAKE PROOF ATTEMPT
------------------------------------
Whether a given F_1 "proves RH" IS the open problem -- no computation here can
decide it. So this is NOT a discovery run. It is a reproducible LEDGER: it encodes
the *documented mathematical status* of each real, published F_1 candidate against
three fixed questions, and sorts it by rule. Same spirit as the (O2) negative:
a logged, hashed verdict, never a proof certificate.

THE FORK (the gate), made mechanical
------------------------------------
Q1 DEFINED   : is there an actual, agreed mathematical object? (not just a wish)
Q2 CARRIES   : does building  Spec Z  x_{F_1}  Spec Z  over it yield the Weil
               explicit-formula functional W(f) as a genuine degree / intersection
               form (the thing whose positivity is RH)?  yes / partial / no
Q3 HONEST    : does it deliver that positivity WITHOUT assuming RH or an
               unproven cohomological positivity?  (not circular)

VERDICT RULE
------------
  not DEFINED                         -> WISH      (names a job, not an object)
  DEFINED, not CARRIES                -> INERT     (real object, does too little)
  DEFINED, CARRIES, not HONEST        -> CIRCULAR  (assumes the answer; fails provenance)
  DEFINED, CARRIES, HONEST            -> CROSSES   (would prove RH -- none reach this)

Every 'status' field below is a documented fact about that programme, with a
literature anchor. The script only applies the rule; it invents nothing.
"""
import json, hashlib

# carries: "no" | "partial" | "yes"   (partial = recovers some structure / the
# explicit formula, but NOT the positivity itself)
CANDIDATES = [
 dict(
   name="F_1 = {*}  (one-point set / trivial monoid)  [Lee's 'unity']",
   defined=True, carries="no", honest=True,
   status="The crudest 'unity'. A perfectly real object (the terminal monoid). "
          "Geometry over it (Deitmar's monoid schemes / Kapranov-Smirnov) is "
          "essentially combinatorial/toric: it sees the COMBINATORICS of a variety "
          "(its toric skeleton) but carries NO nontrivial Frobenius and no Riemann "
          "zeta zeros. Does too little.",
   anchor="Kapranov-Smirnov; Deitmar 2005 (Schemes over F_1)"),

 dict(
   name="F_1-vector space = pointed set (Kapranov-Smirnov)",
   defined=True, carries="no", honest=True,
   status="Linear algebra over F_1 = pointed sets; GL_n(F_1)=S_n (the symmetric "
          "group). Recovers q->1 counting (e.g. Grassmannian point counts -> "
          "binomial coefficients) but the q->1 limit kills exactly the arithmetic "
          "that carries the zeros. Real, elegant, inert for RH.",
   anchor="Kapranov-Smirnov (unpublished); Cohn 2004"),

 dict(
   name="Deitmar monoid schemes / Toen-Vaquie schemes over F_1",
   defined=True, carries="no", honest=True,
   status="Fully rigorous schemes over F_1. Their zeta functions reproduce the "
          "TORIC/combinatorial factors only; Soule's and Deitmar's zeta of Spec Z "
          "over F_1 gives the archimedean Gamma-factor shape, NOT the nontrivial "
          "zeros. Defined, does too little.",
   anchor="Deitmar 2005; Toen-Vaquie 2009; Soule 2004"),

 dict(
   name="Borger Lambda-rings (F_1 = descent data = a lambda-ring structure)",
   defined=True, carries="partial", honest=True,
   status="A genuinely deep, fully-defined proposal: 'F_1-structure' = commuting "
          "Frobenius lifts (a lambda-ring). This DOES supply Frobenius operators on "
          "Spec Z -- the right kind of object -- and is the most arithmetic of the "
          "inert candidates. But it has not been made to yield the explicit-formula "
          "POSITIVITY; it furnishes the lifts, not the inequality. Stalls before W(f).",
   anchor="Borger 2009 (Lambda-rings and the field with one element)"),

 dict(
   name="Connes-Consani arithmetic site / adele class space (Spec Z bar)",
   defined=True, carries="partial", honest=True,
   status="The live frontier. The arithmetic site + the scaling action genuinely "
          "RECOVER the Weil explicit formula as a trace formula -- this is real and "
          "remarkable: the primes appear as periodic orbits, and RH becomes the "
          "POSITIVITY of the Weil distribution (a trace positivity). It does NOT "
          "assume RH. But it stalls at EXACTLY the positivity step: the needed "
          "trace/intersection positivity is unproven. Honest, reaches the wall, "
          "does not cross it. This is the (O2)-analog at the F_1 level.",
   anchor="Connes 1999; Connes-Consani 2014-2021 (arithmetic site, Riemann-Roch)"),

 dict(
   name="Deninger dynamical/cohomological F_1 (hypothetical H^* + flow)",
   defined="partial", carries="yes", honest=False,
   status="A blueprint, not yet an object: IF a certain cohomology with a flow "
          "existed, RH would follow by analogy with the function-field proof. But "
          "the cohomology is conjectural AND the positivity is part of what must be "
          "assumed about the flow. So: object not fully defined, and the crossing "
          "step would assume its own conclusion. Half wish, half circular.",
   anchor="Deninger 1998-2010 (cohomology of dynamical systems)"),

 dict(
   name="F_1 := unity 'defined to make |alpha|=sqrt(q) hold'  (CONTROL)",
   defined=True, carries="yes", honest=False,
   status="The fitted-map trap at the F_1 level, included as a control. Declare an "
          "'object' whose defining axiom is the very norm condition |alpha|=sqrt(q) "
          "(equivalently Re(s)=1/2). It 'carries' the positivity -- because you put "
          "it in by hand. Fails HONEST/provenance: it renames RH, does not prove it. "
          "The gate must reject this, exactly as it rejects the least-squares map.",
   anchor="control (analog of the W5 fitted-map catch)"),
]

def verdict(c):
    if c["defined"] is not True:        # 'partial' or False -> not a finished object
        return "WISH" if c["carries"]!="yes" else "WISH/CIRCULAR"
    if c["carries"]=="no":              return "INERT"
    # defined and carries something:
    if not c["honest"]:                 return "CIRCULAR"
    if c["carries"]=="yes":             return "CROSSES"
    return "OPEN (reaches the wall, does not cross)"   # defined+partial+honest

def cert(c):
    v=verdict(c)
    body=dict(candidate=c["name"], defined=c["defined"], carries=c["carries"],
              honest=c["honest"], verdict=v, status=c["status"], anchor=c["anchor"],
              scope="LEDGER entry (documented status). NOT a proof certificate.")
    body["cert_id"]="f1:"+hashlib.sha256(
        json.dumps(body,sort_keys=True).encode()).hexdigest()[:12]
    return body

if __name__=="__main__":
    ledger=[cert(c) for c in CANDIDATES]
    with open("f1_candidates.json","w") as f: json.dump(ledger,f,indent=2)

    W=78
    print("="*W)
    print("F_1 CANDIDATE LEDGER  --  does any honestly-defined object cross to RH?")
    print("="*W)
    print(f"{'verdict':<38}{'D':>2}{'carries':>9}{'honest':>8}")
    print("-"*W)
    order={"CROSSES":0,"OPEN (reaches the wall, does not cross)":1,"CIRCULAR":2,
           "WISH/CIRCULAR":3,"WISH":4,"INERT":5}
    for b in sorted(ledger,key=lambda b:order.get(b["verdict"],9)):
        d = "Y" if b["defined"] is True else ("~" if b["defined"]=="partial" else "N")
        h = "Y" if b["honest"] else "N"
        print(f"{b['verdict']:<38}{d:>2}{b['carries']:>9}{h:>8}   {b['cert_id']}")
        print(f"    {b['candidate']}")
    print("-"*W)
    tally={}
    for b in ledger: tally[b["verdict"]]=tally.get(b["verdict"],0)+1
    print("tally:", "  ".join(f"{k}={v}" for k,v in
          sorted(tally.items(),key=lambda kv:order.get(kv[0],9))))
    print()
    print("READING:")
    print("  * CROSSES  = would prove RH.            count =", tally.get("CROSSES",0))
    print("  * Every honestly-defined object lands INERT (does too little) or OPEN")
    print("    (Connes-Consani: reaches the positivity, cannot prove it).")
    print("  * The only candidates that 'carry' the positivity are CIRCULAR/WISH:")
    print("    they assume |alpha|=sqrt(q) (or need an undefined cohomology) -- the")
    print("    gate rejects them on provenance, same as the fitted map.")
    print("  * 'F_1 = unity' is REAL but lands INERT. Naming unity does not build the")
    print("    object; forcing it to carry RH makes it CIRCULAR. Same wall, F_1 clothes.")
    print("  -> ledger written to f1_candidates.json")
