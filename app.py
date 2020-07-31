import logging

from flask import Flask
from flask_login import LoginManager
from logging import Formatter, FileHandler

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'sqgtjqzAbk'

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pgroot@localhost/guerreiro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TESTING'] = True
app.config['FLASK_ENV'] = 'development'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)

from routes import routes_import

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


def get_app():
    return app
