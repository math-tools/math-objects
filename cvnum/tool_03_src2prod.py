#!/usr/bin/env python3

from pathlib import *

from src2prod import *

THIS_DIR = Path(__file__).parent

README_DIR = 'readme'
SOURCE_DIR = 'src'
TARGET_DIR = 'cvnum'

project = Project(
    # safemode = False,
    project  = THIS_DIR,
    source   = 'src',
    target   = 'cvnum',
    ignore   = '''
        tool_*/
        tool_*.*
    ''',
    usegit = True,
    readme = 'readme',
)

project.update()
