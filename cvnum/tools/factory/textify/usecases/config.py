#!/usr/bin/env python3

from dsltr    import *


TAGS_FOR_IGNORED_TESTS = [
    DSL_SPECS_IGNORE_GROUP,
    DSL_SPECS_IGNORE_SMALL,
]

KINDS_FOR_TESTS = [
    "small",
    "group",
    "verybig",
    "sign",
]


EMPTY_PATH   = '.'
SPECIAL_FILE = "special.txt"
