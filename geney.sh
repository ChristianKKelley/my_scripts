#!/usr/bin/env bash

filename = $1

awk '{print $1,$2,$3,$4,$5,$6,$7,$8}' | awk '$3=="gene"' | grep -v 'pseudogene' | less -S

