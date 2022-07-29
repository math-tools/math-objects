#!/usr/bin/env python3

from collections import defaultdict
from inspect     import signature, _empty


# ------------------ #
# -- FORMATTINGS -- #
# ------------------ #

def seeat(method):
    return f":see: self.{method}"

def prototype_param(param, method):
    return f"{param} : :see: self.{method}"

def cleantype(onetype):
    for toremove in [
        "typing.",
        "<class '",
        "'>"
    ]:
        onetype = onetype.replace(toremove, "")

    return onetype


# ------------------- #
# -- EXTRA METHODS -- #
# ------------------- #

# Some useful tags.
TAG_XXX_2_NAT, TAG_NAT_2_YYY = int_2_tag = ["XXX_2_nat", "nat_2_YYY"]

TAG_2    = '2'

TAG_BASE = 'base'
TAG_BNB  = 'bnb'

TAG_NB  = 'nb'
TAG_NAT = 'nat'


def cls_xtramethods(cls):
    inst = cls()

# "INPUT" tag & "OUPUT" tag
    tag_input, _, _ = cls.__name__.lower().partition(TAG_2)

    if tag_input == TAG_BASE:
        tag_input = TAG_BNB

    # "FROM" tags & "TO" tags
    tags_from = {}
    tags_to   = {}

# ! -- DEBUGGING -- ! #
    # dircls = {
    #     n
    #     for n in dir(cls)
    #     if n[0] != '_' and TAG_2 in n
    # }
    # print(f"{dircls = }")
# ! -- DEBUGGING -- ! #

    for name in dir(cls):
        if name[0] == "_":
            continue

        if TAG_2 in name:
            before, _, after = name.partition(TAG_2)

            if after == tag_input:
                tags_from[before] = name

            elif before == tag_input:
                tags_to[after] = name

# ! -- DEBUGGING -- ! #
    print(f"{tags_from = }")
    print(f"{tags_to   = }")
    exit()
# ! -- DEBUGGING -- ! #


    # Extra methods added automatically.
    xtra_methods = {}

    for fromtag, frommethod in tags_from.items():
        for totag, tomethod in tags_to.items():
            xtra_methods[f"{fromtag}2{totag}"] = (
                (
                    frommethod,
                    signature(
                        inst.__getattribute__(frommethod)
                    )
                ),
                (
                    tomethod,
                    signature(
                        inst.__getattribute__(tomethod)
                    )
                ),
            )

# ! -- DEBUGGING -- ! #
    # from pprint import pprint;pprint(xtra_methods)
    # print(xtra_methods['digits2bnb'])
    # print(xtra_methods['digits2bnb'][0][1].parameters)
    # print(xtra_methods['digits2bnb'][1][1].parameters)
    # exit()
# ! -- DEBUGGING -- ! #

    xtrainfos = {}

    for xtramethod, metainfos in xtra_methods.items():
        see_return  = ''
        return_type = ''

        methods_called         = {}
        max_len_params         = {}
        infos_params_XXX_2_YYY = defaultdict(list)

        for i, (intermeth, sign) in enumerate(metainfos):
            tag = int_2_tag[i]

            methods_called[tag] = intermeth

            if not intermeth.endswith(TAG_NAT):
                see_return  = seeat(intermeth)
                return_type = cleantype(str(sign.return_annotation))

            max_len_params[tag] = 0

            for p, t in sign.parameters.items():
                if p == TAG_NB:
                    continue

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

                see_params.append(
                    prototype_param(p_all, see)
                )

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
