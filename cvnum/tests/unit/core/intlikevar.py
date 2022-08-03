#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from random import random, choice


# ------------------ #
# -- INT LIKE VAR -- #
# ------------------ #

SOME_SEPS = ".,;"

class FakeINT:
    def __init__(self, n, s = ''):
        self.n = n
        self.s = s

    def __str__(self):
        str_int        = str(self.n)
        rand_polluated = ''

        for i, c in enumerate(str_int):
            if(
                i != 0
                and
                random() < .4
            ):
                rand_polluated += self.s

            rand_polluated += c

        return rand_polluated
