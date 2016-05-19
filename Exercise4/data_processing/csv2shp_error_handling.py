"""
csv2shp.py - Convert csv (with lat,lon coordinates to shapefile
Kris Johnson
16 May 2016
"""

import csv
from packages import shapefile


class CSV2SHP_OS():
    """
    convert csv to shapefile using pyshp library
    """

    def __init__(self):
        # create shapefile writer
        self.shp_writer = shapefile.Writer(shapefile.POINT)
        self.shp_writer.autoBalance = 1  # turn on validation

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
        for name in fields:
            self.shp_writer.field(name, 'C', 100)

    def convert(self, csv_file_path, shapefile_path):
        """
        converts csv data to shapefile
        :param csv_file_path: path to input csv
        :param shapefile_path: path to output shapefile
        :return: nothing
        """

        try:

            # read csv to list of dicts
            data_list = self.read_csv(csv_file_path)

            # add fields to shapefile
            self.add_fields(data_list)

            # write data to shapefile
            for row in data_list:
                # write geometry
                self.shp_writer.point(float(row['Long']), float(row['Lat']))
                # write attributes
                self.shp_writer.record(**row)

            # save shapefile
            # note: resulting shapefile will be unprojected
            #       see https://github.com/GeospatialPython/pyshp/wiki/Map-Projections
            #       for assistance in providing a projection for the data
            self.shp_writer.save(shapefile_path)
            print 'Done'

        except Exception as err:
            return err
