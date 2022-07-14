#!/usr/bin/env python3

from mistool.os_use     import PPath
from mistool.string_use import between

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
PYTEST_DIR       = SRC_DIR / "tests" / "textify" / "integers"
TEST_USECASE_DIR = PYTEST_DIR / "usecases"
TEST_PYFILE      = PYTEST_DIR / "test_01_int2txt_nameof.py"

# ------------------ #
# -- RULES & DEPS -- #
# ------------------ #

print(f"   * Preparing specs to build the tests...")

RULES_TO_IGNORE, DEPENDENCIES = usecases_deps(DIR_LANG)

# ! -- DEBUGGING -- ! #
# print(f"{DEPENDENCIES = }")
# print()
# print(f"{RULES_TO_IGNORE['fr_FR'].keys()           = }")
# print(f"{RULES_TO_IGNORE['fr_BE'].keys()           = }")
# print(f"{RULES_TO_IGNORE['fr_FR_chuquet_1'].keys() = }")
# exit()
# ! -- DEBUGGING -- ! #


# -------------- #
# -- USECASES -- #
# -------------- #

print("   * Looking for usecases...")

USECASES_PATHS, WITH_SPECIAL = usecases_files(
    DIR_LANG,
    DEPENDENCIES
)

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

print("   * Let's build the tests...")

TAG_SPE     = 'with spe cases and no dep'
TAG_DEP_NO  = 'no dep'
TAG_DEP_YES = 'some deps'

langs_met    = WITH_SPECIAL.copy()
langs_categos = {
    TAG_SPE    : WITH_SPECIAL.copy(),
    TAG_DEP_NO : [],
    TAG_DEP_YES: [],
}

for lang in USECASES_PATHS:
    if(
        not lang in DEPENDENCIES
        and
        not lang in langs_met
    ):
        langs_met.append(lang)
        langs_categos[TAG_DEP_NO].append(lang)

for lang in USECASES_PATHS:
    if not lang in langs_met:
        langs_met.append(lang)
        langs_categos[TAG_DEP_YES].append(lang)


langs_sorted = []

for about, langsfound in langs_categos.items():
    langsfound.sort()

    for lang in langsfound:
        langs_sorted.append(lang)

        print(
            f"   * Tests for ``{lang}`` ({about})")

        buildtests_json(
            lang         = lang,
            testdir      = TEST_USECASE_DIR,
            usecases     = USECASES_PATHS[lang],
        )


with TEST_PYFILE.open(
    encoding = "utf-8",
    mode     = "r",
) as f:
    pycode = f.read()

before, _, after = between(
    text     = pycode,
    seps     = ['LANGS_SORTED', '# --'],
    keepseps = True
)

pycode = f"""{before} = {langs_sorted}


{after}"""

with TEST_PYFILE.open(
    encoding = "utf-8",
    mode     = "w",
) as f:
    f.write(pycode)
