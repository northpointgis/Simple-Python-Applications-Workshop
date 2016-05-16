"""
csv2shp.py - Convert csv (with lat,lon coordinates to shapefile
Kris Johnson
16 May 2016
"""

import csv
import shapefile

class CSV2SHP():
    """
    convert csv to shapefile using pyshp library
    """

    def __init__(self):
        pass



    def read_csv(self, file_path):
        """
        reads csv data
        :param file_path: path to csv
        :return: returns csv data
        """

        return [row for row in csv.DictReader(open(file_path))]


    def add_fields(self, data):
        """
        adds fields to shapefile based on data
        :param data: list of dicts
        :return: nothing
        """

        fields = data[0].keys()
        for fld in data[0]():
            if isinstance()


    def convert(self, csv_file_path):
        """
        converts csv data to shapefile
        :param csv_file_path: path to csv
        :return:
        """

        # read csv to list of dicts
        data_list = self.read_csv(csv_file_path)

        # create shapefile writer
        self.shp_writer = shapefile.Writer(shapefile.POINT)

        # add fields to shapefile
        self.add_fields(data_list)





