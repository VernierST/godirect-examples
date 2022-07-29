import logging
from turtle import pos
  
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
    plot_2 = None
    plot_3 = None
    graph_canvas = None
    meter_canvas = None
    meter_text = None
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

        # this also seems to work for deleting the button object
        #canvas.delete(ver_vpython.cb)
        ver_vpython.cb.delete()
        ver_vpython.clsb.delete()
        scene.delete()
        current = canvas.get_selected()
        if current:
            current.delete()

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
        plot_2 = gcurve(color=color.blue)
        ver_vpython.plot_2 = plot_2
        ver_vpython.plot_2.plot(0,0)
        plot_3 = gcurve(color=color.black)
        ver_vpython.plot_3 = plot_3
        ver_vpython.plot_3.plot(0,0)

    def graph_plot(self, data):
        print('time = ', ver_vpython.time)
        if data == None:
            return
        else:
            len_data = len(data)
            if len_data == 1:
                ver_vpython.plot_1.plot(ver_vpython.time, data[0])
            elif len_data == 2:
                ver_vpython.plot_1.plot(ver_vpython.time, data[0])
                ver_vpython.plot_2.plot(ver_vpython.time, data[1])
            else:
                ver_vpython.plot_1.plot(ver_vpython.time, data[0])
                ver_vpython.plot_2.plot(ver_vpython.time, data[1])
                ver_vpython.plot_3.plot(ver_vpython.time, data[2])

        ver_vpython.time = ver_vpython.time + ver_vpython.period
        

    def graph_clear(self, column_headers):
        if column_headers == None:
            column_headers = 'Data'
        ver_vpython.plot_1.delete()
        ver_vpython.plot_2.delete()
        ver_vpython.plot_3.delete()
        ver_vpython.graph_canvas.ytitle = column_headers
        ver_vpython.graph_canvas.xmin = 0
        ver_vpython.graph_canvas.xmax = 5
        
    def graph_delete(self):
        ver_vpython.graph_canvas.delete()

    def meter_init(self):
        from vpython import canvas, wtext, scene
        
        mc = canvas(width=0, height=20)
        ver_vpython.meter_canvas = mc
        scene.append_to_title('\n')
        woutput = wtext(text='', pos=mc.title_anchor)
        ver_vpython.meter_text = woutput
        #<b>mass <i>M</i></b>
        #woutput.text = "<b>{ch_string}</b>\n".format(ch_string)
        
        woutput.text = f""
        

    def meter_data(self, column_headers, data):
        if data == None:
            meter_string = 'No data'
        else:
            meter_string = ' '
            i = 0
            for (ch, d) in zip(column_headers, data):
                round_data = str(round(d, 2))
                meter_string = meter_string + ch + ": " + round_data + '    '
        
        ver_vpython.meter_text.text = f"{meter_string}"

    def meter_delete(self):
        from vpython import canvas
        
        canvas.delete(ver_vpython.meter_text)
        mc = ver_vpython.meter_canvas
        # this worked
        mc.delete()
        # this worked too
        #canvas.delete(mc)
    
        
        


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
  
    


   