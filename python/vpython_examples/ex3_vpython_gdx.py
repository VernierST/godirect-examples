"""
Set the color attribute with a sensor reading. Note you must modify
the 'threshold' variable based on what sensor you are using.

This example simply combines a standard gdx_getting_started example with
VPython code.
"""

import os
import sys

# This tells Python that the /gdx/ folder is up one directory
gdx_module_path = os.path.abspath(os.path.join('.'))
if gdx_module_path not in sys.path:
    sys.path.append(gdx_module_path)

# If the /gdx/ folder is not found, uncomment the print() to see where Python is looking. 
# and move the /gdx/ folder into one of these paths.
# print("path:  ", sys.path)

from vpython import *
from gdx import gdx
gdx = gdx.gdx()


threshold = 50   # modify this threshold based on your sensor reading

gdx.open(connection='USB')    # change to 'ble' for Bluetooth connection
gdx.select_sensors()
gdx.start(500) 
my_sphere = sphere()

for i in range(0,20):
    measurements = gdx.read()
    if measurements == None: 
        break 
    if measurements[0] > threshold:
        sensor_color = vector(1, 0, 0)
    else:
        sensor_color = vector(0, 0, 1)
    my_sphere.color = sensor_color
    print(measurements, ", ", sensor_color)

gdx.stop()
gdx.close()
