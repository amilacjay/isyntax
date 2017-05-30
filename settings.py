# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from configparser import ConfigParser

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(330, 297)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.btnSave = QtWidgets.QPushButton(Dialog)
        self.btnSave.setGeometry(QtCore.QRect(220, 250, 91, 32))
        self.btnSave.setDefault(True)
        self.btnSave.setObjectName("btnSave")
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setGeometry(QtCore.QRect(138, 250, 91, 32))
        self.btnCancel.setObjectName("btnCancel")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 291, 201))
        self.groupBox.setObjectName("groupBox")
        self.txtDatabase = QtWidgets.QLineEdit(self.groupBox)
        self.txtDatabase.setGeometry(QtCore.QRect(120, 160, 161, 21))
        self.txtDatabase.setObjectName("txtDatabase")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 60, 16))
        self.label_3.setObjectName("label_3")
        self.txtHost = QtWidgets.QLineEdit(self.groupBox)
        self.txtHost.setGeometry(QtCore.QRect(120, 40, 161, 21))
        self.txtHost.setObjectName("txtHost")
        self.txtPort = QtWidgets.QLineEdit(self.groupBox)
        self.txtPort.setGeometry(QtCore.QRect(120, 70, 161, 21))
        self.txtPort.setObjectName("txtPort")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 60, 16))
        self.label.setObjectName("label")
        self.txtPassword = QtWidgets.QLineEdit(self.groupBox)
        self.txtPassword.setGeometry(QtCore.QRect(120, 130, 161, 21))
        self.txtPassword.setObjectName("txtPassword")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_6.setObjectName("label_6")
        self.txtUsername = QtWidgets.QLineEdit(self.groupBox)
        self.txtUsername.setGeometry(QtCore.QRect(120, 100, 161, 21))
        self.txtUsername.setObjectName("txtUsername")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btnSave.clicked.connect(self.save)

        config = ConfigParser()
        config.read('config.ini')

        self.txtHost.setText(config.get('Global', 'host'))
        self.txtPort.setText(config.get('Global', 'port'))
        self.txtUsername.setText(config.get('Global', 'username'))
        self.txtPassword.setText(config.get('Global', 'password'))
        self.txtDatabase.setText(config.get('Global', 'database'))



    def save(self):
        config = ConfigParser()
        config.read('config.ini')
        config.set('Global', 'host', self.txtHost.text())
        config.set('Global', 'port', self.txtPort.text())
        config.set('Global', 'username', self.txtUsername.text())
        config.set('Global', 'password', self.txtPassword.text())
        config.set('Global', 'database', self.txtDatabase.text())

        file = open("config.ini", 'w')
        config.write(file)
        file.close()
        self.dialog.close()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.btnSave.setText(_translate("Dialog", "Save"))
        self.btnCancel.setText(_translate("Dialog", "Cancel"))
        self.groupBox.setTitle(_translate("Dialog", "Global Database Settings"))
        self.label_5.setText(_translate("Dialog", "Password:"))
        self.label_3.setText(_translate("Dialog", "Port:"))
        self.label.setText(_translate("Dialog", "Host:"))
        self.label_4.setText(_translate("Dialog", "Username:"))
        self.label_6.setText(_translate("Dialog", "Database:"))

