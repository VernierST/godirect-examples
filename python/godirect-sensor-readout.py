# -*- coding: utf-8 -*-

""" This example automatically finds the nearest GoDirect device
and starts reading measurements from the default sensor at
the typical data rate. The first USB device found will be used,
or if no USB devices are found, then the BLE device
with the strongest signal over -100dB is used.

Installation of the Python module:
# pip install godirect
"""

from godirect import GoDirect

import logging
logging.basicConfig()
#logging.getLogger('godirect').setLevel(logging.DEBUG)
#logging.getLogger('pygatt').setLevel(logging.DEBUG)

godirect = GoDirect(use_ble=True,use_usb=True)
print("GoDirect v"+str(godirect.get_version()))

print("\nSearching...", flush=True, end ="")
device = godirect.get_device(threshold=-100)
if device != None and device.open() and device.start():
        print("connecting.\n")
        sensors = device.get_enabled_sensors()
        print("Connected to "+device.name)
        print("Reading 10 measurements\n")
        for i in range(0,10):
                if device.read():
                        for sensor in sensors:
                                print(sensor.sensor_description+": "+str(sensor.value))
        device.stop()
        device.close()
        print("\nDisconnected from "+device.name)
else: 
        print("device not found.")
godirect.quit()
