"""
Kris's Little GIS App
Kris Johnson
16 May 2016
"""

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

# other imports
import csv

# local custom imports
from csv2shp import CSV2SHP
from graphing import Graphal

class App():

    '''
    This is a basic Tkinter app
    '''

    # class-level attributes

    master = Tk()  # Create Tk instance

    def __init__(self):

        # Assign additional class-level attributes

        self.converter = CSV2SHP()
        self.grapher = Graphal()
        self.configure()
        self.run()


    def configure(self):
        '''
        Configure app
        :return: nothing
        '''

        # set title
        self.master.title("Kris's Amazing App!")

        # Configure Grid
        self.master.columnconfigure(0, pad=5)
        self.master.columnconfigure(1, pad=5)

        # Add labels
        Label(self.master, text='Input Table').grid(row=0, column=0, sticky=W)
        Label(self.master, text='Output Shapefile').grid(row=2, column=0, sticky=W)

        # Add File Inputs

        # text entries
        self.input_table_entry = Entry(self.master, width=50)
        self.input_table_entry.grid(row=1, column=0)
        self.output_shapefile_entry = Entry(self.master, width=50)
        self.output_shapefile_entry.grid(row=3, column=0)

        # file browse buttons
        Button(self.master, text='BROWSE', command=self.open_file)\
            .grid(row=1, column=1, sticky=E)
        Button(self.master, text='BROWSE', command=self.save_file) \
            .grid(row=3, column=1, sticky=E)


        # Add field list box
        Label(self.master, text='Graph Attribute').grid(row=4, column=0, sticky=W)
        self.field_listbox = Listbox(self.master, selectmode=EXTENDED)
        self.field_listbox.grid(row=5, column=0)


        # Add run button
        Button(self.master, text='RUN', command=self.run_btn_click)\
            .grid(row=6, pady=20, sticky=E)


    def display_graphic(self, graphic):
        window = Toplevel(self.master)
        graphic_image = ImageTk.PhotoImage(graphic)
        Label(window, image=graphic_image).pack()

    def run_btn_click(self):
        '''
        Run button click handler
        :return: nothing
        '''
        print "Run!"
        # figure out what user wants based on what they've provided
        csv_path = self.input_table_entry.get()
        shapefile_path = self.output_shapefile_entry.get()
        field_sel_list = self.field_listbox.get(ACTIVE)

        # check for csv
        if csv_path:
            print 'csv path:', csv_path

        # check for shapefile
        if shapefile_path:
            print 'shapefile path:', shapefile_path, 'exporting to shapefile...',
            self.converter.convert(csv_path, shapefile_path)

        # check for graphing
        if len(field_sel_list) > 0:
            self.grapher.graphit(field_sel_list, csv_path)




    def open_file(self):
        '''
        Open tk file dialog window
        ref: http://tkinter.unpythonic.net/wiki/tkFileDialog
        :return: filepath (string)
        '''

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
            self.input_table_entry.insert(0, file_path.name)
            self.populate_fieldbox(file_path.name)


    def save_file(self):
        '''
        open tk save file dialog window
        ref: http://tkinter.unpythonic.net/wiki/tkFileDialog
        :return:
        '''

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
            self.output_shapefile_entry.insert(0, file_path.name)

    def populate_fieldbox(self, input_path):
        """
        populate list box with fields from csv file
        :param input_path:
        :return: nothing
        """
        headers = self.get_csv_headers(input_path)
        for fld in headers:
            self.field_listbox.insert(END, fld)



    def get_csv_headers(self, input_path):
        """
        import csv data
        :param input_path:
        :return: capture data and headers
        """
        with open(input_path, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            return reader.next()



    def run(self):
        '''
        Run the main loop
        :return: nothing
        '''


        self.master.mainloop()




def main():

    myApp = App()


if __name__ == '__main__':
    main()