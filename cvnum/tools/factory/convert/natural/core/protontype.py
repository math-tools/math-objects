#!/usr/bin/env python3

from collections import defaultdict
from inspect     import signature, _empty


# --------------- #
# -- PROTOTYPE -- #
# --------------- #

def seeat(ref, useself = True):
    about = ":see: "

    if useself:
        about += 'self.'

    about += f"{ref}"

    return about

def prototype_param(param, ref, useself = True):
    return f"{param} : " + seeat(ref, useself)


# ------------ #
# -- TYPING -- #
# ------------ #

def cleantype(onetype):
    for toremove in [
        "typing.",
        "<class '",
        "'>"
    ]:
        onetype = onetype.replace(toremove, "")

    return onetype
