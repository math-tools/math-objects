#!/usr/bin/env python3

###
# This module proposes one class to convert naturals between two bases.
###


from typing import *

from .natconv  import NatConv
from .nat2base import Nat2Base
from .base2nat import Base2Nat


# ------------------------------ #
# -- NATURAL: BASE <~~~> BASE -- #
# ------------------------------ #

###
# This class gives an easy-to-use ¨api to convert naturals between two bases.
#
#
# warning::
#     If you only work with conversion from decimal writings to a base,
#     just work with the class ``nat2Base.Nat2Base``.
#     And if you only work with conversion from one base to decimal writings,
#     just work with the class ``base2nat.Base2Nat``.
###
class Base2Base(NatConv):
###
# prototype::
#     :see: NatConv.__init__
###
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.nat2base = Nat2Base(*args, **kwargs)
        self.base2nat = Base2Nat(*args, **kwargs)


# -- METHODS "AUTO" - START -- #

# Lines automatically build by the following file.
#
#     + ``tools/factory/convert/natural/build_02_formats_B2B.py``

###
# prototype::
#     bnb      : :see: base2nat.bnumeralsof
#     base_in  : :see: base2nat.bnumeralsof
#     sep_in   : :see: base2nat.bnumeralsof
#     base_out : :see: base2nat.bnumeralsof
#     sep_out  : :see: base2nat.bnumeralsof
#
#     :return: :see: nat2base.nat2bnb
###
    def bnb2bnb(
        self,
        bnb     : str,
        base_in : int,
        base_out: int,
        sep_in  : str = '',
        sep_out : str = '',
    ) -> str:
        return self.nat2base.nat2bnb(
            nb = self.base2nat.bnb2nat(
                bnb  = bnb,
                base = base_in,
                sep  = sep_in,
            ),
            base = base_out,
            sep  = sep_out,
        )


###
# prototype::
#     bdigits  : :see: base2nat.frombdigits
#     base_in  : :see: base2nat.bnumeralsof
#     base_out : :see: base2nat.bnumeralsof
#     sep_out  : :see: base2nat.bnumeralsof
#
#     :return: :see: nat2base.nat2bnb
###
    def bdigits2bnb(
        self,
        bdigits : List[int],
        base_in : int,
        base_out: int,
        sep_out : str = '',
    ) -> str:
        return self.nat2base.nat2bnb(
            nb = self.base2nat.bdigits2nat(
                bdigits = bdigits,
                base    = base_in,
            ),
            base = base_out,
            sep  = sep_out,
        )


###
# prototype::
#     bnumerals : :see: base2nat.checkbnumerals
#     base_in   : :see: base2nat.bnumeralsof
#     base_out  : :see: base2nat.bnumeralsof
#     sep_out   : :see: base2nat.bnumeralsof
#
#     :return: :see: nat2base.nat2bnb
###
    def bnumerals2bnb(
        self,
        bnumerals: List[str],
        base_in  : int,
        base_out : int,
        sep_out  : str = '',
    ) -> str:
        return self.nat2base.nat2bnb(
            nb = self.base2nat.bnumerals2nat(
                bnumerals = bnumerals,
                base      = base_in,
            ),
            base = base_out,
            sep  = sep_out,
        )


###
# prototype::
#     bdigits  : :see: base2nat.frombdigits
#     base_in  : :see: base2nat.bnumeralsof
#     base_out : :see: base2nat.bnumeralsof
#
#     :return: :see: nat2base.nat2bdigits
###
    def bdigits2bdigits(
        self,
        bdigits : List[int],
        base_in : int,
        base_out: int,
    ) -> List[int]:
        return self.nat2base.nat2bdigits(
            nb = self.base2nat.bdigits2nat(
                bdigits = bdigits,
                base    = base_in,
            ),
            base = base_out,
        )


###
# prototype::
#     bdigits  : :see: base2nat.frombdigits
#     base_in  : :see: base2nat.bnumeralsof
#     base_out : :see: base2nat.bnumeralsof
#
#     :return: :see: nat2base.nat2bnumerals
###
    def bdigits2bnumerals(
        self,
        bdigits : List[int],
        base_in : int,
        base_out: int,
    ) -> List[str]:
        return self.nat2base.nat2bnumerals(
            nb = self.base2nat.bdigits2nat(
                bdigits = bdigits,
                base    = base_in,
            ),
            base = base_out,
        )


###
# prototype::
#     bnb      : :see: base2nat.bnumeralsof
#     base_in  : :see: base2nat.bnumeralsof
#     sep_in   : :see: base2nat.bnumeralsof
#     base_out : :see: base2nat.bnumeralsof
#
#     :return: :see: nat2base.nat2bdigits
###
    def bnb2bdigits(
        self,
        bnb     : str,
        base_in : int,
        base_out: int,
        sep_in  : str = '',
    ) -> List[int]:
        return self.nat2base.nat2bdigits(
            nb = self.base2nat.bnb2nat(
                bnb  = bnb,
                base = base_in,
                sep  = sep_in,
            ),
            base = base_out,
        )


###
# prototype::
#     bnb      : :see: base2nat.bnumeralsof
#     base_in  : :see: base2nat.bnumeralsof
#     sep_in   : :see: base2nat.bnumeralsof
#     base_out : :see: base2nat.bnumeralsof
#
#     :return: :see: nat2base.nat2bnumerals
###
    def bnb2bnumerals(
        self,
        bnb     : str,
        base_in : int,
        base_out: int,
        sep_in  : str = '',
    ) -> List[str]:
        return self.nat2base.nat2bnumerals(
            nb = self.base2nat.bnb2nat(
                bnb  = bnb,
                base = base_in,
                sep  = sep_in,
            ),
            base = base_out,
        )


###
# prototype::
#     bnumerals : :see: base2nat.checkbnumerals
#     base_in   : :see: base2nat.bnumeralsof
#     base_out  : :see: base2nat.bnumeralsof
#
#     :return: :see: nat2base.nat2bdigits
###
    def bnumerals2bdigits(
        self,
        bnumerals: List[str],
        base_in  : int,
        base_out : int,
    ) -> List[int]:
        return self.nat2base.nat2bdigits(
            nb = self.base2nat.bnumerals2nat(
                bnumerals = bnumerals,
                base      = base_in,
            ),
            base = base_out,
        )


###
# prototype::
#     bnumerals : :see: base2nat.checkbnumerals
#     base_in   : :see: base2nat.bnumeralsof
#     base_out  : :see: base2nat.bnumeralsof
#
#     :return: :see: nat2base.nat2bnumerals
###
    def bnumerals2bnumerals(
        self,
        bnumerals: List[str],
        base_in  : int,
        base_out : int,
    ) -> List[str]:
        return self.nat2base.nat2bnumerals(
            nb = self.base2nat.bnumerals2nat(
                bnumerals = bnumerals,
                base      = base_in,
            ),
            base = base_out,
        )

# -- METHODS "AUTO" - END -- #
