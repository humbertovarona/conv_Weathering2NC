#!/bin/bash

FULLNAME=$(basename "$1")
FILENAME=${FULLNAME%.*}
EXT=${FULLNAME##*.}
OUTPUTFN="$FILENAME-1.$EXT"
#echo $OUTPUTFN

awk 'BEGIN{FS=" ";}{print $1";"$2";"$3";"$4";"$5";"$6";"$7;}' $1 > $OUTPUTFN

mv -f $OUTPUTFN $1

exit 0
