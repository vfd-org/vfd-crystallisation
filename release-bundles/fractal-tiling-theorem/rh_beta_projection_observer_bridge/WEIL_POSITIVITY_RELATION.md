# Deliverable F — relation to Weil positivity

## Does the β-projection problem reduce to Weil positivity?

**Yes, for the part that touches RH.** The chain is:

1. The β=4→β=2 *symmetry-class* projection is canonical (complexification) and
   **independent of RH** — it neither needs nor yields Weil positivity. It is
   pure algebra (`ℍ⊗ℂ=M₂(ℂ)`), and it is zero-blind.
2. The β=2 that actually matters — the **GUE spacing of the zeta zeros** — is a
   property of the analytic zeros. The only non-circular object that reaches it
   from the arithmetic side is the explicit formula, and its RH content is the
   **Weil positivity** `W(h) ≥ 0 ∀h ⇔ RH` (built in the sibling WO,
   `weil_wall.py`).

So the genuine question "does the β=4 substrate become the β=2 zero spectrum?"
factors as:

```
β=4 (symplectic symmetry)  --complexify-->  β=2 (unitary symmetry)   [algebra, RH-free]
                                                   |
                                                   |  (no canonical spacing map)
                                                   v
β=2 GUE spacing of the actual zeros  <==  Weil positivity / explicit formula  [= RH]
```

## Answers to the WO's five questions

1. **Does projecting β=4→β=2 require positivity of a Weil-type form?** For the
   *symmetry-class* projection, no. For reaching the *zeros*, yes — that step is
   Weil positivity.
2. **Does the projection become canonical only under `Q[h]≥0`?** The
   complexification is already canonical (RH-free). The zero-reaching map is
   *defined* by the explicit formula and is positive **iff** RH.
3. **Is the β-transition equivalent to a known RH criterion?** The
   zero-reaching half is exactly Weil positivity. The algebraic half is not an
   RH criterion at all.
4. **Does it add anything beyond Weil positivity?** It **clarifies** that the
   β-mismatch is two separate things — an RH-free algebra step (real, done) and
   an RH-equivalent analytic step (Weil, open) — and that conflating them as a
   single "GSE→GUE spacing" projection is a category error. It does not add a new
   route through the positivity wall.
5. **Does it identify the missing positivity mechanism?** It localises it
   precisely: not in the β-class (that complexifies for free), but in the
   archimedean/adelic completion that would make the **complexified** operator
   act self-adjointly on the **zeros** — i.e. the Hilbert–Pólya completion,
   `ADELIC_SCALING.md` Tier-3.

## Verdict

The β-bridge **collapses to Weil positivity** for everything RH-relevant. Its
genuinely new content is negative-but-useful: the β=4/β=2 obstruction is **not**
a fatal spacing mismatch and **not** a new bridge — it is an RH-free
complexification plus the same Weil wall. Stated honestly, this is progress of
the "sharpen the obstruction" kind, not of the "cross it" kind.
