'''
Color Program for Go Direct Light and Color sensor (GDX-LC).
This program is written to connect to GDX-LC via USB.
'''
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
gdx=gdx.gdx()


# setup a Vernier vpython canvas with buttons to control data collection  
gdx.vp_vernier_canvas(slider=False)
gdx.open(connection='usb')   # Use connection='ble' for a Bluetooth connection
#gdx.open_ble("GDX-LC 091001T7") # change to gdx.open_ble("GDX-LC 09100449") >> number to match your device
gdx.select_sensors([1,5,6,7])   # GDX-LC sensors: 1: light; 2: UV; 5: red; 6:green; 7: blue
gdx.start(250)   # data collection period in ms. Set to gdx.start(period=1000) for a sampling rate of 1 sample/second
# setup another  vpython canvas, c2
c2 = canvas(width=800, height=400)
c2.range=2
c2.caption='''This program uses Vernier's Go Direct Light and Color sensor (GDX-LC).
It will collect data using the RGB sensor and display the readings by
changing the length of the colored arrow. It will use those readings to
determine the color of the sphere.'''
#c2.autoscale=False
red_arrow =   arrow(pos=vector(-1.0,-1,0),axis=vector(0,1,0), shaftwidth=.2,headwith=.2,color=color.red)
green_arrow = arrow(pos=vector(-0.7,-1,0),axis=vector(0,1,0), shaftwidth=.2,headwith=.2,color=color.green)
blue_arrow =  arrow(pos=vector(-0.4,-1,0),axis=vector(0,1,0), shaftwidth=.2,headwith=0, color=color.blue)

color_sphere = sphere(pos=vector(1,0,0),radius=1)
# data collection loop:
while gdx.vp_close_is_pressed() == False:  
    while gdx.vp_collect_is_pressed() == True:    

        # # get color measurements from GDX-LC
        measurements = gdx.read()
        if measurements==None:
            break
        gdx.vp_meter(measurements)   # display all data in the vernier canvas meter
        intensity =  measurements[0] # 0 represents the first element of the array that stores the data
        LCRed =   measurements[1] 
        LCGreen = measurements[2]
        LCBlue =  measurements[3]
        '''
        Set the divisors in the lines below to match the color sensors reading with a white reflector.
        If everything is scaled properly, when the program runs and you are using a white object, 
        the arrow's lengths should all be about the sphere's radius."        
        '''
        R_scaled = LCRed/intensity*4
        G_scaled = LCGreen/intensity*4
        B_scaled = LCBlue/intensity*4
        red_arrow.axis.y=R_scaled
        green_arrow.axis.y=G_scaled
        blue_arrow.axis.y=B_scaled
        color_sphere.color = vector(R_scaled,G_scaled,B_scaled)
        