from flask import request
from wall import app
from wall.controllers.users import Users
from wall.controllers.messages import Messages
users = Users()
messages = Messages()

@app.route("/")
def index():
    # return "Index"
    return users.index()

@app.route("/createUser", methods=['POST'])
def createUser():
    return users.create(request.form)

@app.route('/wall')
def wall():
    return messages.index()
@app.route("/blue")
def blah():
    return "Hello Blue!"