# Note: If meters are configured, they will monitor sensor
# readings during data collection and when data collection has been stopped.
# Note: A vpython rate(50) call is coded inside the gdx.vp_collect_is_pressed()
# and therefore a rate() call should not be needed in this code.
# Note: do not call the gdx.start() function until after vp_vernier_canvas()

from vpython import *   

from gdx import gdx
gdx = gdx.gdx()

# MODIFY THIS! Set the connection = 'usb' or 'ble'. 
# Set device_to_open with your device's serial number (e.g., device_to_open='GDX-FOR 071000U9')
gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9')

# MODIFY THIS! Put your sensor number here. Note that when you are reading from just one
# sensor you can just enter the sensor number. If you are reading from multiple 
# sensors they would need to be input as a list (e.g., [1,2,3])
gdx.select_sensors(1)

# setup a vernier vpython canvas to control data collection (Collect/Stop button, 
# Close button, sampling speed control, and live meter readout). 
gdx.vp_vernier_canvas()

# setup a vpython canvas with a box object
c = canvas(width=800, height=150, range=0.25)
c.caption = 'click COLLECT button to move the box with the sensor reading'
b = box(size=0.1*vec(1,1,1), color=color.red)

gdx.start(period=1000) 

# The main loop runs until the user clicks the Close button.
while gdx.vp_close_is_pressed() == False:  
    # The inner loop runs when the user clicks the Collect button, and continues
    # to run until the user clicks the Stop button.
    while gdx.vp_collect_is_pressed() == True:       
        # when there is only 1 sensor configured, 'measurements' is a single value (not a list)
        measurements = gdx.read()
        print(measurements)
        if measurements == None:
            break 
        gdx.vp_meter(measurements)
        b.pos.x = 0.1 * measurements    # modify the multiplier or create a new equation

