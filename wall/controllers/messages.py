from wall import app
from flask import render_template, redirect, flash
from wall.models.message import Message
message = Message()

class Messages:
    def index(self):
        print("here's this", message.index())
        return render_template("wall.html")
    # def create(self, newuser):
    #     result = user.create(newuser)
    #     print("The response", result)
    #     if result[0]==False:
    #         for error in result[1]:
    #             flash(error, "register")
    #     else:
    #         flash("You've been successfully registered", "register")
    #         return redirect('/wall')
    #     return redirect("/")