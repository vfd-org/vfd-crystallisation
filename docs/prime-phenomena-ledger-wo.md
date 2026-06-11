# WO-VFD-PRIME-LEDGER-001 — The Prime Phenomena Ledger

**Goal:** run every named prime-distribution phenomenon through the one instrument
(explicit formula / prime waves / local closure densities, as built in
`closure-positivity-lab`), and publish a single ledger artifact: per phenomenon,
the local layer derived + numerically verified, the classical status stated, and
the global wall located in our coordinates. Consilience by checkable table, not
by assertion.

**Discipline (binding):**
- Layer 1 (local/all-finite-places) results are classical (Hardy–Littlewood,
  Dirichlet, Chebotarev…) — we verify and *organize*, we do not claim discovery.
- Layer 2 (infinitude/global) is open in every famous case. The ledger's claim is
  only: *the wall is the same object every time* (correlations of zeros via the
  explicit formula). No phenomenon gets a "solved" tag that mainstream does not give it.
- Every row ships with a one-command verification script and a falsifier.
- The verification gate (vfd_math_engine) applies: any row whose "derivation"
  smuggles a fitted map is killed, not shipped.

**The unifying statement under test** (the ledger's actual thesis):

> Every prime-distribution phenomenon factors as
> (admissibility × density at every finite place — decidable, closure language)
> × (interference of zero-correlations — the single global wall).
> The local factor is our positivity/closure motif; the wall is the
> diffraction fringes' fine structure.

## The rows

| # | Phenomenon | Local layer (we derive + verify) | Classical status | Wall in our coordinates |
|---|---|---|---|---|
| 1 | Twin primes | Singular series 2C₂ as all-places closure product; **verified 239,101 vs 239,107 to 5e7 (0.003%)** | HL conjecture; bounded gaps ≤246 (Maynard) | pair correlation of zeros (Goldston equivalences) |
| 2 | All even gaps (Polignac) | Gap-h local product; **gap-6 = 2× twins verified (1.995), gap-10 = 4/3 (1.3318), gap-30 = 8/3 (2.6633)** | open (same class) | same pair correlation |
| 3 | Goldbach | Same singular series, additive form: per-N local densities; verify representation counts vs HL prediction | open (ternary proven, Helfgott) | zeros of L-functions in the circle-method minor arcs |
| 4 | Primes in APs / Dirichlet | Place-q closure conditions = admissible residues; equidistribution verified | THEOREM (Dirichlet, PNT-APs) | error term = GRH for Dirichlet L |
| 5 | Chebyshev bias (π(x;4,3) > π(x;4,1)) | Explicit-formula interference of L-zeros — literally a diffraction asymmetry; compute + visualize the bias live | theorem under GRH+LI (Rubinstein–Sarnak) | zero correlations of Dirichlet L |
| 6 | Q(√5) splitting statistics (our field) | split/inert equidistribution mod 5 = place-5 closure; feeds directly into our Brandt prime data | THEOREM (Chebotarev) | error term = ζ_K zeros |
| 7 | Sato–Tate for our cuspidal L | angle distribution, 2nd moment 0.2515 vs 0.25 (already in the lab) | THEOREM (BLGHT, non-CM HMF) | rate/discrepancy = effective ST = symmetric-power Ls |
| 8 | Prime gaps at large (Cramér) | spacing statistics vs exponential model; maximal-gap data | heuristic; gaps ≪ p^0.525 proven | zero density estimates |
| 9 | Mersenne / shape-constrained primes | Lenstra–Pomerance–Wagstaff local-density heuristic in closure form | heuristic only | no L-function handle — honest "beyond the instrument" row |
| 10 | Zero statistics themselves (GUE) | Montgomery pair correlation on computed zeta zeros; our 33 icosian-L zeros as a (small-n) consistency check | conjecture (RMT link) | this row IS the wall, stated as such |

Rows 4, 6, 7 are anchors: theorem-grade rows where instrument output must match
proven mathematics exactly — they calibrate trust in the conjectural rows.

## Deliverables

1. `lab/prime_ledger/` module in closure-positivity-lab: one script per row,
   one JSON artifact per row, one runner (`python3 -m lab.prime_ledger`).
2. Paper: "The Prime Field Through One Instrument" — ledger format, ~12-15 pp,
   the thesis statement above as the only novel claim, status-tagged per row.
3. Campaign: each row = one registry YAML = one weekly post + result page
   (≈10 weeks of content). Rows with strong visuals (1, 2, 5 bias race,
   10 GUE) = explorables/shorts.
4. Website: ledger page under the mathematicians door; each row links its
   verification command.

## Sequencing

Phase A (rows 1, 2, 4, 6 — done or near-done; twin/gap computation exists).
Phase B (rows 3, 5, 7 — circle-method counts, bias visualization, ST already in lab).
Phase C (rows 8, 9, 10 + paper assembly + explorables).

**Falsifier for the whole ledger:** any phenomenon whose local layer cannot be
written as an all-finite-places closure product, or whose wall does not reduce
to zero-correlations via the explicit formula, breaks the thesis — and gets
reported as a counterexample row, not omitted.
