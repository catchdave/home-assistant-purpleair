"""Constants for the Purple Air integration."""

from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import (
    PERCENTAGE,
    SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    UnitOfPressure,
    UnitOfTemperature,
)

# fmt: off
AQI_BREAKPOINTS = {
    'pm2_5': [
        { 'pm_low': 500.5, 'pm_high': 999.9, 'aqi_low': 501, 'aqi_high': 999 },
        { 'pm_low': 350.5, 'pm_high': 500.4, 'aqi_low': 401, 'aqi_high': 500 },
        { 'pm_low': 250.5, 'pm_high': 350.4, 'aqi_low': 301, 'aqi_high': 400 },
        { 'pm_low': 150.5, 'pm_high': 250.4, 'aqi_low': 201, 'aqi_high': 300 },
        { 'pm_low':  55.5, 'pm_high': 150.4, 'aqi_low': 151, 'aqi_high': 200 },
        { 'pm_low':  35.5, 'pm_high':  55.4, 'aqi_low': 101, 'aqi_high': 150 },
        { 'pm_low':  12.1, 'pm_high':  35.4, 'aqi_low':  51, 'aqi_high': 100 },
        { 'pm_low':     0, 'pm_high':  12.0, 'aqi_low':   0, 'aqi_high':  50 },
    ],
}
PARTICLE_PROPS = ['pm1_0_atm', 'pm2_5_atm', 'pm10_0_atm']
# fmt: on

# fmt: off
# Map of sensors to create entities for
SENSORS_MAP = {
    'pm2_5_aqi_a_raw':         {'key': 'pm2_5_aqi_raw',    'uom': SensorDeviceClass.AQI,              'icon': 'mdi:blur-linear'},
    'pm2_5_aqi_b_raw':         {'key': 'pm2_5_aqi_b_raw',  'uom': SensorDeviceClass.AQI,              'icon': 'mdi:blur-linear'},
    'pm2_5_atm_confidence':    {'key': 'pm2_5_atm_conf',   'uom': None,                               'icon': 'mdi:seal'},
    'particulate_matter_0_1':  {'key': 'pm1_0_atm',        'uom': SensorDeviceClass.AQI,              'icon': 'mdi:blur'},
    'particulate_matter_2_5':  {'key': 'pm2_5_atm',        'uom': SensorDeviceClass.AQI,              'icon': 'mdi:blur'},
    'particulate_matter_10':   {'key': 'pm10_0_atm',       'uom': SensorDeviceClass.AQI,              'icon': 'mdi:blur'},
    'air_quality_index_epa':   {'key': 'aqi_epa',          'uom': SensorDeviceClass.AQI,              'icon': 'mdi:weather-hazy'},
    'air_quality_index_lrapa': {'key': 'aqi_lrapa',        'uom': SensorDeviceClass.AQI,              'icon': 'mdi:weather-hazy'},
    'humidity':                {'key': 'current_humidity', 'uom': PERCENTAGE,                         'icon': 'mdi:water-percent'},
    'temperature':             {'key': 'current_temp',     'uom': UnitOfTemperature.FAHRENHEIT,       'icon': 'mdi:thermometer'},
    'dewpoint':                {'key': 'current_dewpoint', 'uom': UnitOfTemperature.FAHRENHEIT,       'icon': 'mdi:water-outline'},
    'pressure':                {'key': 'pressure',         'uom': UnitOfPressure.HPA,                 'icon': 'mdi:gauge'},
    'rssi':                    {'key': 'rssi',             'uom': SIGNAL_STRENGTH_DECIBELS_MILLIWATT, 'icon': 'mdi:wifi'}
}
SENSORS_DUAL_ONLY = ['pm2_5_aqi_b_raw']
# fmt: on

MANUFACTURER = "Purple Air"
DISPATCHER_PURPLE_AIR = "dispatcher_purple_air"
DOMAIN = "purpleair"
TEMP_ADJUSTMENT = -8  # From PurpleAir javascript: `(parseInt(temp) + -8).toFixed(0);`
HUMIDITY_ADJUSTMENT = (
    +4
)  # From PurpleAir javascript: `(hum = parseInt(hum) + 4) > 100 && (hum = 100)`

LOCAL_SCAN_INTERVAL = 30
LOCAL_URL_FORMAT = "http://{0}/json?live=false"

# Models
PMS_SENSOR = "PMS"
BME_SENSOR = "BME"
MODEL_PA_1 = "PA-I"
MODEL_PA_2 = "PA-II"
MODEL_PA_FLEX = "PA-II-FLEX"
