"""Prime Phenomena Ledger (WO-VFD-PRIME-LEDGER-001).

Nine of the ten rows factor a prime-distribution phenomenon as
  (local: all-finite-places closure product — decidable, verified here)
  x (global: a zero-distribution statement for an explicit L-function —
     open, stated, never claimed).
The tenth row (Mersenne, row 9) is included precisely because the
factorisation fails there: it marks the instrument's boundary.

Layer-1 results are classical (Hardy-Littlewood 1923, Dirichlet 1837,
Chebotarev 1926): this module verifies and organises; it discovers nothing
at layer 1 and proves nothing at layer 2.

Run:  python3 -m lab.prime_ledger          # all Phase A rows -> out/prime_ledger.json
"""
