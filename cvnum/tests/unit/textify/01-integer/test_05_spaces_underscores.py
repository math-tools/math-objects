#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from random import randint

from cbdevtools import *


# ------------------------------------------ #
# -- MODULE TESTED IMPORTED FROM SOURCES! -- #
# ------------------------------------------ #

for upfolder in [
    'cvnum',
    'tests',
]:
    _ = addfindsrc(
        file    = __file__,
        project = upfolder,
    )

from src.textify import *
from unit.core   import build_removable

from constants import *


# ------------------------------------ #
# -- SPACES/UNDERSCORES IGNORED BIG -- #
# ------------------------------------ #

def test_nameof_spaces_underscores_ignored():
    for lang in LANGS_SORTED:
        mynamer = IntName(lang)
        nameof  = mynamer.nameof
        maxpos  = 10**(2*mynamer._big_expo_max) - 1

        for _ in range(NB_RAND_TESTS):
            randnb          = str(randint(0, maxpos))
            randnb_polluted = build_removable(
                nb         = randnb,
                toremove   = [' ', '_'],
                atleastone = "_",
            )

            assert nameof(randnb) == nameof(randnb_polluted), \
                   (
                    "\n"
                    f"{randnb          = }"
                    "\n"
                    f"{randnb_polluted = }"
                   )
