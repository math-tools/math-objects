#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from functools import reduce
from random    import choice

from   hypothesis            import given
import hypothesis.strategies as st
import pytest

from cbdevtools import *


# ----------------------- #
# -- CONSTANTS & TOOLS -- #
# ----------------------- #

BUILTINS_CONVERTERS = {
    2 : bin,
    8 : oct,
    16: hex,
}

BUILTINS_CONVERTERS_BASES = list(BUILTINS_CONVERTERS)

KIND_CHGETHIS = [
    ("digits"  , int),
    ("numerals", str)
]

LAMBDA_2_NAT_LIKE = {
# DECIMAL BASE
    "digits": lambda digits: reduce(
        lambda x, y: x*10 + y,
        digits
    ),
    "numerals": lambda numerals: ''.join(numerals),
# GENERAL BASE
    "bdigits": lambda bdigits, base: reduce(
        lambda x, y: x*base + y,
        bdigits
    )
}


# ------------------------------------------ #
# -- MODULE TESTED IMPORTED FROM SOURCES! -- #
# ------------------------------------------ #

for upfolder in [
    'cvnum',
    # 'tests',
]:
    _ = addfindsrc(
        file    = __file__,
        project = upfolder,
    )

from src.convert.natural.nat2base import Nat2Base
# from unit.core       import build_removable



# ---------------- #
# -- NUMERALIZE -- #
# ---------------- #

@given(st.integers(min_value = 2, max_value = 99))
def test_nat2base_numeralize_len_single(base):
    numeralize = Nat2Base().numeralize(base)
    allsingles = set(
        numeralize(n)[0]
        for n in range(base)
    )

    assert len(allsingles) == base, \
           f"{base = }"


@given(st.integers(min_value = 2, max_value = 99))
def test_nat2base_numeralize_good_sorted_values(base):
    numeralize = Nat2Base().numeralize(base)
    allsingles = list(
        numeralize(n)[0]
        for n in range(base)
    )

    assert allsingles == sorted(allsingles), \
           f"{base = }"


# -------------------------- #
# -- DIGITS / NUMERALS OF -- #
# -------------------------- #

@given(st.integers(max_value = -1))
def test_nat2base_digitsof_numeralsof_negative_NOT_OK(bad):
    for kind in ["digits", "numerals"]:
        XXXof = f"{kind}of"

        with pytest.raises(
            (AssertionError, ValueError),
            match = r".*too small.*"
        ):
            Nat2Base().__getattribute__(XXXof)(bad)

            pytest.fail(f"{XXXof = }")


@given(st.integers(min_value = 0))
def test_nat2base_digitsof_numeralsof(nb):
    for kind, chgethis in KIND_CHGETHIS:
        XXXof = f"{kind}of"
        datas = Nat2Base().__getattribute__(XXXof)(nb)

        nbwanted = chgethis(nb)
        nbfound  = LAMBDA_2_NAT_LIKE[kind](datas)

        assert nbwanted == nbfound, \
               (
                 "\n"
                f"{nb    = }"
                 "\n"
                f"{XXXof = }"
                 "\n"
               )


# ---------------------------- #
# -- FROM DIGITS / NUMERALS -- #
# ---------------------------- #

@given(st.integers(min_value = 0))
def test_nat2base_fromdigits_fromnumerals(nb):
    for kind, chgethis in KIND_CHGETHIS:
        fromXXX = f"from{kind}"
        datas   = [chgethis(c) for c in str(nb)]
        nbfound = Nat2Base().__getattribute__(fromXXX)(datas)

        assert nbfound == nb, \
               (
                 "\n"
                f"{nb      = }"
                 "\n"
                 f"{fromXXX = }"
                 "\n"
               )


# ---------------------------------------- #
# -- DECIMAL --> BASE DIGITS / NUMERALS -- #
# ---------------------------------------- #

@given(st.integers(max_value = 1))
def test_nat2base_nat2bdigits_negative_NOT_OK(bad_base):
    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*base.*too small.*"
    ):
        Nat2Base().nat2bdigits(
            nb   = 20220722, # This looks like a date...
            base = bad_base,
        )


@given(st.integers(min_value = 0),
       st.integers(min_value = 2))
def test_nat2base_nat2bdigits(nb, base):
    nbfound = LAMBDA_2_NAT_LIKE["bdigits"](
        Nat2Base().nat2bdigits(
            nb   = nb,
            base = base
        ),
        base
    )

    assert nb == nbfound,\
           (
             "\n"
            f"{nb   = }"
             "\n"
            f"{base = }"
             "\n"
           )


@given(st.integers(min_value = 0),
       st.integers(min_value = 2, max_value=36))
def test_nat2base_nat2bnumerals_via_python_builtins(nb, base):
    nbfound = int(
        ''.join(
            Nat2Base().nat2bnumerals(
                nb   = nb,
                base = base
            )
        ),
        base = base
   )

    assert nb == nbfound, \
           (
             "\n"
            f"{nb   = }"
             "\n"
            f"{base = }"
             "\n"
           )


# ------------------------------ #
# -- DECIMAL --> BASE NUMBERS -- #
# ------------------------------ #

@given(st.integers(min_value = 0),
       st.integers(min_value = 2))
def test_nat2base_nat2bnb_via_nat2bnumerals(nb, base):
    bnb = Nat2Base().nat2bnb(
        nb   = nb,
        base = base
    )

    bnb_from_bnumerals = ''.join(
        Nat2Base().nat2bnumerals(
            nb   = nb,
            base = base
        )
    )

    assert bnb == bnb_from_bnumerals, \
           (
             "\n"
            f"{nb   = }"
             "\n"
            f"{base = }"
             "\n"
           )


@given(st.integers(min_value = 16 + 1),
       st.sampled_from(BUILTINS_CONVERTERS_BASES))
def test_nat2base_nat2bnb_via_python_builtins(nb, base):

    bnb_found =  Nat2Base().nat2bnb(
        nb   = nb,
        base = base
    )

    bnb_python = BUILTINS_CONVERTERS[base](nb)
    bnb_python = bnb_python[2:]     # Cf. '0b', '0o' and '0x'
    bnb_python = bnb_python.upper()  # Python uses the lower case.

    assert bnb_found == bnb_python, \
           (
             "\n"
            f"{nb   = }"
             "\n"
            f"{base = }"
             "\n"
           )


# -------------------------------------------------- #
# -- DIGITS / NUMERALS --> BASE DIGITS / NUMERALS -- #
# -------------------------------------------------- #

# See the "reciprocity law" tests of ``base2nat.Base2Nat``.


# --------------------------------------- #
# -- DIGITS / NUMERALS --> BASE NUMBER -- #
# --------------------------------------- #

# See the "reciprocity law" tests of ``base2nat.Base2Nat``.


# --------------------- #
# -- ... --> BASE 10 -- #
# --------------------- #

@given(st.integers(min_value = 0))
def test_nat2base_base_10_nat2bdigits_nat2bnumerals(nb):
    for kind in ["digits", "numerals"]:
        XXXof    = f"{kind}of"
        nat2bXXX = f"nat2b{kind}"

        nb_using_10_base   = Nat2Base().__getattribute__(XXXof)(nb)
        nb_using_gene_base = Nat2Base().__getattribute__(nat2bXXX)(
            nb   = nb,
            base = 10
        )

        assert nb_using_10_base == nb_using_gene_base, \
               (
                 "\n"
                f"{nb       = }"
                 "\n"
                f"{XXXof    = }"
                 "\n"
                f"{nat2bXXX = }"
                 "\n"
               )


@given(st.integers(min_value = 0))
def test_nat2base_base_10_bnb(nb):
    str_nb             = str(nb)
    nb_using_gene_base = Nat2Base().nat2bnb(
        nb   = nb,
        base = 10
    )

    assert str_nb == nb_using_gene_base
