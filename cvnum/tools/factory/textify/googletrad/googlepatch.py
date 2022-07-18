#!/usr/bin/env python3

import re

from mistool.os_use import PPath
from orpyste.data   import ReadBlock
from regex import P

THIS_DIR = PPath(__file__).parent

for k in ['nb', 'txt']:
    with ReadBlock(
        content = THIS_DIR / f"googlepatch-{k}2txt.txt",
        mode    = "keyval:: =" if k == 'txt' else "verbatim"
    ) as datas:
# The scope of vars()['x'] will be exactly the same as the scope of x.
        vars()[f"{k.upper()}_PATCHES"] = datas.mydict("std nosep nonb")


AT_END, ANYWHERE = range(2)

for lang, lang_txt_patches in TXT_PATCHES.items():
    allbads = list(lang_txt_patches)

    for bad in allbads:
        newbad  = bad.replace(':s:', ' ')
        newgood = lang_txt_patches[bad].replace(':s:', ' ')

        if newbad[-1] == '^':
            where  = AT_END
            newbad = newbad[:-1]

        else:
            where = ANYWHERE

        lang_txt_patches[newbad] = (where, newgood)

        if newbad != bad:
            del lang_txt_patches[bad]


for lang, patterns in NB_PATCHES.items():
    NB_PATCHES[lang] = [
        re.compile(p.replace('*', '.'))
        for p in patterns
        if p
    ]


# ! -- DEBUGGING -- ! #
# print(f"{NB_PATCHES  = }")
# print(f"{TXT_PATCHES = }")
# exit()
# ! -- DEBUGGING -- ! #


def nbmatchpatches(nb, patterns):
    for p in patterns:
        if p.search(nb):
            return p

    return None


def correct_badtrad(lang, nb, gtrad, langnameof):
    # ! -- DEBUGGING -- ! #
    # print(">>> correct_badtrad <<<")
    # print(f"{lang        = }")
    # print(f"{nb          = }")
    # print(f"{gtrad       = }")
    # exit()
    # ! -- DEBUGGING -- ! #

    if lang in NB_PATCHES:
        pattern = nbmatchpatches(nb, NB_PATCHES[lang])

        if not pattern is None:
            return langnameof(nb)

    if lang in TXT_PATCHES:
        for bad, (where, good) in TXT_PATCHES[lang].items():
            if where == ANYWHERE:
                gtrad = gtrad.replace(bad, good)

            elif gtrad.endswith(bad):
                gtrad = gtrad[:-len(bad)] + good

    return gtrad
