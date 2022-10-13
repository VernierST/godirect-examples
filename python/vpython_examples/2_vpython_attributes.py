"""
Add attributes to the VPython sphere objects using the available parameters
"""

from vpython import *


sphere(color=color.red, 
       opacity=1,    # floating value from 0 - 1
       shininess=0.2,    # floating value from 0 - 1
       emissive=False,
       pos=vector(0,0,0),
       size=vector(2,2,2),
       texture=textures.granite,
       axis=vector(1, 0, 0),
       up=vector(0, 1, 0))


