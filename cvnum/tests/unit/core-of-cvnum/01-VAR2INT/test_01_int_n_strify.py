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
    'tests',
]:
    _ = addfindsrc(
        file    = __file__,
        project = upfolder,
    )

from src.core  import Var2Int
from unit.core import FakeINT, SOME_SEPS, choice


# --------------- #
# -- CONSTANTS -- #
# --------------- #

VAR_2_INT_DEFAULT = Var2Int()
VAR_2_INT_CONVERT = Var2Int(tryconvert = True)


# --------------- #
# -- INT INPUT -- #
# --------------- #

@given(st.integers())
def test_var2int_int_n_strify_INT_default(intnb):
    int_ret, str_ret = VAR_2_INT_DEFAULT.int_n_strify(varnb = intnb)

    assert str_ret == str(int_ret)
    assert str_ret == str(intnb)


# -------------------- #
# -- FAKE INT INPUT -- #
# -------------------- #

def test_var2int_int_n_strify_FAKE_INT_convert_NOT_OK():
    with pytest.raises(
        AssertionError,
        match = r".*not an integer.*"
    ):
        VAR_2_INT_DEFAULT.int_n_strify(
            varnb = FakeINT(
                n = 20220803, # This looks like a date...
            )
        )


@given(st.integers())
def test_var2int_int_n_strify_FAKE_INT_convert(intnb):
    int_ret, str_ret = VAR_2_INT_CONVERT.int_n_strify(
        varnb = FakeINT(n = intnb)
    )

    assert str_ret == str(int_ret)
    assert str_ret == str(intnb)


@given(st.integers())
def test_var2int_int_n_strify_FAKE_INT_separator(intnb):
    sep = choice(SOME_SEPS)

    var2int_inst = Var2Int(
        tryconvert = True,
        toremove   = [sep]
    )

    int_ret, str_ret = var2int_inst.int_n_strify(
        varnb = FakeINT(
            n = intnb,
            s = sep
        )
    )

    assert str_ret == str(intnb)
