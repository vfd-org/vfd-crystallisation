"""Exact Q(sqrt5) arithmetic (WO-VFD-H4-E8-TRACE-FORM-003). Element = a + b*sqrt5,
a,b Fraction. phi=(1+sqrt5)/2. sigma: sqrt5->-sqrt5. Tr(x)=x+sigma(x)=2a."""
from fractions import Fraction as F
class G:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a=F(a); self.b=F(b)
    def __add__(s,o): return G(s.a+o.a, s.b+o.b)
    def __sub__(s,o): return G(s.a-o.a, s.b-o.b)
    def __mul__(s,o):
        if isinstance(o,G): return G(s.a*o.a+5*s.b*o.b, s.a*o.b+s.b*o.a)
        return G(s.a*o, s.b*o)
    def __neg__(s): return G(-s.a,-s.b)
    def __eq__(s,o): return s.a==o.a and s.b==o.b
    def __hash__(s): return hash((s.a,s.b))
    def conj(s): return G(s.a,-s.b)            # sigma
    def tr(s): return 2*s.a                    # Tr_{K/Q}
    def norm(s): return s.a*s.a-5*s.b*s.b       # field norm
    def f(s): return float(s.a)+float(s.b)*(5**0.5)
    def __repr__(s): return f"({s.a}+{s.b}v5)"
ZERO=G(0,0); ONE=G(1,0)
PHI=G(F(1,2),F(1,2))                            # (1+sqrt5)/2
def vdot(x,y): 
    s=G(0,0)
    for xi,yi in zip(x,y): s=s+xi*yi
    return s
def qmul(p,q):                                  # quaternion product over the field, p,q = (w,x,y,z) of G
    w1,x1,y1,z1=p; w2,x2,y2,z2=q
    return (w1*w2 - x1*x2 - y1*y2 - z1*z2,
            w1*x2 + x1*w2 + y1*z2 - z1*y2,
            w1*y2 - x1*z2 + y1*w2 + z1*x2,
            w1*z2 + x1*y2 - y1*x2 + z1*w2)
