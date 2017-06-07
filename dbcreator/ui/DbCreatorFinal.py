from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem
from PyQt5.QtWidgets import QTableWidgetItem
# from PyQt5.QtWidgets import
from dbcreator.database_connection.db_connection import DbConnection

from dbcreator.app import App
from dbcreator.core import getContentFromFile
from dbcreator.core import createSQLScript
from dbcreator.models import DataType


class Ui_Dialog(object):
    def __init__(self):
        super().__init__()

        self.setupUi()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(941, 596)
        self.btn_browse = QtWidgets.QPushButton(Dialog)
        self.btn_browse.setGeometry(QtCore.QRect(150, 20, 111, 31))
        self.btn_browse.setObjectName("btn_browse")
        self.btn_reset = QtWidgets.QPushButton(Dialog)
        self.btn_reset.setGeometry(QtCore.QRect(270, 20, 111, 31))
        self.btn_reset.setObjectName("btn_reset")
        self.description = QtWidgets.QTextEdit(Dialog)
        self.description.setGeometry(QtCore.QRect(20, 60, 901, 141))
        self.description.setReadOnly(False)
        self.description.setObjectName("description")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.label.setObjectName("label")
        self.btn_analyze = QtWidgets.QPushButton(Dialog)
        self.btn_analyze.setGeometry(QtCore.QRect(20, 230, 111, 31))
        self.btn_analyze.setObjectName("btn_analyze")
        self.btn_analyze.setEnabled(False)
        self.btn_generate = QtWidgets.QPushButton(Dialog)
        self.btn_generate.setGeometry(QtCore.QRect(140, 230, 111, 31))
        self.btn_generate.setObjectName("btn_generate")
        self.btn_generate.setEnabled(False)
        self.btn_execute = QtWidgets.QPushButton(Dialog)
        self.btn_execute.setGeometry(QtCore.QRect(260, 230, 111, 31))
        self.btn_execute.setObjectName("btn_execute")
        self.btn_execute.setEnabled(False)
        self.chk_generatetxt = QtWidgets.QCheckBox(Dialog)
        self.chk_generatetxt.setGeometry(QtCore.QRect(380, 230, 121, 31))
        self.chk_generatetxt.setObjectName("chk_generatetxt")
        self.chk_generatetxt.setEnabled(False)
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
        self.entitylist.setEnabled(True)
        self.entitylist.setGeometry(QtCore.QRect(20, 320, 231, 261))
        self.entitylist.setAutoFillBackground(False)
        self.entitylist.setProperty("readOnly", False)
        self.entitylist.setObjectName("entitylist")
        self.attributetable = QtWidgets.QTableWidget(Dialog)
        self.attributetable.setGeometry(QtCore.QRect(270, 320, 651, 261))
        self.attributetable.setObjectName("attributetable")
        self.attributetable.setColumnCount(0)
        self.attributetable.setRowCount(0)
        self.txt_displaysql = QtWidgets.QTextEdit(Dialog)
        self.txt_displaysql.setGeometry(QtCore.QRect(510, 230, 411, 71))
        self.txt_displaysql.setReadOnly(True)
        self.txt_displaysql.setObjectName("txt_displaysql")
        self.txt_displaysql.setEnabled(False)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(510, 210, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

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

        ##functions

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

        def generateSqlClicked(self):
            script = createSQLScript(self.entities)

            if self.checkBox.isChecked():
                fileName = str(self.filePath).split('/')[len(str(self.filePath).split('/')) - 1]
                output = open('../generated_sql/' + fileName.replace(".txt", ".sql"), 'w')
                print(script, file=output)
                output.close()

            self.executableScript = script.replace('\n', '').replace('\t', '')
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
                msg.setText("SQL Syntax Error!!")
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
                comboPk = QComboBox()
                comboPk.currentTextChanged.connect(self.comboBoxChangedPk)
                comboPk.addItems([str(d) for d in [True, False]])

                comboDt = QComboBox()
                comboDt.currentTextChanged.connect(self.comboBoxChangedDt)
                comboDt.addItems([str(d) for d in list(DataType)])

                comboNu = QComboBox()
                comboNu.currentTextChanged.connect(self.comboBoxChangedNu)
                comboNu.addItems([str(d) for d in [True, False]])

                comboUq = QComboBox()
                comboUq.currentTextChanged.connect(self.comboBoxChangedUq)
                comboUq.addItems([str(d) for d in [True, False]])

                self.attributetable.setItem(row, 0, QTableWidgetItem(attr.name()))
                self.attributetable.setCellWidget(row, 1, comboPk)
                comboPk.setCurrentText(str(attr.isPrimaryKey))
                comboPk.setProperty('attribute', attr)
                self.attributetable.setCellWidget(row, 2, comboDt)
                comboDt.setCurrentText(str(attr.dtype))
                comboDt.setProperty('attribute', attr)
                self.attributetable.setCellWidget(row, 3, comboNu)
                comboNu.setCurrentText(str(attr.isNotNull))
                comboNu.setProperty('attribute', attr)
                self.attributetable.setCellWidget(row, 4, comboUq)
                comboUq.setCurrentText(str(attr.isUnique))
                comboUq.setProperty('attribute', attr)
                self.attributetable.setItem(row, 5, QTableWidgetItem(str(attr.data)))

        def resetBtnClicked(self):
            self.btn_analyze.setEnabled(False)
            self.btn_generate.setEnabled(False)
            self.entitylist.clear()
            for i in range(self.attributetable.rowCount()):
                self.attributetable.removeRow(0)
            self.description.clear()

        def closeButtonClicked(self, event):
            pass
            # reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
            #                              QMessageBox.Yes | QMessageBox.No,
            #                              QMessageBox.No)
            #
            # if reply == QMessageBox.Yes:
            #     event.accept()
            # else:
            #     event.ignore()

        def tableRowClicked(self, row, column):
            print(row, column)

        def comboBoxChangedPk(self, pk):
            attr = self.sender().property('attribute')
            if (attr != None):
                attr.isPrimaryKey = pk

        def comboBoxChangedDt(self, dType):
            attr = self.sender().property('attribute')
            if (attr != None):
                attr.dtype = DataType[str(dType)]

        def comboBoxChangedNu(self, nu):
            attr = self.sender().property('attribute')
            if (attr != None):
                attr.isNotNull = nu

        def comboBoxChangedUq(self, uq):
            attr = self.sender().property('attribute')
            if (attr != None):
                attr.isUnique = uq

    # if __name__ == "__main__":
    #     import sys
    #     app = QtWidgets.QApplication(sys.argv)
    #     ui = Ui_Dialog()
    #     ui.show()
    #     sys.exit(app.exec_())