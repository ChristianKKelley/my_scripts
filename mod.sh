#!/usr/bin/env bash

VAR = $1
cat ~/Biology/project/genomes/lengths | grep "$1" | awk '{print $2}'

ls | grep 'GCF'

#cat GCF... | awk '{print $1,$2,$3,$4,$5,$6,$7,$8}' | grep 'gene' | grep -v 'pseudogene' | awk '{print $4}' > filename
