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

from src.convert import *

print('---')
bnb = '30AF4'
b = 16
print(f'{bnb} = {basedigits(bnb, b)}')
print(f'{bnb} = {basenumerals(bnb, b)}')

for (n, b) in [
    (1 + 2*5 + 3*5**2, 5),
    (4 + 5*7 + 6*7**2, 7),
    (8 + 9*11 + 10*11**2, 11),
    (30 + 31*36 + 35*36**2, 36),
    (4 + 36*37**2, 37),
    (37 + 38*40 + 39*40**2, 40),
]:
    print('---')

    if n != bnb2int(int2bnb(n, b), b):
        print(f"PB with n = {n} and b = {b}")
        print()
        print(f"int2bnb(n, b)             = {int2bnb(n, b)}")
        print(f"bnb2int(int2bnb(n, b), b) = {bnb2int(int2bnb(n, b), b)}")
        exit(1)

    print(f"{n} OK!")

print('---')
bnb = '30AF4'
b = 16
print(bnb2int(bnb, b))
print(bnumerals2int(['3', '0', 'A', 'F', '4'], b))
print(bdigits2int([3, 0, 10, 15, 4], b))
print(bnumerals2int(['3', '0', 'A', 'F', '4'], b))

print('---')
b = 40
print(bdigits2int([10, 39], b))
print(bnumerals2int(['0A', '13'], b))
print(bnb2int('0A.13', b))
print(bnb2int('0A13', b, sep = ""))
