"""
Use gdx.vp_vernier_canvas() to add a chart to the scene.

The chart updates automatically during the data collection
loop. It plots the active sensors versus time. 
"""

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