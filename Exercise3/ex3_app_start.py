'''App 3 Start'''

from Tkinter import *

class App():

    '''
    This is a basic Tkinter app
    '''

    # class-level attributes

    master = Tk() # Create Tk instance

    def __init__(self):

        # Assign additional class-level attributes

        # Execute core methods
        self.config_widgets()
        self.run_app()

    def config_widgets(self):

        # Insert widgets
        new_entry_box = Entry(self.master)
        new_entry_box['width'] = 50
        new_entry_box.grid(row=0, column=0)

        new_button = Button(self.master)
        new_button['text'] = 'Click Me!'
        new_button.grid(row=0, column=1)

    def run_app(self):

        # Run the mainloop
        self.master.mainloop()

if __name__ == '__main__':
    new_window = App()
