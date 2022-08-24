"""
Use a Go Direct sensor reading to control the length of a vpython box object
"""

from vpython import *   

from gdx import gdx
gdx = gdx.gdx()

gdx.open(connection='usb')   # Use connection='ble' for a Bluetooth connection
gdx.select_sensors()

# setup a vernier vpython canvas with buttons to control data collection  
gdx.vp_vernier_canvas()

# Create a vpython box object.
b = box(size=0.1*vec(1,1,1), color=color.red)

gdx.start(period=250) 

while gdx.vp_close_is_pressed() == False:  
    while gdx.vp_collect_is_pressed() == True:       
        measurements = gdx.read()    # 'measurements' is a list - one data point per sensor
        print(measurements)
        if measurements == None:
            break 
        gdx.vp_meter(measurements)    # display all data in the vernier canvas meter
        sensor0_data =  measurements[0]    # index out the first sensor's data point
        b.length = 0.1 * sensor0_data   # use this sensor's data point to control the length of the object