from wall import app
from wall.config.mysqlconnection import connectToMySQL
mysql = connectToMySQL()
import re
from flask.ext.bcrypt import Bcrypt
bcrypt = Bcrypt(app)


class User:
    def create(self, data):
        print("models create", data)
        passRegex = re.compile(r'^(?=.{8,15}$)(?=.*[A-Z])(?=.*[0-9]).*$')
        emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        nameRegex = re.compile(r'^(?=.{2,})([a-zA-z]*)$')
        errors = []
        for key, value in data.items():
            if len(value)<1:
                errors.append("All fields must be filled")
                break
        if not emailRegex.match(data['email']):
            errors.append("Invalid email address")
        if not passRegex.match(data['password']):
            errors.append("Password must contain a number, a capital letter, and be between 8-15 characters")
        if not nameRegex.match(data['first_name']) or not nameRegex.match(data['last_name']):
            errors.append("Names must contain at least two letters and contain only letters")
        if data['password'] != data['confirm']:
            errors.append("Passwords must match")
        if len(errors)>0:
            print("errors > 0")
            return (False, errors)
        else:
            print("errors = 0")
            unique = mysql.query_db("SELECT * FROM users WHERE email = %s;", data['email'])
            if len(unique) > 0:
                errors.append("This email has already been taken")
                return (False, errors)
            else:
                pw_hash = bcrypt.generate_password_hash(data['password'])
                query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw_hash)s, NOW());"
                newuser = {"first_name" : data["first_name"],
                            "last_name" : data["last_name"],
                            "email" : data["email"],
                            "pw_hash" : pw_hash}
                created = mysql.query_db(query, newuser)
                if created:
                    return (True, created)
                else:
                    errors.append("We're sorry, you could not be registered at this moment")
                    return (False, errors)


    def retrieveAll(self):
       
        mysql.query_db("SELECT * FROM users;")
    
    def retrieveOneById(self, id):
        mysql.query_db("SELECT * FROM users WHERE id=%s;", id)
    
    def update(self, data):
        query = "UPDATE users SET first_name = %(first)s, last_name = %(last)s WHERE id=%(id)s;"
        mysql.query_db(query, data)