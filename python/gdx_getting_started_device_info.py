''' 
This example lists information about the Go Direct device and all of the sensor channels.

"Incompatible sensors" refers to sensor channels that cannot operate at the
same time. Most devices allow all sensor channels to collect data at 
the same time. However, devices like Sound and EKG have some sensors that do not work
when the other on-board sensors are collecting data.

Also note that not all devices have sensor numbers that start with 1, and not all
numbers are used. For example, Light and Color sensor numbers are [1,2,5,6,7]. 
Motion Detector sensor numbers are [5,6,7].

This example highlights the use of the following gdx functions:

gdx.device_info()
gdx.sensor_info()
gdx.enabled_sensor_info()

Note: This example assumes one Go Direct device
'''

from gdx import gdx
gdx = gdx.gdx()

#gdx.open_usb() #uncomment this function and comment out the ble function if you wish to connect via USB
gdx.open_ble() 

# Return the device_info list [name, description, battery %, charger state, rssi]
input('press enter to get device info')
device_info = gdx.device_info() 
device_name = device_info[0]
device_description = device_info[1]  
battery = device_info[2]  
charger_state = device_info[3]
rssi = device_info[4]  
print("device name = ", device_name)
print("device description = ", device_description)
print("battery charge % = ", battery)
print("charging state of the battery = ", charger_state)
print("rssi (bluetooth signal) = ", rssi)
print()

# Return the sensor_info list [sensor number, description, units, incompatible sensors[]]
input('press enter to get sensor info')
sensor_info = gdx.sensor_info() 
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


# The gdx.enabled_sensor_info() function returns each enabled (selected) sensors' description and units. 
# This might be useful as a column header. Note that you need to select sensors using the select_sensors()
# function before calling gdx.enabled_sensor_info() function. 
input('press enter to choose sensor(s) and get column headers')
gdx.select_sensors()  
column_headers= gdx.enabled_sensor_info()
print("column headers = ", column_headers)

gdx.stop()
gdx.close()