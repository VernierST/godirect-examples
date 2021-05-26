# To use Go Direct sensors with Python 3 you must install the godirect module
# using pip3 install godirect[usb,ble]
# If you plan to use the native Windows 10 BLE stack, the Bleak module must also 
# be installed using pip3 install bleak

from godirect import GoDirect

import logging
import time                 

logging.basicConfig()
#logging.getLogger('godirect').setLevel(logging.DEBUG)
#logging.getLogger('bleak').setLevel(logging.DEBUG)
#logging.getLogger('pygatt').setLevel(logging.DEBUG)

class gdx:
    
    # Variables passed between the gdx functions.

    # devices - a 1D list of the connected Go Direct device objects.
    devices = []
    # device_sensors - a 2D list of the sensor numbers selected by the user [[1,2],[1]]
    device_sensors = []
    # enabled_sensors - a 2D list of the sensor objects that have been enabled for data collection.
    enabled_sensors = []
    # buffer - a 2D list to store the excess data from a sensor when multi-points are collected from a read due to fast collection.
    buffer = []
    # ble_open - this is a flag to keep track of when godirect is asked to open ble, to make sure it's not asked twice.
    ble_open = False

    def __init__(self):

        self.godirect = GoDirect(use_ble=False, use_usb=False) 
    


    def open_usb(self):
        """ Discovers all Go Direct devices with a USB connection and opens those devices
        for data collection. 
		""" 

        # Call the godirect module to open a USB connection
        self.godirect.__init__(use_ble=False, use_usb=True)

        found_devices = self.godirect.list_devices()
        number_found_devices = len(found_devices)
        print("number of usb devices found = " +str(number_found_devices))

        if number_found_devices == 0:
            print("open_usb() - no device connected")
            gdx.devices = []

        else:
            gdx.devices = found_devices
            print("attempting to open", len(gdx.devices), "device(s)...")
            i=0
            while i < len(gdx.devices): 
                open_device_success = gdx.devices[i].open()
                print("open device ",i, " = ", open_device_success, sep="")
                i +=1               



    def open_ble(self,device_to_open=None):
        """ Open a Go Direct device via bluetooth for data collection. 
        
        Args: 
            device_to_open: Leave this argument blank to provide a list in the termial of all discovered 
            Go Direct devices. The user then chooses the device or devices from the prompt. To run code 
            without a prompt, the argument can be set to a specific Go Direct device name or names. 
            For example,  "GDX-FOR 071000U9" or "GDX-FOR 071000U9, GDX-HD 151000C1". In addition, the argument
            can be set to "proximity_pairing" to open the device with the highest rssi (closest proximity).
		""" 

        if gdx.ble_open == True:
            #print("open_ble() - ble already open")
            return

        print("wait for bluetooth initialization...")
        
        # Tell godirect you want to use ble. If you need to use the Bluegiga dongle, set the 
        # use_ble_bg equal to True (uncomment the command)
        self.godirect.__init__(use_ble=True, use_ble_bg=False, use_usb=False)
        #self.godirect.__init__(use_ble=True, use_ble_bg=True, use_usb=False)
        
        # Find all available bluetooth devices 
        found_devices = self.godirect.list_devices() 
        number_found_devices = len(found_devices)
        print("number of ble devices found = " +str(number_found_devices))
        
        # Was there 1 or more Go Direct ble devices found?      
        if number_found_devices >= 1: 
             
            # The case below occurs when the device_to_open parameter = "proximity_pairing"
            # In the for loop each device, in the list of found_devices, is pulled out one at a time.
            # That device's rssi is compared to the previous highest rssi.
            # The device with the highest rssi is stored as the device to open                
            if device_to_open == "proximity_pairing": 
                print ("begin proximity pairing")
                i=1
                rmax=-99
                dmax=0
                for device in found_devices:
                    print(str(i)+": "+str(device))
                    v=device.rssi
                    if v>rmax:
                        dmax=i
                        rmax=v
                        #print("rmax: ", rmax," dmax: ", dmax)
                    i+= 1
                x=dmax
                selected = int(x)
                if selected <= number_found_devices:
                    gdx.devices.append(found_devices[selected-1])
                    print("proximity device to open = ", found_devices[selected-1] )
                else:
                    print("Error in proximity selection")

            # The case below occurs when the device_to_open argument is given a specific device
            # name or names, such as "GDX-FOR 071000U9" or "GDX-FOR 071000U9, GDX-HD 151000C1"
            # In the for loop each device to open is compared to the devices found in the list of 
            # found_devices. If the names match, then we store the device as a device to open.               
            elif device_to_open != None: 
                device_to_open_list = device_to_open.split(", ")
                print("searching for device(s) ", device_to_open_list)
                for x in device_to_open_list:
                    for device in found_devices: 
                        if x == str(device.name):
                            print("device_to_open_found = True")
                            gdx.devices.append(device)                
            
            # The case below occurs when there is no device_to_open argument. In this case, provide 
            # a list of all discovered ble sensors and the user chooses which device or devices to open.          
            elif device_to_open == None: 
                #print("found " +str(number_found_devices) + " devices:")
                i=1
                for d in found_devices:
                    print(str(i)+": "+str(d))
                    i += 1
                print("Enter device number. To select multiple devices, separate with commas (no spaces):", end=' ')
                user_selected_device = []
                for s in input().split(','):
                    user_selected_device.append(int(s))
                for selected in user_selected_device: 
                    gdx.devices.append(found_devices[selected-1])
   
            # Open the device or devices that were selected in one of the cases above.         
            i = 0
            print("attempting to open", len(gdx.devices), "device(s)...")
            while i < len(gdx.devices): 
                open_device_success = gdx.devices[i].open()
                print("open device ",i, " = ", open_device_success, sep="")
                if open_device_success:
                    gdx.ble_open = True
                time.sleep(1)
                i +=1    
		
        else:
            print("open_ble() - No Go Direct Devices Found on Bluetooth")
     
           

    def select_sensors(self, sensors=None):
        """ Select the sensors you wish to enable for data collection. 
        
        Args: 
            sensors []: if the sensors argument is left blank, a list of all available sensors is provided
            by a prompt in the terminal for the user to select from. To run code without a prompt, set this argument 
            as a 1D list or a 2D list of lists of the sensors you wish to enable, such as [1,2,3] to enable 
            sensors 1,2 and 3 for one device, or [[1,2,3],[1,2]] to enable sensors 1,2 and 3 for one device and 
            sensors 1 and 2 for a second device. 
		""" 

        # First check to make sure there are devices connected.      
        if not gdx.devices:
            print("select_sensors() - no device connected")
            return
        
        # If the sensors argument is left blank provide an input prompt for the user to select sensors
        if sensors == None: 
            i = 0
            while i < len(gdx.devices):
                selected_sensors = []
                print("select sensors for", gdx.devices[i])
                sensors = gdx.devices[i].list_sensors()
                for s in sensors:
                    c = sensors[s]
                    print(str(c))  
                print("Enter sensor number. To select multiple sensors, separate with commas (no spaces):", end=' ')
                for x in input().split(','):
                    selected_sensors.append(int(x))                    
                gdx.device_sensors.append(selected_sensors)
                i += 1   

        # If the user has input a sensor argument it could be a list (1D) or a list of lists (2D). 
        else:
            # If it is a 1D list then len(sensors[0]) will throw an error. If no error then it is 2D.
            try:
                # If this does not throw an error then it is a 2D list
                if len(sensors[0]):
                    # Does this 2D sensor list have a list of sensors for each device? 
                    if len(sensors)!= len(gdx.devices):
                        print("the sensor parameter in select_sensors() does not match number of devices")
                        self.close()
                    else:
                        # Save the 2D list of sensors in device_sensors, such as [[1],[1,2,3]]
                        gdx.device_sensors = sensors
            # The try threw an error. Therefore it is a 1D list of sensors
            except:
                # A 1D list is appropriate if one device is connected. Make sure just one device is connected
                if len(gdx.devices)!= 1:
                        print("the sensor parameter in select_sensors() does not match number of devices")
                        self.close()                   
                else:
                    # Save the 1D list as a 2D list in device_sensors - [[1,2]]
                    gdx.device_sensors.append(sensors)

        #print("sensors for data collection = ", gdx.device_sensors)

        # Enable the sensors that were selected for data collection.
        i = 0
        while i < len(gdx.devices):
            #print("device ",i, " enabled sensors = ", gdx.device_sensors[i], sep="")
            gdx.devices[i].enable_sensors(sensors = gdx.device_sensors[i])
            i +=1

        # The enabled sensor objects are stored in a variable, to be used in the read() function. 
        i = 0
        while i < len(gdx.devices):
            # The variable "enabled_sensors" is a 2D list that stores each device's enabled sensor objects [[obj],[obj,obj]].
            gdx.enabled_sensors.append(gdx.devices[i].get_enabled_sensors())
            i +=1

        
    
    def start(self, period=None):
        """ Start collecting data from the sensors that were selected in the select_sensors() function. 
        
        Args: 
            period (int): If period is left blank, a prompt in the terminal allows the user to enter
            the period (time between samples). To run the code without this prompt, set this argument to 
            a period in milliseconds, e.g. period=1000
		"""        
        
        # First check to make sure there are devices connected.  
        if not gdx.devices:
            print("start() - no device connected")
            return 

        # If the period argument is left blank provide an input prompt for the user to enter the period.
        if period == None: 
            print("select period (ms):", end=' ')
            period = int(input())
            sample_rate = 1/(period/1000)
            print("sample rate = ", sample_rate, "samples/second")
            
        # Provide a warning message if the user is attempting fast data collection
        if period < 10:
            input("Be aware that sampling at a period less than 10ms may be problemeatic. Press Enter to continue ")
        
        # Start data collection (of the enabled sensors) for each active device.
        i = 0
        while i < len(gdx.devices):
            print("start device ", i, sep="")
            gdx.devices[i].start(period=period)
            i +=1            


    
    def read(self):             
        """ Take single point readings from the enabled sensors and return the readings as a 1D list.

        Returns:
		    retvalues[]: a 1D list of sensor readings. A single data point for each enabled sensor.
		"""
        
        retvalues = []  
        values = []       
        
        # First check to make sure there are devices connected.  
        if not gdx.devices:
            print("read() - no device connected")
            return 
        
        # Are there data in the buffer? If so, read the buffer, not the sensor
        if gdx.buffer:
            i = 0
            for i in range(len(gdx.buffer)):
                pop_values = gdx.buffer[i].pop(0)
                retvalues.append(pop_values)
            # if this was the last value in the buffer, clear the list so that it is not a list of empty lists
            if not gdx.buffer[0]:
                gdx.buffer = []
            return retvalues             

        # The buffer is empty, so take readings from the sensor
        else:
            gdx.buffer = [] 
            i = 0
            # Read from each device, one at a time
            while i < len(gdx.devices):
                if gdx.devices[i].read():  
                    sensors = gdx.enabled_sensors[i]
                    # Take readings from each sensor in the device, one at time
                    if sensors:
                        for sensor in sensors: 
                            # The sensor.values call may read one sensor value, or multiple sensor values (if fast sampling)
                            values[:] = sensor.values
                            # Pull the first value off the values list
                            pop_values = values.pop(0)
                            # Build a list of each sensors' first value (this builds the return list)
                            retvalues.append(pop_values)
                            # Build a list of lists for each sensors data that is not returned and put it in the buffer
                            if values:
                                gdx.buffer.append(values)
                            sensor.clear()
                            values = []
                i +=1  
            return retvalues
        

    def readValues(self):             
        """ Take multiple point readings from the enabled sensors and return the readings as a 2D list.

        Returns:
		    retvalues[]: a 2D list of sensor readings. Multiple points for each enabled sensor.
		"""
        
        retvalues = []
        i = 0
        # Read from each device, one at a time
        while i < len(gdx.devices):
            if gdx.devices[i].read():  
                sensors = gdx.enabled_sensors[i]
                # Take readings from each sensor in the device, one at time
                if sensors:
                    for sensor in sensors: 
                        # The sensor.values call may read one sensor value, or multiple sensor values (if fast sampling)
                        retvalues[:] = sensor.values
                        sensor.clear()
            i +=1
        return retvalues

    def listOfListsReadValues(self, dev2=False):             #Ex 11

        """ Same functionality as read() above, however value sensor.values is copied into
        values[] by value instead of by reference, allowing sensor.clear() to be called.
        Only the most recent measurements are returned from readValues() and then cleared
        from both sensor.values and values[]
        Returns:
            value[]: a list that includes a data point from each of the enabled sensors
        """
        '''if dev2 == False: #this first code sets up dev1. If dev2 = True, then do not call this code.
            if gdx.selected_device == None:
                return 
            device = gdx.selected_device

        elif dev2 == True: #is this function being called to configure dev2? then use this code
            if gdx.selected_device2 == None:
                return 
            device = gdx.selected_device2

        retValues = []  

        #if self.selected_device == None:
            #return None
        #if self.selected_device.read():
        if device.read():
            sensors = device.get_enabled_sensors()
            if sensors != None:
                for sensor in sensors: 
                    values = []
                    values[:] = sensor.values                   #New Examples
                    sensor.clear()
                    retValues.append(values)
                return retValues 
        else:
            return None'''


    
    def stop(self):
        """ Stop data collection on the enabled sensors.
		"""       

        # First check to make sure there are devices connected.  
        if not gdx.devices:
            print("stop() - no device connected")
            return
        
        i = 0
        while i < len(gdx.devices):
            print("stop device ",i, sep="")
            gdx.devices[i].stop()
            i+=1



    def close(self):
        """ Disconnect the USB or BLE device and quit godirect.
        """

        # First check to make sure there are devices connected.  
        if not gdx.devices:
            print("close() - no device connected")
            return

        i = 0
        while i < len(gdx.devices):
            print("close device ", i, sep="")
            gdx.devices[i].close()
            i+=1
        gdx.devices = []

        gdx.ble_open = False
        self.godirect.quit()  
        print("quit godirect")



    def device_info(self):
        """ Returns information about the device. The device must be opened first, 
        using the open() function, before this function can be called.

		Returns:
		    device_info[]: a 1D list for one device or a 2D list for multiple. The list
            includes name, description, battery %, charger state, rssi
		"""         

        if not gdx.devices:
            print("device_info - no device connected")
            return

        # The elements in the device_info list are: 0 = name, 1 = description, 2 = battery %, 3 = charger state, 4 = rssi
        device_info = []  
        
        # If there is just one device connected, package the info in a 1D list [device info]
        if len(gdx.devices) ==1:
            device_info.append(gdx.devices[0]._name)
            device_info.append(gdx.devices[0]._description)
            device_info.append(gdx.devices[0]._battery_level_percent) 
            charger_state = ["Idle", "Charging", "Complete", "Error"]  
            device_info.append(charger_state[gdx.devices[0]._charger_state])
            device_info.append(gdx.devices[0]._rssi)
            return device_info  

        # If there is more than one device connected, package the info in a 2D list [[device0 info], [device1 info]]
        else:
            i = 0
            while i < len(gdx.devices):
                one_device_info = []
                one_device_info.append(gdx.devices[i]._name)
                one_device_info.append(gdx.devices[i]._description)
                one_device_info.append(gdx.devices[i]._battery_level_percent) 
                charger_state = ["Idle", "Charging", "Complete", "Error"]  
                one_device_info.append(charger_state[gdx.devices[i]._charger_state])
                one_device_info.append(gdx.devices[i]._rssi)
                i+=1
                device_info.append(one_device_info)
            return device_info            
                


    def enabled_sensor_info(self):
        """ Returns each enabled sensors' description and units (good for column headers).

		Returns:
		    sensor_info[]: a 1D list that includes each enabled sensors' description 
            with units, e.g. ['Force (N)', 'X-axis acceleration (m/s²)']             
		"""                

        if not gdx.devices:
            print("enabled_sensor_info() - no device connected")
            return

        sensor_info = []

        i = 0
        # Get the enabled sensors from each device, one device at a time
        while i < len(gdx.devices):
            sensors = gdx.enabled_sensors[i] 
            for sensor in sensors:
                info = sensor.sensor_description + " (" + sensor.sensor_units + ")"
                sensor_info.append(info)
            i+=1
        return sensor_info



    def sensor_info(self):
        """ Information about all of the available sensors on a connected Go Direct device.

		Returns:
		    available_sensors[]: a 2D list containing information about each 
            sensor found on the device. This includes sensor number, description, units, and 
            a list of incompatible sensors (if any). An incompatible sensor is a sensor that can
            not run at the same time as this sensor. For example, Go Direct EKG cannot run the EKG
            sensor at the same time as the EMG sensor. 
		"""         

        if not gdx.devices:
            print("sensor_info() - no device connected")
            return

        available_sensors = []  
        all_sensor_numbers = []

        i = 0
        # Get the sensors from each device, one device at a time
        while i < len(gdx.devices):
            sensors = gdx.devices[i].list_sensors()
            
            # the all_sensor_numbers list will be used in the code below to determine incompatible sensors
            for x in sensors:
                c = sensors[x]
                number = c.sensor_number
                all_sensor_numbers.append(number)
        
            for x in sensors:
                incompatible_sensors = []
                s = sensors[x]
                number = s.sensor_number
                description = s.sensor_description
                units = s.sensor_units

                # The exclusion_mask is a number that represents sensor numbers that are incompatible with this sensor.
                exclusion_mask = s._mutual_exclusion_mask
                # Convert the exclusion_mask number to a list of Trues and Falses representing the mask.
                bin_string = format(exclusion_mask, '32b')  
                # Reverse the bin_string (with [::-1]) to format it with the most significant bit first.
                # The answer is a True False list [TRUE, TRUE, FALSE]
                answer =  [x == '1' for x in bin_string[::-1]] 
                
                e = 0
                # Change the True/False list to a list of sensor numbers. e.g, [TRUE, TRUE, FALSE] = [1,2]
                # Pull out the True/False values of the list one at a time and if it is TRUE, then add it to 
                # the list of incompatible sensors. 
                for channel in answer: 
                    # If this value of the list is TRUE and it is a confirmed sensor number. 
                    if channel == True and e in all_sensor_numbers: 
                        incompatible_sensors.append(e)
                    e+=1  

                available_sensors.append([number, description, units, incompatible_sensors])
                
            i+=1
        # Return the available_sensor list [0 = sensor number, 1 = description, 2 = units, 3 = incompatible sensors[]]
        return available_sensors


 
    def discover_ble_devices(self, init=True):
        """ Enables bluetooth, and returns the name and rssi of all discovered GoDirect devices. 
        This function should be called prior to opening a device. The name returned 
        by this function can be used as an argurment in the ble_open() function to open a specific device. 

		Returns:
		    discovered_ble_devices[]: a 2D list. A list containing a list of name and rssi for each device
            [[name1,rssi1],[name2,rssi2],[name3,rssi3]]
		""" 
        
        # If you are going to call this several times, there might be a reason to only call the init code once.
        # The first time you call this function set init = True, the following times set init = False.
        if init == True:

            self.godirect.__init__(use_ble=True, use_usb=False)
    
            gdx.ble_open = True

            print("Begin search for ble devices...")
 
        # Find all available bluetooth devices 
        found_devices = self.godirect.list_devices() 
        number_found_devices = len(found_devices)
        #print("Number of ble devices found = " +str(number_found_devices))
        discovered_ble_devices = []
                
        if number_found_devices >= 1:
            for device in found_devices:
                device_name = device.name
                # Note that you can get the rssi from this call before opening the device
                device_rssi = device.rssi
                discovered_ble_devices.append([device_name, device_rssi])
            
        return discovered_ble_devices

   