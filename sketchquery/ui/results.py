# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_resultsetWindow(object):
    def setupUi(self, resultsetWindow):
        resultsetWindow.setObjectName("resultsetWindow")
        resultsetWindow.resize(530, 360)
        self.centralwidget = QtWidgets.QWidget(resultsetWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tblResult = QtWidgets.QTableWidget(self.centralwidget)
        self.tblResult.setGeometry(QtCore.QRect(10, 10, 511, 301))
        self.tblResult.setObjectName("tblResult")
        self.tblResult.setColumnCount(0)
        self.tblResult.setRowCount(0)
        resultsetWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(resultsetWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 22))
        self.menubar.setObjectName("menubar")
        resultsetWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(resultsetWindow)
        self.statusbar.setObjectName("statusbar")
        resultsetWindow.setStatusBar(self.statusbar)

        self.retranslateUi(resultsetWindow)
        QtCore.QMetaObject.connectSlotsByName(resultsetWindow)

    def retranslateUi(self, resultsetWindow):
        _translate = QtCore.QCoreApplication.translate
        resultsetWindow.setWindowTitle(_translate("resultsetWindow", "Results"))

