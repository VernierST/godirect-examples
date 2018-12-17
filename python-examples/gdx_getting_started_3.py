''' 
Here are the gdx functions used in a typical program to collect data:

gdx.open_usb() or gdx.open_ble()
gdx.select_sensors()
gdx.start()
gdx.read()
gdx.stop()
gdx.close()

Here are other functions that might be useful for customizing a program:

gdx.device_info()
gdx.enabled_sensor_info()
gdx.sensor_info()
gdx.discover_ble_devices()

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

In this example we are highlighting the use of the gdx.sensor_info() function.
Most Go Direct devices have multiple sensors on-board. This program provides information
on the sensor channel number, the description of the sensor, the units and it also
lists the "incompatible sensors". This refers to other sensor channel numbers 
that cannot be used for data collection at the same time as this sensor. Most 
devices allow all sensor channels to collect data at the same time. However, that is
not always the case. Devices like Sound and EKG have some sensors that do not work
together with the other sensors on-board the device.

Also note that not all devices have sensor numbers that start with 1, and not all
numbers are used. For example, Light and Color sensor numbers are [1,2,5,6,7]

'''

from gdx import gdx
gdx = gdx.gdx()

gdx.open_usb()
sensor_info = gdx.sensor_info() # 0 = sensor number, 1 = description, 2 = units, 3 = incompatible sensors 
print()
1
for info in sensor_info:
    sensor_number = info[0]
    sensor_description = info[1]  
    sensor_units = info[2]  
    incompatible_sensors = info[3]  
    print("sensor number = ", sensor_number)
    print("sensor description = ", sensor_description)
    print("sensor units = ", sensor_units)
    print("incompatible sensors = ", incompatible_sensors)
    print()


gdx.close()