#!/usr/bin/env python3

from cbdevtools         import *
from mistool.os_use     import PPath
from mistool.string_use import between

from core.xtra_methods import (
    cls_xtramethods,
    TAG_XXX_2_INTER,
    TAG_INTER_2_YYY
)

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

PYFILES = {
    name: CV_DIR_NAT / f"{name}.py"
    for name in [
        "nat2base",
        "base2nat",
    ]
}

XTRA_METHODS_HARD_SPECS = {n: {} for n in PYFILES}

XTRA_METHODS_HARD_SPECS["base2nat"] = {
    "bnb2nat"           : ["bnumeralsof"  , "bnumerals2nat"           ],
    "bnb2digits"        : ["bnb2nat"      , "self.nat2base.digitsof"  ],
    "bnb2numerals"      : ["bnb2nat"      , "self.nat2base.numeralsof"],
    "bdigits2nat"       : ["frombdigits"  , "bnb2nat"                 ],
    "bnumerals2nat"     : ["frombnumerals", "bnb2nat"                 ],
# Missing methods found with ``check_xtra_methods.py``.
    "bdigits2digits"    : ["frombdigits"  , "bnb2digits"              ],
    "bdigits2numerals"  : ["frombdigits"  , "bnb2numerals"            ],
    "bnumerals2digits"  : ["frombnumerals", "bnb2digits"              ],
    "bnumerals2numerals": ["frombnumerals", "bnb2numerals"            ],
}


# -------------------------------------------- #
# -- REMOVE THE XTRA METHODS IN THE SOURCES -- #
# -------------------------------------------- #

print(f"   * Removing the codes of the extra methods.")

for modulename, pyfile in PYFILES.items():
    print(f"       + Module ``{modulename}``")

    with pyfile.open(
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

    with pyfile.open(
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

from src.convert.natural import Nat2Base, Base2Nat

CLASSES = {
    c.__name__.lower(): c
    for c in [
        Nat2Base,
        Base2Nat,
    ]
}


# --------------- #
# -- TEMPLATES -- #
# --------------- #

TAG_SELF     = "self."
LEN_TAG_SELF = len(TAG_SELF)

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

TEMP_METH_CODE = {
    'nat2base': " "*4 + """
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
""".strip(),
# We keep the unused ``{params_nat_2_YYY}`` to symplifu-y the code.
    'base2nat': " "*4 + """
    def {xtramethod}(
        self,
        {params_xtra}
    ) -> {return_type}:
        return self.{nat_2_YYY}(
            bnb = self.{XXX_2_nat}(
                {params_XXX_2_nat}
            ),
            base = base,{params_nat_2_YYY}
        )
""".strip()
}


# ----------------------- #
# -- METHODS AVAILABLE -- #
# ----------------------- #

for modulename, pyfile in PYFILES.items():
    print(f"   * Module ``{modulename}``")
    print( "       + Building the extra methods.")

    xtrainfos = cls_xtramethods(
        cls                    = CLASSES[modulename],
        xtra_methods_hard_specs = XTRA_METHODS_HARD_SPECS[modulename],
    )

# ! -- DEBUGGING -- ! #
    # for xtramethod, infos in xtrainfos.items():
    #     print('---')
    #     # if xtramethod == "bdigits2nat":
    #     #     print(xtramethod)
    #     #     print(infos)
    #     #     print(f"{infos['params_xtra'] = }")
    #     #     print(f"{infos['return_type'] = }")
    #     #     continue
    #     print(xtramethod)
    #     # from pprint import pprint;pprint(infos)
    #     # print(list(infos.keys()))
    #     print(f"{infos['params_xtra'] = }")
    #     print(f"{infos['return_type'] = }")
    #     input("?")
    #     print()
    # continue
    # exit()
# ! -- DEBUGGING -- ! #


# ------------------------ #
# -- PYTHON CODE UPDATE -- #
# ------------------------ #

    print("       + Updating the Python code.")

    xtra_code = []

    for xtramethod, infos in xtrainfos.items():
        see_params  = TABU_PROTO.join(infos["see_params"])
        params_xtra = TABU_METH_2.join(infos["params_xtra"])

        params_XXX_2_nat = TABU_METH_4.join(
            infos["params_XXX_2_YYY"][TAG_XXX_2_INTER]
        )

        params_nat_2_YYY = TABU_METH_3.join(
            infos["params_XXX_2_YYY"][TAG_INTER_2_YYY]
        )

        code_prototype = TEMP_PROTOTYPE.format(
            see_params = see_params,
            see_return = infos["see_return"],
        )

        temp_name = modulename

        if (
            modulename == 'base2nat'
            and
            infos["methods_called"][TAG_INTER_2_YYY].startswith(TAG_SELF)
        ):
            tagselfused = True

            infos["methods_called"][TAG_INTER_2_YYY] = \
            infos["methods_called"][TAG_INTER_2_YYY][LEN_TAG_SELF:]

            temp_name = 'nat2base'

        else:
            tagselfused = False

        code_meth = TEMP_METH_CODE[temp_name].format(
            xtramethod       = xtramethod,
            params_xtra      = params_xtra,
            XXX_2_nat        = infos["methods_called"][TAG_XXX_2_INTER],
            nat_2_YYY        = infos["methods_called"][TAG_INTER_2_YYY],
            return_type      = infos["return_type"],
            params_XXX_2_nat = params_XXX_2_nat,
            params_nat_2_YYY = params_nat_2_YYY,
        )

        if tagselfused:
            code_meth = '\n'.join(
                l
                for l in code_meth.split('\n')
                if l.strip()
            )

# Ugly hack.
        if temp_name == 'base2nat':
            for old, new in [
                (
                    "bnb = self.bnumeralsof",
                    "bnumerals = self.bnumeralsof"
                )
            ]:
                code_meth = code_meth.replace(old, new)

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

    with pyfile.open(
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

    with pyfile.open(
        encoding = "utf-8",
        mode     = "w",
    ) as f:
        f.write(pycode)
