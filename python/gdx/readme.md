# The gdx Module

The `gdx` module in this folder is used to abstract and simplify interaction with Go Direct® devices. While the implementation of the communication is actually done through the lower level [godirect module](https://pypi.org/project/godirect/), the `gdx` module exposes the features that are most commonly used when writing code that deals with Go Direct devices.

The godirect-examples for python use the `gdx` module. Therefore, the `gdx` module must be placed in a directory that can be found when running the examples. Placing the gdx folder in the same directory as the examples usually insures that the python script will find the `gdx` module.

Modify the `gdx` module as needed for your own custom Go Direct sensor examples.

## License

All of the content in this repository is available under the terms of the [BSD 3-Clause License](../../LICENSE).

Vernier products are designed for educational use. Our products are not designed nor are they recommended for any industrial, medical, or commercial process such as life support, patient diagnosis, control of a manufacturing process, or industrial testing of any kind.