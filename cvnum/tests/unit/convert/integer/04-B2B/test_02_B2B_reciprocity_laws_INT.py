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

from src.convert.integer.base2base import Base2Base
from src.convert.integer.int2base  import Int2Base

from intcore.constants import *


# ------------------------ #
# -- "RECIPROCITY LAWS" -- #
# ------------------------ #

@given(st.integers(min_value = 0),
       st.integers(min_value = 2, max_value = 99),
       st.integers(min_value = 2, max_value = 99),
       st.sampled_from(OUTPUTS_ALL),
       st.sampled_from(OUTPUTS_ALL))
def test_base2base_bYYY2bXXX_o_bXXX2bYYY(nb, base_in, base_out, XXX, YYY):
    int2bXXX_ret = Int2Base().__getattribute__(f"int2b{XXX}")(
        nb   = nb,
        base = base_in,
    )

    bXXX2bYYY_ret = Base2Base().__getattribute__(f"b{XXX}2b{YYY}")(
        int2bXXX_ret,
        base_in  = base_in,
        base_out = base_out,
    )

    bYYY2bXXX_o_bXXX2bYYY_found = Base2Base().__getattribute__(
        f"b{YYY}2b{XXX}"
    )(
        bXXX2bYYY_ret,
        base_in  = base_out,
        base_out = base_in,
    )

    assert bYYY2bXXX_o_bXXX2bYYY_found == int2bXXX_ret, \
           (
             "\n"
            f"{nb       = }"
             "\n"
            f"{base_in  = }"
             "\n"
            f"{base_out = }"
             "\n"
            f"{XXX      = }"
             "\n"
            f"{YYY      = }"
             "\n"
           )
