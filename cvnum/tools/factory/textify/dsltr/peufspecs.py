#!/usr/bin/env python3

from mistool.os_use import PPath
from orpyste.data   import ReadBlock

from .main import *

# --------------------------- #
# -- TRANSLATIONS TO BUILD -- #
# --------------------------- #

def langdefs(dirlang, verbose = True):
    alltrans = {}

    for onepath in dirlang.walk("dir::*"):
        shortpath = onepath - dirlang

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
            shortpathfile = onefile - dirlang

            if onefile.parent.name.startswith("_"):
                continue

            if verbose:
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

                    alltrans[taglang(mainlang, variant)] = Parser(
                        datas.treedict,
                        shortpathfile
                    ).build()

            except Exception as e:
                stopall(
                    # Exception
                    f"         > {e}",
                    shortpathfile
                )

    return alltrans
