#!/bin/bash

FILENAME=$1
count=0
cat $FILENAME | while read LINE
do
	let count++
	echo "$count $LINE"
done
echo -e "\n Total $count Lines read"
