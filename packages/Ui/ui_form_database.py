from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Database(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form_Database, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.Form_Database = QtWidgets.QWidget()

        self.label1 = QtWidgets.QLabel('Database name')
        self.label2 = QtWidgets.QLabel('IP address')
        self.label3 = QtWidgets.QLabel('Port')
        self.label4 = QtWidgets.QLabel('User name')
        self.label5 = QtWidgets.QLabel('Password')

        self.line_edit1 = QtWidgets.QLineEdit('database1')
        self.line_edit2 = QtWidgets.QLineEdit('127.0.0.1')
        self.line_edit3 = QtWidgets.QLineEdit('8529')
        self.line_edit4 = QtWidgets.QLineEdit('root')
        self.line_edit5 = QtWidgets.QLineEdit('')

        self.layout1 = QtWidgets.QGridLayout()

        self.layout1.addWidget(self.label1, 0, 0)
        self.layout1.addWidget(self.label2, 1, 0)
        self.layout1.addWidget(self.label3, 2, 0)
        self.layout1.addWidget(self.label4, 3, 0)
        self.layout1.addWidget(self.label5, 4, 0)

        self.layout1.addWidget(self.line_edit1, 0, 1)
        self.layout1.addWidget(self.line_edit2, 1, 1)
        self.layout1.addWidget(self.line_edit3, 2, 1)
        self.layout1.addWidget(self.line_edit4, 3, 1)
        self.layout1.addWidget(self.line_edit5, 4, 1)

        self.Form_Database.setLayout(self.layout1)
        self.Form_Database.show()

    def hide_ui(self):
        self.label1.hide()
        self.label2.hide()
        self.label3.hide()
        self.label4.hide()
        self.label5.hide()

        self.line_edit1.hide()
        self.line_edit2.hide()
        self.line_edit3.hide()
        self.line_edit4.hide()
        self.line_edit5.hide()

    def __del__(self):
        # print('(Ui_Form_Database)(__del__)')
        self.label1.deleteLater()
        self.label2.deleteLater()
        self.label3.deleteLater()
        self.label4.deleteLater()
        self.label5.deleteLater()

        self.line_edit1.deleteLater()
        self.line_edit2.deleteLater()
        self.line_edit3.deleteLater()
        self.line_edit4.deleteLater()
        self.line_edit5.deleteLater()
