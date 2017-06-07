import xml.etree.ElementTree

import pymysql

tableMatrix = [['course_id'], ['course_id', 'title', 'department_name']]
database_name = 'university'
db_name = ""


# create database
def table_creator():
    attrib_string = ",".join(str(single) for single in tableMatrix[0])
    asd = 'PRIMARY KEY(' + attrib_string + ')'
    sql = 'CREATE TABLE ' + database_name + '_new (' + (
        ",".join(str(get_datatype(single)[0]) for single in tableMatrix[1])) + ' ,' + asd + ');'
    print(sql)
    exec_query(sql)


# get the relevent datatype from the XML file
def get_datatype(attrib):
    returntype = ''
    attrib_list = attribute_types(database_name + '.xml')
    for singleattrib in attrib_list:
        if singleattrib[0] == attrib.lower():
            returntype = singleattrib[1]
    return returntype


# get attribute datatypes from the XML
def attribute_types(file):
    attribute_type = []
    database = xml.etree.ElementTree.parse('..\output\\' + file).getroot()
    for a in database.iter('attribute'):
        attribute_type.append([a.attrib['attname'], a.find('dataType').text])
        if a.find('maxLength').text.lower() != 'none':
            attribute_type.append([a.attrib['attname'], [
                a.attrib['attname'] + ' ' + a.find('dataType').text + '(' + a.find('maxLength').text + ')']])
        else:
            attribute_type.append([a.attrib['attname'], [a.attrib['attname'] + ' ' + a.find('dataType').text]])
    return attribute_type


# Making a database connection
def dbConn(user, passwd, db):
    connection = pymysql.connect(host='localhost',
                                 user=user,
                                 password=passwd,
                                 db=db,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


# Excute SQL query
def exec_query(query):
    connection = dbConn('root', '', 'crud')
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    finally:
        connection.close()


table_creator()
