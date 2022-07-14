#!/usr/bin/env python3

from dsltr import *


# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

DEBUG_CODING = False
# DEBUG_CODING = True

THIS_DIR = PPath(__file__).parent

SRC_DIR = THIS_DIR

while(SRC_DIR.name != "cvnum"):
    SRC_DIR = SRC_DIR.parent

DIR_LANG       = SRC_DIR / "contribute" / "api" / "textify" / "lang"
SRC_DIR_CONFIG = SRC_DIR / "src" / "config"


# ----------------------------------------- #
# -- LET'S BUILD THE PYTHON CONFIG. FILE -- #
# ----------------------------------------- #

LANGS_DEFS = langdefs(DIR_LANG)

print(f"   * Working on the final source codes.")

pythonify(
    DEBUG_CODING,
    LANGS_DEFS,
    SRC_DIR_CONFIG / "textify" / "langint.py"
)
