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

# noinspection PyUnresolvedReferences
from gr.routes import index, login, perfil, quadro, conquistas, apontamentos, sobre
# noinspection PyUnresolvedReferences
from gr.routes.api import api_atividades


def get_app():
    return app


# get_app().run()
