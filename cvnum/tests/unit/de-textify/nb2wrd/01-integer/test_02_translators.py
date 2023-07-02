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

THIS_DIR              = PPath(__file__).parent
DATAS_TRANSLATORS_DIR = THIS_DIR / "translators"


# ----------------- #
# -- TRANSLATORS -- #
# ----------------- #

def test_nameof_translators_small():
    for lang in LANGS_SORTED:
        nameof = IntName(lang).nameof

        gtrad_json_file = DATAS_TRANSLATORS_DIR / "small" / f"{lang}.json"

        if not gtrad_json_file.is_file():
            continue

        with gtrad_json_file.open(
            encoding = 'utf-8',
            mode = 'r'
        ) as f:
            datas = json.load(f)

        allnbs = list(datas)

        for nb in allnbs:
            gtrad = datas[nb]

            assert nameof(nb) == gtrad, \
                   (
                    "\n"
                    f"LANG: {lang}"
                    "\n"
                    f"NB  : {nb}"
                    "\n"
                   )
