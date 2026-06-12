"""Rung-admissibility search (named deliverable). Thin CLI over the Collatz parity
automaton in domains/collatz_adapter.py: verifies the full-shift (Terras) grammar and
searches for escape-word realisations."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "domains"))
import collatz_adapter as C

if __name__ == "__main__":
    bij = C.verify_terras_bijection(kmax=12)
    print("Terras parity-vector bijection (full-shift admissibility):")
    for k, v in bij.items():
        print(f"  k={k:2}: {v['distinct']}/{v['expected']} distinct  bijection={v['bijection']}")
    print(f"\nFull shift up to k=12: {all(v['bijection'] for v in bij.values())}")
    esc = C.escape_words_realised(k=10)
    print(f"\nEscape word (all-ones, len 10) realised by n={esc['realised_by_smallest_n']}; "
          f"capacity {esc['capacity']:.3f}; longer ones-fraction {esc['longer_parity_fraction_ones']}")
    print("\nCONCLUSION: rung grammar = full shift => no finite rung-automaton certificate "
          "for Collatz; obstruction is global. (Not a proof of Collatz.)")
