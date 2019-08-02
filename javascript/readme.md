# Getting Started with JavaScript

If you are new to JavaScript, you may want to visit our [Go Direct FAQ page](./godirect-js-faqs.md) for some tips and troubleshooting ideas.

The examples in this folder will walk you through some of the basics of talking to a Go Direct device using JavaScript. 

For other ideas and more advanced examples, take a look in the [/advanced_examples/](./advanced_examples) folder.

## Example 1: Showing Sensor Information
The [gdx_getting_started_1.html](./gdx_getting_started_1.html) example shows how you can use the gdx functions to list information on all of the sensor channels on a Go Direct device. This includes sensor channel number, sensor description, units, and "incompatible sensors".
Connect to a Go Direct device over BLE
Obtain and show sensor information

## Example 2: Using Defaults and Collecting Data
The [gdx_getting_started_2.html](./gdx_getting_started_2.html) example uses a Bluetooth Low Energy (BLE) connection and demonstrates how you can use the gdx functions to:
- Connect to a Go Direct device over BLE
- Use defaults to set the active sensors and collection rate
- Collect a few measurements from the enabled sensors
- Disconnect

## Example 3: User Prompts and Collecting Data
The [gdx_getting_started_3.html](./gdx_getting_started_3.html) example shows you how to use the gdx functions to:
- Connect to a Go Direct device over BLE
- Provide the user with a prompt to select the active sensors
- Provide the user with a prompt to set the measurement period
- Collect a few measurements from the enabled sensors
- Disconnect

## Example 4: Setting Defaults and Passing Arguments
The [gdx_getting_started_4.html](./gdx_getting_started_4.html) example shows you how to avoid using prompts (and instead pass arguments) to select the active sensors and set the measurement period:
- Connect to a Go Direct device over BLE
- Set the active sensors in your program
- Set the measurement period in your program
- Collect a few measurements from the enabled sensors
- Disconnect

## Example 5: Export Sensor Data as CSV
The [gdx_getting_started_5.py](./gdx_getting_started_5.html) example provides some ideas about what you can do with sensor data by using the the built-in csv Python module. It shows you how to:
- Connect to a Go Direct device over BLE
- Set the active sensors and collection rate
- Collect a few measurements from the enabled sensors
- Allow the user to output the data as a comma-separated-value file

## License

All of the content in this repository is available under the terms of the [BSD 3-Clause License](../LICENSE).

Vernier products are designed for educational use. Our products are not designed nor are they recommended for any industrial, medical, or commercial process such as life support, patient diagnosis, control of a manufacturing process, or industrial testing of any kind.