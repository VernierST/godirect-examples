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
gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9')
#gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9', vpython=True, canvas=None)
# this would place it below the buttons
# c2 = canvas(width=200, height=200)
# b = box(size=0.1*vec(1,1,1), color=color.red)
# graph_canvas = canvas(width=250, height=250, range=0.25)
# graph_canvas.select()
# gdx_graph = graph(canvas=graph_canvas, xtitle='Time', ytitle='Position', scroll=True,
#         width=400, xmin=0, xmax=5, fast=False)
# g = gcurve(color=color.red)

gdx.select_sensors(1)

gdx.vp_setup(buttons=True, slider=True, meters=True, graph=True)

# don't call start() until after vp_setup() has been called
gdx.start(period=1000)    # Set the rate for data collection

# rate(50) is now in gdx_vpython
#g.plot(0,0)
#g.delete()

while gdx.vp_close_is_pressed() == False:  # Run the main loop until the user clicks the Close button
    while gdx.vp_collect_is_pressed() == True:   # Run the inner loop only when user clicks Collect button     
        measurements = gdx.read()
        if measurements == None:
            break 
        gdx.vp_graph(measurements)
        gdx.vp_meter(measurements)
        #print(measurements)

# if there are no buttons, can still send data to the graph
# for i in range(0,20):
#     measurements = gdx.read()
#     if measurements == None:
#         break 
#     gdx.vp_graph(measurements[0])
#     print(measurements)
    
# these can be removed when using the vpython Close button (is that okay?)        
# gdx.stop()
# gdx.close()

print("Done")
