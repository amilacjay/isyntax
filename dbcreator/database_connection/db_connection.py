import pymysql
from configparser import ConfigParser

class DbConnection:

    def connectToDb(self, sql, config_path='config.ini'):
        config = ConfigParser()
        config.read(config_path)

        hostName = config.get('DBCreator', 'host')
        portNo = config.get('DBCreator', 'port')
        username = config.get('DBCreator', 'username')
        password = config.get('DBCreator', 'password')
        database = config.get('DBCreator', 'database')


        conn = pymysql.connect(host = hostName, port = int(portNo), user = username, passwd = password, db = database)

        cursor = conn.cursor()
        cursor.execute(sql)

        cursor.close()
        conn.close()


        # cursor.execute("CREATE TABLE department (name VARCHAR(20) UNIQUE, number VARCHAR(10) UNIQUE, particular_employee VARCHAR(20), department VARCHAR(10))")
        # # for row in cursor:
        # #     print(row)