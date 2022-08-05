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
# -- TO DEBUG -- #
# -------------- #

from src.convert.integer import *

myi2b = Int2Base()


# -------------- #
# -- LET'S GO -- #
# -------------- #

print(f"{myi2b.int2bnb(-18, base = 8) = }")

print(f"{myi2b.int2bnb(8, nb = 18)    = }")

print(f"{myi2b.int2bnb(18, 8)         = }")

# exit()


for x in [
    123,
    -345,
]:
    print()

    print(f"d := numeralsof({x}) =", d := myi2b.numeralsof(x))
    print(f"{myi2b.fromnumerals(d) = }")

    print()

    print(f"d := digitsof({x}) =", d := myi2b.digitsof(x))
    print(f"{myi2b.fromdigits(d) = }")
    print(f"{myi2b.digits2bdigits(d, 100) = }")

exit()


for (n, b) in [
    (1 + 2*5 + 3*5**2, 5),
    # ("+86", 5), # BUG
    # ("-86", 5), # BUG

    # (4 + 5*7 + 6*7**2, 7),
    # (8 + 9*11 + 10*11**2, 11),
    # (30 + 31*36 + 35*36**2, 36),
    # (4 + 36*37**2, 37),
    # (37 + 38*40 + 39*40**2, 40),
    # (0, 4),
    # (1, 1297),
]:
    print('---')
    print(f"                        {n = }")
    print(f"  {myi2b.int2bdigits(n, b) = }")
    print(f"{myi2b.int2bnumerals(n, b) = }")
    print(f"      {myi2b.int2bnb(n, b) = }")

exit()
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
