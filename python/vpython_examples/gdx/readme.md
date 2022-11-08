# The gdx Module

The `gdx` module is used to simplify interaction with Go Direct® devices. While the implementation of the communication is actually done through the lower level [godirect module](https://pypi.org/project/godirect/), the `gdx` module exposes the features that are most commonly used when writing code that deals with Go Direct devices. In other words, the `gdx` module provides a small set of simple functions to write Python and VPython code. Of course you can always modify the `gdx` module as needed for your own custom Go Direct sensor functions.

When writing Python code using the `gdx` module you must first import it.

```python
from gdx import gdx
gdx = gdx.gdx()
```

An important factor for this import is that Python must be able to find the `gdx` module in order to import it. Here are three ways to help insure that Python finds the `gdx` module:

- Locate the /gdx/ folder in the same directory as the example that you are running.
- Manually move the /gdx/ folder into your Python /site-packages/ directory. This is the same directory that all Python libraries are placed, and it is a "path" that Python looks for modules.
- Add code to provide a system 'path' to the /gdx/ folder. A common example is having /gdx/ one directory up. Here is the code used to add a system 'path' one directory up:

```python
import os
import sys

file_path = os.path.abspath(os.path.dirname(sys.argv[0]))
os.chdir(file_path)
os.chdir("..")
gdx_module_path = os.getcwd()
if gdx_module_path not in sys.path:
    sys.path.append(gdx_module_path)
```

For information on using the gdx module for data collection refer to [Getting Started with Vernier Go Direct® Sensors and Python](https://github.com/VernierST/godirect-examples/tree/main/python) manual.

For information on using the gdx module for VPython refer to the [Getting Started with Vernier Go Direct® Sensors and VPython](https://github.com/VernierST/godirect-examples/tree/main/python/vpython_examples) manual.

All of the examples in the godirect-examples repository use the `gdx` module, except for the example located in the ../example_without_gdx/ folder. Run this example if you want to communicate directly to your Go Direct device with the `godirect` module, or you want to do some troubleshooting.

## License

All of the content in this repository is available under the terms of the [BSD 3-Clause License](../../LICENSE).

Vernier products are designed for educational use. Our products are not designed nor are they recommended for any industrial, medical, or commercial process such as life support, patient diagnosis, control of a manufacturing process, or industrial testing of any kind.