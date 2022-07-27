#!/usr/bin/env python3

import black

from cbdevtools         import *
from mistool.os_use     import PPath
from mistool.string_use import between

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = PPath(__file__).parent

SRC_DIR = THIS_DIR

while(SRC_DIR.name != "cvnum"):
    SRC_DIR = SRC_DIR.parent

THIS_FILE_REL_SRC_PATH = PPath(__file__) - SRC_DIR

SRC_DIR    = SRC_DIR / "src"
CV_DIR_NAT = SRC_DIR / "convert" / "natural"
B2B_PYFILE = CV_DIR_NAT / "base2base.py"


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'cvnum',
)

from src.convert.natural import NatConv, Nat2Base, Base2Nat


# ----------- #
# -- TOOLS -- #
# ----------- #

def symcenter2(text):
    left, _, right = text.partition('2')

    return f"{right}2{left}"


def formattag(text, length = 0):
    # text = text.replace('2', '_2_')
    text = text.replace('of', '_of')
    text = text.upper()

    return f"FORMAT_{text}"


def alignspaces(text, maxlength):
    if maxlength > len(text) :
        text += " "*(maxlength - len(text))

    return text


# ----------------------- #
# -- METHODS AVAILABLE -- #
# ----------------------- #

print(f"   * Building the formats for ``natural.base2base.Base2Base.py``.")

print(f"   * Looking for the methods available in ``Nat2Base`` and ``Base2Nat``.")

methods_natconv = dir(NatConv)

methods_nat2base = set(
    name
    for name in dir(Nat2Base)
    if(
        not name in methods_natconv
        and
        name != 'numeralize'
    )
)


methods_base2nat = set(
    name
    for name in dir(Base2Nat)
    if(
        not name in methods_natconv
        and
        name not in [
            'basedigitize',
            'bnb2numerals',
            'bnb2digits',
        ]
    )
)

# ! -- DEBUGGING -- ! #
print(f"{methods_nat2base = }")
print(f"{methods_base2nat = }")
exit()
# ! -- DEBUGGING -- ! #


missing_nat2base = set()
missing_base2nat = set()

# Names (no b-prefix)
for methods_in, methods_out, missngs, transformer in [
    (methods_nat2base,
     methods_base2nat,
     missing_nat2base,
     lambda t: f'b{t}'),
    #
    (methods_base2nat,
     methods_nat2base,
     missing_base2nat,
     lambda t: t[1:]),
]:
    for name in methods_in:
        bprefname = transformer(name)

        if not bprefname in methods_out:
            missngs.add(name)

# "Palindrom" equivalents.
for missings, methods_out in [
    (missing_base2nat,
     methods_nat2base),
    #
    (missing_nat2base,
     methods_base2nat),
]:
    toremove = []

    for name in missings:
        paliname = symcenter2(name)

        if paliname in methods_out:
            toremove.append(name)

    for name in toremove:
        missings.remove(name)

if missing_nat2base or missing_base2nat:
    raise Exception(
         'API - Missing symmetry'
         '\n'
        f'{missing_nat2base = }'
         '\n'
        f'{missing_base2nat = }'
    )


# ----------------------- #
# -- METHODS AVAILABLE -- #
# ----------------------- #

print(f"   * Building constants for the formats of ``Base2Base``.")

formats_base2base = set()

for name in methods_nat2base:
    if name.endswith('of'):
        continue

    for part in name.split('2'):
        if part[0] == 'b':
            part = part[1:]

        formats_base2base.add(f'b{part}')

formats_base2base.remove('bnat')
formats_base2base.add('nat')

# ! -- DEBUGGING -- ! #
# print(f"{methods_base2nat  = }")
# print(f"{formats_base2base = }")
# exit()
# ! -- DEBUGGING -- ! #


# ------------------------------- #
# -- UPDATE OF THE SOURCE FILE -- #
# ------------------------------- #

print("   * Updating the source code of the Python testing file.")

with B2B_PYFILE.open(
    encoding = "utf-8",
    mode     = "r",
) as f:
    pycode = f.read()

before, _, after = between(
    text     = pycode,
    keepseps = True,
    seps     = [
        '# -- FORMATS ALLOWED "AUTO" - START -- #',
        '# -- FORMATS ALLOWED "AUTO" - END -- #'
    ],
)


TAGS_VARS = {
    formattag(n): n
    for n in formats_base2base
}


maxlength = max(len(x) for x in TAGS_VARS)

formats_vars = '\n'.join([
    f'{alignspaces(name, maxlength)} = {repr(val)}'
    for name, val in TAGS_VARS.items()
])


formats_base2base = ", ".join([
    formattag(n)
    for n in formats_base2base
])

all_formats_code = f"""
ALL_FORMATS = {{{formats_base2base}}}
""".strip()

all_formats_code = black.format_file_contents(
    all_formats_code,
    fast = False,
    mode = black.FileMode()
).strip()

pycode = f"""{before}

# Lines automatically build by the following file.
#
#     + ``{THIS_FILE_REL_SRC_PATH}``

# To avoid mistypings of formats.

{formats_vars}

# To test "hard" typing strings of formats.

{all_formats_code}

{after}"""

with B2B_PYFILE.open(
    encoding = "utf-8",
    mode     = "w",
) as f:
    f.write(pycode)
