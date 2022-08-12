# Note: If meters are configured, they will monitor sensor
# readings during data collection and when data collection has been stopped.
# Note: A vpython rate(50) call is coded inside the gdx.vp_collect_is_pressed()
# and therefore a rate() call should not be needed in this code.
# Note: do not call the gdx.start() function until after vp_vernier_canvas()

from vpython import *   

from gdx import gdx
gdx = gdx.gdx()

# MODIFY THIS! Set the connection = 'usb' or 'ble'. 
# Enter the serial number for your devices, separated by a comma
# (e.g., device_to_open='GDX-FOR 071000U9, GDX-HD 151000C1')
gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9, GDX-MD 0B1008M1')

# MODIFY THIS! Enter the sensors for multiple devices using a 2D list 
# e.g., gdx.select_sensor([[1,2], [1]]), where the first list corresponds to the sensors 
# of the first opened device. 
gdx.select_sensors([[1,2], [5]]) 

# setup a vernier vpython canvas to control data collection (Collect/Stop button, 
# Close button, sampling speed control, and live meter readout). 
gdx.vp_vernier_canvas()

# setup a vpython canvas with an object
c = canvas(width=500, height=500)
c.caption = 'click COLLECT button to control length, height, and width with the sensor readings'
el = ellipsoid(size=0.1*vec(1,1,1), color=color.red)

gdx.start(period=1000) 

# The main loop runs until the user clicks the Close button.
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
        el.length = measurements[0]    # first device, first sensor's value
        el.height = measurements[1]    # first device, second sensor's value
        el.width = measurements[2]    # second device, first sensor's value