# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from wordquery.app import App
from wordquery.ui.tableDetails import Ui_Dialog as TableDetailsDialog
import pymysql
from sketchquery.ui.results import ResultDialog

class WordQueryWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(718, 445)
        self.txtSqlCmd = QtWidgets.QPlainTextEdit(self)
        self.txtSqlCmd.setEnabled(True)
        self.txtSqlCmd.setGeometry(QtCore.QRect(30, 100, 661, 101))
        self.txtSqlCmd.setObjectName("txtSqlCmd")
        self.btnGenerateSQL = QtWidgets.QPushButton(self)
        self.btnGenerateSQL.setGeometry(QtCore.QRect(30, 60, 113, 32))
        self.btnGenerateSQL.setObjectName("btnGenerateSQL")
        self.btnTestConn = QtWidgets.QPushButton(self)
        self.btnTestConn.setGeometry(QtCore.QRect(30, 400, 151, 32))
        self.btnTestConn.setObjectName("btnTestConn")
        self.btnExecute = QtWidgets.QPushButton(self)
        self.btnExecute.setGeometry(QtCore.QRect(572, 400, 121, 32))
        self.btnExecute.setDefault(True)
        self.btnExecute.setObjectName("btnExecute")
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 661, 23))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(30, 210, 311, 181))
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
        self.btnTableDetails = QtWidgets.QPushButton(self)
        self.btnTableDetails.setGeometry(QtCore.QRect(140, 60, 151, 32))
        self.btnTableDetails.setObjectName("btnTableDetails")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.btnGenerateSQL.clicked.connect(self.generateSQL)
        self.btnTableDetails.clicked.connect(self.showTableDetails)
        self.btnExecute.clicked.connect(self.executeSQL)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Natural Language Queries"))
        self.btnGenerateSQL.setText(_translate("Dialog", "Generate SQL"))
        self.btnTestConn.setText(_translate("Dialog", "Test Connection"))
        self.btnExecute.setText(_translate("Dialog", "Execute"))
        self.label_6.setText(_translate("Dialog", "Question?"))
        self.groupBox.setTitle(_translate("Dialog", "Database Properties"))
        self.txtHost.setText(_translate("Dialog", "localhost"))
        self.label_4.setText(_translate("Dialog", "Port:"))
        self.label_3.setText(_translate("Dialog", "Password:"))
        self.label.setText(_translate("Dialog", "Database:"))
        self.txtPassword.setText(_translate("Dialog", "1234"))
        self.txtDB.setText(_translate("Dialog", "company_new_new"))
        self.label_2.setText(_translate("Dialog", "Username:"))
        self.label_5.setText(_translate("Dialog", "Host:"))
        self.txtPort.setText(_translate("Dialog", "3306"))
        self.txtUsername.setText(_translate("Dialog", "root"))
        self.btnTableDetails.setText(_translate("Dialog", "Show Table Details"))

    def closeEvent(self, QCloseEvent):
        self.parent().showNormal()

    def generateSQL(self):
        wordQueryApp = App(self.lineEdit.text())
        sql, self.xmlFile = wordQueryApp.run('wordquery/out/')

        self.txtSqlCmd.setPlainText(sql)

    def showTableDetails(self):
        dialogWindow = QtWidgets.QDialog()
        ui = TableDetailsDialog(self.xmlFile)
        ui.setupUi(dialogWindow)
        dialogWindow.exec_()

    def executeSQL(self):
        conn = pymysql.connect(host=self.txtHost.text(),
                               port=int(self.txtPort.text()),
                               user=self.txtUsername.text(),
                               passwd=self.txtPassword.text(),
                               db=self.txtDB.text())
        cur = conn.cursor()
        cur.execute(self.txtSqlCmd.toPlainText())
        data = cur.fetchall()
        columns = [col[0] for col in cur.description]
        resultDialog = ResultDialog(self, data=data, columns=columns)
        resultDialog.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wordQueryWindow = WordQueryWindow()
    wordQueryWindow.show()
    sys.exit(app.exec_())

