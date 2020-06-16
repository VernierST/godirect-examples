'''
In this example we are saving the data to a csv file to be opened with Excel.

'''

from gdx import gdx 
gdx = gdx.gdx()

import csv
import os

#gdx.open_usb() 
gdx.open_ble()  # Comment this out if you decide to use the gdx.open_usb() function instead.

gdx.select_sensors()

with open('csvexample.csv', 'w', newline='') as my_data_file:
# The commented-out code below would be used if you want to hard-code in an absolute file path for the location of the csv file...
#with open('C:/full/path/to/your/documents/folder/csvexample2.csv', 'w', newline='') as my_data_file:    
    csv_writer = csv.writer(my_data_file)

    gdx.start(period=200) 
    column_headers = gdx.enabled_sensor_info()
    csv_writer.writerow(column_headers)

    for i in range(0,40):
        measurements = gdx.read() 
        if measurements == None: 
            break
        csv_writer.writerow(measurements)
        print(measurements)

gdx.stop()
gdx.close()

# If you did not hard-code in an absolute path, this is where the file should be found.
print("location of current working directory = ", os.getcwd()) 