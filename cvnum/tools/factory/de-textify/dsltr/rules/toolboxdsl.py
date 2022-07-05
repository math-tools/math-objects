#!/usr/bin/env python3

# --------------- #
# -- CONSTANTS -- #
# --------------- #

TAG_DELIM_BRACKETS = ("(", ")")
TAG_DELIM_BRACES   = ("{", "}")
TAG_DELIM_HOOKS    = ("[", "]")
TAG_DOUBLE_QUOTE   = '"'

TAG_SHORTCUT_FOR_D_R = ">"

TAG_PIPE      = "|"
TAG_FROM_TO   = ".."
TAG_WILD_CARD = "*"

TAG_IF   = ":if:"
TAG_ELSE = ":else:"


DSL_ACTION_ASIT     = "asit"
DSL_ACTION_MATCHING = "matching"


TAG_CONTENT_QUOTES = "quotes"
TAG_CONTENT_GROUP  = "group"

DSL_ACTION_NAME_IT           = "name-it"
DSL_ACTION_NAME_IT_GROUP     = "name-it-group"
DSL_ACTION_VERBATIM          = "verbatim"
DSL_ACTION_EXTRACT_NUMBER_OF = "d(m..n)"
DSL_ACTION_EXTRACT_REMAIN    = "r(m..n)"

DSL_ACTION_SPEVAR    = "special-var"
DSL_SPEVAR_NUMBER_OF = "d"
DSL_SPEVAR_REMAINING = "r"
DSL_SPECIAL_VARS     = {
    DSL_SPEVAR_NUMBER_OF: DSL_ACTION_EXTRACT_NUMBER_OF,
    DSL_SPEVAR_REMAINING: DSL_ACTION_EXTRACT_REMAIN,
}

DSL_ACTION_IF_ELSE  = "if-else"
TAG_CONTENT_TO_TEST = "to-test"

DSL_COMPOPE_EQ         = "="
DSL_COMPOPE_NOT_EQ     = "!="
DSL_COMPOPE_GREATER    = ">"
DSL_COMPOPE_GREATER_EQ = ">="
DSL_COMPOPE_LOWER      = "<"
DSL_COMPOPE_LOWER_EQ   = "<="

DSL_ILLEGAL_ALL_EQUALS = [
    DSL_COMPOPE_EQ,
    DSL_COMPOPE_NOT_EQ,
]

DSL_ILLEGAL_COUPLES_OPE = [
    [a, b]
    for a in [
        DSL_COMPOPE_GREATER,
        DSL_COMPOPE_GREATER_EQ
    ]
    for b in [
        DSL_COMPOPE_LOWER,
        DSL_COMPOPE_LOWER_EQ
    ]
]

DSL_ILLEGAL_COUPLES_OPE += [
    [b, a]
    for [a, b] in DSL_ILLEGAL_COUPLES_OPE
]

DSL_ALL_COMPOPES = [
    DSL_COMPOPE_EQ,
    DSL_COMPOPE_NOT_EQ,
    DSL_COMPOPE_GREATER,
    DSL_COMPOPE_GREATER_EQ,
    DSL_COMPOPE_LOWER,
    DSL_COMPOPE_LOWER_EQ,
]

DSL_ALL_COMPOPES.sort(key = lambda x: -len(x))


# ------------ #
# -- GROUPS -- #
# ------------ #

def findgroups(
    text,
    delims,
    recursive = True
):
# An empty text.
    if not text:
        return [[DSL_ACTION_VERBATIM, '']]

# A none empty text.
    opener, closer = delims
    delim_counter  = 0

    before = ''
    parts  = []

    for char in text:
# Opening a group.
        if char == opener:
            if delim_counter == 0 and before:
                parts.append((DSL_ACTION_VERBATIM, before))
                before = ""

            delim_counter += 1

            if delim_counter > 1:
                if not recursive:
                    raise Exception(
                        f"starting group found inside another in << {text} >>."
                    )

                before += char

# Closing a group.
        elif char == closer:
            delim_counter -= 1

            if delim_counter < 0:
                raise Exception(
                    f"extra << {closer} >> closing delimiter found in << {text} >>."
                )

            elif delim_counter == 0:
                if recursive:
                    before = findgroups(
                        before,
                        delims,
                        recursive
                    )

                else:
                    before = before

                parts.append((TAG_CONTENT_GROUP, before))
                before = ""

# Just one new basic character.
        else:
            before += char

# Let's finish the job.
    if delim_counter != 0:
        raise Exception(f"a group not closed in << {text} >>.")

    if before:
        parts.append((DSL_ACTION_VERBATIM, before))

    return parts


# ------------ #
# -- QUOTES -- #
# ------------ #

def findquotes(text):
# An empty text.
    if not text:
        return [[DSL_ACTION_VERBATIM, '']]

# A none empty text.
    pieces = text.split(TAG_DOUBLE_QUOTE)

# Good number of quotes?
    if len(pieces) % 2 != 1:
        raise Exception(f"bad number of quotes.")

# Let's build the none empty parts.
    parts     = []
    isposeven = False

    for onepart in pieces:
        isposeven = not isposeven

        if not onepart:
            if not isposeven:
                raise Exception(f"empty quotes found.")

            continue

        context = DSL_ACTION_VERBATIM if isposeven else TAG_CONTENT_GROUP

        parts.append((context, onepart))

    return parts


# --------------------- #
# -- FROM ... TO ... -- #
# --------------------- #

def startend_fromto(text):
    startend = [i.strip() for i in text.split(TAG_FROM_TO)]

    if len(startend) != 2:
        raise Exception(f"illegal use of << {TAG_FROM_TO} >>")

    for i in startend:
        if not i.isdigit():
            raise Exception(
                 "non integers used in "
                f"<< {startend[0]} {TAG_FROM_TO} {startend[1]} >>"
            )

        istart, iend = map(int, startend)

    if istart < 0 or iend < 0:
        raise Exception(
             "negative integer(s) found in "
            f"<< {istart} {TAG_FROM_TO} {iend} >>"
        )

    if istart > iend:
        raise Exception(
             "unsupported case "
            f"<< {istart} {TAG_FROM_TO} {iend} >>"
        )

    return istart, iend
