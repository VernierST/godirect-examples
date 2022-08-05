#from vpython import *   

from gdx_modules import gdx
gdx = gdx.gdx()


gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9')
gdx.open(connection='usb', device_to_open='GDX-VOLT 0G1002Z8')
gdx.select_sensors([[1],[1]])

# gdx.vp_setup()
# #gdx.vp_setup()

# # c2 = canvas(width=300, height=200)
# # b = box(size=0.1*vec(.5,.5,.5), color=color.red)

# # don't call start() until after vpython=True has been set
# gdx.start(period=250)    # Set the rate for data collection

# while gdx.vp_close_button() == False: 
#     while gdx.vp_collect_button() == True:
#         #gdx.read_ch()
#         print("start collecting")
#         measurements = gdx.read()
#         if measurements == None:
#             break 
#         #gdx.vp_graph(measurements[0])
#         print(measurements)

gdx.close()