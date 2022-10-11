# Getting Started with Vernier Go Direct® Sensors and VPython

This guide describes the use of Go Direct sensor data with the VPython module. The VPython module makes it possible, and easy, for a Python program to generate navigable real-time 3D animations. This is a great tool to illustrate physics concepts.

Note that this guide is for using VPython with the installed Python language on one's computer. There is a separate guide for using Go Direct sensors with "Web VPython", which runs in the browser and allows the user to write and run a VPython program without actually installing Python itself. This provides a great advantage in the classroom - you do not need to install anything on your computer to immediately run. Another advantage is that the Web VPython version will work on Chromebooks as well as Mac, Windows, and Linux computers. See: XXXXXXXXXXXXXXX

## Getting Started Requirements

The VPython examples in this folder use the local module named `gdx` that can be found in the [../gdx/](../gdx) folder. The examples assume the `gdx` folder is located one directory up. If you move the `gdx` folder to a different location, make sure to modify the example accordingly.

The VPython module must be installed to run the examples. Run the following command in Powershell or Command Prompt to install the VPython module:

`pip install vpython`

## Coding Go Direct Sensors with VPython

![VPython with box](../images/vpython_box.png = 400x100)

We have added functions to our gdx.py file to make it easy to collect and display data from Go Direct sensors in a VPython canvas. 

In a typical program you will first import vpython and import gdx. After the import, a typical program will look similar to the snippet below. In this example, the length of the VPython box object is controlled by the sensor data:

```python
gdx.open(connection='usb')
gdx.select_sensors()
gdx.vp_vernier_canvas()    
b = box(size=0.1*vec(1,1,1), color=color.red)
gdx.start(period=250)
 
while gdx.vp_close_is_pressed() == False:
    while gdx.vp_collect_is_pressed() == True:       
        measurements = gdx.read()   
        gdx.vp_meter(measurements)   
        sensor0_data =  measurements[0]  
        b.length = 0.1 * sensor0_data 
```



## Notes Regarding the gdx VPython Functions 

The code snippet above uses functions available in the gdx module that provide some convenient features for your VPython program. Here is some more information about the functions:

### `gdx.vp_vernier_canvas()` 
- Use this function to add VPython objects that are useful for data collection to the VPython canvas.
- If this function’s argument is left blank, the following objects will be placed onto the VPython canvas:

![VPython canvas](../images/vpython_buttons_slider_meter.png = 400x200)

  - COLLECT/STOP button
    - Click this button to start and stop data collection
  - CLOSE button
    - Click this button to end your VPython session, disconnect the Go Direct device from the USB or Bluetooth connection, and quit godirect.
  - Slider
    - Modify the data collection sampling rate with this slider.  
  - Live meter readout
    - This VPython object provides a live display of the Go Direct sensor reading, when you are not collecting data. This can be useful for configuring your experiment prior to starting data collection.  
    - If you would like the meter to also be active during data collection you will place the `gdx.vp_meter(measurements)` function in the data collection loop.
- The default settings for the arguments are as follows:
`vp_vernier_canvas(buttons=True, slider=True, meters=True, graph=False, cvs=True)`
- The buttons, slider, and live meter were discussed above. You can disable these VPython objects by setting `buttons=False`, `slider=False`, or `meters=False`
- Set `graph=True` to include a VPython graph object on the canvas.

![VPython with graph](../images/vpython_graph.png =400x500)

  - To make the graph active during data collection you will place the 
    `gdx.vp_graph(measurements)` function in the data collection loop.
- The argument `cvs=True` creates a blank canvas for any VPython objects (such as an arrow, box, sphere, etc..) you would like to include in your program. 
  - If this blank canvas is not needed or causes issues, simply change this to `cvs=False`.

### `while gdx.vp_close_is_pressed() == False`
- The function `gdx.vp_close_is_pressed()` monitors the state of the vpython canvas CLOSE button. 
- When true, this function will call gdx.stop() and gdx.close() to stop data collection and disconnect the device.

### `while gdx.vp_collect_is_pressed() == True`
- The function `gdx.vp_collect_is_pressed()` monitors the state of the vpython canvas COLLECT/STOP button.
- When COLLECT is clicked, the function will call gdx.start(). When STOP is clicked, a 
gdx.stop() is called.

### `gdx.vp_meter(measurements)`
- The live meter will automatically update with sensor readings when you are not performing data collection. If you would like to display data on the meter during data collection, then use the `gdx.vp_meter()` function within your data collection loop.
- The argument for this function is measurement[]: A 1D list of sensor readings. Simply use the 1D list of data that is returned from `measurements = gdx.read()`.
- Make sure that meter=True in the vernier_canvas() function.

### `gdx.vp_graph(measurements)`
- If you would like to display data on the graph during data collection, then use the 
`gdx.vp_graph()` function within your data collection loop.
- The argument for this function is measurements[]: A 1D list of sensor readings. Simply use the 1D list of data that is returned from `measurements = gdx.read()`.
- Make sure that graph=True in the vernier_canvas() function.
- Note that the graph will show up to 3 plots.
 
## Troubleshooting
- If you are familiar with github, you could search the issues or post a question at: https://github.com/VernierST/godirect-examples/issues
- Try a different browser. In most cases using Chrome is suggested.
- Place the `gdx.vp_canvas()` function before `gdx.start()` in your code. This is because there is code in the `gdx.start()` function that checks to see if the data collection rate might be coming from the VPython slider that is configured in `gdx.vp_canvas()`. 
- Write a simple VPython starter program that does not use GO Direct sensors and does not use the functions described above. This can be a good troubleshooting step if you are not sure why VPython is not opening a canvas. Here is an easy example to try:

```python
from vpython import *
sphere()
```

- After running a program the terminal may become unresponsive. If so, delete the terminal and open a new terminal before running the program a second time.
- If any of the vpython functions described here are providing confusion in your program, always recall that you do not need to use them in order to use VPython. 

## License

All of the content in this repository is available under the terms of the [BSD 3-Clause License](../LICENSE).

Vernier products are designed for educational use. Our products are not designed nor are they recommended for any industrial, medical, or commercial process such as life support, patient diagnosis, control of a manufacturing process, or industrial testing of any kind.
