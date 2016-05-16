from Tkinter import *
import tkFileDialog
from ProcessData import DataProcessor


class App():

    '''
    This is a basic Tkinter app
    '''

    # class-level attributesrr

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
##        self.master.geometry('500x500')

    def config_widgets(self):

        # Insert widgets

        input_label = Label(self.master)
        input_label['text'] = 'Input File'
        # input_label.grid(row=0, column=0)
        input_label.grid['row'] = 0
        input_label.grid.column = 0

        self.input_entry_box = input_entry_box = Entry(self.master)
        input_entry_box['width'] = 50
        input_entry_box.grid(row=0,column=1)

        input_button = Button(self.master)
        input_button['text'] = 'BROWSE'
        input_button['command'] = self.open_file
        input_button.grid(row=0, column=2)

        output_label = Label(self.master)
        output_label['text'] = 'Output File'
        output_label.grid(row=1, column=0)

        self.output_entry_box = output_entry_box = Entry(self.master)
        output_entry_box['width'] = 50
        output_entry_box.grid(row=1,column=1)

        output_button = Button(self.master)
        output_button['text'] = 'BROWSE'
        output_button['command'] = self.save_file
        output_button.grid(row=1, column=2)

        exec_button = Button(self.master)
        exec_button['text'] = 'EXECUTE'
        exec_button['command'] = self.gis_process
        exec_button.grid(row=2,column=1)

    def run_app(self):

        # Run the mainloop
        self.master.mainloop()

    def open_file(self):

        # Define file dialog options
        options = {}
        options['defaultextension'] = '.csv'
        options['filetypes'] = [('comma seperated value', '.csv')]
        options['title'] = 'Input csv file:'

        # Open file dialog
        file_path = tkFileDialog.askopenfile(**options)

        # Check to make sure a file was specified
        if file_path:

            # Insert file path into entry box
            self.input_entry_box.insert(0, file_path.name)


    def save_file(self):

        # Define file dialog options
        options = {}
        options['defaultextension'] = '.shp'
        options['filetypes'] = [('shapefile', '.shp')]
        options['title'] = 'Save output as:'

        # Open file dialog
        file_path = tkFileDialog.asksaveasfile(**options)

        # Check to make sure a file was specified
        if file_path:

            # Insert file path into entry box
            self.output_entry_box.insert(0, file_path.name)

    def gis_process(self):

        # Retrieve input parameters
        input_file_path = self.input_entry_box.get()
        output_file_path = self.output_entry_box.get()

        # Process data
        data_processor = DataProcessor(input_file_path, output_file_path)
        data_processor.locate_wrecks()

newApp = App()
