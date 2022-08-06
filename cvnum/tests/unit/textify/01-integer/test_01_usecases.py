#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

import json

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


# ----------------------- #
# -- GENERAL CONSTANTS -- #
# ----------------------- #

THIS_DIR           = PPath(__file__).parent
DATAS_USECASES_DIR = THIS_DIR / "usecases"


# -------------- #
# -- USECASES -- #
# -------------- #

def test_nameof_usecases():
    for lang in LANGS_SORTED:
        nameof = IntName(lang).nameof

        with (DATAS_USECASES_DIR / f"{lang}.json").open(
            encoding = 'utf-8',
            mode = 'r'
        ) as f:
            datas = json.load(f)

        for onedata in datas:
            nb          = onedata[TAG_TEST_INTEGER]
            name_wanted = onedata[TAG_TEST_NAME]

            assert nameof(nb) == name_wanted, \
                   (
                    "\n"
                    f"LANG   : {lang}"
                    "\n"
                    f"INITIAL: {onedata[TAG_TEST_INITIAL]}"
                    "\n"
                    f"WHERE  : {onedata[TAG_TEST_WHERE]}"
                    "\n"
                   )
