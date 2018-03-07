from blue.models.product import Product
from flask import render_template
product = Product()

class Products:
    def index(self):
        product.retrieveAll()
        product.retrieveOneById(1)
        product.update({"id": 5, "first":"Bugs", "last":"Bunny"})
        
        return render_template("index.html")
