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
        with self.connection.cursor() as cursor:
            try:
                executable = cursor.execute(query, data)
                # use matching to find if find()
                # if query[0:6].lower() == 'select':
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                # elif query[0:6].lower() == 'insert':
                else:
                    self.connection.commit()
            except:
                print("Something went wrong")
                return False

def connectToMySQL():
    return MySQLConnection()
