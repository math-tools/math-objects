#!/usr/bin/env python3

from pprint import pprint

from dsltr import *

# Clear the terminal.
print("\033c", end="")

# Hooks
if False:
    text = ""
    text = "123"
    text = "[1..6 | 8]*"
    text = "[d(2) :if: d(2) > 1] [100] [d(1)d(0)]"
    text = "a [d(2) :if: d(2) > 1] b [100] c [d(1)d(0)] d"

    delims    = TAG_DELIM_HOOKS
    recursive = False

    print(
        '---',
        text,
        '',
        sep = "\n"
    )
    print(
        findgroups(text, delims, recursive)
    )

# Quotes
if False:
    text = ''
    text = '123'
    text = '"123"'
    text = 'a "123  ""45678" c "90" d'

    print(
        '---',
        text,
        '',
        sep = "\n"
    )
    print(
        findquotes(text)
    )

# Matching
if False:
    text = "1..6 | 8"
    text = " cents mille "
    text = " 13 "
    text = "[1] "
    text = "[1..6 | 8] * "
    text = "9*"

    print(
        '---',
        text,
        '',
        sep = "\n"
    )
    print(
        matchpatt(text)
    )

# Calc. translations.
if True:
    text = ''
    text = '[123]'
    text = '[123d]'
    text = '[123d(45)678]'
    text = '[12d3d(45)678r(4..88)]'

    # text = '[d(2)]     hundred [d(1)d(0)]'

    text = '[d :if: d(2) > 1] [100] [d(1)d(0)]'
    text = '[d :if: d(2) > 1r(5..7)0 :else: r] [100] [d(1)d(0)]'
    # text = '[d(2)00] [d(1)d(0)]'
    text = '[d :if: d > 1] mil'
    # text = 'a[b]c[e :if: d]f[g]h'

    text = 'billion{s}'
    text = 'billion{can :if : d}'
    # text = 'billion[{NO!}]'

    text = '[d(1)0]-et-[1]'
    text = '[r]'

    text = '"un :if: d == 1 :else: [d]" mill"ón :if: d == 1 :else: ones" [r]'

    text = '[d(2) :if: d(2) > 1] cent"s :if: d(2) > 1" [d(1)d(0) :if: d(1)d(0) != 0]'

    text = 'abc{XYZ}'
    # text = 'billion"s :if: d > 1"' # PLURIAL !!!   {...} <--> "... :if: d > 1"
    # text = 'thousand "and [123] :if: r < 100"'
    # text = 'thousand "and [123] :if: 0 < r < 100"'
    # text = 'thousand "and [123] :if: 0 < r < 8 < 100"'
    # text = 'thousand "and [123] :if: 0 < r <= 100"'
    # text = 'thousand "and [12d(4)3] :if: 0 < r <= 100"'
    # text = 'thousand "and [12d(4)3] :if: 0 < r > 100"'
    # text = 'thousand "and [12d(4)3] :if: 0 < r = 100"'
    # text = '"un :if: d = 1 :else: [d]" mill"[5 :if: d = 5] ok [1230] :if: d = 1 :else: [77]"'
    # text = '[60]-"et- :if: d(0) = 1"[1d(0)]'

    # text = 'a     "[b]c[e :if: d]  :if:   d = 5 :else: f[g]h"   i'
    # text = 'xxx     "[a :if: b :else: c] [X]  :if:   d :else: [e :if: c :else: f] [Y]"     yyy'
    # text = '"a  :if:   d :else: [e :if: c :else: f]"'
    # text = '"a  :if:   d :else: b"'

    print(
        '---',
        text,
        '',
        sep = "\n"
    )
    pprint(
        calctrans(text)
    )
