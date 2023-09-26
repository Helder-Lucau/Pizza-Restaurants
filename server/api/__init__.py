from flask import Flask
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint

from api.models import db

# create the app and configure the SQLite database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzaria.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app) # initialize the app with the extension

# Configure Swagger UI
SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.json"
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Pizza Restaurant REST API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix = SWAGGER_URL)

api = Api(app)

# Import the routes to avoid circular importation 
from api import routes