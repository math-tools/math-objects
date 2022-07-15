#!/usr/bin/env python3

from .config import *


def usecases_deps(dirlang):
    rulestoignore = langdefs(dirlang)
    dependencies  = list(extend_deps(rulestoignore))

    # Just keep the tags useful for testing.
    for specs in rulestoignore.values():
        tags = list(specs)

        for onetag in tags:
            if not onetag in TAGS_FOR_IGNORED_TESTS:
                del specs[onetag]
                continue

            if onetag == DSL_SPECS_IGNORE_SMALL:
                specs[onetag] = [
                    pattern
                    for kind, pattern in specs[onetag]
                    if kind == DSL_ACTION_MATCHING
                ]

    return rulestoignore, dependencies


def usecases_files(
    dirlang,
    dependencies
):
    usecases_paths = {}
    withspecial    = []

    for onepath in dirlang.walk("dir::*"):
        shortpath = onepath - dirlang

        if shortpath.depth != 1:
            continue

        mainlang = shortpath.parent.name
        mainlang = mainlang.lower()
        variant  = shortpath.name
        lang     = taglang(mainlang, variant)

        usecases_lang = defaultdict(list)

        path_usecases_int = onepath / "usecases" / "integers"

        assert path_usecases_int.is_dir(), \
            (
                "Missing folder ``usecases/integers`` "
                f"in ``{mainlang}/{variant}``."
            )

        for onefile in path_usecases_int.walk("file::**.txt"):
            kind = onefile - path_usecases_int
            kind = str(kind.parent)

            # usecases_lang[kind].append(onefile.name)
            usecases_lang[kind].append(onefile)

        for kind, filesfound in usecases_lang.items():
            if kind == EMPTY_PATH:
                assert (
                        len(usecases_lang[EMPTY_PATH]) == 1
                        and
                        usecases_lang[EMPTY_PATH][0].name == SPECIAL_FILE
                       ), (
                        f"only the file ``{SPECIAL_FILE}`` can be used "
                        "directly in the folder ``usecases/integers``."
                       )

                assert not lang in dependencies, \
                       (
                        f"the file ``{SPECIAL_FILE}`` can't be used "
                        f"with ``{lang}`` which has some deps."
                       )

                usecases_lang[kind] = filesfound
                withspecial.append(lang)

            else:
                assert kind in KINDS_FOR_TESTS, \
                    f"unkown kind ``{kind}`` not in {KINDS_FOR_TESTS}"

                usecases_lang[kind] = sorted(
                    filesfound,
                    # key = lambda x: (len(x), x)
                    key = lambda x: (len(x.name), x.name)
                )

        usecases_paths[lang] = usecases_lang

    return usecases_paths, withspecial


def nobig_langs(dirlang):
    langs_nobig = []

    all_langs = langdefs(dirlang)

    for lang, specs in all_langs.items():
        if not DSL_SPECS_GENE in specs:
            continue

        if specs[DSL_SPECS_GENE][DSL_TAG_GENE_BIG] is None:
            langs_nobig.append(lang)

    return langs_nobig
