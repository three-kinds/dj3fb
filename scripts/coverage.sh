#!/usr/bin/env bash

PACKAGE="dj3fb"

PACKAGE_PATH="$(dirname "$0")/.."
export PYTHONPATH=$PYTHONPATH:$PACKAGE_PATH
cd $PACKAGE_PATH

coverage erase
coverage run test_project/manage.py test test_project --debug-mode
coverage html --title="$PACKAGE coverage report"
python -m webbrowser ./htmlcov/index.html
