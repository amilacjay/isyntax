from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem

from dbcreator.database_connection.db_connection import DbConnection
from dbcreator.app import App
from dbcreator.core import *
from dbcreator.models import *


class DBCreatorWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(943, 690)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.label.setObjectName("label")
        self.btn_browse = QtWidgets.QPushButton(self.centralwidget)
        self.btn_browse.setGeometry(QtCore.QRect(140, 10, 113, 32))
        self.btn_browse.setObjectName("btn_browse")
        self.description = QtWidgets.QTextEdit(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(20, 50, 901, 141))
        self.description.setReadOnly(False)
        self.description.setObjectName("description")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 250, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.entitylist = QtWidgets.QListWidget(self.centralwidget)
        self.entitylist.setGeometry(QtCore.QRect(20, 270, 201, 261))
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
        self.attributetable.setGeometry(QtCore.QRect(230, 270, 691, 261))
        self.attributetable.setObjectName("attributetable")
        self.attributetable.setColumnCount(0)
        self.attributetable.setRowCount(0)
        self.btn_analyze = QtWidgets.QPushButton(self.centralwidget)
        self.btn_analyze.setEnabled(False)
        self.btn_analyze.setGeometry(QtCore.QRect(20, 200, 113, 32))
        self.btn_analyze.setObjectName("btn_analyze")
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate.setEnabled(False)
        self.btn_generate.setGeometry(QtCore.QRect(140, 200, 113, 32))
        self.btn_generate.setObjectName("btn_generate")
        self.btn_execute = QtWidgets.QPushButton(self.centralwidget)
        self.btn_execute.setEnabled(False)
        self.btn_execute.setGeometry(QtCore.QRect(380, 200, 113, 32))
        self.btn_execute.setObjectName("btn_execute")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(260, 10, 113, 32))
        self.btn_reset.setObjectName("btn_reset")
        self.chk_generate = QtWidgets.QCheckBox(self.centralwidget)
        self.chk_generate.setEnabled(False)
        self.chk_generate.setGeometry(QtCore.QRect(500, 200, 131, 31))
        self.chk_generate.setObjectName("chk_generate")
        self.relationships = QtWidgets.QTextEdit(self.centralwidget)
        self.relationships.setEnabled(False)
        self.relationships.setGeometry(QtCore.QRect(230, 590, 441, 71))
        self.relationships.setObjectName("relationships")
        self.lbl_relation = QtWidgets.QLabel(self.centralwidget)
        self.lbl_relation.setEnabled(False)
        self.lbl_relation.setGeometry(QtCore.QRect(230, 560, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_relation.setFont(font)
        self.lbl_relation.setObjectName("lbl_relation")
        self.btn_preview = QtWidgets.QPushButton(self.centralwidget)
        self.btn_preview.setEnabled(False)
        self.btn_preview.setGeometry(QtCore.QRect(260, 200, 113, 32))
        self.btn_preview.setObjectName("btn_preview")
        self.chk_NE = QtWidgets.QCheckBox(self.centralwidget)
        self.chk_NE.setEnabled(True)
        self.chk_NE.setGeometry(QtCore.QRect(620, 200, 131, 31))
        self.chk_NE.setObjectName("chk_NE")
        self.chk_nonpotential = QtWidgets.QCheckBox(self.centralwidget)
        self.chk_nonpotential.setEnabled(True)
        self.chk_nonpotential.setGeometry(QtCore.QRect(760, 200, 171, 31))
        self.chk_nonpotential.setObjectName("chk_nonpotential")
        self.chk_relation = QtWidgets.QCheckBox(self.centralwidget)
        self.chk_relation.setEnabled(False)
        self.chk_relation.setGeometry(QtCore.QRect(230, 530, 141, 31))
        self.chk_relation.setObjectName("chk_relation")
        # self.btn_remove = QtWidgets.QPushButton(self.centralwidget)
        # self.btn_remove.setEnabled(False)
        # self.btn_remove.setGeometry(QtCore.QRect(20, 540, 71, 23)) #100, 540, 71, 23
        # self.btn_remove.setObjectName("btn_remove")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 943, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # self.frameGeometry().moveCenter(QtGui.QDesktopWidget().availableGeometry().center())


        ###
        self.closeEvent = self.closeButtonClicked
        self.btn_browse.clicked.connect(self.browseBtnClicked)
        self.btn_analyze.clicked.connect(self.analyzeBtnClicked)
        self.entitylist.itemClicked.connect(self.entityListItemClicked)
        self.btn_reset.clicked.connect(self.resetBtnClicked)
        self.btn_generate.clicked.connect(self.generateSqlClicked)
        self.btn_execute.clicked.connect(self.executeBtnClicked)
        self.chk_relation.clicked.connect(self.relationshipIsChecked)
        self.btn_preview.clicked.connect(self.previewButtonClicked)
        # self.btn_remove.clicked.connect(self.removeButtonClicked)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Database Creator"))
        self.label.setText(_translate("MainWindow", "Database Description:"))
        self.btn_browse.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Attributes :"))
        self.entitylist.setSortingEnabled(False)
        self.label_2.setText(_translate("MainWindow", "Entities :"))
        self.btn_analyze.setText(_translate("MainWindow", "Analyze"))
        self.btn_generate.setText(_translate("MainWindow", "Generate SQL"))
        self.btn_execute.setText(_translate("MainWindow", "Execute"))
        self.btn_reset.setText(_translate("MainWindow", "Reset"))
        self.chk_generate.setText(_translate("MainWindow", "Generate Text File"))
        self.lbl_relation.setText(_translate("MainWindow", "Relationships:"))
        self.btn_preview.setText(_translate("MainWindow", "Preview SQL"))
        self.chk_NE.setText(_translate("MainWindow", "Remove Named Entities"))
        self.chk_nonpotential.setText(_translate("MainWindow", "Remove Non Potential Entities"))
        self.chk_relation.setText(_translate("MainWindow", "Show Relationships"))
        # self.btn_remove.setText(_translate("MainWindow", "Remove"))


    ##functions

    def browseBtnClicked(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(directory='../samples/', filter='*.txt')
        self.filePath = path
        if self.filePath != '':
            content = getContentFromFile(path)
            self.description.setText(content)

            if (content.strip() != ''):
                self.btn_analyze.setEnabled(True)
                self.chk_generate.setEnabled(True)
                self.chk_NE.setEnabled(True)
                self.chk_nonpotential.setEnabled(True)
            else:
                self.btn_analyze.setEnabled(False)


    def analyzeBtnClicked(self):
        app = App(filePath=self.filePath)
        self.entities = app.run(isNEChecked=self.chk_NE.isChecked(), isNPEChecked=self.chk_nonpotential.isChecked())
        self.addEntitiesToList(self.entities)

        if (len(self.entities) > 0):
            self.btn_generate.setEnabled(True)
            self.chk_generate.setEnabled(True)
            self.chk_relation.setEnabled(True)
            # self.btn_remove.setEnabled(True)
        else:
            self.btn_generate.setEnabled(False)
            self.chk_generate.setEnabled(False)
            self.chk_relation.setEnabled(False)
            # self.btn_remove.setEnabled(False)


    def generateSqlClicked(self):
        self.script = createSQLScript(self.entities)

        if self.chk_generate.isChecked():
            fileName = str(self.filePath).split('/')[len(str(self.filePath).split('/')) - 1]
            output = open('../generated_sql/' + fileName.replace(".txt", ".sql"), 'w')
            print(self.script, file=output)
            output.close()

        self.executableScript = self.script.replace('\n','').replace('\t','')
        self.btn_execute.setEnabled(True)
        self.btn_preview.setEnabled(True)
        self.btn_analyze.setEnabled(False)


    def executeBtnClicked(self):
        try:
            dbConn = DbConnection()
            dbConn.connectToDb(self.executableScript, config_path='../../config.ini')

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
        self.attributetable.setColumnCount(7)
        self.attributetable.setHorizontalHeaderLabels(['Name', 'Primary Key', 'Foreign Key', 'Data Type', 'Not Null', 'Unique', 'INFO'])

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

            ##
            self.attributetable.setItem(row, 0, QTableWidgetItem(attr.name().lower()))

            self.attributetable.setCellWidget(row, 1, comboPk)
            comboPk.setCurrentText(str(attr.isPrimaryKey))
            comboPk.setProperty('attribute', attr)

            self.attributetable.setItem(row, 2, QTableWidgetItem(str(attr.isForeignKey)))

            self.attributetable.setCellWidget(row, 3, comboDt)
            comboDt.setCurrentText(str(attr.dtype))
            comboDt.setProperty('attribute', attr)

            self.attributetable.setCellWidget(row, 4, comboNu)
            comboNu.setCurrentText(str(attr.isNotNull))
            comboNu.setProperty('attribute', attr)

            self.attributetable.setCellWidget(row, 5, comboUq)
            comboUq.setCurrentText(str(attr.isUnique))
            comboUq.setProperty('attribute', attr)

            self.attributetable.setItem(row, 6, QTableWidgetItem(str(attr.data)))

        if(self.chk_relation.isChecked()):
            relationshiplist = []
            for relationship in item.relationships:
                relationshiplist.append(relationship[0].name().lower() + ' REFERENCES '+relationship[1].name() + ' (' + ','.join(relationship[2]) + ')')
            self.relationships.setText('\n'.join(relationshiplist))


    def resetBtnClicked(self):
        self.btn_analyze.setEnabled(False)
        self.btn_generate.setEnabled(False)
        self.btn_preview.setEnabled(False)
        self.btn_execute.setEnabled(False)
        # self.btn_remove.setEnabled(False)
        self.chk_relation.setEnabled(False)
        self.chk_generate.setEnabled(False)
        self.chk_NE.setEnabled(False)
        self.relationships.clear()
        # self.chk_nonpotential.setEnabled(False)

        self.entitylist.clear()
        for i in range(self.attributetable.rowCount()):
            self.attributetable.removeRow(0)
        self.description.clear()


    def closeButtonClicked(self, event):
        pass
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def tableRowClicked(self, row, column):
        print(row, column)


    def comboBoxChangedPk(self, pk):
        attr = self.sender().property('attribute')
        if (attr != None):
            attr.isPrimaryKey = pk


    def comboBoxChangedDt(self, dType):
        attr = self.sender().property('attribute')
        if(attr !=None):
            attr.dtype = DataType[str(dType)]


    def comboBoxChangedNu(self, nu):
        attr = self.sender().property('attribute')
        if (attr != None):
            attr.isNotNull = nu


    def comboBoxChangedUq(self, uq):
        attr = self.sender().property('attribute')
        if (attr != None):
            attr.isUnique = uq


    # def removeButtonClicked(self, event):
    #     pass


    def relationshipIsChecked(self, event):
        if self.chk_relation.isChecked():
            self.lbl_relation.setEnabled(True)
            self.relationships.setEnabled(True)
        else:
            self.lbl_relation.setEnabled(False)
            self.relationships.setEnabled(False)


    def previewButtonClicked(self, event):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("SQL Script")
        msg.setText("SQL Script is Generated!!")
        msg.setDetailedText(self.script)
        msg.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = DBCreatorWindow()
    ui.show()
    sys.exit(app.exec_())

