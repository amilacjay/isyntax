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