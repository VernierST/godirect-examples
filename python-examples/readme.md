# Using Python with Go Direct® Devices

If you are new to Python, you may want to visit our [Getting started with Go Direct and Python page](./godirect-py-getting-started.md) or our [Go Direct FAQ page](./godirect-py-faqs.md) for some tips and troubleshooting ideas.

The examples in this folder will walk you through some of the basics of talking to a Go Direct device using Python. Under the hood, they all use the the [`godirect` module](./gdx) to communicate with the Go Direct devices. However, to make things a bit simpler, we created a layer to abstract some of the details away and provide cleaner paths to the most common functions. That layer is named `gdx` and can be found in the /gdx/ folder. All of the examples in this folder make use of it for a cleaner, simpler entry point into coding with Go Direct devices.

## gdx_getting_started_1.py

The [gdx_getting_started_1.py](https://github.com/VernierST/godirect-examples/blob/master/python-examples/gdx_getting_started_1.py) example shows you how to:
- Connect to a Go Direct device through a USB cable
- Allow the user to select some sensors on the device
- Collect a few measurements from the enabled sensors

## gdx_getting_started_2.py

The [gdx_getting_started_2.py](https://github.com/VernierST/godirect-examples/blob/master/python-examples/gdx_getting_started_2.py) example uses a Bluetooth Low Energy connection and demonstrates how you can:
- Find and connect to a Go Direct device over Bluetooth Low Energy (BLE)
- Obtain some device information, like battery level and RSSI (radio signal strength)
- Select some sensors and set the collection rate
- Collect a few measurements from the enabled sensors

## gdx_getting_started_3.py

The [gdx_getting_started_3.py](https://github.com/VernierST/godirect-examples/blob/master/python-examples/gdx_getting_started_3.py) example highlights using the device information to get some details about the Go Direct device. Most Go Direct devices have multiple sensors on-board. This program provides information on all of the device's sensor channel numbers, the description of the sensors, and the units of measure for each sensor.
- Connect to a Go Direct device through a USB cable
- Obtain and show some device information

## gdx_getting_started_4.py

The [gdx_getting_started_4.py](https://github.com/VernierST/godirect-examples/blob/master/python-examples/gdx_getting_started_4.py) example provides some ideas about what you can do with sensor data by using the the built-in `csv` Python module. It shows you how to:
- Connect to a Go Direct device through a USB cable
- Allow the user to select some sensors on the device
- Collect a few measurements from the enabled sensors and output the data as a comma-separated-value file 