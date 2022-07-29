#!/usr/bin/env python3

from pprint import pprint

from cbdevtools     import *
from mistool.os_use import PPath

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = PPath(__file__).parent

SRC_DIR = THIS_DIR

while(SRC_DIR.name != "cvnum"):
    SRC_DIR = SRC_DIR.parent

THIS_FILE_REL_SRC_PATH = PPath(__file__) - SRC_DIR

SRC_DIR    = SRC_DIR / "src"


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'cvnum',
)

from src.convert.natural import Nat2Base, Base2Nat


# ----------- #
# -- TOOLS -- #
# ----------- #

OLD_NEW = {
    'bdig'   : "dig",
    'bnb2nat': "nat2bnb",
    'bnum'   : "num",
    'fromb'  : "from",
    'bnb'    : "nat",
}

def dircls(cls, remove = True):
    dircls_cleaned = set()

    for name in dir(cls):
        if (
            name[0] == '_'
            or
            name.startswith('check')
            or
            name in [
                'basedigitize',
                'numeralize',
            ]
        ):
            continue

        if remove:
            for old, new in OLD_NEW.items():
                name = name.replace(old, new)

        dircls_cleaned.add(name)

    return dircls_cleaned


# -------------------------------- #
# -- DIR OF NAT2BASE & BASE2NAT -- #
# -------------------------------- #

dircls_N2B = dircls(Nat2Base)
dircls_B2N = dircls(Base2Nat)

assert dircls_N2B == dircls_B2N, \
       (
         "\n\n"
        f"{dircls_N2B - dircls_B2N = }"
         "\n\n"
        f"{dircls_B2N - dircls_N2B = }"
         "\n\n"
        f"{dircls(Nat2Base, False) = }"
         "\n\n"
        f"{dircls(Base2Nat, False) = }"
       )

print('Great job !')
print()
print("dircls(Nat2Base, False) = ", end = "")
pprint(dircls(Nat2Base, False))
print()
print("dircls(Base2Nat, False) = ", end = "")
pprint(dircls(Base2Nat, False))
print()
print(f"Sizes: {len(dircls(Nat2Base, False))} & {len(dircls(Base2Nat, False))}")
