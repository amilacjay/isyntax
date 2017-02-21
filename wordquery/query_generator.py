import pymysql.cursors

__author__ = 'ChaminiKD'

def makeConnection(user,passwd,db):
    connection = pymysql.connect(host='localhost',
                                     user=user,
                                     password=passwd,
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    return connection

# attList= ['lname','fname']
# tableList = ['employee']

def createQuery(attList,tableList):
    if (attList):
        basciSQL = "SELECT "+', '.join(attList)+" FROM "+', '.join(tableList)+" ;"
        print(basciSQL)
        return basciSQL
    else:
        basciSQL = "SELECT * FROM "+', '.join(tableList)+" ;"
        print(basciSQL)
        return basciSQL

# sql = createQuery(attList,tableList)
# con = makeConnection('root','','company')

def getResult(connection,query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# asd = getResult(con,sql)
# print(asd)
