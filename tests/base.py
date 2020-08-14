from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import test_config

from flask_testing import TestCase
from ..resource import auth_blueprint

db = SQLAlchemy()

class BaseTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config.update(**test_config)
        app.register_blueprint(auth_blueprint)
        db.init_app(app)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
