"""
Kris's Little GIS App
16 May 2016
"""

from Tkinter import *

class App():

    '''
    This is a basic Tkinter app
    '''

    # class-level attributes

    master = Tk()  # Create Tk instance

    def __init__(self):

        # Assign additional class-level attributes

        self.configure()
        self.run()


    def configure(self):

        # Insert widgets

        pass


    def run(self):

        # Run the mainloop

        self.master.mainloop()




def main():

    myApp = App()


if __name__ == '__main__':
    main()