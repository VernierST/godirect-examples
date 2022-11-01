"""
This example combines the gdx_getting_started_usb example with
VPython code to control the height of a sphere in a cylinder.
"""

from vpython import *
from gdx import gdx
gdx = gdx.gdx()


gdx.open(connection='usb')    # change to 'ble' for Bluetooth connection
gdx.select_sensors()
gdx.start(250) 

my_canvas = canvas(height=500, width=400)
my_sphere = sphere(radius=25, color=color.red)
my_rod = cylinder(pos=vector(0, -200, 0), radius=25, axis=vector(0, 400, 0), opacity=0.2)

for i in range(0,80):
    measurements = gdx.read()
    if measurements == None: 
        break 
    print(measurements)
    sensor0_data = measurements[0]
    my_sphere.pos.y = sensor0_data * 2

gdx.stop()
gdx.close()
