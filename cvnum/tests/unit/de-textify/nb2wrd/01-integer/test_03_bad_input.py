#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

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

from src.textify import *

from constants import *


# --------------- #
# -- BAD INPUT -- #
# --------------- #

def test_nameof_input_string_NOT_OK():
    for lang in LANGS_SORTED:
        nameof = IntName(lang).nameof

        for bad in BAD_STR_INPUTS:
            with pytest.raises(
                (AssertionError, ValueError),
                match = r".*not an integer.*"
            ):
                nameof(bad)


def test_nameof_input_type_NOT_OK():
    for lang in LANGS_SORTED:
        nameof = IntName(lang).nameof

        for bad in BAD_TYPE_INPUTS:
            with pytest.raises(
                (AssertionError, ValueError),
                match = r".*not an integer.*"
            ):
                nameof(bad)
