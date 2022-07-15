from vpython import *

from gdx_modules import gdx
gdx = gdx.gdx()


# Set the rate for data collection
dt_period = 250

gdx.open(connection='ble', device_to_open='GDX-FOR 071000U9', vpython=True)
gdx.select_sensors([1])
gdx.start(period=dt_period)

while gdx.close_vp() == False:
    #print("close button = False")
    rate(50)
    running = gdx.start_vp()
    print("start button = ", running)
    if running == True:
        #gdx.read_ch()
        gdx.read()
        print("start")
    #print("running")

print("Done")
