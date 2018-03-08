from flask import request
from wall import app
from wall.controllers.users import Users
from wall.controllers.messages import Messages
users = Users()
messages = Messages()

@app.route("/")
def index():
    return users.index()

@app.route("/createUser", methods=['POST'])
def createUser():
    return users.create(request.form)

@app.route('/login', methods=['POST'])
def login():
    return users.login(request.form)

@app.route('/wall')
def wall():
    return messages.index()

@app.route('/create_message', methods=['POST'])
def writeMessage():
    return messages.create(request.form)

@app.route('/create_comment', methods=['POST'])
def writeComment():
    return messages.comment(request.form)
    
@app.route("/logout")
def logout():
    return users.logout()