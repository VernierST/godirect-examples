from vpython import *

from gdx_modules import gdx
gdx = gdx.gdx()


gdx.open(connection='ble', device_to_open='GDX-FOR 071000U9', vpython=True)
gdx.select_sensors([1])
gdx.start(period=250)    # Set the rate for data collection

while gdx.vp_close_button() == False:    
    #print("close button = False")
    rate(50)
    if gdx.vp_start_button() == True:
        #gdx.read_ch()
        print("start")
        measurements = gdx.read()
        if measurements == None:
            break 
        print(measurements)
        
    print("loop running")

print("Done")
