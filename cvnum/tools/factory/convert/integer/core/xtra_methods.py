#!/usr/bin/env python3

from cbdevtools import *


# ----------------- #
# -- MODULE USED -- #
# ----------------- #

for upfolder in [
    'convert',
    # 'tests',
]:
    _ = addfindsrc(
        file    = __file__,
        project = upfolder,
    )

from cvcore.protontype import *


# ------------------- #
# -- EXTRA METHODS -- #
# ------------------- #

def replace_int2nat(text):
    return text.replace('int', 'nat')

def replace_nat2int(text):
    return text.replace('nat', 'int')


SPECIFIC_CLASS_TO_IGNORE = {
    'Nat2Base' : ['numeralize'],
    'Base2Nat' : ['basedigitize'],
    'Base2Base': [],
}
SPECIFIC_CLASS_TO_IGNORE = {
    k: [re_compile(s) for s in v]
    for k, v in SPECIFIC_CLASS_TO_IGNORE.items()
}

PATTERNS_TO_IGNORE = [
    re_compile(s)
    for s in ['check.+']
]
PATTERNS_TO_IGNORE.append(PATTERN_UNDERSCORE)


def cls_automethods(intcls, natcls):
    _dircls = shortdir(
        natcls,
        toignore = PATTERNS_TO_IGNORE
                 + SPECIFIC_CLASS_TO_IGNORE[natcls.__name__]
    )

    dircls = []

    for n in _dircls:
        if not replace_nat2int(n) in dir(intcls):
            dircls.append(n)

    return dircls
