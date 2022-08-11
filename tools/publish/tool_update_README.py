#!/usr/bin/env python3

from json import load

from multimd import Builder

from mistool.os_use    import PPath as Path
from orpyste.data      import ReadBlock
from orpyste.parse.ast import ASTError


# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

MONOREPO_DIR = Path(__file__).parent

while(MONOREPO_DIR.name != 'math-objects'):
    MONOREPO_DIR = MONOREPO_DIR.parent

ABOUT_MONOREPO = MONOREPO_DIR / 'about.peuf'

README_PROJECTS = MONOREPO_DIR / 'readme' / 'projects.md'


TEMPLATE_README_SINGLE = """
Just one project in this monorepo
---------------------------------

For the moment, there is just **{project} v-{version} [{date}]** .

  * **Description:** {desc}
""".strip()


TEMPLATE_README_SEVERAL = """
Projects in this monorepo
-------------------------

  1. **{project} v-{version} [{date}]** : {desc}
""".strip()


# ------------------ #
# -- THE PROJECTS -- #
# ------------------ #

print(f"   * Analyzing the ``about.peuf`` of the monorepo.")

try:
    with ReadBlock(
        content = ABOUT_MONOREPO,
        mode    = {"verbatim": 'projects'}
    ) as datas:
        about = datas.mydict("std nosep nonb")

except ASTError:
    raise ValueError(
        'invalid ``about.peuf`` for the monorepo.'
    )

projects = list(about['projects'])
projects.sort()


# --------------------------- #
# -- ABOUT OF EACH PROJECT -- #
# --------------------------- #

print(f"   * Extracting infos from ``about.peuf`` of each project.")

about_projects = []

for oneproj in projects:
    print(f"      + Project ``{oneproj}``.")

    try:
        with ReadBlock(
            content = MONOREPO_DIR / oneproj / 'about.peuf',
            mode    = {"keyval::=": 'general'}
        ) as datas:
            about = datas.mydict("std nosep nonb")

    except ASTError:
        raise ValueError(
            f'invalid ``about.peuf`` for the project ``{oneproj}``.'
        )

    about = about['general']

    with (MONOREPO_DIR / oneproj / 'VERSION.json').open(
        encoding = "utf-8",
        mode     = "r",
    ) as f:
        version = load(f)

    about_projects.append(about)


# ------------------- #
# -- UPDATE README -- #
# ------------------- #

print(f"   * Updating the README file.")

if len(about_projects) == 1:
    template = TEMPLATE_README_SINGLE
else:
    template = TEMPLATE_README_SEVERAL

content = []

for about in about_projects:
    desc = about['desc']
    desc = desc[0].lower() + desc[1:]

    project = about['project']
    project = f"[{project}]({project}/README.md)"

    date = '-'.join(version['date'].values())

    content.append(
        template.format(
            project = project,
            desc    = desc,
            version = version['full'],
            date    = date,
        )
    )
    content.append('')

content = '\n'.join(content)

with README_PROJECTS.open(
    encoding = "utf-8",
    mode     = "w",
) as f:
    f.write(content)

mybuilder = Builder(
    output  = Path('README.md'),
    content = Path('readme'),
)

mybuilder.build()
