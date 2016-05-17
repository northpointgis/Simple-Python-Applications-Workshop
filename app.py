"""
Kris's Little GIS App
Kris Johnson
16 May 2016
"""

from Tkinter import *
import tkFileDialog
from csv2shp import CSV2SHP

class App():

    '''
    This is a basic Tkinter app
    '''

    # class-level attributes

    master = Tk()  # Create Tk instance

    def __init__(self):

        # Assign additional class-level attributes

        self.converter = CSV2SHP()
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


        # Add run button
        Button(self.master, text='RUN', command=self.run_btn_click)\
            .grid(row=4, pady=20, sticky=E)


    def run_btn_click(self):
        '''
        Run button click handler
        :return: nothing
        '''
        print "Run!"
        csv_path = self.input_table_entry.get()
        shapefile_path = self.output_shapefile_entry.get()
        self.converter.convert(csv_path, shapefile_path)


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