''' 
This example lists information about a single Go Direct device and all 
of its sensors.

"Incompatible sensors" refers to sensors that cannot operate at the
same time. Most devices allow all sensors to collect data at 
the same time. However, devices like Sound and EKG have some sensors that do not work
when the other on-board sensors are collecting data.

Also note that not all devices have sensor numbers that start with 1, and not all
numbers are used. For example, Light and Color sensor numbers are [1,2,5,6,7]. 
Motion Detector sensor numbers are [5,6,7].

Note: This example assumes one Go Direct device
'''

from gdx import gdx
gdx = gdx.gdx()


gdx.open(connection='usb')   # change to 'ble' for Bluetooth connection

# Return the device_info list [name, description, battery %, charger state, rssi]
print('\n')
input("Device information (it's especialy important to know the 'device name' \n \
as it is used in other examples as an argument in the gdx.open() function. Be \n \
sure to take note of the 'device name') \n \
   - Press 'enter' \n ")
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
print('\n')

# Return the sensor_info list [sensor number, description, units, incompatible sensors[]]
input("Sensor information (it's especialy important to know the 'sensor number' \n \
as you will use that in python code to specify which sensor to read. Be \n \
sure to take note of the sensor number or numbers) \n \
   - Press 'enter' \n ")
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

# Disconnect the Go Direct connection
gdx.close()