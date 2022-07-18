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

from src.tbox.var2nb import *

class fakeINT:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return str(self.n)


# bignb = "111_222_333 444_555_666";print(intify(bignb, tryconvert = True, toremove = ['']));exit()

for n in [
    123,
    -123,
    "60000",
    fakeINT(54321),
]:
    print()
    print('--- intnonneg ---')
    print(f"{n} with type = {type(n)}")

    print(intify(n))
    # print(intify(n, mini = 10))
    # print(intify(n, tryconvert = True))


for n in [
    "0007",
    8,
    fakeINT(54321),
]:
    print()
    print('--- intbase ---')
    print(f"{n} with type = {type(n)}")
    print(intify(n, tryconvert = True))
