#from vpython import *   # all of the vpython calls are now in gdx, so 
# don't need this import here until the user gets more sophisticated 
# with their vpython canvas, etc..

from gdx_modules import gdx
gdx = gdx.gdx()

# remove vpython = True and instead load that automatically in gdx.vp_setup()
#gdx.open(connection='ble', device_to_open='GDX-FOR 071000U9', vpython=True)
gdx.open(connection='usb', device_to_open='GDX-MD 0B1008M1', vpython=True)
gdx.vp_setup()
gdx.select_sensors([5])

# don't call start() until after vpython=True has been set
gdx.start(period=250)    # Set the rate for data collection

# rate(50) is now in gdx_vpython
while not gdx.vp_close_button():    
    while gdx.vp_start_button():
        #gdx.read_ch()
        print("start")
        measurements = gdx.read()
        if measurements == None:
            break 
        print(measurements)
        
    print("loop running")

print("Done")
