#!/usr/bin/env python3

import json

import translators as ts

from mistool.os_use import PPath
from cbdevtools     import *

from dsltr      import *
from googletrad import *
from usecases   import *


# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'cvnum',
)

from src.textify import *


# ! -- DEBUGGING -- ! #
# nb   = 465
# lang = 'it'
# print(
#     ts.google(
#         query_text  = IntName("en_GB").nameof(nb),
#         to_language = lang
#     )
# )
# exit()
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

TRUSTED_LANG = "en_GB"
# English is better supported by Google Trad than French. Why? :-).

MIN_NB_TESTED = 0

MAX_NB_TESTED = 10**3 - 1
# MAX_NB_TESTED = 0 # No Google Trad.

SLICE_SIZE = 100
# SLICE_SIZE = 14
# 3   : good choice.
#       No coffee beeded.
# 50  : good choice to not be blocked by the API.
#       Slow...
# 100 : possible choice to not be blocked by the API.
#       Very slow...


THIS_DIR = PPath(__file__).parent

SRC_DIR = THIS_DIR

while(SRC_DIR.name != "cvnum"):
    SRC_DIR = SRC_DIR.parent

DIR_LANG             = SRC_DIR / "contribute" / "api" / "textify" / "lang"
PYTEST_DIR           = SRC_DIR / "tests" / "textify" / "integers"
TEST_TRANSLATORS_DIR = PYTEST_DIR / "translators" / "small"


# ----------------- #
# -- TESTS TO DO -- #
# ----------------- #

ALL_LANGS = set(langdefs(DIR_LANG, verbose = False))

LANGS_GOOGLE_IDS = {  # Debug --> None,#
    #
    'de_DE': "de",
    #
    'en_GB': 'en',
    'en_US': "en-US",
    #
    'es_ES': "es",
    # We can look quickly that the script does a good job
    # with the language ``fr_FR``.
    'fr_FR': "fr",
    'fr_BE'          : None,  # Not testable via Google.
    'fr_FR_chuquet_1': None,  # Not testable via Google.
    'fr_FR_chuquet_2': None,  # Not testable via Google.
    'fr_FR_rowlett'  : None,  # Not testable via Google.
    'fr_FR_tiret'    : None,  # Not testable via Google.
    #
    'it_IT': "it",
}

assert ALL_LANGS == set(LANGS_GOOGLE_IDS)

assert not LANGS_GOOGLE_IDS[TRUSTED_LANG] is None
GOOGLE_TRUSTED_LANG = LANGS_GOOGLE_IDS[TRUSTED_LANG]


TAG_BUS        = "bus"
TAGS_TO_REMOVE = set(
    " " + ts.google(
        query_text    = TAG_BUS,
        from_language = GOOGLE_TRUSTED_LANG,
        to_language   = gid
    ).lower()
    for gid in LANGS_GOOGLE_IDS.values()
    if not gid is None
)


TEXTS_TESTED = []

nameof_TRUSTED = IntName(TRUSTED_LANG).nameof

for i in range(MIN_NB_TESTED, MAX_NB_TESTED + 1):
    totrans = f"{nameof_TRUSTED(str(i))}"

    if i == 1:
        totrans += f" {TAG_BUS}"

    TEXTS_TESTED.append( (str(i), totrans) )

# TEXTS_TESTED = TEXTS_TESTED[:20]
# print(TEXTS_TESTED[61]);exit()


# ------------------------------ #
# -- RESULTS FROM TRANSLATORS -- #
# ------------------------------ #

print(
     "    * Working with Google Trad with trusted "
    f"lang << {TRUSTED_LANG} >>. "
     "\n"
     "      It's time to drink a coffee... Or not."
)

for lang, gid in LANGS_GOOGLE_IDS.items():
    # ! -- DEBUGGING -- ! #
    # continue
    # ! -- DEBUGGING -- ! #

    if lang == TRUSTED_LANG:
        continue

    if gid is None:
        print(f"    * Google Trad.: no support for << {lang} >> .")

        continue

# We work by small ranges of values suchas to not saturate
# the Google API.
    gtrad_json_file = TEST_TRANSLATORS_DIR / f"{lang}.json"

    if gtrad_json_file.is_file():
        with gtrad_json_file.open(
            encoding = 'utf-8',
            mode = 'r'
        ) as f:
            results = json.load(f)

    else:
        results = {}

    if len(results) == MAX_NB_TESTED:
        continue

    print(f"    * Google Trad.: << {TRUSTED_LANG} >> to << {lang} >>.")
    tabgtrad = " "*len("    * Google Trad.: ")

    print(f"{tabgtrad}Be patient...")

    nb_treated = 0
    nb_trads   = 0
    lastnb     = None

    for nb, name in TEXTS_TESTED:
        if nb in results and MIN_NB_TESTED == 0:
            continue

        nb_treated += 1

        if(nb_treated > SLICE_SIZE):
            break

        nb_trads += 1
        lastnb    = nb

        gtrad = ts.google(
            query_text    = name,
            from_language = GOOGLE_TRUSTED_LANG,
            to_language   = gid
        )
        gtrad = gtrad.lower()

        if nb == "1":
            for toremove in TAGS_TO_REMOVE:
                gtrad = gtrad.replace(toremove, "")

        gtrad = gtrad.strip()

        results[nb] = gtrad


    print("\x1b[1A\x1b[2K", end = "")

    if lastnb is None:
        print(f"{tabgtrad}Nothing new.")

    else:
        print(f"{tabgtrad}Last number treated: {lastnb}.")
        print(f"{tabgtrad}Building the ''Google'' JSON file.")

        with gtrad_json_file.open(
            encoding = "utf-8",
            mode     = "w"
        ) as f:
            f.write(json.dumps(results))

# ! -- DEBUGGING -- ! #
# from pprint import pprint
# pprint(GOOGLE_RESULTS)
# ! -- DEBUGGING -- ! #


# ------------------------- #
# -- PATCHINGS BAD TRADS -- #
# ------------------------- #

print(f"    * Looking for corrections of some bad Google trads.")

for lang, gid in LANGS_GOOGLE_IDS.items():
    if gid is None:
        continue

    gtrad_json_file = TEST_TRANSLATORS_DIR / f"{lang}.json"

    if not gtrad_json_file.is_file():
        continue

    with gtrad_json_file.open(
        encoding = 'utf-8',
        mode = 'r'
    ) as f:
        allgtrads = json.load(f)

    nberrors   = 0
    langnameof = IntName(lang).nameof

    for nb, gtrad in allgtrads.items():
        correction = correct_badtrad(lang, nb, gtrad, langnameof)

        if gtrad != correction:
            nberrors      += 1
            allgtrads[nb]  = correction

            # print(nb, gtrad, correction, sep = " -> ")

    if nberrors:
        with gtrad_json_file.open(
            encoding = "utf-8",
            mode     = "w"
        ) as f:
            f.write(json.dumps(allgtrads))

        plurial = "s" if nberrors > 1 else ""

        print(
            f"    * Google Trad. << {lang} >> has been corrected. "
             "\n"
            f"      {nberrors} error{plurial} found."
        )
