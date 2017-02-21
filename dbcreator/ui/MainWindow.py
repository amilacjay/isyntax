# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem
from PyQt5.QtWidgets import QTableWidgetItem

from dbcreator.app import App
from dbcreator.core import getContentFromFile


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(789, 587)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.label.setObjectName("label")
        self.btn_browse = QtWidgets.QPushButton(self.centralwidget)
        self.btn_browse.setGeometry(QtCore.QRect(160, 10, 113, 32))
        self.btn_browse.setObjectName("btn_browse")
        self.description = QtWidgets.QTextEdit(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(20, 50, 751, 141))
        self.description.setReadOnly(True)
        self.description.setObjectName("description")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 250, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.entitylist = QtWidgets.QListWidget(self.centralwidget)
        self.entitylist.setGeometry(QtCore.QRect(20, 270, 231, 261))
        self.entitylist.setObjectName("entitylist")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 250, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.attributetable = QtWidgets.QTableWidget(self.centralwidget)
        self.attributetable.setGeometry(QtCore.QRect(270, 270, 501, 261))
        self.attributetable.setObjectName("attributetable")
        self.attributetable.setColumnCount(0)
        self.attributetable.setRowCount(0)
        self.btn_analyze = QtWidgets.QPushButton(self.centralwidget)
        self.btn_analyze.setGeometry(QtCore.QRect(20, 210, 113, 32))
        self.btn_analyze.setObjectName("btn_analyze")
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate.setGeometry(QtCore.QRect(140, 210, 113, 32))
        self.btn_generate.setObjectName("btn_generate")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 210, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(280, 10, 113, 32))
        self.btn_reset.setObjectName("btn_reset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #####
        MainWindow.closeEvent = self.closeButtonClicked
        self.btn_browse.clicked.connect(self.browseBtnClicked)
        self.btn_analyze.clicked.connect(self.analyzeBtnClicked)
        self.entitylist.itemClicked.connect(self.entityListItemClicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Database Creator"))
        self.label.setText(_translate("MainWindow", "Database Description:"))
        self.btn_browse.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Attributes :"))
        self.label_2.setText(_translate("MainWindow", "Entities :"))
        self.btn_analyze.setText(_translate("MainWindow", "Analyze"))
        self.btn_generate.setText(_translate("MainWindow", "Generate SQL"))
        self.pushButton_3.setText(_translate("MainWindow", "Execute"))
        self.btn_reset.setText(_translate("MainWindow", "Reset"))


    ##functions

    def closeButtonClicked(self, event):
        reply = QMessageBox.question(MainWindow, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def browseBtnClicked(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName()
        self.filePath = path
        self.description.setText(getContentFromFile(path))

    def analyzeBtnClicked(self):
        app = App(filePath=self.filePath)
        entities = app.run()
        self.addEntitiesToList(entities)
        pass

    def addEntitiesToList(self, entities):
        for entity in entities:
            self.entitylist.addItem(entity)

    def entityListItemClicked(self, item):
        attributes = item.getAttributes()
        self.attributetable.setColumnCount(5)
        self.attributetable.setRowCount(len(attributes))
        for row, attr in enumerate(attributes):
            self.attributetable.setItem(row, 0, QTableWidgetItem(str([x[0] for x in attr.name])))
            self.attributetable.setItem(row, 1, QTableWidgetItem("NA"))
            self.attributetable.setItem(row, 2, QTableWidgetItem("NA"))
            self.attributetable.setItem(row, 3, QTableWidgetItem("NA"))
            self.attributetable.setItem(row, 4, QTableWidgetItem("NA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
