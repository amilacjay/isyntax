from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem
from PyQt5.QtWidgets import QTableWidgetItem
from dbcreator.database_connection.db_connection import DbConnection

from dbcreator.app import App
from dbcreator.core import getContentFromFile
from dbcreator.core import createSQLScript
from dbcreator.models import DataType


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(911, 584)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.label.setObjectName("label")
        self.btn_browse = QtWidgets.QPushButton(self.centralwidget)
        self.btn_browse.setGeometry(QtCore.QRect(160, 10, 113, 32))
        self.btn_browse.setObjectName("btn_browse")
        self.description = QtWidgets.QTextEdit(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(20, 50, 871, 141))
        self.description.setReadOnly(True)
        self.description.setObjectName("description")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 250, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.entitylist = QtWidgets.QListWidget(self.centralwidget)
        self.entitylist.setGeometry(QtCore.QRect(20, 270, 231, 261))
        self.entitylist.setObjectName("entitylist")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 250, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.attributetable = QtWidgets.QTableWidget(self.centralwidget)
        self.attributetable.setGeometry(QtCore.QRect(270, 270, 621, 261))
        self.attributetable.setObjectName("attributetable")
        self.attributetable.setColumnCount(0)
        self.attributetable.setRowCount(0)
        self.btn_analyze = QtWidgets.QPushButton(self.centralwidget)
        self.btn_analyze.setGeometry(QtCore.QRect(20, 210, 113, 32))
        self.btn_analyze.setObjectName("btn_analyze")
        self.btn_analyze.setEnabled(False)
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate.setGeometry(QtCore.QRect(140, 210, 113, 32))
        self.btn_generate.setObjectName("btn_generate")
        self.btn_generate.setEnabled(False)
        self.btn_execute = QtWidgets.QPushButton(self.centralwidget)
        self.btn_execute.setGeometry(QtCore.QRect(260, 210, 113, 32))
        self.btn_execute.setObjectName("btn_execute")
        self.btn_execute.setEnabled(False)
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(280, 10, 113, 32))
        self.btn_reset.setObjectName("btn_reset")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(390, 200, 141, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setEnabled(False)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(390, 230, 141, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setEnabled(False)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)


        # combobox = QtGui.QComboBox()
        # combo_box_options = ["VARCHAR(50)", "INTEGER", "CHAR", "DOUBLE", "DATETIME"]
        # for item in combo_box_options:
        #     combobox.addItem(item)
        # self.attributetable.setCellWidget(0, 2, QTableWidgetItem)


        ###
        self.closeEvent = self.closeButtonClicked
        self.btn_browse.clicked.connect(self.browseBtnClicked)
        self.btn_analyze.clicked.connect(self.analyzeBtnClicked)
        self.entitylist.itemClicked.connect(self.entityListItemClicked)
        self.btn_reset.clicked.connect(self.resetBtnClicked)
        self.btn_generate.clicked.connect(self.generateSqlClicked)
        self.btn_execute.clicked.connect(self.executeBtnClicked)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Database Creator"))
        self.label.setText(_translate("MainWindow", "Database Description:"))
        self.btn_browse.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Attributes :"))
        self.label_2.setText(_translate("MainWindow", "Entities :"))
        self.btn_analyze.setText(_translate("MainWindow", "Analyze"))
        self.btn_generate.setText(_translate("MainWindow", "Generate SQL"))
        self.btn_execute.setText(_translate("MainWindow", "Execute"))
        self.btn_reset.setText(_translate("MainWindow", "Reset"))
        self.checkBox.setText(_translate("MainWindow", "Generate Text File"))
        self.checkBox_2.setText(_translate("MainWindow", "Generate Database"))

    ##functions

    def closeButtonClicked(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def browseBtnClicked(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(directory='../samples/', filter='*.txt')
        self.filePath = path
        if self.filePath != '':
            content = getContentFromFile(path)
            self.description.setText(content)
            if (content.strip() != ''):
                self.btn_analyze.setEnabled(True)
            else:
                self.btn_analyze.setEnabled(False)


    def analyzeBtnClicked(self):
        app = App(filePath=self.filePath)
        self.entities = app.run()
        self.addEntitiesToList(self.entities)

        if (len(self.entities) > 0):
            self.btn_generate.setEnabled(True)
            self.checkBox.setEnabled(True)
            self.checkBox_2.setEnabled(True)
        else:
            self.btn_generate.setEnabled(False)

    # def generateSqlClicked(self):
    #
    #     script = self.createSQLScript()
    #
    #     fileName = str(self.filePath).split('/')[len(str(self.filePath).split('/'))-1]
    #
    #     output = open('../generated_sql/'+fileName.replace(".txt",".sql"), 'w')
    #     print(script, file=output)
    #     output.close()

    # def createSQLScript(self):
    #     wholeSQL = ''
    #     for entity in self.entities:
    #         firstLine = "DROP TABLE IF EXISTS {} CASCADE; CREATE TABLE {} (".format(entity.name(), entity.name())
    #         queryBody = '\n'
    #         delimiter = ',\n'
    #         lastLine = "\n);\n\n"
    #
    #         attributeList = entity.getAttributes()
    #         for i, attribute in enumerate(attributeList):
    #             uniqueKW = ' UNIQUE'
    #             attributeLine = '\t{} {}{}'.format(attribute.name(), attribute.dtype,
    #                                                uniqueKW if attribute.isUnique else '')
    #             if i != len(attributeList) - 1:
    #                 attributeLine = attributeLine + delimiter
    #             queryBody = queryBody + attributeLine
    #
    #         wholeSQL = wholeSQL + (firstLine + queryBody + lastLine)
    #
    #     return wholeSQL


    def generateSqlClicked(self):


        script = createSQLScript(self.entities)

        # script = self.createSQLScript()

        if self.checkBox.isChecked():
            fileName = str(self.filePath).split('/')[len(str(self.filePath).split('/')) - 1]
            output = open('../generated_sql/' + fileName.replace(".txt", ".sql"), 'w')
            print(script, file=output)
            output.close()

        self.executableScript = script.replace('\n','').replace('\t','')
        self.btn_execute.setEnabled(True)


    def executeBtnClicked(self):
        try:
            dbConn = DbConnection()
            dbConn.connectToDb(self.executableScript)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Database has been created!!")
            msg.setDetailedText(self.executableScript)
            msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Connection failed!")
            msg.setDetailedText(e.args[1])
            msg.exec_()


    def addEntitiesToList(self, entities):
        for entity in entities:
            self.entitylist.addItem(entity)

    def entityListItemClicked(self, item):
        self.currentEntity = item
        attributes = item.getAttributes()
        self.attributetable.setColumnCount(6)
        self.attributetable.setHorizontalHeaderLabels(['Name', 'PrimaryKey', 'DataType', 'NULL', 'Unique', 'INFO'])


        self.attributetable.setRowCount(len(attributes))
        for row, attr in enumerate(attributes):
            combo = QComboBox()
            combo.currentTextChanged.connect(self.comboBoxChanged)
            combo.addItems([str(d) for d in list(DataType)])

            self.attributetable.setItem(row, 0, QTableWidgetItem(attr.name()))
            self.attributetable.setItem(row, 1, QTableWidgetItem(str(attr.isPrimaryKey)))
            self.attributetable.setCellWidget(row, 2, combo)
            combo.setCurrentText(str(attr.dtype))
            combo.setProperty('attribute', attr)
            self.attributetable.setItem(row, 3, QTableWidgetItem(str(attr.isNotNull)))
            self.attributetable.setItem(row, 4, QTableWidgetItem(str(attr.isUnique)))
            self.attributetable.setItem(row, 5, QTableWidgetItem(str(attr.data)))


    def resetBtnClicked(self):
        self.btn_analyze.setEnabled(False)
        self.btn_generate.setEnabled(False)
        self.entitylist.clear()
        for i in range(self.attributetable.rowCount()):
            self.attributetable.removeRow(0)
        self.description.clear()

    def tableRowClicked(self, row, column):
        print(row, column)

    def comboBoxChanged(self, dType):
        attr = self.sender().property('attribute')
        if(attr !=None):
            attr.dtype = DataType[str(dType)]

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())