# standard libs
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api

# our custom config
from api.config import DevelopmentConfig


app = Flask(__name__, static_url_path='/static')
api = Api(app)

# TODO WARNING disable cors compatibility added * to avoid CORS issues in devel NOT IN PRODUCTION!
CORS(app, intercept_exceptions=False,  resources={r"/*": {"origins": "*"}})

# TODO you can switch you configuration for stagging QA, Production etc...
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
