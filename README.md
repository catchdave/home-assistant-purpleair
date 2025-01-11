## Local Purple Air Integration
This is an integration for home assistant that works integrates with local
polling on your PurpleAir devices on your local network.

_Code adapted from https://github.com/johnboiles/home-assistant-purpleair_

It creates one device per Purple Air device registered and several sensors
for each several readings.

### Installation

Simply copy the `/purpleair` directory in to your config's
`custom_components` directory (you may need to create it), restart Home
Assistant, and add the integration via the UI (it's simple!).

To register a new purple air device:
1. Add "Purple Air" Integration.
2. Enter the IP address of your local purple air device
3. Give it a name.

#### Current Sensors
This will create 12 or 13 entities per device:
* Particulate Matter 0.1
* Particulate Matter 2.5
* Particulate Matter 10
* Air Quality Index (EPA)
* Air Quality Index (LRAPA)
* Humidity (Adjusted sensor: +4%)
* Temperature (Adjusted sensor: -8F)
* Dewpoint (Adjusted sensor: re-calculated to take temp & humidity adjustments)
* Pressure
* RSSI
* Particulate Matter 2.5 Aqi Raw value (sensor A)
* Particulate Matter 2.5 Aqi Raw value (sensor B -- only for devices that have two)
* PM 2.5 Confidence Level (Good, Questionable or Severe).

Sensor data on PurpleAir is updated every 60 seconds.

##### Adjusted Sensors
In a similar manner to the actual purple air website, some sensors are adjusted manually to take into
account the fact that the housing itself increases the temperature and has reduced humidity. Calculated
sensors are marked above.

This component is licensed under the MIT license, so feel free to copy,
enhance, and redistribute as you see fit.

## Releases

### 2.0.5
Updated to match Home Assistant's new device constants in 2025

### 2.0.3
Added support for dual sensor devices that have a physical issue with one sensor. If a device has dual sensors and one of them is > 300 difference, it will set the confidence to "Severe" and instead of averaging the values, will use the lower value exclusively.

### 2.0.1
Replace public purple air device support (via purpleair.com) and replace
with purpleair devices that are on your local network only. 

### 1.1.0
Adds support for private hidden sensors and indoor sensors. Fixes #3 and #4.

### 1.0.0
Initial release (after versioning)
