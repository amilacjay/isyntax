


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from sketchquery.app import *
from sketchquery.ui.results import ResultDialog


class SketchQueryWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.filePath = None
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(720, 582)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.intermediateImages = QtWidgets.QCheckBox(self.centralwidget)
        self.intermediateImages.setGeometry(QtCore.QRect(30, 90, 211, 20))
        self.intermediateImages.setObjectName("intermediateImages")
        self.detailedImage = QtWidgets.QCheckBox(self.centralwidget)
        self.detailedImage.setGeometry(QtCore.QRect(30, 120, 211, 20))
        self.detailedImage.setObjectName("detailedImage")
        self.detailedImage.setChecked(True)
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
        self.txtFile = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtFile.setEnabled(False)
        self.txtFile.setObjectName("txtFile")
        self.horizontalLayout.addWidget(self.txtFile)
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
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        try:
            self.btnTestConn.clicked.connect(self.testConn)
        except Exception as e:
            print(e)

        self.btnBrowse.clicked.connect(self.browseBtnClicked)
        self.btnGenerateSQL.clicked.connect(self.generateSQLClicked)
        self.btnExecute.clicked.connect(self.executeSQL)
        self.btnPrev.clicked.connect(self.showImage)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.intermediateImages.setText(_translate("MainWindow", "Generate Intermediate Images"))
        self.detailedImage.setText(_translate("MainWindow", "Generate Detailed Image"))
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
        self.txtDB.setText(_translate("MainWindow", "hotel"))
        self.label_2.setText(_translate("MainWindow", "Username:"))
        self.label_5.setText(_translate("MainWindow", "Host:"))
        self.txtPort.setText(_translate("MainWindow", "3306"))
        self.txtUsername.setText(_translate("MainWindow", "root"))
        self.btnTestConn.setText(_translate("MainWindow", "Test Connection"))

    def browseBtnClicked(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(directory='sketchquery/samples/', filter='*.png;*.jpg')
        self.filePath = path
        self.txtFile.setText(self.filePath)


    def generateSQLClicked(self):
        if(self.filePath != None):
            conn = pymysql.connect(host=self.txtHost.text(),
                                   port=int(self.txtPort.text()),
                                   user=self.txtUsername.text(),
                                   passwd=self.txtPassword.text(),
                                   db=self.txtDB.text())


            sketchQueryApp = SketchQueryApp(self.filePath, self.detailedImage.isChecked(), self.intermediateImages.isChecked(), conn)
            sql = sketchQueryApp.run()
            self.txtSqlCmd.setPlainText(sql)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please select an image file!")
            msg.exec_()

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
        cur.close()
        conn.close()

    def showImage(self):
        image = cv2.imread(self.filePath)
        ratio, resized = optimalSize(image)
        cv2.imshow('Image', resized)
        cv2.waitKey(0)
        cv2.destroyWindow('Image')


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
    window = SketchQueryWindow()
    window.show()
    sys.exit(app.exec_())

