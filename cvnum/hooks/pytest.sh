#!/bin/sh

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$THIS_DIR/../tests"
pytest ./ || exit 1
