"""Invariant Trace-Form Closure — abstract schema + a concrete exact demonstration
that self-adjointness is FORM-RELATIVE (WO-VFD-INVARIANT-TRACE-FORM-LAW-001)."""
from dataclasses import dataclass, asdict
from fractions import Fraction as F
import numpy as np
@dataclass
class TraceFormClosureCase:
    case: str
    domain_space: str
    naive_form: str
    naive_failure: str
    completed_form: str
    completion_term: str
    corrected_property: str
    self_adjoint_or_positive: str   # proved | finite_validated | open | toy_validated | analogy_only
    residual_before: str
    residual_after: str
    canonical_derived_not_tuned: bool
    closure_delivered_by_form: bool # KEY: does completing the form actually CLOSE it?
    limits: str
    def dict(self): return asdict(self)

def form_relative_selfadjointness_demo():
    """mult-by-phi on Q(sqrt5) (basis {1, sqrt5}): NOT symmetric under naive form,
    but self-adjoint under the trace form B(x,y)=Tr(xy). Concrete, exact."""
    # phi = 1/2 + 1/2 sqrt5. T = matrix of (mult by phi) on basis {1, sqrt5}:
    #   phi*1   = 1/2 + 1/2 sqrt5  -> column (1/2, 1/2)
    #   phi*sqrt5 = 5/2 + 1/2 sqrt5 -> column (5/2, 1/2)
    T=np.array([[F(1,2),F(5,2)],[F(1,2),F(1,2)]])
    # trace form B on {1,sqrt5}: B(1,1)=Tr(1)=2, B(1,sqrt5)=Tr(sqrt5)=0, B(sqrt5,sqrt5)=Tr(5)=10
    B=np.array([[F(2),F(0)],[F(0),F(10)]])
    naive_symmetric = bool(np.array_equal(T, T.T))
    BT=B@T
    Bsa = bool(np.array_equal(BT, BT.T))     # B-self-adjoint <=> B T symmetric (B symmetric)
    return dict(T=[[str(x) for x in r] for r in T], naive_symmetric=naive_symmetric,
                BT=[[str(x) for x in r] for r in BT], B_self_adjoint=Bsa)
