import arcpy
import csv
import os


class DataProcessor():

    def __init__(self, csv_path, output_path):

        # Set class-level attributes

        self.csv_path = csv_path
        self.output_path = output_path


    def read_csv(self):
        with open(self.csv_path) as csv_file:
         reader = csv.DictReader(csv_file)

         for row in reader:
             print row

    def create_shapefile(self):
        arcpy.env.workspace = 'in_memory'

        if arcpy.Exists('tempXY'):
           arcpy.Delete_management('tempXY')

        arcpy.MakeXYEventLayer_management(self.csv_path,'Long','Lat','tempXY')

        if os.path.isfile(self.output_path):
           os.remove(self.output_path)

        arcpy.CopyFeatures_management('tempXY', self.output_path)
