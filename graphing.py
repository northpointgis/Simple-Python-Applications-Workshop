"""
Python Charting with Pygal
Kris Johnson
17 May 2016
"""

import csv
import inspect
import os
import sys

# realpath() will make your script run, even if you symlink it :)
# cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
# if cmd_folder not in sys.path:
#     sys.path.insert(0, cmd_folder)

from packages import pygal


class Graphal():
    """
    Basic python graphing with Pygal
    Using data from a csv
    """

    def __init__(self):
       self.bar_chart = pygal.Bar()

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

        # isolate values from selected field
        out_list = []
        for row in data:
            for k,v in row.iteritems():
                if k == summary_field:
                    out_list.append(v)

        # get counts into dictionary
        count_dict = {}
        for i in out_list:
            count_dict[i] = count_dict.get(i,0) + 1

        # return count dictionary
        return count_dict

    def add_data_to_chart(self, data):
        """
        add data to bar chart
        :param data:
        :return:
        """
        for key,value in data.iteritems():
            self.bar_chart.add(key, value)

    def graphit(self, summary_field, input_file):
        """
        create a graph from a csv file
        :param output_file: (string) path to output graphic
        :param input_file: (string) path to input csv file
        :param summary_field: (string) name of field from csv to show on graph
        :return: nothing
        """

        data_list = self.read_csv(input_file)

        summarized_data = self.summarize_data(summary_field, data_list)

        self.add_data_to_chart(summarized_data)

        self.bar_chart.render_in_browser()
