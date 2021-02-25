#!/bin/bash
CURDIR=$(cd $(dirname ${BASH_SOURCE[0]}); pwd )
PYTHONDIR=$(which python)
$PYTHONDIR $CURDIR/../addkline_csv.py --all