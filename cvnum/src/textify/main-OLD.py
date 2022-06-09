#!/usr/bin/env python3

###
# This module proposes one class to name integers in several languages.
###

from typing import *

from .automata import *


# --------------------- #
# -- NAMING INTEGERS -- #
# --------------------- #

###
# This class can name integers in different languages.
###
class IntName(IntNameAutomata):
###
# prototype::
#     :return: the name build using a list of "small" numbers (concretly,
#              this name is the one expected without taking care of any sign)
###
    def _build_name_from_slices(self) -> str:
# Just zero to name.
        if(
            len(self._reversed_strslices) == 1
            and
            int(self._reversed_strslices[0]) == 0
        ):
            return self.nameofsmall('0')

# A none zero value to name.
        istart_grp = 0

        for i, smallnb in enumerate(self._reversed_strslices):
            print('---')

# We have to ignore intermediate zeros.
            if int(smallnb) != 0:
                print(self.nameofsmall(smallnb))

            nb_group_slice = i % self._groups_nb_slices - 1
            nb_of_biggrps  = i // self._groups_nb_slices - 1

            if nb_group_slice == -1 and nb_of_biggrps >= 0:
                istart_grp = i + 1

                spevar_grp_D = self._build_spevar(
                    i,
                    i + self._groups_nb_slices
                )
                spevar_grp_R = self._build_spevar(
                    0,
                    i
                )

                print('>>> NB OF OF  :', self._gene_big*nb_of_biggrps)

            else:
                spevar_grp_D = smallnb
                spevar_grp_R = self._build_spevar(
                    istart_grp,
                    i
                )

                print('>>> GROUP POWER:', self._groups_slices[nb_group_slice])


            print(f'{spevar_grp_D=}')
            print(f'{spevar_grp_R=}')


###
# prototype::
#     start : the start position in ``self._reversed_strslices``
#     end   : just after the end in ``self._reversed_strslices``
#
#     :return: the string representation of the number obtained by concatening,
#              in the good order, the slicesfrom position ``start`` to the
#              position just before ``end``.
###
    def _build_spevar(
        self,
        start: int,
        end  : int
    ) -> str:
        return "".join(
            reversed(
                self._reversed_strslices[start: end]
            )
        )


###
# prototype::
#     intnb : an integer to slice respecting the groups used by the
#             language ``self.lang``
#           @ intnb >= 0
#
#     :return: a list of string slices following the specifications of
#              groups for the language ``self.lang``
###
    def _build_reverse_strslices(self, intnb: int) -> List[str]:
        slices = []

        iprev  = 0

        for i in self._groups_slices:
            delta_i     = i - iprev
            iprev       = i
            powerofbase = 10**(delta_i)

# We need to fill with zeros (for groups with zero number).
            strnb = str(intnb % powerofbase).zfill(delta_i)

            slices.append(strnb)

            intnb = intnb // powerofbase

            if intnb == 0:
                break

# We have to continue recursively.
        if intnb != 0:
            slices += self._build_reverse_strslices(intnb)

# Nothing more left to do.
        return slices
