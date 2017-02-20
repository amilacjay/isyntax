from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QToolTip
from dbcreator.app import App

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gobtn = QtWidgets.QPushButton(self.centralwidget)
        self.gobtn.setGeometry(QtCore.QRect(520, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gobtn.setFont(font)
        self.gobtn.setObjectName("gobtn")
        self.entitylist = QtWidgets.QListWidget(self.centralwidget)
        self.entitylist.setGeometry(QtCore.QRect(30, 140, 221, 261))
        self.entitylist.setObjectName("entitylist")
        self.attributelist = QtWidgets.QListWidget(self.centralwidget)
        self.attributelist.setGeometry(QtCore.QRect(270, 140, 221, 261))
        self.attributelist.setObjectName("attributelist")
        self.clearbtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearbtn.setGeometry(QtCore.QRect(520, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clearbtn.setFont(font)
        self.clearbtn.setObjectName("clearbtn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 120, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 381, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        self.browsebtn = QtWidgets.QPushButton(self.centralwidget)
        self.browsebtn.setGeometry(QtCore.QRect(420, 30, 75, 23))
        self.browsebtn.setObjectName("browsebtn")
        self.relationlist = QtWidgets.QListWidget(self.centralwidget)
        self.relationlist.setGeometry(QtCore.QRect(510, 140, 221, 261))
        self.relationlist.setObjectName("relationlist")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 120, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setWindowIcon(QIcon('isyntax.png'))
        self.gobtn.clicked.connect(self.goBtnClicked)
        self.clearbtn.clicked.connect(self.clearBtnClicked)
        MainWindow.closeEvent = self.cancelBtnClicked
        self.entitylist.itemClicked.connect(self.listItemClicked)
        QToolTip.setFont(QFont('SansSerif', 10))
        self.gobtn.setToolTip("Click to retrieve <b>entities</b> in your text")
        self.clearbtn.setToolTip("Click to clear the text")
        self.browsebtn.clicked.connect(self.browseBtnClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gobtn.setText(_translate("MainWindow", "Go"))
        self.clearbtn.setText(_translate("MainWindow", "Clear"))
        self.label_2.setText(_translate("MainWindow", "Entities :"))
        self.label_3.setText(_translate("MainWindow", "Attributes :"))
        self.browsebtn.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "Relationships:"))

    def browseBtnClicked(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName()
        self.lineEdit.setText(path)


    def goBtnClicked(self, path):
        app = App(path)
        self.entities = app.run()
        self.entitylist.addItem(self.entities)


    def clearBtnClicked(self):
        self.lineEdit.clear()
        self.browsebtn.setFocus()


    def cancelBtnClicked(self, event):
        reply = QMessageBox.question(MainWindow, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def listItemClicked(self, item):
        self.attributelist.clear()
        self.attributelist.addItem(item.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
