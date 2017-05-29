# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 582)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.enableSaving = QtWidgets.QCheckBox(self.centralwidget)
        self.enableSaving.setGeometry(QtCore.QRect(30, 90, 211, 20))
        self.enableSaving.setObjectName("enableSaving")
        self.enablePrev = QtWidgets.QCheckBox(self.centralwidget)
        self.enablePrev.setGeometry(QtCore.QRect(30, 120, 211, 20))
        self.enablePrev.setObjectName("enablePrev")
        self.txtSqlCmd = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtSqlCmd.setEnabled(True)
        self.txtSqlCmd.setGeometry(QtCore.QRect(30, 200, 661, 101))
        self.txtSqlCmd.setObjectName("txtSqlCmd")
        self.btnGenerateSQL = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerateSQL.setGeometry(QtCore.QRect(30, 160, 113, 32))
        self.btnGenerateSQL.setObjectName("btnGenerateSQL")
        self.btnExecute = QtWidgets.QPushButton(self.centralwidget)
        self.btnExecute.setGeometry(QtCore.QRect(572, 500, 121, 32))
        self.btnExecute.setObjectName("btnExecute")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 661, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.btnBrowse = QtWidgets.QPushButton(self.layoutWidget)
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.btnPrev = QtWidgets.QPushButton(self.layoutWidget)
        self.btnPrev.setObjectName("btnPrev")
        self.horizontalLayout.addWidget(self.btnPrev)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 310, 311, 181))
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
        self.btnTestConn.setGeometry(QtCore.QRect(30, 500, 151, 32))
        self.btnTestConn.setObjectName("btnTestConn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        try:
            self.btnTestConn.clicked.connect(self.testConn)
        except Exception as e:
            print(e)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enableSaving.setText(_translate("MainWindow", "Generate Intermediate Results"))
        self.enablePrev.setText(_translate("MainWindow", "Preview Intermediate Results"))
        self.btnGenerateSQL.setText(_translate("MainWindow", "Generate SQL"))
        self.btnExecute.setText(_translate("MainWindow", "Execute"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse Sketch"))
        self.btnPrev.setText(_translate("MainWindow", "Preview "))
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
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

