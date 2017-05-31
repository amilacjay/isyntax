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
def createQuery(attList, tableList, value, symbol, prv_attribute):
    if value:
        att_for_value = prv_attribute
        print("attribute for value = ", att_for_value)
        basciSQL = "SELECT " + ', '.join(attList) + " FROM " + ', '.join(tableList) + " WHERE " + att_for_value[
            0] + symbol + value + ";"
        return basciSQL
    if attList:
        basciSQL = "SELECT " + ', '.join(attList) + " FROM " + ', '.join(tableList) + " ;"
        return basciSQL
    else:
        basciSQL = "SELECT * FROM " + ', '.join(tableList) + " ;"
        # print(basciSQL)
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


