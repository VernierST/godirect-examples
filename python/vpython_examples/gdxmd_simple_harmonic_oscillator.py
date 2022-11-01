'''
Use the Go Direct Motion Detector (GDX-MD) to record the oscillations of a mass
on a spring. Compare measured data to modeled data. Vpython is used to give a 
3D visual representation of both the measured and modeled data.

This example assumes the Go Direct Motion Sensor is connected via USB, change to Bluetooth
as needed in the code below.

Look closely at the Experimental Setup Variables section below to modify variables, as needed.
'''

from vpython import * 
from gdx import gdx
gdx = gdx.gdx()

gdx.open(connection='usb')   # Use connection='ble' for a Bluetooth connection
gdx.select_sensors([5])     # GDX-MD uses sensor #5

# setup a vernier vpython canvas with buttons to control data collection  
gdx.vp_vernier_canvas() 

# setup a vpython canvas
scene = canvas(width=600, height=400)     
#Set up scene:
scene.autoscale = False
scene.title = '<b> Simple Harmonic Motion, with Vectors'
scene.title = '<b> Real Data or Modelling Data'
scene.align = "left"
scene.center = vector(0,30,0)
scene.forward = vector(-.2,0,1)
scene.background = color.white
scene.range = 40
scene.camera.angle = (-13.4254, 0, 67.1268)


###############
#Modelling values:
k = 19  # Spring constant in N/m
ymax = 45.0  # Position of the bottom of the object, when released (it is also the maximum position(cm))
y0 = 40  # Equilibrium position - distance from detector to bottom of object when hanging without oscillating(cm)
mass_of_object = 0.5  # mass of object on spring in kg
###############


# Draw apparatus:
base = box(pos=vector(0,0,0), size=vector(30,2,20), color=color.yellow)
rod_actual = cylinder(pos=vector(base.pos.x-5,0,0), axis=vector(0,65,0), radius=1, color=color.blue)
rodtop_support = cylinder(pos=vector(rod_actual.pos.x-5,rod_actual.axis.y-5,0), axis=vector(25,0,0), radius=1, color=color.blue)
motiondetector = box(pos=vector(10,4,0), size=vector(6,6,6), color=color.gray(0.5))
motiondetector_foil = cylinder(pos=vector(motiondetector.pos), axis =vector(0,3.1,0), radius = 2, color=color.white)
object = cylinder(pos=vector(10,37,0), axis =vector(0,-8,0), radius = 3, color=color.red, opacity=1)
model = cylinder(pos=vector(1,37,0), axis =vector(0,-8,0), radius = 3, color=color.blue, opacity=1,visible=False)
model.p = 0
spring = helix(pos=vector(10,rodtop_support.pos.y,0), axis=vector(0,-1,0), coils=20, radius=1)
spring.length = 65-object.pos.y 
spring.pos.y = rodtop_support.pos.y - rodtop_support.radius #move the spring y position to the underside of the top support
model_spring = helix(pos=vector(1,rodtop_support.pos.y,0), axis=vector(0,-1,0), coils=20, radius=1,visible=False)
model_spring.length = 65-object.pos.y 
model_spring.pos.y = rodtop_support.pos.y - rodtop_support.radius #move the spring y position to the underside of the top support

v_arrow = arrow(position =vector(15,0,0),axis=vector(0,1,0), color=color.black, shaftwidth=1,visible=False)
a_arrow = arrow(position =vector(-17,0,0),axis=vector(0,1,0), color=color.green,  shaftwidth=1,visible=False)
v_arrow.pos.x = 17
a_arrow.pos.x = 6
v_label = label(pos=vec(26,40,10), text='velocity\n(black)')
a_label = label(pos=vec(-25,40,10), text='acceleration\n(green)')
ks = str(k)
k_label = label(pos=vector(-25,60,10), text='k = '+str(k)+ 'N/m',visible=True)

# add a checkbox to the canvas so the user can choose to add a model plot on the graph
def checkbox_code(r):
    print(r.checked) # alternates   
modeling_checkbox = checkbox(bind=checkbox_code, text='model this run of data') # text to right of checkbox
modeling_checkbox.checked = True

#set up graph:
tmax = 10 
my_graph = graph(width=400, height=300,
    title='Height vs time; red=real data, blue=model',
    xtitle='Time', ytitle='Position', scroll=True, xmin=0, 
    xmax=tmax,  ymin=0, ymax=50,fast=False, align='left')
g = gcurve(color=color.red)
gg = gcurve(color=color.blue)

# Setting up for data collection:
previous_height = object.pos.y 
previous_v = 0
v_arrow.visible = True
a_arrow.visible = True
model.p = 0
model.pos.y = ymax

gdx.start(50) # 50 ms period = 20 samples/sec. Note it can be changed by the slider
while gdx.vp_close_is_pressed() == False:  
    i = 0
    while gdx.vp_collect_is_pressed() == True: 
        # clear the graph on the first iteration
        if i == 0:
            g.delete()
            gg.delete()
            my_graph.xmin = 0
            my_graph.xmax = tmax
            t = 0
            model.p = 0
            model.pos.y = ymax
            model.visible = False
            model_spring.visible = False
            k_label.visible = False     
        dt = gdx.vp_get_slider_period()/1000  # get the period(ms) and convert to seconds
        measurements = gdx.read()    # 'measurements' is a list - one data point per sensor
        if measurements == None:
            break 
        #print(measurements)
        height = measurements[0]*100   # read the new data; use cm for this program
        object.pos.y = height
        spring_length = 65 - object.pos.y
        if spring_length > 0:  # Do not want to invert the spring
            spring.length = spring_length
        v = (height-previous_height)/dt
        a = (v-previous_v)/dt
        v_arrow.pos.y = height
        v_arrow.axis.y = v/6 #this is velocity; the divisor is just a scaling factor
        a_arrow.pos.y = height
        a_arrow.axis.y = a/20 #this is acceleration; the divisor is just a scaling factor
        g.plot(t, height)
        previous_height = height
        previous_v = v
        if modeling_checkbox.checked:
            model.visible = True
            model_spring.visible = True
            k_label.visible = True
            Fe = -k*(model.pos.y-y0) # forces acting on the system (elastic force)
            model.p = model.p + Fe*dt # update the momentum
            model.pos.y = model.pos.y+model.p/mass_of_object *dt
            model_spring.length = 65-model.pos.y
            gg.plot(t, model.pos.y)
        t = t + dt
        i += 1
    
    
         
