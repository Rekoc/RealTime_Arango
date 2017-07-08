# python 3.5.X
# Pipeline creation and management

import multiprocessing
import re
from packages.fileanalytics import FileAnalytics
from packages.terminal import Terminal
from packages.arangomanagement import DataManagement


class Pipeline(multiprocessing.Process):

    flag = False
    path_file = ""
    file_analyse = FileAnalytics(path=path_file)
    list_data = []
    database = DataManagement()

    def __init__(self, database, path_file='NULL'):
        print('(Pipeline)(__init__) Object created')
        multiprocessing.Process.__init__(self)
        self.path_file = path_file
        self.database = database

    def run(self):
        self.import_from_file()

    def import_from_file(self):
        konsole = Terminal(False)
        list_database = konsole.header_creation_automatic('database_4',
                                                          'Blablabla!!!')
        list_column = konsole.column_creation_automatic(['c1', 'c2', 'c3', 'c4',
                                                         'c5', 'c6', 'c7', 'c8', 'q'])
        with open(self.path_file, 'r') as file:
            line = 'empty'
            regex = re.compile(r'[\n\r\t]')
            while self.flag:
                if line:
                    line = regex.sub(" ", line)
                    # print('(Main) line = ', line)
                    line_treated = line.split(';')
                    for i in range(line.count(';')):
                        self.list_data.append(int(line_treated[i]))
                    # print('(Main) list_data = ', list_data)
                    kwarg = self.file_analyse.get_dic_from_two_lists(list_column, self.list_data)
                    # print('(Main) line merge = ', kwarg)
                    self.list_data.clear()
                    result = self.database.add_data(**kwarg)
                    kwarg.clear()
                    # print('(Main) kwarg = ', kwarg)
                else:
                    print('(Main) line empty')
        return True

    def __str__(self):
        return 'Pipeline'