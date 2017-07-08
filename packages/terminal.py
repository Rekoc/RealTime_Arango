# python 3.5.X
# Database management creation Terminal

from packages.mainwindow import *
from packages.Ui import ui_terminal


class Terminal(MainWindow):

    list_column = []
    list_database = []
    ui_terminal = object
    value = ''

    def __init__(self, select_mode=True, parent=None):
        print('(Terminal)(__init__) Terminal object was created')
        super(Terminal, self).__init__(parent)
        self.ui_terminal = ui_terminal.Ui_terminal()

        if select_mode:
            pass
            # print('(Terminal)(__init__) Manual mode selected')
            # self.header_creation_manual()
        else:
            # print('(Terminal)(__init__) Automatic mode selected')
            pass

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

    def add_widget(self, arg):
        self.ui_terminal.setupUi(self)
        self.ui_terminal.label.setText(arg)
        # self.ui_terminal.pushButton.clicked.connect(self.pushButton_save_clicked)
        # self.value_change.connect(self.Ui_terminal_value_change)
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
        # self.ui_terminal.pushButton.disconnect()
        # super.value_change.emit(self.value)
        print('(Terminal)(pushButton_save_clicked) END')

    def Ui_terminal_value_change(self):
        self.value = self.ui_terminal.lineEdit.text()
        print("(Terminal)(Ui_terminal_value_change) value =", self.value)

    def close_QDialog(self):
        self.close()

    def __str__(self):
        return 'Terminal'

    def __delete__(self, instance):
        print('(Terminal)(__delete__) Terminal object will be kill')


