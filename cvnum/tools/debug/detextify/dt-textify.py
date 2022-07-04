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

lang = de_DE
lang = en_GB
lang = it_IT
lang = es_ES
lang = fr_FR

nbtests_by_slice = 2

intname = IntName(lang)

for x in [
    0,
    # 987,
    # 999,
    # - 435,
    # 506,
    # 4**3, # = 64
    # - 23_456_789_012,
    - 999_000_000_000_666_555_444_333_222_111,
    # 123456789012345678901234567890,
]:
    testandprint(intname, x)

print('---')

exit()

print()

powers = [2, 3, 6, 9, 12, 15]

for i, n in enumerate(powers):
    x_tested = []
    n_prev   = powers[i-1]

    min = 0 if i == 0 else 10**n_prev
    max = 10**powers[i]

    min_txt = "0" if min == 0 else f"10**{n_prev}"

    print(f'--- RANDOM -- {min_txt} <= ... <= 10**{n} -- RANDOM ---')

    for _ in range(nbtests_by_slice):
        while((x := randint(min, max)) in x_tested):
            continue

        x_tested.append(x)

        testandprint(intname, x)

print('---')
