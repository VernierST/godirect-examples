'''
This example assumes the Go Direct sensor is connected via bluetooth (ble), using 
the gdx.open_ble() function in place of gdx.open_usb() function.

When using gdx.open_ble(), note that there are a few options:

gdx.open_ble() - When there are no arguments, the function finds all available Go Direct 
                ble devices, prints the list to the terminal, and prompts the user
                to select the device to connect.

gdx.open_ble("GDX-FOR 071000U9") - Use your device's name as the argument. The function will
                search for a ble device with this name. If found it will connect it.

gdx.open_ble("proximity_pairing") - Use "proximity_pairing" as the argument. The function will
                find the ble device with the strongest rssi (signal strength) and connect that
                device.

Note the example also uses gdx.device_info() and gdx.enabled_sensor_info() to get device 
and sensor information.

**** go to the gdx.open_ble() function and delete "GDX-FOR 071000U9" and 
replace it with your device's name (order code followed by a blank space followed by 
the serial number) or "proximity_pairing", or leave it blank. 

'''

from gdx import gdx
gdx = gdx.gdx()

gdx.open_ble("GDX-FOR 071000U9") #replace "GDX-FOR 071000U9" with the name of your device (order code, space, serial number)

device_info = gdx.device_info() # device_info list [0 = name, 1 = description, 2 = battery %, 3 = charger state, 4 = rssi]
battery_level = device_info[2]
charger_state = device_info[3]  
print("battery level % = ", battery_level)
print("charger state = ", charger_state)

gdx.select_sensors([1,2])
gdx.start(period=500) 
column_headers = gdx.enabled_sensor_info()
print(column_headers)

for i in range(0,5):
    measurements = gdx.read() 
    if measurements == None: 
        break
    print(measurements)

gdx.stop()
gdx.close()