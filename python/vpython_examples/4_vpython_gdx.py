"""
Modify the color attribute with a sensor reading. Note you must modify
line 11 based on what sensor you are using.
"""
import os
import sys

# This allows us to import the local gdx module that is up one 
file_name = '4_vpython_gdx.py'
os_path = os.path.abspath(file_name)
print("os path:  ", os_path)
gdx_module_path = os.path.abspath(os.path.join('.'))
# If the module is not found, uncomment and try two dots. Also, uncomment the print(sys.path)
#gdx_module_path = os.path.abspath(os.path.join('..'))
print("gdx module path :", gdx_module_path)
if gdx_module_path not in sys.path:
    sys.path.append(gdx_module_path)

# If there is an error trying to find the gdx module, uncomment this to see where
# the program is looking to find the gdx folder
#print("looking here: ", sys.path)


from vpython import *
from gdx import gdx
gdx = gdx.gdx()

my_sphere = sphere()
threshold = 50   # modify this threshold based on your sensor reading

gdx.open(connection='USB')    # change to 'ble' for Bluetooth connection
gdx.select_sensors()
gdx.start() 

for i in range(0,20):
    measurements = gdx.read()
    if measurements == None: 
        break 
    if measurements[0] > threshold:
        sensor_color = vector(1, 0, 0)
    else:
        sensor_color = vector(0, 0, 1)
    my_sphere.color = sensor_color
    print(measurements)
    print(sensor_color)

gdx.stop()
gdx.close()