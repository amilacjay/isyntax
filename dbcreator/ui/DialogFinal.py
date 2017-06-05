# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogFinal.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(910, 596)
        self.btn_browse = QtWidgets.QPushButton(Dialog)
        self.btn_browse.setGeometry(QtCore.QRect(150, 20, 111, 31))
        self.btn_browse.setObjectName("btn_browse")
        self.btn_reset = QtWidgets.QPushButton(Dialog)
        self.btn_reset.setGeometry(QtCore.QRect(270, 20, 111, 31))
        self.btn_reset.setObjectName("btn_reset")
        self.description = QtWidgets.QTextEdit(Dialog)
        self.description.setGeometry(QtCore.QRect(20, 60, 871, 141))
        self.description.setReadOnly(True)
        self.description.setObjectName("description")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.label.setObjectName("label")
        self.btn_analyze = QtWidgets.QPushButton(Dialog)
        self.btn_analyze.setGeometry(QtCore.QRect(20, 230, 111, 31))
        self.btn_analyze.setObjectName("btn_analyze")
        self.btn_generate = QtWidgets.QPushButton(Dialog)
        self.btn_generate.setGeometry(QtCore.QRect(140, 230, 111, 31))
        self.btn_generate.setObjectName("btn_generate")
        self.btn_execute = QtWidgets.QPushButton(Dialog)
        self.btn_execute.setGeometry(QtCore.QRect(260, 230, 111, 31))
        self.btn_execute.setObjectName("btn_execute")
        self.chk_generatetxt = QtWidgets.QCheckBox(Dialog)
        self.chk_generatetxt.setGeometry(QtCore.QRect(380, 230, 121, 31))
        self.chk_generatetxt.setObjectName("chk_generatetxt")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 300, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(270, 300, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.entitylist = QtWidgets.QListWidget(Dialog)
        self.entitylist.setGeometry(QtCore.QRect(20, 320, 231, 261))
        self.entitylist.setObjectName("entitylist")
        self.attributetable = QtWidgets.QTableWidget(Dialog)
        self.attributetable.setGeometry(QtCore.QRect(270, 320, 621, 261))
        self.attributetable.setObjectName("attributetable")
        self.attributetable.setColumnCount(0)
        self.attributetable.setRowCount(0)
        self.txt_displaysql = QtWidgets.QTextEdit(Dialog)
        self.txt_displaysql.setGeometry(QtCore.QRect(510, 230, 381, 71))
        self.txt_displaysql.setObjectName("txt_displaysql")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(510, 210, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_browse.setText(_translate("Dialog", "Browse"))
        self.btn_reset.setText(_translate("Dialog", "Reset"))
        self.label.setText(_translate("Dialog", "Database Description:"))
        self.btn_analyze.setText(_translate("Dialog", "Analyze"))
        self.btn_generate.setText(_translate("Dialog", "Generate SQL"))
        self.btn_execute.setText(_translate("Dialog", "Execute"))
        self.chk_generatetxt.setText(_translate("Dialog", "Generate Text File"))
        self.label_2.setText(_translate("Dialog", "Entities :"))
        self.label_3.setText(_translate("Dialog", "Attributes :"))
        self.label_4.setText(_translate("Dialog", "SQL:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

