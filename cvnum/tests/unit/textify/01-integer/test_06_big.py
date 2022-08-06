#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from random import randint

import pytest

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


# ------------- #
# -- BIGGEST -- #
# ------------- #

def test_nameof_biggest():
    for lang in LANGS_NOBIG:
        mynamer = IntName(lang)
        nameof  = lambda x: IntName(lang).nameof(str(x))
        maxpos  = 10**(2*mynamer._big_expo_max) - 1
        minneg  = - maxpos

        assert nameof(maxpos)
        assert nameof(minneg)


# ------------ #
# -- NO BIG -- #
# ------------ #

def test_nameof_nobig_NOT_OK():
    for lang in LANGS_NOBIG:
        mynamer  = IntName(lang)
        nameof   = lambda x: IntName(lang).nameof(str(x))
        maxpower = mynamer._big_expo_max

        for _ in range(NB_RAND_TESTS):
            rnd_big = 10**(2*maxpower) + randint(0, 10**6)

            if randint(0, 1) == 0:
                rnd_big *= -1

            with pytest.raises(
                AssertionError,
                match = r".*number too big.*"
            ):
                nameof(rnd_big)
