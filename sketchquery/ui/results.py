# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem


class ResultDialog(QMainWindow):
    def __init__(self, parent=None, data=None, columns=None):
        QMainWindow.__init__(self, parent)
        self.data = data
        self.columns = columns
        self.setupUi()


    def setupUi(self):
        self.setObjectName("resultDialog")
        self.resize(572, 363)
        self.results = QtWidgets.QTableWidget(self)
        self.results.setGeometry(QtCore.QRect(10, 20, 551, 321))
        self.results.setObjectName("results")
        self.results.setColumnCount(0)
        self.results.setRowCount(0)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        if(self.columns != None):
            self.results.setColumnCount(len(self.columns))
            self.results.setHorizontalHeaderLabels(self.columns)
            self.results.setRowCount(len(self.data))

            for r, row in enumerate(self.data):
                for c, col in enumerate(row):
                    self.results.setItem(r, c, QTableWidgetItem(col))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("resultDialog", "Results"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    resultDialog = ResultDialog()
    resultDialog.show()
    sys.exit(app.exec_())

