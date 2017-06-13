from enum import Enum
from PyQt5.QtWidgets import QListWidgetItem


class DataType(Enum):
    def __str__(self):
        return self.name

    VARCHAR = 0
    CHAR = 1
    INTEGER = 2
    DOUBLE = 3
    DATETIME = 4


class Entity(QListWidgetItem):
    def __init__(self, data):
        super().__init__()
        self.data = data
        super().setText(str(self.name()))
        self.attributes = []
        self.relationships=[]

    def setAttributes(self, attributes):
        self.attributes = attributes

    def getAttributes(self):
        return self.attributes

    def addAttribute(self, attribute):
        self.attributes.append(attribute)

    def name(self):
        words = []
        for chunk in self.data:
            words.append(chunk[0])
        return ('_'.join(words)).strip()


class Attribute:
    def __init__(self, data):
        self.data = data
        self.dtype = DataType.VARCHAR
        self.isPrimaryKey = False
        self.isUnique = False
        self.isNotNull = False
        self.isForeignKey = False

    def name(self):
        words = []
        for chunk in self.data:
            words.append(chunk[0])

        return ('_'.join(words)).strip()



