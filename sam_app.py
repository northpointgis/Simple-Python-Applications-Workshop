from Tkinter import *
import tkFileDialog
from ProcessData import DataProcessor


class App():

    '''
    This is a basic Tkinter app
    '''

    # class-level attributes

    master = Tk() # Create Tk instance

    def __init__(self):

        # Assign additional class-level attributes

        # Execute core methods
        self.config_app()
        self.config_widgets()
        self.run_app()

    def config_app(self):

        # Configure app
        self.master.title('SAMPLE')

    def config_widgets(self):

        # Insert widgets

        label_one = Label(self.master, text="Input File")
        label_one.grid(row=0, column=0)

        self.entry_box_one = Entry(self.master, width=50)
        self.entry_box_one.grid(row=0,column=1)

        button_one = Button(self.master, text='BROWSE', command=self.open_file)
        button_one.grid(row=0, column=2)

        label_two = Label(self.master, text="Output File")
        label_two.grid(row=1, column=0)

        self.entry_box_two = Entry(self.master, width=50)
        self.entry_box_two.grid(row=1,column=1)

        button_two = Button(self.master, text='BROWSE', command=self.save_file)
        button_two.grid(row=1, column=2)

        execute_button = Button(self.master, text='EXECUTE', command=self.gis_process)
        execute_button.grid(row=2,column=1)

    def run_app(self):

        # Run the mainloop
        self.master.mainloop()

    def open_file(self):

        # Open file dialog
        file_path = tkFileDialog.askopenfile()

        # Check to make sure a file was specified
        if file_path:

            # Insert file path into entry box
            self.entry_box_one.insert(0, file_path.name)


    def save_file(self):

        # Open file dialog
        file_path = tkFileDialog.asksaveasfile()

        # Check to make sure a file was specified
        if file_path:

            # Insert file path into entry box
            self.entry_box_two.insert(0, file_path.name)

    def gis_process(self):

        # Retrieve input parameters
        input_file_path = self.entry_box_one.get()
        output_file_path = self.entry_box_two.get()

        data_processor = DataProcessor(input_file_path, output_file_path)
        data_processor.locate_wrecks()

newApp = App()
