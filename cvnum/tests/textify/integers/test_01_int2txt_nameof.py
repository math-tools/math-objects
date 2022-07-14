#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

import json

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

TAG_TEST_WHERE   = 'where'
TAG_TEST_INTEGER = 'integer'
TAG_TEST_INITIAL = 'initial'
TAG_TEST_NAME    = 'name'

LANGS_SORTED = ['fr_FR', 'it_IT', 'de_DE', 'en_GB', 'es_ES', 'en_US', 'fr_BE', 'fr_FR_chuquet_1', 'fr_FR_chuquet_2', 'fr_FR_rowlett', 'fr_FR_tiret']


# -------------- #
# -- USECASES -- #
# -------------- #

def test_int2txt_usecases():
    for lang in LANGS_SORTED:
        nameof = IntName(lang).nameof

        with (DATAS_DIR / f"{lang}.json").open(
            encoding = 'utf-8',
            mode = 'r'
        ) as f:
            datas = json.load(f)

        for onedata in datas:
            int_val     = onedata[TAG_TEST_INTEGER]
            name_wanted = onedata[TAG_TEST_NAME]

            assert nameof(int_val) == name_wanted, \
                   (
                    "\n"
                    f"LANG   : {lang}"
                    "\n"
                    f"INITIAL: {onedata[TAG_TEST_INITIAL]}"
                    "\n"
                    f"WHERE  : {onedata[TAG_TEST_WHERE]}"
                   )
