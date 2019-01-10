'''
In this example we are saving the data to a csv file to be opened with Excel.

'''

from gdx import gdx 
gdx = gdx.gdx()

import csv

myFile = open('csvexample.csv', 'w', newline='') 
writer = csv.writer(myFile)

gdx.open_usb()
gdx.select_sensors([1,2])
gdx.start(period=500) 
column_headers = gdx.enabled_sensor_info()
writer.writerow(column_headers)

for i in range(0,5):
    measurements = gdx.read() 
    if measurements == None: 
        break
    writer.writerow(measurements)
    print(measurements)

gdx.stop()
gdx.close()