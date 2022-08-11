#!/usr/bin/env python3

from collections import defaultdict
from inspect     import signature, _empty

from cbdevtools import *


# ----------------- #
# -- MODULE USED -- #
# ----------------- #

for upfolder in [
    'convert',
    # 'tests',
]:
    _ = addfindsrc(
        file    = __file__,
        project = upfolder,
    )

from cvcore.protontype import *


# ------------------- #
# -- EXTRA METHODS -- #
# ------------------- #

# Some useful tags.
TAG_XXX_2_INTER, TAG_INTER_2_YYY = int_2_tag = ["XXX_2_inter", "inter_2_YYY"]

TAG_2      = '2'
TAG_FROM   = 'from'
lentagfrom = len(TAG_FROM)

TAG_BNUMERALS       = 'bnumerals'
TAG_BNUMERALS_2_NAT = 'bnumerals2nat'
TAG_BNB_2_NAT       = 'bnb2nat'

TAG_SEP = 'sep'

TAG_BASE = 'base'
TAG_BNB  = 'bnb'

TAG_NB  = 'nb'
TAG_NAT = 'nat'


def cls_xtramethods(
    cls,
    xtra_methods_hard_specs,
):
    dircls = shortdir(cls)
    inst   = cls()

# "INPUT" tag & "OUPUT" tag
    tag_input, _, _ = cls.__name__.lower().partition(TAG_2)

    if tag_input == TAG_BASE:
        tag_input = TAG_BNB

    # "FROM" tags & "TO" tags
    tags_from = {}
    tags_to   = {}

# ! -- DEBUGGING -- ! #
    # _dircls = {
    #     n
    #     for n in dircls
    #     if n[0] != '_'
    # }
    # print(f"{_dircls = }")
# ! -- DEBUGGING -- ! #

    for name in dircls:
        if TAG_2 in name:
            _, _, after = name.partition(TAG_2)

            tags_to[after] = name

        elif name.startswith(TAG_FROM):
            tags_from[name[lentagfrom:]] = name

# ! -- DEBUGGING -- ! #
    # print(f"{tags_from = }")
    # print(f"{tags_to   = }")
    # exit()
# ! -- DEBUGGING -- ! #


    # Extra methods specified directly.
    xtra_methods = xtra_methods_hard_specs

    # Extra methods added automatically.
    for fromtag, frommethod in tags_from.items():
        for totag, tomethod in tags_to.items():
            xtra_name = f"{fromtag}2{totag}"

            if not xtra_name in xtra_methods:
                xtra_methods[xtra_name] = [
                    frommethod,
                    tomethod
                ]

# ! -- DEBUGGING -- ! #
    # for n in xtra_methods:
    #     print()
    #     print(f"--- {n} ---")
    #     print(xtra_methods[n])
    # exit()
# ! -- DEBUGGING -- ! #

    # Signatures for "known" methods.
    for xtraname, methodsused in xtra_methods.items():
        for i, meth in enumerate(methodsused):
            if meth in dircls:
                sign = signature(inst.__getattribute__(meth))

            elif meth.startswith('self.nat2base'):
                submeth = meth.split('.')[-1]
                sign    = signature(
                    inst
                        .__getattribute__('nat2base')
                        .__getattribute__(submeth)
                    )

            else:
                sign = None

            methodsused[i] = (meth, sign)

        xtra_methods[xtraname] = methodsused

    # Signatures for "unknown" methods.
    dynasign = {}

    for xtraname, methodsused in xtra_methods.items():
        for i, (meth, sign) in enumerate(methodsused):
            if sign is None:
                if meth in dynasign:
                    sign = dynasign[meth]

                else:
                    _, sign   = xtra_methods[meth][0]
                    _, retval = xtra_methods[meth][1]

                    sign = sign.replace(
                        return_annotation = retval.return_annotation
                    )

                    dynasign[meth] = sign

                methodsused[i] = (meth, sign)

# ! -- DEBUGGING -- ! #
    # for n in xtra_methods:
    #     print()
    #     print(f"--- {n} ---")
    #     print(xtra_methods[n])
    # exit()
# ! -- DEBUGGING -- ! #

    xtrainfos = {}

    for xtramethod, metainfos in xtra_methods.items():
        if xtramethod in dircls:
            continue

        see_return  = ''
        return_type = ''

        methods_called         = {}
        max_len_params         = {}
        infos_params_XXX_2_YYY = defaultdict(list)

        prefix_xtra = xtramethod.split(TAG_2)[0]

        fromb_used   = False
        params_found = []

        for i, (intermeth, sign) in enumerate(metainfos):
            if intermeth.startswith("fromb"):
                fromb_used = True

            tag = int_2_tag[i]

            methods_called[tag] = intermeth

            if not intermeth.endswith(TAG_NAT):
                see_return  = seeat(
                    intermeth,
                    useself  = not(intermeth.startswith('self.'))
                )
                return_type = cleantype(str(sign.return_annotation))

            max_len_params[tag] = 0

            for p, t in sign.parameters.items():
                if (
                        p in params_found
                ) or (
                        p != prefix_xtra
                    and p in [TAG_NB, TAG_BNB]
                ) or (
                        p == TAG_BNUMERALS
                    and i == 1
                    and intermeth == TAG_BNUMERALS_2_NAT
                ) or (
                        p == TAG_SEP
                    and fromb_used
                ):
                    continue

                params_found.append(p)

                default = sign.parameters[p].default

                if default == _empty:
                    default = None

                max_len_params[tag] = max(
                    len(p),
                    max_len_params[tag]
                )

                infos_params_XXX_2_YYY[tag].append({
                    'p'      : p,
                    'ptype'  : cleantype(str(t.annotation)),
                    'see'    : intermeth,
                    'default': default,
                })

# ! -- DEBUGGING -- ! #
        # print(f"{see_return  = }")
        # print(f"{return_type = }")
        # print()
        # print(f"{methods_called         = }")
        # print(f"{infos_params_XXX_2_YYY = }")
        # exit()
# ! -- DEBUGGING -- ! #

        see_params       = []
        params_xtra      = []
        params_XXX_2_YYY = defaultdict(list)

        maxlen_all = max(m for m in max_len_params.values())

        for tag, aboutparams in infos_params_XXX_2_YYY.items():
            maxlen = max_len_params[tag]

            for infos in aboutparams:
                p       = infos['p']
                ptype   = infos['ptype']
                see     = infos['see']
                default = infos['default']

                len_p = len(p)
                p_all = p + ' '*(maxlen_all - len_p)

                proto_p = prototype_oneparam(p_all, see)
                see_params.append(proto_p)

                if default is None:
                    default = ''

                else:
                    default = f" = {repr(default)}"

                params_xtra.append(f"{p_all}: {ptype}{default},")

                p += ' '*(maxlen - len_p)

                params_XXX_2_YYY[tag].append(f"{p} = {p.strip()},")

        xtrainfos[xtramethod] =  {
            "see_return"      : see_return,
            "return_type"     : return_type,
            "see_params"      : see_params,
            "params_xtra"     : params_xtra,
            "params_XXX_2_YYY": params_XXX_2_YYY,
            "methods_called"  : methods_called,
        }

    return xtrainfos
