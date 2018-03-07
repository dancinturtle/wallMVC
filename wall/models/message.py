from wall import app
from wall.config.mysqlconnection import connectToMySQL
mysql = connectToMySQL()

class Message:
    def index(self):
        result = mysql.query_db("SELECT * FROM messages;")
        return result