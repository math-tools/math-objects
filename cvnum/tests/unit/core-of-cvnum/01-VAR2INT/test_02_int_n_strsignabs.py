#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from functools import reduce

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

from src.core import Var2Int
# from unit.core        import FakeINT, SOME_SEPS, choice


# --------------- #
# -- CONSTANTS -- #
# --------------- #

INT_N_STRSIGNABS_DEFAULT = Var2Int().int_n_strsignabs
INT_N_STRSIGNABS_CONVERT = Var2Int(
    tryconvert = True,
).int_n_strsignabs


# ------------------------------- #
# -- INT INPUT - NO ``+`` SIGN -- #
# ------------------------------- #

@given(st.integers())
def test_var2int_int_n_strsignabs_INT_no_plus(intnb):
    str_intnb  = '+' if intnb > 0 else ''
    str_intnb += str(intnb)

    int_ret, sign, absstr_ret = INT_N_STRSIGNABS_CONVERT(
        varnb = str_intnb
    )

    assert int_ret == intnb
    assert absstr_ret == str(abs(int_ret))

    if intnb < 0:
        assert sign == '-'

    elif intnb == 0:
        assert sign == ''

    else:
        assert sign == '+'



# --------------------------------- #
# -- INT INPUT - WITH ``+`` SIGN -- #
# --------------------------------- #

@given(st.integers())
def test_var2int_int_n_strsignabs_INT_with_plus(intnb):
    int_ret, sign, absstr_ret = INT_N_STRSIGNABS_DEFAULT(
        varnb = intnb
    )

    assert int_ret == intnb
    assert absstr_ret == str(abs(int_ret))

    if intnb < 0:
        assert sign == '-'

    else:
        assert sign == ''
