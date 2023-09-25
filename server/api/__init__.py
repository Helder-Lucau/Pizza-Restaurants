from flask import Flask
from flask_restful import Api, Resource
from flask_migrate import Migrate

from api.models import db

# create the app and configure the SQLite database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzaria.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

# Import the routes to avoid circular importation 
from api import routes