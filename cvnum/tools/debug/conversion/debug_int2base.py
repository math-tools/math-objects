#!/usr/bin/env python3

from cbdevtools import *


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

from src.convert.integer import *

print('---')
x = 123456789
print(f'{x} = {intdigits(x)}')
print(f'{x} = {intnumerals(x)}')

for (n, b) in [
    (1 + 2*5 + 3*5**2, 5),
    (4 + 5*7 + 6*7**2, 7),
    (8 + 9*11 + 10*11**2, 11),
    (30 + 31*36 + 35*36**2, 36),
    (4 + 36*37**2, 37),
    (37 + 38*40 + 39*40**2, 40),
    (0, 4),
    (1, 1297),
]:
    print('---')
    print(f"{n} = {int2bdigits(n, b)}_{b}")
    tab = " "*len(f"{n} ")
    print(f"{tab}= {int2bnumerals(n, b)}")
    print(f"{tab}= {int2bnb(n, b)}")

print('---')
n = 1 + 39*40 + 10*40**5
b = 40
print(int2bdigits(n, b))
print(int2bnumerals(n, b))
print(repr(int2bnb(n, b)))

print('---')
n = 1 + 39*3000 + 10*3000**7
b = 3000
print(int2bnumerals(n, b))
print(repr(int2bnb(n, b, "")))
