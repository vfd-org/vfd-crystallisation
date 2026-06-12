# Deliverable E — observer-compatibility formalism

## The observer map, mathematically

Stripped of interpretation, the "observer" `O: bulk arithmetic geometry → spectral
data on the critical line` is one of the standard reductions, and the experiments
say **which one it is and is not**:

| candidate meaning of `O` | is it the observer map? | why |
|---|---|---|
| choice of complex structure (`ℍ→ℂ`) | **partial** | canonical (complexification), changes β=4→β=2 *symmetry*, but zero-blind |
| boundary trace | no | loses doubling but yields no zero-spectrum |
| quotient `ψ∼Jψ` | no | removes Kramers degeneracy; spacing stays β=4 |
| test-function selection | **yes, effectively** | the Weil test functions `h` are exactly the "observable" degrees of freedom |
| spectral projection to the zeros | this **is** RH | no construction; it is the unknown Hilbert–Pólya operator |
| the explicit formula | **yes** | the genuine prime→zero map; but it *is* RH content |

So the only mathematically honest "observer" that reaches the zeros is **the
explicit formula / Weil pairing** — and that is the RH-equivalent object, not a
new reduction.

## What is lost and preserved under observation

- **Preserved:** the reduced trace / norm (arithmetic data), self-adjointness,
  positivity of the coefficient-side form.
- **Lost:** the quaternionic (β=4) antiunitary `J` (it leaves the commutant under
  complexification); the Kramers doubling.
- **Never gained:** zero-sensitivity. No observed object computed here becomes a
  function of the zero locations without invoking the explicit formula.

## Why would β=4 become β=2?

At the **symmetry-class** level it does, canonically: complexification
`ℍ⊗_ℝℂ ≅ M₂(ℂ)` turns the symplectic class into the unitary class (the antiunitary
`T` with `T²=−1` ceases to be a symmetry). This is a theorem of algebra, not of
RH. At the **spacing** level it does **not** become β=2 by any canonical map
(distinct universality classes), and the substrate has no GSE spacing anyway.

## Is the observer map canonical?

- Complexification: **canonical** (unique up to conjugacy), but zero-blind.
- The zero-reaching observer (explicit formula / Weil): canonical **and**
  RH-equivalent — i.e. it is the wall, not a step through it.

## Theorem template and its status

```
O(H_{β=4})  ≅  H_{β=2}              -- TRUE as symmetry classes (complexification), zero-blind
Stats(O(R_{β=4})) ≈ Stats_GUE       -- FALSE/undefined: R_{β=4} (icosian) has no GSE spacing,
                                       and no canonical projection produces GUE spacing
```

The observer that would put the **zeros** on a β=2 self-adjoint footing is the
Hilbert–Pólya operator — open, with the `ADELIC_SCALING.md` archimedean completion
as the missing piece.
