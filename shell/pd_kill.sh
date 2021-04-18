#!/bin/bash

prossname=price_dect
ps -aux | grep ${prossname} | grep -v grep |awk '{print $2}' | while read pid
do
	echo "front is running, to kill front pid=$pid"
	kill -9 $pid
	echo "kill result: $?"
done
