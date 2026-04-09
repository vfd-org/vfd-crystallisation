# Proof: ΔC = 15 Is a Laplacian Eigenvalue of the 600-Cell

## The Claim

The leading-order mass exponent ΔC = 15 is simultaneously:
- the closure invariant difference C({2,3,4}) − C({1}) = 14 − (−1) = 15
- an eigenvalue of the 600-cell graph Laplacian, with multiplicity 16

## What Is Proven

### Part A: ΔC = 15 (arithmetic, exact)

C({1}) = 1 − 1 − 1 = −1

C({2,3,4}) = 2 × 3 × 4 − (2+3+4) − 1 = 24 − 9 − 1 = 14

ΔC = 14 − (−1) = **15**

Status: Exact arithmetic. No computation needed beyond multiplication.

### Part B: λ = 15 is a Laplacian eigenvalue (computational, exact)

The 600-cell vertex graph has 120 vertices whose coordinates are
known exactly (involving φ, 1/φ, φ/2, 1/(2φ)). Two vertices are
adjacent if their Euclidean distance equals the minimum nonzero
distance (= 1/φ on the unit 3-sphere). This gives a 12-regular
graph on 120 vertices with 720 edges.

The graph Laplacian L = D − A (where D = 12·I) is a 120×120
symmetric matrix with integer entries (since the adjacency matrix
has entries 0 or 1).

Direct eigenvalue computation yields 9 distinct eigenvalues:

| λ | Multiplicity | Algebraic form | Sum check |
|---|-------------|----------------|-----------|
| 0 | 1 | 0 | 1 |
| 2.2918 | 4 | 9 − 3√5 | 5 |
| 5.5279 | 9 | 12 − 4φ | 14 |
| 9 | 16 | 9 | 30 |
| 12 | 25 | 12 | 55 |
| 14 | 36 | 14 | 91 |
| 14.4721 | 9 | 4 + 4φ² | 100 |
| **15** | **16** | **15** | **116** |
| 15.7082 | 4 | 9 + 3√5 | 120 |

Total multiplicity: 1+4+9+16+25+36+9+16+4 = **120** ✓

**λ = 15 appears with multiplicity 16.** This is exact — the eigenvalue
is the integer 15, not an approximation.

### Verification protocol

This result is reproducible by anyone with standard linear algebra software:

1. Construct the 120 vertices of the 600-cell (coordinates from Coxeter 1963)
2. Build the adjacency matrix (edges at minimum distance)
3. Compute L = 12·I − A
4. Diagonalise L (120×120 symmetric integer matrix)
5. Observe eigenvalue 15 with multiplicity 16

The computation takes under 1 second on any modern computer.
Our code: `run_aria_self_spectral.py`

### Status

This is a **computational theorem**: the result is exact (integer eigenvalue,
integer multiplicity) and deterministically reproducible. It does not depend
on numerical precision, windowing, or parameter choices.

An algebraic proof via the representation theory of the H₄ Coxeter group
would be more satisfying but is not required for the paper. The eigenvalue
is verifiable by direct computation on a well-defined mathematical object.

---

## Part C: The Connection

The zeroth-order mass law states:

m_p/m_e = φ^{ΔC} = φ^{15}

We have shown:
- ΔC = 15 from closure invariant arithmetic (Part A)
- λ = 15 from the 600-cell Laplacian spectrum (Part B)

Therefore: **the mass exponent is a Laplacian eigenvalue of the 600-cell.**

This is a structural connection between:
- the combinatorial state-counting invariant (closure formula)
- the spectral structure of the underlying geometry (Laplacian eigenvalue)

### What this means for the paper

The mass law does not merely use an arbitrary combinatorial formula that
happens to give the right number. The number 15 appears independently in:
1. The composite-minus-separable-minus-vacuum state count
2. The eigenvalue spectrum of the polytope

These are different mathematical computations that produce the same integer.
The probability that this is coincidental can be bounded:

The 600-cell Laplacian has 9 distinct eigenvalues. The closure invariant
ΔC could in principle take any positive integer value (depending on shell
assignments). The probability that ΔC happens to equal one of the 9
distinct eigenvalues is 9/N where N is the range of plausible ΔC values.
For ΔC ∈ [1, 20] (the range giving mass ratios in the right order of
magnitude), the chance is 9/20 ≈ 45%. This is NOT vanishingly small.

**Honest assessment:** The λ = 15 connection is real and striking, but not
statistically overwhelming on its own. Its force comes from being PART of
a larger structure (the three-order expansion, the φ-exponential law, the
connected state counting) rather than standing alone.

### What this does NOT prove

- It does not prove that mass IS the spectral gap (that remains a framework postulate)
- It does not prove that the 600-cell IS the relevant geometry (that is a modelling postulate)
- It does not prove that the corrections |E|/|V| and Var(deg) are also eigenvalue-related

### What would strengthen it further

1. Show that the correction terms (2/3 and 4/81) also appear in the
   eigenvalue structure (e.g., as eigenvalue spacings or ratios)
2. Prove the connection algebraically via H₄ representation theory
3. Show that 15 is not just AN eigenvalue but THE eigenvalue selected
   by some natural spectral criterion (e.g., the eigenvalue closest to
   ΔC for ALL valid shell assignments)

---

## Additional observations about the spectrum

### λ = 14 has multiplicity 36 (the largest)

ΔC for {1,2,3,4} = C({1,2,3,4}) − C({1}) = 13 − (−1) = **14**. This is also
a Laplacian eigenvalue (the one with the largest multiplicity).

### λ = 0 matches ΔC for single shells

For any single shell {k}: ΔC = C({k}) − C({1}) = −1 − (−1) = **0**. And
λ = 0 is the smallest Laplacian eigenvalue. Single shells have zero closure
difference, matching the zero eigenvalue.

### Pattern: ΔC is an eigenvalue for small supports

| Support S | ΔC | Is ΔC a Laplacian eigenvalue? |
|-----------|----|-----------------------------|
| {k} (any single) | 0 | **YES** (λ₀ = 0) |
| {1,2,3,4} | 14 | **YES** (λ = 14, mult 36) |
| {2,3,4} | 15 | **YES** (λ = 15, mult 16) |
| {2,3} | 1 | no |
| {3,4} | 5 | no |
| {4,5} | 11 | no |
| {3,4,5} | 48 | no (outside spectral range) |

Three of the seven connected supports with ΔC in [0, 15.7] match
Laplacian eigenvalues. For supports with large ΔC (> 15.7), matching
is impossible since the Laplacian's maximum eigenvalue is ~15.71.

The matching for ΔC = 0, 14, and 15 — which includes both the electron
reference and the proton — is exact.
