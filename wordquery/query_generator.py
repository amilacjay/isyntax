import pymysql.cursors

__author__ = 'ChaminiKD'


def makeConnection(user, passwd, db):
    connection = pymysql.connect(host='localhost',
                                 user=user,
                                 password=passwd,
                                 db=db,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


# create the sql query
def createQuery(attList, tableList, value, symbol, prv_attribute, condition_list, operator):
    if value and len(condition_list) >= 2:
        basciSQL = "SELECT " + ', '.join(attList) + " FROM " + ', '.join(tableList) + " WHERE " + condition_list[
            0][0] + condition_list[0][1] + value[0] + operator[0].upper() + " " + condition_list[1][0] + \
                   condition_list[1][1] + value[1] + ";"
        return basciSQL

    if value and not attList :
        att_for_value = prv_attribute
        basciSQL = "SELECT * FROM " + ', '.join(tableList) + " WHERE " + att_for_value[
            0] + symbol[0][0] + value[0] + ";"
        return basciSQL

    if value and attList:
        att_for_value = prv_attribute
        basciSQL = "SELECT " + ', '.join(attList) + " FROM " + ', '.join(tableList) + " WHERE " + att_for_value[
            0] + symbol[0][0] + value[0] + ";"
        return basciSQL

    if attList:
        basciSQL = "SELECT " + ', '.join(attList) + " FROM " + ', '.join(tableList) + " ;"
        return basciSQL
    if not attList :
        basciSQL = "SELECT * FROM " + ', '.join(tableList) + " ;"
        # print(basciSQL)
        return basciSQL
    else:
        basciSQL = "none"
        return basciSQL


# get the result
def getResult(connection, query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
            result = cursor.fetchall()
            return result
    except:
        print("Invalid")
    finally:
        connection.close()
