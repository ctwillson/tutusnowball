#!/bin/bash
# crontab eg: 38 00 * * *  /home/ubuntu/stock/tutusnowball/shell/addkline_csv.sh
#put your token
export TS_TOKEN=''
#put your cookie
export export XUEQIULOGINCOOKIE=''
CURDIR=$(cd $(dirname ${BASH_SOURCE[0]}); pwd )
PYTHONDIR=$(which python)
$PYTHONDIR $CURDIR/../addkline_csv.py --all