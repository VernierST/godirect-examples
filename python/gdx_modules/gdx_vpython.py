import logging
  
# from gdx_modules.gdx import gdx_class
# gdx = gdx_class()
#import gdx_modules.gdx


#Are these variable required outside the class? 
# woutput = wtext(text='')
# collectbutton = None
# closebutton = None

class ver_vpython:


    closed = False
    collect_button_state = False
    period = 0.01
    time = 0
    plot_1 = None    # vpython gcurve for the graph canvas
    graph_canvas = None
    cb = None    # collect button
    clsb = None    # close button

    def __init__(self):  
        """
        """

    def setup_canvas(self):

        # Can we install the vpython library, with godirect?
        #from vpython import canvas, button, box, wtext, checkbox, rate
        from vpython import button, scene
        #global collectbutton, closebutton
        # if they are using vpython, then create the canvas and collect/stop/close buttons
        
        #global collectbutton, closebutton
        
        scene.width = 0
        scene.height = 10

        scene.append_to_title('\n')
        collectbutton = button(text='<b style="color:green; font-size:26px"> COLLECT </b>', 
                            pos=scene.title_anchor, bind=vp_collect_stop)
        ver_vpython.cb = collectbutton
        scene.append_to_title('  ')
        closebutton = button(text='<b style="color:red; font-size:26px">   CLOSE   </b>', 
                            pos=scene.title_anchor, bind=vp_closed)
        ver_vpython.clsb = closebutton
        scene.append_to_title('\n')

    def canvas_delete(self):
        from vpython import canvas, scene

        ver_vpython.cb.delete()
        ver_vpython.clsb.delete()
        scene.delete()
        current = canvas.get_selected()
        if current:
            current.delete()

        
    def graph(self, state='init', data=[]):
        from vpython import graph, gcurve, color

        if state == 'init': 
            gd = graph(xtitle='Time', ytitle='Data', scroll=True,
                width=400, xmin=0, xmax=5, fast=False)
            ver_vpython.graph_canvas = gd
            plot_1 = gcurve(color=color.red)
            ver_vpython.plot_1 = plot_1
            ver_vpython.plot_1.plot(0,0)

        elif state == 'plot':
            ver_vpython.plot_1.plot(ver_vpython.time, data)
            ver_vpython.time = ver_vpython.time + ver_vpython.period
            print('vp time = ', ver_vpython.time)

        elif state == 'clear':
            ver_vpython.plot_1.delete()

        else:
            ver_vpython.graph_canvas.delete()

    def graph_init(self, column_headers):
        from vpython import graph, gcurve, color
        if column_headers == None:
            column_headers = 'Data'
        gd = graph(xtitle='Time', ytitle=column_headers, scroll=True,
        width=400, xmin=0, xmax=5, fast=False)
        ver_vpython.graph_canvas = gd
        plot_1 = gcurve(color=color.red)
        ver_vpython.plot_1 = plot_1
        ver_vpython.plot_1.plot(0,0)

    def graph_plot(self, data=[]):
        print('time = ', ver_vpython.time)
        ver_vpython.plot_1.plot(ver_vpython.time, data)
        ver_vpython.time = ver_vpython.time + ver_vpython.period
        

    def graph_clear(self, column_headers):
        if column_headers == None:
            column_headers = 'Data'
        ver_vpython.graph_canvas.ytitle = column_headers
        ver_vpython.plot_1.delete()
    def graph_delete(self):
        ver_vpython.graph_canvas.delete()


    def print_to_canvas(self):
        """ Feedback to the user on the vpython screen 
		"""  
        from vpython import canvas

        canvas.get_selected().append_to_caption('Must specify device channels.')
        canvas.get_selected().caption = 'test caption'
        raise AttributeError('Must specify device channels.')     

    def collect_button(self):
        """ Return value = True if the button is in the Collect state. Return
        value = False if it is in the Stop state.
        """
        from vpython import rate, color

        if ver_vpython.collect_button_state:
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

    
def vp_collect_stop(f):
    """ This function gets called only when the button has been pressed. Return
    value = True if the button is in the Collect state.
    """
    
    if f.text == '<b style="color:green; font-size:26px"> COLLECT </b>':
        f.text = '<b style="color:black; font-size:26px">    STOP     </b>'
        #
        # "Change the class variable’s value using the class name only."
        ver_vpython.collect_button_state = True

    else:
        f.text = '<b style="color:green; font-size:26px"> COLLECT </b>'
        ver_vpython.collect_button_state = False

def vp_closed():
    from vpython import rate, canvas

    ver_vpython.closed = True
    ver_vpython.collect_button_state = False
    # gdx = gdx_modules.gdx.gdx()
    # #x = ver.readall() # clear things out
    # ver.collect_button_state = False
    #gdxvp.stop()
    # n = 0
    # while True: # shut down gracefully
    #     rate(100)
    #     n += 1
    #     if n > 100: break
    #gdxvp.close()
    # current = canvas.get_selected()
    # if current:
    #     current.delete()
    
    #collectbutton.delete()
    #closebutton.delete()
    


   