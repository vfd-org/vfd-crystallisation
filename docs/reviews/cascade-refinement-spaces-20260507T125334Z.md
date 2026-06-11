Line numbers below refer to `papers/cascade-refinement-spaces/cascade-refinement-spaces.tex` unless marked P1/P2.

**1. Claim Audit**
- L430-440, Proposition “Refinement properties”: proves the stated set-inclusion, equivariance, and two-parent claims for the paper’s abstract construction. It does not prove that the datum is a genuine 2-dimensional cell complex in the usual sense: class-(a) subdividing edges L320-321 are not in any face boundary L331-337. If “cell-complex” is intended, this is under-specified.
- L583-591, “finite-dimensional real Hilbert spaces” and dimensions: established, assuming the imported fibre inner products are defined. The Clifford dagger form is not defined locally.
- L656-663, “bonding contractions”: established. Edge proof is loose by a factor but sufficient.
- L739-750, “adjoint relation”: established; the factor `1/2` in `j^1` is correct.
- L849-858, `X_cyl^0 \cong c_{00}`: established for vertex sector.
- L918-921, finite-level norm compatibility: established.
- L954-957, inverse-limit norm/inner-product limits: established for real Hilbert spaces.
- L975-989, `X_inv^0 \cong \ell^2(V_\infty;F^0)`: established.
- L1033-1040, density of `X_cyl^0`: established.
- L1106-1108, Coxeter unitarity: mathematically plausible for standard reflection representations, but the proof cites “P2 §§3--5” L1114 rather than a theorem/label that establishes orthogonality. Needs a precise classical or P2 citation.
- L1157-1172, mixed-form dimensions `36` vs real dimension `32`: correct and usefully qualified.
- L1202-1210, `sigma_n` is Q-linear and not R-linear: established by construction.
- L1224-1284, Theorem “Intertwining identities”: item (1) established; item (2) proves `p^1` but omits the adjunction step for `j^1`; item (3) is now directly proved for both `p^0` and `j^0`; item (4) is established only in the restricted sectorwise sense. The descent sentence L1275-1278 is imprecise because item (2) is edge-sector but the descent named is vertex-only.

**2. Internal Consistency**
- Main defect: the refinement datum is advertised as carrying 2-face data, but `E_{n+1}` contains subdividing edges L320-321 that never appear in `F_{n+1}` boundaries L331-337. Either allow “edges not incident to faces” explicitly, or change the face construction.
- Cross-references resolve; I found no undefined local `\ref`/`\eqref`.
- L1435-1437 says “refinement-σ (full)”; this conflicts with L1213-1217 and L1279-1284, where σ is vertex-sector, mixed-form only, with no edge or real-Hilbert σ action.
- L1393 writes `|_{\Q(\varphi)}` instead of the defined `|_{\Q(\varphi)/\Q}`.
- L819 says `j` is used “below for inverse-limit constructions”; the actual inverse-limit construction uses vertex restriction `p^0`, not edge `j^1`.

**3. External Consistency**
- P1 `def:sigma` verified: P1 L189-199 defines `σ(φ)=1-φ`.
- P1 `def:sigmaV` verified: P1 L297-307 defines coefficientwise `σ_V`. But bibliography L1513 incorrectly calls it `\S\texttt{def:sigmaV}`; it is a definition label, not a section.
- P1 `thm:pisigma-functorial` verified: P1 L590-610 proves functoriality for scalar extensions `T_K` of Q-linear maps. P3’s negative use is substantively right, but L1289-1292 overstates the source wording. The theorem does not literally state a “defined over the σ-fixed Q-form” hypothesis; that is P3’s interpretation for applying it to K-spaces.
- P2 `def:V600`, `def:V24`, `prop:24-in-600` verified: P2 L778-830.
- P2 `def:Cl-basis` and `def:octonions` verified: P2 L1672-1684 and L1717-1733. For the Q-forms used at L1134-1141, P2 `def:Q-forms` L1868-1884 is the cleaner citation and is currently missing.
- P2 `thm:icosian-closure` verified only for closure/group structure: P2 L964-970. It does not itself assert “Z[φ]-rational coordinates” as bibliography L1523-1534 suggests; that comes from `def:V600`/`def:icosian-ring`.
- L1114 “P2 §§3--5” and L1297 generic `\cite{AlgebraicSubstrate}` are stale citation forms. Use label-form citations.
- L1300-1301 claims a nontrivial H4 reflection “does not restrict to a Q-linear endomorphism of any Q-form.” That is stronger than shown. The needed claim is only that it does not preserve the chosen standard fixed `Q^4` form.

**4. Tightness**
- L302: replace “Schläfli refinement” with “abstract Schläfli-style refinement datum” unless the face/edge incidence issue is fixed.
- L1275: replace “The Coxeter intertwinings of (1)--(2) descend…” with “The vertex Coxeter intertwining of (1) descends…”
- L1289: replace “requires” with “applies here only when the map is a scalar extension of a Q-linear map on the chosen fixed Q-form.”
- L1300: replace “any Q-form” with “the chosen standard `Q^4` form.”
- L1435-1437: replace “refinement-σ (full)” with “refinement-σ for `p^0` and `j^0` on the mixed-form vertex sector.”

**5. Surface Issues**
- Undefined/underdefined `\dagger` in the Clifford inner product L517-519.
- Stale non-label citation: L1114.
- Notation slip: L1393 missing `/\Q`.
- Bibliography wording L1513 uses `\S` before a definition label.
- Bibliography L1523-1534 attributes coordinate rationality to `thm:icosian-closure`; cite `def:V600`/`def:icosian-ring` instead.

**6. Top Three Fixes**
1. Fix the refinement datum incidence problem at L317-339: either add the missing face structure involving subdividing edges, or explicitly weaken “cell-complex/Schläfli refinement” to an abstract graph-plus-selected-faces datum.
2. Tighten Theorem 8.3/handoff scope at L1233-1284 and L1435-1458: σ is mixed-form vertex-only; edge `j^1` needs the adjunction proof sentence; “full refinement-σ” must go.
3. Clean P1/P2 citation hygiene at L1114, L1289-1305, and L1513-1535: use exact labels, cite P2 `def:Q-forms`, and stop attributing coordinate rationality to `thm:icosian-closure`.
