"""
Set the color attribute with a sensor reading. Note you must modify
the 'threshold' variable based on what sensor you are using.

This example simply combines a standard gdx_getting_started example with
VPython code.
"""

# Code to tell Python to look for the gdx module up one directory
import os
import sys
# get the path (note that sys.argv[0] gives the name of this file)
file_path = os.path.abspath(os.path.dirname(sys.argv[0]))
# make 'file_path' the current working directory (cwd)
os.chdir(file_path)
# move the cwd path up one directory
os.chdir("..")
gdx_module_path = os.getcwd()
# add the cwd path to the system path, so Python will look there for the gdx folder
if gdx_module_path not in sys.path:
    sys.path.append(gdx_module_path)
# Here are the paths where Python is looking for the gdx module. If the gdx module is 
# not found, move the /gdx/ folder into one of the paths.
print('\n', "System Paths:")
for path in sys.path:
    print(path)


from vpython import *
from gdx import gdx
gdx = gdx.gdx()


threshold = 50   # modify this threshold based on your sensor reading

gdx.open(connection='USB')    # change to 'ble' for Bluetooth connection
gdx.select_sensors()
gdx.start(500) 
my_sphere = sphere()

for i in range(0,40):
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
