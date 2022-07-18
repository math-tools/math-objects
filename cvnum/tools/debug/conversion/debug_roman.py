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

for i in [1, 4, 49, 51, 4428, 4500, 4999]:
    print('---')
    print(f"{i}  =  {int2roman(i)}")
    print(f"{i} =?= {roman2int(int2roman(i))}")

romlongest = ""

for i in range(1, 5000):
    rom = int2roman(i)

    if len(romlongest) < len(rom):
        romlongest = rom

print('---')
print(f"Longest roman : {romlongest} = {roman2int(romlongest)}")

print('---')
print(isroman("XXIII"))
print(isroman("XXXXXIII"))
