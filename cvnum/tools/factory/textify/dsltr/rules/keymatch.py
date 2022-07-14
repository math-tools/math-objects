#!/usr/bin/env python3

import re

from .toolboxdsl import *


# -------------- #
# -- MATCHING -- #
# -------------- #

def singlepatt(pattern):
    isregex    = TAG_WILD_CARD in pattern
    patternnew = ""

    for c in pattern:
        if c == " ":
            continue

        if c.isdigit():
            patternnew += c

        elif c == TAG_WILD_CARD:
            patternnew += '.'

        else:
            raise Exception(
                f"illegal character << {c} >> found in << {pattern} >>"
            )

    return isregex, patternnew


def regexify(
    pattern,
    canusealter = False
):
# Alternatives forbidden.
    if not canusealter:
        return singlepatt(pattern)

# Alternatives.
    isregex    = False
    alterparts = []

    if TAG_PIPE in pattern:
        isregex = True

    for onepart in pattern.split(TAG_PIPE):
        onepart = onepart.strip()

# Shortcut for alternatives.
        if TAG_FROM_TO in onepart:
            isregex = True

            istart, iend = startend_fromto(onepart)

            onepart = TAG_PIPE.join([
                str(i)
                for i in range(istart, iend + 1)
            ])

# Wildcard or just digits.
        else:
            _isregex, onepart = singlepatt(onepart)
            isregex           = isregex or _isregex

        alterparts.append(onepart)

# Some alternatives used, or not.
    pattern = TAG_PIPE.join(alterparts)

    return isregex, pattern


def matchpatt(rules):
# Good groups?
    groups = findgroups(
        rules,
        TAG_DELIM_HOOKS,
        recursive = False
    )

# Let's analyze!
    ismatching = False
    pattrule   = []

    for kind, content in groups:
        if kind == DSL_ACTION_VERBATIM:
            isregex, rule = regexify(content)

        else:
            isregex, rule = regexify(
                content,
                canusealter = True
            )

            if isregex:
                rule = f"[{rule}]"

        ismatching = ismatching or isregex
        pattrule.append(rule)

    pattrule = "".join(pattrule)

# Let's try to compile the regex.
    if ismatching:
        try:
            re.compile(pattrule)

        except Exception as e:
            raise Exception(
                f"BUG: an illegal pattern << {pattrule} >> "
                 "has been build by the module keymatch."
            )

# No technical problem found.
    return ismatching, pattrule
