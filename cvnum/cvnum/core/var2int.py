#!/usr/bin/env python3

###
# This module proposes just one class to convert one ¨python variable into
# useful representations of an integer.
###


from typing import *


# ---------------------------- #
# -- CONVERTING TO INTEGERS -- #
# ---------------------------- #

###
# This class can convert a "legal" integer into severla representations.
#
#
# note::
#     A "legal" integer is any ¨python variable ``varnb`` such that
#     ``int(str(varnb))`` is a ¨python ``int``.
###

class Var2Int:
###
# prototype::
#     mini       : the minimum value allowed for the integer representation
#                @ mini in RR or mini in {-inf, +inf}
#     maxi       : the maximum value allowed for the integer representation
#                @ maxi in RR or maxi in {-inf, +inf} ;
#                  mini <= maxi
#     tryconvert : to allow, or not, the use of the printed version of
#                  the ¨python variables such as to try to convert then to
#                  an integer
#     toremove   : a list of strings to remove in the string representation
#                  of the ¨python variables (this can be spaces, or digital
#                  separators for example).
#                @ len(toremove) >= 0 ;
#                  if   tryconvert = False
#                  then ignore(toremove)
#     errname    : the name used in case of error message
###
    def __init__(
        self,
        mini      : float     = float('-inf'),
        maxi      : float     = float('inf'),
        tryconvert: bool      = False,
        toremove  : List[str] = [],
        errname   : str       = "number",
    ) -> None:
        assert mini <= maxi, \
               f"invalid mini and maxi: ``{mini = } > {maxi = }``."

        self.mini       = mini
        self.maxi       = maxi
        self.tryconvert = tryconvert
        self.toremove   = toremove
        self.errname    = errname


###
# prototype::
#     varnb : either a ¨python integer if ``self.tryconvert = False``,
#             or any object that is printable as a "legal" integer after
#             removing the each text of the list ``self.toremove``
#           @ if   self.tryconvert = False
#             then varnb in ZZ
#             else str(varnb) in str(ZZ) ;
#
#     :return: a ¨python integer respecting the following constraints
#            @ return[1] = str(varnb) ;
#              return[0] = int(return[1]) ;
#              self.mini <= return[0] <= self.maxi
###
    def int_n_strify(self, varnb: Any) -> Tuple[int, str]:
# An integer ready to use.
        if isinstance(varnb, int):
            intnb = varnb
            strnb = str(varnb)

# Use of the string representation.
        else:
            assert self.tryconvert, \
                   (
                    f"the {self.errname} ``{str(varnb) = }`` is not an integer."
                     "\n"
                    f"Info: try to convert not allowed, and ``{varnb = }``."
                   )

            strnb = str(varnb)

# Remove spaces and decimal separators.
            for xtra in self.toremove:
                strnb = strnb.replace(xtra, '')

            try:
                intnb = int(strnb)

            except Exception:
                raise ValueError(
                    f"the {self.errname} ``{str(varnb) = }`` is not an integer."
                     "\n"
                    f"Infos: ``{varnb = }`` and ``{self.toremove = }``."
                )

# We have an integer. Is it in the good range?
        assert intnb >= self.mini, \
               f"the {self.errname} ``{varnb}`` is too small ({self.mini = })."

        assert intnb <= self.maxi, \
               f"the {self.errname} ``{varnb}`` is too big ({self.maxi = })."

# Thanks for using this method safely.
        return intnb, strnb


###
# prototype::
#     varnb : :see: self.int_n_strify
#
#     :return: the integer value of ``varnb`` build by ``self.int_n_strify``,
#              the sign of the "integer string" version of ``varnb`` or
#              an empty string if no sign ``+`` has been used, and the string
#              version of the absolute numerical value of ``str(nb)``
#            @ return[0] = int(str(varnb)) ;
#              return[2] = str(abs(return[0])) ;
#              if   return[0] < 0
#              then return[1] = '-'
#              else return[1] in ['', '+']
#
#     :see: self.int_n_strify
###
    def int_n_strsignabs(self, varnb: Any) -> Tuple[int, str, str]:
# ``int`` and ``str`` versions of ``varnb``.
        intnb, strnb = self.int_n_strify(varnb)

# A plus sign?
        if strnb[0] in "+-":
            sign  = strnb[0]
            strnb = strnb[1:]

        else:
            sign = ""

# Thanks for using this method safely.
        return intnb, sign, str(int(strnb))
