#!/bin/bash


for eachfile in `ls ./*.txt`; do
   ./convWeatherData.sh $eachfile
done

exit 0
