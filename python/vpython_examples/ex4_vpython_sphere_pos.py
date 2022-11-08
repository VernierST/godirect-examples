"""
This example controls the height of a sphere in a cylinder.
"""

from vpython import *   
from gdx import gdx
gdx = gdx.gdx()


gdx.open(connection='usb')    # change to 'ble' for Bluetooth connection
gdx.select_sensors()
gdx.vp_vernier_canvas()

my_canvas = canvas(height=500, width=400)
my_sphere = sphere(radius=25, color=color.red)
my_rod = cylinder(pos=vector(0, -200, 0), radius=25, axis=vector(0, 400, 0), opacity=0.2)

gdx.start(250) 

while gdx.vp_close_is_pressed() == False:  
    while gdx.vp_collect_is_pressed() == True:       
        measurements = gdx.read()    # 'measurements' is a list - one data point per sensor
        if measurements == None:
            break 
        print(measurements)
        sensor0_data =  measurements[0]    # index out the first sensor's data point
        my_sphere.pos.y = sensor0_data * 2   