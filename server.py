from wall import app
from flask import session
app.secret_key = "rainbowswithapotofgold"
from wall.config import routes
app.run(debug=True)