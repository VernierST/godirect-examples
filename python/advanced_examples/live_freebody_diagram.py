'''
This program takes advantage of the 3-axis accelerometer built into GDX-FOR. Using the accelerometer 
values, the program creates a "live" freebody diagram for a ring with three forces acting on it:
1) The force of a hanging mass, pulling downward on the ring
2) The force of the GDX-FOR sensor, pulling up at an angle on the ring
3) The force of a string, tied an upright ring stand and on the ring, also pulling up at an angle on the ring

The resulting freebody diagram is "Y" shaped. As you run the program, move the GDX-FOR around. 
The freebody diagram will update itself to reflect the GDX-FOR's current orientation and the force 
exerted by its load cell.

This program is written to connect to GDX-FOR via Bluetooth. 
You can run the program connected to GDX-FOR via USB; just change line 25 to "gdx.open_usb".

This program requires the godirect-py, vpython, and math packages.
'''

import os
import sys

# This allows us to import the local gdx module that is up one directory
gdx_module_path = os.path.abspath(os.path.join('.'))
# If the module is not found, uncomment and try two dots. Also, uncomment the print(sys.path)
#gdx_module_path = os.path.abspath(os.path.join('..'))
if gdx_module_path not in sys.path:
    sys.path.append(gdx_module_path)

# If there is an error trying to find the gdx module, uncomment this to see where
# the program is looking to find the gdx folder
#print(sys.path)

from gdx import gdx
from vpython import *
gdx = gdx.gdx()

import math

canvas(title='<b>Live Freebody Diagram<b>')

hanging_mass=float(input("Enter the mass (in kg) of the hanging mass:"))    # prompts user for mass of hanging mass

gdx.open_ble('GDX-FOR 07200362') # change GDX-FOR ID to match your device
gdx.select_sensors([1,2,3,4])   # GDX-FOR sensors: 1 - force sensor, 2 - x axis accel, 3 - y axis accel, 4 - z axis accel
gdx.start(period=200)   # data collection period of 200 ms, means a sampling rate of 5 samples/second

# create vpython objects for the ring and each force, as well as labels for the forces
obj = ring(axis=vector(0,0,1),radius=0.5,thickness=0.1,color=color.blue)
Pointer_hm = arrow (pos=vector(0,-1.1,0),axis=vector(0,-1,0),length=hanging_mass*9.8,color=color.red)
Label_hm = label(text='<i><b>F</i></b><sub>hanging mass</sub> = '+str(round(9.8*hanging_mass,2))+' N @ 270°',color=color.red,pos=Pointer_hm.pos,xoffset=10,yoffset=-10,box=False,line=False)
Pointer_gdx = arrow(color=color.green)
Label_gdx=label(text='<i><b>F</i></b><sub>GDX-FOR</sub>',color=color.green,pos=Pointer_gdx.pos,xoffset=50,yoffset=20,box=False,line=False)
Pointer_string = arrow(color=color.yellow)
Label_string=label(text='<i><b>F</i></b><sub>string</sub>',color=color.yellow,pos=Pointer_string.pos,xoffset=-50,yoffset=20,box=False,line=False)

# data collection loop, runs for 100 samples or 20 seconds (with a 200 ms period -> see line 27)
for i in range(0,100):
    # get force and direction measurements from GDX-FOR
    measurements = gdx.read()
    if measurements == None:
        break
    print(measurements)
    force_reading = measurements[0] # sensor channel 1 is force (in Newtons)
    direction = vector(-measurements[2],-measurements[1],measurements[3])   # use the accelerometer values to create a vector for the force exerted by the force sensor
    f_gdx = force_reading*direction.norm()  # vector that represents the force exerted by the force sensor
    # update the GDX-FOR arrow in the freebody diagram
    Pointer_gdx.axis=f_gdx.norm()
    Pointer_gdx.pos=f_gdx/f_gdx.mag
    Pointer_gdx.length=f_gdx.mag
    Angle_gdx=math.atan2(direction.y,direction.x)*180/math.pi
    Label_gdx.text='<i><b>F</i></b><sub>GDX-FOR</sub> = '+str(round(force_reading,2))+' N @ '+str(round(Angle_gdx,2))+'°'

    # define the hanging mass vector
    f_hm = vector(0,-9.8*hanging_mass,0)
    # update the hanging mass arrow in the freebody diagram
    Pointer_hm.axis=f_hm.norm()
    Pointer_hm.pos=vector(0,-1.1,0)
    Pointer_hm.length=f_hm.mag

    # calculate the force/direction exerted by the string
    f_string = -(f_gdx+f_hm)    # python does the vector addition, no need to separate into components
    # update the string arrow in the freebody-diagram
    Pointer_string.axis=f_string.norm()
    Pointer_string.pos=f_string/f_string.mag
    Pointer_string.length=f_string.mag
    Angle_string=math.atan2(Pointer_string.axis.y,Pointer_string.axis.x)*180/math.pi
    Label_string.text='<i><b>F</i></b><sub>string</sub> = '+str(round(f_string.mag,2))+' N @ '+str(round(Angle_string,2))+'°'
    
        
gdx.stop() 
gdx.close() 

