#!/usr/bin/env bash

#grep out the '>' stuff first

PLACE="$1"

echo $PLACE

myvar=`expr $PLACE / 81`
myvarl=`expr $myvar - 1`
myvarm=`expr $myvar + 1`
spot=$(($PLACE % 81))

echo $myvarl
echo $myvar
echo $myvarm
echo $spot

#make ugly

grep -v '>' | awk 'BEGIN{t=-1}{t = t + 1; {print t, $0}}' | grep "$myvarl\|$myvar\|$myvarm" > temp


