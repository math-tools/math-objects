#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

import json

from mistool.os_use import PPath


# ------------------------------------------ #
# -- MODULE TESTED IMPORTED FROM SOURCES! -- #
# ------------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'cvnum',
)


# ----------------------- #
# -- GENERAL CONSTANTS -- #
# ----------------------- #

THIS_DIR  = PPath(__file__).parent
DATAS_DIR = THIS_DIR / "datas-lang"

READ_SECTION_CLASS = section.Read


# --------------- #
# -- CLEANINGS -- #
# --------------- #

def test_data_read_all():
    for jsonpath in DATAS_DIR.walk("file::read/**.json"):
        with jsonpath.open() as f:
            mode = json.load(f)

        with jsonpath.with_ext("txt").open(
            encoding = "utf-8",
            mode     = "r"
        ) as f:
            output = f.read().strip()

        with READ_SECTION_CLASS(
            content = jsonpath.with_ext("peuf"),
            mode    = mode
        ) as data_infos:
            outputfound = []

            for oneinfo in data_infos:
                if oneinfo.isblock():
                    outputfound.append(
                        'QUERYPATH:{0}'.format(oneinfo.querypath)
                    )
                    outputfound.append(
                        'MODE:{0}'.format(oneinfo.mode)
                    )

                elif oneinfo.isdata():
                    outputfound.append('{0}'.format(oneinfo.rtu))

            outputfound = "\n".join(outputfound)

        assert output == outputfound
