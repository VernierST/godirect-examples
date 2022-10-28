"""
Use gdx.vp_vernier_canvas() to add a chart to the scene.

The chart updates automatically during the data collection
loop. It plots the active sensors versus time. 
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

gdx.open(connection='usb')   # Use connection='ble' for a Bluetooth connection
gdx.select_sensors()

# By default, buttons, slider, and live meters are all True. But the default for
# chart is False. Change the chart to True to add a chart to the scene. 
gdx.vp_vernier_canvas(chart=True)

gdx.start(period=250) 

while gdx.vp_close_is_pressed() == False:  
    while gdx.vp_collect_is_pressed() == True:       
        measurements = gdx.read()    # 'measurements' is a list - one data point per sensor
        if measurements == None:
            break 
        print(measurements)