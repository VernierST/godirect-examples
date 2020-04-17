'''
Use the Go Direct Motion Detector (GDX-MD) to record the oscillations of a mass
on a spring. Compare measured data to modeled data. Vpython is used to give a 
3D visual representation of both the measured and modeled data.

This example assumes the Go Direct Motion Sensor is connected via USB, change to Bluetooth
as needed in the code below.

Look closely at the Experimental Setup Variables section below to modify variables, as needed.

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
gdx = gdx.gdx()

from vpython import *
import math

#Vpython Canvas
scene = canvas(title='<b>Simple Harmonic Oscillation',align = "left", center=vector(0,30,0))
scene.caption = '  Click Record for Data Collection'
scene.append_to_caption('\n\n', '   ')
scene.width = 300
scene.height = 500

#Experimental Setup Variables
'''An easy way to get the starting_spring_postion value is to measure the distance using the motion detector.
To do this, run the program without the mass oscillating and click the Record button to take measurements. 
You want the Vpython graph to have a plot with a 0 amplitude. If it is not 0 then look at the measurements 
that are printed to the terminal. Use those measurements to determine the starting_spring_position value'''
tmax = 10 #duration to take measurements from the motion detector (seconds)
starting_spring_position = 35.56 #equilibrium position - distance from detector to bottom of mass when hanging without oscillating (cm)
spring_equilibrium_length = 21 #length of spring with mass hanging
k=6 # spring constant starting value. A Vpython slider is created to adjust this value when running the program. 
# (note theoretical T = 2 pi SQR(mass/k); I measured as about 0.8N/0.154cm = 5.1 N/m)


#Variables
spring_stretch_model = 0 #variable to store location of spring in the model
max_stretch = 0
time_at_max_stretch = 0
index_at_max_stretch = 0
actual_list = []


#Vpython Configuration:
base_actual = box(pos=vector(0,0,0), size=vector(30,2,20), color=color.yellow)
rod_actual = cylinder(pos=vector(base_actual.pos.x-5,0,0), axis=vector(0,65,0), radius=1, color=color.blue)
top_support_actual = cylinder(pos=vector(rod_actual.pos.x-5,rod_actual.axis.y-5,0), axis=vector(25,0,0), radius=1, color=color.blue)
spring_actual = helix(pos=vector(top_support_actual.pos), axis=vector(0,-spring_equilibrium_length,0), coils=20, radius=1)
spring_actual.axis.y = -spring_equilibrium_length
spring_actual.pos.x = top_support_actual.pos.x + top_support_actual.axis.x/1.25
spring_actual.pos.y = top_support_actual.pos.y - top_support_actual.radius #move the spring y position to the underside of the top support
mass_actual = cylinder(pos=vector(spring_actual.pos), axis =vector(0,-8,0), radius = 3, color=color.blue, opacity=1)
mass_actual.pos.y = spring_actual.pos.y-spring_equilibrium_length
motiondetector = box(pos=vector(mass_actual.pos.x,4,0), size=vector(6,6,6), color=color.gray(0.5))
motiondetector_foil = cylinder(pos=vector(motiondetector.pos), axis =vector(0,3.1,0), radius = 2, color=color.white)
spring_model = helix(pos=vector(top_support_actual.pos), axis=vector(0,-spring_equilibrium_length,0), coils=20, radius=1)
spring_model.axis.y = -spring_equilibrium_length
spring_model.pos.x = top_support_actual.pos.x + top_support_actual.axis.x/2
spring_model.pos.y = top_support_actual.pos.y - top_support_actual.radius #move the spring y position to the underside of the top support
mass_model = cylinder(pos=vector(spring_model.pos), axis =vector(0,-8,0), radius = 3, color=color.red, opacity=1)
mass_model.pos.y = spring_model.pos.y-spring_equilibrium_length
mass_model.mass = 0.1 # mass hung on the spring(kg)
mass_model.p = 0 # initial momentum of mass (kg*m/s)


#Vpython graph:
pos_graph=graph(title= "position vs time", xmin=0, xmax=tmax, ymin=-5, ymax=5, align='right')
pos_graph.width = 800
pos_graph.height = 500
model_data=gcurve(color=color.red)
actual_data=gcurve(color=color.blue)
model_data.plot(0,0)  
actual_data.plot(0,0)
model_data.delete()
actual_data.delete()


scene.autoscale = False


gdx.open_usb()
#gdx.open_ble()

gdx.select_sensors([5]) #use the motion detector distance channel only. This is channel 5


##############################
# A record button is created. Use it to take live measurements from the Motion Detector
##############################
def Record(r):

    model_data.delete() #clear the graph
    actual_data.delete()

    global time_at_max_stretch #these variables will be used to pass the info to the Model function
    global index_at_max_stretch
    global actual_list
    global max_stretch
    global dt
     
    spring_stretch_actual = 0 
    max_stretch = 0
    i=0
    t = 0.0
    dt = 0.05 #note gdx.start below where it sets the sampling period to 100ms (or 0.1 seconds)
 
    time_at_max_stretch = 0
    index_at_max_stretch = 0
    actual_list = []

    #gdx.start(period=50) #start data collection
    gdx.start(period = (dt*1000))
    
    while t < tmax + dt: #use the loop to read the data
    
        measurements = gdx.read() #returns a list of measurements from the sensors selected.
        if measurements == None: 
            break 
        print('distance (cm) = ', measurements[0]*100)
        spring_stretch_actual = measurements[0]*100 - starting_spring_position
        spring_actual.axis.y =  -spring_equilibrium_length + spring_stretch_actual
        mass_actual.pos.y = spring_actual.pos.y-spring_equilibrium_length + spring_stretch_actual
        actual_data.plot(t,spring_stretch_actual)
        actual_list.append(spring_stretch_actual) #create a list of all the measurements. Store in a variable to send to the Model function
    
        if spring_stretch_actual>max_stretch: #Capture the biggest stretch. Store in variables to send to the Model function
            max_stretch=spring_stretch_actual
            time_at_max_stretch = t
            index_at_max_stretch = i
    
        t = t + dt
        i = i + 1
    gdx.stop()  
button( bind=Record, text='Record', pos=scene.caption_anchor)


##############################
# A Model button is created. Use it to plot the model data and the saved measurements from Record
##############################
def model(m):
    global actual_list
    print ("len of list at beginning = ", len(actual_list))
    print('\n\n')

    actual_list_for_model = []
    spring_model.pos.y = top_support_actual.pos.y - top_support_actual.radius #move the spring y position to the underside of the top support
    mass_model.pos.y = spring_model.pos.y-spring_equilibrium_length
    spring_model.axis.y = -spring_equilibrium_length
    spring_actual.pos.y = top_support_actual.pos.y - top_support_actual.radius
    mass_actual.pos.y = spring_actual.pos.y-spring_equilibrium_length
    spring_actual.axis.y = -spring_equilibrium_length
    model_data.delete()
    actual_data.delete()
    print('model actual list =', actual_list)
    print('\n\n')
    print ("len of list = ", len(actual_list))
    print('\n\n')
    actual_list_for_model = list(actual_list)
    i=0
    del actual_list_for_model[0:index_at_max_stretch]
    print ("len of list after del = ", len(actual_list))
    print('\n\n')
    print ("len of model after del = ", len(actual_list_for_model))
    print('\n\n')

    t = time_at_max_stretch
    spring_stretch_model = max_stretch
    print('spring stretch model =', spring_stretch_model)
    print('\n\n')
    #dt = 0.05
    print('k = ', k)
    print('\n\n')
    mass_model.p = 0

    while t < tmax + dt:
        rate(10)
        actual_data.plot(t,actual_list_for_model[i])
        model_data.plot(t,spring_stretch_model)

        Fe =  k*(spring_stretch_model)*-1 # forces acting on the system (elastic force)
        mass_model.p = mass_model.p + Fe*dt # update the momentum
        spring_stretch_model = spring_stretch_model + (mass_model.p/mass_model.mass)*dt

        spring_actual.axis.y =  -spring_equilibrium_length + actual_list_for_model[i]
        spring_model.axis.y = -spring_equilibrium_length + spring_stretch_model
        mass_actual.pos.y = spring_actual.pos.y-spring_equilibrium_length + actual_list_for_model[i]
        mass_model.pos.y = spring_model.pos.y-spring_equilibrium_length + spring_stretch_model       
        
        t = t + dt
        i = i + 1
button( bind=model, text='Model', pos=scene.caption_anchor)

##############################
# An Exit button is created. Use it to close the USB connection
##############################
def exit(e):
    gdx.close()
button( bind=exit, text='EXIT', color=color.red, pos=scene.caption_anchor)
scene.append_to_caption('\n\n')

##############################
'''
A slider is created. Use it to modify the spring constant. The function specified by "bind" is 
called when the user drags the slider. In this case, the function S is called. This function
updates the variable "k" with the value of the slider and updates the variable "wt" with new text.
'''
##############################
def S(s): # this is the function that is called when the slider is changed.
    print(s.value)
    global k #the k value is modified by the slider and used in the model function
    k = s.value
    wt.text = 'spring constant k = {:1.2f}'.format(s.value)
sl = slider(min=0, max=10, value=k, length=200, bind=S, left=20) #when the slider is changed, the function S is called using "bind = S"
#scene.append_to_caption('\n\n')
scene.append_to_caption('  ')

wt = wtext(text='spring constant k = {:1.2f}'.format(k))
scene.append_to_caption('\n\n')

##############################
# A second slider is created. Use it to modify the start position (distance from top of MD to bottom of weight)
##############################
def R(r): 
    print(r.value)
    global starting_spring_position #the k value is modified by the slider and used in the model function
    starting_spring_position = r.value
    rt.text = 'start position = {:1.2f}'.format(r.value)
slsl = slider(min=30, max=40, value=starting_spring_position, length=200, bind=R, left=20)
scene.append_to_caption('  ')

rt = wtext(text='start positions = {:1.2f}'.format(starting_spring_position))





