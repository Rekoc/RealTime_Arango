# python 3.5.X
# Made for ArangoDB 3.1.X - PyQt5 - Pyuic5

from packages.arangomanagement import DataManagement
from packages.fileanalytics import FileAnalytics
from packages.Ui.ui_mainwindow import Ui_MainWindow
from packages.Ui.ui_terminal import Ui_terminal
from packages.Ui.ui_form_database import Ui_Form_Database
from packages.Ui.ui_form_collection import Ui_Form_Collection
from PyQt5.QtWidgets import QWidget, QDialog, QFileDialog, QErrorMessage, QMessageBox, QLabel, QLineEdit, QFormLayout, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QObject, pyqtSignal
import re
import os


class MainWindow(Ui_MainWindow):

    database = DataManagement()
    ui = object
    term = object
    path_file = ''
    term_var = 0
    term_value_changed = pyqtSignal(int)

    def __init__(self):
        super(MainWindow, self).__init__()
        print('(MainWindow)(__init__) Object created')

    def init(self, Ui_MainWindow):
        self.ui = Ui_MainWindow
        self.database = DataManagement()
        '''self.db12 = '''
        # self.database.create_database()
        # self.database.add_collection('test3')
        # self.database_ui_update()

        #############
        self.ui.pushButton_connection.clicked.connect(self.pushButton_connection_clicked)
        self.ui.pushButton_disconnection.clicked.connect(self.pushButton_disconnection_clicked)
        self.ui.pushButton_scan.clicked.connect(self.pushButton_scan_clicked)
        self.ui.pushButton_create_flux.clicked.connect(self.pushButton_create_flux_clicked)
        self.ui.pushButton_file_import.clicked.connect(self.pushButton_file_import_clicked)
        self.ui.actionUpdate.triggered.connect(self.actionUpdate_clicked)
        self.ui.pushButton_send.clicked.connect(self.pushButton_send)
        ##############
        ###DEBUG#####
        self.ui.pushButton_file_import_DEBUG.clicked.connect(self.pushButton_file_import_DEBUG_clicked)
        # self.term_value_changed.connect(self.term_value_changed)
        #############

        # self.term = Terminal()
        self.widget = Ui_Form_Database()
        self.push_button_validation = QPushButton('Send')
        self.ui.verticalLayout.addWidget(self.widget.Form_Database)
        self.ui.verticalLayout.addWidget(self.push_button_validation)
        self.push_button_validation.clicked.connect(self.push_button_database_validation_clicked)

        self.ui.pushButton_send2.hide()
        self.ui.label_collection.hide()
        self.ui.lineEdit_collection.hide()

    def database_ui_update(self):
        self.ui.database_name.setText(self.database._database_name)
        self.ui.ip_address.setText(self.database._database_host)
        self.ui.database_port.setText(str(self.database._database_port))
        self.ui.user_name.setText(str(self.database._user_name))
        if self.database._database_status == True:
            self.ui.status_connection.setText('Available')
        else:
            self.ui.status_connection.setText('Unavailable')

    # Qt Creator slot
    def pushButton_connection_clicked(self):
        # self.term.add_widget('Database name:')
        # self.term.exec_()
        self.ui.label_database_name.show()
        self.ui.lineEdit_database_name.show()
        self.ui.lineEdit_ip_address.show()
        self.ui.label_ip_address.show()
        self.ui.lineEdit_port.show()
        self.ui.label_port.show()
        self.ui.lineEdit_user_name.show()
        self.ui.label_user_name.show()
        self.ui.lineEdit_password.show()
        self.ui.label_password.show()
        self.ui.pushButton_send.show()
        # self.ui.pushButton_send.clicked.connect(self.pushButton_send)

    def pushButton_send(self):
        self.database.database_name = self.ui.lineEdit_database_name.text()
        self.database.database_host = self.ui.lineEdit_ip_address.text()
        self.database.database_port = int(self.ui.lineEdit_port.text())
        self.database.user_name = self.ui.lineEdit_user_name.text()
        self.database.user_password = self.ui.lineEdit_password.text()

        self.ui.label_database_name.hide()
        self.ui.lineEdit_database_name.hide()
        self.ui.lineEdit_ip_address.hide()
        self.ui.label_ip_address.hide()
        self.ui.lineEdit_port.hide()
        self.ui.label_port.hide()
        self.ui.lineEdit_user_name.hide()
        self.ui.label_user_name.hide()
        self.ui.lineEdit_password.hide()
        self.ui.label_password.hide()
        self.ui.pushButton_send.hide()

        self.database.create_database()
        self.database_ui_update()
        self.database.add_collection('test3')
        self.ui.pushButton_send.disconnect()
        self.ui.pushButton_send2.clicked.connect(self.pushButton_send2)

        self.ui.pushButton_send2.show()
        self.ui.label_collection.show()
        self.ui.lineEdit_collection.show()

    def pushButton_send2(self):
        self.database.add_collection(self.ui.lineEdit_collection.text())

        self.ui.pushButton_send2.hide()
        self.ui.label_collection.hide()
        self.ui.lineEdit_collection.hide()

        self.ui.pushButton_connection.setEnabled(True)
        self.ui.pushButton_disconnection.setEnabled(True)
        self.ui.pushButton_file_import_DEBUG.setEnabled(True)

        self.ui.pushButton_send2.disconnect()

    def pushButton_disconnection_clicked(self):
        pass

    def pushButton_scan_clicked(self):
        pass

    def term_value_changed(self):
        print("(MainWindow)(term_value_changed) term_var = ", self.term_var)

    def actionUpdate_clicked(self):
        self.database_ui_update()

    def pushButton_create_flux_clicked(self):
        pass

    def pushButton_file_import_clicked(self):
        # print("(MainWindow)(pushButton_file_import_clicked)")
        self.path_file = QFileDialog.getOpenFileName(None, "Open txt file", os.getenv('HOME'), "Text File (*.txt)")
        self.ui.label_path.setText(self.path_file[0])
        # print("(MainWindow)(pushButton_file_import_clicked) path = ", self.path_file[0])
        # print("(MainWindow)(pushButton_file_import_clicked) path = ", len(self.path_file[0]))

    def pushButton_file_import_DEBUG_clicked(self):
        # path_file = 'TEST_short.TXT'
        if self.path_file[0]=='':
            print("(MainWindow)(pushButton_file_import_DEBUG_clicked) self.path_file[0]=='' ")
            error_message = QMessageBox(None)
            error_message.setText('Please click on "File import" and choose your path first ...')
            error_message.setWindowTitle('Warning')
            error_message.setIconPixmap(QPixmap('../ressource/icon/Warning.png'))
            error_message.exec()
        else:
            file_analyse = FileAnalytics(path=self.path_file[0])
            list_data = []
            konsole = Terminal()

            list_database = konsole.header_creation_automatic('database_9',
                                                          'Blablabla!!!')
            list_column = konsole.column_creation_automatic(['c1', 'c2', 'c3', 'c4',
                                                             'c5', 'c6', 'c7', 'c8', 'q'])
            with open(self.path_file[0], 'r') as file:
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

                del regex, result, kwarg, list_column, list_database, line, konsole, file_analyse, file, line_treated

    def push_button_database_validation_clicked(self):
        self.database.database_name = self.widget.line_edit1.text()
        self.database.database_host = self.widget.line_edit2.text()
        self.database.database_port = self.widget.line_edit3.text()
        self.database.user_name = self.widget.line_edit4.text()
        self.database.user_password = self.widget.line_edit5.text()
        self.push_button_validation.disconnect()
        self.push_button_validation.deleteLater()
        del self.widget

        self.widget = Ui_Form_Collection()
        self.push_button_validation = QPushButton('Send')
        self.ui.verticalLayout.addWidget(self.widget.Form_Collection)
        self.ui.verticalLayout.addWidget(self.push_button_validation)
        self.push_button_validation.clicked.connect(self.push_button_ui_collection_validation_clicked)

    def push_button_ui_collection_validation_clicked(self):
        self.database.add_collection(self.widget.line_edit1.text())
        self.push_button_validation.disconnect()
        self.push_button_validation.deleteLater()
        del self.widget


##########################
##########################
##########################


class Terminal(MainWindow):

    list_column = []
    list_database = []
    ui_terminal = object
    value = ''

    def __init__(self):
        print('(Terminal)(__init__) Terminal object was created')
        super(Terminal, self).__init__()
        self.ui_terminal = Ui_terminal()

    def enter_value(self, parameter):
        print('(Terminal)(enter_value) Enter ', parameter, ' : ')
        value = input()
        print('(Terminal)(enter_value) value = ', value)
        return value

    def enter_value_automatic(self, parameter):
        return parameter

    def _list_column(self):
        print('(Terminal)(_list_column) return list_column')
        return self.list_column

    def _list_database(self):
        print('(Terminal)(_list_database) return list_database')
        return self.list_database

    def database_information(self):
        print('(Terminal)(database_information) BEGIN')
        label = QLabel()
        self.field = QLineEdit()
        self.layoutt = QFormLayout()
        self.layoutt.addRow('lol', self.field)
        self.ui.setCentralWidget(self.layoutt)
        print('(Terminal)(database_information) END')

    def add_widget(self, arg):
        print('(Terminal)(add_widget) BEGIN')
        self.ui_terminal.label.setText(arg)
        # self.ui_terminal.pushButton.clicked.connect(self.pushButton_save_clicked)
        print('(Terminal)(add_widget) END')
        return self.ui_terminal

    def header_creation_manual(self):
        # print('(Terminal)(header_creation_manual) BEGIN')
        # print("Let's create a database ! First of all, you have to enter a database name, next step will be a "
              # "comment and finally the column")
        self.list_database.append(self.enter_value('database name'))
        self.list_database.append(self.enter_value('comment'))
        # print('(Terminal)(header_creation_manual) list_database = ', self.list_database)
        return self._list_database()

    def column_creation_manual(self):
        # print('(Terminal)(column_creation_manual) BEGIN')
        self.list_database.append(self.enter_value('database name'))
        self.list_database.append(self.enter_value('comment'))
        string = ''
        while string != 'q' and string != 'Q':
            string = self.enter_value('column name')
            if string == 'q' or string == 'Q':
                # print('(Terminal)(column_creation_manual) Creation column finish')
                break
            else:
                self.list_column.append(string)
        # print('(Terminal)(column_creation_manual) list_column = ', self.list_column)
        return self._list_column()

    def header_creation_automatic(self, database_name, comment):
        # print('(Terminal)(header_creation_automatic) BEGIN')
        self.list_database.append(database_name)
        self.list_database.append(comment)
        # print('(Terminal)(column_creation_automatic) list_database = ', self.list_database)
        return self._list_database()

    def column_creation_automatic(self, args):
        # print('(Terminal)(column_creation_automatic) BEGIN')
        i = 0
        while args:
            # print('(Terminal)(column_creation_automatic) loop ', i)
            if args[i] == 'q' or args[i] == 'Q':
                # print('(Terminal)(column_creation_automatic) Creation column finish')
                break
            else:
                # print('(Terminal)(column_creation_automatic) arg = ', args[i])
                self.list_column.append(args[i])
                i += 1
        # print('(Terminal)(column_creation_automatic) list_column = ', self.list_column)
        return self._list_column()

    def pushButton_save_clicked(self):
        print('(Terminal)(pushButton_save_clicked) BEGIN')
        self.value = self.ui_terminal.lineEdit.text()
        self.ui_terminal.pushButton.disconnect()
        self.close_QDialog()
        print('(Terminal)(pushButton_save_clicked) END')

    def Ui_terminal_value_change(self):
        self.value = self.ui_terminal.lineEdit.text()
        print("(Terminal)(Ui_terminal_value_change) value =", self.value)

    def close_QDialog(self):
        self.ui_terminal.close()

    def __str__(self):
        return 'Terminal'

    def __delete__(self, instance):
        print('(Terminal)(__delete__) Terminal object will be kill')