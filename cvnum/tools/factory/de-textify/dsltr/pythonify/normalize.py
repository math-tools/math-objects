#!/usr/bin/env python3

from collections import defaultdict

from numpy import isin
from ..rules import *

# ! -- DEBUGGING -- ! #
from pprint import pprint
# ! -- DEBUGGING -- ! #


# -------------------------------- #
# --  NORMALIZE THE TRANS DICT  -- #
# -------------------------------- #

def shorten_nameit_verb(
    onerule,
    asitdict,
    strictmode = False
):
    newrule       = []
    asitkeysfound = []

    for kind, params in onerule:
        if (
            kind == DSL_ACTION_NAME_IT
            and
            len(params) == 1
            and
            params[0][0] == DSL_ACTION_VERBATIM
            and
            params[0][1] in asitdict
        ):
            oneasitkey = params[0][1]

            if strictmode:
                if oneasitkey in asitkeysfound:
                    raise Exception(
                         "one circular definition with asit keys "
                        f"for small integers, see << {oneasitkey} >>"
                    )

            newrule += list(asitdict[oneasitkey])

        else:
            newrule.append((kind, params))

    return shorten_verb_n_verb(newrule)


def shorten_verb_n_verb(onerule):
    newrule  = []
    prevverb = False

    for kind, params in onerule:
        if kind == DSL_ACTION_VERBATIM:
            if prevverb:
                newtxt      = newrule[-1][1] + params
                newrule[-1] = (kind, newtxt)
                continue

            prevverb = True

        else:
            prevverb = False

        newrule.append((kind, params))

    return newrule


def shorten(specs):
# The ASIT dict.
    asitdict = specs[DSL_SPECS_SMALL][DSL_ACTION_ASIT]

    for strnb, onerule in asitdict.items():
        asitdict[strnb] = shorten_nameit_verb(
            onerule,
            asitdict,
            strictmode = True
        )

# The MATCHING dict.
    matchingdict = specs[DSL_SPECS_SMALL][DSL_ACTION_MATCHING]

    for length, rules in matchingdict.items():
        newrules = OrderedDict()

        for onepattern, onerule in rules.items():
            newrules[onepattern] = shorten_nameit_verb(
                onerule,
                asitdict
            )

        matchingdict[length] = newrules

    specs[DSL_SPECS_SMALL][DSL_ACTION_MATCHING] = matchingdict

    return specs


def simplify(onevar, keepordereddict = False):
# Nothing to do.
    if (
        isinstance(onevar, (str, int, bool))
        or
        onevar is None
    ):
        return onevar

# One list or a tuple.
    if isinstance(onevar, (list, tuple)):
        return tuple(
            simplify(
                onevar          = v,
                keepordereddict = keepordereddict
            )
            for v in onevar
        )

# Ordered dict are sometimes expected.
    if keepordereddict and isinstance(onevar, OrderedDict):
        newvar = OrderedDict()

        for k, v in onevar.items():
            newvar[k] = simplify(
                onevar          = v,
                keepordereddict = keepordereddict
            )

        return newvar

# One dict.
    if isinstance(onevar, dict):
        return {
            k: simplify(
                onevar          = v,
                keepordereddict = (
                    keepordereddict
                    or
                    k == DSL_ACTION_MATCHING
                )
            )
            for k, v in onevar.items()
        }

# Something that should not be here!
    raise Exception(
        f"BUG: unsupported simplification of the type << {type(onevar)} >>"
    )


def normalize_rules(alltrans):
# Let's take care of small rules.
    for lang, specs in alltrans.items():
        newspecs_small = {
            DSL_ACTION_ASIT    : {},
            DSL_ACTION_MATCHING: defaultdict(OrderedDict),
        }

# We copy the rules wuanted from the initial lang.
        for (kind, pattern), rule in specs[DSL_SPECS_SMALL].items():
# No matching.
            if kind == DSL_ACTION_ASIT:
                newspecs_small[DSL_ACTION_ASIT][pattern] = rule
                continue

# Matching.
            length = 0

            for partkind, partrule in findgroups(
                pattern,
                TAG_DELIM_HOOKS,
                recursive = False
            ):
                if partkind == TAG_CONTENT_GROUP:
                    length += 1

                else:
                    length += len(partrule)

            newspecs_small[DSL_ACTION_MATCHING][length][pattern] = rule

# Small rules are ok now.
        specs[DSL_SPECS_SMALL] = newspecs_small

        for formatter in [
            shorten,
            simplify,
        ]:
            specs = formatter(specs)

        alltrans[lang] = specs

# Job hase been done.
    return alltrans
