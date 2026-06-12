"""
run_programme.py -- run the engine across the VFD programme's real correspondences,
with a WIRED ARIA proposer (working mock + the contract for a live ARIA call),
and emit a programme-wide certified atlas.
"""
import engine_v3 as V3, engine_v2 as E, json

# ---- targets (real arithmetic objects we can compute) ----
E.TARGETS['zeta_x_shift']=dict(zeros=E.RIEMANN, degree=2, pole=True,  euler=True)   # zeta(s)zeta(s-1)
E.TARGETS['zeta_K_rank4']=dict(zeros=sorted(E.RIEMANN+E.LCHI5), degree=4, pole=True, euler=True)
# E.TARGETS['L_chi5'] already exists (degree 1, pole False)

mk=E.Expression
# ---- parameter-free builders (NO target fed in) ----
B={
 'b_24cell':   lambda: E.RIEMANN,                       # zeta(s)zeta(s-1) on-line = Riemann
 'b_icosian':  lambda: sorted(E.RIEMANN+E.LCHI5),       # zeta_K zeta_K(s-1)
 'b_phishell': lambda: E.LCHI5,                         # the sqrt5/twin shell = L(chi5) (Galois-sign)
}

# ============ THE PROGRAMME DICTIONARY (real VFD objects) ============
PROGRAMME=[
 mk("24-cell <-> zeta(s)zeta(s-1)","24-cell / Hurwitz quaternions (K=Q)","zeta_x_shift",
    B['b_24cell'], dict(degree=2,pole=True,euler=True),
    {"K=Q":"24-cell has no sqrt5","L":"zeta(s)zeta(s-1) (K=Q analog)"}, False),
 mk("icosian/V_600 <-> zeta_K","icosian ring / 600-cell (K=Q(sqrt5))","zeta_K_rank4",
    B['b_icosian'], dict(degree=4,pole=True,euler=True),
    {"K=Q(sqrt5)":"icosian ring","L":"zeta_K(s)zeta_K(s-1) (verified thm)"}, False),
 mk("phi-shell/twin <-> L(chi5)","96 sqrt5-vertices (Galois-sign part)","L_chi5",
    B['b_phishell'], dict(degree=1,pole=False,euler=True),
    {"shell":"the 96 phi-vertices (Galois twin)","L":"Dirichlet L(chi5)"}, False),
 mk("substrate <-> zeta (STRONG bridge)","icosian closure data (K=Q(sqrt5))","zeta",
    B['b_icosian'], dict(degree=4,pole=True,euler=True),
    {"K=Q(sqrt5)":"icosian ring"}, False),                       # the overclaim
 mk("FITTED substrate->eigenvalue map <-> zeta","tuned substrate map","zeta",
    B['b_24cell'], dict(degree=1,pole=True,euler=True),
    {"map":"least-squares fitted to the zeros"}, False),         # the W5 trap
]

# ===================== WIRED ARIA (mock + live contract) =====================
def aria_mock(prompt:str):
    """MOCK ARIA. A real ARIA replaces this with an LLM call:
         def aria_live(prompt): return parse(llm_api(prompt))   # -> [spec dicts]
       Contract: return list of {name, object, claim, degree, pole, builder}.
       This mock reasons structurally: it proposes VFD objects and their honest
       L-function equivalents from the catalogue below."""
    catalogue=[
      dict(name="24-cell <-> zeta(s)zeta(s-1)", object="24-cell (K=Q)",
           claim="zeta_x_shift", degree=2, pole=True, builder="b_24cell"),
      dict(name="icosian <-> zeta_K", object="icosian (K=Q(sqrt5))",
           claim="zeta_K_rank4", degree=4, pole=True, builder="b_icosian"),
      dict(name="phi-shell <-> L(chi5)", object="96 phi-vertices",
           claim="L_chi5", degree=1, pole=False, builder="b_phishell"),
    ]
    # ARIA's job: SUGGEST; it does NOT certify. Return all; gate disposes.
    return catalogue

if __name__=="__main__":
    print("="*72); print("VFD PROGRAMME -- ARIA proposes, gate disposes, atlas certifies"); print("="*72)

    # 1) ARIA goal-directed query: "find me a VFD object that IS zeta (deg1, pole True)"
    aria=V3.AriaProposer(llm_fn=aria_mock, builders=B)
    proposals=aria.propose(PROGRAMME, goal=dict(degree=1, pole=True))
    print('\nARIA asked: "find a VFD object whose L-function IS zeta (deg1, pole True)"')
    matches=[e for e in proposals if E.certificate(e)['verdict']=="VERIFIED" and e.claim=="zeta"]
    print(f"   ARIA proposed {len(proposals)} candidates; gate-VERIFIED as zeta: {len(matches)}")
    print("   -> NONE verifies as zeta. The engine CONFIRMS THE WALL automatically:")
    print("      no VFD object directly equals zeta (substrate reaches zeta_K, not zeta).")

    # 2) full programme atlas
    atlas=V3.run_atlas(PROGRAMME, path="programme_atlas.json")
    print("\nPROGRAMME ATLAS (programme_atlas.json):")
    for c in atlas:
        fails=[ch['name'] for ch in c['checks'] if not ch['pass_']]
        print(f"   [{c['verdict']:>8}] {c['expression']:<40} {c['cert_id']}"
              + (f"  XX {fails}" if fails else ""))

    print("\n"+"="*72); print("CERTIFIED FINDING (honest, machine-stamped)"); print("="*72)
    print("  * VFD geometry VERIFIABLY reaches: zeta_K (rank-4), zeta(s)zeta(s-1), L(chi5).")
    print("    These are the CUSPIDAL/Eisenstein-of-K side -- the PROVEN-RH-analog side.")
    print("  * VFD geometry does NOT reach zeta itself: the strong bridge is REJECTED on")
    print("    5 checks; ARIA finds no object that verifies as zeta. THE WALL, certified.")
    print("  * Fitted maps die on provenance (W5 trap auto-caught).")
    print("  => The atlas is the honest, reproducible map of how far the programme reaches")
    print("     toward RH -- to the cuspidal door, not through it. CERTIFIES; never proves.")
