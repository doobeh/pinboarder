__author__ = 'Anthony Plunkett'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flaskext.markdown import Markdown

app = Flask(__name__)
app.config.from_object('config')

Markdown(app, extensions=['extra','codehilite',])
db = SQLAlchemy(app)

# Where shall we send a failed login?
login_manager = LoginManager()
login_manager.setup_app(app)
login_manager.login_view = 'login'

from views import *