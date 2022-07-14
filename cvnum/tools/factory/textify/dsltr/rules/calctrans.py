#!/usr/bin/env python3

from string import digits

from .toolboxdsl import *


# ------------------------ #
# -- BASE CLASS FOR DSL -- #
# ------------------------ #

def withsinglespaces(text):
    while('  ' in text):
        text = text.replace('  ', ' ')

    return text


def expandbraces(rules):
# No pb found!
    return "".join([
        c
        if k == DSL_ACTION_VERBATIM else
        f'"{c} :if: d > 1"'
        for k, c in findgroups(
            rules,
            TAG_DELIM_BRACES,
            recursive = False
        )
    ])


def calctrans(rules):
# No double spaces needed.
    rules = withsinglespaces(rules)

# Use of {...}
    initrules = rules
    rules     = expandbraces(rules)

# We have to build "tokens".
    tokens = []

# Quotes take precedence over brackets.
    try:
        grps_quotes = findquotes(rules)

    except Exception as e:
        raise Exception(f"{e} See << {initrules} >>.")

    for kind, onerule in grps_quotes:
        insidequotes = bool(kind != DSL_ACTION_VERBATIM)
        subtokens    = []

# We have to manage hooks.
        try:
            grps_groups = findgroups(
                onerule,
                TAG_DELIM_HOOKS,
                recursive = False
            )

        except Exception as e:
            raise Exception(f"{e} See << {initrules} >>.")

        for subkind, subonerule in grps_groups:
            subtokens += tokenize(
                kind            = subkind,
                onerule         = subonerule,
                ifelseforbidden = not insidequotes
            )

        if insidequotes:
            subtokens = [[TAG_CONTENT_QUOTES, subtokens]]

        tokens += subtokens

# We build the final normalized form.
    actions = prenormalize(tokens)
    actions = normalize(actions)

    return actions


def tokenize(
    kind,
    onerule,
    ifelseforbidden
):
# One group.
    if kind == TAG_CONTENT_GROUP:
        return [[
            kind,
            tokenize(
                DSL_ACTION_NAME_IT,
                onerule,
                ifelseforbidden = False
            )
        ]]

# No group, no quote.
#
# Alternative used?
    if TAG_IF in onerule:
        if ifelseforbidden:
            raise Exception(
                f"illegal use of << {TAG_IF} >> , see << {onerule} >>"
            )

        win_rule, _, test = onerule.partition(TAG_IF)

        if TAG_ELSE in test:
            test, _, loose_rule = test.partition(TAG_ELSE)

        else:
            loose_rule = ''

        return [[
            DSL_ACTION_IF_ELSE,
            [
                test.strip(),
                win_rule.strip(),
                loose_rule.strip()
            ]
        ]]

# An ELSE alone.
    if TAG_ELSE in onerule:
        raise Exception(
            f"one << {TAG_ELSE} >> used without an << {TAG_IF} >> , "
            f"see << {onerule} >>"
        )

# Nothing special found.
    return [[kind, onerule]]


def prenormalize(tokens):
    actions = []

    for kind, datas in tokens:
# Group (just validate its content).
        if kind == TAG_CONTENT_GROUP:
            datas = datas[0]

            if datas[0] == DSL_ACTION_IF_ELSE:
                winrules = (
                    [[DSL_ACTION_NAME_IT, datas[1][1]]]
                    if datas[1][1] else
                    []
                )

                looserules = (
                    [[DSL_ACTION_NAME_IT, datas[1][2]]]
                    if datas[1][2] else
                    []
                )

                datas = [
                    datas[0],
                    datas[1][0],
                    winrules,
                    looserules,
                ]

            actions.append(datas)

# Quote (no more than one if-else).
        elif kind == TAG_CONTENT_QUOTES:
            quote_actions = []

# Build with optimism.
            ifelseused = False

            for subkind, subdatas in datas:
                if subkind == DSL_ACTION_IF_ELSE:
                    if ifelseused:
                        raise Exception(
                            f"too much << {TAG_IF} >> used"
                        )

                    ifelseused = True

                    # We have to take care of string only win/loose rules
                    # coming from cases like ``a :if: b :else: c``.
                    for i in range(1, 3):
                        if subdatas[i]:
                            if isinstance(subdatas[i], str):
                                subdatas[i] = [DSL_ACTION_VERBATIM, subdatas[i]]

                    subdatas[1] = (
                        quote_actions + [subdatas[1]]
                        if subdatas[1] else
                        quote_actions
                    )
                    subdatas[2] = [subdatas[2]] if subdatas[2] else []

                    quote_actions = [[subkind] + subdatas[0:]]

                else:
                    # We use ``normalize`` with a list of one single action.
                    normalized_about = prenormalize([(subkind, subdatas)])[0]

                    if ifelseused:
                        quote_actions[-1][3].append(normalized_about)

                    else:
                        quote_actions.append(normalized_about)

            actions += quote_actions

# Verbatim content.
        else:
            actions.append((kind, datas))

    return actions


def normalize(actions):
    shortactions = []

    for kind, *about in actions:
# IF-ELSE
        if kind == DSL_ACTION_IF_ELSE:
            test, winrules, looserules = about

            shortactions.append((
                kind,
                [
                    _RTU[TAG_CONTENT_TO_TEST](test),
                    normalize(winrules),
                    normalize(looserules),
                ]
            ))

# Something else.
        else:
            shortactions.append((
                kind,
                _RTU[kind](about[0])
            ))

    return shortactions


def rtu_name_it(rule):
    actions = []

    for subkind, onesubrule in findgroups(
        rule,
        TAG_DELIM_BRACKETS,
        recursive = False
    ):
# Verbatim
        if subkind == DSL_ACTION_VERBATIM:
            i    = 0
            imax = len(onesubrule)

            str_lastint = ""

            while(c := onesubrule[i]):
# One digit.
                if c in digits:
                    str_lastint += c

# Spaces are forbidden.
                elif c == " ":
                    raise Exception(
                        f"spaces are not allowed in << {rule} >>"
                    )

# One letter ?
                elif not c in DSL_SPECIAL_VARS:
                    raise Exception(
                        f"illegal variable << {c} >> in << {rule} >>"
                    )

                else:
                    if str_lastint:
                        actions.append((
                            DSL_ACTION_VERBATIM,
                            str_lastint
                        ))

                        str_lastint  = ""

                    actions.append((
                        DSL_ACTION_SPEVAR,
                        c
                    ))

# Ley's continue...
                i += 1

# ... or not!
                if i == imax:
                    break

# One last integer?
            if str_lastint:
                actions.append((
                    DSL_ACTION_VERBATIM,
                    str_lastint
                ))

# Braces
        else:
            lastkind, lastcontent = actions[-1]

            if lastkind != DSL_ACTION_SPEVAR:
                raise Exception(
                    f"brackets not following a special variable in << {rule} >>"
                )

            else:
                if onesubrule.isdigit():
                    istart = iend = int(onesubrule)

                else:
                    istart, iend = startend_fromto(onesubrule)

                actions.pop(-1)
                actions.append((
                    DSL_SPECIAL_VARS[lastcontent],
                    (istart, iend)
                ))

# The job has been done.
    return actions


def split_onecompope(text):
    i_ope     = len(text)
    ope_found = None

    for compope in DSL_ALL_COMPOPES:
        if compope in text:
            i = text.index(compope)

            if i < i_ope:
                i_ope      = i
                ope_found = compope

    if ope_found is None:
        return None

    left, _, right = text.partition(ope_found)

    return left, ope_found, right


def rtu_test(rule):
# One ope?
    parts = split_onecompope(rule)

    if parts is None:
        raise Exception(
            f"no comparison operator found in << {rule} >>"
        )

    left, compope, right = parts

    left = rtu_name_it(left.strip())

# Two ope ?
    parts = split_onecompope(right)

    if parts is None:
        right = rtu_name_it(right.strip())

        return [[compope], [left, right]]


    between, compope_bis, right = parts


# Three ope?
    for c in DSL_ALL_COMPOPES:
        if c in right:
            raise Exception(
                f"too much comparison operators found in << {rule} >>"
            )

# Legal double comparison?
    if (
        compope in DSL_ILLEGAL_ALL_EQUALS
        or
        compope_bis in DSL_ILLEGAL_ALL_EQUALS
    ):
        raise Exception(
            f"the operators << {DSL_COMPOPE_EQ} >> and "
            f"<< {DSL_COMPOPE_NOT_EQ} >> must be alone, "
            f"see << {rule} >>"
        )

    if [compope, compope_bis] in DSL_ILLEGAL_COUPLES_OPE:
        raise Exception(
            f'the use of " ... {compope} ... {compope_bis} ... " '
            f"is illegal, see << {rule} >>"
        )

# No pb found.
    between = rtu_name_it(between.strip())
    right   = rtu_name_it(right.strip())

    return [
        (compope, compope_bis),
        (left, between, right)
    ]


def rtu_verbatim(rule):
# Nothing is forbidden!
    return rule


_RTU = {
    TAG_CONTENT_TO_TEST: rtu_test,
    DSL_ACTION_VERBATIM: rtu_verbatim,
    DSL_ACTION_NAME_IT : rtu_name_it,
}
