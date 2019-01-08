''' 
This example lists information about all of the sensor channels on a Go Direct device.
This includes sensor channel number, sensor description, units and "incompatible sensors". 

"Incompatible sensors" refers to sensor channels that cannot operate at the
same time. Most devices allow all sensor channels to collect data at 
the same time. However, devices like Sound and EKG have some sensors that do not work
when the other on-board sensors are collecting data.

Also note that not all devices have sensor numbers that start with 1, and not all
numbers are used. For example, Light and Color sensor numbers are [1,2,5,6,7] and 
Motion Detector is [5,6,7], with each channel being incompatible with the others.

This example highlights the use of the gdx.sensor_info() function.

'''

from gdx import gdx
gdx = gdx.gdx()

gdx.open_usb()
sensor_info = gdx.sensor_info() # 0 = sensor number, 1 = description, 2 = units, 3 = incompatible sensors 
print()

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