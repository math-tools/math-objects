#!/usr/bin/env python3

from mistool.os_use import PPath


# ----------------------- #
# -- GENERAL CONSTANTS -- #
# ----------------------- #

STD_MAXI = 10**9 - 1
STD_MINI = - STD_MAXI

NB_RAND_TESTS = 50


BAD_TYPE_INPUTS = [
    PPath("3") / "2" / "1",
]

BAD_STR_INPUTS = [
    '_112345',
    '112345_',
    '1+2+3*5',
]


# -- CONSTANTS "AUTO" - START -- #

# Lines automatically build by the following file.
#
#     + ``tools/factory/textify/build_02_int2txt_tests.py``

LANGS_SORTED = [
    "fr_FR",
    "it_IT",
    "de_DE",
    "en_GB",
    "es_ES",
    "en_US",
    "fr_BE",
    "fr_FR_chuquet_1",
    "fr_FR_chuquet_2",
    "fr_FR_rowlett",
    "fr_FR_tiret",
]

LANGS_NOBIG = ["fr_FR_chuquet_1", "fr_FR_chuquet_2", "fr_FR_rowlett"]

# -- CONSTANTS "AUTO" - END -- #


TAG_TEST_WHERE   = 'where'
TAG_TEST_INTEGER = 'integer'
TAG_TEST_INITIAL = 'initial'
TAG_TEST_NAME    = 'name'
