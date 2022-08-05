#!/usr/bin/env python3

from collections import defaultdict
from inspect     import signature, _empty

from .protontype import *


# ------------------- #
# -- EXTRA METHODS -- #
# ------------------- #

# Some useful tags.
TAG_PARAMS   = 'params'
TAG_OPTIONAL = 'optional'
TAG_RETURN   = 'return'

TAG_TYPING  = 'typing'
TAG_DEFAULT = 'default'



def replace_int2nat(text):
    return text.replace('int', 'nat')

def replace_nat2int(text):
    return text.replace('nat', 'int')


TO_IGNORE = {
    'Nat2Base': ['numeralize'],
}

def cls_automethods(intcls, natcls):
    dircls = {
        n
        for n in dir(natcls)
        if not(
               n[0] == '_'
            or n.startswith('check')
            or n in TO_IGNORE[natcls.__name__]
            or replace_nat2int(n) in dir(intcls)
        )
    }

    return dircls


def easysignature(inst, methodname):
    sign = signature(inst.__getattribute__(methodname))

    easysign = {
        TAG_PARAMS    : {},
        TAG_OPTIONAL : [],
        TAG_RETURN    : cleantype(str(sign.return_annotation)),
    }

    for param, annotation in sign.parameters.items():
        _, param_type_default = str(annotation).split(':')

        param_type, *param_default = param_type_default.split('=')

        if param_default:
            param_default = param_default[0].strip()

            easysign[TAG_OPTIONAL].append(param)

        else:
            param_default = None

        easysign[TAG_PARAMS][param] = {
            TAG_TYPING : cleantype(param_type),
            TAG_DEFAULT: param_default,
        }

    return easysign
