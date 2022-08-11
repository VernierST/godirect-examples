from gdx import gdx
gdx = gdx.gdx()


# Set the connection = 'usb' or 'ble'.
# MODIFY device_to_open with your device's serial number (e.g., device_to_open='GDX-FOR 071000U9')
gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9')

# Multiple sensors for one device are entered as a list (e.g., [1,3,4,5])
gdx.select_sensors([1,2]) 

# Set the rate for data collection. This is the period in milliseconds.
gdx.start(period=1000)    

# 'column_headers' is a string with the description and units of each selected 
# sensor. When there are multiple sensors this is returned as a 1D list.
column_headers= gdx.enabled_sensor_info()

for i in range(0,5):
    # 'measurements' is a 1D list containing a single data point from each sensor 
    measurements = gdx.read()
    if measurements == None:
        break    
    # print the data point from each sensor
    print(measurements[0], column_headers[0])    
    print(measurements[1], column_headers[1])  
           
# Stop collecting data from the sensor
gdx.stop()

# Disconnect the Go Direct connection
gdx.close()