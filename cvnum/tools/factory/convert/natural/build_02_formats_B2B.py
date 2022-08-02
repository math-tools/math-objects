#!/usr/bin/env python3

from inspect import signature, _empty
from collections import defaultdict

# import black

from cbdevtools         import *
from mistool.os_use     import PPath
from mistool.string_use import between

from core.protontype import *
from core.templates  import *


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


TAG_PROTO       = "prototype"
TAG_PARAMS      = "params"
TAG_RETURN_TYPE = "return_type"

TAG_ALL = "all"
TAG_IN  = "in"
TAG_OUT = "out"


# -------------------------------------------- #
# -- REMOVE THE XTRA METHODS IN THE SOURCES -- #
# -------------------------------------------- #

print("   * Removing the codes of the auto-build methods.")

with B2B_PYFILE.open(
    encoding = "utf-8",
    mode     = "r",
) as f:
    pycode = f.read()

before, _, after = between(
    text     = pycode,
    keepseps = True,
    seps     = [
        '# -- METHODS "AUTO" - START -- #',
        '# -- METHODS "AUTO" - END -- #'
    ],
)

pycode = f"""{before}
{after}"""

with B2B_PYFILE.open(
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
                TAG_PARAMS: {
                    TAG_IN: dict(
                        signature(
                            inst_B2N.__getattribute__(inname)
                        ).parameters
                    ),
                    TAG_OUT: dict(
                        signature(
                            inst_N2B.__getattribute__(outname)
                        ).parameters
                    ),
                },
                TAG_RETURN_TYPE: signature(
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

print("   * Building the signatures of the methods.")

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
        (
            f"{n}_{TAG_IN}"
            if n in IN_OUT_PARAMS else
            n
        ): str(s)
        for n, s in signs_in[TAG_PARAMS][TAG_IN].items()
    }

    for name_out, signs_out in methods.items():
        name = f"{name_in}2{name_out}"

        params = {
            'in' : params_in,
            'out': {
                (
                    f"{n}_{TAG_OUT}"
                    if n in IN_OUT_PARAMS else
                    n
                ): str(s)
                for n, s in signs_out[TAG_PARAMS][TAG_OUT].items()
                if n != 'nb'
            }
        }

        return_type = str(signs_out[TAG_RETURN_TYPE])
        return_type = cleantype(return_type)

# ! -- DEBUGGING -- ! #
        # print('---')
        # print(f"{name        = }")
        # print(f"{params      = }")
        # print(f"{return_type = }")
        # print()
        # exit()
# ! -- DEBUGGING -- ! #

        signatures[name] = {
            TAG_PARAMS     : params,
            TAG_RETURN_TYPE: return_type,
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
# print(list(signatures_sorted.keys()))
# from pprint import pprint
# pprint(signatures_sorted)
# exit()
# ! -- DEBUGGING -- ! #


# ---------- #
# -- CODE -- #
# ---------- #

print("   * Building the code of the methods.")

PARAMS_SEE_REF = {
# Inputs / Outputs.
    'bnb'      : "bnumeralsof",
    'bdigits'  : "frombdigits",
    'bnumerals': "checkbnumerals",
# Specs.
    'base': "bnumeralsof",
    'sep' : "bnumeralsof",
}

PARAMS_SEE_REF = {
    n: f"base2nat.{r}"
    for n, r in PARAMS_SEE_REF.items()
}

# ! -- DEBUGGING -- ! #
# from pprint import pprint
# pprint(PARAMS_SEE_REF)
# exit()
# ! -- DEBUGGING -- ! #

TEMP_METH_CODE = " "*4 + """
    def {name}(
        self,
        {params_all}
    ) -> {return_type}:
        return self.nat2base.{nat_2_YYY}(
            nb = self.base2nat.{XXX_2_nat}(
                {params_in}
            ),
            {params_out}
        )
""".strip()

code = []

for name, sign in signatures_sorted.items():
    XXX, YYY = name.split('2')

    XXX_2_nat = f"{XXX}2nat"
    nat_2_YYY = f"nat2{YYY}"

    see_return = seeat(
        ref     = f"nat2base.{nat_2_YYY}",
        useself = False
    )

    params       = defaultdict(dict)
    maxlen       = {}
    maxlen_proto = {}


    for tag in [TAG_IN, TAG_OUT]:
        tag_     = '_' + tag
        len_tag_ = len(tag_)

        maxlen[tag] = max(
            len(
                p[:-len_tag_]
                if p.endswith(tag_) else
                p
            )
            for p in sign[TAG_PARAMS][tag]
        )

        maxlen_proto[tag] = max(len(p) for p in sign[TAG_PARAMS][tag])

    maxlen_all = max(maxlen_proto.values())

    for tag in [TAG_IN, TAG_OUT]:
        tag_     = '_' + tag
        len_tag_ = len(tag_)

        for p, s in sign[TAG_PARAMS][tag].items():
            new_p  = p + ' '*(maxlen_proto[tag] - len(p))
            sign_p = p + ' '*(maxlen_all - len(p))

            if p.endswith(tag_):
                p = p[:-len_tag_]

            new_s = s.replace(f"{p}: ", f"{sign_p}: ")

            p = p + ' '*(maxlen[tag] - len(p))

            params[tag][(p, new_p)] = new_s


    params[TAG_PROTO] = []
    params[TAG_ALL]   = []

    for tag in [TAG_IN, TAG_OUT]:
        params[TAG_PROTO] += [
            prototype_param(
                param   = new_p + ' '*(maxlen_all - len(new_p)),
                ref     = PARAMS_SEE_REF[p.strip()],
                useself = False
            )
            for (p, new_p) in params[tag]
        ]

        params[TAG_ALL] += [
            f"{s},"
            for (p, new_p), s in params[tag].items()
        ]

        if tag == TAG_IN:
            tabu = TABU_METH_4

        else:
            tabu = TABU_METH_3

        params[tag] = tabu.join([
            f"{p} = {new_p.strip()},"
            for (p, new_p) in params[tag]
        ])

    params[TAG_PROTO] = TABU_PROTO.join(params[TAG_PROTO])


    unsorted_params_all = params[TAG_ALL].copy()
    params[TAG_ALL]     = []
    optional_params     = []

    for p in unsorted_params_all:
        if '=' in p:
            optional_params.append(p)

        else:
            params[TAG_ALL].append(p)

    params[TAG_ALL] += optional_params
    params[TAG_ALL]  = TABU_METH_2.join(params[TAG_ALL])


    method_code = TEMP_PROTOTYPE.format(
        see_params = params[TAG_PROTO],
        see_return = see_return,
    )

    method_code += "\n"

    method_code += TEMP_METH_CODE.format(
        name        = name,
        params_all  = params[TAG_ALL],
        XXX_2_nat   = XXX_2_nat,
        nat_2_YYY   = nat_2_YYY,
        return_type = sign[TAG_RETURN_TYPE],
        params_in   = params[TAG_IN],
        params_out  = params[TAG_OUT],
    )

# ! -- DEBUGGING -- ! # TEMP_METH_CODE
    # print('---')
    # print(name)
    # for tag in [TAG_IN, TAG_OUT, TAG_PROTO]:
    #     print()
    #     print(f"--- params[{tag}] ---")
    #     print(params[tag])
    # print(sign)
    # print()
    # print(method_code)
    # exit()
# ! -- DEBUGGING -- ! #

    code.append(method_code)


code = ("\n"*3).join(code)


# ------------------------ #
# -- PYTHON CODE UPDATE -- #
# ------------------------ #

print("   * Updating the Python code.")

with B2B_PYFILE.open(
    encoding = "utf-8",
    mode     = "r",
) as f:
    pycode = f.read()

before, _, after = between(
    text     = pycode,
    keepseps = True,
    seps     = [
        '# -- METHODS "AUTO" - START -- #',
        '# -- METHODS "AUTO" - END -- #'
    ],
)

pycode = f"""{before}

# Lines automatically build by the following file.
#
#     + ``{THIS_FILE_REL_SRC_PATH}``

{code}

{after}"""

# ! -- DEBUGGING -- ! #
# print(pycode)
# exit()
# ! -- DEBUGGING -- ! #

with B2B_PYFILE.open(
    encoding = "utf-8",
    mode     = "w",
) as f:
    f.write(pycode)
