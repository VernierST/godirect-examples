from gdx_modules import gdx
gdx = gdx.gdx()


gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9')
gdx.select_sensors([1])
gdx.vp_setup(buttons=True, graph=False)

# don't call start() until after vp_setup()
gdx.start(period=250) 

# Note that the Close button will also call gdx.close() to shut down the hardware properly
while gdx.vp_close_button() == False:  # Run the main loop until the user clicks the Close button
    # Note that the Collect/Stop button will also call gdx.start() and gdx.stop()
    while gdx.vp_collect_button() == True:   # Run the inner loop only when user clicks Collect button
        #gdx.read_ch()
        print("start collecting")
        measurements = gdx.read()
        if measurements == None:
            break 
        print(measurements)

# do not need to call gdx_stop() and gdx_close() because that code is 
# called when user clicks the buttons.