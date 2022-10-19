from vpython import * 
from gdx import gdx
gdx = gdx.gdx()

gdx.open(connection='usb')   # Use connection='ble' for a Bluetooth connection
gdx.select_sensors(5) 

# setup a vernier vpython canvas with buttons to control data collection  
gdx.vp_vernier_canvas()

# setup another  vpython canvas, c2
scene= canvas(width=600, height=400)

def checkbox_code(r):#why can't I put this at the end of the program?
    print(r.checked) # alternates        

#Set up scene:
scene.autoscale=False
scene.title = '<b> Simple Harmonic Motion, with Vectors'
scene.title = '<b> Real Data or Modelling Data'
scene.align = "left"
scene.center = vector(0,30,0)
scene.forward=vector(-.2,0,1)
scene.background = color.white
scene.range=40
scene.camera.angle=(-13.4254, 0, 67.1268)

###############
#Modelling values:
k=19 # Spring constant in N/m (I roughly measured it at 19 N/m for the large brass spring)
#for reasons I do not understand, the modelinng implies about 3 N/m ???
ymax=45.0 # Position of the bottom of the object, when released (it is also the maximum position(cm))
y0 = 40 # Equilibrium position - distance from detector to bottom of object when hanging without oscillating(cm)
mass_of_object =0.5 #object of object on spring in kg
#############
dt=.125
tmax=10
# Draw apparatus:
base = box(pos=vector(0,0,0), size=vector(30,2,20), color=color.yellow)
rod_actual = cylinder(pos=vector(base.pos.x-5,0,0), axis=vector(0,65,0), radius=1, color=color.blue)
rodtop_support = cylinder(pos=vector(rod_actual.pos.x-5,rod_actual.axis.y-5,0), axis=vector(25,0,0), radius=1, color=color.blue)
motiondetector = box(pos=vector(10,4,0), size=vector(6,6,6), color=color.gray(0.5))
motiondetector_foil = cylinder(pos=vector(motiondetector.pos), axis =vector(0,3.1,0), radius = 2, color=color.white)
object = cylinder(pos=vector(10,37,0), axis =vector(0,-8,0), radius = 3, color=color.red, opacity=1)
model = cylinder(pos=vector(1,37,0), axis =vector(0,-8,0), radius = 3, color=color.blue, opacity=1,visible=False)
model.p=0
spring = helix(pos=vector(10,rodtop_support.pos.y,0), axis=vector(0,-1,0), coils=20, radius=1)
spring.length = 65-object.pos.y 
spring.pos.y = rodtop_support.pos.y - rodtop_support.radius #move the spring y position to the underside of the top support
model_spring = helix(pos=vector(1,rodtop_support.pos.y,0), axis=vector(0,-1,0), coils=20, radius=1,visible=False)
model_spring.length = 65-object.pos.y 
model_spring.pos.y = rodtop_support.pos.y - rodtop_support.radius #move the spring y position to the underside of the top support

v_arrow=arrow(position =vector(15,0,0),axis=vector(0,1,0), color=color.black, shaftwidth=1,visible=False)
a_arrow=arrow(position =vector(-17,0,0),axis=vector(0,1,0), color=color.green,  shaftwidth=1,visible=False)
v_arrow.pos.x=17
a_arrow.pos.x=6
v_label=label( pos=vec(26,40,10), text='velocity\n(black)' )
a_label=label(pos=vec(-25,40,10), text='acceleration\n(green)' )
ks=str(k)
k_label=label(pos=vector(-25,60,10), text='k = '+str(k)+ 'N/m',visible=True )
#L = label(pos=vector(-30,2,2),text='') #I got rid of this since we have the motion detector reading built in above    
modeling_checkbox=checkbox(bind=checkbox_code, text='model this run of data') # text to right of checkbox
modeling_checkbox.checked=True

#set up graph:
graph(width=400, height=300,title='Height vs time; red=real data, blue=model',xtitle='Time', ytitle='Position', scroll=True, xmin=0, xmax=tmax,  ymin=0, ymax=50,fast=False, align='left')
g= gcurve(color=color.red)
gg=gcurve(color=color.blue)
# Setting up for data collection:
previous_height=object.pos.y 
previous_v=0
v_arrow.visible=True
a_arrow.visible=True
model.p=0
model.pos.y=ymax
t=0
dt=0.125
units = 'cm'
gdx.start(period=250) 
while gdx.vp_close_is_pressed() == False:  
    while gdx.vp_collect_is_pressed() == True:       
        measurements = gdx.read()    # 'measurements' is a list - one data point per sensor
        if measurements == None:
            break 
        #print(measurements)
        height=measurements[0]*100 # read the new data; use cm for this program
        gdx.vp_meter(measurements)    # display all data in the vernier canvas meter
        #L.text = f'height= {height:.2f}'    #I got rid of this since we have the motion detector reading built in above    
        object.pos.y = height
        spring.length = 65-object.pos.y
        v=(height-previous_height)/dt
        a = (v-previous_v)/dt
        v_arrow.pos.y=height
        v_arrow.axis.y =v/6 #this is velocity; the divisor is just a scaling factor
        a_arrow.pos.y=height
        a_arrow.axis.y=a/20 #this is acceleration; the divisor is just a scaling factor
        t=t+dt 
        g.plot(t, height)
        previous_height=height
        previous_v=v

        if modeling_checkbox.checked:
            model.visible=True
            model_spring.visible=True
            k_label.visible=True
            Fe =-k*(model.pos.y-y0) # forces acting on the system (elastic force)
            model.p = model.p + Fe*dt # update the momentum
            model.pos.y = model.pos.y+model.p/mass_of_object *dt
            model_spring.length = 65-model.pos.y
            gg.plot(t, model.pos.y)
        t=t+dt
    

g.delete()
gg.delete()
t= 0  #for restarting
model.p=0
model.pos.y=ymax
model.visible=False
model_spring.visible=False
k_label.visible=False
         
