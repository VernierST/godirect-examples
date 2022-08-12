from gdx import gdx
gdx = gdx.gdx()


# MODIFY THIS! Set the connection = 'usb' or 'ble'. 
# Enter the serial number for your devices, separated by a comma
# (e.g., device_to_open='GDX-FOR 071000U9, GDX-HD 151000C1').
# Note that the first device in the string will be the first device to be opened.
gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9, GDX-MD 0B1008R4')

# MODIFY THIS! Enter the sensors for multiple devices using a 2D list 
# e.g., gdx.select_sensor([[1,2], [1]]), where the first list corresponds to the sensors 
# of the first opened device. 
gdx.select_sensors([[1,2], [5]]) 

# Set the rate for data collection. This is the period in milliseconds.
gdx.start(period=1000)    

# 'column_headers' is a string with the description and units of each selected 
# sensor from each device. When there are multiple sensors this is returned as a 1D list.
column_headers= gdx.enabled_sensor_info()

for i in range(0,5):
    # 'measurements' is a 1D list containing a single data point from each sensor from each device 
    measurements = gdx.read()
    if measurements == None:
        break    
    # index out the 3 sensor values from the measurements list
    print(measurements[0], column_headers[0])   # first device, first sensor's value 
    print(measurements[1], column_headers[1])   # first device, second sensor's value
    print(measurements[2], column_headers[2])   # second device, first sensor's value
           
# Stop collecting data from the sensor
gdx.stop()

# Disconnect the Go Direct connection
gdx.close()