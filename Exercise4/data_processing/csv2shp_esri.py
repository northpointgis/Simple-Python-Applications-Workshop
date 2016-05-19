import arcpy
import os


class CSV2SHP_ESRI():

    def __init__(self):
        pass

    def convert(self, csv_path, output_path):
        arcpy.env.workspace = 'in_memory'

        if arcpy.Exists('tempXY'):
           arcpy.Delete_management('tempXY')

        arcpy.MakeXYEventLayer_management(csv_path,'Long','Lat','tempXY')

        if os.path.isfile(output_path):
           os.remove(output_path)

        arcpy.CopyFeatures_management('tempXY', output_path)
