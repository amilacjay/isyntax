# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableDetails.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from wordquery.table_fetcher import *

class Ui_Dialog(object):
    def __init__(self, xmlFile):
        self.xmlFile = xmlFile
        self.tblDetails = table_extractor(xmlFile)



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(431, 358)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(220, 20, 61, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 320, 113, 32))
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 40, 391, 271))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableList = QtWidgets.QListWidget(self.widget)
        self.tableList.setObjectName("tableList")
        self.horizontalLayout.addWidget(self.tableList)
        self.attributeList = QtWidgets.QListWidget(self.widget)
        self.attributeList.setObjectName("attributeList")
        self.horizontalLayout.addWidget(self.attributeList)

        self.tableList.addItems([tbld[0][0] for tbld in self.tblDetails])
        self.tableList.itemClicked.connect(self.tableListItemClicked)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Table Details"))
        self.label.setText(_translate("Dialog", "Tables:"))
        self.label_2.setText(_translate("Dialog", "Attributes:"))
        self.pushButton.setText(_translate("Dialog", "Close"))

    def tableListItemClicked(self, item):
        self.attributeList.clear()
        for tblDetail in self.tblDetails:
            if tblDetail[0][0] == item.text():
                self.attributeList.addItems(tblDetail[1])
                break


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

