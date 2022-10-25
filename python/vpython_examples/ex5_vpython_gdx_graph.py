"""
Use gdx.vp_vernier_canvas() to add a graph to the scene.

When you add a graph, you need to input the data to the graph
in the collection loop using this function:
gdx.vp_graph() 
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

gdx.open(connection='usb')   # Use connection='ble' for a Bluetooth connection
gdx.select_sensors()

# By default, buttons, slider, and live meters are all True. But the default for
# graph is False. Change the graph to True to add a graph to the scene. 
gdx.vp_vernier_canvas(graph=True)

gdx.start(period=250) 

while gdx.vp_close_is_pressed() == False:  
    while gdx.vp_collect_is_pressed() == True:       
        measurements = gdx.read()    # 'measurements' is a list - one data point per sensor
        if measurements == None:
            break 
        print(measurements)