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

from src.toolbox import *

class fakeINT:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return str(self.n)

for n in [
    50000,
    "60000",
    fakeINT(54321),
]:
    print()
    print('--- intnonneg ---')
    print(f"{n} with type = {type(n)}")
    print(intnonneg(n, tryconvert = True))


for n in [
    "0007",
    8,
    fakeINT(54321),
]:
    print()
    print('--- intbase ---')
    print(f"{n} with type = {type(n)}")
    print(intbase(n, tryconvert = True))
