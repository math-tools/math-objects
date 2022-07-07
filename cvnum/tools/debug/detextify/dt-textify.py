#!/usr/bin/env python3

from random import randint

from cbdevtools import *


# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'cvnum',
)


# ----------- #
# -- TOOLS -- #
# ----------- #

def testandprint(intname, x):
    print('---')
    print()
    print(x)
    print(f'  --> {intname.nameof(x)}')
    print()


# -------------- #
# -- LET'S GO -- #
# -------------- #

from src.textify import *

USE_RAND = True
USE_RAND = False

RAND_POWERS = [2, 3, 6, 9, 12, 15]
RAND_POWERS = [2, 3, 4, 5]

lang = de_DE
lang = en_GB
lang = it_IT
lang = es_ES
lang = fr_FR
lang = fr_FR_tiret

nbtests_by_slice = 2

intname = IntName(lang)

if not USE_RAND:
    for x in [
        # 0,
        # 1,
        # 11,
        # 111,
        # 2111,
        # 22111,
        # 222111,
        # 3222111,
        # 33222111,
        # 333222111,
        # 4333222111,
        # 44333222111,
        # 444333222111,
        5444333222111,
        55444333222111,
        "   123  ",
        "-   321",
        # 1,
        # 22,
        # 4444,
        # 55555,
        # 987,
        # 999,
        # - 435,
        # 506,
        # 4**3, # = 64
        # 444_333222111,
        # 555444_333222111,
        # 444_333000111,
        # - 23_456789012,
        # - 999_000000000_666555444_333222111,
        10**9,
        2*10**18,
        3*10**36 + 10**18,
        4*10**36,
        # 123456789012345678901234567890,
    ]:
        testandprint(intname, x)

    print('---')

else:
    for i, n in enumerate(RAND_POWERS):
        x_tested = []
        n_prev   = RAND_POWERS[i-1]

        min = 0 if i == 0 else 10**n_prev
        max = 10**RAND_POWERS[i]

        min_txt = "0" if min == 0 else f"10**{n_prev}"

        title = f'--- RANDOM -- {min_txt} <= ... <= 10**{n} -- RANDOM ---'
        deco  = "-"*len(title)

        print()
        print(deco)
        print(title)
        print(deco)
        print()

        for _ in range(nbtests_by_slice):
            while((x := randint(min, max)) in x_tested):
                continue

            x_tested.append(x)

            testandprint(intname, x)

    print('---')
