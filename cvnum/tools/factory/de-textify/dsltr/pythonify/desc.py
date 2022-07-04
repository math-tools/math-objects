#!/usr/bin/env python3

from ..rules import *


# ! -- DEBUGGING -- ! #
from pprint import pprint
# ! -- DEBUGGING -- ! #


# -------------------------------- #
# --  NORMALIZE THE TRANS DICT  -- #
# -------------------------------- #

def extracts_desc(alltrans):
    return {
        lang: specs[DSL_SPECS_THIS]['desc']['value']
        for lang, specs in alltrans.items()
    }
