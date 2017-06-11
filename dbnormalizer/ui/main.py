# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from dbnormalizer.experiments.tableNormalizer import *


class DBNormalizerWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(716, 580)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.btnExecute = QtWidgets.QPushButton(self.centralwidget)
        self.btnExecute.setGeometry(QtCore.QRect(190, 260, 151, 32))
        self.btnExecute.setObjectName("btnExecute")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 661, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtFilePath = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtFilePath.setEnabled(False)
        self.txtFilePath.setObjectName("txtFilePath")
        self.horizontalLayout.addWidget(self.txtFilePath)
        self.btnBrowse = QtWidgets.QPushButton(self.layoutWidget)
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 70, 311, 181))
        self.groupBox.setObjectName("groupBox")
        self.txtHost = QtWidgets.QLineEdit(self.groupBox)
        self.txtHost.setGeometry(QtCore.QRect(140, 30, 151, 21))
        self.txtHost.setObjectName("txtHost")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 90, 111, 16))
        self.label.setObjectName("label")
        self.txtPassword = QtWidgets.QLineEdit(self.groupBox)
        self.txtPassword.setGeometry(QtCore.QRect(140, 150, 151, 21))
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")
        self.txtDB = QtWidgets.QLineEdit(self.groupBox)
        self.txtDB.setGeometry(QtCore.QRect(140, 90, 151, 21))
        self.txtDB.setObjectName("txtDB")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.label_5.setObjectName("label_5")
        self.txtPort = QtWidgets.QLineEdit(self.groupBox)
        self.txtPort.setGeometry(QtCore.QRect(140, 60, 151, 21))
        self.txtPort.setObjectName("txtPort")
        self.txtUsername = QtWidgets.QLineEdit(self.groupBox)
        self.txtUsername.setGeometry(QtCore.QRect(140, 120, 151, 21))
        self.txtUsername.setObjectName("txtUsername")
        self.btnTestConn = QtWidgets.QPushButton(self.centralwidget)
        self.btnTestConn.setGeometry(QtCore.QRect(30, 260, 151, 32))
        self.btnTestConn.setObjectName("btnTestConn")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 171, 16))
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 340, 661, 201))
        self.textEdit.setObjectName("textEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 310, 231, 16))
        self.label_7.setObjectName("label_7")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.btnBrowse.clicked.connect(self.browseBtnClicked)
        self.btnExecute.clicked.connect(self.executeBtnClicked)
        self.btnTestConn.clicked.connect(self.testConn)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Database Normalizer"))
        self.btnExecute.setText(_translate("MainWindow", "Execute"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse "))
        self.groupBox.setTitle(_translate("MainWindow", "Database Properties"))
        self.txtHost.setText(_translate("MainWindow", "localhost"))
        self.label_4.setText(_translate("MainWindow", "Port:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.label.setText(_translate("MainWindow", "Database:"))
        self.txtPassword.setText(_translate("MainWindow", "1234"))
        self.txtDB.setText(_translate("MainWindow", "school"))
        self.label_2.setText(_translate("MainWindow", "Username:"))
        self.label_5.setText(_translate("MainWindow", "Host:"))
        self.txtPort.setText(_translate("MainWindow", "3306"))
        self.txtUsername.setText(_translate("MainWindow", "root"))
        self.btnTestConn.setText(_translate("MainWindow", "Test Connection"))
        self.label_6.setText(_translate("MainWindow", "Functional Dependency File:"))
        self.label_7.setText(_translate("MainWindow", "SQL Script for Normalized Database:"))

    def browseBtnClicked(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(directory='../input/', filter='*.txt')
        self.filePath = path
        self.txtFilePath.setText(self.filePath)

    def executeBtnClicked(self):
        start_normalizer(file_name=self.filePath, xml_file=self.txtDB.text() + '.xml')

    def testConn(self):
        try:
            conn = pymysql.connect(host=self.txtHost.text(),
                                   port=int(self.txtPort.text()),
                                   user=self.txtUsername.text(),
                                   passwd=self.txtPassword.text(),
                                   db=self.txtDB.text())
            cur = conn.cursor()
            cur.execute("SELECT version()")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Connection Test successful!")
            version = cur.fetchone()[0]
            msg.setInformativeText('MySQL version: '+ version)
            msg.setWindowTitle("Connection Test")
            msg.setDetailedText("The details are as follows:\nExecuted: SELECT version()\nResult: " + version)
            msg.exec_()

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Connection failed!")
            msg.setDetailedText(e.args[1])
            msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = DBNormalizerWindow()
    window.show()
    sys.exit(app.exec_())

