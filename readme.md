# Weather satellite receiving automation scripts for raspberry PI

These bash scripts are based on [https://www.instructables.com/Raspberry-Pi-NOAA-Weather-Satellite-Receiver/](this) tutorial.

I slighty modified the scripts to use an Airspy receiver and use GNU radio flowgraph to record raw data. I also added METEOR M2 support. 

The GNU radio flowgraphs can be found in the grc folder, the generated python scripts is modified to be able to use it with input parameters.

The METEOR demodulator can be found [https://github.com/Digitelektro/MeteorDemod](here).

## Prerequisites
Other dependencies that the forementioned tutorial does not include must be installed:

 - GNU radio
 - Airspy driver
 - OSMOCOM source with airspy support
 - [https://github.com/dbdexter-dev/meteor_demod](meteor_demod)