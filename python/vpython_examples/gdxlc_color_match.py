'''
Color Program for Go Direct Light and Color sensor (GDX-LC).
This program is written to connect to GDX-LC via USB.
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
gdx=gdx.gdx()


# setup a Vernier vpython canvas with buttons to control data collection  
gdx.vp_vernier_canvas(slider=False)
gdx.open(connection='usb')   # Use connection='ble' for a Bluetooth connection
gdx.select_sensors([1,5,6,7])   # GDX-LC sensors: 1: light; 2: UV; 5: red; 6:green; 7: blue
gdx.start(250)   # data collection period in ms.

# setup another  vpython canvas, c2
c2 = canvas(width=800, height=400)
c2.range=2
c2.caption='''This program uses Vernier's Go Direct Light and Color sensor (GDX-LC).
It will collect data using the RGB sensor and display the readings by
changing the length of the colored arrow. It will use those readings to
determine the color of the sphere.'''
red_arrow =   arrow(pos=vector(-1.0,-1,0),axis=vector(0,1,0), shaftwidth=.2,headwith=.2,color=color.red)
green_arrow = arrow(pos=vector(-0.7,-1,0),axis=vector(0,1,0), shaftwidth=.2,headwith=.2,color=color.green)
blue_arrow =  arrow(pos=vector(-0.4,-1,0),axis=vector(0,1,0), shaftwidth=.2,headwith=0, color=color.blue)
color_sphere = sphere(pos=vector(1,0,0),radius=1)

# data collection loop:
while gdx.vp_close_is_pressed() == False:  
    while gdx.vp_collect_is_pressed() == True:    
        # get color measurements from GDX-LC
        measurements = gdx.read()
        if measurements==None:
            break
        intensity =  measurements[0]  # 0 represents the first element of the array that stores the data
        LCRed =   measurements[1] 
        LCGreen = measurements[2]
        LCBlue =  measurements[3]
        '''
        Set the divisors in the lines below to match the color sensors reading with a white reflector.
        If everything is scaled properly, when the program runs and you are using a white object, 
        the arrow's lengths should all be about the sphere's radius."        
        '''
        if intensity > 0:    # do not want to divide by 0
            R_scaled = LCRed/intensity*4
            G_scaled = LCGreen/intensity*4
            B_scaled = LCBlue/intensity*4
            red_arrow.axis.y=R_scaled
            green_arrow.axis.y=G_scaled
            blue_arrow.axis.y=B_scaled
            color_sphere.color = vector(R_scaled,G_scaled,B_scaled)
        