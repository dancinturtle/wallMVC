from blue import app

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/blue")
def blah():
    return "Hello Blue!"