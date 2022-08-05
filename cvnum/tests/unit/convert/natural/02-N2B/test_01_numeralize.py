#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from functools import reduce
from random    import choice

from   hypothesis            import given
import hypothesis.strategies as st
# import pytest

from cbdevtools import *


# ------------------------------------------ #
# -- MODULE TESTED IMPORTED FROM SOURCES! -- #
# ------------------------------------------ #

for upfolder in [
    'cvnum',
    # 'natural',
    # 'tests',
]:
    _ = addfindsrc(
        file    = __file__,
        project = upfolder,
    )

from src.convert.natural.nat2base import Nat2Base
# from unit.core       import build_removable

# from natcore.constants import *


# ---------------- #
# -- NUMERALIZE -- #
# ---------------- #

@given(st.integers(min_value = 2, max_value = 99))
def test_nat2base_numeralize_len_singles(base):
    numeralize = Nat2Base().numeralize(base)
    allsingles = set(
        numeralize(n)[0]
        for n in range(base)
    )

    assert len(allsingles) == base, \
           f"{base = }"


@given(st.integers(min_value = 2, max_value = 99))
def test_nat2base_numeralize_good_sorted_values(base):
    numeralize = Nat2Base().numeralize(base)
    allsingles = list(
        numeralize(n)[0]
        for n in range(base)
    )

    assert allsingles == sorted(allsingles), \
           f"{base = }"
