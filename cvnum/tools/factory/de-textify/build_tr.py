#!/usr/bin/env python3

from mistool.os_use import PPath
from orpyste.data import ReadBlock

from dsltr import *


# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

DEBUG_CODING = False
DEBUG_CODING = True

THIS_DIR = PPath(__file__).parent
DIR_LANG = THIS_DIR / "lang"

SRC_DIR_CONFIG = THIS_DIR

while(SRC_DIR_CONFIG.name != "cvnum"):
    SRC_DIR_CONFIG = SRC_DIR_CONFIG.parent

SRC_DIR_CONFIG = SRC_DIR_CONFIG / "src" / "config"


# --------------------------- #
# -- TRANSLATIONS TO BUILD -- #
# --------------------------- #

ALL_TRANS = {}

for onepath in DIR_LANG.walk("dir::*"):
    shortpath = onepath - DIR_LANG

    if shortpath.depth != 1:
        continue

    mainlang = shortpath.parent.name
    mainlang = mainlang.lower()
    variant  = shortpath.name

# ! -- DEBUGGING -- ! #
    # if mainlang != "fr":
    # if variant != "BE":
    # if not(mainlang == "fr" and variant == "FR"):
    #     continue
# ! -- DEBUGGING -- ! #

    for onefile in onepath.walk("file::*.txt"):
        shortpathfile = onefile - DIR_LANG

        if onefile.parent.name.startswith("_"):
            continue

        print(f"   * Working on << {shortpathfile} >>.")

        try:
            with ReadBlock(
                content = onefile,
                mode    = MODE_TRANS
            ) as datas:
# ! -- DEBUGGING -- ! #
                # LANG_TESTED = "fun_SHA"
                # LANG_TESTED = "fr_FR"
                # LANG_TESTED = "en_GB"
                # if f"{mainlang}_{variant}" != LANG_TESTED:
                #     continue
# ! -- DEBUGGING -- ! #

                ALL_TRANS[taglang(f"{mainlang}_{variant}")] = Parser(
                    datas.treedict,
                    shortpathfile
                ).build()

        except Exception as e:
            stopall(
                # Exception
                f"         > {e}",
                shortpathfile
            )


# ----------------------------------------- #
# -- LET'S BUILD THE PYTHON CONFIG. FILE -- #
# ----------------------------------------- #

print(f"   * Working on the final source codes.")

pythonify(
    DEBUG_CODING,
    ALL_TRANS,
    SRC_DIR_CONFIG / "detextify" / "langint.py"
)
