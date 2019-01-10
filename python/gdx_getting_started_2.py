''' 
This examples is the same as gdx_getting_started_1.py, except we are now 
passing arguments in the select_sensors() and start() functions to avoid the prompts.

This example assumes the Go Direct sensor is connected via USB. Go to the
gdx_getting_started_4.py example to see how to open a bluetooth connection.

Note that the select_sensors argument is a list and the sensor numbers must be inside 
list brackets, e.g. gdx.select_sensors([1,2,3]).

How do you know what the sensor numbers are on your Go Direct device? Go to 
gdx_getting_started.3.py example to list all of the sensor channels.

'''

from gdx import gdx #the gdx function calls are from a gdx.py file inside the gdx folder.
gdx = gdx.gdx()

gdx.open_usb()
gdx.select_sensors([1,2])
gdx.start(period=1000) 

for i in range(0,5):
    measurements = gdx.read() #returns a list of measurements from the sensors selected.
    if measurements == None: 
        break 
    print(measurements)

gdx.stop()
gdx.close()