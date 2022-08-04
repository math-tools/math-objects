#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from random import choice

from   hypothesis            import given
import hypothesis.strategies as st
# import pytest

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

from src.convert.natural.base2nat import Base2Nat
from src.convert.natural.nat2base import Nat2Base
# from unit.core       import build_removable

from core.constants import *


# ------------------------ #
# -- "RECIPROCITY LAWS" -- #
# ------------------------ #

@given(st.integers(min_value = 0),
       st.integers(min_value = 2, max_value = 99),
       st.sampled_from(OUTPUTS_NO_NB))
def test_base2nat_frombXXX_o_bXXXof(nb, base, XXX):
    bnb = Nat2Base().nat2bnb(
        nb   = nb,
        base = base
    )

    bXXXof_ret = Base2Nat().__getattribute__(f"b{XXX}of")(
        bnb  = bnb,
        base = base
    )

    frombXXX_ret = Base2Nat().__getattribute__(f"fromb{XXX}")(
        bXXXof_ret,
        base = base
    )

    assert bnb == frombXXX_ret, \
           (
             "\n"
            f"{nb         = }"
             "\n"
            f"{base       = }"
             "\n"
            f"{XXX        = }"
             "\n"
            f"{bXXXof_ret = }"
             "\n"
           )


@given(st.integers(min_value = 0),
       st.integers(min_value = 2, max_value = 99),
       st.sampled_from(OUTPUTS_ALL))
def test_base2nat_bXXX2nat_o_nat2bXXX(nb, base, XXX):
    n2b_XXX_ret = Nat2Base().__getattribute__(f"nat2b{XXX}")(
        nb   = nb,
        base = base
    )

    b2n_n2b_NB = Base2Nat().__getattribute__(f"b{XXX}2nat")(
        n2b_XXX_ret,
        base = base
    )

    assert nb == b2n_n2b_NB, \
           (
             "\n"
            f"{nb   = }"
             "\n"
            f"{base = }"
             "\n"
            f"{XXX  = }"
             "\n"
           )


@given(st.integers(min_value = 0),
       st.integers(min_value = 2, max_value = 99),
       st.sampled_from(OUTPUTS_NO_NB),
       st.sampled_from(OUTPUTS_ALL))
def test_base2nat_bYYY2XXX_o_XXX2bYYY(nb, base, XXX, YYY):
    return_of = Nat2Base().__getattribute__(f"{XXX}of")(nb)

    XXX2bYYY_ret = Nat2Base().__getattribute__(f"{XXX}2b{YYY}")(
        return_of,
        base = base,
    )

    bYYY2XXX_ret = Base2Nat().__getattribute__(f"b{YYY}2{XXX}")(
        XXX2bYYY_ret,
        base = base,
    )

    assert return_of == bYYY2XXX_ret, \
           (
             "\n"
            f"{nb   = }"
             "\n"
            f"{base = }"
             "\n"
            f"{XXX  = }"
             "\n"
            f"{YYY  = }"
             "\n"
           )



@given(st.integers(min_value = 0),
       st.integers(min_value = 2, max_value = 99),
       st.sampled_from(SOME_SEPS))
def test_base2nat_bnb2nat_o_nat2bnb_with_sep(nb, base, sep):
    nat2bnb_ret = Nat2Base().nat2bnb(
        nb   = nb,
        base = base,
        sep  = sep
    )

    bnb2nat_nat2bnb_NB = Base2Nat().bnb2nat(
        bnb  = nat2bnb_ret,
        base = base,
        sep  = sep
    )

    assert nb == bnb2nat_nat2bnb_NB, \
           (
             "\n"
            f"{nb   = }"
             "\n"
            f"{base = }"
             "\n"
            f"{sep  = }"
             "\n"
           )
