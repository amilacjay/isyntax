import pymysql
from configparser import ConfigParser

class DbConnection:

    def connectToDb(self, sql):
        config = ConfigParser()
        config.read('../../config.ini')

        hostName = config.get('Global', 'host')
        portNo = config.get('Global', 'port')
        username = config.get('Global', 'username')
        password = config.get('Global', 'password')
        database = config.get('Global', 'database')


        conn = pymysql.connect(host = hostName, port = int(portNo), user = username, passwd = password, db = database)

        cursor = conn.cursor()
        cursor.execute(sql)

        cursor.close()
        conn.close()


        # cursor.execute("CREATE TABLE department (name VARCHAR(20) UNIQUE, number VARCHAR(10) UNIQUE, particular_employee VARCHAR(20), department VARCHAR(10))")
        # # for row in cursor:
        # #     print(row)