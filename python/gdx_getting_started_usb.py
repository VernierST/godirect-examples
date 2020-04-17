''' 
The gdx functions are located in a gdx.py file inside a folder named "gdx". In order for 
the import to find the gdx folder, the folder needs to be in the same directory as this python program.

The gdx functions used in a typical program to collect data include:

gdx.open_usb() or gdx.open_ble()
gdx.select_sensors()
gdx.start()
gdx.read()
gdx.stop()
gdx.close() 

Below is a simple starter program that uses these functions to collect data from a Go Direct 
device (or devices) connected via USB. This example will provide you with prompts to select 
the sensors and the sampling period. Try a period of 1000 ms (1 sample/second). 

Tip: Skip the prompts to select the sensors and period by entering arguments in the functions.
Example 1, collect data from sensor 1 at a period of 1000ms using:
gdx.select_sensors([1]), gdx.start(1000)
Example 2, collect data from sensors 1, 2 and 3 at a period of 100ms using:
gdx.select_sensors([1,2,3]), gdx.start(100)

'''

# This code imports the gdx functions. 
from gdx import gdx
gdx = gdx.gdx()

# This code uses the gdx functions to collect data from your Go Direct sensors. 
gdx.open_usb()
gdx.select_sensors()
gdx.start() 

for i in range(0,5):
    measurements = gdx.read()
    if measurements == None: 
        break 
    print(measurements)

gdx.stop()
gdx.close()