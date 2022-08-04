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


# ------------------------------------------ #
# -- MODULE TESTED IMPORTED FROM SOURCES! -- #
# ------------------------------------------ #

for upfolder in [
    'cvnum',
    'natural',
    # 'tests',
]:
    _ = addfindsrc(
        file    = __file__,
        project = upfolder,
    )

from src.convert.natural.nat2base import Nat2Base
# from unit.core       import build_removable

from core.constants import *


# ----------------------- #
# -- CONSTANTS & TOOLS -- #
# ----------------------- #

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


# -------------------------------------------------- #
# -- DIGITS / NUMERALS --> BASE DIGITS / NUMERALS -- #
# -------------------------------------------------- #

# See the "reciprocity law" tests of ``base2nat.Base2Nat``.


# --------------------------------------- #
# -- DIGITS / NUMERALS --> BASE NUMBER -- #
# --------------------------------------- #

# See the "reciprocity law" tests of ``base2nat.Base2Nat``.


# ------------------------ #
# -- BDIGITS - BAD BASE -- #
# ------------------------ #

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


# -------------------------- #
# -- DIGITS / NUMERALS OF -- #
# -------------------------- #

@given(st.integers(max_value = -1),
       st.sampled_from(KINDS_ALL))
def test_nat2base_XXXof_negative_NOT_OK(bad, kind):
    XXXof = f"{kind}of"

    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*too small.*"
    ):
        Nat2Base().__getattribute__(XXXof)(bad)

        pytest.fail(f"{XXXof = }")


@given(st.integers(min_value = 0),
       st.sampled_from(KINDS_ALL))
def test_nat2base_XXXof(nb, kind):
    chgethis = KINDS_CHGETHIS[kind]

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

@given(st.integers(min_value = 0),
       st.sampled_from(KINDS_ALL))
def test_nat2base_fromXXX(nb, kind):
    chgethis = KINDS_CHGETHIS[kind]

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
