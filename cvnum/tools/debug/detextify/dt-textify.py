#!/usr/bin/env python3

from random import randint

from cbdevtools import *


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


# -------------- #
# -- LET'S GO -- #
# -------------- #

from src.textify import *

lang = 'fr_FR'
# lang = 'ge_GE'

nbtests_by_slice = 1

intname = IntName(lang)

print('---')

x = - 999_888_777_000_666_555_444_333_222_111
print(x)
print(f'    -> {intname.nameof(x)}')
print()

exit()

x = 0
print(x)
print(f'    -> {intname.nameof(x)}')
print()

exit()

x = - 23_456_789_012
print(x)
print(f'    -> {intname.nameof(x)}')
print()

exit()

x = 987
print(x)
print(f'    -> {intname.nameof(x)}')
print()

exit()

x = 999
print(x)
print(f'    -> {intname.nameof(x)}')
print()

exit()

x = -435
print(x)
print(f'    -> {intname.nameof(x)}')
print()

# exit()

x = 4**3
print(x)
print(f'    -> {intname.nameof(x)}')
print()

exit()

x = 123456789012345678901234567890
print(x)
print(f'    -> {intname.nameof(x)}')
print()

# exit()

x = 506

print(x)
print(f'    -> {intname.nameof(x)}')
print()

# exit()

powers = [2, 3, 6, 9, 12, 15]

for i, n in enumerate(powers):
    x_tested = []

    min = 0 if i == 0 else 10**powers[i-1]
    max = 10**powers[i]

    min_txt = "0" if min == 0 else f"10*{powers[i-1]}"

    print(f'--- {min_txt} <= ... <= 10**{n} ---')

    for _ in range(nbtests_by_slice):
        while((x := randint(min, max)) in x_tested):
            continue

        x_tested.append(x)

        print(x)
        print(f'    -> {intname.nameof(x)}')

    print()
