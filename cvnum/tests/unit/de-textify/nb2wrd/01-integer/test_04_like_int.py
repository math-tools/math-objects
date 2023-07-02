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
    'tests',
]:
    _ = addfindsrc(
        file    = __file__,
        project = upfolder,
    )

from src.textify import *
from unit.core   import FakeINT

from constants import *


# -------------------------------------------- #
# -- FAKE INT INPUT - INT & STRING VERSIONS -- #
# -------------------------------------------- #

@given(st.integers(min_value = STD_MINI, max_value = STD_MAXI))
def test_nameof_FAKE_INT_convert(nb):
    for lang in LANGS_SORTED:
        nameof = IntName(lang).nameof

        int_name  = nameof(varnb = FakeINT(n = nb))
        fake_name = nameof(varnb = nb)

        assert int_name == fake_name, \
               (
                "\n"
                f"LANG: {lang}"
                "\n"
                f"NB  : {nb}"
                "\n"
               )
