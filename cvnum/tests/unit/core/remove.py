#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from random import choice, randint


# ------------ #
# -- REMOVE -- #
# ------------ #

def build_removable(nb, toremove, atleastone = ""):
    nb          = str(nb)
    nb_polluted = ''

    for c in nb:
        if (
            nb_polluted
            and
            not nb_polluted[-1] in toremove
            and
            randint(0, 10) <= 7
        ):
            nb_polluted += choice(toremove)

        nb_polluted += c

    if(
        atleastone
        and
        not atleastone in nb_polluted
    ):
        nb_polluted = nb_polluted[:1] + atleastone + nb_polluted[1:]

    return nb_polluted
