# Getting Started with Vernier Go Direct® Sensors and VPython

The examples in this folder demonstrate some more advanced uses of Go Direct devices and Python. Most of these examples use the local module named `gdx` that can be found in the [../gdx/](../gdx) folder. Many of these examples may also require that you install other dependencies to get them to work. You should be able to use `pip` to install these, as needed.


VPython is a Python module that you can download to add great graphics to your Python programs. We use it in many of the examples we have posted on our websiteweb site.  Here are some screenshotsscreens of VPython  programs collecting data from our GDX sensors:

  
 


We have added functions to our gdx.py file to make VPython easy to display use in collecting data from GDX sensors in a variety of ways.
If you want to use the VPython features described below, you will need to install VPython. To do so use this command in a terminal program:
Pip3 install vpython
The example program gdx_getting_started_vpython will demonstrate many of nice features of our GDX sensors when used with VPython.
 Let’s take a look at the gdx_getting_started_vpython program, line by line. Most of it is the same as the getting_started_usb program discussed earlier. The only new lines of code are in bold.
 
from vpython import *   
from gdx import gdx
gdx = gdx.gdx()
gdx.open(connection='usb')
gdx.select_sensors()
gdx.vp_vernier_canvas()    
b = box(size=0.1*vec(1,1,1), color=color.red)
gdx.start(period=250)
 
while gdx.vp_close_is_pressed() == False:
    while gdx.vp_collect_is_pressed() == True:       
        measurements = gdx.read()   
        print(measurements)
        if measurements == None:
            break 
        gdx.vp_meter(measurements)   
        sensor0_data =  measurements[0]  
        b.length = 0.1 * sensor0_data   
 
Notice that this program is not much longer than the earlier getting_started_usb program listed above, but it has a lot of new features,
 
The function gdx.vp_vernier_canvas() adds some features that are often nice for programs involving data collection.  The default form:
 
gdx.vp_vernier_canvas()  
will set up a display like this:
 
 
Any GDX data collection program can then be set up so that the COLLECT button starts data collection. It will change to STOP and then you can stop data collection. These operations can be repeated as you like. The CLOSE button will nicely shut down the GDX connection with the computer. 
 
Notice on the sample screen above there is a slider to the right of the buttons than can be used to control the data collection rate of the GDX sensor.
 
Another feature that you get by using the gdx.vp_vernier_canvas() function is a live display of GDX sensor readings, when you are not collecting data. Here is an example, when using a GDX-FOR sensor.
 
 
By default, this display will be active, reading the sensor, when you are not collecting data. You can have it active while collecting data if you add code like this in your data collection loop:
       measurements = gdx.read()    # 'measurements' is a list 
       if measurements == None:
            break
      gdx.vp_meter(measurements)
 
You can also add a graph by adding "graph=True" to the  gdx.vp_vernier_canvas() function. The function  gdx.vp_vernier_canvas(graph=True)  yields:
 
 
The complete format for the gdx.vp_vernier_canvas function is:
gdx.vp_vernier_canvas(buttons=True, meters=True, slider=True, graph=False)
 
The statement above has the default settings. In short, you will get the buttons, slider, and meters by default, and you have to specifically turn on the graph feature, if you want it.
 



## License

All of the content in this repository is available under the terms of the [BSD 3-Clause License](../LICENSE).

Vernier products are designed for educational use. Our products are not designed nor are they recommended for any industrial, medical, or commercial process such as life support, patient diagnosis, control of a manufacturing process, or industrial testing of any kind.
