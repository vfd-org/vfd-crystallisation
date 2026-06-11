**1. Claim Audit**

- `docs/pentagonal-torsion-derivation.md:3-5` claims every step is proved or referenced. False. B8'/B9/B10 are partly sim output, not derivation-grade math.
- `:21-33` F1 and Theorem 1.1 are established by the quadratic formula.
- `:42-66` `O_K=Z[φ]`, σ, and the unit group are standard and mostly correct, but not “pure algebra from §1” in the strong sense. The unit-group proof needs the fundamental-unit argument, not just Dirichlet rank.
- `:91-110` pentagonal cyclotomy is basically correct, but the proof only checks `n=3,4,5,6` and omits the conductor theorem needed for “exactly when 5 | n.”
- `:125-154` norm parity `N(φ^n)=(-1)^n` is established. Calling this “pentagonal chirality” is stronger than the algebra proves.
- `:156-159` loop obstruction is conditional on an actual `Z[φ]^×` transport. That transport is not constructed.
- `:176-196` order distribution and chosen τ are locally sim-supported. But canonicity remains “up to choice between two order-10 classes.”
- `:198-209` `τ^5=-1` is established. The “closing a 5-fold loop” interpretation is not proved by the displayed cosine calculation.
- `:230-253` clock map cycle structure is established for a chosen order-10 τ.
- `:255-280` local-frame cocycle is not established. It is explicitly “BUILD REQUIRED” and conflicts with later Route Q-min `κ(v)` claims.
- `:282-289` argmin characterization is unproved and likely not true for the selected τ without extra hypotheses; the B5/B8 scripts choose an order-10 τ in shell 5, not the nearest shell.
- `:302-306` weighted Artin-Mazur zeta formula is correct once a multiplicative orbit weight exists. That weight is not supplied by §6.3.
- `:309-311` σ-symmetry is formal, but only after σ is defined on the correct substrate. It is not a B10 theorem.
- `:313-325` “factor as ζ(s)·L(s,χ5)” is not a well-defined test yet. No Mellin or Dirichlet map from this finite rational zeta to Dedekind ζ is defined.
- `:370-380` B8'/B9/B10 “sim-complete” is computationally true for the chosen κ script, but overclaimed as derivation. The 4-profile is observed, not proved inevitable.
- `:382-384` contradicts `:373`: it says ζ coefficients to degree 30 are still to be computed, but the sim prints them.
- `:392-394` “σ-fixed sub-lattice to Re(s)=1/2” is too strong. Local `rh-formal` says σ alone fixes only `s=1/2`; the critical line needs σ plus complex conjugation.

**2. WO Acceptance Audit**

- Goal 1, B8' `docs/codex-derive/pentagonal-clock-wo-B8prime-B10.md:8-9`: partially resolved. The script defines `κ(v)=(shell(v)-4)^2`; the derivation does not integrate it as the actual cocycle.
- Goal 2, B9 `:10`: mostly resolved computationally. Weights are `φ^K`, coefficients to degree 30 are printed exactly.
- Goal 3, B10 `:11-12`: not resolved. The script symmetrises coefficients; it does not prove `σ∘Tτ = Tσ(τ)∘σ` on `2I ⊔ σ(2I)`.
- B8' questions `:62-78`: route chosen, but minimality and canonicity are not proved. Distinguishable weights are computed.
- B9 deliverable `:80-88`: resolved for `W_i={φ^72,1,φ^52,φ^20}` and degree 30 coefficients; factorisation is just `φ^K`.
- B10 deliverable `:90-96`: only the integer σ-paired zeta is shown. Correct substrate theorem is absent.
- Required A-F output `:98-107`: not present in the reviewed derivation.
- Exact arithmetic constraint `:113-114`: satisfied by `derive_pentagonal_clock_B8p_proper.py`; not by older B7/B8, which uses float sorting at `derive_pentagonal_clock_B7_B8.py:92-100`.
- F1-chain constraint `:115-116`: not satisfied. κ is a chosen radial grade from shell indexing, not derived from F1.
- Out of scope `:121-123`: respected only in the WO. The derivation still gestures at Dedekind/Mellin conclusions without a built bridge.

**3. Catalogue Audit**

No pentagonal-clock math catalogue was supplied. The repo catalogues found are for observer-zeta, H-grad-1, and biology-rung. `cascade-h-grad-1-catalogue.md:67-71` explicitly says pentagonal holonomy belongs elsewhere, and `cascade-observer-zeta-catalogue.md:21` says the zeta object is “NOT DEFINED.” Therefore every new object in this derivation, including F1/Theorem 1.1 through B8'/B10 numerical results, is uncatalogued for this WO.

**4. Attribution / External Consistency**

- F1 is locally supported by `papers/cascade-correspondence-foundations/foundations.tex:116-152`, but that source explicitly limits F1’s scope at `:204-223`. It does not support “F1 derives Z[φ], icosians, zeta.”
- Paper XXII supports 2I closure and shell-class matching at `papers/paper-xxii/paper-xxii.tex:200-217`. It does not support “E8 double cover” language; `:238` prefers “two-to-one pairing” and rejects topological double-cover wording.
- `cascade-12d-closure.tex` does not support WO line `E8 ⊕ Z[φ]^4`; it states `L12=E8⊕M`, `M≅Oφ^2` at `:45-53`.
- B7/B8 supports the σ escape finding, but its own summary is wrong: `derive_pentagonal_clock_B7_B8.py:262-279` says σ does not preserve 2I, while `:371-373` prints “σ permutes 2I.”
- `rh-formal.tex:867-875` says σ’s holomorphic fixed set is one point, not the critical line; `:891-900` adds complex conjugation to get `Re(s)=1/2`.

**5. Sim Correctness**

The supplied sim correctly computes the advertised K-multiset and coefficient:
`{72:1, 0:1, 52:5, 20:5}` and `[z^10]ẑ = 1,114,945,460,806,394`.

It implements Route Q-min vertex weights, not the derivation’s local-frame holonomy cocycle. It also does not implement B10 σ-equivariance on `2I ⊔ σ(2I)`.

I checked all 24 order-10 elements, left and right multiplication: the same K-multiset appears every time. That strongly indicates a group-theoretic invariant, not a τ-enumeration accident. But the artefacts do not prove it; they hard-code the expected K-multiset at `derive_pentagonal_clock_B8p_proper.py:281-288`.

The Lucas factorisation is correct given even K:
`(1-φ^K u)(1-φ^{-K}u)=1-L_K u+u^2`.

The null comparison is weak. `derive_pentagonal_clock_B8p_proper.py:348-366` compares against a uniform `K=40` Lucas-shift null, not the actual naive cocycle null from B7/B8, which is `(1-z^10)^(-12)`. No χ²/KL/statistical comparison is present or needed.

**6. Tightness**

- Replace `docs/pentagonal-torsion-derivation.md:3-5` with: “Sections §1-§6 contain classical algebra plus build obligations; B8'/B9/B10 are currently exact computational findings.”
- Replace `:68` “Everything in §2 is forced by F1” with: “§2 uses classical quadratic-field arithmetic after F1 identifies φ.”
- Rename `:145` from “pentagonal chirality theorem” to “unit norm-parity theorem.”
- Replace `:255-280` or `:370-372`; they define incompatible cocycles.
- Replace `:382` “not open mathematically” with “not yet built.”
- Replace `:392-394` with: “Mellin/critical-line comparison requires σ plus complex conjugation and a zeta-specific transform.”

**7. Top Three Fixes**

1. `docs/pentagonal-torsion-derivation.md:255-280` and `:370-372`: choose one B8' object. Either local-frame holonomy or Route Q-min κ. Do not claim both.
2. `docs/pentagonal-torsion-derivation.md:370-380`: add a proof that the 4-profile K-multiset is forced by the shell class function and order-10 cosets. The sim is not a proof.
3. `docs/pentagonal-torsion-derivation.md:313-325`: remove the Dedekind escape claim until a Mellin/Dirichlet comparison map exists.

Next build should be **B11 Mellin-bridge first**. A B12 Dedekind audit without B11 can only say “not comparable yet,” not “escapes” or “reduces.”

**8. Verdict**

Publication ready: no.
