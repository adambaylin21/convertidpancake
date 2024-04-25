# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from gui import Ui_MainWindow
from logic import convertID

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.convertID)
    
    def convertID(self):
        listlink = self.plainTextEdit.toPlainText()
        listlink = listlink.split('\n')
        final = []
        for link in listlink:
            if link != '':
                result = convertID(link)
                final.append('{}|{}'.format(link, result))

        f = ''.join([line + '\n' for line in final])
        self.plainTextEdit_2.appendPlainText(f)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
