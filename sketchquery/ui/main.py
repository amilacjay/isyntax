# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2
import pymysql


class Ui_MainWindow(object):
    def __init__(self):
        self.imagePath = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 90, 211, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 120, 211, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 200, 751, 131))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 360, 321, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 360, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 390, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 420, 111, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 390, 151, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 420, 151, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 160, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 460, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 751, 33))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.btnBrowse = QtWidgets.QPushButton(self.widget)
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.btnBrowse.clicked.connect(self.browseClicked)
        self.pushButton_2.clicked.connect(self.executeClicked)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "Generate Intermediate Results"))
        self.checkBox_2.setText(_translate("MainWindow", "Preview Intermediate Results"))
        self.label.setText(_translate("MainWindow", "MySQL DB name:"))
        self.label_2.setText(_translate("MainWindow", "Username:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.pushButton.setText(_translate("MainWindow", "Generate SQL"))
        self.pushButton_2.setText(_translate("MainWindow", "Execute"))
        self.btnBrowse.setText(_translate("MainWindow", "Browse Sketch"))

    def browseClicked(self, e):
        ret = QFileDialog.getOpenFileName(filter='Images (*.png *.xpm *.jpg)')
        self.imagePath = ret[0]
        self.lineEdit.setText(self.imagePath)
        image = cv2.imread(self.imagePath)
        cv2.imshow('Preview', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def executeClicked(self, e):
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='sinhalalyrics')
        cur = conn.cursor()
        cur.execute(self.plainTextEdit.toPlainText())
        for row in cur:
            print(row)
        cur.close()
        conn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

