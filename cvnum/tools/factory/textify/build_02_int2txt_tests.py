#!/usr/bin/env python3

from collections import defaultdict

from mistool.os_use import PPath
from orpyste.data   import ReadBlock

from dsltr    import *
from usecases import *

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = PPath(__file__).parent

SRC_DIR = THIS_DIR

while(SRC_DIR.name != "cvnum"):
    SRC_DIR = SRC_DIR.parent

DIR_LANG         = SRC_DIR / "contribute" / "api" / "textify" / "lang"
TEST_USECASE_DIR = SRC_DIR / "tests" / "textify" / "integers" / "usecases"


TAGS_FOR_IGNORED_TESTS = [
    DSL_SPECS_IGNORE_GROUP,
    DSL_SPECS_IGNORE_SMALL,
]

EMPTY_PATH   = '.'
SPECIAL_FILE = "special.txt"

TAGS_FOR_IGNORED_TESTS = [
    DSL_SPECS_IGNORE_GROUP,
    DSL_SPECS_IGNORE_SMALL,
]

KINDS_FOR_TESTS = [
    "group",
    "sign",
    "small",
    "verybig",
]


# ------------------ #
# -- LANGS & DEPS -- #
# ------------------ #

print(f"   * Preparing specs to build the tests.")

RULES_TO_IGNORE = langdefs(DIR_LANG)
DEPENDENCIES    = extend_deps(RULES_TO_IGNORE)

# Just keep the tags useful for testing.
for specs in RULES_TO_IGNORE.values():
    tags = list(specs)

    for onetag in tags:
        if not onetag in TAGS_FOR_IGNORED_TESTS:
            del specs[onetag]
            continue

        if onetag == DSL_SPECS_IGNORE_SMALL:
            specs[onetag] = [
                pattern
                for kind, pattern in specs[onetag]
                if kind == DSL_ACTION_MATCHING
            ]

# ! -- DEBUGGING -- ! #
# print(f"{DEPENDENCIES = }")
# print()
# print(f"{LANG_TO_IGNORE['fr_FR'].keys()           = }")
# print(f"{LANG_TO_IGNORE['fr_BE'].keys()           = }")
# print(f"{LANG_TO_IGNORE['fr_FR_chuquet_1'].keys() = }")
# exit()
# ! -- DEBUGGING -- ! #


# -------------- #
# -- USECASES -- #
# -------------- #

print("   * Looking for usecases.")

USECASES     = {}
WITH_SPECIAL = []

for onepath in DIR_LANG.walk("dir::*"):
    shortpath = onepath - DIR_LANG

    if shortpath.depth != 1:
        continue

    mainlang = shortpath.parent.name
    mainlang = mainlang.lower()
    variant  = shortpath.name
    lang     = taglang(mainlang, variant)

    usecases_lang = defaultdict(list)

    path_usecases_int = onepath / "usecases" / "integers"

    assert path_usecases_int.is_dir(), \
           (
             "Missing folder ``usecases/integers`` "
            f"in ``{mainlang}/{variant}``."
           )

    for onefile in path_usecases_int.walk("file::**.txt"):
        kind = onefile - path_usecases_int
        kind = str(kind.parent)

        usecases_lang[kind].append(onefile.name)

    for kind, filesfound in usecases_lang.items():
        if kind == EMPTY_PATH:
            assert usecases_lang[EMPTY_PATH] == [SPECIAL_FILE], \
                   (
                    f"only the file ``{SPECIAL_FILE}`` can be used "
                    "directly in the folder ``usecases/integers``."
                   )

            usecases_lang[kind] = SPECIAL_FILE
            WITH_SPECIAL.append(lang)

        else:
            assert kind in KINDS_FOR_TESTS, \
                   f"unkown kind ``{kind}`` not in {KINDS_FOR_TESTS}"

            usecases_lang[kind] = sorted(
                filesfound,
                key = lambda x: (len(x), x)
            )

    USECASES[lang] = usecases_lang

# ! -- DEBUGGING -- ! #
# from pprint import pprint
# print(f"{WITH_SPECIAL = }")
# pprint(USECASES["en_GB"])
# pprint(USECASES["fr_FR"])
# exit()
# ! -- DEBUGGING -- ! #


# --------------------- #
# -- BUILD THE TESTS -- #
# --------------------- #

print("   * Let's build the tests.")


for lang in WITH_SPECIAL:
    print(f"   * Tests for ``{lang}`` (that uses special cases).")

    buildtestsforlang(
        lang         = lang,
        testdir      = TEST_USECASE_DIR,
        usecases     = USECASES,
        deps         = DEPENDENCIES,
        rulesignored = RULES_TO_IGNORE,
    )
    del USECASES[lang]


for lang, usecases_lang in USECASES.items():
    print(f"   * Tests for ``{lang}``.")
