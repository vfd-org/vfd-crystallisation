"""
vfd_math_engine v3 -- adds: (1) sharper gate (density + rigidity discriminators),
(2) a real ARIA proposer INTERFACE (LLM slot with mock fallback),
(3) run_atlas() that gates a batch and writes a certified atlas.json.

HONEST SCOPE unchanged: CERTIFIES the landscape (verification certs only).
Never proves RH. ARIA PROPOSES; the gate DISPOSES.
"""
import numpy as np, json, hashlib
import engine_v2 as E   # reuse TARGETS, RIEMANN, LCHI5, Expression, certificate-core

# ---------------- NEW DISCRIMINATORS ----------------
def _density(z):
    z=np.sort(np.array(z)); return len(z)/(z[-1]-z[0])      # zeros per unit height
def disc_density(pred, tgt):
    a,b=_density(pred), _density(E.TARGETS[tgt]['zeros'])
    return abs(a-b)/b < 0.15, f"density {a:.3f} vs {b:.3f} (zeros/height)"
def _numvar(z, L=6, nwin=1500):
    z=np.sort(np.array(z)); d=np.diff(z); u=np.cumsum(d)/np.mean(d)  # unfold
    lo,hi=u.min()+1,u.max()-L-1
    if hi<=lo: return 0.0
    s=np.linspace(lo,hi,nwin); c=np.array([np.sum((u>=x)&(u<x+L)) for x in s])
    return float(c.var())
def disc_rigidity(pred, tgt):
    a,b=_numvar(pred), _numvar(E.TARGETS[tgt]['zeros'])
    return abs(a-b)<0.4, f"numvar(L=6) {a:.3f} vs {b:.3f} (GUE rigid ~0.3)"

# extend the gate's discriminator list
E.DISCRIMINATORS = E.DISCRIMINATORS + [('density',disc_density),('rigidity',disc_rigidity)]

# ---------------- ARIA PROPOSER INTERFACE ----------------
class Proposer:
    """ARIA plugs in HERE. propose(dictionary, goal) -> [Expression].
       goal = desired arithmetic signature, e.g. dict(degree=1,pole=True,fp=0.0).
       A real ARIA implements propose() by REASONING over the dictionary and
       suggesting geometric objects + their arithmetic equivalents."""
    def propose(self, dictionary, goal): raise NotImplementedError

class HeuristicProposer(Proposer):
    def propose(self, dictionary, goal):
        scored=[]
        for e in dictionary:
            score=sum(e.meta.get(k)==v for k,v in goal.items() if k in e.meta)
            scored.append((score,e))
        return [e for _,e in sorted(scored,key=lambda t:-t[0])]

class AriaProposer(Proposer):
    """Real-ARIA slot. Pass llm_fn(prompt:str)->list[dict] of candidate specs.
       Falls back to heuristic if no llm_fn wired."""
    def __init__(self, llm_fn=None, builders=None):
        self.llm_fn=llm_fn; self.builders=builders or {}
    def propose(self, dictionary, goal):
        if self.llm_fn is None:
            return HeuristicProposer().propose(dictionary, goal)
        prompt=(f"Goal: find a VFD geometric object whose L-function has signature {goal}. "
                f"Dictionary objects: {[e.geometry for e in dictionary]}. "
                f"Return candidate (object, claimed L-function, degree, pole, builder-key).")
        specs=self.llm_fn(prompt)                          # <-- real ARIA call
        out=[]
        for s in specs:
            b=self.builders.get(s.get('builder'))
            if b: out.append(E.Expression(s['name'],s['object'],s['claim'],b,
                       dict(degree=s['degree'],pole=s['pole'],euler=True),
                       {'source':'ARIA-proposed'}, False))
        return out or HeuristicProposer().propose(dictionary, goal)

# ---------------- RUN ATLAS ----------------
def run_atlas(expressions, path="atlas.json"):
    atlas=[E.certificate(e) for e in expressions]
    with open(path,"w") as f: json.dump(atlas,f,indent=2)
    return atlas

# ================================== DEMO ==================================
if __name__=="__main__":
    E.TARGETS['zeta_x_shift']=dict(zeros=E.RIEMANN,degree=2,pole=True,euler=True)
    E.TARGETS['zeta_K_rank4']=dict(zeros=sorted(E.RIEMANN+E.LCHI5),degree=4,pole=True,euler=True)
    mk=E.Expression
    dictionary=[
      mk("24-cell <-> zeta(s)zeta(s-1)","24-cell K=Q","zeta_x_shift",lambda:E.RIEMANN,
         dict(degree=2,pole=True,euler=True),{"K=Q":"no sqrt5","L":"zeta(s)zeta(s-1)"},False),
      mk("substrate <-> zeta_K","icosian K=Q(sqrt5)","zeta_K_rank4",lambda:sorted(E.RIEMANN+E.LCHI5),
         dict(degree=4,pole=True,euler=True),{"K=Q(sqrt5)":"icosian ring","L":"zeta_K zeta_K(s-1)"},False),
      mk("substrate <-> zeta (STRONG bridge)","icosian K=Q(sqrt5)","zeta",lambda:sorted(E.RIEMANN+E.LCHI5),
         dict(degree=4,pole=True,euler=True),{"K=Q(sqrt5)":"icosian ring"},False),
      mk("FITTED map <-> zeta","tuned map","zeta",lambda:E.RIEMANN,
         dict(degree=1,pole=True,euler=True),{"map":"least-squares fitted to zeros"},False),
    ]
    print("="*70); print("ARIA PROPOSER (goal-directed) -> 8-CHECK GATE -> ATLAS"); print("="*70)
    aria=AriaProposer(llm_fn=None)        # llm_fn=None -> heuristic fallback (wire real ARIA here)
    goal=dict(degree=1,pole=True)         # 'find me something that IS zeta'
    ranked=aria.propose(dictionary, goal)
    print(f"ARIA goal={goal}; narrowed ranking (best first):")
    for e in ranked: print(f"   - {e.name}  (deg {e.meta['degree']})")
    atlas=run_atlas(dictionary, path="atlas.json")
    print(f"\nCERTIFIED ATLAS written to atlas.json ({len(atlas)} entries):")
    for c in atlas:
        fails=[ch['name'] for ch in c['checks'] if not ch['pass_']]
        print(f"   [{c['verdict']:>8}] {c['expression']:<34} {c['cert_id']}"
              + (f"  failed: {fails}" if fails else ""))
    print("\n"+"="*70); print("STATUS"); print("="*70)
    print("  * 8-check gate live (no_hardcoding, provenance, fingerprint, pointwise,")
    print("    degree, pole, density, rigidity).")
    print("  * ARIA interface live: goal-directed propose(); llm_fn slot = real ARIA;")
    print("    heuristic fallback works now. ARIA proposes; the gate disposes.")
    print("  * atlas.json emitted -- reproducible, hashed, stamped. Run across the whole")
    print("    programme to build the full certified atlas. CERTIFIES; never proves RH.")
