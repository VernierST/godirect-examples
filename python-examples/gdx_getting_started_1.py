
''' 
Here are the gdx functions used in a typical program to collect data:

gdx.open_usb() or gdx.open_ble()
gdx.select_sensors()
gdx.start()
gdx.read()
gdx.stop()
gdx.close()

Here are other functions that might be useful for customizing a program:

gdx.device_info()
gdx.enabled_sensor_info()
gdx.sensor_info()
gdx.discover_ble_devices()
monitor_rssi()

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Below is a simple starter program. Note that this program does not pass any 
arguments in the functions. Go to the gdx_getting_started_2.py example to 
see how you can pass arguments to the open(), select sensors(), and start() 
functions, and avoid the prompts.

**** This example assumes the Go Direct sensor is connected via USB.

'''

from gdx import gdx #the gdx function calls are from a gdx.py file inside the gdx folder.
gdx = gdx.gdx()

gdx.open_usb()
gdx.select_sensors()
gdx.start() 

for i in range(0,5):
    measurements = gdx.read() #returns a list of measurements from the sensors selected.
    if measurements == None: 
        break 
    print(measurements)

gdx.stop()
gdx.close()