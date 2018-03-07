import pymysql.cursors

class MySQLConnection:
    def __init__(self):
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='rootroot',
                                    db='wall',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.connection = connection
    def query_db(self, query, data=None):
        print("The query", query)
        with self.connection.cursor() as cursor:
            try:
                executable = cursor.execute(query, data)
                if query[0:6].lower() == 'select':
                    result = cursor.fetchall()
                    return result
                elif query[0:6].lower() == 'insert':
                    self.connection.commit()
                    return cursor.lastrowid
                else:
                    self.connection.commit()
            except:
                print("Something went wrong")

def connectToMySQL():
    return MySQLConnection()
