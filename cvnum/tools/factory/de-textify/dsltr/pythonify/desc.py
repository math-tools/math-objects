#!/usr/bin/env python3

from ..rules import *


# ! -- DEBUGGING -- ! #
from pprint import pprint
# ! -- DEBUGGING -- ! #


# -------------------------------- #
# --  NORMALIZE THE TRANS DICT  -- #
# -------------------------------- #

def extracts_desc(alltrans):
    alldescs = {}

    for lang, specs in alltrans.items():
        if not 'desc' in specs[DSL_SPECS_THIS]:
            raise Exception(
                 'missing key "desc" in the "this block". '
                f'See the translation "{lang}".'
            )

        alldescs[lang]= specs[DSL_SPECS_THIS]['desc']['value']

    return alldescs
