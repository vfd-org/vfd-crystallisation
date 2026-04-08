# Base Ratio Derivation from Closure-Class Complexity

## Definitions (from Paper II)

Closure-class complexity:
    C(A) = prod(shells) - sum(shells) - 1

Electron class A_e: shells = {1}
    C(A_e) = 1 - 1 - 1 = -1

Proton class A_p: shells = {2,3,4}
    C(A_p) = 24 - 9 - 1 = 14

## Base Ratio

If mass scales as phi^C(A):
    m_p / m_e = phi^(C_p) / phi^(C_e) = phi^(C_p - C_e) = phi^(14-(-1)) = phi^15

phi^15 = 1364.000...

Observed: 1836.15267...
Error: 25.7%

## What is derived

1. The shell assignments {1} and {2,3,4} follow from five tested rule families.
2. C(A) is a pure integer determined entirely by shell occupancy.
3. Delta C = 15 follows algebraically. No choices, no fitting.
4. phi enters from the manifold structure (the scale hierarchy).

## What is NOT derived

1. Why mass should scale as phi^C rather than some other function of C.
2. Whether C is the correct class invariant for mass, as opposed to another
   shell-derived quantity (shell sum, product, energy sum, etc.).
3. Any correction beyond phi^15.

The choice "mass ~ phi^C" is the simplest exponential scaling consistent with
the phi-manifold. But it is a modelling choice, not a theorem.
