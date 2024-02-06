""" This example automatically connects to a Go Direct device via USB (if USB 
is not connected, then it searches for the nearest GoDirect device via Bluetooth)
and starts reading measurements from the default sensor at a period of 
1000ms (1 sample/second). Unlike the 'gdx_getting_started' examples that use the gdx module,
this example works directly with the godirect module. This example might
be important for troubleshooting, or if you do not want to use the gdx module.

If you want to enable specific sensors, you will need to know the sensor numbers.
Run the example called 'gdx_getting_started_device_info.py' to get that information.

Installation of the godirect package is required using 'pip3 install godirect'
"""

from godirect import GoDirect

import logging
logging.basicConfig()
#logging.getLogger('godirect').setLevel(logging.DEBUG)
#logging.getLogger('bleak').setLevel(logging.DEBUG)
#logging.getLogger('pygatt').setLevel(logging.DEBUG)

# The first USB device found will be used. If no USB devices are found, then 
# the BLE device with the strongest signal over -100 is used.
# Note that you can choose to enable USB, BLE, or both. By default both will be enabled.
godirect = GoDirect(use_ble=True, use_usb=True)
print("GoDirect v"+str(godirect.get_version()))
print("\nSearching...", flush=True, end ="")
device = godirect.get_device(threshold=-100)
 
# Once a device is found or selected it must be opened.
if device != None and device.open(auto_start=False):
        print("connecting.\n")
        print("Connected to "+device.name)

        # A specific sensor (or sensors) can be selected for data collection by calling
        # device.enable_sensors([]) prior to calling device.start().
        # If you do not use device.enable_sensors([]), the default sensor(s) will be automatically
        # enabled when device.start() is called. 

        #device.enable_sensors([1,2])    # Uncomment this line if you want to enable specific sensors
        device.start(period=1000) 
        print("start")
        sensors = device.get_enabled_sensors()   # after start() is called, an enabled sensor list is available
                
        print("Reading measurements\n")
        for i in range(0,10):
                if device.read():
                        for sensor in sensors:
                                # The 'sensor.values' call returns a list of measurements. This list might contain 
                                # one sensor value, or multiple sensor values (if fast sampling)
                                print(sensor.sensor_description+": "+str(sensor.values))                  
                                sensor.clear()
        device.stop()
        device.close()
        print("\nDisconnected from "+device.name)

else:
        print("Go Direct device not found/opened")

godirect.quit()


