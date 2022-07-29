#!/usr/bin/env python3

from collections import defaultdict
from inspect     import signature, _empty

from cbdevtools         import *
from mistool.os_use     import PPath
from mistool.string_use import between

from core.xtra_methods import (
    cls_xtramethods,
    TAG_XXX_2_NAT,
    TAG_NAT_2_YYY
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
        # "nat2base",
# tags_from = {'digits': 'digits2nat', 'numerals': 'numerals2nat'}
# tags_to   = {'bdigits': 'nat2bdigits', 'bnb': 'nat2bnb', 'bnumerals': 'nat2bnumerals'}
        "base2nat",
# tags_from = {'bdigits': 'bdigits2bnb', 'bnumerals': 'bnumerals2bnb'}
# tags_to   = {'digits': 'bnb2digits', 'nat': 'bnb2nat', 'numerals': 'bnb2numerals'}
    ]
}


# -------------------------------------------- #
# -- REMOVE THE XTRA METHODS IN THE SOURCES -- #
# -------------------------------------------- #

for modulename, pyfile in PYFILES.items():
    print(f"   * Module ``{modulename}`` - Removing the codes of the extra methods.")

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

from src.convert.natural import Nat2Base, Base2Nat, Base2Base

CLASSES = {
    c.__name__.lower(): c
    for c in [
        Nat2Base,
        Base2Nat,
        Base2Base,
    ]
}


# --------------- #
# -- TEMPLATES -- #
# --------------- #

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


# ----------------------- #
# -- METHODS AVAILABLE -- #
# ----------------------- #

for modulename, pyfile in PYFILES.items():
    print(f"   * Module ``{modulename}`` - Looking for the extra methods.")

    xtrainfos = cls_xtramethods(
        cls = CLASSES[modulename],
    )

# ! -- DEBUGGING -- ! #
    # for xtramethod, infos in xtrainfos.items():
    #     print('---')
    #     print(xtramethod)
    #     # print(infos)
    #     print()
    # continue
    # exit()
# ! -- DEBUGGING -- ! #


# ------------------------ #
# -- PYTHON CODE UPDATE -- #
# ------------------------ #

    print(f"   * Module ``{modulename}`` - Updating the Python code.")

    xtra_code = []

    for xtramethod, infos in xtrainfos.items():
        see_params  = TABU_PROTO.join(infos["see_params"])
        params_xtra = TABU_METH_2.join(infos["params_xtra"])

        params_XXX_2_nat = TABU_METH_4.join(
            infos["params_XXX_2_YYY"][TAG_XXX_2_NAT]
        )

        params_nat_2_YYY = TABU_METH_3.join(
            infos["params_XXX_2_YYY"][TAG_NAT_2_YYY]
        )

        code_prototype = TEMP_PROTOTYPE.format(
            see_params = see_params,
            see_return = infos["see_return"],
        )

        code_meth = TEMP_METH_CODE.format(
            xtramethod       = xtramethod,
            params_xtra      = params_xtra,
            XXX_2_nat        = infos["methods_called"][TAG_XXX_2_NAT],
            nat_2_YYY        = infos["methods_called"][TAG_NAT_2_YYY],
            return_type      = infos["return_type"],
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
