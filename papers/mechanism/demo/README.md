# ARIA Deterministic Proof Pack

**Pack Hash:** `c67b74d5311bdd68662fae47e46e8cbc...`
**Schema Version:** 1.0
**Candidates:** 3
**Deterministic:** True
**Execution Mode:** strict_local

## What This Pack Contains

This proof pack captures a complete deterministic governed reasoning run.
All artifacts needed to verify that identical inputs produced identical
candidates and identical final selection are included.

## Verification

Run the following to verify this pack:

```bash
python replay_verify.py ./proof_pack
```

Or manually:

- 1. Load manifest.json and verify proof_pack_schema_version
- 2. Load hashes.json and verify each artifact file hash
- 3. Verify request_hash matches canonical_request.json content hash
- 4. Verify context_hash matches context_snapshot.json content hash
- 5. Verify proposal_hash matches proposal_slots.json content hash
- 6. Verify proposal_space_hash matches proposal_bundle.json content hash
- 7. Load normalized_candidates.json and verify candidate ordering
- 8. Replay crystallisation selection from normalized candidates
- 9. Verify selected_candidate_id matches crystallisation result
- 10. Verify selected_candidate_hash matches candidate content hash
- 11. Verify enforcement_result.json shows allowed=true
- 12. Confirm all hashes match → DETERMINISM VERIFIED

## Key Hashes

- Request: `30870cec5791cf50`
- Context: `a7dc473f567c61e2`
- Proposal: `66d6623b7fdcca08`
- Space: `21866da06e76b534`
- Selected: `cand-eed80f757799`

## Determinism Claim

This pack supports the claim that ARIA implements deterministic
proposal-space formation and deterministic crystallisation over
canonicalized inputs. Identical inputs reproduce identical candidate
sets and identical final selections.
