from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'sqgtjqzAbk'
app.debug = True
app.config.from_object("config.DevelopmentConfig")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)

from routes import index, perfil, api, login, atividades, quadro


def get_app():
    return app
