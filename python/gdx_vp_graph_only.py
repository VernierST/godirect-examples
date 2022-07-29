from gdx_modules import gdx
gdx = gdx.gdx()


gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9')
gdx.select_sensors([1])
gdx.vp_setup(buttons=False, graph=True)

# don't call start until after sensors and vp_setup() have been called
gdx.start(period=250) 

for i in range(0,20):
    measurements = gdx.read()
    if measurements == None:
        break 
    gdx.vp_graph(measurements[0])
    print(measurements)
           
gdx.stop()
gdx.close()