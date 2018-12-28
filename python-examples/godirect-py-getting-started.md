# Getting started with Go Direct® and Python

If you are new to Python, you may want to visit our [Go Direct FAQ page](./godirect-py-faqs.md) for some tips and troubleshooting ideas.

## Install Python 3

The godirect-examples and the godirect module are written for Python 3. Install the latest version of Python 3.x from the [Python Software Foundation site](https://www.python.org/downloads/). All examples in this repository and its documentation assume that you only have Python 3 installed.

## Install the godirect Module

After Python 3 is installed, you will be able to `pip` to install the `godirect` module that will enable these example scripts to talk to Vernier Go Direct devices. 

```
pip install godirect[usb,ble]
```
There are some helpful hints about installing the godirect module on the [Go Direct FAQ page](./godirect-py-faqs.md), and more detailed instructions on installing the `godirect` module at the [Python Packaging Index site](https://pypi.org/project/godirect/) or in the [godirect-py repository](https://github.com/VernierST/godirect-py).

## Get godirect-examples

Clone the entire [godirect-examples repository](../godirect-examples) or download one or more of the [godirect Python example files](./).

## Run an example

- If you are using USB, connect your Go Direct device to your computer with your USB cable
- If you are using Bluetooth Low Energy, connect your BlueGiga BLE dongle to your computer and turn on your Go Direct device
- Run the following command

```
python gdx_getting_started_1.py
```
