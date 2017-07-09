# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'terminal.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_terminal(QtWidgets.QWidget):
    def setupUi(self, terminal):
        terminal.setObjectName("terminal")
        terminal.setWindowModality(QtCore.Qt.WindowModal)
        terminal.resize(480, 71)
        self.horizontalLayoutWidget = QtWidgets.QWidget(terminal)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 461, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(terminal)
        self.pushButton.setGeometry(QtCore.QRect(180, 40, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(terminal)
        QtCore.QMetaObject.connectSlotsByName(terminal)

    def retranslateUi(self, terminal):
        _translate = QtCore.QCoreApplication.translate
        terminal.setWindowTitle(_translate("terminal", "Dialog"))
        self.label.setText(_translate("terminal", "String"))
        self.pushButton.setText(_translate("terminal", "Send"))

