#!/usr/bin/env bash

spot=$1                         # assigned to "10051" or whatever
awk -v spot="$spot" '!/^>/ {
    amount += length
    if (amount >= spot) {
        print(prev substr($0, 1, spot - (amount - length)))
        exit
    }
    prev = $0 RS
}'
