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


# -------------------- #
# -- HARD CHECKINGS -- #
# -------------------- #

@given(st.integers(min_value = 0),
       st.integers(min_value = 2))
def test_nat2base_nat2bdigits_by_hand(nb, base):
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
