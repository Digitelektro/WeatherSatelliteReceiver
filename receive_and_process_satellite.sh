#!/bin/bash

# $1 = Satellite Name
# $2 = Frequency
# $3 = FileName base
# $4 = TLE File
# $5 = EPOC start time
# $6 = Time to capture

currenttime=$(date +%H:%M)

if test "$1" = 'METEOR-M 2'; then
	python ~/weather/predict/meteor_rec.py ${2} $3.wav $6
    
	meteor_demod -s 120000  -f 128 -O 4 -b 50 -B $3.wav -o $3.s
    
	/usr/local/bin/meteordemod -t /home/pi/weather/predict/weather.tle -i $3.s -o /home/pi/weather/ -f jpg
    
    #if you want to remove decoded files to save place, uncomment these lines:
	#rm $3.s
	#rm $3.wav
else
	python ~/weather/predict/noaa_rec.py ${2} $3.wav $6
	
	PassStart=`expr $5 + 90`

	if [ -e $3.wav ]
	  then
		/usr/local/bin/wxmap -T "${1}" -H $4 -p 0 -l 0 -o $PassStart ${3}-map.png
		/usr/local/bin/wxtoimg -m ${3}-map.png -e ZA $3.wav $3-ZA.png
		/usr/local/bin/wxtoimg -m ${3}-map.png -e MSA $3.wav $3-MSA.png
		/usr/local/bin/wxtoimg -m ${3}-map.png -e MCIR $3.wav $3-MCIR.png
		/usr/local/bin/wxtoimg -m ${3}-map.png -e sea $3.wav $3-sea.png
		/usr/local/bin/wxtoimg -m ${3}-map.png -e therm $3.wav $3-therm.png
	fi
fi

