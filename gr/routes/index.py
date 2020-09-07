from flask import render_template
from flask_login import current_user

from app import app


@app.route('/')
def index():
    usuario = current_user
    return render_template('pages/index.html', titulo="Início", usuario=usuario)
