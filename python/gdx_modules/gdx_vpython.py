import logging

from matplotlib.pyplot import gray
  



# from gdx_modules.gdx import gdx_class
# gdx = gdx_class()
#import gdx_modules.gdx


#Are these variable required outside the class? 
# woutput = wtext(text='')
# startbutton = None
# closebutton = None

class ver_vpython:


    closed = False
    start_button_state = False
    #period = 100

    def __init__(self):  
        """
        """

    def setup_canvas(self):

        # Can we install the vpython library with godirect?
        #from vpython import canvas, button, box, wtext, checkbox, rate
        from vpython import canvas, box, button

        # if they are using vpython, then create the canvas and start/stop/close buttons
        global startbutton, closebutton
        canvas(width=2, height=2)
        box()
        #startbutton = button(text='<b>COLLECT</b>', bind=vp_start_stop)  
        #<h1 style="color: #2ecc71">freeCodeCamp</h1>
        #startbutton = button(text='<h1 style="color: #2ecc71">COLLECT</h1>', bind=vp_start_stop)  
        startbutton = button(text='<b style="color:green; font-size:26px"> COLLECT </b>', bind=vp_start_stop)
        canvas.get_selected().append_to_caption('  ')
        closebutton = button(text='<b style="color:red; font-size:26px">   CLOSE   </b>', bind=vp_closed)


    def print_to_canvas(self):
        """ Feedback to the user on the vpython screen 
		"""  
        from vpython import canvas

        canvas.get_selected().append_to_caption('Must specify device channels.')
        canvas.get_selected().caption = 'test caption'
        raise AttributeError('Must specify device channels.')     

    def start_button(self):
        """ Return value = True if the button is in the Start state. Return
        value = False if it is in the Stop state.
        """
        from vpython import rate, color

        if ver_vpython.start_button_state:
            return True
            
        else:
            # assumption is that rate() is only needed when data collection is not occurring
            # When it is, the computer will automatically be slowed because of the time
            # required to talk to the hardware.
            rate(50)
            return False

    def closed_button(self):
        if ver_vpython.closed:
            return True
        else:
            return False

    
def vp_start_stop(f):
    """ This function gets called only when the button has been pressed. Return
    value = True if the button is in the Start state.
    """
    
    if f.text == '<b style="color:green; font-size:26px"> COLLECT </b>':
        f.text = '<b style="color:black; font-size:26px">    STOP     </b>'
        #
        # "Change the class variable’s value using the class name only."
        ver_vpython.start_button_state = True

    else:
        f.text = '<b style="color:green; font-size:26px"> COLLECT </b>'
        ver_vpython.start_button_state = False

def vp_closed():
    from vpython import rate

    ver_vpython.closed = True
    ver_vpython.start_button_state = False
    # gdx = gdx_modules.gdx.gdx()
    # #x = ver.readall() # clear things out
    # ver.start_button_state = False
    #gdxvp.stop()
    n = 0
    while True: # shut down gracefully
        rate(100)
        n += 1
        if n > 100: break
    #gdxvp.close()
    startbutton.delete()
    closebutton.delete()
    


   