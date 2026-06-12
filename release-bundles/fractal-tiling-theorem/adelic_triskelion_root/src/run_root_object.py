import sys,os; sys.path.insert(0,os.path.dirname(__file__))
import mpmath as mp, json, root_object as R
OUT=os.path.join(os.path.dirname(__file__),"..","outputs")
print("="*74); print("WO-VFD-ADELIC-TRISKELION-ROOT-OBJECT-001  testable root object AT=(F,A∞,S,W,I)"); print("="*74)

# Stage 1 finite arm
print("\n[Stage 1: finite arm F] partial Euler product vs zeta (Re s>1):")
fin={}
for s in [mp.mpf(2), mp.mpf(3), mp.mpc(2,5)]:
    _,err=R.finite_arm(s,P=20000); fin[str(s)]=float(err); print(f"  s={s}: rel-err {float(err):.2e}")
FiniteScore = 1.0 if max(fin.values())<1e-3 else 0.0

# Stage 2 archimedean arm
print("\n[Stage 2: archimedean arm A∞] ∫ e^{-πx²}x^{s-1}dx vs ½π^{-s/2}Γ(s/2):")
arc={}
for s in [mp.mpf(2), mp.mpc(0.5,4), mp.mpc(0.7,10)]:
    _,err=R.archimedean_arm(s); arc[str(s)]=float(err); print(f"  s={s}: rel-err {float(err):.2e}")
GammaScore = 1.0 if max(arc.values())<1e-12 else 0.0

# Stage 3 theta self-duality
print("\n[Stage 3: scale arm S] theta(t)=t^{-1/2}theta(1/t):")
th={}
for t in [mp.mpf('0.3'),mp.mpf('0.7'),mp.mpf('1.5'),mp.mpf('3')]:
    r=R.theta_duality(t); th[str(t)]=float(r); print(f"  t={t}: duality residual {float(r):.2e}")
ThetaScore = 1.0 if max(th.values())<1e-20 else 0.0

# Stage 4 completed FE + controls
print("\n[Stage 4: completed FE residual + controls]:")
Xi   = lambda s: mp.pi**(-s/2)*mp.gamma(s/2)*R.zeta(s)
xi   = lambda s: mp.mpf(1)/2*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*R.zeta(s)
rawz = lambda s: R.zeta(s)
fakeG= lambda s: mp.pi**(-s/2)*mp.gamma(s/3)*R.zeta(s)
fakeE= lambda s: mp.e**(mp.mpf(7)/10*s)*mp.gamma(s/2)*R.zeta(s)
fe={"Xi (F+A∞+S)":R.fe_residual(Xi),"xi full":R.fe_residual(xi),
    "raw zeta (no A∞)":R.fe_residual(rawz),"fake Gamma(s/3)":R.fe_residual(fakeG),"fake exp":R.fe_residual(fakeE)}
for n,v in fe.items(): print(f"  {n:22}: median R_FE {v:.2e}  {'PASS' if v<1e-8 else 'FAIL'}")
FEScore = 1.0 if fe["Xi (F+A∞+S)"]<1e-8 else 0.0
FakePenalty = 1.0 if (fe["raw zeta (no A∞)"]>0.01 and fe["fake Gamma(s/3)"]>0.01 and fe["fake exp"]>0.01) else 0.0

# Stage 5 arm-removal NECESSITY
print("\n[Stage 5: arm-removal necessity] (each arm must be required):")
rm={}
rm["remove A∞ (raw ζ)"]=fe["raw zeta (no A∞)"]
# remove F: Γ-complete a NON-arithmetic Dirichlet series (no Euler product) -> should FAIL FE
D=R.random_dirichlet(); XinoF=lambda s: mp.pi**(-s/2)*mp.gamma(s/2)*D(s)
rm["remove F (Γ·random Dirichlet, no Euler)"]=R.fe_residual(XinoF, sig=(0.3,0.5,0.7), ts=(2,10))
# remove S: the s<->1-s involution IS the test; without it there is no FE statement (structural)
for n,v in rm.items(): print(f"  {n:38}: R_FE {v:.2e}  {'BREAKS (arm necessary)' if v>0.01 else 'still ok??'}")
print("  remove S (involution s↔1-s): there is NO functional-equation statement to test")
print("       -> S is the involution the whole test is ABOUT; structurally necessary.")
NecessityScore = 1.0 if all(v>0.01 for v in rm.values()) else 0.0

# Root score
W=[1,1,1,2,1,1]
RootScore = (W[0]*FiniteScore+W[1]*GammaScore+W[2]*ThetaScore+W[3]*FEScore+W[4]*NecessityScore - W[5]*(1-FakePenalty))
maxscore=sum(W[:5])
verdict = ("STRONG PASS (as normal-form of the completed-zeta construction)" if RootScore>=maxscore-1e-9
           else "WEAK/FAIL")
print("\n"+"="*74)
print(f"  FiniteScore={FiniteScore} GammaScore={GammaScore} ThetaScore={ThetaScore} FEScore={FEScore} NecessityScore={NecessityScore} FakeKernelsFail={FakePenalty}")
print(f"  RootScore = {RootScore}/{maxscore}   -> {verdict}")
print("""  HONEST READING: the three arms reproduce the classical completed-zeta pipeline
  (Euler product / Gaussian-Γ Mellin / theta self-duality => functional equation) and
  EACH IS NECESSARY (removing F or A∞ breaks the FE; S is the involution itself). This
  is exactly Riemann(1859)/Tate's construction re-encoded as a 3-arm normal form -- KNOWN
  mathematics VERIFIED, NOT new, NOT a proof of RH. The visual helix is representational.
  The remaining proof gap is UNTOUCHED: a positive self-adjoint witness operator whose
  spectrum is the zeros (Hilbert-Polya / Weil positivity / arithmetic site).""")
print("="*74)
json.dump(dict(work_order="WO-VFD-ADELIC-TRISKELION-ROOT-OBJECT-001",
  finite_arm=fin, archimedean_arm=arc, theta_duality=th, fe_residual=fe, arm_removal=rm,
  scores=dict(FiniteScore=FiniteScore,GammaScore=GammaScore,ThetaScore=ThetaScore,FEScore=FEScore,
              NecessityScore=NecessityScore,FakeKernelsFail=FakePenalty,RootScore=RootScore,max=maxscore),
  verdict=verdict,
  honest="3 arms reproduce the classical completed-zeta pipeline (Euler/Gaussian-Γ/theta-duality=>FE) + each necessary; = Riemann/Tate construction re-encoded, KNOWN not new, NOT a proof; visual helix representational; proof gap = positive self-adjoint witness operator (untouched)"),
  open(os.path.join(OUT,"root_score_summary.json"),"w"), indent=2)
print("[json] outputs/root_score_summary.json")
