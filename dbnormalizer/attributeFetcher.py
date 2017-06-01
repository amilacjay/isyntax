import pymysql.cursors
from xml.etree.ElementTree import Element, SubElement, ElementTree


class Fetcher:
    def __init__(self, user, password, dbname):
        self.user = user
        self.passwd = password
        self.db = dbname

    # Making a database connection
    def dbConn(self):
        connection = pymysql.connect(host='localhost',
                                     user=self.user,
                                     password=self.passwd,
                                     db=self.db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection

    # Extract Schema of the database
    def getSchema(self, connection):
        try:
            with connection.cursor() as cursor:
                # forming an XML
                root = Element('database')
                root.set('dbname', self.db)
                tree = ElementTree(root)
                tablesElement = Element('tables')
                root.append(tablesElement)

                # Using Cursor to fetch data as SQL queries
                cursor.execute("SHOW TABLES")
                connection.commit()
                tables = cursor.fetchall()
                for table in tables:
                    tablekeyList = sorted(list(table.keys()))
                    tableSubElement = SubElement(tablesElement, "table")
                    tableSubElement.set('tbname', str(table[tablekeyList[0]]))
                    cursor.execute("select table_name, column_name, data_type, character_maximum_length, column_key "
                                   "from INFORMATION_SCHEMA.COLUMNS "
                                   "where table_name = %s;", table[tablekeyList[0]])
                    atts = cursor.fetchall()
                    connection.commit()
                    attsSubElement = SubElement(tableSubElement, "attributes")
                    for att in atts:
                        attKeyList = sorted(list(att.keys()))
                        attSubElement = SubElement(attsSubElement, "attribute")
                        dataTypeSubElement = SubElement(attSubElement, "dataType")
                        lengthSubElement = SubElement(attSubElement, "maxLength")
                        columnKeyElement = SubElement(attSubElement, "columnKey")
                        refTableSubElement = SubElement(attSubElement, "referencedTable")
                        refColumnSubElement = SubElement(attSubElement, "referencedColumn")
                        valuesSubElement = SubElement(attSubElement, "values")
                        attSubElement.set('attname', str(att[attKeyList[2]]))
                        dataTypeSubElement.text = str(att[attKeyList[3]])
                        lengthSubElement.text = str(att[attKeyList[0]])
                        columnKeyElement.text = str(att[attKeyList[1]])
                        cursor.execute("SELECT table_name,column_name,referenced_table_name,referenced_column_name "
                                       "FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE "
                                       "WHERE column_name = '" + str(att[attKeyList[1]]) + "' AND table_name = '" + str(
                            table[tablekeyList[
                                0]]) + "' AND referenced_column_name IS NOT NULL AND constraint_name = '" + self.db + "';")
                        foreigns = cursor.fetchall()
                        connection.commit()

                        cursor.execute("SELECT " + str(att[attKeyList[2]]) + " FROM " + str(table[tablekeyList[0]]))
                        dataSet = cursor.fetchall()
                        connection.commit()

                        i = 1
                        for data in dataSet:
                            dataSubElement = SubElement(valuesSubElement, "data")
                            dataSubElement.set('id', str(i))
                            if data:
                                dataSubElement.text = str(data[str(att[attKeyList[2]])])
                                i += 1

                        for foreign in foreigns:
                            foreignKeyList = sorted(list(foreign.keys()))
                            if foreign:
                                refTableSubElement.text = foreign[foreignKeyList[2]]
                                refColumnSubElement.text = foreign[foreignKeyList[1]]
                return tree
        finally:
            connection.close()

    # Write to an XMl file
    def writeXML(self, tree):
        tree.write("output/" + self.db + ".xml")
        # adding the xml version line to the begging of the xml
        with open("output/" + self.db + ".xml", 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            line = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>"
            f.write(line.rstrip('\r\n') + '\n' + content)


# using existing database

fet = Fetcher("root", "1234", "company")

tre = fet.getSchema(fet.dbConn())
fet.writeXML(tre)
