#!/usr/bin/env python3

from cbdevtools import *


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

from src.convert.natural import (
    Nat2Base,
    Base2Nat,
    Base2Base as NatBase2Base
)

from src.convert.integer import (
    Int2Base,
    Base2Int,
    Base2Base
)


# ------------------------ #
# -- SYMTREY OF THE API -- #
# ------------------------ #

PATTERNS_TO_IGNORE = [
    re_compile(s)
    for s in [
        'check.+',
        'intsign.*',
        'strsign.*',
    ]
]
PATTERNS_TO_IGNORE.append(PATTERN_UNDERSCORE)

def shortdircls(cls, toignore):
    dircls_cleaned = set()

    for name in shortdir(
        cls,
        PATTERNS_TO_IGNORE + [
            re_compile(s)
            for s in toignore
        ]
    ):
        for old, new in [
            ('nat2', 'int2'),
            ('2nat', '2int'),
        ]:
            name = name.replace(old, new)

        dircls_cleaned.add(name)

    return dircls_cleaned


def test_sym_apis_INT_vs_NAT():
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
        shortdirs[onecls] = shortdircls(
            cls      = onecls,
            toignore = methods_ignored.get(onecls, []),
        )

# ! -- DEBUGGING -- ! #
    # from pprint import pprint
    # pprint(shortdirs)
    # exit()
# ! -- DEBUGGING -- ! #

    for natcls, intcls in nat2int_cls.items():
        assert shortdirs[natcls] == shortdirs[intcls], \
               (
                 "\n"
                f"Unequal public APIs of {natcls.__name__} and {intcls.__name__}."
                 "\n\n"
                f"{shortdirs[natcls] - shortdirs[intcls] = }"
                 "\n\n"
                f"{shortdirs[intcls] - shortdirs[natcls] = }"
                 "\n"
               )
