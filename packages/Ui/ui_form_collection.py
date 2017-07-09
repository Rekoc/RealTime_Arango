from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Collection(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form_Collection, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.Form_Collection = QtWidgets.QWidget()

        self.label1 = QtWidgets.QLabel('Collection name')

        self.line_edit1 = QtWidgets.QLineEdit('test3')

        self.layout1 = QtWidgets.QGridLayout()

        self.layout1.addWidget(self.label1, 0, 0)

        self.layout1.addWidget(self.line_edit1, 0, 1)

        self.Form_Collection.setLayout(self.layout1)
        self.Form_Collection.show()

    def hide_ui(self):
        self.label1.hide()

        self.line_edit1.hide()

    def __del__(self):
        # print('(Ui_Form_Database)(__del__)')
        self.label1.deleteLater()

        self.line_edit1.deleteLater()
