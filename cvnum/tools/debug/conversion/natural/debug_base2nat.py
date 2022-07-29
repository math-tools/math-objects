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

myb2n = Base2Nat()
myn2b = Nat2Base()


# -------------- #
# -- LET'S GO -- #
# -------------- #

print(f"{myb2n.bnumerals2bnb(['A', '5'], 16) = }")
print(f"{myb2n.bdigits2bnb([10, 5], 16) = }")

exit()


for b in [
    2,
    # 8,
    # 10,
    16,
    36,
    37
]:
    print('---')
    print(f"                 {b = }")
    print(f"{myb2n.basedigitize(b) = }")

# exit()


print('---')
bnb = '30AF4'
b = 16

print(f'                    {bnb, b = }')
print(f'  {myb2n.bdigitsof(bnb, b) = }')
print(f'{myb2n.bnumeralsof(bnb, b) = }')

# exit()


print('---')
mydigits   = [3, 0, 10, 15, 4]
mynumerals = ['3', '0', 'A', 'F', '4']
b          = 16
nbbyhand   = (((3 *16 +0)*16 + 10)*16 + 15)*16 + 4

print(f'                       {b, mydigits = }')
print(f'    {myb2n.bdigits2nat(mydigits, b) = }')
print(f'{myb2n.bnumerals2nat(mynumerals, b) = }')
print(f'                          {nbbyhand = }')

# print('---')
# b = 40
# print(bdigits2nat([10, 39], b))
# print(bnumerals2nat(['0A', '13'], b))
# print(bnb2nat('0A.13', b))
# print(bnb2nat('0A13', b, sep = ""))

# exit()


print('---')

for (n, b) in [
    (1 + 2*5 + 3*5**2, 5),
    (4 + 5*7 + 6*7**2, 7),
    (8 + 9*11 + 10*11**2, 11),
    (30 + 31*36 + 35*36**2, 36),
    (4 + 36*37**2, 37),
    (37 + 38*40 + 39*40**2, 40),
]:
    print('---')

    if n != myb2n.bnb2nat(myn2b.nat2bnb(n, b), b):
        print(f"PB with {n = } and {b = }")
        print()
        print(f"                  {myn2b.nat2bnb(n, b) = }")
        print(f"{myb2n.bnb2nat(myn2b.nat2bnb(n, b), b) = }")
        exit(1)

    print(f"OK!   {n, b = }")
