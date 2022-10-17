'''
This example uses the Go Direct Hand Dynamometer (GDX-HD) to control a Turtle object.

The GDX-HD is equipped with a 3-axis accelerometer, 3-axis gyro, and force sensor. 
This example uses the accelerometer readings from two of the three axis to calculate tilt angle
and use that calculation to control the tilt angle of a turtle object. The force readings are 
used to control the size of the turtle object. The example was written assuming a hand dynamometer 
with the usb cable down and the label facing left.

The example will continue to run until the user squeezes hard (force goes above 10 Newtons)

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

from gdx import gdx
gdx = gdx.gdx()

import math
import turtle


gdx.open(connection='usb')   # change to 'ble' for Bluetooth connection

gdx.select_sensors([1,3,4])   # Hand Dynamometer sensors to use: 3 - y axis accel, 4 - z axis accel
gdx.start(period=200) 

square = turtle.Turtle()
square.shape("square")
square.shapesize(5,20)

#for i in range(0,100):
a = True
while a:
    measurements = gdx.read()
    if measurements == None:
        break
    force = measurements[0]/5
    x_direction = measurements[1]/9.8  
    y_direction = measurements[2]/9.8  
    angle = math.atan2(y_direction, x_direction)  #compute the roll using two accelerometers (radians)
    print("angle radians =", angle)
    angle = (angle*180)/3.14  #convert radians to degrees
    print("angle degrees= ", angle)
    square.tiltangle(angle)
    square.shapesize(2+force,8+force)
    print("force/5 = ", force)
    if force>10:
        a = False
        
gdx.stop() 
gdx.close() 

turtle.done()