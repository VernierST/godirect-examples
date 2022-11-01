''' 
Simple starter program to show how to configure the gdx functions to read 
from more than one Go Direct device.  

Two things to note for connecting multiple devices. The first is listing
all devices in the 'device_to_open' argument, separating the device names
with a comma, such as:

gdx.open(connection='ble', device_to_open='GDX-FOR 071000U9, GDX-HD 151000C1')

The second is setting the select_sensor() argument as a 2D list of sensor
numbers, such as:

gdx.select_sensors([[1,2,3], [1]])

To review how to set the select_sensors() argument based on how many devices
and sensors are configured, here are some examples:
    Configure 1 device with sensor number 1:
    gdx.select_sensors([1])
    Configure 1 device with sensor numbers 1, 5, and 6:
    gdx.select_sensors([1,5,6])
    Configure 2 devices. Device 1 with sensor number 1. Device 2 with sensor 5:
    gdx.select_sensors([[1], [5]])
    Configure 3 devices. Device 1 with sensors 1,5,6. Device 2 with sensor 5. 
    Device 3 with sensors 1 and 2:
    gdx.select_sensors([[1,5,6], [5], [1,2]]) 
'''

from gdx import gdx
gdx = gdx.gdx()


# ENTER YOUR DEVICE NAMES HERE
gdx.open(connection='ble', device_to_open='enter 1st device name here, 2nd device name here')
#gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9, GDX-MD 0B1008M1')

# ENTER YOUR 2D LIST OF SENSORS HERE
gdx.select_sensors([[], []])
#gdx.select_sensors([[1,2], [5]])

gdx.start(500) 
column_headers= gdx.enabled_sensor_info()   # returns a string with sensor description and units
print('\n')
print(column_headers)

for i in range(0,5):
    measurements = gdx.read()
    if measurements == None: 
        break 
    print(measurements)

gdx.stop()
gdx.close()