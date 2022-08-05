#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from functools import reduce

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

from src.convert.natural.base2base import Base2Base
from src.convert.natural.base2nat  import Base2Nat
from src.convert.natural.nat2base  import Nat2Base
# from unit.core       import build_removable

from natcore.constants import *


# ------------------------ #
# -- BASE IN = BASE OUT -- #
# ------------------------ #

@given(st.integers(min_value = 0),
       st.integers(min_value = 2, max_value = 99),
       st.sampled_from(SOME_SEPS))
def test_base2base_same_base_bnb2bnb_with_sep(nb, base, sep):
    bnb = Nat2Base().nat2bnb(
        nb   = nb,
        base = base,
        sep  = sep
    )

    bnb_found = Base2Base().bnb2bnb(
        bnb      = bnb,
        base_in  = base,
        base_out = base,
        sep_in   = sep,
        sep_out  = sep,
    )

    assert bnb == bnb_found, \
           (
             "\n"
            f"{nb   = }"
             "\n"
            f"{base = }"
             "\n"
            f"{sep  = }"
             "\n"
           )


@given(st.integers(min_value = 0),
       st.integers(min_value = 2, max_value = 99),
       st.sampled_from(OUTPUTS_NO_NB))
def test_base2base_same_base_bXXX2bXXX(nb, base, XXX):
    nat2bXXX_ret = Nat2Base().__getattribute__(f"nat2b{XXX}")(
        nb   = nb,
        base = base,
    )

    bXXX2bXXX_found = Base2Base().__getattribute__(f"b{XXX}2b{XXX}")(
        nat2bXXX_ret,
        base_in  = base,
        base_out = base,
    )

    assert bXXX2bXXX_found == nat2bXXX_ret, \
           (
             "\n"
            f"{nb   = }"
             "\n"
            f"{base = }"
             "\n"
            f"{XXX  = }"
             "\n"
           )
