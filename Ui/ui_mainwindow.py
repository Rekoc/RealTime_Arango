# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(50, 40))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 20, 781, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.status_connection = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.status_connection.setObjectName("status_connection")
        self.horizontalLayout.addWidget(self.status_connection)
        self.database_name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.database_name.setObjectName("database_name")
        self.horizontalLayout.addWidget(self.database_name)
        self.database_port = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.database_port.setObjectName("database_port")
        self.horizontalLayout.addWidget(self.database_port)
        self.ip_address = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.ip_address.setObjectName("ip_address")
        self.horizontalLayout.addWidget(self.ip_address)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.user_name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.user_name.setObjectName("user_name")
        self.horizontalLayout.addWidget(self.user_name)
        self.label_fixe1 = QtWidgets.QLabel(self.centralwidget)
        self.label_fixe1.setGeometry(QtCore.QRect(40, 10, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_fixe1.setFont(font)
        self.label_fixe1.setObjectName("label_fixe1")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(220, 10, 551, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 10, 21, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 50, 781, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton_scan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_scan.setEnabled(True)
        self.pushButton_scan.setGeometry(QtCore.QRect(630, 90, 113, 32))
        self.pushButton_scan.setObjectName("pushButton_scan")
        self.pushButton_file_import = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_file_import.setGeometry(QtCore.QRect(10, 90, 113, 32))
        self.pushButton_file_import.setObjectName("pushButton_file_import")
        self.pushButton_create_flux = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_flux.setGeometry(QtCore.QRect(320, 90, 113, 32))
        self.pushButton_create_flux.setObjectName("pushButton_create_flux")
        self.pushButton_file_import_DEBUG = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_file_import_DEBUG.setGeometry(QtCore.QRect(10, 120, 181, 51))
        self.pushButton_file_import_DEBUG.setObjectName("pushButton_file_import_DEBUG")
        self.pushButton_connection = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_connection.setGeometry(QtCore.QRect(10, 60, 113, 32))
        self.pushButton_connection.setObjectName("pushButton_connection")
        self.pushButton_disconnection = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_disconnection.setGeometry(QtCore.QRect(320, 60, 113, 32))
        self.pushButton_disconnection.setObjectName("pushButton_disconnection")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 180, 371, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_widget = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_widget.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_widget.setObjectName("verticalLayout_widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.menuDatabase.addAction(self.actionUpdate)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.status_connection.setText(_translate("MainWindow", "database_status"))
        self.database_name.setText(_translate("MainWindow", "database_name"))
        self.database_port.setText(_translate("MainWindow", "database_port"))
        self.ip_address.setText(_translate("MainWindow", "database_ip_address"))
        self.label.setText(_translate("MainWindow", "                       User:"))
        self.user_name.setText(_translate("MainWindow", "user_name"))
        self.label_fixe1.setText(_translate("MainWindow", "Database information"))
        self.pushButton_scan.setText(_translate("MainWindow", "Scan"))
        self.pushButton_file_import.setText(_translate("MainWindow", "File import"))
        self.pushButton_create_flux.setText(_translate("MainWindow", "Create flux"))
        self.pushButton_file_import_DEBUG.setText(_translate("MainWindow", "File import DEBUG"))
        self.pushButton_connection.setText(_translate("MainWindow", "Connection"))
        self.pushButton_disconnection.setText(_translate("MainWindow", "Disconnection"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
