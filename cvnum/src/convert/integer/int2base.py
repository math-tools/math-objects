#!/usr/bin/env python3

###
# This module converts decimal writings into specific base writings.
###


from typing import *

from math import (
    ceil,
    log
)

from .intconv import IntConv


# -------------------------------- #
# -- DECIMAL ~~~> SPECIFIC BASE -- #
# -------------------------------- #

class Int2Base(IntConv):
###
# prototype::
#     :see: ``common.BaseConverter.__init__``
###
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


###
# prototype::
#     varnb : :see: tbox.var2int.Var2Int.int_n_strify
#
#     :return: the sign, and the list of textual decimal digits of ``nb``
#              from the biggest weight to the smallest one
#            @ v in return[1] ==> v in str(0..9)
###
    def intnumerals(self, varnb: Any) -> Tuple[str, List[str]]:
# Is ``nb`` a natural ?
        _, sign, strnb = self.legalint.int_n_strsignabs(varnb)

# We can do the conversion.
        return sign, [d for d in strnb]


###
# prototype::
#     varnb : :see: tbox.var2int.Var2Int.int_n_strify
#
#     :return: the sign, and the list of decimal digits of ``nb``, the digits
#              beeing sorted from the biggest weight to the smallest one
#            @ v in return[1] ==> v in 0..10
###
    def intdigits(self, varnb: Any) -> List[int]:
# Is ``nb`` a natural ?
        _, sign, strnb = self.legalint.int_n_strsignabs(varnb)

# We can do the conversion.
        return sign, [int(d) for d in strnb]


###
# prototype::
#     varnb   : :see: tbox.var2int.Var2Int.int_n_strify
#     varbase : :see: tbox.var2int.Var2Int.int_n_strify
#             @ int(str(varbase)) > 1
#
#     :return: the sign, and the list of integer digits of ``varnb`` converted
#              into the base ``varbase``, the digits beeing sorted from
#              the biggest weight to the smallest one
#            @ v in return[1] ==> v in 0 .. (base-1)
#
#
# note::
#     The name ``int2bdigits`` comes from "integer to base digits".
###
    def int2bdigits(
        self,
        varnb  : Any,
        varbase: Any,
    ) -> List[int]:
# Is ``nb`` a natural ?
        intnb, sign, _ = self.legalint.int_n_strsignabs(varnb)

# Is ``base`` a natural greater than one ?
        intbase, _ = self.legalint.int_n_strify(varbase)

# Let's go.
        bdigits = []

        if intnb == 0:
            bdigits = [0]

        else:
            while(intnb):
                bdigits.append(intnb % intbase)
                intnb = intnb // intbase

            bdigits.reverse()

        return sign, bdigits


###
# prototype::
#     base : the base used to write a natural integer
#          @ base in 2 .. +inf  {not checked}
#
#     :return: a function that converts a ``base`` integer digit into
#              a textual numeral.
#
#
# warning::
#     This method is an internal one even if we let it public.
###
    def numeralize(self, base: int) -> Callable[[int], str]:
    # Number of characters needed to code one single digit.
        max_singledigit = 36

        if base > max_singledigit:
            nbchars = ceil(log(base) / log(max_singledigit))

        else:
            nbchars = 1

    # Internal functions
        def alphanum_single(
            x      : int,
            padding: bool = True
        ) -> str:
    # We need more than one character.
            if x >= max_singledigit:
                result = "".join(
                    alphanum_single(
                        x       = d,
                        padding = False
                    )
                    for d in self.int2bdigits(
                        varnb   = x,
                        varbase = max_singledigit,
                    )[1]
                )

    # One single decimal numeral.
            elif x < 10:
                result = str(x)

    # One single upper case letter.
            else:
    # 65 - 10 = 55
                result = chr(55 + x)

    # Padding or not padding? That is the question...
            if padding:
                result = result.rjust(nbchars, '0')

            return result


        def alphanum(nb: int) -> str:
            coding = list(
                map(
                    alphanum_single,
                    self.int2bdigits(
                        varnb   = nb,
                        varbase = base,
                    )[1]
                )
            )

            return coding

    # We return the coding function.
        return alphanum


###
# prototype::
#     varnb   : :see: tbox.var2int.Var2Int.int_n_strify
#     varbase : :see: tbox.var2int.Var2Int.int_n_strify
#             @ int(str(varbase)) > 1
#
#     :return: the sign, and the list of textual numerals of ``nb`` converted
#              into the base ``base``, the numerals beeing sorted from
#              the biggest weight to the smallest one
#
#     :see: numeralize
#
#
# note::
#     The name ``int2bdigits`` comes from "integer to base numerals".
###
    def int2bnums(
        self,
        varnb  : Any,
        varbase: Any,
    ) -> List[int]:
# Is ``nb`` a natural ?
        intnb, sign, strabsnb = self.legalint.int_n_strsignabs(varnb)

# Is ``base`` a natural greater than one ?
        intbase, _ = self.legalint.int_n_strify(varbase)

        return sign, self.numeralize(intbase)(int(strabsnb))


###
# prototype::
#     varnb   : :see: tbox.var2int.Var2Int.int_n_strify
#     varbase : :see: tbox.var2int.Var2Int.int_n_strify
#             @ int(str(varbase)) > 1
#     sep     : the text that will be used if needed to separate numerals
#               using at least two digits (that is the case when the base
#               is bigger than 36)
#
#     :return: an easy-to-read string version of ``nb`` converted into
#              the base ``base``
#
#     :see: int2bnumerals ,
#           ./dec2base.bnb2int
#
#
# note::
#     The name ``int2bnb`` comes from "integer to base number".
###
    def int2bnb(
        self,
        varnb  : int,
        varbase: int,
        sep : str = "."
    ) -> str:
# Is ``nb`` a natural ?
        intnb, sign, strabsnb = self.legalint.int_n_strsignabs(varnb)

# Is ``base`` a natural greater than one ?
        intbase, _ = self.legalint.int_n_strify(varbase)

        if intbase < 37:
            sep = ""

        sign, numerals = self.int2bnumerals(
            varnb   = strabsnb,
            varbase = varbase,
        )

        return sign + sep.join(numerals)
