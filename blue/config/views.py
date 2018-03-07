from blue import app
from blue.controllers.products import Products
products = Products()

@app.route("/")
def hello():
    # return "Index"
    products.index()

@app.route("/blue")
def blah():
    return "Hello Blue!"