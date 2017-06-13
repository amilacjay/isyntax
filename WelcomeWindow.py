# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WelcomeWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from configparser import ConfigParser

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMainWindow

from dbnormalizer.ui.main import DBNormalizerWindow
from settings import Ui_Dialog as Settings
from sketchquery.ui.app import SketchQueryWindow
from wordquery.ui.main import WordQueryWindow
from dbcreator.ui.FinalMain import DBCreatorWindow

class WelcomeWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(760, 534)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.btnDBCreator = QtWidgets.QPushButton(self.centralwidget)
        self.btnDBCreator.setGeometry(QtCore.QRect(280, 170, 201, 32))
        self.btnDBCreator.setStyleSheet("")
        self.btnDBCreator.setObjectName("btnDBCreator")
        self.btnDBNormalizer = QtWidgets.QPushButton(self.centralwidget)
        self.btnDBNormalizer.setGeometry(QtCore.QRect(290, 340, 181, 32))
        self.btnDBNormalizer.setObjectName("btnDBNormalizer")
        self.btnQueryBySketch = QtWidgets.QPushButton(self.centralwidget)
        self.btnQueryBySketch.setGeometry(QtCore.QRect(510, 290, 181, 32))
        self.btnQueryBySketch.setObjectName("btnQueryBySketch")
        self.btnQueryByText = QtWidgets.QPushButton(self.centralwidget)
        self.btnQueryByText.setGeometry(QtCore.QRect(50, 290, 181, 32))
        self.btnQueryByText.setObjectName("btnQueryByText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 771, 511))
        self.label.setMinimumSize(QtCore.QSize(771, 511))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 20, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnSettings = QtWidgets.QPushButton(self.centralwidget)
        self.btnSettings.setGeometry(QtCore.QRect(630, 50, 113, 32))
        self.btnSettings.setObjectName("btnSettings")
        self.label.raise_()
        self.btnDBCreator.raise_()
        self.btnQueryBySketch.raise_()
        self.btnQueryByText.raise_()
        self.btnDBNormalizer.raise_()
        self.label_2.raise_()
        self.btnSettings.raise_()
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.btnSettings.clicked.connect(self.showSettings)
        self.btnDBCreator.clicked.connect(self.showDBCreator)
        self.btnQueryByText.clicked.connect(self.showWordQuery)
        self.btnQueryBySketch.clicked.connect(self.showSketchQuery)
        self.btnDBNormalizer.clicked.connect(self.showDBNormalizer)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "NLP Interface for Databases"))
        self.btnDBCreator.setText(_translate("MainWindow", "Database Creator"))
        self.btnDBNormalizer.setText(_translate("MainWindow", "Database Normalizer"))
        self.btnQueryBySketch.setText(_translate("MainWindow", "Query by Sketches"))
        self.btnQueryByText.setText(_translate("MainWindow", "Query by Texts"))
        self.label_2.setText(_translate("MainWindow", "Natural Language Interface for Databases"))
        self.btnSettings.setText(_translate("MainWindow", "Settings"))


    def showSettings(self):
        dialog = QDialog()
        dialog.ui = Settings()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()

    def showDBCreator(self):
        dbCreatorWindow = DBCreatorWindow(self)
        dbCreatorWindow.show()
        self.showMinimized()

    def showWordQuery(self):
        wordQueryWindow = WordQueryWindow(self)
        wordQueryWindow.show()
        self.showMinimized()

    def showSketchQuery(self):
        sketchQueryWindow = SketchQueryWindow(self)
        sketchQueryWindow.show()
        self.showMinimized()

    def showDBNormalizer(self):
        dbNormalizerWindow = DBNormalizerWindow(self)
        dbNormalizerWindow.show()
        self.showMinimized()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    welcomeWindow = WelcomeWindow()
    welcomeWindow.show()
    sys.exit(app.exec_())

