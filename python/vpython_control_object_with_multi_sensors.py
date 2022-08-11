from vpython import *   

from gdx import gdx
gdx = gdx.gdx()

# MODIFY device_to_open with your device's serial number (e.g., device_to_open='GDX-FOR 071000U9')
gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9')

# Multiple sensors for one device are entered as a list (e.g., [1,3,4,5])
gdx.select_sensors([1,2,3])

# setup a vernier vpython canvas to control data collection (Collect/Stop button, 
# Close button, sampling speed control, and live meter readout). 
gdx.vp_vernier_canvas(buttons=True, slider=True, meters=True, graph=False)

# setup a vpython canvas with an object
c = canvas(width=500, height=500)
c.caption = 'click COLLECT button to control the object with the sensor readings'
el = ellipsoid(size=0.1*vec(1,1,1), color=color.red)

# don't call start() until after vp_vernier_canvas() has been called
gdx.start(period=1000) 

# The main loop runs until the user clicks the Close button.
# Note that if meters are configured, they will continue to monitor sensor
# readings, even when data collection is stopped.
while gdx.vp_close_is_pressed() == False:  
    # The inner loop runs when the user clicks the Collect button, and continues
    # to run until the user clicks the Stop button.
    while gdx.vp_collect_is_pressed() == True:       
        # 'measurements' is a 1D list containing a single data point from each sensor 
        measurements = gdx.read()
        print(measurements)
        if measurements == None:
            break 
        gdx.vp_meter(measurements)
        # index out the 3 sensor values from the measurements list
        el.length = measurements[0]    # first sensor's value
        el.height = measurements[1]    # second sensor's value
        el.width = measurements[2]    # third sensor's value
    
    