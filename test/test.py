from arango import ArangoClient, ArangoError
from Gui.ArangoManagement import DataManagement
from Gui.Terminal import Terminal
from Gui.FileAnalytics import FileAnalytics
from Gui.Pipeline import Pipeline
from multiprocessing import Process
import re
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

print('(Main) BEGIN test.py')

# path_file = 'TEST_ALBi_QUENTIN_motor_1_only.TXT'
path_file = 'TEST_short.TXT'

print('(Main) BEGIN Terminal')
file_analyse = FileAnalytics(path=path_file)
list_data = []
konsole = Terminal(False)



list_database = konsole.header_creation_automatic('database_4',
                                                'Blablabla!!!')
list_column = konsole.column_creation_automatic(['c1', 'c2', 'c3', 'c4',
                                                 'c5', 'c6', 'c7', 'c8', 'q'])
# print('(Main) list_column = ', list_column)
# print('(Main) list_database_option = ', list_database)
print('(Main) END Terminal')

print('')

print('(Main) BEGIN DataManagement')
database = DataManagement()
db12 = database.create_database()
database.add_collection('test1')


print('(Main) END DataManagement')

print('')

# print('(Main)(database.read_data) = ', database.read_data("570034"))

with open(path_file, 'r') as file:
    line = 'empty'
    regex = re.compile(r'[\n\r\t]')
    for line in file:
        line = file.readline()
        if line:
            line = regex.sub(" ", line)
            # print('(Main) line = ', line)
            line_treated = line.split(';')
            for i in range(line.count(';')):
                list_data.append(int(line_treated[i]))
            # print('(Main) list_data = ', list_data)
            kwarg = file_analyse.get_dic_from_two_lists(list_column, list_data)
            # print('(Main) line merge = ', kwarg)
            list_data.clear()
            result = database.add_data(**kwarg)
            kwarg.clear()
            # print('(Main) kwarg = ', kwarg)
        else:
            print('(Main) line empty')

result = database.add_data(**kwarg)

print('(Main) Read file END ')

print('')

database.use_query('test1', 'more_than')

# Pipe, Thread  and Mutex
# pipes = pip()

print('')

del database
del db12
del kwarg
del file_analyse
del konsole
del list_column
del list_data
print('(Main) every object were killed')

print('(Main) END test.py')
