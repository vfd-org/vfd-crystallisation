"""Dic_5 = bulk subgroup tests."""
from __future__ import annotations

from collections import Counter

from vfd_v600.icosian import qq_mul, qq_key
from vfd_v600.group import left_cosets, right_cosets, dic5_is_normal, find_dic5_presentation


def test_dic5_has_20_elements(state):
    assert len(state["Dic5"]) == 20


def test_dic5_is_closed_under_multiplication(state):
    verts = state["verts"]
    idx_of = state["idx_of"]
    Dic5 = state["Dic5"]
    for i in Dic5:
        for j in Dic5:
            prod_idx = idx_of[qq_key(qq_mul(verts[i], verts[j]))]
            assert prod_idx in Dic5


def test_dic5_contains_identity(state):
    verts = state["verts"]
    idx_of = state["idx_of"]
    one = state["one"]
    one_idx = idx_of[qq_key(one)]
    assert one_idx in state["Dic5"]


def test_six_left_cosets(state):
    cosets = left_cosets(state)
    assert len(cosets) == 6


def test_left_cosets_partition_v600(state):
    cosets = left_cosets(state)
    union = set()
    for c in cosets:
        assert len(c) == 20
        assert union.isdisjoint(c)
        union |= c
    assert union == set(range(state["n"]))


def test_non_bulk_left_cosets_aggregate_K52_K20(state):
    """Each non-bulk left coset has aggregate K-counts {52: 10, 20: 10}.

    This is WEAKER than whole-cycle decomposition (left cosets are NOT
    cycle unions — see test_non_bulk_left_cosets_2_per_cycle for the
    structural fact). The aggregate K-count holds because each non-bulk
    left coset draws 2 vertices from each of the 10 non-bulk cycles.
    """
    cosets = left_cosets(state)
    cycle_of = state["cycle_of"]
    K_of_cycle = state["K_of_cycle"]

    for coset in cosets[1:]:
        K_classes = Counter(K_of_cycle[cycle_of[v]] for v in coset)
        assert K_classes == {52: 10, 20: 10}, f"unexpected coset K-distribution: {K_classes}"


def test_non_bulk_right_cosets_pair_K52_K20(state):
    """Each non-bulk right coset is one WHOLE K=52 cycle ∪ one WHOLE K=20 cycle.

    Stronger than aggregate K-counts: tests whole-cycle decomposition.
    Right cosets satisfy this because T_τ commutes with right multiplication
    by H (since τ ∈ H).
    """
    cosets = right_cosets(state)
    cycle_of = state["cycle_of"]
    K_of_cycle = state["K_of_cycle"]
    cycles = state["cycles"]

    for coset in cosets[1:]:
        cycles_present = sorted(set(cycle_of[v] for v in coset))
        assert len(cycles_present) == 2, f"right coset must span exactly 2 cycles, got {cycles_present}"
        # Each present cycle must be FULLY contained.
        for ci in cycles_present:
            assert set(cycles[ci]).issubset(coset), \
                f"cycle {ci} only partially in right coset"
        K_classes = sorted(K_of_cycle[ci] for ci in cycles_present)
        assert K_classes == [20, 52], f"K-classes of present cycles: {K_classes}"


def test_non_bulk_left_cosets_2_per_cycle(state):
    """Each non-bulk left coset contains 2 vertices from each of the 10 non-bulk cycles.

    The complementary structural fact to test_non_bulk_right_cosets_pair_K52_K20:
    left cosets are NOT unions of whole T_τ-cycles when H is non-normal.
    """
    cosets = left_cosets(state)
    cycle_of = state["cycle_of"]
    K_of_cycle = state["K_of_cycle"]

    for coset in cosets[1:]:
        per_cycle = Counter(cycle_of[v] for v in coset)
        # Must touch all 10 non-bulk cycles, with 2 vertices each.
        non_bulk_cycle_indices = {ci for ci in range(12) if K_of_cycle[ci] in (52, 20)}
        assert set(per_cycle.keys()) == non_bulk_cycle_indices
        assert all(c == 2 for c in per_cycle.values())


def test_dic5_is_not_normal_in_2i(state):
    """Codex caught this: Dic_5 is NOT normal. Paper 1 must not assume normality."""
    assert not dic5_is_normal(state)


def test_six_right_cosets(state):
    cosets = right_cosets(state)
    assert len(cosets) == 6


def test_right_cosets_partition_v600(state):
    cosets = right_cosets(state)
    union = set()
    for c in cosets:
        assert len(c) == 20
        assert union.isdisjoint(c)
        union |= c
    assert union == set(range(state["n"]))


def test_dic5_binary_dihedral_presentation(state):
    """Verify Dic_5 contains a, b with a^10=1, b²=a⁵, bab⁻¹=a⁻¹."""
    a_idx, b_idx = find_dic5_presentation(state)
    assert a_idx in state["Dic5"]
    assert b_idx in state["Dic5"]
