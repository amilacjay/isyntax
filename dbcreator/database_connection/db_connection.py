import pymysql

class DbConnection:

    def connectToDb(self, sql):

        conn = pymysql.connect(host = "localhost", port = 3306, user = "root", passwd = "1234", db = "school")

        cursor = conn.cursor()
        cursor.execute(sql)

        cursor.close()
        conn.close()


        # cursor.execute("CREATE TABLE department (name VARCHAR(20) UNIQUE, number VARCHAR(10) UNIQUE, particular_employee VARCHAR(20), department VARCHAR(10))")
        # # for row in cursor:
        # #     print(row)