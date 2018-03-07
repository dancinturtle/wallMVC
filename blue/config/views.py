from flask import render_template
from blue import app
from blue.controllers.products import Products
products = Products()

@app.route("/")
def hello():
    # return "Index"
    products.index()
    return render_template('index.html')

@app.route("/blue")
def blah():
    return "Hello Blue!"