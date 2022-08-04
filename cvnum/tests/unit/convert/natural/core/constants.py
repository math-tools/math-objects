#!/usr/bin/env python3

# ----------------------- #
# -- CONSTANTS & TOOLS -- #
# ----------------------- #

SOME_SEPS = list(",.:;") + ['']


OUTPUTS_NO_NB = [
    "digits",
    "numerals",
]

OUTPUTS_ALL = OUTPUTS_NO_NB + [
    "nb",
]


KINDS_CHGETHIS = {
    "digits"  : int,
    "numerals": str,
}

KINDS_ALL = list(KINDS_CHGETHIS)


BUILTINS_CONVERTERS = {
    2 : bin,
    8 : oct,
    16: hex,
}

BUILTINS_CONVERTERS_BASES = list(BUILTINS_CONVERTERS)
