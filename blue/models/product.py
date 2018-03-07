from blue import app
from blue.config.mysqlconnection import connectToMySQL
mysql = connectToMySQL()


class Product:
    def create(self, data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(first)s, %(last)s);"
        mysql.query_db(query, data)

    def retrieveAll(self):
       
        mysql.query_db("SELECT * FROM users;")
    
    def retrieveOneById(self, id):
        mysql.query_db("SELECT * FROM users WHERE id=%s;", id)
    
    def update(self, data):
        query = "UPDATE users SET first_name = %(first)s, last_name = %(last)s WHERE id=%(id)s;"
        mysql.query_db(query, data)