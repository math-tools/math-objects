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
    nb_polluted = ""

    for c in nb:
        if (
            nb_polluted
            and
            not nb_polluted[-1] in toremove
            and
            randint(0, 10) <= 6
        ):
            nb_polluted += choice(toremove)

        nb_polluted += c

    while(nb[0] in toremove):
        nb = nb[1:]

    while(nb[-1] in toremove):
        nb = nb[:-1]

    if(
        atleastone
        and
        not atleastone in nb_polluted
    ):
        nb_polluted = nb_polluted[0] + atleastone + nb_polluted[1:]

    return nb_polluted


# --------------- #
# -- HAND TEST -- #
# --------------- #

if __name__ == '__main__':
    print(
        build_removable(
            # nb         = "123456",
            nb         = "76",
            toremove   = [' ', '_'],
            atleastone = "_",
        )
    )
