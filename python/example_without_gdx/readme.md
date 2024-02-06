# Go Direct® Sensor Readout

Simple example of using the [godirect-py module](https://pypi.org/project/godirect/) to connect to a Vernier Go Direct device and log sensor values.

[go-direct-sensor-readout](./godirect-sensor-readout.py)

## API of godirect-py

Connect to the first available USB device, or closest BLE device within the default threshold, and collect 10 samples from the default sensor.
```python
from godirect import GoDirect
godirect = GoDirect()
device = godirect.get_device()
if device != None and device.open(auto_start=True):
	sensors = device.get_enabled_sensors()
	print("Connected to "+device.name)
	print("Reading 10 measurements")
	for i in range(0,10):
		if device.read():
			for sensor in sensors:
				print(sensor.sensor_description+": "+str(sensor.values))
				sensor.clear()
	device.stop()
	device.close()
godirect.quit()
```

Note that you can choose to enable USB, BLE, or both. By default both will be enabled.
```python
godirect = GoDirect(use_ble=True, use_usb=True)
```

Here is how to obtain a list of GoDirectDevice objects from the BLE and/or USB backends.
```python
# returns a list of GoDirectDevice objects
devices = godirect.list_devices()
```

Or you can let the library automatically find the nearest device for you.
```python
# returns a GoDirectDevice on success or None on failure
mydevice = godirect.get_device()

# to adjust the BLE threshold pass in a minimum dB value
mydevice = godirect.get_device(threshold=-200)
```

Once a device is found or selected it must be opened. By default, only information will be gathered on Open. To automatically enable the default sensors and start measurements, set the `open()` parameter to `auto_start=True`. With this parameter set to True there is no need to call the `enable_sensors()` and `start()` functions. Otherwise, if the parameter is set to `auto_start=False`, then you will call the `enable_sensors()` and `start()` functions.
```python
# returns True on success or False on failure
mydevice.open(auto_start=False)
```

Once a device is opened you can obtain a list of sensor objects available on the device.
```python
# returns a list of Sensor objects
sensors = mydevice.list_sensors()
```

Select the sensors you want to enable for data collection. If you do not call this function, then the default sensor(s) will be automatically enabled when `start()` is called.
```python
# pass a list of sensor numbers to enable
mydevice.enable_sensors([2,3,4])
```

Start data collection at the typical rate. If sensors were not enabled, the default sensors will be enabled when start is called.
```python
# start measurements at the typical data rate
mydevice.start() # returns True on success

# start measurements at 1000ms per sample
mydevice.start(period=1000)
```

After `start()` has been called, the enabled sensor objects are available
```python
# get a list of the GoDirectSensor objects that are enabled
mysensors = mydevice.get_enabled_sensors()
```

The `read()` method will block until data is returned so it is acceptable to read in a tight loop.

```python
for i in range(0,10):
	# read() will append new measurement(s) received to the values list in the Sensor object
	if mydevice.read():
		for sensor in mysensors:
			print(sensor.values)
			sensor.clear()
```

The `stop()` method will stop data collection on the device. 

The `close()` method will disconnect the USB or BLE device. 

The `quit()` method will stop the USB or BLE backends gracefully.

## Debugging

godirect uses the standard python logging module. You can set the logging verbosity to INFO or DEBUG to see more communication detail.

```python
import logging
logging.basicConfig()
logging.getLogger('godirect').setLevel(logging.DEBUG)
logging.getLogger('bleak').setLevel(logging.DEBUG)
logging.getLogger('pygatt').setLevel(logging.DEBUG)
```

## License

[BSD 3-Clause License](../../../LICENSE)

Vernier products are designed for educational use. Our products are not designed nor are they recommended for any industrial, medical, or commercial process such as life support, patient diagnosis, control of a manufacturing process, or industrial testing of any kind.

