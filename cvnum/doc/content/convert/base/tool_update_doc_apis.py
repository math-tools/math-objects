#!/usr/bin/env python3

from cbdevtools         import *
from mistool.os_use     import PPath
from mistool.string_use import between

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = PPath(__file__).parent

DOC_DIR = THIS_DIR


# ------------------------------------------ #
# -- MODULE TESTED IMPORTED FROM SOURCES! -- #
# ------------------------------------------ #

for upfolder in [
    'cvnum',
    # 'tests',
]:
    _ = addfindsrc(
        file    = __file__,
        project = upfolder,
    )

# from src.convert.natural.natconv import NatConv
from src.convert.natural import (
    Nat2Base,
    Base2Nat,
    Base2Base as NatBase2Base
)

# from src.convert.integer.intconv import IntConv
from src.convert.integer import (
    Int2Base,
    Base2Int,
    Base2Base
)


# ----------- #
# -- TOOLS -- #
# ----------- #

def shortdircls(cls, toignore):
    dircls_cleaned = set()

    for name in dir(cls):
        if not(
            name[0] == '_'
            or
            any(
                name.startswith(ignorestart)
                for ignorestart in [
                    'check',
                    'intsign',
                    'strsign',
                ]
            )
            or
            name in toignore
        ):
            for old, new in [
                ('nat2', 'int2'),
                ('2nat', '2int'),
            ]:
                name = name.replace(old, new)

            dircls_cleaned.add(name)

    return dircls_cleaned


def build_dircls():
    nat2int_cls = {
        Nat2Base    : Int2Base,
        Base2Nat    : Base2Int,
        NatBase2Base: Base2Base,
    }

    methods_ignored = {
        Nat2Base    : ['numeralize'],
        Base2Nat    : ['basedigitize'],
    }

    shortdirs = {}

    for onecls in list(nat2int_cls.keys()) + list(nat2int_cls.values()):
        onedircls = shortdircls(
            cls      = onecls,
            toignore = methods_ignored.get(onecls, []),
        )

        onedircls = list(onedircls)
        onedircls.sort()

        shortdirs[onecls] = onedircls

    return shortdirs


# ---------------------- #
# -- DOC. OF THE APIS -- #
# ---------------------- #

print(f"   * Updating the doc. of the APIs of convert.natural and convert.integer.")

shortdirs = build_dircls()

# ! -- DEBUGGING -- ! #
# from pprint import pprint
# pprint(shortdirs)
# exit()
# ! -- DEBUGGING -- ! #

for cls, methods in shortdirs.items():
    docfile = cls.__name__.lower()
    docdir  = cls.__module__.split('.')[-2].lower()

    docfile = DOC_DIR / docdir / f"{docfile}.txt"


    with docfile.open(
        encoding = "utf-8",
        mode     = "r",
    ) as f:
        doc = f.read()

    before, _, after = between(
        text     = doc,
        keepseps = True,
        seps     = [
            '// -- ALL METHODS "AUTO" - START -- //',
            '// -- ALL METHODS "AUTO" - END -- //'
        ],
    )

    methods = ('\n' + ' '*4).join(f"1) ``{n}``" for n in methods)
    doc = f"""{before}

    {methods}

{after}"""


# ! -- DEBUGGING -- ! #
    # print(doc)
    # exit()
# ! -- DEBUGGING -- ! #


    with docfile.open(
        encoding = "utf-8",
        mode     = "w",
    ) as f:
        f.write(doc)
