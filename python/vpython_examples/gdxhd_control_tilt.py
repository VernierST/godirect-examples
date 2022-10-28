'''
This example uses the Go Direct Hand Dynamometer (GDX-HD) to control a box object.
The GDX-HD is equipped with a 3-axis accelerometer, 3-axis gyro, and force sensor. 
This program uses the accelerometer readings from two of the three axis to calculate tilt angle
and use that calculation to control the tilt angle of a object. The force readings are 
used to control the size of the object. 

Hold the hand dynamometer with the label facing you and the USB cable at the bottom.
Start data collection and then tilt the hand-dynamometer left and right, always with 
the label facing you. Do not tilt back and forward. Do not rotate the label away from
you.  
'''

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
gdx.select_sensors([1,2,3,4])

# setup a vernier vpython canvas with buttons to control data collection  
gdx.vp_vernier_canvas()

# create a canvas for the box that will be rotated
c = canvas(width=500, height=500, align='left')
c.forward=vector(0,-1,0)
c.range=12
az = arrow(pos=vector(0,0,0), axis=vector(0,0,8), radius=1, label="z",shaftwidth=.2,color=color.green)
ax = arrow(pos=vector(0,0,0), axis=vector(8,0,0), radius=1, label="x",shaftwidth=.2,color=color.cyan)

lz = label(pos=vector(0,0,4), text="z",color=color.green)
lx = label(pos=vector(4,0,0), text="x")
box_object = box(pos=vector(0,0,0), axis=vector(8,8,0), radius=1, label="x",color=color.red)
scale=.3 #scale factor, controlling the size of the box on screen
scene.autoscale=False
gdx.start(period=250) #period in milliseconds
while gdx.vp_close_is_pressed() == False:  
    while gdx.vp_collect_is_pressed() == True:   
        measurements = gdx.read()    # 'measurements' is a list - one data point per sensor
        if measurements == None:
            break 
        print(measurements)
        force =  measurements[0]    # index out the first sensor's data point
        box_size=force*.05+4 # make the box always have some length and scale it to be controlled by the grip strength
        x =  measurements[1] 
        y =  measurements[2] # the y is not used in this example
        z =  measurements[3]  
        box_object.axis = vec(box_size*scale*x, 0,-box_size*scale*z)
            