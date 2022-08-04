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


# --------------------- #
# -- ... --> BASE 10 -- #
# --------------------- #

@given(st.integers(min_value = 0),
       st.sampled_from(KINDS_ALL))
def test_nat2base_BASE_10_nat2bXXX_vs_XXXof(nb, kind):
    chgethis = KINDS_CHGETHIS[kind]

    XXXof    = f"{kind}of"
    nat2bXXX = f"nat2b{kind}"

    XXXof_ret    = Nat2Base().__getattribute__(XXXof)(nb)
    nat2bXXX_ret = Nat2Base().__getattribute__(nat2bXXX)(
        nb   = nb,
        base = 10
    )

    assert XXXof_ret == nat2bXXX_ret, \
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
def test_nat2base_BASE_10_bnb_vs_str_nb(nb):
    str_nb      = str(nb)
    nat2bnb_ret = Nat2Base().nat2bnb(
        nb   = nb,
        base = 10
    )

    assert str_nb == nat2bnb_ret
