from wall import app
from flask import render_template, redirect, flash, session
from wall.models.message import Message
message = Message()

class Messages:
    def index(self):
        if 'userid' not in session:
            flash("You must be logged in to view the wall", "register")
            return redirect('/')
        allnotes = message.index()
        return render_template("wall.html", messages = allnotes[0], comments = allnotes[1])

    def create(self, newmessage):
        if 'userid' not in session:
            flash("You must be logged in to create messages", "register")
            return redirect('/')
        else:
            result = message.create(newmessage, session['userid'])
            if result[0]==False:
                if result[1]=="length":
                    flash("Messages must be at least 4 characters long", "error")
                else:
                    flash("We could not create your message at this time", "error")
            return redirect('/wall')

    def comment(self, newcomment):
        if 'userid' not in session:
            flash("You must be logged in to comment on posts", "register")
            return redirect('/')
        else:
            result = message.comment(newcomment, session['userid'])
            if result[0]==False:
                if result[1]=="length":
                    flash("Comments must be at least 4 characters long", "error")
                else:
                    flash("We could not create your comment at this time", "error")
            return redirect('/wall')