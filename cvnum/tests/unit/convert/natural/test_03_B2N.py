#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from random import choice

from   hypothesis            import given
import hypothesis.strategies as st
import pytest

from cbdevtools import *


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

from src.convert.natural.base2nat import Base2Nat
from src.convert.natural.nat2base import Nat2Base
# from unit.core       import build_removable


# ----------------------- #
# -- CONSTANTS & TOOLS -- #
# ----------------------- #

OUTPUTS = [
    "nb",
    "digits",
    "numerals",
]


# ----------------------- #
# -- "RECIPROCITY LAW" -- #
# ----------------------- #

@given(st.integers(min_value = 0),
       st.integers(min_value = 2, max_value = 99),
       st.sampled_from(OUTPUTS))
def test_nat2XXX_o_XXX2nat(nb, base, XXX):
    n2b_NB = Nat2Base().__getattribute__(f"nat2b{XXX}")(
        nb   = nb,
        base = base
    )

    b2n_n2b_NB = Base2Nat().__getattribute__(f"b{XXX}2nat")(
        n2b_NB,
        base = base
    )

    assert nb == b2n_n2b_NB, \
           (
             "\n"
            f"{nb    = }"
             "\n"
            f"{XXX = }"
             "\n"
           )
