# python 3.5.X
# Made for ArangoDB 3.1.X - PyQt5 - Pyuic5

from Arango_GUI.ui_mainwindow import Ui_MainWindow
from ArangoManagement import DataManagement
from Terminal import Terminal
from FileAnalytics import FileAnalytics
import re


class MainWindow(Ui_MainWindow):

    database = DataManagement()
    ui = object
    term = object
    value = ''

    def __init__(self, Ui_MainWindow):
        print('(MainWindow)(__init__) Object created')
        self.ui = Ui_MainWindow
        self.database = DataManagement()
        '''self.db12 = '''
        self.database.create_database()
        self.database.add_collection('test2')
        self.database_ui_update()
        ###############
        self.ui.pushButton_connection.clicked.connect(self.pushButton_connection_clicked)
        self.ui.pushButton_disconnection.clicked.connect(self.pushButton_disconnection_clicked)
        self.ui.pushButton_scan.clicked.connect(self.pushButton_scan_clicked)
        self.ui.pushButton_create_flux.clicked.connect(self.pushButton_create_flux_clicked)
        self.ui.pushButton_file_import.clicked.connect(self.pushButton_file_import_clicked)
        self.ui.actionUpdate.triggered.connect(self.actionUpdate_clicked)
        ##############
        ###DEBUG#####
        self.ui.pushButton_file_import_DEBUG.clicked.connect(self.pushButton_file_import_DEBUG_clicked)
        #############
        self.term = Terminal(True)

    def database_ui_update(self):
        self.ui.database_name.setText(self.database._database_name)
        self.ui.ip_address.setText(self.database._database_host)
        self.ui.database_port.setText(str(self.database._database_port))
        self.ui.user_name.setText(str(self.database._user_name))
        if self.database._database_status == True:
            self.ui.status_connection.setText('Available')
        else:
            self.ui.status_connection.setText('Unavailable')

    # Qt Creator signals
    def pushButton_connection_clicked(self):
        # self.ui.verticalLayout_widget.addWidget(term.add_widget('Database name:'))
        self.term.add_widget('Database name:')
        self.term.exec_()
        self.term.ui_terminal.pushButton.clicked.connect(self.Ui_terminal_pushButton())

    def Ui_terminal_pushButton(self):
        # self.term.ui_terminal.pushButton.clicked.disconnect()
        self.term.close()
        self.value = self.term.value
        print("(MainWindow)(Ui_terminal_pushButton) value =", self.value)

    def pushButton_disconnection_clicked(self):
        pass

    def pushButton_scan_clicked(self):
        pass

    def actionUpdate_clicked(self):
        self.database_ui_update()

    def pushButton_create_flux_clicked(self):
        pass

    def pushButton_file_import_clicked(self):
        self.ui.addWidget()

    def pushButton_file_import_DEBUG_clicked(self):
        path_file = 'TEST_short.TXT'
        file_analyse = FileAnalytics(path=path_file)
        list_data = []
        konsole = Terminal(False)

        list_database = konsole.header_creation_automatic('database_9',
                                                          'Blablabla!!!')
        list_column = konsole.column_creation_automatic(['c1', 'c2', 'c3', 'c4',
                                                         'c5', 'c6', 'c7', 'c8', 'q'])
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
                    result = self.database.add_data(**kwarg)
                    kwarg.clear()
                    # print('(Main) kwarg = ', kwarg)
                else:
                    print('(Main) line empty')

            result = self.database.add_data(**kwarg)

            del regex, result, kwarg, list_column, list_database, line, konsole, file_analyse, file, path_file, line_treated