#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from cbdevtools import *


# ------------------------------------------ #
# -- MODULE TESTED IMPORTED FROM SOURCES! -- #
# ------------------------------------------ #

for upfolder in [
    'cvnum',
    # 'tests',
]:
    _ = addfindsrc(
        file    = __file__,
        project = upfolder,
    )

from src.convert.natural import Nat2Base, Base2Nat


# ----------- #
# -- TOOLS -- #
# ----------- #

def shortdircls(cls, toignore):
    dircls_cleaned = set()

    for name in dir(cls):
        if not(
            name[0] == '_'
            or
            name.startswith('check')
            or
            name in toignore
        ):
            dircls_cleaned.add(name)

    return dircls_cleaned


def test_nat2base_sym_apis_N2B_B2N():
    methods_ignored = {
        Nat2Base: [
            'numeralize',
        ],
        Base2Nat: [
            'basedigitize',
        ],
    }

    api = {}

    for onecls in [
        Nat2Base,
        Base2Nat
    ]:
        api[onecls] = shortdircls(
            cls      = onecls,
            toignore = methods_ignored[onecls],
        )

# No common name for methods.
    assert api[Nat2Base].intersection(api[Base2Nat]) == set()

# Special case of ``nat2bnb`` and ``bnb2nat``.
    for name, onecls in [
        ("nat2bnb", Nat2Base),
        ("bnb2nat", Base2Nat),
    ]:
        assert name in api[onecls]

        api[onecls].remove(name)

# Looking for other symetric names.
    toremove = {
        Nat2Base: set(),
        Base2Nat: set(),
    }

    len_nat2b = len('nat2b')
    len_from  = len('from')
    len_2nb   = len('2nb')

    for name in api[Nat2Base]:
        symname = None

        for where, what, newpre, slicepos in [
# ``where = 0`` for the start.
# ``where = 1`` for the end.
#
# nat2bXYZ...   <-->   bnb2XYZ
#
# For example, we have ``Nat2Base.nat2bnumerals`` and
# we want ``Base2Nat.bnb2numerals``.
            (0, 'nat2b', 'bnb2', len_nat2b),
# XYZ...of   <-->   bXYZ...of
#
# For example, we have ``Nat2Base.digitsof`` and
# we want ``Base2Nat.bdigitsof``.
            (1, 'of', 'b', 0),
# fromXYZ...   <-->   frombXYZ
#
# For example, we have ``Nat2Base.fromnumerals`` and
# we want ``Base2Nat.frombnumerals``.
            (0, 'from', 'fromb', len_from),
        ]:
            if where == 0:
                if name.startswith(what):
                    symname = newpre + name[slicepos:]

            elif name.endswith(what):
                symname = newpre + name[slicepos:]

# RST2bXYZ...   <-->   bRST2XYZ
#
# For example, we have ``Nat2Base.digits2bnumerals`` and
# we want ``Base2Nat.bdigits2numerals``.
        if symname is None and '2b' in name:
            parts = name.split('2b')

            assert len(parts) == 2

            symname = 'b' + '2'.join(parts)

            if symname.endswith('2nb'):
                symname = symname[:-len_2nb] + '2nat'

            assert symname in api[Base2Nat], \
                   (
                       f"Missing methdod ``{symname}`` "
                        "in the API of ``Base2Nat``"
                   )

            toremove[Nat2Base].add(name)
            toremove[Base2Nat].add(symname)

# Something expected is missing...
        if not symname is None:
            assert symname in api[Base2Nat], \
                   (
                       f"Missing methdod ``{symname}`` "
                        "in the API of ``Base2Nat``"
                   )

            toremove[Nat2Base].add(name)
            toremove[Base2Nat].add(symname)

# Nothing remaining?
    for onecls, matchings in toremove.items():
        api[onecls] -= matchings

    assert (api[Nat2Base] == set()
            and
            api[Base2Nat] == set()
           ),(
             "what is remaining:"
             "\n\n"
            f"{api[Nat2Base] = }"
             "\n\n"
            f"{api[Nat2Base] = }"
           )


test_nat2base_sym_apis_N2B_B2N()
