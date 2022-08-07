#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from   hypothesis            import given
import hypothesis.strategies as st

from cbdevtools import *


# ------------------------------------------ #
# -- MODULE TESTED IMPORTED FROM SOURCES! -- #
# ------------------------------------------ #

for upfolder in [
    'cvnum',
    'integer',
    # 'tests',
]:
    _ = addfindsrc(
        file    = __file__,
        project = upfolder,
    )

from src.convert.integer.base2int import Base2Int
from src.convert.integer.int2base import Int2Base
# from unit.core       import build_removable

from intcore.constants import *


# ------------------------ #
# -- "RECIPROCITY LAWS" -- #
# ------------------------ #

@given(st.integers(min_value = 0),
       st.integers(min_value = 2, max_value = 99),
       st.sampled_from(OUTPUTS_NO_NB))
def test_base2int_frombXXX_o_bXXXof(nb, base, XXX):
    bnb = Int2Base().int2bnb(
        nb   = nb,
        base = base
    )

    bXXXof_ret = Base2Int().__getattribute__(f"b{XXX}of")(
        bnb  = bnb,
        base = base
    )

    frombXXX_ret = Base2Int().__getattribute__(f"fromb{XXX}")(
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
def test_base2int_bXXX2int_o_int2bXXX(nb, base, XXX):
    n2b_XXX_ret = Int2Base().__getattribute__(f"int2b{XXX}")(
        nb   = nb,
        base = base
    )

    b2n_n2b_NB = Base2Int().__getattribute__(f"b{XXX}2int")(
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
def test_base2int_bYYY2XXX_o_XXX2bYYY(nb, base, XXX, YYY):
    return_of = Int2Base().__getattribute__(f"{XXX}of")(nb)

    XXX2bYYY_ret = Int2Base().__getattribute__(f"{XXX}2b{YYY}")(
        return_of,
        base = base,
    )

    bYYY2XXX_ret = Base2Int().__getattribute__(f"b{YYY}2{XXX}")(
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
def test_base2int_bnb2int_o_int2bnb_with_sep(nb, base, sep):
    int2bnb_ret = Int2Base().int2bnb(
        nb   = nb,
        base = base,
        sep  = sep
    )

    bnb2int_int2bnb_NB = Base2Int().bnb2int(
        bnb  = int2bnb_ret,
        base = base,
        sep  = sep
    )

    assert nb == bnb2int_int2bnb_NB, \
           (
             "\n"
            f"{nb   = }"
             "\n"
            f"{base = }"
             "\n"
            f"{sep  = }"
             "\n"
           )
