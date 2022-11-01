"""
Modify the color attribute in order to cycle through various colors using 
the R, the G, or the B values.

In the RGB scheme, white is the color with a maximum of red, blue, and 
green (1, 1, 1). Black has minimum amounts (0, 0, 0).
"""

from vpython import *


my_sphere = sphere()

my_sphere.color = vector(0, 0, 0)
sleep(1)
my_sphere.color = vector(1, 0, 0)
sleep(1)
my_sphere.color = vector(1, 1, 0)
sleep(1)
my_sphere.color = vector(0, 1, 0)
sleep(1)
my_sphere.color = vector(0, 1, 1)  
sleep(1)
my_sphere.color = vector(0, 0, 1) 
sleep(1)
my_sphere.color = vector(1, 0, 1) 
sleep(1)
my_sphere.color = vector(1, 1, 1)
