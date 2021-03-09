#!/bin/bash

ls
MAX=$(ls | awk '{print $1}' | grep -E '[0-9]{1,4}' | tail -1)
echo "max is: "
echo $MAX
ls | head -$MAX > album.txt
echo "album is: "
cat album.txt
