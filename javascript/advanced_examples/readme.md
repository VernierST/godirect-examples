# Getting Started with JavaScript

If you are new to JavaScript, you may want to visit our [Go Direct FAQ page](./godirect-js-faqs.md) for some tips and troubleshooting ideas.

The examples in this folder will walk you through some advanced examples of connecting to a Go Direct device using JavaScript. 

For more basic examples, take a look in the [/advanced_examples/](./advanced_examples) folder.

## Example 1: Making a Chart
The [gdx_making_a_chart.html](./gdx_making_a_chart.html) example shows how you can use the gdx functions to create a chart of sensor data using the chart.js library and:
- Connect to a Go Direct device over BLE
- Collect 10 data points
- Graph 10 data points 
- Disconnect

## Example 2: Start and Stopping Data Collection
The [gdx_start_stop_desmos.html](./gdx_start_stop_desmos.html) example uses a Bluetooth Low Energy (BLE) connection and demonstrates how you can use the gdx functions to:
- Connect to a Go Direct device over BLE
- Start Collection with a button
- Graph Data in a Desmos window
- Find the line of best fit for the data
- Stop Collection and Disconnect

## Example 3: User Prompts and Collecting Data
The [gdx_using_desmos.html](./gdx_using_desmos.html) example shows you how to use the library:
- Connect to a Go Direct device over BLE
- Collect 10 data points
- Graph the data in a Desmos Window
- Find the line of best fit for the data
- Disconnect

## Example 4: Connecting to Two Devices
The [gdx_using_two_devices.html](./gdx_using_two_devices.html) example shows you how to connect to two Go Direct Devices using the GDX and Chart.js library:
- Connect to a Go Direct device over BLE
- Connect to a second Go Direct Device
- Collect 10 data points from each device
- Graph each device's dataset in chart.js
- Disconnect

## License

All of the content in this repository is available under the terms of the [BSD 3-Clause License](../LICENSE).

Vernier products are designed for educational use. Our products are not designed nor are they recommended for any industrial, medical, or commercial process such as life support, patient diagnosis, control of a manufacturing process, or industrial testing of any kind.