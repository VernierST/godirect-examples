# Using Python with Go Direct® Devices

If you are new to Python, you may want to visit our [Getting started with Go Direct and Python page](./godirect-py-getting-started.md) or our [Go Direct FAQ page](./godirect-py-faqs.md) for some tips and troubleshooting ideas.

The examples in this folder will walk you through some of the basics of talking to a Go Direct device using Python. Under the hood, they all use the [godirect module](https://pypi.org/project/godirect/) to communicate with the Go Direct devices. However, to make things a bit simpler, we created a layer to abstract some of the details away and provide cleaner paths to the most common functions. That layer is named `gdx` and can be found in the [/gdx/](./gdx) folder. All of the examples in this folder make use of it for a cleaner, simpler entry point into coding with Go Direct devices.

For other ideas and more advanced examples, take a look in the [/advanced_examples/](./advanced_examples) folder.

## Example 1: User Prompts and Collecting Data

The [gdx_getting_started_1.py](https://github.com/VernierST/godirect-examples/blob/master/python/gdx_getting_started_1.py) example shows you how to use the gdx functions to:
- Connect to a Go Direct device through a USB cable
- Provide the user with a prompt to select the active sensors
- Provide the user with a prompt to set the measurement period
- Collect a few measurements from the enabled sensors

## Example 2: Setting Defaults and Passing Arguments

The [gdx_getting_started_2.py](https://github.com/VernierST/godirect-examples/blob/master/python/gdx_getting_started_2.py) example shows you how to avoid using prompts (and instead pass arguments) to select the active sensors and set the measurement period:
- Connect to a Go Direct device through a USB cable
- Set the active sensors in your program
- Set the measurement period in your program
- Collect a few measurements from the enabled sensors

## Example 3: Showing Sensor Information

The [gdx_getting_started_3.py](https://github.com/VernierST/godirect-examples/blob/master/python/gdx_getting_started_3.py) example shows how you can use the gdx functions to list information on all of the sensor channels on a Go Direct device. This includes sensor channel number, sensor description, units, and "incompatible sensors".
- Connect to a Go Direct device through a USB cable
- Obtain and show sensor information

## Example 4: Communicating with Go Direct Sensor via Bluetooth

The [gdx_getting_started_4.py](https://github.com/VernierST/godirect-examples/blob/master/python/gdx_getting_started_4.py) example uses a Bluetooth Low Energy (BLE) connection and demonstrates how you can use the gdx functions to:
- Find and connect to a Go Direct device over BLE
- Obtain some device information, like battery level, charger state, and RSSI (radio signal strength)
- Set the active sensors and collection rate
- Collect a few measurements from the enabled sensors

## Example 5: Export Sensor Data as CSV

The [gdx_getting_started_5.py](https://github.com/VernierST/godirect-examples/blob/master/python/gdx_getting_started_5.py) example provides some ideas about what you can do with sensor data by using the built-in csv Python module. It shows you how to:
- Connect to a Go Direct device through a USB cable
- Set the active sensors and collection rate
- Collect a few measurements from the enabled sensors
- Output the data as a comma-separated-value file

## License

All of the content in this repository is available under the terms of the [BSD 3-Clause License](../LICENSE).

Vernier products are designed for educational use. Our products are not designed nor are they recommended for any industrial, medical, or commercial process such as life support, patient diagnosis, control of a manufacturing process, or industrial testing of any kind.
