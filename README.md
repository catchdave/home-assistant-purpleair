## Local Purple Air Integration
This is an integration for home assistant that works integrates with local
polling on your PurpleAir devices on your local network.

_Code adapted from https://github.com/johnboiles/home-assistant-purpleair_

It creates one device per Purple Air device registered and several sensors
for each several readings.

***Still very much a work in progress***

### Installation

Simply copy the `/purpleair` directory in to your config's
`custom_components` directory (you may need to create it), add "purpleair:" to configuration.yaml, restart Home
Assistant, and add the integration via the UI (it's simple!).

To register a new purple air device, under Settings -> Integrations:
1. Add "Purple Air" Integration.
2. Enter the IP address of your local purple air device.
3. Give it a name.

#### Current Sensors
This will create 10 entities per device:
* Particulate Matter 0.1
* Particulate Matter 2.5
* Particulate Matter 10
* Air Quality Index (EPA)
* Air Quality Index (LRAPA)
* Humidity
* Temperature
* Dewpoint
* Pressure
* RSSI

Sensor data on PurpleAir is updated every 60 seconds.

This component is licensed under the MIT license, so feel free to copy,
enhance, and redistribute as you see fit.

## Releases

### 2.0.1
Replace public purple air device support (via purpleair.com) and replace
with purpleair devices that are on your local network only. 

### 1.1.0
Adds support for private hidden sensors and indoor sensors. Fixes #3 and #4.

### 1.0.0
Initial release (after versioning)
