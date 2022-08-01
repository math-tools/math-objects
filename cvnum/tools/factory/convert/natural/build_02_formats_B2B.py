#!/usr/bin/env python3

from inspect import signature, _empty

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

from src.convert.natural import Nat2Base, Base2Nat


# ----------------------- #
# -- METHODS AVAILABLE -- #
# ----------------------- #

print("   * Looking for the methods available in``Base2Nat``.")

methods      = {}
inst_N2B     = Nat2Base()
inst_B2N     = Base2Nat()
dir_inst_B2N = dir(inst_B2N)

for name in dir_inst_B2N:
    if "2" in name:
        name, _ = name.split("2")

        if name == 'nat':
            continue

        if not name in methods:
            inname  = f"{name}2nat"
            outname = f"nat2{name}"

            methods[name] = {
                "params": {
                    "in": dict(
                        signature(
                            inst_B2N.__getattribute__(inname)
                        ).parameters
                    ),
                    "out": dict(
                        signature(
                            inst_N2B.__getattribute__(outname)
                        ).parameters
                    ),
                },
                "return": signature(
                    inst_N2B.__getattribute__(outname)
                ).return_annotation,

            }

# ! -- DEBUGGING -- ! #
# print()
# from pprint import pprint;pprint(methods)
# print()
# print(f"{dir(Base2Nat) = }")
# print()
# print(f"{dir(Nat2Base) = }")
# print()
# exit()
# ! -- DEBUGGING -- ! #


# ---------------- #
# -- SIGNATURES -- #
# ---------------- #

print("   * Building the codes of the methods.")

IN_OUT_PARAMS = [
    'base',
    'sep',
]

def good_param_name(name, kind):
    return (
        f"{name}_{kind}"
        if name in IN_OUT_PARAMS else
        name
    )

signatures = {}

for name_in, signs_in in methods.items():
    params_in = {
        n: str(s)
        for n, s in signs_in["params"]["in"].items()
    }

    for name_out, signs_out in methods.items():
        name = f"{name_in}2{name_out}"

        params = {
            'in' : params_in,
            'out': {
                n: str(s)
                for n, s in signs_out["params"]["out"].items()
                if n != 'nb'
            }
        }

        return_type = str(signs_out['return'])
        return_type = return_type.replace('typing.', '')

# ! -- DEBUGGING -- ! #
        # print('---')
        # print(f"{name        = }")
        # print(f"{params      = }")
        # print(f"{return_type = }")
        # print()
        # exit()
# ! -- DEBUGGING -- ! #

        signatures[name] = {
            'params'     : params,
            'return_type': return_type,
        }

# To simplify the ``:see: ...``
signatures_sorted = {
    'bnb2bnb': signatures['bnb2bnb']
}

del signatures['bnb2bnb']

allnames = list(signatures)


for name in allnames:
    if name.endswith('2bnb'):
        signatures_sorted[name] = signatures[name]

        del signatures[name]

signatures_sorted.update(signatures)

del signatures

# ! -- DEBUGGING -- ! #
print(list(signatures_sorted.keys()))
from pprint import pprint
pprint(signatures_sorted)
exit()
# ! -- DEBUGGING -- ! #


# ---------- #
# -- CODE -- #
# ---------- #

print("   * Building the code of the methods.")

PROTO_DESCS = {
# Datas.
    'bnb'      : "BNB",
    'bdigits'  : "BDIGITS",
    'bnumerals': "BNUMERALS",
# About.
    'base_in'  : "BASE IN",
    'base_out' : "BASE OUT",
    'sep_in'   : "SEP IN",
    'sep_out'  : "BASE OUT",
}

TEMP_PROTOTYPE = """
###
# prototype::
#     {see_params}
#
#     :return: {see_return}
###
""".strip()

TEMP_METH_CODE = " "*4 + """
    def {name}(
        self,
        {params}
    ) -> {return_type}:
        return self.{nat_2_YYY}(
            nb = self.{XXX_2_nat}(
                {params_in}
            ),
            {params_out}
        )
""".strip()
