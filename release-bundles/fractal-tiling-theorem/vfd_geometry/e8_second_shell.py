"""Second icosian shell for the H4->E8 trace-form bridge (WO-...-004).
shell_2 = (1/phi)*shell_1 = (phi-1)*shell_1. Reason: B=2(p+q) for <x,x>=p+q√5;
B-norm 2 <=> p+q=1. units: <x,x>=1=(1,0) [p+q=1]. (1/phi)x: <,>=1/phi^2=(3-√5)/2
=(3/2,-1/2) [p+q=1] -> norm 2. (phi)x: phi^2=(3+√5)/2 [p+q=2] -> norm 4 (the prior fail).
1/phi=phi-1 in Z[phi], so x/phi stays an icosian."""
from golden_field import G, PHI, ONE, ZERO, vdot
INV_PHI = PHI + G(-1,0)        # 1/phi = phi - 1 = G(-1/2,1/2)
def scale(v, s): return tuple(x*s for x in v)
def second_shell(shell1): return [scale(v, INV_PHI) for v in shell1]
C=G(1, __import__('fractions').Fraction(1,5))     # c = 1 + (1/5)√5
def B(x,y): return (C*vdot(x,y)).tr()
