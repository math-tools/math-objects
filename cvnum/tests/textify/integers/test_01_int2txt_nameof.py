#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

import json
import toml

from cbdevtools     import *
from mistool.os_use import PPath


# ------------------------------------------ #
# -- MODULE TESTED IMPORTED FROM SOURCES! -- #
# ------------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'cvnum',
)

from src.textify import *


# ----------------------- #
# -- GENERAL CONSTANTS -- #
# ----------------------- #

THIS_DIR  = PPath(__file__).parent
DATAS_DIR = THIS_DIR / "usecases"


# -------------- #
# -- USECASES -- #
# -------------- #

def test_int2txt_usecases_fr_FR():
    nameof = IntName(fr_FR).nameof
    assert nameof(0) == 0, "OKI?"

def test_int2txt_usecases_AAA():
    assert 4 == 4, "D'ACC?"
