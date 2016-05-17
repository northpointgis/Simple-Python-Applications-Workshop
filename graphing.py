"""
Python Charting with Pygal
Kris Johnson
17 May 2016
"""

import csv
from collections import Counter
from packages import pygal

class Graphal():
    """
    Basic python graphing with Pygal
    Using data from a csv
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

    def summarize_data(self, summary_field, data):
        """
        summarize data by field and return dict
        :type data: object
        :param data:
        :return: dict of summarized values
        """

        out_list = []
        for row in data:
            for k,v in row.iteritems():
                if k == summary_field:
                    out_list.append(v)

        return out_list

    def graphit(self, summary_field, input_file, output_file):
        """
        create a graph from a csv file
        :param output_file: (string) path to output graphic
        :param input_file: (string) path to input csv file
        :param summary_field: (string) name of field from csv to show on graph
        :return: nothing
        """

        data_list = self.read_csv(input_file)

        summarized_data = self.summarize_data(summary_field, data_list)