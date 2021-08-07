#!/bin/bash
FILE=links.txt
OUTPUTDIR=bruteforceout
MYVAR=""
let COUNT=0

cat $FILE | while read line
do
	echo $COUNT : $line
	MYVAR=`curl -I $line | grep 404`
	if [ "$MYVAR" != "" ]
	then
		echo not found
	else
		echo FOUND
	fi
	let "COUNT=COUNT+1"
	sleep 1
done
