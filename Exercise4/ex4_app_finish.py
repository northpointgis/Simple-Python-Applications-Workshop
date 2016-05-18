'''App 4 Finished'''

# use this if you want to include modules from a subfolder
# http://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
import os, sys, inspect
cmd_subfolder = os.path.realpath(
    os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "packages")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

# Tkinter imports
from Tkinter import *
import tkFileDialog

# import custom modules
from data_processing.csv2shp import CSV2SHP
from data_processing.graphing import Graphal
from data_processing.ProcessData import DataProcessor


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
        input_label.grid(row=0, column=0)

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
        exec_button['command'] = self.execute_tool
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

    def execute_tool(self):

        # Retrieve input parameters
        input_file_path = self.input_entry_box.get()
        output_file_path = self.output_entry_box.get()

        # Process data
        data_processor = DataProcessor(input_file_path, output_file_path)
        data_processor.create_shapefile()

    # def run_btn_click(self):
    #     '''
    #     Run button click handler
    #     :return: nothing
    #     '''
    #     print "Run!"
    #     # figure out what user wants based on what they've provided
    #     csv_path = self.input_table_entry.get()
    #     shapefile_path = self.output_shapefile_entry.get()
    #     field_sel_list = self.field_listbox.get(ACTIVE)
    #
    #     # check for csv
    #     if csv_path:
    #         print 'csv path:', csv_path
    #
    #     # check for shapefile
    #     if shapefile_path:
    #         print 'shapefile path:', shapefile_path, 'exporting to shapefile...',
    #         self.converter.convert(csv_path, shapefile_path)
    #
    #     # check for graphing
    #     if len(field_sel_list) > 0:
    #         self.grapher.graphit(field_sel_list, csv_path)

newApp = App()
