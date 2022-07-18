#!/usr/bin/env python3

import json

from mistool.os_use import PPath
from cbdevtools import *


# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

LANG_TESTED = 'de_DE'

TO_ANALYSE = [
    50 + x*100
    for x in range(2, 10)
    # if
]
# TO_ANALYSE = range(10**3)


THIS_DIR = PPath(__file__).parent

SRC_DIR = THIS_DIR

while(SRC_DIR.name != "cvnum"):
    SRC_DIR = SRC_DIR.parent

DIR_LANG             = SRC_DIR / "contribute" / "api" / "textify" / "lang"
PYTEST_DIR           = SRC_DIR / "tests" / "textify" / "integers"
TEST_TRANSLATORS_DIR = PYTEST_DIR / "translators" / "small"


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'cvnum',
)

from src.textify import *


# ----------------- #
# -- TESTS TO DO -- #
# ----------------- #

for lang in ALL_LANGS:
    if lang != LANG_TESTED:
        continue

    gtrad_json_file = TEST_TRANSLATORS_DIR / f"{lang}.json"

    if not gtrad_json_file.is_file():
        continue

    nameof = IntName(lang).nameof

    with gtrad_json_file.open(
        encoding = 'utf-8',
        mode = 'r'
    ) as f:
        gnames = json.load(f)

    for nb in TO_ANALYSE:
        nb = str(nb)

        if not nb in gnames:
            continue

        name   = gnames[nb]
        cvname = nameof(nb)

        if name != cvname:
            print(f"{nb} -- Google [{lang}] --> {name}")
            print(f"{' '*len(nb)} -- cvnum  [{lang}] --> {cvname}")
