from enum import Enum

class DataType(Enum):
    VARCHAR = 0
    CHAR = 1
    INTEGER = 2
    DOUBLE = 3
    DATETIME = 4


class Entity:
    def __init__(self, name):
        self.name = name
        self.attributes = []

    def setAttributes(self, attributes):
        self.attributes = attributes

    def getAttributes(self):
        return self.attributes

    def addAttribute(self, attribute):
        self.attributes.append(attribute)


class Attribute:
    def __init__(self, name):
        self.name = name
        self.dtype = DataType.VARCHAR
        self.isPrimaryKey = False
        self.isUnique = False
        self.isNotNull = False



