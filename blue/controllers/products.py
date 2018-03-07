from blue.models.product import Product
from flask import render_template
product = Product()

class Products:
    def index(self):
        product.retrieveAll()
        return render_template("index.html")
