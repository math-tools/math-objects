#!/usr/bin/env python3

import json
from string import digits

from .config import *


SPACES_FOR_INT = " _"
CHARS_FOR_INT  = set(digits + SPACES_FOR_INT + "+-*")

def localintify(txtexopr):
    memo_txtexopr = txtexopr

    assert set(txtexopr) <= CHARS_FOR_INT, \
           f"illegal chars found inside ``{memo_txtexopr}``."

    for s in SPACES_FOR_INT:
        txtexopr = txtexopr.replace(s, '')

    try:
        intval = eval(txtexopr)

    except Exception:
        raise ValueError(
            f"``{memo_txtexopr}`` can't be evaluated to an integer."
        )

    if memo_txtexopr.strip()[0] == '+':
        intval = f"+{intval}"

    return str(intval)


def buildjson(kind, onepath):
    jsoncode = []

    if kind == EMPTY_PATH:
        where = SPECIAL_FILE

    else:
        where = f"{kind}/{onepath.name}"

    key = val = ''

    for oneline in onepath.read_text().splitlines():
        oneline = oneline.strip()

        if not oneline:
            continue

        if not '=' in oneline:
            val += ' ' + oneline

        else:
            if val:
                jsoncode.append({
                    'where'  : where,
                    'integer': localintify(key),
                    'initial': key,
                    'name'   : val,
                })

            key, _, val = oneline.partition('=')

            key = key.strip()
            val = val.strip()

    if val:
        jsoncode.append({
            'where'  : where,
            'integer': localintify(key),
            'initial': key,
            'name'   : val,
        })

    return jsoncode


def buildtests_json(
    lang,
    testdir,
    usecases,
):
    json_tests    = []

    for kind in [EMPTY_PATH] + KINDS_FOR_TESTS:
        for onepath in usecases[kind]:
            json_tests += buildjson(kind, onepath)

    with (testdir / f"{lang}.json").open(
        encoding = "utf-8",
        mode     = "w",
    ) as f:
        f.write(
            f"{json.dumps(json_tests)}"
             "\n"
        )
