from flask import Flask, render_template, redirect, flash, session, request
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import requests
import re
app = Flask(__name__)
app.secret_key = "rainbowswithapotofgold"
bcrypt = Bcrypt(app)
mysql = connectToMySQL('register')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/createUser", methods=['POST'])
def create():
    data = request.form
    passRegex = re.compile(r'^(?=.{8,15}$)(?=.*[A-Z])(?=.*[0-9]).*$')
    emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    nameRegex = re.compile(r'^(?=.{2,})([a-zA-z]*)$')
    errors = False
    for key, value in data.items():
        if len(value)<1:
            flash("This field is required", key)
            errors = True
            # break
    if data['email'] and not emailRegex.match(data['email']):
        flash("Invalid email address", "email")
        errors = True
    if data['password'] and not passRegex.match(data['password']):
        flash("Password must contain a number, a capital letter, and be between 8-15 characters", "password")
        errors = True
    if data['first_name'] and not nameRegex.match(data['first_name']): 
        flash("First name must contain at least two letters and contain only letters", "first_name")
        errors = True
    if data['last_name'] and not nameRegex.match(data['last_name']):
        flash("Last name must contain at least two letters and contain only letters", "last_name")
        errors = True
    if data['confirm'] and data['password'] != data['confirm']:
        flash("Passwords must match", "confirm")
        errors = True
    if not errors:
        unique = mysql.query_db("SELECT * FROM users WHERE email = %s;", data['email'])
        if unique:
            flash("This email has already been taken", "email")
        else:
            pw_hash = bcrypt.generate_password_hash(data['password'])
            query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw_hash)s, NOW());"
            newuser = {"first_name" : data["first_name"],
                        "last_name" : data["last_name"],
                        "email" : data["email"],
                        "pw_hash" : pw_hash}
            created = mysql.query_db(query, newuser)
            if created:
                flash("You've been successfully registered", "success")
                session['username']=newuser['first_name']
                session['userid'] = created
                return redirect('/success')
            else:
                flash("We're sorry, you could not be registered at this moment", "register")
    flash(request.form['first_name'], "badfirst")
    flash(request.form['last_name'], "badlast")
    flash(request.form['email'], "bademail")
    return redirect("/")

@app.route('/login', methods=['POST'])
def login():
    # query = "SELECT * FROM users WHERE email = '{}'".format(request.form['email'])
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {"email" : request.form['email']}
    result = mysql.query_db(query, data)
    # result = mysql.query_db(query)
    print("got this result", result)
    if result:
        if bcrypt.check_password_hash(result[0]['pw_hash'], request.form['password']):
            session['username'] = result[0]['first_name']
            session['userid'] = result[0]['id']
            return redirect('/success')
    flash("You could not be logged in", "login")
    return redirect('/')
    
@app.route('/success')
def wall():
    if 'userid' not in session:
        flash("You must be logged in to enter this website", "register")
        return redirect('/')
    return render_template("wall.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out", "register")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)