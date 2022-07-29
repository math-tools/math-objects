#!/usr/bin/env python3

from collections import defaultdict
from inspect     import signature, _empty

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
N2B_PYFILE = CV_DIR_NAT / "nat2base.py"


# -------------------------------------------- #
# -- REMOVE THE XTRA METHODS IN THE SOURCES -- #
# -------------------------------------------- #

print(f"   * Removing the codes of the extra methods. TODO!")

with N2B_PYFILE.open(
    encoding = "utf-8",
    mode     = "r",
) as f:
    pycode = f.read()

before, _, after = between(
    text     = pycode,
    keepseps = True,
    seps     = [
        '# -- EXTRA METHODS "AUTO" - START -- #',
        '# -- EXTRA METHODS "AUTO" - END -- #'
    ],
)

pycode = f"""{before}
{after}"""

with N2B_PYFILE.open(
    encoding = "utf-8",
    mode     = "w",
) as f:
    f.write(pycode)


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'cvnum',
)

from src.convert.natural import Nat2Base, Base2Nat, Base2Base


# ----------- #
# -- TOOLS -- #
# ----------- #

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


# ----------------------- #
# -- METHODS AVAILABLE -- #
# ----------------------- #

print(f"   * Looking for the extra methods.")

# Some useful tags.
TAG_BASE = 'base'
TAG_BNB  = 'bnb'
TAG_2    = '2'

cls  = Nat2Base
inst = cls()

# "INPUT" tag & "OUPUT" tag
tag_input, _, _ = cls.__name__.lower().partition(TAG_2)

if tag_input == TAG_BASE:
    tag_input = TAG_BNB

# "FROM" tags & "TO" tags
tags_from = {}
tags_to   = {}

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
# print(f"{tags_from = }")
# print(f"{tags_to   = }")
# exit()
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


# ----------------------- #
# -- METHODS AVAILABLE -- #
# ----------------------- #

print(f"   * Building the codes of the extra methods.")

TAG_NB  = 'nb'
TAG_NAT = 'nat'

TABU_PROTO  = '\n# ' + ' '*4
TABU_METH_2 = '\n' + ' '*8
TABU_METH_3 = '\n' + ' '*12
TABU_METH_4 = '\n' + ' '*16

TEMP_PROTOTYPE = """
###
# prototype::
#     {see_params}
#
#     :return: {see_return}
###
""".strip()

TEMP_METH_CODE = " "*4 + """
    def {xtramethod}(
        self,
        {params_xtra}
    ) -> {return_type}:
        return self.{nat_2_YYY}(
            nb = self.{XXX_2_nat}(
                {params_XXX_2_nat}
            ),
            {params_nat_2_YYY}
        )
""".strip()

xtra_code = []

for xtramethod, metainfos in xtra_methods.items():
# ! -- DEBUGGING -- ! #
    # print('---')
    # print(xtramethod)
    # print()
# ! -- DEBUGGING -- ! #

    see_return  = ''
    return_type = ''

    TAG_XXX_2_NAT, TAG_NAT_2_YYY = int_2_tag = ["XXX_2_nat", "nat_2_YYY"]

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

# ! -- DEBUGGING -- ! #
    # print(f"{see_params  = }")
    # print(f"{params_xtra = }")
    # print()
    # print(f"{methods_called   = }")
    # print(f"{params_XXX_2_YYY = }")
    # exit()
# ! -- DEBUGGING -- ! #

    see_params       = TABU_PROTO.join(see_params)
    params_xtra      = TABU_METH_2.join(params_xtra)
    params_XXX_2_nat = TABU_METH_4.join(params_XXX_2_YYY[TAG_XXX_2_NAT])
    params_nat_2_YYY = TABU_METH_3.join(params_XXX_2_YYY[TAG_NAT_2_YYY])

    code_prototype = TEMP_PROTOTYPE.format(
        see_params = see_params,
        see_return = see_return,
    )

    code_meth = TEMP_METH_CODE.format(
        xtramethod       = xtramethod,
        params_xtra      = params_xtra,
        XXX_2_nat        = methods_called[TAG_XXX_2_NAT],
        nat_2_YYY        = methods_called[TAG_NAT_2_YYY],
        return_type      = return_type,
        params_XXX_2_nat = params_XXX_2_nat,
        params_nat_2_YYY = params_nat_2_YYY,
    )

    xtra_code.append(f"{code_prototype}\n{code_meth}")

# ! -- DEBUGGING -- ! #
    # print('---')
    # print()
    # print("TEMP_PROTOTYPE:")
    # print(code_prototype)
    # print()
    # print(code_meth)
    # print()
    # exit()
# ! -- DEBUGGING -- ! #

xtra_code = ("\n"*3).join(xtra_code)

with N2B_PYFILE.open(
    encoding = "utf-8",
    mode     = "r",
) as f:
    pycode = f.read()

before, _, after = between(
    text     = pycode,
    keepseps = True,
    seps     = [
        '# -- EXTRA METHODS "AUTO" - START -- #',
        '# -- EXTRA METHODS "AUTO" - END -- #'
    ],
)

pycode = f"""{before}

# Lines automatically build by the following file.
#
#     + ``{THIS_FILE_REL_SRC_PATH}``

{xtra_code}

{after}"""

# ! -- DEBUGGING -- ! #
# print(pycode)
# exit()
# ! -- DEBUGGING -- ! #

with N2B_PYFILE.open(
    encoding = "utf-8",
    mode     = "w",
) as f:
    f.write(pycode)
