
#!/usr/bin/env python3

from cbdevtools         import *
from mistool.os_use     import PPath
from mistool.string_use import between

from core.templates    import *
from core.xtra_methods import *

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
CV_DIR_NAT = SRC_DIR / "convert" / "integer"

PYFILES = {
    name: CV_DIR_NAT / f"{name}.py"
    for name in [
        "int2base",
        "base2int",
        "base2base",
    ]
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

from src.convert.natural import Nat2Base, Base2Nat, Base2Base as NatBase2Base
from src.convert.integer import Int2Base, Base2Int, Base2Base


TAG_INT_CLS = "int_cls"
TAG_NAT_CLS = "nat_cls"

CLASSES = {
    ic.__name__.lower() : {
        TAG_INT_CLS: ic,
        TAG_NAT_CLS: nc,
    }
    for ic, nc in [
        (Int2Base, Nat2Base),
        (Base2Int, Base2Nat),
        (Base2Base, NatBase2Base)
    ]
}


# --------------- #
# -- TEMPLATES -- #
# --------------- #

TAG_SELF     = "self."
LEN_TAG_SELF = len(TAG_SELF)

TEMP_METH_CODE = " "*4 + """
    @deco_callof(tocall = {tag_tocall},
                 {params_deco})
    def {methodname}(
        self,
        {params_xtra}
    ) -> {return_type}:
        ...
""".strip()


SEE_REFS = {
    'int2base': {
        p: (True, r)
        for p, r in {
            'digits'    : "fromdigits",
            'numerals'  : "fromnumerals",
            'nb'        : "numeralsof",
            'bnb'       : "int2bnb",
            'base'      : "int2bnb",
            'sep'       : "int2bnb",
            'bdigits'   : "int2bdigits",
            'bnumerals' : "int2bnumerals",
        }.items()
    }
}


SEE_REFS['base2int'] = {
    p: (False, f"integer.int2base.{r}")
    for p, (_, r) in SEE_REFS['int2base'].items()
}

SEE_REFS['base2int']['nat'] = (True, "bdigits2int")


SEE_REFS['base2base'] = {
    p: (
        (False, f"integer.base2int.{r}")
        if s else
        (s, r)
    )
    for p, (s, r) in SEE_REFS['base2int'].items()
    if p not in ['base', 'sep']
}

for p in ['base', 'sep']:
    s, r = SEE_REFS['base2int'][p]

    for suffix in ['in', 'out']:
        SEE_REFS['base2base'][f"{p}_{suffix}"] = (
            (False, f"integer.base2int.{r}")
            if s else
            (s, r)
        )


# ! -- DEBUGGING -- ! #
# from pprint import pprint
# pprint(SEE_REFS['base2base'])
# exit()
# ! -- DEBUGGING -- ! #

# ----------------------- #
# -- METHODS AVAILABLE -- #
# ----------------------- #

for modulename, pyfile in PYFILES.items():
    nat_modulename = replace_int2nat(modulename)

    theclasses = CLASSES[modulename]
    intcls     = theclasses[TAG_INT_CLS]
    natcls     = theclasses[TAG_NAT_CLS]
    natinst    = natcls()

    print(f"   * Module ``{modulename}``")
    print( "       + Building the extra methods.")

# ! -- DEBUGGING -- ! #
    # print(f"{dir(intcls) = }")
    # print(f"{dir(natcls) = }")
# ! -- DEBUGGING -- ! #

    easyinfos = {
        name: easysign(natinst.__getattribute__(name))
        for name in cls_automethods(
            intcls,
            natcls,
        )
    }

# ! -- DEBUGGING -- ! #
    # print("\n".join(list(easyinfos.keys())))
    # from pprint import pprint;pprint(easyinfos)
    # exit()
# ! -- DEBUGGING -- ! #


# ------------------------ #
# -- PYTHON CODE UPDATE -- #
# ------------------------ #

    print("       + Updating the Python code.")

    auto_code = []

    for methodname in sorted(easyinfos):
        infos   = easyinfos[methodname]
        allrefs = SEE_REFS[modulename]


        see_params = build_see_params(
            about_params = infos[TAG_PARAMS],
            refs         = allrefs,
        )
        see_params = TABU_PROTO.join(see_params)


# ! -- DEBUGGING -- ! #
        # print(f"--- {methodname} ---")
        # print(f"{build_return_ref(methodname)  = }")
        # print()
        # exit()
# ! -- DEBUGGING -- ! #


        return_refs = allrefs[
            build_return_ref(methodname)
        ]


        see_return = seeat(
            ref     = return_refs[1],
            useself = return_refs[0]
        )


        tag_tocall = nat_modulename

        for toremove in ['at', 'ase']:
            tag_tocall = tag_tocall.replace(toremove, '')

        tag_tocall = tag_tocall.upper()
        tag_tocall = f"DECO_TAG_{tag_tocall}"


        params_deco = ', '.join(
            f"DECO_TAG_{p.upper()}"
            for p in infos[TAG_PARAMS]
        )
        params_deco = [f"params = [{params_deco}]"]

        if infos[TAG_OPTIONAL]:
            params_deco[0] = params_deco[0].replace(
                "params = [",
                "params   = ["
            #   "optional = [
            ) + ","

            optional_deco = ', '.join(
                f"DECO_TAG_{p.upper()}"
                for p in infos[TAG_OPTIONAL]
            )
            optional_deco = f"optional = [{optional_deco}]"

            params_deco.append(optional_deco)

            spaceafter_tocall = ' '*(len("optional") - len("tocall"))

        else:
            spaceafter_tocall = ''

        params_deco = TABU_DECO.join(params_deco)


        params_xtra = build_method_params(infos[TAG_PARAMS])
        params_xtra = TABU_METH_2.join(params_xtra)

# ! -- DEBUGGING -- ! #
        # print(f"--- {methodname} ---")
        # print(f"{see_params  = }")
        # print(f"{see_return  = }")
        # print(f"{params_deco = }")
        # print(f"{params_xtra = }")
        # print()
        # exit()
# ! -- DEBUGGING -- ! #

        code_prototype = TEMP_PROTOTYPE.format(
            see_params = see_params,
            see_return = see_return,
        )

        code_meth = TEMP_METH_CODE.format(
            tag_tocall  = tag_tocall,
            params_deco = params_deco,
            methodname  = replace_nat2int(methodname),
            params_xtra = params_xtra,
            return_type = infos[TAG_RETURN],
        )

        if spaceafter_tocall:
            code_meth = code_meth.replace(
                 "@deco_callof(tocall =",
                f"@deco_callof(tocall{spaceafter_tocall} ="
            )

        auto_code.append(f"{code_prototype}\n{code_meth}")

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

    auto_code = ("\n"*3).join(auto_code)

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

{auto_code}

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
