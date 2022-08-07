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


KINDS_SIGNS = {
    "digits": {
        '-': -1,
        '+': 1,
    },
    "numerals": {
        '-': "-",
        '+': "",
    },
}


KINDS_CHGETHIS = {
    "digits"  : int,
    "numerals": str,
}

KINDS_ALL = list(KINDS_CHGETHIS)
