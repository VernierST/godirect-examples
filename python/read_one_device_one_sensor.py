from gdx import gdx
gdx = gdx.gdx()


# MODIFY THIS! Set the connection = 'usb' or 'ble'. 
# Set device_to_open with your device's serial number (e.g., device_to_open='GDX-FOR 071000U9')
gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9')

# MODIFY THIS! Put your sensor number here. Note that when you are reading from just one
# sensor you can just enter the sensor number. If you are reading from multiple 
# sensors they would need to be input as a list (e.g., [1,2,3]).
gdx.select_sensors(1) 

# Set the rate for data collection. This is the period in milliseconds.
gdx.start(period=1000)    

# 'column_headers' is a string with the description and units of the selected sensor.
column_headers= gdx.enabled_sensor_info()
print(column_headers)

for i in range(0,5):
    # when only 1 sensor is configured, 'measurments' is returned as single value, when 
    # multiple sensors are configured, 'measurements' is returned as a list of values.
    measurements = gdx.read()
    if measurements == None:
        break 
    print(measurements)
           
# Stop collecting data from the sensor
gdx.stop()

# Disconnect the Go Direct connection
gdx.close()