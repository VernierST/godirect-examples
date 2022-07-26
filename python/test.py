from vpython import *   # all of the vpython calls are now in gdx, so 
# don't need this import here until the user gets more sophisticated 
# with their vpython canvas, etc..

from gdx_modules import gdx
gdx = gdx.gdx()

# this would place the canvas above the buttons
# c2 = canvas(width=200, height=200)
# b = box(size=0.1*vec(1,1,1), color=color.red)
# c3= canvas(width=200, height=200, range=0.25,background=color.cyan)

# remove vpython = True and instead load that automatically in gdx.vp_setup()
#gdx.open(connection='ble', device_to_open='GDX-FOR 071000U9', vpython=True)
#gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9', vpython=True, canvas=c2)
gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9', vpython=True)
#gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9', vpython=True, canvas=None)
# this would place it below the buttons
# c2 = canvas(width=200, height=200)
# b = box(size=0.1*vec(1,1,1), color=color.red)
# graph_canvas = canvas(width=250, height=250, range=0.25)
# graph_canvas.select()
# gdx_graph = graph(canvas=graph_canvas, xtitle='Time', ytitle='Position', scroll=True,
#         width=400, xmin=0, xmax=5, fast=False)
# g = gcurve(color=color.red)

gdx.select_sensors([1])

gdx.vp_setup(graph=True)

# don't call start() until after vpython=True has been set
gdx.start(period=250)    # Set the rate for data collection

# rate(50) is now in gdx_vpython
#g.plot(0,0)
#g.delete()
i=0 
while not gdx.vp_close_button(): 
    #g.delete()  
    
    while gdx.vp_collect_button():
        #gdx.read_ch()
        print("start collecting")
        measurements = gdx.read()
        if measurements == None:
            break 
        gdx.vp_graph(measurements[0])
        #g.plot(i, measurements[0])
        print(measurements)
        i+=1
        
    #print("loop running")

print("Done")
