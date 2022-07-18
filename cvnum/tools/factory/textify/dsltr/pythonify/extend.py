#!/usr/bin/env python3

from ..rules import *

# ! -- DEBUGGING -- ! #
from pprint import pprint
# ! -- DEBUGGING -- ! #


# -------------------- #
# --  EXTENDED LANG -- #
# -------------------- #

_KINDS_TO_KEEP = set(DSL_ALL_FINAL_SPECS) - set([
    DSL_SPECS_EXTEND,
    DSL_SPECS_IGNORE_GROUP,
    DSL_SPECS_IGNORE_SMALL,
])

_REMAINING_KINDS_TO_KEEP = _KINDS_TO_KEEP - set([
    DSL_SPECS_GROUP,
    DSL_SPECS_SMALL,
])


def sortlangs(alltrans):
    deps = {}

    for lang, specs in alltrans.items():
        if DSL_SPECS_EXTEND in specs:
            deps[lang] = specs[DSL_SPECS_EXTEND][DSL_TAG_LANG]

    # ! -- DEBUGGING -- ! #
    # del deps['fr_BE']
    # deps['fr_BE'] = 'fr_FR'
    # deps['fr_FR_chuquet_2'] = 'fr_FR_rowlett'
    # deps['fr_FR_rowlett']   = 'fr_FR_chuquet_1'

    # print(deps)
    # exit()
    # ! -- DEBUGGING -- ! #

    sortedlangs = [lang for lang in alltrans if not lang in deps]

    for lang, langtoextend in deps.items():
# Do we have a circular use of languages ?
        if lang in sortedlangs:
            i = sortedlangs.index(lang)

            if langtoextend in sortedlangs[i+1:]:
                circular = []

                while(not lang in circular):
                    circular.append(lang)

                    lang = deps[lang]

                circular.append(circular[0])

                circular = ' -> '.join(circular)

                raise Exception(
                     "cicrcular used of languages:\n"
                    f"{circular}"
                )

            if not langtoextend in sortedlangs[:i]:
                sortedlangs[i:i] = [langtoextend]

        else:
            if not langtoextend in sortedlangs:
                sortedlangs.append(langtoextend)

            sortedlangs.append(lang)

    # ! -- DEBUGGING -- ! #
    # print(f"{sortedlangs = }")
    # exit()
    # ! -- DEBUGGING -- ! #

    return sortedlangs


def manage_extend(alltrans):
# Chaining extensions
    sortedlangs      = sortlangs(alltrans)
    pyspecs_alltrans = {}

    for lang in sortedlangs:
        specs           = alltrans[lang]
        pyspecs_onelang = {}

# Illegal use of IGNORE blocks.
        if (
            not DSL_SPECS_EXTEND in specs
            and
            (
                DSL_SPECS_IGNORE_GROUP in specs
                or
                DSL_SPECS_IGNORE_SMALL in specs
            )
        ):
            raise Exception(
                 'use of an "ignore block" without using '
                f'the "extend block". See the translation "{lang}".'
            )

# Not an extension.
        if not DSL_SPECS_EXTEND in specs:
            for kind in _KINDS_TO_KEEP:
                pyspecs_onelang[kind] = specs.get(kind, {})

# An extension.
        else:
            ignored_keys = {
                DSL_SPECS_GROUP: specs.get(DSL_SPECS_IGNORE_GROUP, []),
                DSL_SPECS_SMALL: specs.get(DSL_SPECS_IGNORE_SMALL, []),
            }

            lang_ext = specs[DSL_SPECS_EXTEND][DSL_TAG_LANG]

            # ! -- DEBUGGING -- ! #
            # if lang_ext == "en_GB":
            #     print (f"alltrans['{lang_ext}']['small']")
            #     pprint(alltrans[lang_ext]['small'])
            #     print()
            #     print (f"pyspecs_alltrans['{lang_ext}']['small']")
            #     pprint(pyspecs_alltrans[lang_ext]['small'])
            #     exit()
            # ! -- DEBUGGING -- ! #

# The rules wanted from the initial lang.
            if lang_ext in pyspecs_alltrans:
                rules_extended = pyspecs_alltrans[lang_ext]

            else:
                rules_extended = alltrans[lang_ext]

# Copy the rules that are not ignored.
            for kind in [DSL_SPECS_GROUP, DSL_SPECS_SMALL]:
                ignoreme = ignored_keys[kind]
                all_rules = OrderedDict()

# Let's copy.
                for k, v in rules_extended[kind].items():
                    if k in ignoreme:
                        continue

                    all_rules[k] = v

                # ! -- DEBUGGING -- ! #
                # if kind == 'small' and lang == "en_US":
                #     print (f"all_rules for small")
                #     pprint(all_rules)
                #     exit()
                # ! -- DEBUGGING -- ! #

# We add the rules from the extended lang.
                for k, v in specs.get(kind, {}).items():
                    all_rules[k] = v

                # ! -- DEBUGGING -- ! #
                # if kind == 'small' and lang == "en_US":
                #     print (f"all_rules for small")
                #     pprint(all_rules)
                #     exit()
                # ! -- DEBUGGING -- ! #

# We store all the rules.
                pyspecs_onelang[kind] = all_rules

            # ! -- DEBUGGING -- ! #
            # if lang == "en_US":
            #     print (f"pyspecs_onelang['small']")
            #     pprint(pyspecs_onelang['small'])
            #     exit()
            # ! -- DEBUGGING -- ! #

# Let's copy block from the initial lang.
            for kind in _REMAINING_KINDS_TO_KEEP:
                pyspecs_onelang[kind] = rules_extended.get(kind, {}).copy()

# Do the ``sign`` block have been redefined?
            if DSL_SPECS_SIGN in alltrans[lang]:
                for tag in [DSL_TAG_SIGN_PLUS, DSL_TAG_SIGN_MINUS]:
                    if not alltrans[lang][DSL_SPECS_SIGN][tag] is None:
                        pyspecs_onelang[DSL_SPECS_SIGN][tag] = alltrans[lang][DSL_SPECS_SIGN][tag]

# Do the ``patch`` block has been redefined?
            if DSL_SPECS_PATCH in alltrans[lang]:
                pyspecs_onelang[DSL_SPECS_PATCH] = alltrans[lang][DSL_SPECS_PATCH].copy()

# Take care of changes in the block ``general``.
            for k, v in alltrans[lang].get(DSL_SPECS_GENE, {}).items():
                if(
                    v == ''
                    and
                    k == DSL_TAG_GENE_SEP
                ):
                    v = rules_extended[DSL_SPECS_GENE][k]

                pyspecs_onelang[DSL_SPECS_GENE][k] = v

# Nothing more to do.
        pyspecs_alltrans[lang] = pyspecs_onelang

# Job hase been done.
    return pyspecs_alltrans
