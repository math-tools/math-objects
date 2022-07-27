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

from src.convert.natural import *

myn2b = Nat2Base()


# -------------- #
# -- LET'S GO -- #
# -------------- #

print('---')
print(f"{myn2b.digits2bnb([1, 5, 3], 16) = }")
assert(153 == int(myn2b.digits2bnb([1, 5, 3], 16), 16))

exit()


print('---')
mydigits   = [3, 0, 5, 9, 4]
mynumerals = [str(d) for d in mydigits]

print(f'                      {mydigits = }')
print(f'    {myn2b.digits2nat(mydigits) = }')
print(f'{myn2b.numerals2nat(mynumerals) = }')

# exit()


for (n, b) in [
    (1 + 2*5 + 3*5**2,
     5),
    (4 + 5*7 + 6*7**2,
     7),
    (8 + 9*11 + 10*11**2,
     11),
    (30 + 31*36 + 35*36**2,
     36),
    (4 + 36*37**2,
     37),
    (37 + 38*40 + 39*40**2,
     40),
    (0,
     4),
    (1,
     1297),
    (1 + 39*40 + 10*40**5,
     40),
    (1 + 39*3000 + 10*3000**7,
     3000),
]:
    print('---')
    print(f"                     {n, b = }")
    print(f"  {myn2b.nat2bdigits(n, b) = }")
    print(f"{myn2b.nat2bnumerals(n, b) = }")
    print(f"      {myn2b.nat2bnb(n, b) = }")
