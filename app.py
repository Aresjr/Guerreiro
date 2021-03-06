from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'sqgtjqzAbk'
app.debug = True
app.config.from_object("config.TestingConfig")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)

# noinspection PyUnresolvedReferences
from gr.routes import index, view, login, error_responses
# noinspection PyUnresolvedReferences
from gr.routes.api import api_atividades, api_xp, api_tarefas, api_usuario


def get_app():
    return app


if __name__ == "__main__":
    get_app().run(debug=True)
