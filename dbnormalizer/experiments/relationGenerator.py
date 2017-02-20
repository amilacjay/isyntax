import xml.etree.ElementTree as ET


class Generator:
    def __init__(self, file):
        self.file = file + '.xml'

    def getPrimaryKeys(self):
        # store Primary Keys
        pKeys = []
        # store non key attributes
        nKeys = []
        tree = ET.parse('output/' + self.file)
        database = tree.getroot()

        for tables in database.findall('tables'):
            for table in tables.findall('table'):
                atts = []
                natts = []
                for attributes in table.findall('attributes'):
                    for attribute in attributes.findall('attribute'):
                        for key in attribute.findall('columnKey'):
                            if key.text == 'PRI':
                                atts.append(attribute.attrib)
                            else:
                                natts.append(attribute.attrib)
                pKeys.append([atts, table.attrib])
                nKeys.append([natts, table.attrib])

        return pKeys, nKeys


asd = Generator('company')
asd.getPrimaryKeys()
