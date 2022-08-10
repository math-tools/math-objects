#!/usr/bin/env python3

LOCAL_TEST = False
# LOCAL_TEST = True


from random import randint


if LOCAL_TEST:
    from cbdevtools import *


# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end = "")
# ! -- DEBUGGING -- ! #


# ------------- #
# -- CHOICES -- #
# ------------- #

STEP_BY_STEP = True
STEP_BY_STEP = False

USE_RAND = True
USE_RAND = False

RAND_POWERS      = [2, 3, 6, 9, 12, 15, 27]
NBTESTS_BY_SLICE = 1

# RAND_POWERS      = [2, 3, 4, 5]
# NBTESTS_BY_SLICE = 3

lang = "de_DE"
lang = "en_GB"    # TESTS OK
lang = "en_US"    # TESTS OK
# lang = "es_ES"
# lang = "fr_FR"    # TESTS OK
# lang = "fr_BE"    # TESTS OK
# lang = "fr_FR_chuquet_1"
# lang = "fr_FR_chuquet_2"
# lang = "fr_FR_rowlet"
# lang = "fr_FR_tiret"
# lang = "it_IT"

FIXED_INTS = [
    "100", # Pour extend
    "-63_005",
    # 0,
    # 1,
    # 11,
    # 111,
    # 2111,
    # "22_111",
    # "222_111",
    # "3_222_111",
    # "33_222_111",
    # "333_222_111",
    # "4_333_222_111",
    # "44_333_222_111",
    # "444_333_222_111",
    # "5_444_333_222_111",
    # "55_444_333_222_111",
    # "5_000_000_000_001",
    # "-   321",
    # "200",
    # "200*10**3",
    # "200*10**6",
    # "200*10**9",
    # "200*10**12",
    # "200*10**15",
    # "200*10**18",
    # "200*10**21",
    # "200*10**24",
    # "200*10**27",
    # "200*10**27 + 200*10**18",
    # "200*10**30",
    # "200*10**30 + 200*10**21",
    # "200*10**30 + 200*10**15",
    # "123*10**27 + 123*10**18",
    # 1,
    # 22,
    # 4444,
    # "55_555",
    # 987,
    # 999,
    # - 435,
    # 506,
    # "4**3",
    # "444_333222111",
    # "555444_333222111",
    # "444_333000111",
    # "- 23_456789012",
    # "- 999_000000000_000000000_000000000",
    # "- 999_000000000_666555444_333222111",
    # "10**9",
    # "2*10**18",
    "3*10**36 + 10**18",
    # "4*10**36",
    # "123_456_789_012_345_678_901_234_567_890",
]


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

if LOCAL_TEST:
    MODULE_DIR = addfindsrc(
        file    = __file__,
        project = 'cvnum',
    )


# ----------- #
# -- TOOLS -- #
# ----------- #

def testandprint(nameof, x):
    print('---')
    print()

    x_eval = eval(str(x))

    if (
        isinstance(x, int)
        or
        x \
            .replace('_', '') \
            .replace(' ', '') \
            .isdigit()
    ):
        print(f"{x_eval:_}")

    else:
        print(f"  {x}")
        print(f"= {x_eval:_}")

    x_eval = str(x_eval)

    print(f'  --> {nameof(x_eval)}')
    print()


# -------------- #
# -- LET'S GO -- #
# -------------- #

if LOCAL_TEST:
    from src.textify import *

else:
    from cvnum import *


nameof = IntName(lang).nameof

# nameof(666);exit()

if not USE_RAND:
    for x in FIXED_INTS:
        testandprint(nameof, x)

        if STEP_BY_STEP:
            input("Next one?")

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

        for _ in range(NBTESTS_BY_SLICE):
            while((x := randint(min, max)) in x_tested):
                continue

            x_tested.append(x)

            testandprint(nameof, x)

        if STEP_BY_STEP:
            input("Next one?")

    print('---')
