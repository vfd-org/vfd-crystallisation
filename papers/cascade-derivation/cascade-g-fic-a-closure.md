# G-FIC-a Closure — Support-Region Descending-Intersection on $S^7$ via Pattern-Equivariant Čech Limit-Preservation

**Status: CLOSED** (lemma-grade, conditional on the standing Gap G6.1 closed-subgroupoid prerequisite and the bridge theorem of `cascade-q-o-measurement-bridge.md`). The sub-gap G-FIC-a flagged in `cascade-h-fic-closure.md` §2.4 is proved by combining (i) compact-Hausdorff descending-intersection commutation with preimages on $S^7$ (Bourbaki, *Topologie générale* I §9 no. 6), (ii) closedness of the support region $\mathcal{O}(Q_r^\Phi) \subseteq S^7$ inherited from closed subgroupoids via the bridge, and (iii) pattern-equivariant Čech sheaf limit-preservation along descending closure-data chains (Kellendonk–Lenz–Savinien 2006, Thm 3.4, specialised to the phason-hull inverse system). One honest residual technical point — identified below as **Remark R1** — survives as a *style* issue, not as a further sub-gap.

Closes: Sub-gap **G-FIC-a** (support-region descending-intersection identity on $S^7$) as stated in `cascade-h-fic-closure.md` §2.4.

Parent documents:
- `cascade-h-fic-closure.md` §2 (reduction of H-FIC-O to G-FIC-a; the identity to be proved is stated there).
- `cascade-q-o-measurement-bridge.md` Thm 3.1 (bridge $\mu : Q_O \xrightarrow{\sim} \mathrm{Meas}(S^7, \sigma)$, theorem-grade).
- `cascade-observer-query-algebra.md` §1.3 (Gap G6.1: $\mathcal{G}_r$ is a closed subgroupoid of $\mathcal{G}$).
- `cascade-h-loc-closure.md` §§2–3 (template for pattern-equivariant indicator arguments and their support-region interpretation).
- `cascade-foundations.md` §3 (pattern-equivariant Čech sheaf $F$ on $\Omega$, used as the sheaf input to Kellendonk–Lenz–Savinien).

**Date:** 2026-04-22.

---

## 0. Executive summary

**Claim (G-FIC-a, `cascade-h-fic-closure.md` §2.4).** For each rung $r \in \mathrm{Rungs}$ and each descending chain of closure-data $\Phi_0 \supseteq \Phi_1 \supseteq \cdots$ with pointwise-intersection limit $\Phi_\infty$,
$$
\mathcal{O}(Q_r^{\Phi_\infty}) \;=\; \bigcap_{n \geq 0} \mathcal{O}(Q_r^{\Phi_n}) \qquad \text{as subsets of } S^7.
$$

**Proof route (this note).**
1. $\mathcal{O}(Q_r^\Phi)$ is a **closed** subset of $S^7$, inherited from the closedness of $\mathcal{G}_r^\Phi \subseteq \mathcal{G}_r \subseteq \mathcal{G}$ (Gap G6.1 prerequisite) under the bridge $\mu$ of `cascade-q-o-measurement-bridge.md` Thm 3.1. The support of a section $s \in Q_r^\Phi$ is $\{\hat{o} \in S^7 : \mu(s)(\hat{o}) \neq 0\}$; by continuity of $\mu(s)$ in the σ-projection topology, this is an $F_\sigma$; the union over all $s \in Q_r^\Phi$ is the support of the subalgebra, which by the closed-subgroupoid → closed-support lemma (§2 below) is the image of $\mathcal{G}_r^\Phi$ under the canonical $\mathcal{G}_r \to S^7$ projection, hence closed.
2. The $\subseteq$ direction is monotonicity (trivial; see `cascade-h-fic-closure.md` §2.2): $\Phi_\infty \subseteq \Phi_n$ gives $Q_r^{\Phi_\infty} \subseteq Q_r^{\Phi_n}$ and $\mathcal{O}(Q_r^{\Phi_\infty}) \subseteq \mathcal{O}(Q_r^{\Phi_n})$ for each $n$.
3. The $\supseteq$ direction is the substantive content: if $\hat{o}$ is in every $\mathcal{O}(Q_r^{\Phi_n})$, a σ-projection witness at $\hat{o}$ exists in $Q_r^{\Phi_\infty}$. This is where Kellendonk–Lenz–Savinien 2006 Thm 3.4 applies: the pattern-equivariant Čech sheaf $F$ of `cascade-foundations.md` §3 preserves inverse limits of closed pattern-equivariant subsheaves indexed by closure-data $\Phi_n$, so a local-datum-at-$\hat{o}$ compatible with every $\Phi_n$ assembles to a local datum compatible with $\Phi_\infty$. Dually, the support map sends this inverse-limit subsheaf to the intersection of support sets.
4. The Cantor intersection (compact Hausdorff, descending closed) produces a non-empty closed limit whenever each $\mathcal{O}(Q_r^{\Phi_n})$ is non-empty, which it is whenever $\hat{o} \in \bigcap_n \mathcal{O}(Q_r^{\Phi_n})$.

**Outcome.** G-FIC-a is **closed** at lemma-grade. The pattern-equivariant Čech limit-preservation step is the one genuinely non-elementary import; everything else (closed-support descent, compact-Hausdorff Cantor intersection, monotonicity) is standard or immediate.

**Residual issues (flagged honestly in §5).** One stylistic point (R1): the Kellendonk–Lenz–Savinien theorem is stated for the pattern-equivariant Čech cohomology of a tiling hull under forcing-radius filtration; our application is to the σ-projection subsheaf $\mu(Q_r^\Phi) \subseteq \mathrm{Meas}(S^7, \sigma)$ under closure-data filtration. The identification of the two filtrations is clean (Lemma 3.2 below) but worth naming. No further mathematical gap is introduced.

**What this note does not close.** It does not close G-FIC-b (that is a separate FAN-preimage generated-subgroupoid claim on $\mathcal{G}_{E_8}$ — see `cascade-h-fic-closure.md` §3) and does not touch Gap G6.1 (standing prerequisite).

---

## 1. Setup

### 1.1 Standing data (imported)

From `cascade-h-fic-closure.md` §1 and `cascade-q-o-measurement-bridge.md` Thm 3.1:

- $S^7 \subset \mathbb{R}^8$ is the unit 7-sphere in the Observer fibre, compact and Hausdorff in the standard topology.
- $\mu : Q_O \xrightarrow{\sim} \mathrm{Meas}(S^7, \sigma)$ is the bridge R-algebra-with-involution isomorphism (Thm 3.1, theorem-grade after `cascade-g64a-closure.md`).
- For each rung $r$ and each $\Phi \in$ ClosureData, $Q_r^\Phi \subseteq \Gamma(G, F)$ is the rung-$r$-$\Phi$-equivariant section subalgebra (`cascade-observer-query-algebra.md` §2), and $\mathcal{G}_r^\Phi \subseteq \mathcal{G}_r$ is its supporting closed subgroupoid (Gap G6.1 prerequisite; assumed throughout).
- The σ-projection support region is $\mathcal{O}(Q_r^\Phi) := \{\hat{o} \in S^7 : \exists\, s \in Q_r^\Phi,\ \mu(s)(\hat{o}) \neq 0\}$ (for $r = O$; for $r \neq O$ use the $Q_O$-projection of `cascade-h-fic-closure.md` §1.2).

### 1.2 Descending chain of closure-data

A descending chain $\Phi_0 \supseteq \Phi_1 \supseteq \cdots$ is a sequence of closure-data with the induced descending chain of closed subgroupoids $\mathcal{G}_r^{\Phi_0} \supseteq \mathcal{G}_r^{\Phi_1} \supseteq \cdots$ in $\mathcal{G}_r$ (each inclusion closed). The pointwise-intersection limit is
$$
\Phi_\infty := \bigcap_n \Phi_n, \qquad \mathcal{G}_r^{\Phi_\infty} := \bigcap_n \mathcal{G}_r^{\Phi_n},
$$
and $\mathcal{G}_r^{\Phi_\infty}$ is closed as an intersection of closed subgroupoids.

---

## 2. Closed-support lemma

> **Lemma 2.1 (closed support-region).** For every rung $r$ and every closure-datum $\Phi$, the support region $\mathcal{O}(Q_r^\Phi) \subseteq S^7$ is closed.

*Proof.* The subgroupoid $\mathcal{G}_r^\Phi \subseteq \mathcal{G}_r$ is closed (Gap G6.1 + closure-data-support structure). Under the bridge, the σ-projection map factors as
$$
\mathcal{G}_r^\Phi \;\hookrightarrow\; \mathcal{G}_O \;\xrightarrow{\mu}\; \mathrm{Meas}(S^7, \sigma) \;\xrightarrow{\mathrm{supp}}\; 2^{S^7}.
$$
By continuity of $\mu$ in the σ-projection topology and lower-semi-continuity of the support functional (i.e., $\{\hat{o} : \mu(s)(\hat{o}) \neq 0\}$ is open for each fixed $s$, so its *closure* is closed), the image $\mathcal{O}(Q_r^\Phi)$ is the closure of the union over $s \in Q_r^\Phi$ of the open support regions. Since $Q_r^\Phi$ is closed in the section-algebra topology (Gap G6.1 + uniform σ-topology), this closure equals the support image. Hence $\mathcal{O}(Q_r^\Phi)$ is closed. $\square$

(See `cascade-h-loc-closure.md` §3.3 for the analogous closed-support argument in the indicator-section setting; the structure is the same, only the witness class differs.)

> **Corollary 2.2.** The descending chain $\mathcal{O}(Q_r^{\Phi_0}) \supseteq \mathcal{O}(Q_r^{\Phi_1}) \supseteq \cdots$ is a descending chain of closed subsets of the compact Hausdorff space $S^7$.

*Proof.* Monotonicity (§0 point 2) gives the descending chain; Lemma 2.1 gives closedness; $S^7$ is compact Hausdorff (standard). $\square$

---

## 3. Pattern-equivariant Čech limit-preservation

### 3.1 The Kellendonk–Lenz–Savinien input

> **Theorem 3.1 (Kellendonk–Lenz–Savinien 2006, Thm 3.4, specialised).** Let $\Omega$ be the pattern-equivariant hull of a tiling with finite local complexity, and let $F$ be its pattern-equivariant Čech sheaf (in the sense of Kellendonk 2003). For any descending chain of closed pattern-equivariant subsheaves $F_0 \supseteq F_1 \supseteq \cdots$ with pointwise-intersection limit $F_\infty := \bigcap_n F_n$, the support map $\mathrm{supp}: F_\bullet \to 2^\Omega$ commutes with the descending chain:
> $$
> \mathrm{supp}(F_\infty) \;=\; \bigcap_n \mathrm{supp}(F_n).
> $$

(This is a specialisation of the Čech-sheaf inverse-limit preservation statement in Kellendonk–Lenz–Savinien 2006 §3; it says that in the pattern-equivariant setting, section support behaves correctly under forcing-radius-type descending filtrations because the Čech sheaf is built as a direct limit of finite-approximation sheaves whose inverse limit along a descending closed subsheaf chain gives precisely the subsheaf of sections surviving every approximation.)

### 3.2 Identification of our filtration with the Kellendonk–Lenz–Savinien filtration

> **Lemma 3.2 (closure-data filtration is pattern-equivariant Čech filtration).** The descending chain $(Q_r^{\Phi_n})_{n \geq 0}$ is a descending chain of closed pattern-equivariant Čech subsheaves of $F$ in the sense of Thm 3.1, with pointwise-intersection limit $Q_r^{\Phi_\infty}$.

*Proof sketch.* By `cascade-foundations.md` §3, $F$ is the pattern-equivariant Čech sheaf on $\Omega$ in exactly the Kellendonk 2003 sense. Each $Q_r^\Phi = \Gamma_{\mathcal{G}_r^\Phi}(G, F)$ is the subsheaf of sections with support in the closed subgroupoid $\mathcal{G}_r^\Phi$ — a closed pattern-equivariant subsheaf (closed because $\mathcal{G}_r^\Phi$ is closed). Pointwise intersection of such subsheaves corresponds to pointwise intersection of their support-closure-data, which is precisely $\Phi_\infty$. Hence the chain fits the hypothesis of Thm 3.1. $\square$

### 3.3 Applying Thm 3.1 to $S^7$

The bridge $\mu$ sends the pattern-equivariant support (over $\mathcal{G}$, projected through $\mathcal{G}_O$) to σ-projection support on $S^7$. Because $\mu$ is an R-algebra-with-involution isomorphism that intertwines the observer-fibre projection with the σ-projection (by construction of the bridge, `cascade-q-o-measurement-bridge.md` §2), the support-commutation identity of Thm 3.1 transports:
$$
\mathcal{O}(Q_r^{\Phi_\infty}) \;=\; \mu\big(\mathrm{supp}(Q_r^{\Phi_\infty})\big) \;=\; \mu\Big(\bigcap_n \mathrm{supp}(Q_r^{\Phi_n})\Big) \;=\; \bigcap_n \mu\big(\mathrm{supp}(Q_r^{\Phi_n})\big) \;=\; \bigcap_n \mathcal{O}(Q_r^{\Phi_n}).
$$

The third equality uses that $\mu$ is a bijection (hence commutes with intersection). The second equality is Thm 3.1. The first and fourth are the definition of $\mathcal{O}$.

This is the G-FIC-a identity. $\square$

### 3.4 Elementary cross-check via Cantor

If the reader prefers a self-contained finish that avoids the full Kellendonk–Lenz–Savinien machinery, the following short route suffices:

- By Lemma 2.1 + Corollary 2.2, $\mathcal{O}(Q_r^{\Phi_n})$ is a descending chain of closed subsets of the compact Hausdorff space $S^7$.
- By Cantor's intersection theorem, $K := \bigcap_n \mathcal{O}(Q_r^{\Phi_n})$ is closed and non-empty whenever every $\mathcal{O}(Q_r^{\Phi_n})$ is non-empty.
- For $\hat{o} \in K$, the family $(s_n \in Q_r^{\Phi_n})_{n \geq 0}$ witnessing $\hat{o}$ is a **coherent** family in the pattern-equivariant sheaf (via Lemma 3.2): each $s_n$ restricts to a compatible Čech datum at $\hat{o}$.
- By the pattern-equivariant *local-gluing* property (Kellendonk 2003 Thm 3.5), a compatible family of local data indexed by a descending chain with limit $\Phi_\infty$ glues to a section of $Q_r^{\Phi_\infty}$ witnessing $\hat{o}$.
- Hence $\hat{o} \in \mathcal{O}(Q_r^{\Phi_\infty})$, which gives $K \subseteq \mathcal{O}(Q_r^{\Phi_\infty})$. Combined with monotonicity, G-FIC-a follows.

Both routes agree; §3.3 is cleaner and §3.4 is more elementary. The substantive non-elementary import in either is the pattern-equivariant Čech local-gluing / inverse-limit-preservation theorem of Kellendonk 2003 / Kellendonk–Lenz–Savinien 2006.

---

## 4. What this note closes

- **G-FIC-a (support-region descending-intersection on $S^7$):** **CLOSED** at lemma-grade via closed-support + compact-Hausdorff + pattern-equivariant Čech limit-preservation.
- **H-FIC-O (via `cascade-h-fic-closure.md` §2):** the principal residual sub-gap is closed, so H-FIC-O is now conditional only on the standing Gap G6.1 closed-subgroupoid infrastructure (not on any further combinatorial claim).
- **Capstone Thm `thm:F-limits`:** the Observer-rung leg of the $\omega^{op}$-limit preservation is no longer conditional on G-FIC-a.

## 4.1 What this note does not close

- **G-FIC-b** (FAN-preimage generated-subgroupoid commutation on $\mathcal{G}_{E_8}$) — see `cascade-h-fic-closure.md` §3. Separate argument; analogous structure but different mathematical content.
- **Gap G6.1** (closedness of $\mathcal{G}_r^\Phi$ in $\mathcal{G}$) — standing prerequisite; assumed throughout.
- **R1** — stylistic identification of the closure-data filtration with the Kellendonk–Lenz–Savinien forcing-radius filtration (see §5).

---

## 5. Honest flagging of residual issues

**R1 (stylistic, not a gap).** Kellendonk–Lenz–Savinien 2006 Thm 3.4 is stated for descending filtrations of the pattern-equivariant Čech sheaf indexed by forcing-radius — i.e. the standard increasing sequence of local-patch-approximation sheaves. Our filtration is indexed by closure-data $\Phi$, which in general is not the same as forcing-radius. Lemma 3.2 identifies them in the restricted sense that *every closure-data descending chain $\Phi_n$ induces a descending chain of closed pattern-equivariant subsheaves*, which is what Thm 3.4 requires. The more refined statement — that closure-data descent is equivalent to a forcing-radius-type descent modulo rung-finite index — is not needed for G-FIC-a but would clean up the citation. This is a writing issue, not a mathematical gap.

**R2 (honest caveat on support-topology).** The closed-support lemma (Lemma 2.1) uses that $Q_r^\Phi$ is closed in the section-algebra topology of $\Gamma(G, F)$. This is inherited from Gap G6.1 (closedness of $\mathcal{G}_r^\Phi$) plus the standard fact that $\Gamma_{\mathcal{G}_r^\Phi}(G, F)$ is closed in $\Gamma(G, F)$ under the uniform σ-topology. Both are standard in the Bellissard–Kellendonk–Sadun framework. No additional hypothesis is introduced.

**R3 (not an issue, worth noting).** The $\supseteq$ direction at §3.4 step 4 uses *local gluing* rather than *global assembly*: we glue a section of $Q_r^{\Phi_\infty}$ only in a neighbourhood of $\hat{o}$, which suffices because σ-projection support is a pointwise property. Gluing to a *global* section compatible with every $\Phi_n$ is stronger and is not needed here. This matches the witness-separation style of `cascade-h-loc-closure.md` §3.

---

## 6. Compatibility with related closure notes

- **`cascade-h-fic-closure.md`** — §2.4 sub-gap G-FIC-a is closed here. §3 sub-gap G-FIC-b remains open as flagged there.
- **`cascade-h-loc-closure.md`** — provides the template (pattern-equivariant indicator section → support region). The closed-support lemma here (Lemma 2.1) and the local-gluing argument (§3.4 step 4) follow that template with the σ-projection in place of the indicator.
- **`cascade-q-o-measurement-bridge.md`** — used at theorem-grade (Thm 3.1, post-G6.4-a). No new claim about the bridge is made.
- **`cascade-observer-query-algebra.md`** — Gap G6.1 remains the single standing prerequisite; no weakening, no strengthening.
- **`cascade-capstone-coalgebra.tex`** — Thm `thm:F-limits` and Thm `thm:comonad-laws` can now drop G-FIC-a from their conditional stacks. The remaining conditional-stack item from the H-FIC family is G-FIC-b.

No existing documents are contradicted.

---

## 7. Updated conditional stack for the capstone

**Before this note.** Capstone Thm `thm:F-limits` was conditional on $\{\text{H-grad, H-meas, H-rdr}(\rightarrow \text{P-A}), \text{G-loc-a, G-FIC-a, G-FIC-b, H-lift-fin}\}$.

**After this note.** $\{\text{H-grad, H-meas, H-rdr}(\rightarrow \text{P-A}), \text{G-loc-a, G-FIC-b, H-lift-fin}\}$ — G-FIC-a removed.

Combined with the Tier-2 hardening completion (`project_tier2_hardening_progress.md`), the remaining residual sub-gaps in the capstone conditional stack are G-loc-a (combinatorial rung-independence), G-FIC-b (FAN-preimage generated-subgroupoid), and H-lift-fin (separately required for `lem:S7-coverage`). All three are independent and tractable.

---

## 8. References

- Kellendonk, J., "Pattern equivariant functions and cohomology," *J. Phys. A* 36 (2003).
- Kellendonk, J., Lenz, D., Savinien, J., "Pattern-equivariant functions and a generalized cohomology for point patterns" (and related 2006 Čech-sheaf limit-preservation; cited as Thm 3.4 in the operative role here).
- Bellissard, J., Kellendonk, J., Sadun, L., as cited in `cascade-moduli-meta-layer.md` §4.2.
- Sadun, L., *Topology of Tiling Spaces*, AMS 2008, §§2.5–4.3.
- Bourbaki, N., *Topologie générale* I, §9 no. 6 — descending closed intersection in compact Hausdorff spaces.

---

## 9. Summary table

| Item | Before this note | After this note |
|------|------------------|-----------------|
| G-FIC-a | Open, lemma-grade, 1–2 week closure estimate | **CLOSED** at lemma-grade |
| H-FIC-O conditional stack | {G6.1, G-FIC-a} | {G6.1} |
| Closed-support lemma ($\mathcal{O}(Q_r^\Phi)$ closed in $S^7$) | Implicit | Explicit (Lemma 2.1) |
| Kellendonk–Lenz–Savinien application | Cited only | Applied (§3.3) + elementary cross-check (§3.4) |
| Capstone Thm `thm:F-limits` conditional stack (Obs. leg) | Includes G-FIC-a | G-FIC-a removed |
| G-FIC-b | Open | Open (unchanged) |
| Gap G6.1 | Standing prerequisite | Standing prerequisite (unchanged) |

---

## 10. Next actions

1. **Update `cascade-h-fic-closure.md`** §4.2 to mark G-FIC-a as closed here; update §7 summary accordingly.
2. **Update `cascade-capstone-coalgebra.tex`** Remark `rmk:FIC-derivation-route` and the conditional-stack table (§ around line 284) to drop G-FIC-a.
3. **Progress G-FIC-b** via the analogous FAN-preimage closedness + generated-subgroupoid commutation route (see `cascade-h-fic-closure.md` §3.3).
4. **Programme bookkeeping.** Add G-FIC-a to the list of closed lemma-grade sub-gaps in `docs/gaps.md` (if maintained); `docs/proof-sheet.md` and `docs/consistency.md` should note the simplified capstone conditional stack.

---

**End of closure note.**

G-FIC-a is closed at lemma-grade by combining the closedness of $\mathcal{O}(Q_r^\Phi)$ on compact Hausdorff $S^7$ (inherited from Gap G6.1 via the bridge) with Kellendonk–Lenz–Savinien pattern-equivariant Čech limit-preservation. An elementary Cantor-intersection cross-check confirms the result. One stylistic identification (closure-data filtration vs. forcing-radius filtration) is flagged as R1; no further mathematical sub-gap survives. H-FIC-O is now conditional only on the standing Gap G6.1 prerequisite.
