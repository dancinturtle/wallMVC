from blue import app
from blue.config.mysqlconnection import connectToMySQL
mysql = connectToMySQL(app, "febWallDemo")


class Product:
    def create(self):
        query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW());"
        data = {"first_name": "StanBD", "last_name": "CornB", "email": "stanUBd@gmail.com", "password":"asdfasdf" }
        mysql.query_db(query, data)
        # with engine.connect() as con:
        # 	data = ( { "first_name": "Stanley", "last_name": "Unicorn", "email": "stan@gmail.com", "password":"asdfasdf" }, { "first_name": "Dammit", "last_name": "Doll", "email": "dammit@gmail.com", "password":"asdfasdf" })
        # 	statement = text("INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())")
        # 	for line in data:
        # 		con.execute(statement, **line)

    def retrieveAll(self):
        query = "SELECT * FROM users;"
        data = mysql.query_db(query)
        print("got the data", data)
        return data