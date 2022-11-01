"""
Create a VPython sphere. Add attributes using the available parameters.

- Zoom in or out of the 3D object using two fingers
on a touchpad or the scroll wheel on a mouse. 
- To rotate the object, hold
down the right button (or CTRL + left button) and move the cursor.

"""

from vpython import *


my_sphere = sphere(
            color=color.red, 
            opacity=1,    # floating value from 0 - 1
            shininess=0.2,    # floating value from 0 - 1
            emissive=False,
            pos=vector(0,0,0),
            size=vector(2,2,2),
            texture=textures.granite,
            axis=vector(1, 0, 0),
            up=vector(0, 1, 0))