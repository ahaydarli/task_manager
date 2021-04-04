from playhouse.flask_utils import FlaskDB
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from celery import Celery
from flask_cors import CORS


db = FlaskDB()
ma = Marshmallow()
jwt = JWTManager()
celery = Celery()
cors = CORS()
