'''import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Arango_GUI.mainwindow import Ui_MainWindow
from Arango_GUI.test import Ui_Form'''


'''class ShipHolderApplication():
    def __init__(self, parent=None):
        # super(ShipHolderApplication, self).__init__(parent)
        self.createWidgets()

    def createWidgets(self):
        s = QtGui()
        self.ui = Ui_Form()
        self.ui.setupUi(s)


myapp = ShipHolderApplication()
myapp.show()'''


'''class ExampleApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app

main()                              # run the main function'''

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from packages import *
from packages.Ui import *

app = QApplication(sys.argv)
window = QMainWindow()
ui = ui_mainwindow.Ui_MainWindow()
ui.setupUi(window)

fenetre = mainwindow.MainWindow()
fenetre.init(ui)

# ui est l'objet a modifier pour atteindre l'IHM
# ui.database_name.setText('1234azer')

window.show()
sys.exit(app.exec_())
