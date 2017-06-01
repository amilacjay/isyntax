from enum import Enum
class Table:
    def __init__(self):
        self.name = None
        self.condition = None
        self.projectionFields = []
        self.sortingFields = []

    def setName(self, name):
        self.name = name

    def setCondition(self, condition):
        self.condition = condition

    def setProjectionFields(self, fields):
        self.projectionFields = fields

    def setSortingFields(self, fields):
        self.sortingFields = fields


class ELEMENT_TYPE(Enum):
    TABLE = 0
    JOINED_TABLE = 1
    CONDITION = 2
    COL_LIST = 3
    VARIABLE = 4