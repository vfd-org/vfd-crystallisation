"""WO-VFD-INVARIANT-TRACE-FORM-LAW-001 — comparative synthesis of three closure cases
under one lens: self-adjointness/positivity/integrality is FORM-RELATIVE. Honest
grading: H4->E8 = form-completion SOLVES closure; RH = right form known but closure
(positivity)=RH still OPEN (counterexample to 'right form => closure'); horizon = analogy."""
import json
from invariant_trace_form import TraceFormClosureCase, form_relative_selfadjointness_demo

A=TraceFormClosureCase(
  case="H4_E8",
  domain_space="H4/600-cell roots = icosians over Q(sqrt5)",
  naive_form="naive Euclidean embedding x->(x, sigma x)",
  naive_failure="inner products include +-1/2; not even-integral E8",
  completed_form="B(x,y)=Tr_{Q(sqrt5)/Q}(c.<x,y>), c=1+1/sqrt5",
  completion_term="golden trace factor c=1+1/sqrt5 (Tr c=2)",
  corrected_property="shell1 U (1/phi)shell1 = 240 roots, norm^2=2, ips{-2..2}, even integral E8 (56,56,126,1,1)",
  self_adjoint_or_positive="proved (exact arithmetic; canonical E8 matched)",
  residual_before="nonintegral inner products (+-1/2)",
  residual_after="0 nonintegral; exact E8",
  canonical_derived_not_tuned=True,
  closure_delivered_by_form=True,         # <-- the form COMPLETION actually closes it
  limits="known Wilson/Moody-Patera construction, VERIFIED not discovered")

B=TraceFormClosureCase(
  case="RH_Weil_Connes",
  domain_space="prime-pressure / test-function (Weil-Connes) space",
  naive_form="Li/Toeplitz moment kernel; prime-only Euler product; no-Gamma",
  naive_failure="naive kernels not PSD; prime-only diverges at s=1; smooth-PNT over-capacity (mu=1.26>1)",
  completed_form="completed Weil/Connes quadratic form D=H-R, H=A(arch Gamma)+P(pole)",
  completion_term="archimedean place (Gamma/digamma) + pole correction",
  corrected_property="H PSD after pole lift; K=H^-1/2 R H^-1/2; RH <=> ||K||<=1; finite compressions PSD",
  self_adjoint_or_positive="finite_validated; FULL-LIMIT POSITIVITY = RH, OPEN",
  residual_before="non-PSD naive kernels; divergence",
  residual_after="finite-cutoff PSD validated; full-limit positivity UNRESOLVED (=RH)",
  canonical_derived_not_tuned=True,
  closure_delivered_by_form=False,        # <-- KEY: right form known, closure NOT delivered = RH stands
  limits="the correct/canonical form is identified (the explicit formula) but does NOT prove positivity; RH is the standing COUNTEREXAMPLE to 'right form => closure'")

C=TraceFormClosureCase(
  case="Horizon_Scattering",
  domain_space="Poschl-Teller QNM / horizon wave scattering (toy)",
  naive_form="static geometry / compressed-funnel shape / mode counting",
  naive_failure="static geometry is cosmetic (radius bijective); no new invariant",
  completed_form="scattering determinant / Jost function + boundary flux form",
  completion_term="horizon boundary condition / greybody (Gamma-ratio) factor",
  corrected_property="Gamma-determinant -> digamma response -> resonances; damped QNMs for real(self-adjoint) potential",
  self_adjoint_or_positive="toy_validated; arithmetic instance = self-adjointness = Hilbert-Polya = RH (analogy_only, no proof transfer)",
  residual_before="no stable geometry invariant",
  residual_after="shared determinant/log-derivative architecture with arithmetic; NO proof transfer",
  canonical_derived_not_tuned=False,
  closure_delivered_by_form=False,
  limits="analogy/known scattering framework; toy provable because real potential; arithmetic self-adjointness OPEN")

cases=[A,B,C]
demo=form_relative_selfadjointness_demo()
print("="*78); print("WO-VFD-INVARIANT-TRACE-FORM-LAW-001  comparative synthesis"); print("="*78)
print("\n[Concrete anchor] self-adjointness is FORM-RELATIVE (exact):")
print(f"  mult-by-phi  T={demo['T']}  symmetric under NAIVE form: {demo['naive_symmetric']}")
print(f"  B*T={demo['BT']}  symmetric => SELF-ADJOINT under trace form B=Tr(xy): {demo['B_self_adjoint']}")
print("  -> the SAME operator is non-symmetric naively, self-adjoint in the trace form. Form-relative.")

print("\n[Comparative matrix]")
hdr=f"{'case':18}{'completion term':34}{'corrected':16}{'closure by form?':17}{'status'}"
print(hdr); print("-"*len(hdr))
for c in cases:
    print(f"{c.case:18}{c.completion_term[:33]:34}{c.corrected_property.split(';')[0][:15]:16}"
          f"{str(c.closure_delivered_by_form):17}{c.self_adjoint_or_positive.split(';')[0]}")

print("""
[Candidate VFD law -- honest form]
 LENS (supported): self-adjointness / positivity / integrality is FORM-RELATIVE.
   A naive failure (fractional residual, non-PSD kernel, cosmetic geometry) can be a
   wrong-form artefact; completing to the canonical invariant trace/flux form can
   convert apparent leakage into closed structure.
 EXACT EXEMPLAR: H4->E8. The golden trace form c=1+1/sqrt5 is DERIVED (not tuned)
   and the completion DELIVERS closure (exact even-integral E8).
 CRUCIAL LIMIT (RH counterexample): having the canonical form is NECESSARY, NOT
   SUFFICIENT. The completed Weil/Connes form IS the canonical arithmetic form and is
   finite-positive, yet full positivity = RH and stays OPEN. So 'right form => closure'
   is FALSE in general. The law is a LENS + a search heuristic, NOT a closure guarantee.
 HEURISTIC VALUE: it sharpens the RH operator search to 'find the canonical arithmetic
   trace form making the prime-pressure operator self-adjoint' -- but RH shows that is
   the hard problem, not a shortcut.
 GRADING: H4/E8 = EXACT (closure delivered); RH = STRONG-but-OPEN (form right, closure not);
   horizon = ANALOGY (known scattering framework, no transfer).
""")
print("Defensible law version: v1/v2 (form-relativity + completion CAN repair failures),")
print("NOT v3-as-guarantee. Closure = structure + symmetry + correct form, where 'correct")
print("form' is necessary; sufficiency is system-specific (exact for H4/E8, = RH for primes).")

res=dict(work_order="WO-VFD-INVARIANT-TRACE-FORM-LAW-001",
  concrete_demo=dict(operator="mult-by-phi on Q(sqrt5)", naive_symmetric=demo['naive_symmetric'],
     trace_form_self_adjoint=demo['B_self_adjoint'], point="self-adjointness is form-relative (exact)"),
  cases=[c.dict() for c in cases],
  law=dict(
     lens="self-adjointness/positivity/integrality is FORM-RELATIVE; completion to the canonical invariant trace/flux form can repair a naive failure",
     exact_exemplar="H4->E8 (golden trace form c=1+1/sqrt5, derived, delivers closure)",
     crucial_limit="right form is NECESSARY not SUFFICIENT; RH is the counterexample (canonical Weil/Connes form known + finite-positive, full positivity=RH open)",
     defensible_version="v1/v2 (form-relativity + repair), NOT v3-as-guarantee",
     strength_by_case=dict(H4_E8="exact", RH="strong_but_open", horizon="analogy")),
  recommended_next=["WO-RH-ARITHMETIC-TRACE-FORM-SEARCH-001 (find canonical arithmetic trace form behind Weil/Connes; necessary not sufficient per RH limit)",
     "WO-VFD-SELF-ADJOINT-FOLDING-ENGINE-002 (search invariant forms making transformations self-adjoint -- generalises the mult-by-phi demo)",
     "WO-VFD-H4-E8-FORMAL-PAPER-004 (write the one EXACT exemplar up, cite Wilson/Moody-Patera)"])
json.dump(res, open("results/invariant_trace_form_law_001/result.json","w"), indent=2, default=str)
print("[json] results/invariant_trace_form_law_001/result.json")
