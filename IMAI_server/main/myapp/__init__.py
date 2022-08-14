from flask import Flask

from .api.routes import api
from .site.routes import site
from .db.routes import db

app = Flask(__name__)

app.register_blueprint(api)
app.register_blueprint(site)
app.register_blueprint(db)