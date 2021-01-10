#!/bin/bash

# Update Satellite Information
wget -qr https://www.celestrak.com/NORAD/elements/weather.txt -O /home/pi/weather/predict/weather.txt
grep "NOAA 15" /home/pi/weather/predict/weather.txt -A 2 > /home/pi/weather/predict/weather.tle
grep "NOAA 18" /home/pi/weather/predict/weather.txt -A 2 >> /home/pi/weather/predict/weather.tle
grep "NOAA 19" /home/pi/weather/predict/weather.txt -A 2 >> /home/pi/weather/predict/weather.tle
grep "METEOR-M 2" /home/pi/weather/predict/weather.txt -A 2 >> /home/pi/weather/predict/weather.tle
grep "METEOR-M2 2" /home/pi/weather/predict/weather.txt -A 2 >> /home/pi/weather/predict/weather.tle


#Remove all AT jobs
for i in `atq | awk '{print $1}'`;do atrm $i;done

#delete old files older than x days to save place
find /home/pi/weather/ -type f -name '*.png' -mtime +30 -exec rm -f {} \;
find /home/pi/weather/ -type f -name '*.bmp' -mtime +5 -exec rm -f {} \;
find /home/pi/weather/ -type f -name '*.jpg' -mtime +30 -exec rm -f {} \;
find /home/pi/weather/ -type f -name '*.wav' -mtime +5 -exec rm -f {} \;
find /home/pi/weather/ -type f -name '*.s' -mtime +5 -exec rm -f {} \;


#Schedule Satellite Passes:
/home/pi/weather/predict/schedule_satellite.sh "NOAA 19" 137.1000
/home/pi/weather/predict/schedule_satellite.sh "NOAA 18" 137.9125
/home/pi/weather/predict/schedule_satellite.sh "NOAA 15" 137.6200
/home/pi/weather/predict/schedule_satellite.sh "METEOR-M 2" 137.103



