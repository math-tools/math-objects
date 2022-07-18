#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

import json
import pytest
from   random import randint

from cbdevtools     import *
from mistool.os_use import PPath


# ------------------------------------------ #
# -- MODULE TESTED IMPORTED FROM SOURCES! -- #
# ------------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'cvnum',
)

from src.textify import *


# ----------------------- #
# -- GENERAL CONSTANTS -- #
# ----------------------- #

NB_RAND_TESTS = 50

BAD_INPUTS = [
    '_112345',
    '112345_',
    '1+2+3*5',
]

# -- CONSTANTS "AUTO" - START -- #

LANGS_SORTED = ['fr_FR', 'it_IT', 'de_DE', 'en_GB', 'es_ES', 'en_US', 'fr_BE', 'fr_FR_chuquet_1', 'fr_FR_chuquet_2', 'fr_FR_rowlett', 'fr_FR_tiret']

LANGS_NOBIG = ['fr_FR_chuquet_1', 'fr_FR_chuquet_2', 'fr_FR_rowlett']

# -- CONSTANTS "AUTO" - END -- #


THIS_DIR              = PPath(__file__).parent
DATAS_USECASES_DIR    = THIS_DIR / "usecases"
DATAS_TRANSLATORS_DIR = THIS_DIR / "translators"

TAG_TEST_WHERE   = 'where'
TAG_TEST_INTEGER = 'integer'
TAG_TEST_INITIAL = 'initial'
TAG_TEST_NAME    = 'name'


# ------------------------------------ #
# -- SPACES/UNDERSCORES IGNORED BIG -- #
# ------------------------------------ #

def test_nameof_spaces_underscores_ignored():
    for lang in LANGS_SORTED:
        mynamer = IntName(lang)
        nameof  = lambda x: mynamer.nameof(x, tryconvert = True)
        maxpos  = 10**(2*mynamer._big_expo_max) - 1
        minneg  = - maxpos

        for _ in range(NB_RAND_TESTS):
            randnb          = randint(minneg, maxpos)
            randnb_polluted = ''

            for c in str(randnb):
                if (
                    c != '-'
                    and
                    randnb_polluted not in ['', '-']
                    and
                    randint(0, 10) <= 7
                ):
                    if randint(0, 1) == 0:
                        randnb_polluted += " "

                    else:
                        randnb_polluted += "_"

                randnb_polluted += c

            assert nameof(randnb) == nameof(randnb_polluted)


# --------------- #
# -- BAD INPUT -- #
# --------------- #

def test_nameof_badinput():
    for lang in LANGS_SORTED:
        nameof = lambda x: IntName(lang).nameof(x, tryconvert = True)

        for badinput in BAD_INPUTS:
            with pytest.raises(
                ValueError,
                match = r".*not an integer.*"
            ):
                nameof(badinput)


# ------------- #
# -- BIGGEST -- #
# ------------- #

def test_nameof_biggest():
    for lang in LANGS_NOBIG:
        mynamer = IntName(lang)
        maxpos  = 10**(2*mynamer._big_expo_max) - 1
        minneg  = - maxpos

        assert mynamer.nameof(maxpos)
        assert mynamer.nameof(minneg)


# ------------ #
# -- NO BIG -- #
# ------------ #

def test_nameof_nobig():
    for lang in LANGS_NOBIG:
        mynamer  = IntName(lang)
        maxpower = mynamer._big_expo_max

        for _ in range(NB_RAND_TESTS):
            rnd_big = 10**(2*maxpower) + randint(0, 10**6)

            if randint(0, 1) == 0:
                rnd_big *= -1

            with pytest.raises(
                AssertionError,
                match = r".*number too big.*"
            ):
                mynamer.nameof(rnd_big)


# -------------- #
# -- USECASES -- #
# -------------- #

def test_nameof_usecases():
    for lang in LANGS_SORTED:
        nameof = lambda x: IntName(lang).nameof(x, tryconvert = True)

        with (DATAS_USECASES_DIR / f"{lang}.json").open(
            encoding = 'utf-8',
            mode = 'r'
        ) as f:
            datas = json.load(f)

        for onedata in datas:
            int_val     = onedata[TAG_TEST_INTEGER]
            name_wanted = onedata[TAG_TEST_NAME]

            assert nameof(int_val) == name_wanted, \
                   (
                    "\n"
                    f"LANG   : {lang}"
                    "\n"
                    f"INITIAL: {onedata[TAG_TEST_INITIAL]}"
                    "\n"
                    f"WHERE  : {onedata[TAG_TEST_WHERE]}"
                   )


# ----------------- #
# -- TRANSLATORS -- #
# ----------------- #

def test_nameof_translators_small():
    for lang in LANGS_SORTED:
        nameof = lambda x: IntName(lang).nameof(x, tryconvert = True)

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
                   )
