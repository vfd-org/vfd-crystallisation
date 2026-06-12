"""Translation engine dictionary entries.

The dictionary maps substrate / mathematical objects to their formal
referents in the translation framework.  Each entry captures the
typed correspondence the grammar can use.

Dictionary entries are ADDITIVE: each new entry expands the engine's
ability to reason about a new class of substrate <-> analytic
correspondence.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


@dataclass
class DictionaryEntry:
    """A typed substrate -> analytic referent mapping."""
    entry_id: str
    substrate_object: str
    mathematical_referent: str
    layer: int  # 1 = vocabulary, 2 = grammar, 3 = interpretive
    bridge_hypotheses: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


# Original Layer-1 vocabulary entries (substrate primitives)
DICTIONARY: Dict[str, DictionaryEntry] = {
    "V_600": DictionaryEntry(
        entry_id="V_600",
        substrate_object="V_600 = 120 unit icosian quaternions",
        mathematical_referent="vertex set of regular 600-cell;"
                              " 2I as binary icosahedral group",
        layer=1,
    ),
    "C_phi": DictionaryEntry(
        entry_id="C_phi",
        substrate_object="closure operator C_phi = L + phi^-2 I",
        mathematical_referent="self-adjoint positive operator;"
                              " 94 + 13 + 13 sigma-pairing decomposition",
        layer=2,
    ),
    "N_H": DictionaryEntry(
        entry_id="N_H",
        substrate_object="generation operator N_H : I -> Z[phi]",
        mathematical_referent="quaternary norm form representing all"
                              " totally positive Z[phi]-primes",
        layer=2,
    ),
    "tau_galois": DictionaryEntry(
        entry_id="tau_galois",
        substrate_object="tau involution",
        mathematical_referent="Galois action sigma : phi -> 1-phi"
                              " lifted to C_phi spectrum;"
                              " induces 94 + 13 + 13 split",
        layer=2,
    ),
}


# ---------------------------------------------------------------------------
# v0.2 additions: ANALYTIC-SIDE dictionary entries
# ---------------------------------------------------------------------------

ANALYTIC_DICTIONARY: Dict[str, DictionaryEntry] = {

    "completed_L": DictionaryEntry(
        entry_id="completed_L",
        substrate_object="completed L-function Lambda(s)",
        mathematical_referent="Lambda(s) = pi^(-s/2) Gamma(s/2) zeta(s);"
                              " entire on C except poles at s=0, 1;"
                              " satisfies Lambda(s) = Lambda(1-s)",
        layer=2,
        bridge_hypotheses=["H-EulerBridge"],
        notes=["the basic analytical object whose zeros are the"
               " non-trivial zeros of zeta",
               "functional equation s <-> 1-s is the substrate's"
               " required spectral symmetry"],
    ),

    "zero_count_N_T": DictionaryEntry(
        entry_id="zero_count_N_T",
        substrate_object="N(T) = #{zeros gamma <= T}",
        mathematical_referent="Riemann-Hardy-Littlewood asymptotic"
                              " N(T) ~ (T/2pi) log(T/2pi) - T/(2pi)",
        layer=2,
        notes=["density of zeros along the critical line",
               "substrate operator must have spectral density"
               " matching this asymptotic"],
    ),

    "pair_correlation": DictionaryEntry(
        entry_id="pair_correlation",
        substrate_object="pair correlation function R(alpha)",
        mathematical_referent="Montgomery's pair correlation;"
                              " conjecturally matches GUE kernel"
                              " 1 - (sin(pi alpha) / (pi alpha))^2",
        layer=2,
        notes=["the substrate's natural analytic test:"
               " do candidate eigenvalue spacings match GUE?"],
    ),

    "explicit_formula": DictionaryEntry(
        entry_id="explicit_formula",
        substrate_object="Weil explicit formula",
        mathematical_referent="sum over zeros = sum over primes"
                              " + boundary contribution",
        layer=2,
        notes=["the strongest constraint:"
               " test functions phi must give the same total"
               " when summed against zeros vs primes"],
    ),

    "selberg_class_S": DictionaryEntry(
        entry_id="selberg_class_S",
        substrate_object="Selberg class S",
        mathematical_referent="axiomatic class of L-functions:"
                              " analytic continuation,"
                              " functional equation,"
                              " Euler product,"
                              " Ramanujan bound",
        layer=2,
        notes=["L_sub belongs to Selberg class S;"
               " substrate-derived L-functions must too"],
    ),

    "hecke_T_p": DictionaryEntry(
        entry_id="hecke_T_p",
        substrate_object="Hecke operator T_p for prime ideal p of Z[phi]",
        mathematical_referent="commuting family of self-adjoint"
                              " operators on Hilbert modular forms;"
                              " eigenvalues are Dirichlet coefficients"
                              " of the L-function",
        layer=2,
        bridge_hypotheses=["H-EulerBridge"],
        notes=["the missing transformation kind:"
               " currently a prototype, needs Brandt matrix"
               " implementation",
               "T_m T_n = T_{mn} for gcd(m, n) = 1"],
    ),

    "brandt_matrix": DictionaryEntry(
        entry_id="brandt_matrix",
        substrate_object="Brandt matrix B_p of the icosian order",
        mathematical_referent="finite-dim Hecke action coming from"
                              " ideal class representatives of the"
                              " maximal icosian order over Z[phi]",
        layer=2,
        notes=["computable in SAGE / Magma / Pari",
               "for our class-number-1 case the Brandt matrices"
               " are scalars; richer action requires non-trivial"
               " ideal class structure -- a strict extension"],
    ),

    "sato_tate_measure": DictionaryEntry(
        entry_id="sato_tate_measure",
        substrate_object="Sato-Tate distribution",
        mathematical_referent="semicircular measure on Hecke"
                              " eigenvalue normalisations;"
                              " conjecturally satisfied by"
                              " non-CM modular forms",
        layer=2,
        notes=["secondary test: substrate-derived Hecke"
               " eigenvalues normalised by 2 sqrt(p)"
               " should follow this measure"],
    ),

    "U_symmetry_class": DictionaryEntry(
        entry_id="U_symmetry_class",
        substrate_object="L-function symmetry class U(infinity)",
        mathematical_referent="random-matrix-theory classification"
                              " of L-functions; zeta(s) belongs to"
                              " unitary class U with GUE statistics",
        layer=2,
        notes=["KW / random matrix prediction:"
               " the Hilbert-Polya operator must have"
               " U-class spectrum"],
    ),
}


def all_dictionary_entries() -> Dict[str, DictionaryEntry]:
    """Return the merged dictionary (substrate primitives +
    analytic entries)."""
    return {**DICTIONARY, **ANALYTIC_DICTIONARY}


def find_entry(query: str) -> Optional[DictionaryEntry]:
    """Look up an entry by its id."""
    return all_dictionary_entries().get(query)


def grammar_summary() -> List[str]:
    """Summary of the engine's current grammatical rules,
    grouped by layer."""
    return [
        "VOCABULARY (Layer 1):",
        "  V_600, V_24, A_1, irreducible representations of 2I",
        "",
        "GRAMMAR (Layer 2 - substrate side):",
        "  Closure operator C_phi = L + phi^-2 I",
        "  Generation operator N_H : I -> Z[phi]",
        "  Galois involution tau lifted from sigma : phi -> 1-phi",
        "  Schlaefli decomposition V_600 = 5 cosets of 2T",
        "  Lambda = 12 lift theorem (positive grammar rule)",
        "  Lambda = 12 uniqueness scan (negative grammar rule)",
        "  12 transformation kinds (DUAL, ..., DIMENSIONAL_PROJECTION)",
        "",
        "GRAMMAR (Layer 2 - analytic side, v0.2 additions):",
        "  Completed L-function Lambda(s)",
        "  Functional equation s <-> 1-s",
        "  Zero-counting asymptotic N(T)",
        "  Pair correlation / GUE measure",
        "  Selberg class S axioms",
        "  Hecke operator family T_p",
        "  Brandt matrix construction",
        "  Sato-Tate distribution",
        "  U-symmetry class membership",
        "",
        "TRANSFORMATION KINDS (extended v0.2):",
        "  Original 12: DUAL, SHELL_PROJECTION, ... (engine v0.1)",
        "  HECKE_LIFT (prototype; needs SAGE backend for genuine)",
        "  MODULAR_EMBED (metadata-level)",
        "  ANALYTIC_EXTEND (numerical proxy)",
        "  SPECTRAL_LIFT_INFINITE (direct-sum prototype)",
        "  TRACE_FORMULA_CLOSE (3 power-traces)",
        "",
        "ADMISSIBILITY CLASSES (extended v0.2):",
        "  Original 5: EXACT, CANDIDATE, APPROXIMATE, BROKEN, DEGENERATE",
        "  SPECTRAL_MATCH (RMSE vs gamma_n)",
        "  ZERO_LINE_FORCED (spacing CV)",
        "  HECKE_COMPATIBLE (commutator norm)",
        "  MODULAR_INVARIANT (action invariance)",
        "  FUNCTIONAL_EQUATION_RESPECTED (s <-> 1-s symmetry)",
        "  DENSITY_CONSISTENT (Riemann-Hardy-Littlewood)",
        "  GUE_DISTRIBUTED (Montgomery-Odlyzko)",
        "  HECKE_MULTIPLICATIVE (lambda_mn = lambda_m lambda_n coprime)",
    ]
