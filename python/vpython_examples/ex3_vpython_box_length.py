"""
Use a Go Direct sensor reading to control the length of a vpython box object.

This example introduces the gdx functions for VPython. These functions create VPython objects
that help facilitate data collection with Go Direct sensors in VPython.

gdx.vp_vernier_canvas() - add buttons, sliders, and live sensor readouts to the scene
gdx.vp_close_is_pressed() - monitors the state of the CLOSE button
gdx.vp_collect_is_pressed() - monitors the state of the COLLECT/STOP button
"""
    
from vpython import *   
from gdx import gdx
gdx = gdx.gdx()

gdx.open(connection='usb')   # Use connection='ble' for a Bluetooth connection
gdx.select_sensors()

# setup a vernier vpython canvas with buttons to control data collection  
gdx.vp_vernier_canvas()

# Create a vpython box object.
my_box = box(size=0.1*vec(1,1,1), color=color.red)

gdx.start(period=250) 

while gdx.vp_close_is_pressed() == False:  
    while gdx.vp_collect_is_pressed() == True:       
        measurements = gdx.read()    # 'measurements' is a list - one data point per sensor
        if measurements == None:
            break 
        print(measurements)
        sensor0_data =  measurements[0]    # index out the first sensor's data point
        my_box.length = 0.1 * sensor0_data   # use this sensor's data point to control the length of the object