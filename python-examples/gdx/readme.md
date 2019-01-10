# The gdx Module

The `gdx` module in this folder is used to abstract and simplify interaction with Go Direct® devices. While the implementation of the communication is actually done through the lower level [godirect module](https://pypi.org/project/godirect/), the `gdx` module exposes the features that are most commonly used when writing code that deals with Go Direct devices.

## The gdx module API

### open_usb:
Discovers the Go Direct device with a USB connection and opens that device for data collection. If there are multiple devices discovered, a list of devices is printed to the terminal with a prompt for the user to choose one.

Arguments: None

### open_ble:
Open a Go Direct device via bluetooth for data collection.

Arguments: 
- `device_to_open`: Set to None to receive a list of all discovered Go Direct devices for the user to choose one. Set to a specific Go Direct device name, for example "GDX-FOR 071000U9", to open that device. Set to "proximity_pairing" to open the device with the highest rssi (closest proximity).

### select_sensors:
Select the sensors (by number) to enable for data collection. Note that the sensors are not enabled in this function, that happens in the start() function.

Arguments:
- `sensors` []: if sensors is left blank, a list of all available sensors is provided by a prompt in the terminal for the user to select from. Otherwise, enter a list of sensor numbers such as [1,2,3].

### start:
Enables the sensors that were selected in the select_sensors() function and then starts data collection.

Arguments: 
- `period` (int): If period is left blank, a prompt in the terminal allows the user to enter the period. Otherwise, enter a period in milliseconds, e.g. 1000

### read:

### stop:

### close:

### device_info:

### enabled_sensor_info:

### sensor_info:

### discover_ble_devices:

### monitor_rssi:

## License

All of the content in this repository is available under the terms of the [BSD 3-Clause License](../../LICENSE).

Vernier products are designed for educational use. Our products are not designed nor are they recommended for any industrial, medical, or commercial process such as life support, patient diagnosis, control of a manufacturing process, or industrial testing of any kind.