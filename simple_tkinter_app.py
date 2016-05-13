from Tkinter import *

class App():

    '''
    This is a basic Tkinter app
    '''

    # class-level attributes

    master = Tk() # Create Tk instance

    def __init__(self):

        # Assign additional class-level attributes

        self.config_widgets()
        self.run_app()


    def config_widgets(self):

        # Insert widgets

        pass


    def run_app(self):

        # Run the mainloop

        self.master.mainloop()


newApp = App()
