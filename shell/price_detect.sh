#!/bin/bash
# crontab eg: 38 00 * * *  /home/ubuntu/stock/tutusnowball/shell/addkline_csv.sh
#put your token
export TS_TOKEN=''
#put your cookie
export XUEQIULOGINCOOKIE=''
#put your pushplus
export PUSHPLUSTOKEN=''
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
CURDIR=$(cd $(dirname ${BASH_SOURCE[0]}); pwd )
PYTHONDIR=$(which python)
$PYTHONDIR $CURDIR/../price_dect.py