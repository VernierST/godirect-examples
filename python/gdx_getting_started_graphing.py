'''
This example collects data from one or more Vernier GDX devices and displays and 
graphs the readings.
Note that if your computer is slow, the graph may not keep up with the data collection.
This program supports up to three sensors.
You can stop data collection with a control-c keypress.

This program uses Pyplot, which is part of MatPlotLib. Pyplot allows hundreds of options for graph style.
See https://matplotlib.org/users/index.html and https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html?highlight=pyplot 
for information.
'''

import time
import matplotlib.pyplot as plt

from gdx import gdx #The gdx function calls are from a gdx.py file inside the gdx folder, which must be with this program.
gdx = gdx.gdx()


fig, ax = plt.subplots()

# CHANGE TO MATCH YOUR EXPERIMENT
time_between_readings_in_seconds = 0.5
number_of_readings = 20
digits_of_precision = 2

gdx.open(connection='usb')   # Use connection='ble' for a Bluetooth connection
#gdx.open(connection='usb', device_to_open='GDX-FOR 071000U9')  # You can also use an argument to specify the device

gdx.select_sensors() # You will be asked to select the sensors to be used. You can select up to three.
#gdx.select_sensors([1]) # You can also use an argument to select sensors. Separate multiple sensors with a comma, ([1,3])

# This gets the name and units of the sensors selected.
column_headers = gdx.enabled_sensor_info() 

# Store the number of sensors. This variable is used in plot_graph() and print_table()
number_of_sensors=len(column_headers)

# Use the columm_headers to create a list of the units for each sensor. 
# Use this list of units in the Collect loop below to add the units to the graph
unit_list = []
units = ''
for headers in column_headers:
    units = str(headers[headers.find('(') : headers.find(')') +1])
    unit_list.append(units)

# Save the column_headers as a string, to be used in the title of the graph
column_headers_string = str(column_headers)
column_headers_string = column_headers_string.replace("'","")
column_headers_string = column_headers_string.replace("[","")
column_headers_string = column_headers_string.replace("]","")

# Variables to store the time and readings from the sensors
sensor_times=[]
sensor_readings0=[]
sensor_readings1=[]   
sensor_readings2=[] 
print_table_string = []

plt.pause(1)

period_in_ms = time_between_readings_in_seconds*1000

#Start data collection at the specified rate. The period argument is in milliseconds
gdx.start(period_in_ms) 

# This graphing function will be used to set up the graph and may be used during data collection to give you 
# a "live" graph. Note that plotting to the graph during data collection may slow the data collection loop.
def plot_graph():
    
    # Customize the graph See Pyplot documentation
    ax.plot(sensor_times,sensor_readings0, color='r',label=column_headers[0]) #red line for sensor 1
    
    # sensor_times and sensor_readings are variables storing the time and measurements from the data collection loop.
    if (number_of_sensors>1):
        ax.plot(sensor_times,sensor_readings1, color='b',label=column_headers[1]) #blue line for sensor 2
    if (number_of_sensors>2):
        ax.plot(sensor_times,sensor_readings2, color='k',label=column_headers[2]) #black line for sensor 3

    plt.ylabel(column_headers_string) #name and units of the sensor selected#
    plt.xlabel('Time(s)')
    plt.grid(True) #This controls whether there is a grid on the graph
    plt.pause (0.05) # display the graph briefly, as the readings are taken


def print_table():
    print ("Data Table:")
    print ('Time (s) ',column_headers_string) #label the data table that will be printed on the Python Shell

    # The print_table_string is a list of strings. Each element in the list contains the time and readings.
    # This variable is created in the Data Collection loop.
    for string in print_table_string:
        print(string)
           
# Data Collection:
collection_complete=False
while not collection_complete:
    try:
        time = 0
        print ('Collecting Data...')

        # Print the column headers, starting with Time(s)
        print('Time(s), ' + column_headers_string) 

        for i in range(0,number_of_readings):
            
            # Create a list of times to be used in the graph and data table.
            sensor_times.append(time)

            # This is where we are reading the list of measurements from the sensors.
            measurements=gdx.read() 
            if measurements == None: 
                break 

            # Store each sensor's measurement in a list to be used in plot_graph() and print_table()
            d = 0
            data_string = ''
            title_string =''
            for data in measurements:
                if d == 0:
                    sensor_readings0.append(data)
                if d == 1:
                    sensor_readings1.append(data)
                if d == 2:
                    sensor_readings2.append(data)

                # Build a string for printing to the terminal and to be used as the title of the graph
                round_data = str(round(data,digits_of_precision))
                data_string = data_string + round_data + '   '
                title_string = title_string + round_data + unit_list[d] + '   '
                d += 1

            # Create a list for the print_table() function. Only used for fast data collection
            if time_between_readings_in_seconds<=0.4:
                print_table_string.append(str(round(time,2)) + '   ' + data_string)

            # For slower data collection, print the data to the terminal and the graph
            if  time_between_readings_in_seconds>0.4:

                # Print the time and the data to the terminal
                print(str(round(time,2)) + '   '+ data_string)

                # If the last reading is finished update the graph's title
                if  i >=number_of_readings-1: 
                    plt.title(column_headers_string +' vs '+'Time (s)')
                
                # If collection is in process, use the data as the graph's title, for real-time updates
                else:
                    plt.title(title_string)
                
                # Call the plot_graph() function to update the graph with the new data set. 
                plot_graph() 

            # Update the time variable with the new time for the next data point
            time = time+time_between_readings_in_seconds 

        # The data collection loop is finished
        collection_complete=True
        print ('data  collection complete')
        print ('Number of readings: ',i+1)
        print ('Time between readings: ',time_between_readings_in_seconds, " s")
        print ('Total time for data collection ', time, ' s')
        
        # Stop sensor readings and disconnect the device.
        gdx.stop()
        gdx.close()
        
        # For fast collection we did not print to the graph during data collection. Now that all data
        # have been collected, send the data to the print_table() and plot_graph() function.
        if  time_between_readings_in_seconds<=0.4:
            print_table()
            plt.title(column_headers[0]+' vs '+'Time (s)') #put a title on the top of graph
            plot_graph()
        

    except KeyboardInterrupt:
        collection_complete=True
        gdx.stop() #Stop sensor readings
        gdx.close()#Disconnect the device
        print ('data  collection stopped by keypress')
        print ('Number of readings: ',i+1)

# Command to leave the graph window open when the program ends.
plt.show()

