''' 
Simple starter program that uses the gdx functions to collect data from a Go Direct device 
connected via USB. 

When using gdx.open(), note it has two arguments that can be set. They are 'connection' 
and 'device_to_open'. Here are some ways to configure gdx.open() for a USB connection:

gdx.open(connection='usb')
            When the 'device_to_open' argument is left blank, the function finds all available 
            Go Direct devices connected via USB. If only one device is found it will
            automatically connect to that device. If more than one device is found it prints 
            the list to the terminal, and prompts the user to select the device to connect.

gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9')
            Use your device's name as the argument. The function will search for a 
            USB device with this name. If found it will connect it. If connecting to 
            multiple devices separate the names with a comma, such as,
            device_to_open='GDX-FOR 071000U9, GDX-HD 151000C1'

Tip: Skip the prompts to select the sensors and period by entering arguments in the functions.

Example 1, collect data from sensor 1 at a period of 1000ms using:
gdx.select_sensors([1])
gdx.start(1000)

Example 2, collect data from sensors 1, 2 and 3 at a period of 100ms using:
gdx.select_sensors([1,2,3])
gdx.start(100)
'''

from gdx import gdx
gdx = gdx.gdx()


gdx.open(connection='usb')
gdx.select_sensors()
gdx.start() 
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