from time import perf_counter
from vpython import *

# Choose one of these vernier6 files to test
#from vernier6 import ver
#from vernier6_Sam_modifications import ver

from gdx_modules import gdx
gdx = gdx.gdx()

scene.width = 400
scene.height = 50
scene.range = 1

# A box graphic to visualize the sensor measurement
b = box(size=0.5*vec(1,1,1), color=color.red)

# A graph to keep track of the lag 
g2 = graph(xtitle='Time', ytitle='Lag (s)', scroll=True,
      width=400, height=250, xmin=0, xmax=20, ymin=0, ymax=6, fast=False)
g = gcurve(color=color.red)

# A graph to see the amount of lag that occurs for each measurement
g1 = graph(title='hello', xtitle='Time', ytitle='Lag per Reading (s)', scroll=True,
      width=400, height=250, xmin=0, xmax=20, ymin=-0.2, ymax=0.2, fast=False)
j = gcurve(color=color.green)

# Set the rate for data collection
dt_period = 50

#ver.setup(connection='USB', channels=[1], period=dt_period)
gdx.open(connection='ble', device_to_open='GDX-FOR 071000U9', vpython=True)
gdx.select_sensors([1])
#start occurs when start button is pressed, so not sure if this will work???
# because start is called here and then again when the button is pressed.
gdx.start(period=dt_period)

dt = dt_period/1000   #this gives period in seconds
sample_time = int(1/dt)

t = None
dt_time = 0
lasttime = perf_counter()
i = 0

while gdx.close_vp() == False:
    # rate(50)
    # if gdx.start_vp() == True:
    #     gdx.read_ch()
    print("running")



while True:
    rate(50)
    
    
    if ver.ready():
        ready_time = perf_counter()-lasttime
        lasttime = perf_counter()
        x = ver.read(1)
        if x is not None:
            #print("measurement = ", '%.1f'%x)
            b.pos.x = x/4
            if t == None:
                t = clock()
                ready_time =  dt   # on the first iteration don't count how long it took
                extra_time = 0
            time = clock()-t

            # when there is no lag, the clock 'time' should be the same
            # as the sensor's 'dt_time'.
            g.plot(time, time - dt_time) #the total lag
            j.plot(time, extra_time) # lag per reading

        dt_time = dt_time + dt
        # running total of how much more time it took the program
        # to loop than the sampling period. For a properly running
        # program this should hover around 0.
        extra_time = ready_time - dt
        samples = int(time/dt + 1)
        g2.title = 'collecting at ' +str(sample_time) +' samples/sec'
        g1.title = 'collected ' +str(i) +' of ' +str(samples) +' samples'
        i += 1
