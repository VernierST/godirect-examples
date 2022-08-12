# Note: If meters are configured, they will monitor sensor
# readings during data collection and when data collection has been stopped.
# Note: A vpython rate(50) call is coded inside the gdx.vp_collect_is_pressed()
# and therefore a rate() call should not be needed in this code.
# Note: do not call the gdx.start() function until after vp_vernier_canvas()

from vpython import *   

from gdx import gdx
gdx = gdx.gdx()

# MODIFY THIS! Set the connection = 'usb' or 'ble'. 
# Enter the serial number for your device
gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9')

# MODIFY THIS! Enter the sensors for your device
gdx.select_sensors([1,2]) 

# setup a vernier vpython canvas to control data collection (Collect/Stop button, 
# Close button, sampling speed control, and live meter readout). 
gdx.vp_vernier_canvas()

# setup a vpython canvas with an ellipsoid
c = canvas(width=300, height=300)
el = ellipsoid(size=0.1*vec(1,1,1), color=color.red)

# setup a 2nd vpython canvas with a box
c2 = canvas(width=300, height=300)
c.caption = 'click COLLECT button to control the objects'
b = box(size=0.1*vec(1,1,1), color=color.red)

gdx.start(period=1000) 

# The main loop runs until the user clicks the Close button.
while gdx.vp_close_is_pressed() == False:  
    # The inner loop runs when the user clicks the Collect button
    while gdx.vp_collect_is_pressed() == True:       
        # 'measurements' is a 1D list containing a single data point from each sensor 
        measurements = gdx.read()
        print(measurements)
        if measurements == None:
            break 
        gdx.vp_meter(measurements)
        # index out the sensor values from the measurements list
        el.height = measurements[0] 
        b.height = measurements[1]  