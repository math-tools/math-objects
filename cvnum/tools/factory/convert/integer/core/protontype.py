#!/usr/bin/env python3

from collections import defaultdict
from inspect     import signature, _empty


# --------------- #
# -- TOOLS -- #
# --------------- #

def maxlen(strings):
    return max(len(s) for s in strings)



# --------------- #
# -- PROTOTYPE -- #
# --------------- #

def seeat(ref, useself = True):
    about = ":see: "

    if useself:
        about += 'self.'

    about += f"{ref}"

    return about

def prototype_oneparam(param, ref, useself = True):
    return f"{param} : " + seeat(ref, useself)


def build_see_params(about_params, refs):
# ! -- DEBUGGING -- ! #
    # print("--- build_see_params ---")
    # print(f"{about_params = }")
    # print(f"{refs         = }")
    # print("--- build_see_params ---")
# ! -- DEBUGGING -- ! #

    maxlen_param = maxlen(about_params)

    return [
        prototype_oneparam(
            param   = param + ' '*(maxlen_param - len(param)),
            ref     = refs[param][1],
            useself = refs[param][0]
        )
        for param in about_params
    ]


def build_return_ref(methodname):
    if methodname.endswith('of'):
        methodname = methodname[:-2]

    elif methodname.startswith("from"):
        methodname = methodname[4:]

    else:
        _, methodname = methodname.split('2')

    return methodname


# ------------ #
# -- PARAMS -- #
# ------------ #

def method_oneparam(param, about):
    text = f"{param}: {about['typing']}"

    if not about['default'] is None:
        text += f" = {about['default']}"

    text += ","

    return text

def build_method_params(about_params):
    maxlen_param = maxlen(about_params)

    return [
        method_oneparam(
            param = param + ' '*(maxlen_param - len(param)),
            about = about_params[param]
        )
        for param in about_params
    ]


# ------------ #
# -- TYPING -- #
# ------------ #

def cleantype(onetype):
    onetype = onetype.strip()

    for toremove in [
        "typing.",
        "<class '",
        "'>"
    ]:
        onetype = onetype.replace(toremove, "")

    return onetype
