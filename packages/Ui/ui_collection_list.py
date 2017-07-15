from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Collection_List(QtWidgets.QWidget):
    def __init__(self, *item_list):
        super(Ui_Collection_List, self).__init__()
        self.setup_ui(item_list)

    def setup_ui(self, item_list):
        self.Collection_List = QtWidgets.QWidget()

        self.list = QtWidgets.QListWidget()
        '''
        We can add some description, icon, ... to the list with QListWidgetItem
        have a look on : http://pythoncentral.io/pyside-pyqt-tutorial-the-qlistwidget/

        self.item = QtWidgets.QListWidgetItem(list)
        '''
        i = 0
        j=len(item_list)
        while i < j:
            # print('(Ui_Collection_List)(setup_ui) item_list[i = ', item_list[i])
            self.add_line(item_list[i])
            i += 1

        self.layout1 = QtWidgets.QVBoxLayout()
        self.layout1.addWidget(self.list)

        self.Collection_List.setLayout(self.layout1)
        self.Collection_List.show()

    def add_line(self, element):
        self.list.addItem(element)

    def hide_ui(self):
        pass

    def __del__(self):
        # print('(Ui_Collection_Tree)(__del__)')
        pass